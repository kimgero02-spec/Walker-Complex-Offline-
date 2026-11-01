# [R06-researcher3] 이산 호지 이론으로 본 $\tau=\operatorname{zig}$: 독립 복합체 번역, 우월 정점 불변성, 호몰로지·실수 호지 분해의 반증

- 작성자·라운드·역할: researcher3 / 라운드 6 / 망상꾼 (분야: 이산 호지 이론 = 단체 복합체 위의 코경계·조합 라플라시안 $L_k$·호지 분해, 그리고 독립 복합체의 이산 모스 매칭).
- 용어: 조합 라플라시안 $L_k=\partial_{k+1}\partial_{k+1}^{*}+\partial_k^{*}\partial_k$ 의 영공간은 조화 $k$-사슬이며 그 차원이 $\tilde\beta_k$ 다. 이산 모스 매칭은 면들을 짝지어 임계 셀만 남기는 방법이다.
- 코드: `rooms/researcher3/r06_lib.py` (면 구성, 호몰로지, $\operatorname{zig}$ 완전 탐색), `r06_t1.py` ~ `r06_t7.py`, `r06_hodge.py` (실수 호지 분해), `r06_zigsearch.py` (상계 탐색). 중간 목록: `library/R06-researcher3-interim.md`.
- 도서관 확인: 반례꾼2 의 R06 공격 결과 (`R06-researcher2*.md`) 는 이 보고서를 쓰는 시점에 없었다. 공격 반영은 하지 못했다.

## 요약
1. **번역 [증명]:** 빈 면 허용 박스 복합체 $X(G)=B_0^{\emptyset}(G)$ 는 이분 그래프 $H^c$ 의 독립 복합체다. $H^c$ 는 $a_1\sim b_2\iff(a=b$ 또는 $ab\notin E)$ 인 이분 그래프. 이로부터 $X(G)\simeq\Sigma N(G)$ 가 나오고 ($N(G)$ 는 이웃 복합체, 일반 보조정리는 [기억-미검증]), $\tau(G)=\operatorname{coind}(N(G))+2$ 로 읽힌다. 8개 그래프에서 호몰로지 일치 [계산 확인].
2. **우월 정점 불변성 [증명]:** $N(a)\subseteq N(c)$ 이면 $\operatorname{zig}(G)=\operatorname{zig}(G-a)$ 이고 $\tau(G)=\tau(G-a)$ 다 (동변 단체 사상 $a_i\mapsto c_i$ 로 $\operatorname{coind}$ 가 양방향으로 같다). 따라서 $\tau=\operatorname{zig}$ 의 최소 반례는 우월 정점이 없다. 7개 예에서 $\operatorname{zig}$ 불변 확인 [계산 확인].
3. **순진한 호몰로지 번역은 깨짐 [계산 확인+증명]:** $C_6$ 에서 $\operatorname{zig}=\tau=2$ 인데 $\tilde H_2(X(C_6))\cong\mathbb Z^2\ne0$. 따라서 $\operatorname{zig}-1$ 차원 CW 모델에 의한 이산 모스 증명 (매칭 트리 포함) 은 $C_6$ 에서 불가능하다. $\tau\le\operatorname{zig}$ 의 증명은 셀 모델이 아니라 사상 (모멘트 곡선) 으로 가야 한다.
4. **실수 호지 분해는 $\operatorname{coind}$ 를 못 본다 [계산 확인]:** 반대칭 조화류의 최고 차원은 $K_n$ 에서 $n$ 의 홀짝으로 갈리고 ($K_4$ 는 0), 그래서 실수 부호 분해는 $\operatorname{coind}$ 의 하계가 아니다. $\mathbb F_2$ 의 Stiefel–Whitney 높이만 후보다.
5. **반증 가능한 예측 12개 중 판정:** P1, P3, P5(K_2–K_6), P7, P8, P9, P10 은 성립 또는 확인. P2, P4($C_6$), P6, P12 는 반증됨. P11($C_5[K_3]$) 은 계산 비용 때문에 미시험. **$\tau=\operatorname{zig}$ 에 대해서는 새 반례도 새 증명도 없다.** 호지 쪽 도구는 등호 판정에 직접 쓰이지 않는다.

## 번역 사전
| 문제 쪽 | 이산 호지 쪽 | 어긋나는 지점 |
|---|---|---|
| 박스 복합체 $B_0(G)$, 빈 면 허용 (두 복사본 $V\times\{1,2\}$, 면 $(A,B)$, $A\times B\subseteq E$) | 1-골격이 $H(G)$ 인 클리크 복합체 $\mathrm{Cl}(H)$, $H(G)$ 는 $K_n\sqcup K_n$ 에 교차 간선 $G\times K_2$ 를 더한 것 [증명] | 표준 $B_0$ (비공집합) 과 $\Sigma$ 만큼 어긋난다 (호몰로지 대조로 확인) |
| 면 $(A,B)$ 의 차원 $|A|+|B|-1$ | 단체 차원, 사슬 $C_k$ | 없음 |
| $\operatorname{coind}$ (Z_2-지표) | 독립 복합체 $\operatorname{Ind}(H^c)$ 의 대칭 $x_1\leftrightarrow x_2$ 에 대한 조화 사슬의 부호 분해 | 실수 부호 분해는 패리티만 본다 (아래 T3). $\mathbb F_2$ 에는 직교 분해가 없다 |
| 런 수 $r(X,Y;\sigma)$ | 경로 위 0/1 라벨의 전변동 $1+\|\delta f\|_1$ | $L^1$ 량이며 $L^2$ 라플라시안과 무관 |
| $\operatorname{zig}=\min_\sigma\max_{(X,Y)}r$ | 경로 위 부호 변화 수의 min-max (Sturm 류) | 호몰로지 차원과 무관 (P2, $C_6$) |
| 라플라시안 $L_k$, 조화류 $\cong\tilde H^k$ | 호지 분해 | 조화 차원은 호몰로지 차원이며 쌍대 지표가 아니다 |
| 이산 모스 셀 | 독립 복합체의 매칭 트리 | 임계 차원 $\ge$ 최고 호몰로지 차원 (P12 반증) |
| 우월 정점 $N(a)\subseteq N(c)$ | 독립 복합체의 fold (Engström) | 동변 판이 필요하다 (O3 에서 자체 증명) |

**팀이 쓴 대상과의 차이:** 팀 보고서들은 $B_0$ 의 coind 와 Radon 인증서를 썼고, $N(G)$ 나 독립 복합체, fold 는 쓰지 않았다 (`library` 전수 검색, 'neighborhood', 'independence', 'fold', 'Morse' 없음 확인).

## 가져온 도구
1. ★ **독립 복합체의 현수 보조정리** [기억-미검증]: 이분 그래프 $H$ (부분 $X,Y$) 에 대해 $\operatorname{Ind}(H)\simeq\Sigma K$, $K=\{\sigma\subseteq X: N(\sigma)\ne Y\}$. 여기서 $K=N(G)$ (공통 이웃 복합체) 로 확인: $\sigma\subseteq V$ 에 대해 $N_{H^c}(\sigma)\ne V_2$ 는 $\sigma$ 가 공통 이웃을 가진다는 뜻이다 [증명]. 대응: $\tau=\operatorname{coind}(N(G))+2$ 로 번역.
   - 시험: `r06_t1.py` 에서 $\tilde H_k(X(G))\cong\tilde H_{k-1}(N(G))$ 를 $\mathbb F_{10007}$ 계수로 8개 그래프에서 확인 [계산 확인]. 추가로 $C_5[K_2]$: $\tilde H_3(X)=\mathbb Z^{10}$, $\tilde H_2(X)=\mathbb Z$ 이고 $N$ 쪽은 $\tilde H_2=\mathbb Z^{10}$, $\tilde H_1=\mathbb Z$ 로 한 칸 어긋남 [계산 확인]. $\overline{C_7}$ 도 같은 형태 ($\tilde H_2(X)$, $\tilde H_1(N)$).
2. ★ **동변 우월 정점 사상** [증명, 자체 증명]: $N(a)\subseteq N(c)$ ($a\ne c$, 따라서 $a\not\sim c$) 이면 $\varphi:X(G)\to X(G-a)$, $\varphi(a_i)=c_i$, 나머지 항등, 는 단체 사상이며 $\mathbb Z_2$-동변이다. 증명 요지: 면 $(A,B)$ 가 $a\in A$ 이면 $B\subseteq N(a)\subseteq N(c)$ 이고 $c\notin B$ (안 그러면 $a\sim c$), 따라서 $(A\setminus a\cup c,B)$ 가 면이다. $a\in B$ 쪽은 대칭. $a\in A$ 와 $a\in B$ 가 동시에 나오는 면은 없다 ($a\sim a$ 불가). $\iota:X(G-a)\hookrightarrow X(G)$ 는 동변이고 $\varphi\iota=\mathrm{id}$. 자유 작용 (면이 대칭으로 자기 자신에 가지 않음) 과 함께 $\operatorname{coind}X(G)=\operatorname{coind}X(G-a)$ 이므로 $\tau(G)=\tau(G-a)$ [증명].
   - $\operatorname{zig}$ 불변 [증명]: $\ge$ 은 제한 단조성 (부분 그래프의 극대 쌍은 전체의 쌍 안에 들어가고 제한은 런 수를 늘리지 않음). $\le$ 은 $\operatorname{zig}(G-a)$ 를 이루는 순서 $\sigma'$ 에서 $a$ 를 $c$ 바로 뒤에 넣는다. 극대 쌍 $(X,Y)\ni a$ 이면 $c\in X$ (강제 극대성) 이고, $a$ 와 $c$ 가 인접하므로 런 수가 변하지 않는다.
   - 시험: `r06_t2.py`, 7개 그래프 (K_4, C_5+pendant, P_4, C_5+거짓쌍둥이, C_7+pendant, K_{1,3}+간선) 에서 $\operatorname{zig}(G)=\operatorname{zig}(G-a)$ [계산 확인].
   - 결과: **최소 반례 축약**: $\tau=\operatorname{zig}$ 의 최소 반례는 우월 정점이 없다.
3. ★ **실수 이산 호지 분해와 스왑 부호 분해** [계산 확인]: $L_k$ 의 조화 공간을 스왑 $S$ 의 $\pm1$ 고유공간으로 나눈다. $\dim\ker(L_k|_{\pm})$ 을 $K_2..K_6$, $C_5$, $C_6$, $\overline{C_7}$ 에서 계산 (`r06_hodge.py`, `r06_t6.py`, `r06_t7.py`).
   - 결과: $K_n$ 의 최고 차원 조화류는 $n$ 이 홀수면 반대칭, 짝수면 대칭 (예: $K_3$, $K_5$, $\overline{C_7}$ 은 반대칭; $K_4$, $K_6$ 은 대칭). 즉 실수 부호 분해는 $\dim\ker$ 의 패리티만 본다. 구면 $S^k$ 의 대척 작용이 최고 차원에서 $(-1)^{k+1}$ 로 작용하기 때문이며, 이것은 $\operatorname{coind}=k$ 와 무관하다 [계산 확인, 구면 사실은 [기억-미검증]].
   - 함의: 실수 계수 호지 분해는 $\operatorname{coind}$ 의 하계 도구가 못 된다. 쓸 수 있는 것은 $\mathbb F_2$ Stiefel–Whitney 높이이며, 그 계산 (쐐기 곱) 은 팀이 이미 일부 했다.
4. ★ **호몰로지 차원과 셀 모델의 하한** [증명]: $\tilde H_k(Y)\ne0$ 이면 $Y$ 의 임의 CW 모델은 차원 $\ge k$ 셀을 가진다. $C_6$ 에서 $\tilde H_2\ne0$ 이므로 차원 $\le1$ 모델은 없다 (동변 모델이든 아니든). 대응: P12 (매칭 트리 상계) 반증.
5. 이산 모스 매칭 트리 (Bousquet-Mélou–Linusson–Nevo 2009) [기억-미검증]: 독립 복합체의 임계 셀. 시험은 하지 않았다. 4번에 의해 $\operatorname{zig}$ 상계로는 쓸 수 없다.
6. Sturm 진동 정리 (경로 Jacobi 행렬의 $k$ 번째 고유벡터는 부호 변화 $k-1$ 개) [기억-미검증]: 런 수를 부호 변화로 읽는 번역을 제안하지만, 이 보고서에서 $\operatorname{zig}$ 와의 연결은 증명하지 못했다 [망상].

## 예측 목록 (반증 가능; 시험 결과는 다음 절)
| # | 한 줄 주장 | 이유 (분야) | 검증 방법 (작은 예) | 결과 |
|---|---|---|---|---|
| P1 | 우월 정점 $a$ 에 대해 $\operatorname{zig}(G)=\operatorname{zig}(G-a)$ | 동변 사상 (O3) | $C_5$+pendant, $P_4$, $K_{1,3}$+간선, $C_7$+pendant, $C_5$+거짓쌍둥이 | **확인** (증명 포함) |
| P2 | $\operatorname{zig}(G)\ge1+\max\{k:\tilde H_k(X(G))\ne0\}$ | 호몰로지 차원 상계 | $C_6$ | **반증됨** ($\operatorname{zig}=2$, $\tilde H_2=\mathbb Z^2$) |
| P3 | 비이분 $G$ 에서 $\tau(G)=1+\max\{k:\tilde H_k(X(G))\ne0\}$ | 구면형 패턴 | $K_3$(top 2, $\tau=3$), $K_4$(3), $K_5$(4), $C_5$(2), $C_7$(2), $\overline{C_7}$(2, $\tau=3$), $C_5[K_2]$(3, $\tau=4$), $V_8$(2, $\tau\le\operatorname{zig}=3$), $W_5$(3, $\operatorname{zig}=4$) | **확인** (알려진 $\tau$ 와 전부 일치; $\tau$ 자체는 팀 기존 값 또는 $\operatorname{zig}$ 상계) |
| P4 | 이분 $G$ 에서는 P3 가 깨진다 | $N(G)$ 의 다중 성분 | $C_6$ ($\tau=2$, top 2) | **$C_6$ 에서 깨짐** (확인) |
| P5 | $K_n$ 의 반대칭 최고 조화류는 $n$ 이 홀수일 때만 | 구면 대척 작용의 부호 | $K_2..K_6$; $K_7$ 미시험 | $K_2..K_6$ **확인**; $K_7$ 예측 반대칭 [추측] |
| P6 | 실수 반대칭 조화 지표 $r^-(G)=\max\{k:\ker L_k^-\ne0\}$ 는 $\tau-1$ 과 같다 | 구면 상계 | $K_4$ ($\tau-1=3$, $r^-$ 없음) | **반증됨** |
| P7 | $\mathbb Z_2$-CW 모델 $X(C_6)$ 은 차원 $\ge2$ | $\tilde H_2\ne0$ | 호몰로지 | **증명** |
| P8 | $\overline{C_7}$: $\operatorname{zig}=3$, 최고 $\tilde H$ 차원 2 | P3 | 계산 | **확인** |
| P9 | 최소 반례는 우월 정점이 없다 | O3 | 논리 | **증명** |
| P10 | $\operatorname{zig}(\text{Petersen})=3$ | 상계 | 국소 탐색 (수학적 하계는 미확인) | **상계 3 확인** [계산 확인]; 최고 $\tilde H$ 차원 2 확인 (P3 와 맞음) |
| P11 | $C_5[K_3]$ 의 최고 $\tilde H$ 차원 $=5$ (P3 로 $\tau=6$) | P3 | $n=15$ 계산 필요 | **미시험** [추측] |
| P12 | 독립 복합체 매칭 트리의 임계 차원 $\le\operatorname{zig}-1$ | 모스 이론 | $C_6$ | **반증됨** (P2 와 증명 4 에서 따름) |

## 시험 결과
- **T1 (P3, P1, 번역)**: 8개 그래프 호몰로지 일치 `r06_t1.py` [계산 확인]. 우월 정점 불변 `r06_t2.py` [계산 확인]. 표는 위 도구 1–2 와 같다.
- **T2 (P2, P4, P12)**: 전 그래프 $\operatorname{zig}$ 와 최고 $\tilde H$ 차원 표 (`r06_t3.py`): 

| 그래프 | $n$ | $\operatorname{zig}$ | 최고 $\tilde H_k(X)$ | 비고 |
|---|---|---|---|---|
| $K_3$ | 3 | 3 | 2 | |
| $K_4$ | 4 | 4 | 3 | |
| $C_5$ | 5 | 3 | 2 | |
| $C_6$ | 6 | **2** | **2** ($\mathbb Z^2$) | P2 반례 |
| $C_7$ | 7 | 3 | 2 | |
| $K_{3,3}$ | 6 | 2 | 1 | |
| $W_5$ | 6 | 4 | 3 | |
| $V_8$ | 8 | 3 | 2 | |
| $\overline{C_7}$ | 7 | 3 | 2 | |
| $C_5[K_2]$ | 10 | $\ge4$ ($\tau=4$ 에서 따름, 상계 미계산) | 3 | $\tilde H_3=\mathbb Z^{10}$ |
| Petersen | 10 | $\le3$ (국소 탐색) | 2 ($\mathbb Z^{11}$) | |

- **T3 (P5, P6, 실수 호지)**: `r06_hodge.py` 결과 (inv, anti) 의 최고 차원: $K_2$ $(1,0)$ at $k=1$; $K_3$ $(0,1)$ at $k=2$; $K_4$ $(1,0)$ at $k=3$; $K_5$ $(0,1)$ at $k=4$; $K_6$ $(1,0)$ at $k=5$; $C_5$ $(0,1)$ at $k=2$; $C_6$ 은 $k=2$ 에서 $(1,1)$; $\overline{C_7}$ $(0,1)$ at $k=2$. **패리티 현상 확인, 실수 지표 반증됨.**
- **T4 (zig 상계 탐색)**: `r06_zigsearch.py` 의 국소 탐색으로 $\operatorname{zig}(\text{Petersen})\le3$, $\operatorname{zig}(C_7)\le3$ 확인 (상계만).
- **T5 (반례 탐색 결과)**: $\tau=\operatorname{zig}$ 의 반례는 나오지 않았다. 호지 쪽 "상식"이 깨진 것은 호몰로지 차원 번역 (C_6) 과 실수 부호 분해 (K_4) 뿐이며, 둘 다 $\tau$ 나 $\operatorname{zig}$ 의 값을 바꾸지 않는다.
- **정직한 한계**: $\tau$ 의 값은 팀 기존 계산 또는 $\operatorname{zig}$ 상계에서 가져왔다. 독자적인 $\operatorname{coind}$ 하계 계산은 하지 않았다. P11 은 계산 비용 때문에 미시험이다. 현수 보조정리 (도구 1) 의 일반 증명과 Engström 식 fold 의 문헌 확인도 없다.

## 문주님께 요청
- 없음. (선택 사항: 이산 호지 쪽 현수 보조정리의 출처 — Barmak 의 독립 복합체 책 또는 Nagel–Reiner 논문 — 이 있으면 도구 1 을 [증명] 으로 승격할 수 있다. 없어도 진행 가능.)

## 후속연구 지점
1. **$\mathbb F_2$ Stiefel–Whitney 높이를 $X(G)$ 위에서 직접 계산 (P3 의 $\tau-1$ 과 비교).** 이유: 실수 호지 분해는 코호몰로지 링을 못 보므로 (T3), $\mathbb F_2$ 의 $w_1^k\ne0$ 판정이 유일한 호지 쪽 $\operatorname{coind}$ 하계 도구다. 우선순위 1: 이것이 P3 를 하계 쪽에서 확인하면 $\tau$ 의 값이 호몰로지로 정해지는지 알 수 있다. 시작: $X(G)$ 의 면 위에 $\mathbb F_2$ 쐐기 곱을 구현하고 $G/\mathbb Z_2$ 의 $H^*$ 에서 $w^k$ 를 찾는다 (작은 예 $C_5$, $\overline{C_7}$, $W_5$). 난점: 단체 쐐기 곱의 순서 의존성, 계산량.
2. **P3 를 비이분 $C_5[K_3]$ 로 시험 (P11).** 이유: $\tau(C_5[K_m])=2m$ 추측의 $m=3$ 경우이고, 최고 $\tilde H$ 차원 예측 5 가 맞으면 P3 가 블로업 족에서도 지지된다. 시작: $n=15$ 면 구성을 희소 행렬 랭크 (mod p) 로, `r06_lib.B0_empty` 를 바꿔 쓴다. 난점: 면 수 (약 $10^5$) 와 파이썬 소거. 전용 희소 소거가 필요하다.
3. **$\operatorname{zig}$ 가 $N(G)$ 의 호몰로지 형으로 정해지는가 (O2 의 역).** 이유: $\tau$ 는 $N(G)$ 의 $\mathbb Z_2$-호모토피 형의 함수이므로, 같은 $N(G)$ 를 주는 두 그래프에서 $\operatorname{zig}$ 가 다르면 $\tau\ne\operatorname{zig}$ 의 반례 후보다 (단 $\tau$ 가 $N$ 의 동변 형으로만 정해진다는 것도 확인해야 한다). 시작: 우월 정점 축약 후의 최소 그래프족 (fold-free) 에서 $N(G)$ 가 같은 쌍을 찾는다. 난점: 동변 현수 보조정리의 증명 (지금은 비동변 판만 계산됨).
4. **$\operatorname{zig}$ 의 $L^2$ 판 (Sturm/Dirichlet) 정의.** 이유: 런 수 $=1+\|\delta f\|_1$ 이므로 $L^1$ 최소화를 $L^2$ 디리클레 에너지로 바꾸면 고유값 번호가 부호 변화 번호가 된다 (Sturm). 이 판이 $\operatorname{zig}$ 와 같은 값을 주는지 보면 호지 쪽 등식 후보가 생긴다. 시작: 경로 위 라벨의 에너지와 부호 변화의 관계를 작은 예 (길이 5–7) 에서 계산. 난점: 이것은 [망상] 단계이고 $\tau$ 와의 연결은 아직 없다.
5. **반례꾼 공격 대상 정리.** 이유: O2 (현수 보조정리 동변성), O3 (동변 우월 사상의 단체성) 가 이 보고서의 증명 중 가장 약한 부분이다. 시작: $\varphi$ 의 정의역에서 $a\in A$, $c\in A$ 인 면 (그 면의 상이 실제로 면인지) 을 직접 확인. 난점: 없음 (확인 가능).
