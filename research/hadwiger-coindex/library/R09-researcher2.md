# [R09-researcher2] 평면 블록 시트 정의의 검증: 정점 시트 (V) 와 간선 시트 (E), 그리고 τ 블록 합 법칙의 지위

- 작성자·라운드·역할: researcher2 / 라운드 9 / 연구원2 (정의 검증). 대상: 연구원1 의 정의 후보. R09 중간본 `R09-researcher1-interim.md` 는 제출 시점에 도서관에 없었다. 대신 `R08-researcher1.md` (후보 $\alpha$–$\gamma$, $\iota$ 판) 와 `R08-researcher3.md` (P1 주장) 를 검증 대상으로 삼았다.
- 정의 (검증 대상): **V (정점 시트)** $V=\bigsqcup_{i}V_i$, 각 $G[V_i]$ 평면. **E (간선 시트)** $E=\bigsqcup_i E_i$, 각 $(V,E_i)$ 평면.
- 계산 코드: `rooms/researcher2/r08/` (`zig_small.py`, `zig_dfs.py`, `planar_base.py`). 이번 라운드 새 코드는 `planar_base.py` 하나. 그래프 구성 오류 (R08 의 C_5[K_2] 간선 누락) 는 R08 에서 수정했다.
- 표기: 모든 주장에 `[증명]` `[계산 확인]` `[추측]` `[망상]` `[기억-미검증]` 중 하나. 프로젝트 기존 결과는 인용으로 표시.

## 요약
1. **[증명] V 의 ι 부분가법.** $\iota(G):=\operatorname{ind}(B_0G)+1$ 로 두면 $\iota(G)\le\sum_i\iota(G[V_i])$. 핵심: $B_0(G)\subseteq *_i B_0(G[V_i])$ (ind 는 부분복합체에 단조) 이고 조인의 사상은 동변. **R08-r3 의 P1 은 이 ι 판으로만 증명되며, τ 판 (coind) 으로 옮겨 쓴 것은 오류다.** coind 는 조각에 대해 단조 상계가 없어 옮길 수 없다. τ 판 부분가법은 R08-r1 의 조인 상계 $J$ 와 동치 [증명] 이며 $J$ 는 **열림 [추측]**. 두 보고서의 충돌은 R08-r1 이 맞다.
2. **[증명] V 의 평면 함의.** $\tau\le\iota\le\chi\le 4k$ (평면 조각 $k$ 개). $K_{4k}$ 에서 tight. 새 정보 없음 (χ 와 같은 강도).
3. **[반례] E 의 가법 법칙.** $K_6=\mathrm{Oct}\cup 3K_2$ (두 층 모두 평면): $\tau(K_6)=6>3+2$, $\operatorname{zig}(K_6)=6>3+2$. E 로는 τ 나 zig 의 합 상계를 얻을 수 없다. E 의 쓸모 있는 함의는 $\chi\le 6\theta$ [증명] 뿐이다.
4. **[반례] 평면 블록의 τ 상계 $3k$.** 평면 $K_4$ 는 $\tau=4$. 따라서 "평면 블록 $k$ 개면 $\tau\le 3k$" 는 거짓 (k=1). 올바른 블록 불변량은 평면성이 아니라 $\operatorname{zig}$ (또는 $\iota$) 이다: $\operatorname{zig}\le3$ 인 블록 $k$ 개면 $\tau\le 3k$ [증명], $K_{3k}$ 에서 tight.
5. **[확인] 작은 예 시험.** $K_5$ (4+1), $K_6$ (3+3), $K_6$ (4+2) 는 τ 블록 합에서 tight. $C_5[K_2]$ 의 2-분할은 모두 $\sum\tau_i\ge4$ 이라 반례가 될 수 없다 (분할 시험은 간극을 가리지 못함). J 를 실제로 시험하려면 조각의 $\iota=\tau$ 가 필요하고, $C_5[K_2]+C_5[K_2]$ 에서 $\tau=8=4+4$ [증명] 으로 J 가 성립한다.
6. **[확인] 평면 기초값.** $\tau(K_3)=3$, $\tau(K_4)=4$, $\tau(\text{외평면, 비이분}) = 3$, $\tau(K_{2,3})=2$ [증명]. $\operatorname{zig}$ 는 각각 3, 4, 3, 2 [계산 확인].

## 검증 표 (정의 | 함의 | 판정 | 근거 | 표기)

| 정의 | 함의 | 판정 | 근거 | 표기 |
|---|---|---|---|---|
| V: $\tau(G)\le\sum\tau(G[V_i])$ (B 판 τ 부분가법) | τ 블록 합 | **열림 (J 와 동치)** | 정리 4 (R08-r1): $\iff$ $\tau(G_1+G_2)\le\tau_1+\tau_2$. J 증명 없음 | [추측] |
| V: $\iota(G)\le\sum\iota(G[V_i])$ | ι 블록 합 | **증명** | $B_0(G)\subseteq *_iB_0(G[V_i])$ (ind 단조); 조인 사상 $*f_i$ 동변; $\operatorname{ind}(*_iB_0)\le\sum(n_i+1)-1$ | [증명] |
| V: $\tau\le\iota\le\min(\chi_i,\operatorname{zig}_i)$ 블록 합 | χ, zig 부분가법 재증명 | 증명 | 보조정리 3 ($\iota\le\chi$), R04 ($\iota\le\operatorname{zig}$) | [증명] (R04 인용) |
| V: 평면 블록 $k$ 개 $\Rightarrow\tau\le 4k$ | τ 상계 | 증명, tight | $\iota\le\chi\le4$ (4색정리 인용), $K_{4k}=kK_4$ 에서 $\tau=4k$ | [증명] |
| V: 평면 블록 $k$ 개 $\Rightarrow\tau\le 3k$ (R07/R08 의 제안) | τ 상계 | **반례** | $K_4$ (k=1, 평면): $\tau=4>3$ | [증명] |
| V: $\operatorname{zig}\le3$ 블록 $k$ 개 $\Rightarrow\tau\le3k$ | τ 상계 | 증명, tight | $\tau\le\operatorname{zig}$ + zig 블록 합 $\operatorname{zig}(G)\le\sum\max(1,\operatorname{zig}_i)$; $K_{3k}=kK_3$ | [증명] |
| V: 블록 $\tau$ 의 $\max+1$ 상계 | τ | **반례** | $K_4=K_2\sqcup K_2$: $4>2+1$; $K_5=K_2\sqcup K_3$: $5>4$ | [증명] |
| E: $\tau(G)\le\sum\tau(E_i)$ | τ 층 합 | **반례** | $K_6=\mathrm{Oct}\cup 3K_2$: $\tau(\mathrm{Oct})=3$ ($K_3\subseteq\mathrm{Oct}$, $\chi=3$), $\tau(3K_2)=2$, $\tau(K_6)=6$ | [증명] |
| E: $\operatorname{zig}(G)\le\sum\operatorname{zig}(E_i)$ | zig 층 합 | **반례** | $\operatorname{zig}(K_6)=6$, $\operatorname{zig}(\mathrm{Oct})=3$, $\operatorname{zig}(3K_2)=2$ | [계산 확인] |
| E: $\chi(G)\le 6\theta$ | χ, τ, ι 상계 | 증명 | $|E|\le\theta(3n-6)$ 이므로 평균 차수 $<6\theta$, 퇴화도 $\le 6\theta-1$, 귀납 색칠 | [증명] |
| E: $\chi\le 4^\theta$ | χ 상계 | 증명 (약함) | 층별 4색의 곱 색칠 | [증명] |
| 조인 하한 $\tau(G_1+G_2)\ge\tau_1+\tau_2$ | τ 하한 | 증명 | $B_0(G_1+G_2)=B_0(G_1)*B_0(G_2)$, 조인 사상 $S^p*S^q=S^{p+q+1}$ | [증명] |
| J: $\tau(G_1+G_2)\le\tau_1+\tau_2$ | 조인 상계 | **열림** | 조각이 $\iota=\tau$ 이면 증명 ($\tau\le\iota\le\sum\iota_i$). 일반 조각은 $\operatorname{coind}$ 조인 상계가 필요 | [추측] |

## 본문

### 1. 충돌의 해소: ι 판과 τ 판
- **ind 와 coind 의 방향.** $\operatorname{ind}(X)$ 는 동변 사상 $X\to S^n$ 의 최소 $n$, $\operatorname{coind}(X)$ 는 $S^n\to X$ 의 최대 $n$. 부분복합체 $X'\subseteq X$ 에 대해 $\operatorname{ind}X'\le\operatorname{ind}X$ (사상 제한) 이지만 $\operatorname{coind}X'\le\operatorname{coind}X$ (포함 합성). 두 방향 모두 단조이므로, **ind 는 "블록을 포함하는 큰 조인" 쪽으로 상계를 준다.**
- **[증명] 정리 A (ι 블록 합).** $\iota(G)\le\sum_i\iota(G[V_i])$. 증명: $\sigma\in B_0(G)$ 는 $(A\cap V_i,B\cap V_i)_i$ 로 분해되고 각 조각은 $B_0(G[V_i])$ 의 면이다. 따라서 $B_0(G)\subseteq *_iB_0(G[V_i])$. 각 $f_i:B_0(G[V_i])\to S^{n_i}$ ($n_i=\operatorname{ind}$) 의 조인 $*f_i$ 는 대각 대척 작용과 호환되는 동변 사상 $*_iB_0(G[V_i])\to*_iS^{n_i}=S^{\sum(n_i+1)-1}$. 제한하면 $\operatorname{ind}B_0(G)\le\sum(n_i+1)-1$. ∎
- **[증명] 정리 B (τ 판은 J 와 동치, R08-r1 정리 4).** (i) 모든 분할에 대해 $\tau(G)\le\sum\tau(G[V_i])$ $\iff$ (ii) 모든 $G_1,G_2$ 에 대해 $\tau(G_1+G_2)\le\tau_1+\tau_2$. (i)⇒(ii) 는 분할 $V(G_1)\sqcup V(G_2)$ 를 $G_1+G_2$ 에 적용. (ii)⇒(i) 는 $G\subseteq G[V_1]+\cdots+G[V_k]$ 와 단조성 $\tau(G)\le\tau(G')$, 그리고 $k-1$ 번의 J.
- **왜 R08-r3 의 P1 증명은 τ 판으로 옮겨지지 않는가.** 그 증명은 정리 A 와 같은 조인 보조정리이며 결론은 $\operatorname{ind}$ 로 쓰인다 (보고서의 "$\operatorname{ind}$ 의 덮개 부분가법"). $\tau=\operatorname{coind}+1$ 로 바꾸려면 $\operatorname{ind}(B_0G[V_i])=\operatorname{coind}(B_0G[V_i])$ 가 조각마다 필요하다. 이것은 증명되지 않았다 (R08-r1 의 장애물과 같다). 따라서 P1 은 **ι 판 증명 + τ 판 열림** 으로 정정해야 한다.

### 2. 작은 예 시험 (정리 B 의 J 를 실제로 본다)
| $G$ | 분할 | $\tau(G)$ | $\sum\tau_i$ | $\sum\iota_i$ | 판정 |
|---|---|---|---|---|---|
| $K_5$ | $K_4\sqcup K_1$ | 5 | 4+1 = 5 | 4+1 = 5 | tight [증명] |
| $K_5$ | $K_2\sqcup K_3$ | 5 | 2+3 = 5 | 5 | tight [증명] |
| $K_6$ | $K_3\sqcup K_3$ | 6 | 3+3 = 6 | 6 | tight [증명] |
| $K_6$ | $K_4\sqcup K_2$ | 6 | 4+2 = 6 | 6 | tight [증명] |
| $C_5[K_2]$ | 2-분할 (모든 경우) | 4 | $\ge4$ | $\ge4$ | 반례 아님. 근거: $\tau_i\in\{1,2\}$ 이면 블록은 각각 독립집합 또는 이분. 차 합 $\le3$ 인 분할은 $\chi\le3$ 을 준다 (독립집합 1 개 + 이분 1 개, 또는 독립집합 3 개), 모순 [증명] |
| $C_5[K_2]+C_5[K_2]$ | 조인 (두 블록) | $\ge8$ | 4+4 = 8 | 4+4 = 8 | J 성립 [증명]: $\tau\ge8$ (조인 하한), $\tau\le\iota\le\sum\iota_i=8$ ($\iota(C_5[K_2])=\tau=4$, $\operatorname{zig}=4$ [계산 확인]) |
| $K_{3,3}$ | 두 독립 3-집합 | 2 | 1+1 | 1+1 | tight [증명] |

- 해석. 작은 예 모두 J 와 부합한다. 그러나 $\iota\neq\tau$ 인 조각이 없으면 J 는 시험되지 않는다. 현재 $\iota>\tau$ 인 그래프를 알지 못한다. 따라서 "τ 판 부분가법은 증명됨" 이라는 주장은 **작은 예로 뒷받침되는 추측** 이다.
- $C_5[K_2]$ 블록 분할 주의: R08-r3 의 표 "블록 $\{0,1\}$: $\tau=2$" 는 틀렸다. 블록 $\{0,1\}$ 은 두 블랍 (각각 $K_2$) 의 합집합 $K_4$ 이므로 $\tau=4$ [증명]. 그 표의 "$4\le2+2$" 는 성립하지 않는 계산이다 (실제로는 $4\le4+\tau(P_3[K_2])$ 로 무의미).

### 3. 평면 블록의 기초값
| 그래프 | 평면? | $\chi$ | $\tau$ | $\operatorname{zig}$ | 근거 |
|---|---|---|---|---|---|
| $K_3$ | 예 | 3 | 3 | 3 | $B_0(K_3)=S^2$ [증명]; zig 완전 탐색 [계산 확인] |
| $K_4$ | 예 | 4 | 4 | 4 | $B_0(K_4)=S^3$ [증명]; zig [계산 확인] |
| 외평면, 비이분 (예: $C_5$, 팬 $F_{1,4}$) | 예 | 3 | 3 | 3 | $\chi\le3$ (외평면 3색, 표준 [증명]); 홀수 사이클 $\subseteq$ 이므로 $\tau\ge\tau(C_5)=3$ [증명]; zig 팬 3, $C_5$ 3 [계산 확인] |
| 외평면, 이분 (예: $P_n$) | 예 | 2 | 2 | 2 | 이분이고 간선 있음 [증명] |
| $K_{2,3}$ | 예 | 2 | 2 | 2 | 이분, 간선 있음 [증명]; zig 2 [계산 확인] |

- 일반 사실: 평면 블록의 $\tau\le4$ (χ). 등호 $\tau=4$ 는 $K_4$ 가 달성한다 [증명]. 따라서 평면 블록 하나는 τ 를 4 까지 올릴 수 있다. 3 으로 제한하는 것은 "외평면" 이나 "$\operatorname{zig}\le3$" 같은 더 강한 조건이 필요하다 [증명].

### 4. V 와 E 의 최종 판정
- **V (정점 시트).** 쓸모 있는 것은 τ 블록 합의 ι 판 (정리 A) 과 $\tau\le4k$ 이다. $\tau\le 4k$ 는 $\chi\le 4k$ 와 같은 정보이다 (tight). 평면이라는 조건으로는 τ 를 더 줄일 수 없다 ($K_4$). **쓸모 있는 강화는 평면 대신 $\operatorname{zig}\le3$ (또는 $\iota\le3$) 조각**이다: $\tau\le3k$ [증명]. 이 경우 $\operatorname{zig}\le3$ 인 그래프는 $K_4$ 를 포함하지 않으므로 평면 조건과 다르다 ($K_4$-마이너 없음 vs 평면).
- **E (간선 시트).** τ 와 zig 의 층 합이 모두 거짓. 함의는 $\chi\le6\theta$ 뿐이다. 간선 시트는 τ 법칙의 도구로 쓸 수 없다.

## 문주님께 요청
없음.

## 후속연구 지점
1. **J (τ 조인 상계) 의 증명 또는 반례 (우선순위 1).** 이유: 정리 B 로 τ 블록 합 법칙과 동치이며, V 정의에서 τ 판을 얻는 유일한 빈칸이다. 시작: $X=B_0(G_1)$, $Y=B_0(G_2)$ 에 대해 $\operatorname{coind}(X*Y)\le\operatorname{coind}X+\operatorname{coind}Y+1$ 을 시험. 특히 $\iota=\tau$ 가 아닌 조각이 필요하므로 $\operatorname{ind}>\operatorname{coind}$ 인 $B_0$ 를 찾는 것이 핵심. 난점: 자유 $\mathbb Z_2$-복합체의 coind 조인 상계는 일반적으로 알려져 있지 않다 [기억-미검증].
2. **$\iota\ne\tau$ 인 $B_0$ 찾기 (간극 탐지).** 이유: J 가 깨질 가능성은 $\iota>\tau$ 인 조각에서만 나온다. 시작: $\tau<\operatorname{zig}$ 이거나 $\tau<\chi$ 인 소형 그래프 (예: $C_5[K_2]+K_1$, $\tau=5<\chi=6$ 은 $\iota$ 로 이미 5 로 잠김) 에서 $\iota$ 를 계산할 도구를 찾는다. 난점: 정확한 $\operatorname{ind}$ 계산 도구가 없다.
3. **$\operatorname{zig}\le3$ 블록의 구조 (V 의 강화 후보).** 이유: $\tau\le3k$ 를 주는 유일한 후보. 평면 $\Rightarrow$ $\operatorname{zig}\le3$ 는 거짓 ($K_4$). 핵심 질문: $\operatorname{zig}\le3$ 인 그래프에서 $\tau\le3$ 인가? 시작: $\operatorname{zig}\le3$ 인 소형 그래프 족 (외평면, $C_{10}^2$ 류 $\chi=4$ 후보) 과 Grötzsch (χ=4) 의 zig 값. 난점: $\operatorname{zig}\le 3$ 판정은 조합적으로 강해 탐색이 빠르게 커진다.
4. **E 의 쓸모를 찾는 대안: 층별 조인 구조.** 이유: 간선 층 합이 실패하므로 E 는 χ 경로로만 쓰인다. 간선 시트 중 "교차 완전" (조인) 인 것만 법칙을 준다 (정리 B). 시작: 간선 분할이 정점 분할과 맞물리는 혼합 정의 (블록 안은 평면, 블록 사이는 완전) 를 정의하고 J 와 비교. 난점: 혼합 정의가 V 와 같은 정보만 줄 수 있다.
