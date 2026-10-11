# [R07-researcher3] 평면 시트 분해 (thickness 류) 의 이산 호지 번역과 $\operatorname{zig}$ 에 주는 것

- 작성자·라운드·역할: researcher3 / 라운드 7 / 망상꾼 (분야: 이산 호지 이론). 요청: 문주님 제안 "평면 시트를 빌딩블록으로 한 결합 관점" (오케스트레이터 전달).
- 해석 (명시): "시트 분해" = 간선 집합의 분할 $E(G)=E_1\sqcup\dots\sqcup E_k$, 각 $G_i=(V,E_i)$ 가 평면 (두께 $\theta(G)\le k$ 와 같은 개념, [기억-미검증]). 시트 사이 간선의 정체는 이 해석에서 시트 간선 자체다. 정점 분할 해석 (정점 쪽 결합) 은 시험하지 않았다.
- 코드: `rooms/researcher3/r07_sheets.py`, `r07_sheets2.py`, `r07_union.py` (기존 `r06_lib.py` 재사용).

## 요약
1. **번역 [증명]:** 시트 $X_i=B_0^{\emptyset}(G_i)\subseteq X(G)$ 는 부분 복합체다 (시트 안의 biclique 는 $G$ 의 biclique). 그런데 $\bigcup_i X_i\subsetneq X(G)$: $G$ 의 biclique 가 여러 시트에 걸친 간선으로 만들어지면 그 면은 어느 $X_i$ 에도 없다. 이 "시트 결함" 이 호지 쪽 새 대상이다.
2. **$\operatorname{zig}$ 에 주는 것:** 합 법칙 $\operatorname{zig}(G_1\cup G_2)\le\operatorname{zig}(G_1)+\operatorname{zig}(G_2)-1$ 은 **거짓** (반례 $K_6=\text{oct}\cup PM_3$: $\operatorname{zig}$ 는 $6>3+2-1$). 곱 법칙 $\operatorname{zig}(G_1\cup G_2)\le\operatorname{zig}(G_1)\operatorname{zig}(G_2)$ 는 4개 예에서 성립하고 $K_6$ 에서 등호 [추측]. 확실한 결과는 $\chi$ 쪽: $\chi(G)\le\prod\chi(G_i)\le 4^k$ [증명] (색칠의 곱). 즉 시트 결합은 $\operatorname{zig}$ 를 다루지 못하고 $\chi$ 상계만 준다.
3. **$\tau$ 에 주는 것:** $\tau\le\chi\le 4^k$ 만 얻는다 [증명]. $\tau\ge$ 하한을 시트에서 올리는 방법은 찾지 못했다 [망상].
4. **예측 판정:** 반증 가능한 예측 7개 중 $\operatorname{zig}$ 합 법칙 반증, 곱 법칙 3예 확인 (추측 유지), 시트 결함의 호몰로지 기여 $K_5$, $K_6$ 에서 확인.

## 1. 번역 사전
| 시트 쪽 | 이산 호지 쪽 | 어긋나는 점 |
|---|---|---|
| 평면 시트 $G_i$ | 부분 복합체 $X_i=X(G_i)\subseteq X(G)$ (빈 면 허용 박스 복합체, 이분 독립 복합체 $\operatorname{Ind}(H^c)$ 의 부분 복합체) | 시트 면들의 합이 $X(G)$ 전체를 주지 않는다 |
| 시트 사이 간선 | 면 $(A,B)$ 가 여러 시트의 간선으로 만들어짐 | 결합은 면 단위이지 정점 단위가 아니다 |
| "층화" | 필터레이션 $\bigcup_{j\le i}X_j$ (시트 순서). 하지만 $X_i$ 가 단조 아님 | 시트 순서에 따라 결함이 달라진다 |
| 결합 사상 | 포함 $\bigcup X_i\hookrightarrow X(G)$ 와 그 상대 호몰로지 $H_*(X(G),\bigcup X_i)$ = 시트 결함 | 실수 호지 분해는 결함을 부호로만 보고 ([R06] T3) 대칭 작용 파악 불가 |
| $\operatorname{zig}$ | 경로 위 런 수 min-max | 시트 합에 대해 선형 법칙 없음 (2절) |
| $\chi$ 의 곱 색칠 | 시트 쌍의 곱 사상 $V\to\prod\{1..4\}$ | $\operatorname{zig}$ 에는 대응 없음 (런 수는 곱 구조를 안 따름) |

## 2. 가져온 도구
1. ★ **시트 결함 (상대 호몰로지)** [계산 확인]: $X(G)$ 와 $\bigcup_i X(G_i)$ 의 호몰로지 차이. 팀 기존 보고서에 없음.
2. ★ **색칠의 곱 보조정리** [증명]: 각 $G_i$ 의 진색칠 $c_i$ 에 대해 $c=(c_1,\dots,c_k)$ 는 $G$ 의 진색칠. 따라서 $\chi\le\prod\chi(G_i)$.
3. ★ **두께 개념과 $K_n$ 의 두께** [기억-미검증]: $\theta(K_n)=\lfloor (n+7)/6\rfloor$ ($n\ne9,10$), $\theta(K_5)=\theta(K_6)=2$.
4. (R06 에서 이어짐) 우월 정점 불변성 ([R06] O3) 과 $\operatorname{coind}$ 의 동변 불변성 (시트 쪽 축약에 쓸 수 있음).

## 3. 예측 (반증 가능)
| # | 주장 | 이유 | 검증 (작은 예) | 결과 |
|---|---|---|---|---|
| S1 | $\operatorname{zig}(G_1\cup G_2)\le\operatorname{zig}(G_1)+\operatorname{zig}(G_2)-1$ | 가법 | $K_5=C_5\cup\overline{C_5}$ (3,3→5 OK), $K_5=(K_5-e)\cup e$ (4,2→5 OK), $K_6=\text{oct}\cup PM_3$ (3,2→**6 > 4**) | **반증됨** ($K_6$) |
| S2 | $\operatorname{zig}(G_1\cup G_2)\le\operatorname{zig}(G_1)\operatorname{zig}(G_2)$ | 곱 (색칠 류 직관) | 위 3예 ($5\le9$, $5\le8$, $6\le6$) | **확인 (3예), 추측 유지** |
| S3 | $\chi(G_1\cup G_2)\le\chi(G_1)\chi(G_2)$ | 곱 색칠 | 일반 성질 | **증명** [증명] |
| S4 | $X(G)\ne\bigcup X(G_i)$ 이고 $G$ 의 최고 $\tilde H$ 차원 $\tau-1$ 은 시트 결함에서 온다 | 결함 | $K_5$: $\tilde H_4(X)=\mathbb Z$, $\bigcup$ 은 $\tilde H_2=\mathbb Z^3$; $K_6$: $\tilde H_5(X)=\mathbb Z$, $\bigcup$ 은 $\tilde H_1=\mathbb Z^6$, $\tilde H_2=\mathbb Z$ | **확인** (두 예) |
| S5 | 두께 $k$ 인 $G$ 에서 $\operatorname{zig}(G)\le 4^k$ (평면 $\operatorname{zig}\le4$ 가정) | 곱 + 평면 Q_3 | $K_n$ ($\theta\le 2$ 에서 $n\le8$): $\operatorname{zig}(K_8)=8\le16$ | 조건부 [추측]; 평면 $\operatorname{zig}\le4$ 는 팀의 열린 문제 (R04) |
| S6 | $\tau(G_1\cup G_2)\ge\tau(G_1)+\tau(G_2)-1$ | 결함이 호몰로지 차원을 올림 | $K_5$: $\tau=5$, 시트 $\operatorname{zig}$ 값 3,3 (τ 는 $\le$ zig 이므로 시트 τ 상계 사용 주의) ; $K_6$: $\tau(K_6)=6$, 시트 zig 값 $3,2$ 로 $3+2-1=4\le6$ | **확인 (2예, 시트 τ 대신 zig 상계 사용), [추측]** |
| S7 | 평면 시트 두 장을 붙이면 ($G=G_1\cup G_2$, 공통 정점 $\le 3$) $\operatorname{zig}\le 8$ | 평면 zig 4 + 곱 | $K_{3,3}$: 2 ≤ 8 | [추측], 시험 미실시 (큰 예) |

## 4. 해석과 한계
- S1 의 반례는 "시트는 값이 작은데 합의 런 수가 곱처럼 큰" 현상을 보여 준다. 시트 결합은 런 수에 대해 가법이 아니다.
- S4 는 "결함이 상단 호몰로지를 만든다" 는 관찰이고 증명은 없다 (두 예뿐).
- S6 는 $\tau$ 쪽의 가법형 추측이며 두 예만 확인. $\tau$ 가 $\operatorname{zig}$ 의 등호 질문에 어떻게 관련되는지는 여기서 결정하지 못했다.
- 정점 분할 해석 (정점별 시트) 은 시험하지 않았다.

## 문주님께 요청
- 없음. (선택: 두께 $\theta(K_n)$ 공식과 예외 $n=9,10$ 의 출처 확인 — [기억-미검증].)

## 후속연구 지점
1. **곱 법칙 S2 의 반증 시도 (우선순위 1).** 이유: 가법 S1 이 깨졌으므로 $\operatorname{zig}$ 의 시트 결합 법칙으로 남은 후보. 시작: 두께 2 인 큰 그래프에서 시트 분해를 고르고 $\operatorname{zig}$ 를 상계/하계로 계산 (국소 탐색 상계 사용). 난점: $\operatorname{zig}$ 의 정확한 계산은 $n\le8$ 까지만 가능.
2. **시트 결함의 호몰로지 공식 (S4).** 이유: 결함이 상단 차원을 만든다면 $\tau$ 의 시트 하한 (S6) 이 증명 가능. 시작: 멸종 쌍 $(X(G), \bigcup X_i)$ 의 Mayer–Vietoris 열 계산 ($K_5$, $K_6$, 그리고 $K_{3,3}$). 난점: 결함의 기저를 정하는 일.
3. **정점 분할 해석 실험.** 이유: 문주님의 "시트" 가 정점 분할일 가능성. 시작: 정점을 두 조각으로 나누고 각 조각의 유도 부분그래프의 $\operatorname{zig}$ 와 결합 간선 수. 난점: 해석 확정 필요 (문주님 확인 요청).
4. **$\tau$ 가법 S6 의 반례 탐색 (n≤8 목표 족).** 이유: 가법이 맞으면 $\tau$ 하한이 시트에서 나온다. 시작: $K_{3,3}$, 기타 두께 2 족. 난점: $\tau$ 의 정확한 계산 부재 (coind 하계 필요).
