"""Team MAD 연구 세션: 라운드 진행과 마스터 보고."""

from __future__ import annotations

import logging
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

from .agents import Orchestrator, Researcher
from .llm import Backend
from .prompts import DEFAULT_SPECIALTIES, MASTER
from .rooms import CentralLibrary, PersonalRoom

log = logging.getLogger("mad")

RESEARCHERS = list(DEFAULT_SPECIALTIES)


class TeamMAD:
    def __init__(self, problem: str, backend: Backend, workspace: Path,
                 max_rounds: int = 3, parallel: bool = True, pdf_maker=None):
        self.problem = problem
        self.max_rounds = max_rounds
        self.parallel = parallel
        self.root = workspace / datetime.now().strftime("session-%Y%m%d-%H%M%S")
        self.root.mkdir(parents=True, exist_ok=True)
        (self.root / "problem.md").write_text(f"# 연구 과제\n\n{problem}\n", encoding="utf-8")

        self.library = (CentralLibrary(self.root, RESEARCHERS, "orchestrator", pdf_maker)
                        if pdf_maker else CentralLibrary(self.root, RESEARCHERS, "orchestrator"))
        self.researchers = {
            name: Researcher(name, spec, PersonalRoom(name, self.root), self.library, backend)
            for name, spec in DEFAULT_SPECIALTIES.items()
        }
        self.orchestrator = Orchestrator(self.library, RESEARCHERS, backend)

    def _round_prompt(self, round_no: int) -> str:
        head = (f"[라운드 {round_no}/{self.max_rounds}] {MASTER}의 연구 과제:\n{self.problem}\n\n"
                if round_no == 1 else f"[라운드 {round_no}/{self.max_rounds}] 이전 라운드 보고서가 도착했습니다.\n\n")
        tail = ("이번이 마지막 라운드입니다. 임무를 더 줄 수도 있지만, 이번 라운드 이후에는 반드시 최종 보고해야 합니다."
                if round_no == self.max_rounds else
                "도서관을 검토하고 연구원들에게 임무를 배정하거나, 충분하면 마스터에게 최종 보고하세요.")
        return f"{head}[중앙 도서관 목록]\n{self.library.catalog('orchestrator')}\n\n{tail}"

    def run(self) -> Path:
        for round_no in range(1, self.max_rounds + 1):
            self.orchestrator.missions.clear()
            log.info("=== 라운드 %d: 오케스트레이터 검토 ===", round_no)
            self.orchestrator.run_turn(self._round_prompt(round_no))
            if self.orchestrator.final_report:
                break
            if not self.orchestrator.missions:
                self.orchestrator.run_turn("임무가 배정되지 않았습니다. assign_mission 또는 report_to_master 중 하나를 호출하세요.")
                if self.orchestrator.final_report:
                    break
                if not self.orchestrator.missions:
                    break

            missions = dict(self.orchestrator.missions)
            log.info("라운드 %d 임무 배정: %s", round_no, ", ".join(missions))
            if self.parallel:
                with ThreadPoolExecutor(max_workers=len(missions)) as pool:
                    for f in [pool.submit(self.researchers[r].work, round_no, m) for r, m in missions.items()]:
                        f.result()
            else:
                for r, m in missions.items():
                    self.researchers[r].work(round_no, m)

        if not self.orchestrator.final_report:
            self.orchestrator.run_turn(
                f"연구 라운드가 모두 끝났습니다. 도서관을 종합하여 지금 report_to_master로 {MASTER}에게 최종 보고하세요.\n\n"
                f"[중앙 도서관 목록]\n{self.library.catalog('orchestrator')}")
        return self._write_final()

    def _write_final(self) -> Path:
        out = self.root / "master" / "final_report.md"
        out.parent.mkdir(exist_ok=True)
        if self.orchestrator.final_report:
            title, body = self.orchestrator.final_report
        else:
            title = "최종 보고 누락 – 도서관 요약본"
            body = self.library.catalog("orchestrator")
        out.write_text(f"# {title}\n\n받는 사람: {MASTER}\n보낸 사람: 오케스트레이터\n\n{body}\n", encoding="utf-8")
        log.info("최종 보고서: %s", out)
        return out
