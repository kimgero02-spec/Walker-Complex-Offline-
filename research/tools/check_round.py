#!/usr/bin/env python3
"""라운드 점검: 모든 연구원이 보고서(.md)와 PDF(.pdf)를 도서관에 제출했는지 확인한다.

사용법: python3 research/tools/check_round.py <주제 폴더> <라운드 번호> [--fix]
  예) python3 research/tools/check_round.py research/torus-homology 1

- .md 가 없으면 실패(연구원이 직접 써야 함).
- .md 만 있고 PDF 가 없으면 실패. --fix 를 주면 PDF 를 대신 만들고 '시스템 생성'이라고 알린다.
- 하나라도 빠지면 종료 코드 1. 오케스트레이터는 통과하기 전에는 라운드를 끝낼 수 없다.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "math_research_ai"))
from mad.pdf import make_pdf  # noqa: E402

RESEARCHERS = ("researcher1", "researcher2", "researcher3")

args = [a for a in sys.argv[1:] if not a.startswith("--")]
fix = "--fix" in sys.argv
if len(args) != 2:
    raise SystemExit(__doc__)
lib = Path(args[0]) / "library"
rnd = int(args[1])
bad = 0
for r in RESEARCHERS:
    md = lib / f"R{rnd:02d}-{r}.md"
    pdf = md.with_suffix(".pdf")
    if not md.exists():
        print(f"[누락] {r}: 보고서 {md.name} 없음"); bad += 1; continue
    if not pdf.exists():
        if fix:
            make_pdf(md, pdf)
            print(f"[시스템 생성] {r}: {pdf.name} (연구원이 만들지 않아 대신 생성)")
        else:
            print(f"[누락] {r}: PDF {pdf.name} 없음"); bad += 1
            continue
    else:
        print(f"[통과] {r}: {md.name} + {pdf.name}")
print("라운드 점검", "실패" if bad else "통과")
sys.exit(1 if bad else 0)
