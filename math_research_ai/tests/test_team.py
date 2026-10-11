from types import SimpleNamespace

import pytest

import shutil

from mad.agents import Researcher
from mad.llm import DryRunBackend
from mad.rooms import AccessDenied, CentralLibrary, PersonalRoom
from mad.team import TeamMAD


def fake_pdf(md, pdf):
    pdf.write_bytes(b"%PDF-fake" + b"0" * 2000)
    return pdf


def test_personal_room_is_private(tmp_path):
    room = PersonalRoom("researcher1", tmp_path)
    room.write_note("researcher1", "t", "x")
    assert "x" in room.read_notes("researcher1")
    with pytest.raises(AccessDenied):
        room.read_notes("researcher2")


def test_only_researchers_submit_and_everyone_reads(tmp_path):
    lib = CentralLibrary(tmp_path, ["researcher1"], "orchestrator", fake_pdf)
    with pytest.raises(AccessDenied):
        lib.submit("orchestrator", 1, "m", "t", "s", "b")
    r = lib.submit("researcher1", 1, "m", "제목", "요약", "본문")
    assert "요약" in lib.catalog("orchestrator")
    assert "본문" in lib.read("researcher1", r.report_id)
    with pytest.raises(AccessDenied):
        lib.catalog("outsider")


def test_dry_run_full_session(tmp_path):
    team = TeamMAD("테스트 과제", DryRunBackend(), tmp_path, max_rounds=2, pdf_maker=fake_pdf)
    final = team.run()
    assert final.exists() and "대수검존" in final.read_text(encoding="utf-8")
    authors = {r.author for r in team.library.reports()}
    assert authors == {"researcher1", "researcher2", "researcher3"}


class SilentBackend:
    """보고서를 끝까지 제출하지 않는 연구원."""

    def create(self, **_):
        return SimpleNamespace(content=[SimpleNamespace(type="text", text="생각만 했습니다.")], stop_reason="end_turn")


def test_report_is_forced_when_researcher_skips_it(tmp_path):
    lib = CentralLibrary(tmp_path, ["researcher1"], "orchestrator", fake_pdf)
    r = Researcher("researcher1", "spec", PersonalRoom("researcher1", tmp_path), lib, SilentBackend())
    r.work(1, "임무")
    [report] = lib.reports()
    assert report.status == "강제 제출" and "생각만" in report.body


class ForbiddenToolBackend:
    """연구원이 마스터 보고 도구를 호출하려 시도."""

    def __init__(self):
        self.calls = 0

    def create(self, **_):
        self.calls += 1
        if self.calls == 1:
            call = SimpleNamespace(type="tool_use", id="t1", name="report_to_master", input={"title": "x", "report": "y"})
            return SimpleNamespace(content=[call], stop_reason="tool_use")
        return SimpleNamespace(content=[SimpleNamespace(type="text", text="끝")], stop_reason="end_turn")


def test_researcher_cannot_report_to_master(tmp_path):
    lib = CentralLibrary(tmp_path, ["researcher1"], "orchestrator", fake_pdf)
    r = Researcher("researcher1", "spec", PersonalRoom("researcher1", tmp_path), lib, ForbiddenToolBackend())
    r.run_turn("임무")
    result = r.messages[2]["content"][0]
    assert result["is_error"] and "권한" in result["content"]


def test_submit_fails_and_rolls_back_without_pdf(tmp_path):
    def broken(md, pdf):
        raise RuntimeError("pandoc 없음")

    lib = CentralLibrary(tmp_path, ["researcher1"], "orchestrator", broken)
    with pytest.raises(ValueError, match="PDF"):
        lib.submit("researcher1", 1, "m", "t", "s", "b")
    assert not lib.has_report("researcher1", 1)
    assert not list((tmp_path / "library").glob("*.md"))


def test_pdf_saved_next_to_markdown(tmp_path):
    lib = CentralLibrary(tmp_path, ["researcher1"], "orchestrator", fake_pdf)
    r = lib.submit("researcher1", 1, "m", "t", "s", "b")
    assert (tmp_path / "library" / f"{r.report_id}.pdf").exists()


@pytest.mark.skipif(not shutil.which("pandoc"), reason="pandoc 필요")
def test_real_pdf_with_korean_and_math(tmp_path):
    lib = CentralLibrary(tmp_path, ["researcher1"], "orchestrator")
    r = lib.submit("researcher1", 1, "임무", "토러스", "$H_1(T^2)=\\mathbb Z^2$", "한글 본문과 수식 $x^2+y^2=p$")
    pdf = tmp_path / "library" / f"{r.report_id}.pdf"
    assert pdf.read_bytes().startswith(b"%PDF")
