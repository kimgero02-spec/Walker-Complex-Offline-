# Team MAD — 수학 연구 AI 시스템

오케스트레이터 1명과 연구원 3명이 **방 시스템**(개인 연구실 + 중앙 도서관) 안에서 협업하는 Claude 기반 멀티 에이전트 수학 연구 시스템입니다. 모든 출력은 한국어로 작성됩니다.

## 팀 구조

| 구성원 | 역할 | 사용할 수 있는 도구 |
|---|---|---|
| **대수검존** (마스터) | 연구 과제를 내리고 최종 보고를 받음 | — |
| **오케스트레이터** | 마스터에게 보고할 수 있는 **유일한** 구성원. 연구원별 임무 지시 | `list_library`, `read_report`, `assign_mission`, `report_to_master` |
| **researcher1** | 기본 역할: 예제 계산 | `write_note`, `read_my_notes`, `list_library`, `read_report`, `submit_report` (+ 코드 실행) |
| **researcher2** | 기본 역할: 패턴 추출·이론 구조화 | 위와 동일 |
| **researcher3** | 기본 역할: 장애물·반례 탐색, 검증 | 위와 동일 |

연구 원칙: **여러 예제를 계산 → 공통 패턴과 공통 장애물 추출 → 이론 구조화**. 증명된 것, 수치로만 확인된 것, 추측을 구분합니다.

## 방 시스템과 규칙 (코드로 강제됨)

- **개인 연구실** (`rooms/<연구원>/notes.md`): 주인 연구원만 읽고 쓸 수 있습니다.
- **중앙 도서관** (`library/*.md`, `index.json`): 연구원과 오케스트레이터 모두 열람 가능. 보고서 제출은 연구원만 가능하며, 제출된 보고서는 수정되지 않습니다.
- **매 턴 보고서 제출 필수**: 연구원이 보고서를 내지 않으면 한 번 재촉하고, 그래도 없으면 시스템이 마지막 응답을 `강제 제출` 상태로 도서관에 등록합니다.
- **마스터 보고 권한**: `report_to_master`는 오케스트레이터에게만 있습니다. 연구원이 호출하면 권한 오류가 돌아갑니다.

## 진행 흐름

```
라운드 k:
  오케스트레이터 ── 도서관 검토 ──> assign_mission(연구원별 임무)  또는  report_to_master(종료)
  연구원 1·2·3 (병렬) ── 개인 연구실에서 연구 ──> submit_report → 중앙 도서관
마지막 라운드 후: 오케스트레이터가 도서관을 종합해 대수검존에게 최종 보고
```

결과물은 `workspace/session-<시각>/` 아래 저장됩니다: `problem.md`, `rooms/`, `library/`, `master/final_report.md`.

## 실행

```bash
cd math_research_ai
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...        # 또는 `ant auth login`

python -m mad "x^2 + y^2 = p 를 만족하는 소수 p의 특징을 연구하라" --rounds 3
python -m mad --problem-file problem.txt --effort xhigh
python -m mad "아무 과제" --dry-run   # API 호출 없이 흐름만 시험
```

옵션: `--rounds`(기본 3), `--effort low|medium|high|xhigh|max`(기본 high), `--model`(기본 `claude-opus-5-5`), `--no-code-exec`, `--sequential`, `--workspace`.

API 설정: adaptive thinking, 서버 측 거절 폴백(`fallbacks: "default"`)을 켜 두었습니다. 연구원은 예제 계산을 위해 서버 측 코드 실행 도구를 쓸 수 있습니다(`--no-code-exec`로 끔).

## 테스트

```bash
python -m pytest -q tests
```
