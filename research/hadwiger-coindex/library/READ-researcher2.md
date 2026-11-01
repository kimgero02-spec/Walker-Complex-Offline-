# READ-researcher2: 도서관 전체 읽기 기록과 자기 점검

- 작성자·역할: researcher2 (연구 중단 지시 후 읽기 전용 작업). 기존 파일은 수정하지 않았다. 새 계산·새 증명은 하지 않았다.
- 표기: `[읽음-전문]` 본문을 끝까지 읽음, `[읽음-앞부분]` 앞 1–5 KB 와 요약·결론 위주, `[목록]` 파일명만 확인 (내용 미확인).

## 1. 읽은 파일 목록

| 범위 | 파일 | 읽은 정도 |
|---|---|---|
| 문제·STATUS·최종 | problem.md, STATUS.md (R07–R08 절, 열린 문제 절, 중단 기록), master/final_report.md (§1–7 및 R12–R34 추가 보고) | [읽음-앞부분] (STATUS 는 전체 구조와 R04·R06·R08 절 위주) |
| 원문 노트 | SRC-diestel-ch7.md, SRC-steiner-2312.17130.md, SRC-norin-steiner-2610.05291.md | [읽음-전문] |
| 원문 연구 노트 | STUDY-researcher1.md (Steiner 정독, 전문 확인 가능한 범위), STUDY-researcher2.md (Norin–Steiner 정독, 앞부분 5 KB), STUDY-researcher3.md (Diestel 발췌 검증, 앞부분 5 KB) | [읽음-앞부분] |
| N1 (R05) | N1-researcher1.md, N1-researcher2.md, N1-researcher3.md | [읽음-앞부분] (각 4.5 KB) |
| R01 | 9 개 파일 (orchestrator-verify, researcher1/2/3, interim 3 개) | [읽음-앞부분] |
| R02 | 8 개 파일 (orch-data-C5Km, orchestrator-verify, researcher1/2/3 과 interim 2 개, researcher1-interim) | [읽음-앞부분] (orch-data 의 배치 JSON 은 내용 확인만) |
| R03 | 7 개 (orchestrator-verify, researcher1/2/3, interim 3 개 중 일부) | [읽음-앞부분] |
| R04 | 7 개 (orchestrator-verify, researcher1/2/3, interim 3 개) | [읽음-앞부분] |
| R06 | 6 개 (researcher1/2/3 과 interim 2 개) | [읽음-앞부분] |
| R07 | 6 개 (researcher1/2/3, interim 2 개 포함) | [읽음-앞부분] |
| R08 | researcher1, researcher1-interim, researcher3, researcher3-interim | [읽음-앞부분] (R08-researcher1 은 §요약·§본문 일부 전문) |
| R09 | researcher1, researcher2 (내 것, 본문 전체 작성), researcher3 | [읽음-앞부분] |
| R10 | researcher1, researcher2 (내 것), researcher3 | [읽음-앞부분] |
| R11 | researcher2 (내 것) | [읽음-전문] |
| R12 | researcher1, researcher2 (내 것), researcher3, researcher3-ideas | [읽음-앞부분] (ideas 는 I-1, I-5 절 읽음) |
| R13 | researcher1, researcher2 (내 것), researcher3 | [읽음-앞부분] |
| R14 | researcher1, researcher2 (내 것), researcher3 | [읽음-앞부분] |
| R15 | researcher1, researcher2 (내 것), researcher3 | [읽음-앞부분] |
| R16 | researcher1, researcher2 (내 것), researcher3 | [읽음-앞부분] |
| R17 | researcher1, researcher2 (내 것), researcher3 | [읽음-앞부분] |
| R18 | researcher1, researcher2 (내 것), researcher3 | [읽음-앞부분] |
| R19 | researcher1, researcher2 (내 것) | [읽음-앞부분] |
| R20 | researcher1, researcher2 (내 것), researcher3 | [읽음-앞부분] |
| R21 | researcher1, researcher2 (내 것), researcher3 | [읽음-앞부분] |
| R22 | researcher1, researcher2 (내 것), researcher3 | [읽음-앞부분] |
| R23 | researcher1, researcher3 | [읽음-앞부분] |
| R24 | researcher1 | [읽음-앞부분] |
| R25 | researcher1 | [읽음-앞부분] |
| R26 | researcher1 | [읽음-앞부분] |
| R27–R31 | researcher2 (모두 내 것) | [읽음-앞부분] (내 것이므로 본문은 기억) |
| R32 | researcher3 | [읽음-앞부분] |
| R33–R34 | researcher2 (내 것) | [읽음-앞부분] |
| 목록만 | R05 나머지 (N2/N3 는 파일명 없음), 기타 R 파일의 중간 본문 | [목록] |

한계: 전체 105 파일 중 본문을 끝까지 읽은 것은 SRC 3 개, R11-researcher2 (내 것) 뿐이다. 나머지는 앞부분과 요약 위주다. 따라서 아래 지적은 "앞부분에서 본 주장" 에 한정된다.

## 2. 남의 보고서에서 내가 몰랐거나 틀렸다고 생각하는 주장 (3개 이하)

1. **R18-researcher3 §1 (P3 판정, C_5[K_2]) — 의심.** "부분그래프 $K_t\subseteq G$ 이면 $h(B_0G)\ge t-1$" 을 단조성 보조정리로 썼다. 그런데 $h$ (Stiefel–Whitney 높이) 는 부분복합체에 대해 단조라는 근거가 보고서에 없다. $S^{t-1}=B_0(K_t)$ 가 부분복합체인 것만으로는 $h(B_0G)$ 의 하한이 나오지 않는다. 같은 보고서가 $h\le\operatorname{coind}$ 를 쓰므로, 판정 "h=3=τ−1" 은 단조성 없이는 닫히지 않는다. 판정: 틀렸다고 단정하지는 않지만, 근거가 빠져 있다.
2. **R09-researcher3 §4 (J 증명 주장) — 틀림 (내가 R09 부록에서 정정).** 레트랙션 $U_i\to X(G[V_i])$ 와 조인 보조정리는 ind 판 상계만 준다. coind 판 J 는 이 논법으로 나오지 않는다. 같은 오류가 R08-researcher3 P1 에도 있었다. 이후 R10–R13 은 이 정정을 반영했다 (확인: R10-researcher1 의 "τ=Στ_i 는 τ_i=ι_i 일 때만"). 판정: 정정 완료.
3. **R02-researcher2 / R03-researcher2 / R04-researcher2 (τ ≤ zig 의 직접 증명, "문헌 없이").** 모멘트 사상 $B_0(G)\to\mathbb R^{d}\setminus0$ 과 Gale 보조정리 (런 $\le d+1$ 이면 분리) 로 $\tau\le\operatorname{zig}$ 를 얻는다고 했다. 이 부등식은 이후 거의 모든 간극·상계 결과 (R14–R34 의 $\tau\le3$ 판정, 17정점 예의 간극 판단 등) 의 기반이다. 나는 R03-researcher2 의 증명 세부 (모든 극대쌍 분리) 를 독립 재검증하지 않았고, R04-researcher2 가 "S3 완전 자립" 이라 쓴 것도 이 한 부등식에 달려 있다. 판정: 미검증 기반. 외부 검증 전에는 확정으로 쓰지 말 것.

## 3. 나 자신의 결과 중 본질 (Hadwiger 시트 질문) 과 무관한 것

- R18 (K_4,K_4), (K_4,K_3) 의 χ/τ 임계와 2^16 패턴 전수 스캔 (scan_all, scan5): 간극 탐색이지 Hadwiger 가 아님. 결과 (ω=χ) 는 τ=χ 를 주지만 마이너 질문은 건드리지 않음.
- R20 3 블록 임계 (|F|≤4 전수): 임계 4 는 K_5 별. 자명에 가까움.
- R21 7 정점 아틀라스 간극 목록, 평면 여부: 간극 목록 확인. 본질과 무관.
- R22 8 정점 확장 317 개와 17정점 평면 여부 판정: 간극 존재 확인. 본질과 무관.
- R27 (8 정점 이하 모두 $\mathcal C_2$) 과 R28 (9 정점 5+4 분할): 시트 조건이 n≤9 에서 자명하다는 확인. 시트 질문의 "자명화" 결과이므로 본질과 가깝지만 Hadwiger 를 건드리지 않음.
- R29 (6 정점 집합 평균 논증, E≥33): 시트 실패의 필요조건. 간접적으로 본질에 가깝지만 K_t 마이너와는 연결이 없음.
- R30 (X_M 차수 장벽), R31 (진짜 X_M 간극 없음, C_5[K_2] 실패): 교차 공리 쪽. 본질과 간접 관련.
- R33 (χ≤4 미결 진술, 색 치환 Hall 실패): 증명 시도 자체는 무관. 결론은 "미결".
- R34 (17 정점 진짜 X_M 에서 χ=5): χ=5 는 Hadwiger t=5 (Wagner, 이미 알려짐) 와 같은 수준. 그래프 자체는 K_5 마이너를 가지며 Hadwiger 를 시험하지 않음. 간극 여부도 미판정. 가장 무관함.
- R11 (τ ≤ 3k+s): τ 상계는 Hadwiger 와 연결되지 않음 (τ 는 마이너 단조가 아님, R12 확인). 본질과 간접 관련.

## 4. 도서관 전체를 보고 나서 본질로 돌아가는 질문 1개와 판정 기준

**질문**: 2-시트 평면 클래스 $\mathcal C_2$ (정점 분할 $V=V_1\sqcup V_2$, 각 $G[V_i]$ 평면, 교차 간선 무제한) 에서, $\chi(G)\ge7$ 인 모든 $G$ 가 $K_7$ 마이너를 가지는가? (Hadwiger 의 $t=7$ 을 시트 클래스에 제한한 것.)

**판정 기준**
- **참 (증명)**: 블록 색수 분해 $\chi\le\chi_1+\chi_2$ 와 최소 블록 쌍 모델로, 모든 $(B_1,B_2)$ 쌍 (χ_1+χ_2≥7) 에 대해 $K_7$ 모델이 교차 패턴과 무관하게 존재함을 보이면 참. 현재 증명된 것은 완전 교차 (조인) 뿐 (R25-r1).
- **거짓 (반례)**: $\chi\ge7$ 이면서 $K_7$ 마이너가 없는 $\mathcal C_2$ 그래프 하나. 판정 도구: 반례 후보는 $(W_5,K_3)$ 또는 $(K_4,K_3)$ 블록의 교차 패턴 중 $K_7$ 모델이 깨지는 최소 패턴이다 (R17 에서 $W_5+C_5$ 의 $|F|=10$ 깨짐 상계, R26 에서 $(W_5,K_3)$ 의 $m^*\in[8,12]$).
- **판정 완료 조건**: $(W_5,K_3)$ 의 교차 8–11 구간 전수 (대량 계산 허가 필요) 또는 $K_7$ 모델의 구조 정리 (분기 집합 혼합 허용). 어느 쪽이든 나오면 질문이 닫힌다.

이 질문은 τ 를 쓰지 않고 시트 구조와 Hadwiger 를 직접 잇는다. 나머지 결과 (간극 소속, χ=5 예, zig 판정) 는 이 질문의 보조일 때만 가치가 있다.
