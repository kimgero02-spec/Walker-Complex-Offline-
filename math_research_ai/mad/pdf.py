#!/usr/bin/env python3
"""마크다운 보고서를 PDF로 변환한다 (한글 + 수식 지원).

사용법: python3 -m mad.pdf 보고서.md [출력.pdf]   (math_research_ai 폴더에서)

pandoc 이 수식을 MathML 로 바꾸고, 헤드리스 Chromium 이 PDF 로 인쇄한다.
인터넷 연결이 필요 없다. 실패하면 0이 아닌 코드로 종료한다.
"""
import glob
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CSS = """
@page { size: A4; margin: 18mm 16mm; }
body { font-family: 'Noto Sans CJK KR','Noto Sans KR','NanumGothic','Malgun Gothic',
       'WenQuanYi Zen Hei','Unifont-JP',sans-serif; font-size: 11pt; line-height: 1.6; }
h1 { font-size: 20pt; border-bottom: 2px solid #333; padding-bottom: 4px; }
h2 { font-size: 15pt; margin-top: 1.4em; } h3 { font-size: 12.5pt; }
table { border-collapse: collapse; margin: 0.8em 0; font-size: 10pt; }
th, td { border: 1px solid #888; padding: 3px 7px; }
th { background: #eee; }
code, pre { font-family: 'DejaVu Sans Mono',monospace; font-size: 9.5pt; background: #f4f4f4; }
pre { padding: 6px; white-space: pre-wrap; }
math { font-size: 1.05em; }
"""


def find_chromium() -> str:
    for name in ("chromium", "chromium-browser", "google-chrome"):
        p = shutil.which(name)
        if p:
            return p
    hits = glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome")
    if hits:
        return sorted(hits)[-1]
    raise RuntimeError("Chromium 을 찾을 수 없습니다.")


def make_pdf(md: Path, pdf: Path) -> Path:
    with tempfile.TemporaryDirectory() as td:
        css = Path(td) / "style.css"
        css.write_text(CSS, encoding="utf-8")
        html = Path(td) / "report.html"
        subprocess.run(
            ["pandoc", str(md), "-f", "markdown+tex_math_dollars", "-t", "html5", "-s",
             "--mathml", "--metadata", f"title={md.stem}", "-c", str(css), "--embed-resources",
             "-o", str(html)],
            check=True)
        # pandoc 의 자동 제목 블록은 중복이므로 제거
        text = html.read_text(encoding="utf-8")
        html.write_text(text.replace(f'<h1 class="title">{md.stem}</h1>', ""), encoding="utf-8")
        pdf.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [find_chromium(), "--headless", "--no-sandbox", "--disable-gpu",
             "--no-pdf-header-footer", f"--print-to-pdf={pdf}", html.as_uri()],
            check=True, capture_output=True)
    if not pdf.exists() or pdf.stat().st_size < 1000:
        raise RuntimeError(f"PDF 생성 실패: {pdf}")
    return pdf


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".pdf")
    print(make_pdf(src, out))
