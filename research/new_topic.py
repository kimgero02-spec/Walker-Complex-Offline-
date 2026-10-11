#!/usr/bin/env python3
"""새 연구 주제 폴더(칸막이)를 만든다.

사용법: python3 research/new_topic.py <영문-슬러그> "<연구 과제>"
  예) python3 research/new_topic.py knot-invariants "매듭 불변량 연구"

research/<슬러그>/ 아래에 library/, rooms/researcher1~3/, master/, problem.md 를 만든다.
주제 하나가 하나의 독립된 칸막이이며, 다른 주제의 도서관과 섞이지 않는다.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

if len(sys.argv) != 3 or not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", sys.argv[1]):
    raise SystemExit(__doc__)
slug, problem = sys.argv[1], sys.argv[2]
topic = ROOT / slug
if topic.exists():
    raise SystemExit(f"이미 존재하는 주제입니다: {topic} (기존 주제를 이어서 하려면 새로 만들지 마세요)")
for sub in ("library", "master", "rooms/researcher1", "rooms/researcher2", "rooms/researcher3"):
    (topic / sub).mkdir(parents=True)
    (topic / sub / ".gitkeep").touch()
(topic / "problem.md").write_text(f"# 연구 과제 (대수검존)\n\n{problem}\n", encoding="utf-8")
print(f"칸막이 생성: {topic}")
