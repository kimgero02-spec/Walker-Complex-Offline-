"""방(Room) 시스템: 개인 연구실(PersonalRoom)과 중앙 도서관(CentralLibrary).

규칙
- 개인 연구실: 주인 연구원만 읽고 쓸 수 있다.
- 중앙 도서관: 모든 연구원과 오케스트레이터가 읽을 수 있다.
  보고서는 연구원만 제출할 수 있으며, 제출된 보고서는 수정할 수 없다(append-only).
"""

from __future__ import annotations

import json
import threading
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path


class AccessDenied(PermissionError):
    """방 접근 규칙 위반."""


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class PersonalRoom:
    """연구원 한 명의 개인 연구실. 연구 노트를 보관한다."""

    def __init__(self, owner: str, root: Path):
        self.owner = owner
        self.dir = root / "rooms" / owner
        self.dir.mkdir(parents=True, exist_ok=True)
        self.notes_path = self.dir / "notes.md"

    def _check(self, who: str) -> None:
        if who != self.owner:
            raise AccessDenied(f"{who}은(는) {self.owner}의 개인 연구실에 들어갈 수 없습니다.")

    def write_note(self, who: str, title: str, content: str) -> str:
        self._check(who)
        with self.notes_path.open("a", encoding="utf-8") as f:
            f.write(f"\n## {title}  ({_now()})\n\n{content.strip()}\n")
        return f"노트 '{title}'을(를) 개인 연구실에 저장했습니다."

    def read_notes(self, who: str) -> str:
        self._check(who)
        if not self.notes_path.exists():
            return "(아직 노트가 없습니다.)"
        return self.notes_path.read_text(encoding="utf-8")


@dataclass
class Report:
    report_id: str
    author: str
    round: int
    mission: str
    title: str
    summary: str
    body: str
    status: str  # "제출" | "강제 제출"
    created_at: str = field(default_factory=_now)

    def to_markdown(self) -> str:
        return (
            f"# [{self.report_id}] {self.title}\n\n"
            f"- 작성자: {self.author}\n- 라운드: {self.round}\n- 상태: {self.status}\n"
            f"- 임무: {self.mission}\n- 작성 시각: {self.created_at}\n\n"
            f"## 요약\n\n{self.summary.strip()}\n\n## 본문\n\n{self.body.strip()}\n"
        )


class CentralLibrary:
    """모든 연구원이 보고서를 제출하고 열람하는 공용 공간."""

    def __init__(self, root: Path, researchers: list[str], orchestrator: str):
        self.dir = root / "library"
        self.dir.mkdir(parents=True, exist_ok=True)
        self.researchers = set(researchers)
        self.readers = self.researchers | {orchestrator}
        self._reports: dict[str, Report] = {}
        self._lock = threading.Lock()

    def _check_reader(self, who: str) -> None:
        if who not in self.readers:
            raise AccessDenied(f"{who}은(는) 중앙 도서관 출입 권한이 없습니다.")

    def submit(self, who: str, round_no: int, mission: str, title: str,
               summary: str, body: str, status: str = "제출") -> Report:
        if who not in self.researchers:
            raise AccessDenied(f"{who}은(는) 보고서를 제출할 수 없습니다(연구원 전용).")
        with self._lock:
            rid = f"R{round_no:02d}-{who}-{sum(r.author == who for r in self._reports.values()) + 1}"
            report = Report(rid, who, round_no, mission, title, summary, body, status)
            self._reports[rid] = report
            (self.dir / f"{rid}.md").write_text(report.to_markdown(), encoding="utf-8")
            (self.dir / "index.json").write_text(
                json.dumps([asdict(r) for r in self._reports.values()], ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
        return report

    def has_report(self, author: str, round_no: int) -> bool:
        with self._lock:
            return any(r.author == author and r.round == round_no for r in self._reports.values())

    def catalog(self, who: str) -> str:
        self._check_reader(who)
        with self._lock:
            reports = list(self._reports.values())
        if not reports:
            return "(중앙 도서관이 비어 있습니다.)"
        return "\n".join(
            f"- {r.report_id} | {r.author} | 라운드 {r.round} | {r.title}\n  요약: {r.summary.strip()}"
            for r in reports
        )

    def read(self, who: str, report_id: str) -> str:
        self._check_reader(who)
        with self._lock:
            report = self._reports.get(report_id)
        if report is None:
            return f"보고서 {report_id}을(를) 찾을 수 없습니다."
        return report.to_markdown()

    def reports(self) -> list[Report]:
        with self._lock:
            return list(self._reports.values())
