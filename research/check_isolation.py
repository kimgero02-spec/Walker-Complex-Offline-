#!/usr/bin/env python3
"""주제 간 칸막이 점검: 한 주제의 파일이 다른 주제 폴더를 참조하면 위반으로 보고한다.

사용법: python3 research/check_isolation.py [research 폴더 경로]
- 다른 주제의 슬러그나 경로(예: research/other-topic, ../other-topic)가 등장하면 위반.
- 위반이 있으면 종료 코드 1. 오케스트레이터는 라운드를 끝내기 전에 이 점검을 통과해야 한다.
"""
import sys
from pathlib import Path

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
# 연구 주제 폴더 = problem.md 가 있는 폴더. (formations/ 같은 공용 폴더는 제외)
topics = sorted(p.name for p in root.iterdir() if p.is_dir() and (p / "problem.md").exists())
TEXT = {".md", ".py", ".txt", ".json", ".csv", ".tex"}
bad = 0
for t in topics:
    others = [o for o in topics if o != t]
    for f in (root / t).rglob("*"):
        if not f.is_file() or f.suffix not in TEXT:
            continue
        text = f.read_text(encoding="utf-8", errors="ignore")
        for o in others:
            if o in text:
                print(f"[위반] {f.relative_to(root)} 가 다른 주제 '{o}' 를 참조")
                bad += 1
        if "../../" in text:
            print(f"[위반] {f.relative_to(root)} 가 주제 밖 경로(../../)를 참조")
            bad += 1
print(f"주제 {len(topics)}개 점검:", "칸막이 위반 있음" if bad else "칸막이 이상 없음")
sys.exit(1 if bad else 0)
