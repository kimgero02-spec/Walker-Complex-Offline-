# [R15-researcher2] 공격: zig 정점 분할 가법 $\operatorname{zig}(G)\le\sum_i\max(1,\operatorname{zig}(G[V_i]))$

- 작성자·라운드·역할: researcher2 / 라운드 15 / 연구원2 (독립 공격). 연구원1 결과 미참조.
- 대상: 정점 분할 $V=\bigsqcup_i V_i$ 에 대해 $\operatorname{zig}(G)\le\sum_i\max(1,\operatorname{zig}(G[V_i]))$. 이것이 R14 의 "zig≤3 블록 k 개 ⇒ τ≤3k" 경로의 zig 쪽 근거다.
- 정의 (R04 명제 O): $\operatorname{zig}(H)=\min_\sigma\max_{(A,B)}\operatorname{runs}(\sigma|_{A\cup B})$, $(A,B)$ 는 $A,B\ne\emptyset$, $A\cap B=\emptyset$, $A\times B\subseteq E(H)$ (완전이분쌍). $\operatorname{runs}$ 는 라벨 $a/b$ 열의 최대 연속 구간 수.
- 표기: `[증명]` `[계산 확인]` `[추측]` `[망상]` `[기억-미검증]`.

## 요약
1. **[증명] 가법은 정점 분할에서 성립한다.** 블록별 최적 순서를 이어 붙이면, $G$ 의 모든 완전이분쌍의 런 수가 블록 런 수의 합 이하다. 교차 간선은 증명에 필요하지 않다 (완전이분쌍의 블록 제한이 블록의 완전이분쌍이라는 사실만 쓴다).
2. **[증명] 깨지는 최소 반례는 없다.** 위 증명이 모든 $G$ 와 모든 분할에 대해 성립하므로 반례는 존재하지 않는다. "교차 패턴이 최적 순서를 방해한다" 는 우려는 증명 구조상 생기지 않는다: 순서는 블록마다 독립으로 고르고, 교차 패턴은 완전이분쌍의 집합을 정할 뿐 런 상계를 바꾸지 않는다.
3. **[증명] 주의 조건 두 개.** (a) 한쪽만 있는 제한 (one-sided) 은 런 1 이므로 규약 $\max(1,\cdot)$ 가 필요하다 (간선 없는 블록). (b) 같은 식이 **간선 분할** 에서는 성립하지 않는다 (R07 기록: $K_6=\mathrm{Oct}\cup 3K_2$, $6>3+2$). 정점 분할과 간선 분할을 혼동하면 안 된다.
4. **[증명] tight 예.** $K_{4k}$ ($k$ 개 $K_4$ 블록, $\operatorname{zig}=4k$), $K_{3k}$ ($k$ 개 $K_3$, $\operatorname{zig}=3k$), $K_{3,3}$ (두 독립 3-집합 블록, $\operatorname{zig}=2=1+1$). 모두 등호.

## 1. 보조 정리: 런 수의 이어붙임
**보조정리 1.** 단어 $w=w_1w_2\cdots w_k$ (빈 조각 허용) 에 대해 $\operatorname{runs}(w)\le\sum_i\operatorname{runs}(w_i)$ (빈 조각의 런은 0).
증명: $m$ 개의 비어 있지 않은 조각을 두자. $\operatorname{runs}(w)=1+\#\{\text{변화}\}$. 변화는 조각 내부 변화 $\sum(\operatorname{runs}(w_i)-1)$ 와 조각 경계 변화 (최대 $m-1$) 의 합이다. 따라서 $\operatorname{runs}(w)\le1+\sum(\operatorname{runs}(w_i)-1)+(m-1)=\sum\operatorname{runs}(w_i)$. ∎

## 2. 정리: 정점 분할 가법
**정리 2 [증명].** $V=\bigsqcup_{i=1}^kV_i$ 이면 $\operatorname{zig}(G)\le\sum_i\max(1,\operatorname{zig}(G[V_i]))$.
증명: 각 $i$ 에서 $\operatorname{zig}(G[V_i])$ 를 달성하는 순서 $\sigma_i$ 를 고르고 $\sigma=\sigma_1\sigma_2\cdots\sigma_k$ (블록 순서대로 이어붙임) 를 쓴다. $G$ 의 임의의 완전이분쌍 $(A,B)$ 를 잡는다.
- 각 $i$ 에서 $A_i=A\cap V_i$, $B_i=B\cap V_i$ 는 $A_i\times B_i\subseteq E(G[V_i])$ 이다 (부분집합의 완전성 상속).
- $A_i,B_i$ 가 모두 비어 있지 않으면 $(A_i,B_i)$ 는 $G[V_i]$ 의 완전이분쌍이므로 그 런 수는 $\le\operatorname{zig}(G[V_i])$ (σ_i 의 선택).
- 한쪽만 비어 있지 않으면 그 조각의 런 수는 1 $\le\max(1,\cdot)$.
- $\sigma$ 에 제한한 $A\cup B$ 의 라벨 열은 조각별 열의 이어붙임이므로 보조정리 1 로 $\operatorname{runs}\le\sum_i\max(1,\operatorname{zig}(G[V_i]))$.
모든 $(A,B)$ 에 대해 성립하므로 $\operatorname{zig}(G)\le$ 우변. ∎

**보조 확인 [증명].** 교차 간선이 많아져 $(A,B)$ 가 늘어나도 정리 2 의 우변은 바뀌지 않는다 (우변은 블록만 쓴다). 따라서 "교차 패턴이 순서를 방해" 하는 경우는 존재하지 않는다: 정리 2 는 교차 패턴에 대해 균일하다.

## 3. 공격 시도와 결과
| 시도 | 대상 | 결과 | 표기 |
|---|---|---|---|
| 간선 분할 가법 | $K_6=\mathrm{Oct}\cup3K_2$ | 깨짐 ($6>3+2$) — 정점 분할이 아니므로 범위 밖 | [계산 확인] |
| 정점 분할, 블록 4+1 | $K_5$ | $5\le4+1$ 등호 | [계산 확인] |
| 정점 분할, 3+3 | $K_6$ | $6\le3+3$ 등호 | [계산 확인] |
| 정점 분할, 두 독립 3-집합 | $K_{3,3}$ | $2\le1+1$ 등호 (one-sided 규약 필요) | [계산 확인] |
| 정점 분할, 2+3 | $C_5$ | $3\le2+2$ | [계산 확인] |
| "+1" 형 $\operatorname{zig}\le\max\operatorname{zig}_i+1$ | $K_4=K_2\sqcup K_2$ | $4>3$ 깨짐 — 합 형태만 맞다 | [증명] |

- 손으로 한 계산은 모두 $(A,B)$ 의 열거와 정리 2 의 부등식으로 확인했다. 대량 점검은 하지 않았다.

## 4. R14 경로와의 연결 (τ ≤ 3k)
- 정리 2 와 $\tau\le\operatorname{zig}$ (R03/R04 프로젝트 증명, 모멘트 곡선 + Borsuk–Ulam, 본 보고서는 재검증하지 않음) 로 $\tau(G)\le\sum_i\max(1,\operatorname{zig}(G[V_i]))$ 를 얻는다.
- 따라서 "zig≤3 인 블록 $k$ 개 ⇒ $\tau\le3k$" 는 정리 2 의 결과이다 [증명]. 이 경로의 zig 쪽 근거는 건전하다.
- 남은 의존: $\tau\le\operatorname{zig}$ (프로젝트 기존 결과 인용). 이것이 틀리면 경로 전체가 무너진다. 본 보고서에서 독립 재검증은 하지 않았다.

## 5. 판정
| 명제 | 판정 | 표기 |
|---|---|---|
| 정점 분할 zig 가법 (max(1,·) 규약) | 증명, 반례 없음 | [증명] |
| 간선 분할 zig 가법 | 거짓 ($K_6$) | [계산 확인] |
| tight 족 $K_{4k}$, $K_{3k}$ | 등호 | [증명] |
| $\tau\le3k$ (zig≤3 블록) | 정리 2 + $\tau\le\operatorname{zig}$ 로 성립 | [증명] (τ≤zig 인용) |

## 문주님께 요청
없음.

## 후속연구 지점
1. **$\tau\le\operatorname{zig}$ 의 독립 재검증 (우선순위 1).** 이유: 정리 2 가 맞아도 τ 상계는 이 한 부등식에 달려 있다. 시작: 모멘트 사상 $B_0\to\mathbb R^{d+1}\setminus0$ 의 존재를 Gale 보조정리 (런 $\le d+1$ 이면 분리) 로 재확인하고, 단사성 없이 $\mathbb Z_2$-사상만 쓰는지 본다. 난점: Gale 보조정리의 역방향 증명 세부.
2. **정점 분할 zig 가법의 등호 조건.** 이유: tight 족 $K_{4k}$, $K_{3k}$ 외의 등호 조각을 알면 τ 상계의 최적 분할을 고를 수 있다. 시작: 등호가 성립하려면 블록 순서의 경계에서 런이 합쳐지지 않아야 한다는 조건을 정식화. 난점: 최적 순서가 여럿일 때 등호 판정이 어렵다.
3. **zig≤3 블록의 구조.** 이유: 경로의 블록 조건 "zig≤3" 은 평면 조건보다 강하지 않다 ($K_4$ 는 평면이지만 zig=4). 시작: zig≤3 인 그래프의 금지 구조 (완전이분 $K_{2,2}$? 등) 를 찾고, $\overline{C_7}$ 과 $C_5$ 가 이 클래스에 속함을 이용한다. 난점: 금지 마이너 조건이 zig 에 단조적인지 불명 (zig 는 부분그래프에 단조이지만 마이너에는 아님).
