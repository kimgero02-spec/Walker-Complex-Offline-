#!/usr/bin/env python3
"""보고서 PDF 변환 실행기. 사용법: python3 research/tools/make_pdf.py 보고서.md [출력.pdf]"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "math_research_ai"))
from mad.pdf import make_pdf  # noqa: E402

if len(sys.argv) < 2:
    raise SystemExit(__doc__)
src = Path(sys.argv[1])
out = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".pdf")
print(make_pdf(src, out))
