"""실행: python -m mad "연구 과제" [옵션]"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from .llm import DEFAULT_MODEL, AnthropicBackend, DryRunBackend
from .team import TeamMAD


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="mad", description="Team MAD 수학 연구 AI 시스템")
    p.add_argument("problem", nargs="?", help="연구 과제(생략하면 --problem-file 사용)")
    p.add_argument("--problem-file", type=Path, help="연구 과제가 적힌 파일")
    p.add_argument("--rounds", type=int, default=3, help="최대 연구 라운드 수 (기본 3)")
    p.add_argument("--workspace", type=Path, default=Path("workspace"), help="방·도서관 저장 위치")
    p.add_argument("--model", default=DEFAULT_MODEL)
    p.add_argument("--effort", default="high", choices=["low", "medium", "high", "xhigh", "max"])
    p.add_argument("--no-code-exec", action="store_true", help="연구원의 코드 실행 도구 끄기")
    p.add_argument("--sequential", action="store_true", help="연구원을 순서대로 실행")
    p.add_argument("--dry-run", action="store_true", help="API 호출 없이 흐름만 시험")
    args = p.parse_args(argv)

    problem = args.problem or (args.problem_file.read_text(encoding="utf-8") if args.problem_file else None)
    if not problem:
        p.error("연구 과제를 인자로 주거나 --problem-file 을 지정하세요.")

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%H:%M:%S")
    backend = DryRunBackend() if args.dry_run else AnthropicBackend(
        model=args.model, effort=args.effort, code_execution=not args.no_code_exec)
    team = TeamMAD(problem, backend, args.workspace, max_rounds=args.rounds, parallel=not args.sequential)
    final = team.run()
    print(final.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
