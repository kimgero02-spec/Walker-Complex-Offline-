"""오케스트레이터와 연구원 에이전트."""

from __future__ import annotations

import logging
from typing import Any, Callable

from .llm import Backend
from .prompts import MASTER, ORCHESTRATOR_SYSTEM, researcher_system
from .rooms import AccessDenied, CentralLibrary, PersonalRoom

log = logging.getLogger("mad")


def _tool(name: str, description: str, props: dict[str, str]) -> dict:
    return {
        "name": name,
        "description": description,
        "strict": True,
        "input_schema": {
            "type": "object",
            "properties": {k: {"type": "string", "description": v} for k, v in props.items()},
            "required": list(props),
            "additionalProperties": False,
        },
    }


LIBRARY_TOOLS = [
    _tool("list_library", "중앙 도서관의 보고서 목록과 요약을 본다.", {}),
    _tool("read_report", "중앙 도서관 보고서 전문을 읽는다.", {"report_id": "보고서 ID (예: R01-researcher1-1)"}),
]


class Agent:
    """도구를 쓰는 대화형 에이전트. 대화 기록은 라운드를 넘어 유지된다."""

    max_steps = 40

    def __init__(self, name: str, system: str, tools: list[dict],
                 handlers: dict[str, Callable[..., str]], backend: Backend):
        self.name = name
        self.system = system
        self.tools = tools
        self.handlers = handlers
        self.backend = backend
        self.messages: list[dict[str, Any]] = []

    def run_turn(self, user_text: str) -> str:
        self.messages.append({"role": "user", "content": user_text})
        final_text = ""
        for _ in range(self.max_steps):
            resp = self.backend.create(agent=self.name, system=self.system,
                                       messages=self.messages, tools=self.tools)
            # 응답 블록(사고 블록 포함)을 수정 없이 그대로 기록에 남긴다.
            self.messages.append({"role": "assistant", "content": resp.content})
            texts = [b.text for b in resp.content if b.type == "text"]
            if texts:
                final_text = "\n".join(texts)

            if resp.stop_reason == "refusal":
                log.warning("%s: 모델이 요청을 거절했습니다.", self.name)
                break
            if resp.stop_reason == "pause_turn":  # 서버 도구(코드 실행)가 이어서 진행
                continue
            calls = [b for b in resp.content if b.type == "tool_use"]
            if calls:
                # 병렬 호출 결과는 하나의 user 메시지로 모아서 돌려준다.
                self.messages.append({"role": "user", "content": [self._execute(b) for b in calls]})
            elif resp.stop_reason == "max_tokens":
                self.messages.append({"role": "user", "content": "출력이 잘렸습니다. 이어서 진행하세요."})
            else:
                break
        return final_text

    def _execute(self, block: Any) -> dict:
        handler = self.handlers.get(block.name)
        try:
            if handler is None:
                raise AccessDenied(f"{self.name}은(는) '{block.name}' 도구를 사용할 권한이 없습니다.")
            output = handler(**block.input)
            is_error = False
        except (AccessDenied, TypeError, ValueError) as e:
            output, is_error = f"오류: {e}", True
        log.info("%s → %s%s", self.name, block.name, " (오류)" if is_error else "")
        return {"type": "tool_result", "tool_use_id": block.id, "content": output, "is_error": is_error}


class Researcher(Agent):
    def __init__(self, name: str, specialty: str, room: PersonalRoom,
                 library: CentralLibrary, backend: Backend):
        self.room = room
        self.library = library
        self.round = 0
        self.mission = ""
        tools = [
            _tool("write_note", "개인 연구실에 작업 노트를 저장한다(본인만 열람 가능).",
                  {"title": "노트 제목", "content": "노트 내용"}),
            _tool("read_my_notes", "개인 연구실의 내 노트를 모두 읽는다.", {}),
            *LIBRARY_TOOLS,
            _tool("submit_report", "이번 턴의 요약 보고서를 중앙 도서관에 제출한다. 매 턴 필수.",
                  {"title": "보고서 제목", "summary": "3~6줄 핵심 요약", "body": "계산·근거·남은 질문을 담은 본문"}),
        ]
        handlers = {
            "write_note": lambda title, content: room.write_note(name, title, content),
            "read_my_notes": lambda: room.read_notes(name),
            "list_library": lambda: library.catalog(name),
            "read_report": lambda report_id: library.read(name, report_id),
            "submit_report": self._submit,
        }
        super().__init__(name, researcher_system(name, specialty), tools, handlers, backend)

    def _submit(self, title: str, summary: str, body: str) -> str:
        r = self.library.submit(self.name, self.round, self.mission, title, summary, body)
        return f"보고서 {r.report_id}이(가) 중앙 도서관에 등록되었습니다."

    def work(self, round_no: int, mission: str) -> None:
        self.round, self.mission = round_no, mission
        self.run_turn(f"[라운드 {round_no}] 오케스트레이터의 임무:\n{mission}")
        if not self.library.has_report(self.name, round_no):
            last = self.run_turn("이번 턴의 보고서가 아직 중앙 도서관에 없습니다. 지금 submit_report로 제출하세요.")
            if not self.library.has_report(self.name, round_no):
                # 규칙: 매 턴 보고서 필수 → 시스템이 마지막 응답으로 강제 제출한다.
                self.library.submit(self.name, round_no, mission, f"{self.name} 강제 제출 보고서",
                                    "연구원이 보고서를 제출하지 않아 시스템이 마지막 응답을 기록했습니다.",
                                    last or "(응답 없음)", status="강제 제출")


class Orchestrator(Agent):
    def __init__(self, library: CentralLibrary, researchers: list[str], backend: Backend):
        self.library = library
        self.researchers = researchers
        self.missions: dict[str, str] = {}
        self.final_report: tuple[str, str] | None = None
        tools = [
            *LIBRARY_TOOLS,
            _tool("assign_mission", "연구원에게 이번 라운드 임무를 지시한다.",
                  {"researcher": "researcher1 | researcher2 | researcher3", "mission": "구체적인 임무 지시"}),
            _tool("report_to_master", f"{MASTER}에게 최종 보고서를 올린다. 오케스트레이터만 가능.",
                  {"title": "보고서 제목", "report": "최종 보고서 전문(마크다운)"}),
        ]
        handlers = {
            "list_library": lambda: library.catalog("orchestrator"),
            "read_report": lambda report_id: library.read("orchestrator", report_id),
            "assign_mission": self._assign,
            "report_to_master": self._report,
        }
        super().__init__("orchestrator", ORCHESTRATOR_SYSTEM, tools, handlers, backend)

    def _assign(self, researcher: str, mission: str) -> str:
        if researcher not in self.researchers:
            raise ValueError(f"알 수 없는 연구원: {researcher} (가능: {', '.join(self.researchers)})")
        self.missions[researcher] = mission
        return f"{researcher}에게 임무를 배정했습니다."

    def _report(self, title: str, report: str) -> str:
        self.final_report = (title, report)
        return f"{MASTER}에게 최종 보고를 전달했습니다."
