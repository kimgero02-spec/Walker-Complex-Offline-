"""LLM 백엔드.

- AnthropicBackend: Claude API(Messages API)를 호출한다.
- DryRunBackend: API 키 없이 시스템 흐름(방·권한·보고 규칙)을 시험하기 위한 가짜 백엔드.
"""

from __future__ import annotations

import itertools
import json
from types import SimpleNamespace
from typing import Any, Protocol

DEFAULT_MODEL = "claude-opus-5-5"


class Backend(Protocol):
    def create(self, *, agent: str, system: str, messages: list, tools: list[dict]) -> Any: ...


class AnthropicBackend:
    def __init__(self, model: str = DEFAULT_MODEL, effort: str = "high",
                 code_execution: bool = True, max_tokens: int = 16000):
        import anthropic

        self.client = anthropic.Anthropic()
        self.model = model
        self.effort = effort
        self.code_execution = code_execution
        self.max_tokens = max_tokens

    def create(self, *, agent: str, system: str, messages: list, tools: list[dict]) -> Any:
        all_tools = list(tools)
        # 연구원은 예제 계산을 위해 서버 측 코드 실행 도구를 쓸 수 있다.
        if self.code_execution and agent.startswith("researcher"):
            all_tools.append({"type": "code_execution_20260521", "name": "code_execution"})
        return self.client.beta.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=system,
            messages=messages,
            tools=all_tools,
            thinking={"type": "adaptive"},
            output_config={"effort": self.effort},
            # 안전 분류기가 요청을 거절하면 서버가 권장 모델로 자동 재시도한다.
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
        )


def _text(text: str) -> SimpleNamespace:
    return SimpleNamespace(type="text", text=text)


class DryRunBackend:
    """정해진 각본대로 도구를 호출하는 가짜 모델. 실제 수학 연구는 하지 않는다."""

    def __init__(self) -> None:
        self._ids = itertools.count(1)

    def _tool(self, name: str, **inp: Any) -> SimpleNamespace:
        return SimpleNamespace(type="tool_use", id=f"toolu_dry_{next(self._ids)}", name=name, input=inp)

    @staticmethod
    def _resp(blocks: list, stop: str) -> SimpleNamespace:
        return SimpleNamespace(content=blocks, stop_reason=stop)

    def create(self, *, agent: str, system: str, messages: list, tools: list[dict]) -> Any:
        last = messages[-1]["content"]
        if not isinstance(last, str):  # 도구 결과를 받은 직후 → 턴 종료
            return self._resp([_text("이번 턴 작업을 마쳤습니다.")], "end_turn")

        if agent == "orchestrator":
            rounds = sum(1 for m in messages if m["role"] == "user" and isinstance(m["content"], str))
            if rounds == 1:
                blocks = [
                    self._tool("assign_mission", researcher=r, mission=f"[DRY-RUN] {r} 기본 전문 분야에 따라 과제를 조사하라.")
                    for r in ("researcher1", "researcher2", "researcher3")
                ]
                return self._resp([_text("1라운드 임무를 배정합니다."), *blocks], "tool_use")
            return self._resp([
                self._tool("report_to_master", title="[DRY-RUN] 최종 보고",
                           report="DRY-RUN 모드: 도서관 보고서를 종합했다고 가정한 최종 보고서입니다.\n\n"
                                  + last.split("[중앙 도서관 목록]")[-1].strip()),
            ], "tool_use")

        mission = last.splitlines()[1] if "\n" in last else last
        return self._resp([
            self._tool("write_note", title="작업 노트", content=f"임무 확인: {mission}"),
            self._tool("submit_report", title=f"{agent} 보고서",
                       summary=f"{agent}이(가) DRY-RUN 임무를 수행했습니다.",
                       body=json.dumps({"mission": mission}, ensure_ascii=False)),
        ], "tool_use")
