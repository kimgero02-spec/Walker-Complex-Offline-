# [R08-researcher1] 시트 평면 분해의 정의 설계: 정점 시트의 $\iota$-버전과 $\tau$ 부분가법

- 작성자·라운드·역할: researcher1 / 라운드 8 / 연구원1 (정의 설계). 중간본: `R08-researcher1-interim.md`.
- 표기: 모든 주장에 `[증명]` `[계산 확인]` `[추측]` `[망상]` `[기억-미검증]` 중 하나. 업로드 논문 두 편은 검증하지 않고 인용만 했다 (문주님 지시).
- 계산 도구: `rooms/researcher1/r08_zig.py` (무작위 탐색으로 $\operatorname{zig}$ 상계), `r08_mult.py`, `r08_bip2.py` (유도 이분 2분할 전수). `networkx` 가 이 환경에 없어 평면성 판정은 손으로 했다.
- 정의: $B_0(G)$ 는 면 $(A,B)$, $A\times B\subseteq E$ 의 복합체 ($A,B$ 중 하나는 공집합 가능, $\mathbb Z_2$ 는 두 복사본 교환). $\tau=\operatorname{coind}(B_0)+1$, $\operatorname{zig}=\rho$ (선형순서의 극대 완전이분쌍 런 수의 최솟값, R04 명제 O). 증명된 사슬 $\operatorname{cd}\le\tau\le d_R+1\le\operatorname{zig}\le\chi$ 는 STATUS 인용.

## 요약
1. **[증명] 정점 시트의 $\iota$-버전.** $\iota(G):=\operatorname{ind}(B_0G)+1$ (ind = 최소 $n$, $\mathbb Z_2$-사상 $B_0\to S^n$) 로 정의하면 $\tau\le\iota\le\min(\operatorname{zig},\chi)$ 이고, 임의의 정점 분할에 대해 $\iota(G)\le\sum_i\iota(G[V_i])$ 가 **증명된다**. 핵심은 $B_0(G)$ 가 조각들의 $B_0$ 의 조인에 $\mathbb Z_2$-동변으로 들어간다는 것이다.
2. **[증명] $\tau$ 부분가법은 조인 상계와 동치.** $\tau(G)\le\sum\tau(G[V_i])$ (B 해석 부분가법) $\iff$ $\tau(G_1+G_2)\le\tau(G_1)+\tau(G_2)$ (조인 상계 $J$). 조인에 대해서는 반대 부등식 $\tau(G_1+G_2)\ge\tau_1+\tau_2$ 가 항상 성립한다 [증명]. 따라서 $J$ 가 $\tau$ 판 부분가법의 정확한 남은 내용이며, **$J$ 는 열린 문제 [추측]** 이다. 참이면 $\tau=\iota$ 인 조각들에 대해서는 이미 증명됨.
3. **[증명] 평면 시트 $k$ 개 $\Rightarrow\tau\le4k$** (4색정리 인용, $\iota\le\chi$). 이 상계는 $\chi\le4k$ 와 같은 수준이고 $K_{4k}$ 에서 tight 이므로 **평면 시트 자체로는 새 정보가 없다.** 새 정보는 조각의 $\iota$ 가 $\chi$ 보다 작을 때 (예: $\operatorname{zig}\le3$ 이면서 $\chi=4$ 인 $C_{10}^2$) 에서만 나온다.
4. **판정.** A (간선 두께): $\tau$ 의 합 법칙과 곱 법칙 모두 **거짓** [증명, $K_6=\text{oct}\cup PM_3$: $6>3+2$; $K_{10}=C_{10}(1,2)\cup C_{10}(3,4,5)$: $10>3\cdot3$]. C (책 두께): 페이지가 간선 분할이라 A 의 실패를 물려받음, 조합 상계 $\operatorname{zig}\le2\,\mathrm{bt}$ 는 추측. D (분기 피복): 준동형 단조 $\tau(G)\le\tau(H)$ [증명] 만 남고 합 법칙 없음. **B 가 살아남는다** (정점 시트, $\iota$ 판으로 정의를 바꿔서).
5. **추천 정의 $\alpha$** (정점 시트 $\iota$-버전). 작은 예 $K_5,K_6,K_{3,3}$ 에서 분할 상계가 정확히 닿는다 ($5=4+1$, $6=4+2$, $2=1+1$). $C_5[K_2]$ 는 $\tau=\iota=\operatorname{zig}=4<\chi=5$ 이지만 시도한 분할은 모두 상계 $\ge6$ 이다 (두 유도 이분 조각으로의 분할은 불가능 [계산 확인]).

## 정의 후보

### 후보 $\alpha$: 정점 시트의 $\iota$-버전 (추천)
- **(a) 정의.** $\iota(G):=\operatorname{ind}(B_0G)+1$. 시트 분해는 $V=\bigsqcup_{i=1}^k V_i$ (빈 조각 허용) 이고, 조각 $G[V_i]$ 의 상계 $\operatorname{ub}(G[V_i])\ge\iota(G[V_i])$ 를 쓴다 (예: 평면이면 $\operatorname{ub}=4$, 일반이면 $\operatorname{ub}=\operatorname{zig}$ 또는 $\chi$).
- **(b) 기대 함의.** $\tau\le\iota\le\sum_i\operatorname{ub}(G[V_i])$. 특히 $\tau$ 의 시트 수 상계. $\tau$ 부분가법 (조인 상계 $J$ 가 참이면).
- **(c) 증명 시도 / 장애물.** 부분가법 $\iota(G)\le\sum\iota(G[V_i])$ 는 증명됨 (정리 2 아래). $\tau$ 판은 $\operatorname{coind}$ 와 $\operatorname{ind}$ 의 간극 때문에 막힌다: $\tau\le\iota$ 는 $\operatorname{coind}\le\operatorname{ind}$ 에서 오고, 우변을 $\tau$ 로 바꾸려면 $\operatorname{ind}(B_0H)=\operatorname{coind}(B_0H)$ 가 조각마다 필요하다 (또는 $J$).
- **(d) 작은 예.**
  | $G$ | $\chi$ | $\tau$ | $\iota$ | $\operatorname{zig}$ | 최선 분할 상계 | 판정 |
  |---|---|---|---|---|---|---|
  | $K_5$ | 5 | 5 | 5 | 5 | $K_4\sqcup K_1$: $4+1=5$ | tight [증명] |
  | $K_6$ | 6 | 6 | 6 | 6 | $K_4\sqcup K_2$: $4+2=6$ | tight [증명] |
  | $K_{3,3}$ | 2 | 2 | 2 | 2 | 두 독립 3-집합: $1+1=2$ | tight [증명] |
  | $C_5[K_2]$ | 5 | 4 | 4 | 4 | 시도한 분할 $\ge6$ | 간극 (상계 미달) |

### 후보 $\beta$: 평면 정점 시트 (B 의 원래 형태)
- **(a) 정의.** $p(G):=\min\{k: V=\bigsqcup V_i,\ G[V_i]\text{ 평면}\}$.
- **(b) 기대 함의.** $\tau\le\iota\le4p(G)$ (4색정리). 평면 조각의 $\iota\le4$ 가 전부다.
- **(c) 증명 시도 / 장애물.** $\iota$ 부분가법 + 평면 조각의 $\iota\le4$. 조합적으로 $\iota(H)\le4$ ($H$ 평면) 를 얻으려면 평면 $\Rightarrow Q_3$ (R04 의 열린 목표 W) 가 필요하다. 이 목표가 서면 4색정리 없이 같은 상계가 나온다.
- **(d) 작은 예.** $p(K_5)=2$ ($K_4\sqcup K_1$), $p(K_6)=2$ ($K_4\sqcup K_2$), $p(K_{3,3})=2$ ($K_{2,3}\sqcup K_1$ [증명]), $p(C_5[K_2])=2$ (블록 0–2 의 유도 부분그래프 $K_2+2K_2$ 는 평면, 블록 3–4 는 $K_4$ [증명, 손으로 그림]). 상계는 모두 8 이며 $\tau$ 는 $5,6,2,4$. 평면 시트는 $K_{4k}$ 에서만 tight: $\tau(K_{4k})=4k=4p$ [증명].
- **판정.** 새 정보 없음 ($\chi\le4p$ 와 같다). 살아남는 것은 **구조**: 평면 조각을 $\iota$ 로 읽는 틀과 $Q_3$ 목표와의 연결.

### 후보 $\gamma$: 조인 시트 (교차 완전 분할)
- **(a) 정의.** $G=G_1+\cdots+G_k$ (교차 간선이 전부). $\alpha$ 의 특수형으로 $B_0(G)$ 가 조인과 정확히 같다.
- **(b) 기대 함의.** $\sum\tau_i\le\tau(G)\le\sum\iota_i$. $\tau_i=\iota_i$ 이면 $\tau(G)=\sum\tau_i$ [증명]. $\tau_i=\operatorname{zig}_i$ 이면 $\operatorname{zig}$ 부분가법으로도 $\le\sum\tau_i$ (자명).
- **(c) 증명 / 장애물.** 하한과 $\iota$ 상계는 증명. 상계 $\tau(G)\le\sum\tau_i$ 는 $J$ 와 같다.
- **(d) 작은 예.** $K_5=K_1+K_1+K_1+K_2$: $1+1+1+2=5$ [증명]. $K_{2,2,2}=3\times2K_1$ (옥타헤드론): $\tau=3$ [증명]. $W_5=C_5+K_1$: $\tau=4=\chi$ [증명]. $C_5[K_2]+K_1$: $\tau=5<\chi=6$ [증명, $\tau(C_5[K_2])=\iota=4$]. $K_{3,3}=3K_1+3K_1$: $2$ [증명].
- **판정.** 정확한 법칙이 나오는 가장 깨끗한 형태. 새 그래프 클래스 ($\tau<\chi$ 인 $C_5[K_2]+K_1$) 를 준다.

### 기존 후보 판정 (A, C, D)
- **A (간선 두께 $\theta$).** $\chi\le4^\theta$ 만 남는다. $\tau$ 합 법칙: 거짓 [증명] ($K_6=\text{oct}\cup PM_3$, $\tau(\text{oct})=3$, $\tau(PM_3)=2$, $\tau(K_6)=6$). 곱 법칙: 거짓 [계산 확인] ($K_{10}=C_{10}(1,2)\cup C_{10}(3,4,5)$, 두 조각의 $\operatorname{zig}=3$ 이므로 $\tau\le9<10$). 작은 예 $K_5=(K_5-e)\cup e$: $5\le4+1$ 성립, $C_5[K_2]$: 25 간선 $>24$ 이므로 $\theta\ge2$ [증명]. **탈락** (τ 법칙용으로는).
- **C (책 두께 $\mathrm{bt}$).** 조각이 간선 집합이라 A 의 실패를 물려받는다. $\mathrm{bt}=1\Rightarrow\tau\le3$ [증명] (외평면은 $K_4$-마이너-자유). $\operatorname{zig}\le2\,\mathrm{bt}$ 는 [추측] (작은 값 $K_5$: $5\le6$, $K_6$: $6\le6$ tight). **약하게 생존** (zig 인증서 공급원).
- **D (분기 피복 / 준동형).** $f:G\to H$ 이면 $X(f)$ 가 동변 단체 사상이므로 $\tau(G)\le\tau(H)$, $\iota(G)\le\iota(H)$ [증명]. 예: $K_{3,3}\to K_2$: $2\le2$. 합 법칙 없음. **보조 보조정리로 생존** (정의 후보는 아님).

## 본문

### 1. 기본 보조정리 (정의 $\iota$ 를 쓴다)
- **보조정리 1 [증명] (조인 포함).** $V=\bigsqcup_{i=1}^kV_i$, $G_i=G[V_i]$. 면 $(A,B)$ 에 대해 $(A\cap V_i,B\cap V_i)$ 는 $G_i$ 의 면이고, $(A,B)=\bigsqcup_i(A\cap V_i,B\cap V_i)$ 는 각 조각의 면들의 조인 면이다. 따라서 $B_0(G)\subseteq B_0(G_1)*\cdots*B_0(G_k)$, $\mathbb Z_2$-동변 부분복합체. (교차 조건 $A_i\times B_j\subseteq E$ 는 $B_0(G)$ 를 조인의 진부분으로 만든다.)
- **보조정리 2 [증명] ($\operatorname{coind}\le\operatorname{ind}$).** $\mathbb Z_2$-사상 $S^m\to X\to S^n$ 이 있으면 Borsuk–Ulam 으로 $m\le n$. 따라서 $\tau\le\iota$.
- **보조정리 3 [증명] ($\iota\le\chi$).** 진색칠 $c$ 에 대해 $\phi(v,1)=e_{c(v)}$, $\phi(v,2)=-e_{c(v)}\in\mathbb R^{\chi}$ 로 정의한다. 면 $(A,B)$ 에서 $c(A)\cap c(B)=\emptyset$ (인접 쌍은 색이 다르다). $\sum_{a}\lambda_ae_{c(a)}-\sum_b\mu_be_{c(b)}=0$ 이면 $i\in c(A)$ 좌표에서 $\lambda$ 합이 0 이어야 하므로 $\lambda=0$, 모순. 따라서 $0\notin\operatorname{conv}\phi(\sigma)$ 이고 정규화로 $\mathbb Z_2$-사상 $B_0\to S^{\chi-1}$. $\operatorname{ind}\le\chi-1$, $\iota\le\chi$.
- **보조정리 4 [인용, R04] ($\iota\le\operatorname{zig}$).** $\operatorname{zig}\le d+1$ 이면 R04 모멘트 사상 $g_d:B_0\to\mathbb R^{d+1}\setminus0$ 가 $\mathbb Z_2$-사상이므로 $\operatorname{ind}\le d$, $\iota\le d+1$. (R04 보조정리 G′, 명제 O 에 의존. 나는 재검증하지 않았다.)

### 2. 정리 (정점 시트 부분가법, $\iota$ 판)
**정리 2 [증명].** 임의의 $V=\bigsqcup_{i=1}^kV_i$ 에 대해 $\iota(G)\le\sum_{i=1}^k\iota(G[V_i])$.

*증명.* $n_i:=\operatorname{ind}(B_0G_i)$, $f_i:B_0(G_i)\to S^{n_i}$ 를 $\mathbb Z_2$-사상으로 잡는다. 조인 $f:=f_1*\cdots*f_k:\ *_iB_0(G_i)\to*_iS^{n_i}$ 는 $\mathbb Z_2$-동변 (대각 작용)이고, $*_iS^{n_i}=S^{\sum n_i+k-1}$ (대척 작용과 호환). 보조정리 1 에 의해 $f$ 를 $B_0(G)$ 에 제한하면 $\operatorname{ind}B_0(G)\le\sum n_i+k-1$. 양변에 $+1$: $\iota(G)\le\sum_i(n_i+1)=\sum_i\iota(G_i)$. ∎

*부산물.* 보조정리 3 과 결합: $\tau(G)\le\iota(G)\le\sum_i\min(\chi_i,\operatorname{zig}_i)$. 이는 $\chi$ 와 $\operatorname{zig}$ 의 부분가법을 $\iota$ 판에서 다시 얻은 것이다 (두 번째 것은 $\iota$ 자체가 더 작을 때 더 강하다).

### 3. $\tau$ 판과 조인 상계 $J$
**정리 3 [증명] (조인).** $B_0(G_1+G_2)=B_0(G_1)*B_0(G_2)$ (교차 간선이 전부이므로 조건이 사라진다). 따라서
$$\tau(G_1+G_2)\ \ge\ \tau(G_1)+\tau(G_2),\qquad \iota(G_1+G_2)\ \le\ \iota(G_1)+\iota(G_2).$$
*증명.* 첫째: $\operatorname{coind}X$ 를 달성하는 $f:S^p\to X$, $g:S^q\to Y$ 의 조인 $S^p*S^q=S^{p+q+1}\to X*Y$ 가 동변이므로 $\operatorname{coind}(X*Y)\ge p+q+1$, $\tau=\operatorname{coind}+1$ 이므로 결론. 둘째는 정리 2. ∎

**정리 4 [증명] (동치).** 다음은 동치다.
(i) 모든 그래프와 모든 정점 분할에 대해 $\tau(G)\le\sum_i\tau(G[V_i])$ (B 판 $\tau$ 부분가법).
(ii) 모든 $G_1,G_2$ 에 대해 $\tau(G_1+G_2)\le\tau(G_1)+\tau(G_2)$ ($J$).
*증명.* (i)⇒(ii): $G_1+G_2$ 의 분할 $V(G_1)\sqcup V(G_2)$ 에 (i) 를 적용하면 $\tau(G_1+G_2)\le\tau(G_1)+\tau(G_2)$. (ii)⇒(i): $G\subseteq G':=G[V_1]+\cdots+G[V_k]$ (같은 정점 집합, 교차 간선 추가) 이고 $B_0(G)\subseteq B_0(G')$ 이므로 $\tau(G)\le\tau(G')$; (ii) 를 $k-1$ 번 적용하면 $\tau(G')\le\sum\tau(G[V_i])$. ∎

**따름 5 [증명].** $\tau=\operatorname{zig}$ 가 모든 그래프에서 성립하면 $J$ 가 성립한다 (zig 는 조인에서 부분가법: 두 최적 순서를 이어 붙이면 런 수가 합 이하). 즉 R05 판정 대상 $\tau=\operatorname{zig}$ 는 $\tau$ 부분가법을 함의한다. 역은 모른다.

**따름 6 [증명] (쓸 수 있는 조각 클래스).** $\mathcal T:=\{H:\tau(H)=\iota(H)\}$ 의 조각으로 된 분할에 대해서는 $\tau(G)\le\sum\tau(G_i)$ 가 정리 2 에서 바로 나온다. $\mathcal T$ 는 다음을 포함한다: $\tau=\chi$ 인 그래프 (예: $K_n$, 이분, 홀수 사이클, $\chi$-tight 조인), $\tau=\operatorname{zig}$ 인 그래프 (예: $K_4$-마이너-자유, $C_5[K_2]$ [계산 확인: $\operatorname{zig}\le4$ 인증서 + $\tau=4$]). 단, $\tau=\chi$ 나 $\tau=\operatorname{zig}$ 인 조각들에 대해서는 $\chi$ 나 $\operatorname{zig}$ 의 부분가법으로 이미 자명하다. **비자명한 부분은 $\iota<\operatorname{zig}$ 인 조각**이며 현재 그런 그래프를 알지 못한다 (STATUS 열린 문제와 같다).

### 4. 작은 예의 상세
- **$K_5$, $K_6$.** $\iota=\tau=\chi=\operatorname{zig}=n$ [증명, $B_0(K_n)\cong S^{n-1}$]. 분할 $K_4\sqcup K_1$, $K_4\sqcup K_2$ 에서 $\iota$ 부분가법이 tight.
- **$K_{3,3}$.** 이분이므로 $\tau=\iota=2$ [증명, 보조정리 3 with $\chi=2$ 와 $\tau\ge\omega=2$]. 두 독립 3-집합 분할: $1+1=2$.
- **옥타헤드론 $K_{2,2,2}=3\times2K_1$.** $\tau\ge1+1+1=3$ (정리 3) 과 $\chi=3$ 으로 $\tau=3$ [증명].
- **$C_5[K_2]$.** $\tau=4$ (R03, $\tau(C_n[K_m])=2m$), $\chi=5$, $\operatorname{zig}\le4$ 인증서 [계산 확인: 무작위 탐색이 런 수 4 인 선형순서를 찾음, `r08_zig.py`]. 따라서 $\iota=4$ [증명]. 분할 시도: 두 조각 모두 유도 이분은 불가능 [계산 확인, `r08_bip2.py`, 1024 색칠 전수]. 블록 0–2 와 3–4 로 나누면 $\iota$ 상계 $\iota(K_2+2K_2)+\iota(K_4)$ 로 $\ge 8$. 또 $C_5[K_2]+K_1$: $\tau=5<\chi=6$ [증명, 정리 3 과 $\iota\le\zig$].
- **간선 분할 예 (A).** $K_6=\text{oct}\cup PM_3$: 평면 두 조각, $\tau$ 합 $3+2=5<6$ [증명]. 곱 예 $K_{10}$: $\operatorname{zig}$ 인증서 3, 3 [계산 확인, `r08_mult.py`], 간선 분할 확인 (20+25=45).

### 5. 평면 연결
- 평면 시트 $k$ 개의 상계는 $\tau\le\iota\le4k$ (4색정리 [기억-미검증 외부 정리]). $K_{4k}$ 에서 tight.
- 평면 $\Rightarrow\iota\le4$ 의 조합적 증명은 $Q_3$ (R04 열린 목표 W, 평면 $\Rightarrow$ 순서 런 $\le4$) 와 같다. 성공하면 4색정리 없이 $\tau\le4p(G)$ 가 나온다.
- 평면 조각을 $\iota$ 로 읽는 것은 $\tau\le d_R+1$ 과 같은 역할이지만 평면 조각 자체가 $\chi$ 상계보다 더 주지 않는다.

## 문주님께 요청
없음.

## 후속연구 지점
1. **$J$ 증명 또는 반례 (우선순위 1).** 이유: 정리 4 로 $\tau$ 정점 부분가법이 $J$ 와 동치이며, 채택한 정의 $\alpha$ 에서 $\tau$ 판으로 옮기는 유일한 빈칸이다. 시작: $\operatorname{coind}(X*Y)\le\operatorname{coind}X+\operatorname{coind}Y+1$ 이 $X,Y=B_0$ 에 대해 성립하는지 본다. 조인 $\mathbb Z_2$-사상을 $\operatorname{coind}$ 쪽으로 구성 (정리 3 의 역) 하거나, $\operatorname{coind}=\operatorname{ind}$ 가 $B_0$ 에서 성립하는지 확인한다. 난점: 자유 $\mathbb Z_2$-복합체의 $\operatorname{coind}$ 조인 상계는 일반적으로 알려져 있지 않다 [기억-미검증].
2. **$\iota\neq\tau$ 인 그래프 찾기 (간극 탐지).** 이유: $J$ 가 깨질 가능성은 간극 조각에서만 나오므로 $\iota>\tau$ 인 그래프가 있어야 한다. 시작: STATUS 의 $\tau<\operatorname{zig}$ 후보 (열린 문제) 나 $\tau<\chi$ 인 7 정점 5개 그래프에서 $\operatorname{zig}$ 와 $\tau$ 를 비교. 난점: $\operatorname{ind}$ 의 정확한 계산 도구가 없다.
3. **$\iota<\chi$ 인 조각으로 된 분할 (새 정보 찾기).** 이유: 평면 조각은 $\chi$ 상계와 같아 쓸모 없다. $\operatorname{zig}\le3$ 이면서 $\chi=4$ 인 $C_{10}^2$ 류 조각으로 $\tau\le3k$ 를 얻을 수 있는지 본다. 시작: $C_{10}^2$ 을 두 조각으로 나누고 $\iota$ 상계를 확인, $n\ge9$ 족에서 $\tau=3$ 과 대조. 난점: 분할 구조가 조각 안에서 $\operatorname{zig}$ 인증서를 깨지 않아야 한다.
4. **평면 $\Rightarrow\operatorname{zig}\le4$ 의 조합 증명 (B 정의를 4색정리 없이).** 이유: 후보 $\beta$ 의 상계를 4색정리에서 떼어 낸다. 시작: R04 에서 얻은 쌍 환원과 5색칠 환원을 $\iota$ 판에 옮긴다 (보조정리 4 를 통해 $\operatorname{zig}\le4$ 면 $\iota\le4$). 난점: 가설 C3 의 반례 탐색이 계속 실패했다 (R04 기록).
