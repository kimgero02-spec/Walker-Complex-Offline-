# [R4-researcher2] 피복·균등분할·이중덮개에서 Γ 의 함자성: 「제곱 피복」 위에서만 함자

- 작성자: researcher2 / 라운드: R04 / 역할: 피복·균등분할 몫·이중덮개 (수신: 대수검존)
- 코드: `rooms/researcher2/r4lib.py r4_search.py r4_ce.py r4_ap.py r4_gam.py r4_t2.py r4_k5.py r4_s3.py r4_c18.py`

## 요약
1. [증명] 구조 보조정리: 임의의 $P,Q$ 에 대해 $\nu:C_P\to C_{PQ^2}$, $(t,w)\mapsto(t,Qw)$ 는 유한 쌍유리 사상(무한원점 근방에서 동형)이고 $1\to L\to\Gamma_{PQ^2}\xrightarrow{\nu^*}\Gamma_P\to1$ 이 완전하다. $L=\mathrm{R}_{A/k}\mathbb G_m/\mathrm{R}_{F/k}\mathbb G_m$ ($A=k[t,w]/(w^2-P,Q)$, $F=k[t]/Q$), 연결·가환·선형군, 차원 $\deg Q$. $Q$ 의 근 $a$ (중복도 $m$) 마다 **$P(a)=0$ 이면 단위멱(차원 $m$), $P(a)\neq0$ 이면 (노름1 토러스)$\times$(단위멱 $m-1$)**. 방향은 힌트와 반대: 곡선 사상은 $C_G\to C_H$ (H 가 더 특이), $\Gamma$ 사상이 $\Gamma_H\twoheadrightarrow\Gamma_G$.
2. [증명] 피복 $H\to G$ 와 균등분할 모두 $A_HP_f=P_fA_G$ (또는 $AS=SB$) 로 $P_G\mid P_H$, $P_B\mid P_G$. 그러나 몫 $R=P_H/P_G$ 는 일반적으로 **제곱이 아니다**. 곡선 사상이 $t$-선 위에서 존재 $\iff$ $R$ 이 제곱 (정리 3). 일반 경우 $C_H$ 는 $C_G\times_{\mathbb P^1}C_R$ 의 $V_4$-몫 셋째 곡선이라 $\Gamma_G,\Gamma_H$ 사이에 정준 사상이 없다.
3. [증명 + 계산 확인] **결정적 반례** (연결 6정점 그래프의 연결 이중덮개: $\Gamma_G$ 는 타원곡선 몫을 갖고 $\Gamma_H$ 는 선형군; $K_5\to K_5\times K_2$: 토러스 $T_{-5}$ vs $T_{-15}^2$, $|\Gamma_G(\mathbb F_7)|=42\nmid3136$; $P_4\sqcup P_4\to P_4$). 따라서 $\Gamma$ 는 전체 피복 범주의 함자가 **아니다**.
4. [증명] $R$ 이 제곱인 피복들 ("제곱 피복", 홀수 위수 갈루아 피복 포함: $C_9\to K_3$, $C_{18}\to C_6$) 은 합성에 닫힌 wide 부분범주 $\mathrm{Cov}_\square$ 를 이루고, 거기서 $f\mapsto\nu_f^*$ 는 **공변** 함자 (전사, 핵 연결 선형군). 전체 범주에서의 함자는 $G\mapsto P_G$ (약수 poset) 와 그 쿠머 류 $\kappa(G)=[P_G]\in k(t)^\times/k(t)^{\times2}$ 뿐이다.

## 본문

### 0. 모델과 기본 사실
$k$: 표수 $\ne2$ 인 체 (표수 2 에서는 $w^2=P$ 가 비분리라 정의가 달라져야 함 — §9). $A$ 의 특성다항식 $\chi(x)=\sum_{j=0}^n c_jx^{n-j}$ 이면
$$P_G(t)=\det(tA-I)=(-1)^n\sum_{j}c_jt^j.\quad[\text{증명: }t^n\chi(1/t)=\det(tI\cdot\tfrac1t\ldots)\text{, 즉 }\textstyle\prod(\lambda_it-1)]$$
차수 $d=\mathrm{rank}A$, $P_G(0)=(-1)^n$, 모든 근은 $0$ 이 아니다.

곡선 $C_P$: 아핀 $w^2=P(t)$, 무한원점 쪽 차트 $s=1/t$, $w'=w/t^{N/2}$ ($N=2\lceil d/2\rceil$), $w'^2=s^{N-d}\cdot s^dP(1/s)$. $s^dP(1/s)$ 의 $s=0$ 값 = $P$ 의 최고차 계수 $\neq0$ 이므로 [증명] **무한원점은 항상 매끈** (d 짝수: 두 점, 홀수: 분기점). 특이점은 전부 $P$ 의 중근에 있다. $p_a=\lfloor(d-1)/2\rfloor$. $\Gamma_P:=\mathrm{Pic}^0(C_P)$ (기하적으로 기약일 때; $P=cS^2$ 인 가약 경우는 §1 끝).

### 1. 구조 보조정리 (임무 (1))

**정리 1** [증명]. $P,Q\in k[t]$, $P$ 는 (상수)$\times$(제곱) 이 아님, $Q(0)\neq0$. $O_G=k[t,w]/(w^2-P)$, $O_H=k[t,w_H]/(w_H^2-PQ^2)$.
(a) $w_H\mapsto Qw$ 로 $O_H=k[t]\oplus k[t]Qw=k[t]+Q\,O_G\subset O_G$. 따라서 $\nu:C_P\to C_{PQ^2}$ 는 유한 쌍유리. 무한원점에서는 $w'_H=w'\cdot s^eQ(1/s)$ ($e=\deg Q$) 이고 $s^eQ(1/s)|_{s=0}=Q$ 의 최고차 계수 $\neq0$, 즉 $\nu$ 는 거기서 동형. $O_G/O_H\cong k[t]/Q$ (길이 $e$) 이므로 $p_a(H)=p_a(G)+e$. **$C_H$ 는 $C_G$ 의 부분 정규화가 아니라, $C_G$ 를 $Q$ 의 근에서 "접착"해 특이점을 늘린 곡선** (힌트의 $C_H\to C_G$ 는 방향이 반대; $\Gamma$ 쪽 방향 $\Gamma_H\to\Gamma_G$ 는 맞다).
(b) 층열 $1\to\mathcal O_{C_H}^*\to\nu_*\mathcal O_{C_G}^*\to\mathcal L\to1$, $\nu$ 유한이므로 $H^1(\nu_*\mathcal O_{C_G}^*)=\mathrm{Pic}(C_G)$, $H^1(\mathcal L)=0$ (스카이스크래퍼). $H^0(\mathcal O^*)=k^\times$ 양쪽 (기하적으로 기약) 이므로
$$1\to \mathcal L(C_H)\to\mathrm{Pic}(C_H)\xrightarrow{\nu^*}\mathrm{Pic}(C_G)\to0 .$$
(c) $\mathcal L$ 의 줄기: $Q(a)=0$ 인 점에서 $(k[t]+QO_G)^*=k[t]^*(1+QO_G)$ (근방에서 $Q\in\mathrm{rad}$, 잔류값이 $f(a)$) 이므로 $\mathcal L_a=(O_G/Q)^*/(k[t]/Q)^*$. 대수군으로
$$L=\mathrm R_{A/k}\mathbb G_m\big/\mathrm R_{F/k}\mathbb G_m,\ A=O_G/QO_G=k[t,w]/(w^2-P,Q),\ F=k[t]/Q,$$
$\dim_kA=2e,\ \dim_kF=e$ 이므로 $L$ 은 연결·가환·선형, $\dim L=e$. 연결이라 차수 0 에 들어가고 $\deg\nu^*M=\deg M$ 이므로
$$\boxed{1\to L\to\Gamma_{PQ^2}\xrightarrow{\ \nu^*\ }\Gamma_P\to1}\quad(\text{차원: }p_a(H)=p_a(G)+e\ \checkmark).$$
$k$-점: 힐베르트 90 ($H^1(k,\mathrm R_{F/k}\mathbb G_m)=0$) 로 $L(k)=A^\times/F^\times$. $k=\mathbb F_q$: 랭 정리로 $\Gamma_H(\mathbb F_q)\to\Gamma_G(\mathbb F_q)$ 전사, $|\Gamma_H(\mathbb F_q)|=|L(\mathbb F_q)|\,|\Gamma_G(\mathbb F_q)|$. (랭 정리, 일반화 야코비안의 대수군 구조는 표준 사실 [기억-미검증]; 위 완전열 자체는 위 논증으로 [증명].) $\square$

**국소 구조 (공통근·중복도·표수 조건 해소).** $Q$ 의 기약인수 $\pi$ (차수 $f$, $q'=q^f$, $Q$ 안의 중복도 $m$) 마다 $A_\pi=(\mathbb F_q[t]/\pi^m)[w]/(w^2-P)$:

| 조건 ($a$=$\pi$ 의 근) | $A_\pi$ 의 극대이상 | $\lvert L_\pi(\mathbb F_q)\rvert$ | 군의 형 |
|---|---|---|---|
| $P(a)=0$ **(공통근)** | 1개, 잔류체 $\mathbb F_{q'}$ | $q'^{\,m}$ | 단위멱 (차원 $mf$), 표수 0 에서 $\mathbb G_a^{mf}$ |
| $P(a)\neq0$ 제곱 | 2개, 잔류체 $\mathbb F_{q'}$ | $q'^{\,m-1}(q'-1)$ | $\mathrm R_{k(a)/k}(\mathbb G_m\times U_{m-1})$ |
| $P(a)\neq0$ 비제곱 | 1개, 잔류체 $\mathbb F_{q'^2}$ | $q'^{\,m-1}(q'+1)$ | $\mathrm R_{k(a)/k}(R^1_{k(a)(\sqrt{P(a)})/k(a)}\mathbb G_m\times U_{m-1})$ |

[증명] $|A_\pi^\times|=|A_\pi|\prod(1-|\kappa|^{-1})$, $|F_\pi^\times|=q'^m(1-q'^{-1})$ 의 비.
- **공통근**이 있으면 토러스가 아니라 단위멱: $K_4$ ($S_0=-(3t-1)(t+1)$, $Q=t+1$, $S_0(-1)=0$) $\Gamma=\mathbb G_a$ 와 일치.
- **중복도**: $P_H$ 의 근 $a$ 의 중복도 $\mu$ 는 $S_0$ 에 $\mu \bmod 2$, $Q$ 에 $\lfloor\mu/2\rfloor$ 로 들어간다. $\mu$ 홀수 $\ge3$: 첨점형 (공통근, 단위멱 $(\mu-1)/2$), $\mu$ 짝수: 마디형 (토러스 1 + 단위멱 $\mu/2-1$).
- **표수**: $p$ 홀수에서 단위멱 부분은 벡터군이 아니라 Witt형 곱일 수 있으나 위수 $q'^{\,\cdot}$ 은 동일. 환원 mod $p$ 에서 $P_H=P_GQ^2$ 는 유지되나 $S_0$ 의 형태(제곱무인수 여부)가 바뀌므로 공식은 **환원한 다항식에 적용**해야 한다. $p=2$ 는 §9.
- **가약 경우** $P=cS^2$ (스펙트럼의 모든 고윳값이 짝수 중복, 예: $G=F\sqcup F$): $C_P$ 는 $\mathbb P^1$ 두 장이 $S$ 의 근에서 붙은 곡선 (또는 $c$ 비제곱이면 $\mathbb P^1_{k(\sqrt c)}$). 같은 증명에서 $H^0(C_{\mathrm{norm}},\mathcal O^*)/k^\times$ 만큼 줄어든다: $\Gamma=L/\big(H^0(\tilde C,\mathcal O^*)/k^\times\big)$, $\dim=\deg S-1$ (다차수 0 의 Pic). 예: $2K_2$: $P=(1-t^2)^2$, $\Gamma=\mathbb G_m$, $p_a=1$ ✓.
- $k$ 가 유한체가 아니면 $\Gamma_H(k)\to\Gamma_G(k)$ 의 여핵은 $H^1(k,L)=\ker\big(\mathrm{Br}\,F\to\mathrm{Br}\,A\big)$ ($\supset$ 4원수 대수 $(P(a),\cdot)$ 류) 에 들어간다 [증명 스케치: $1\to\mathrm R_F\mathbb G_m\to\mathrm R_A\mathbb G_m\to L\to1$, $H^1(\mathrm R_A\mathbb G_m)=0$]. $\mathbb Q$ 위에서는 전사가 깨질 수 있다.

**예 (계산 확인, 아래 $q=p$ 소수, $|\Gamma(\mathbb F_p)|$):**
$K_3$: $P=(t+1)^2(2t-1)$ → $p-(\tfrac{-3}{p})$ ($p=5,7,11,13,17$: 6,6,12,12,18).
$C_6$: $P=(1-4t^2)(1-t^2)^2$ → $S_0=1-4t^2$ (원뿔), $Q=1-t^2$, 근 $\pm1$, $S_0(\pm1)=-3$: $\Gamma_{C_6}\cong T\times T$, $T=R^1_{\mathbb Q(\sqrt{-3})/\mathbb Q}\mathbb G_m\cong\Gamma_{K_3}$ (값 36,36,144,144,324 = $|\Gamma_{K_3}|^2$ ✓).
$C_9$: $P_{C_9}=P_{K_3}\cdot(t^3-3t^2+1)^2$ [계산 확인: sympy 정확 인수분해], $Q_9=t^3-3t^2+1$ 은 $\mathbb Q(\zeta_9)^+$ 를 정의하는 기약 삼차식, $P_{K_3}(a)\ne0$ → $L$ 은 3차원 토러스, $|\Gamma_{C_9}|$ = 756, 2052, 15984, 26352, 82944 ($p=5,7,11,13,17$); 비 $|\Gamma_{C_9}|/|\Gamma_{K_3}|$ = 126, 342, 1332, 2196, 4608 (정수 ✓, 정리 1 의 $|L|$ 과 일치하도록 계산).
$Q_3\to K_4$: $P_{Q_3}=(1-9t^2)(1-t^2)^3$, $S_0=(1-9t^2)(1-t^2)$ (종수 1, 타원곡선 $E_0:y^2=(1-9t^2)(1-t^2)$), $Q=1-t^2$, $S_0(\pm1)=0$ 공통근 → $\Gamma_{Q_3}$ = $E_0$ 의 $\mathbb G_a^2$ 확대, $|\Gamma_{Q_3}(\mathbb F_p)|=p^2\#E_0(\mathbb F_p)$ (200, 392, 968, 2704, 4624). $\Gamma_{K_4}=\mathbb G_a$: $|\Gamma_{K_4}|=p$ 가 나누지만 **정리 1 이 아니라 자명한 이유** ($p\mid p^2$). $\Gamma_{Q_3}$ 의 아벨 몫 $E_0\ne0$ 이 $\Gamma_{K_4}$ 에는 없다는 점이 이후 반례의 형태를 예고한다.

### 2. 피복·균등분할의 스펙트럼 관계 (임무 (2),(3) 앞부분)

**정리 2** [증명, 직접 구성]. (i) $f:H\to G$ 가 $m$ 겹 피복 (국소 전단사: 모든 $h$ 에서 $f$ 가 $N(h)$ 를 $N(f(h))$ 로 전단사) 이고 $G$ 연결이면, 모든 올 $V_u=f^{-1}(u)$ 의 크기는 같은 $m$ (간선 $uv$ 위에서 $V_u\leftrightarrow V_v$ 가 일대일). 각 간선 $uv\in E(G)$ 에서 $V_u,V_v$ 사이의 $H$-간선은 완전 대응, 따라서 $V(H)=V(G)\times[m]$ 로 두면
$$A_H=(\Pi_{uv})_{u,v},\quad\Pi_{uv}\in S_m\ (uv\in E(G)),\ \Pi_{vu}=\Pi_{uv}^{T},\ 0\ \text{(비간선)}.$$
당김 행렬 $P_f$ (행=$H$ 정점, 열=$G$ 정점, 올 지시함수) 에 대해 $(A_HP_f)(h,u)=\#\{h'\sim h: f(h')=u\}=A_G(f(h),u)=(P_fA_G)(h,u)$, 즉
$$A_HP_f=P_fA_G,\quad P_f \text{ 단사}.$$
(ii) **균등분할**: 특성행렬 $S$ ($n\times k$), $AS=SB$ ($B$=몫 행렬, 일반적으로 비대칭). 피복은 올 분할이 균등분할이고 $B=A_G$ 인 특수 경우 ($P_f=S$). 즉 (2) $\subset$ (3).
(iii) $\mathrm{col}(S)$ 는 $A$-불변, 그 위에서 $A$ 는 $B$. 기저 $[S\,|\,\text{여공간}]$ 에서 블록삼각이므로 $\det(I-tA)=\det(I-tB)\det(I-t\tilde A)$ ($\tilde A$: 몫 공간 위의 작용; $A$ 대칭이면 $S^\perp$ 위의 $A|_{S^\perp}$). 부호 $(-1)^n$ 를 정리하면
$$P_G=\pm P_B\cdot R_\pi,\qquad R_\pi=\pm\det(I-tA|_{S^\perp});\quad\text{피복: }P_H=P_G\cdot R_f,\ R_f=\pm\det(I-tA_H|_{W^\perp}).$$
$B=(S^TS)^{-1}S^TAS$ 는 대칭행렬 $(S^TS)^{-1/2}S^TAS(S^TS)^{-1/2}$ 와 닮음이므로 $B$ 의 고윳값은 실수·대각화 가능 [증명]. $\square$

**따름 (스펙트럼 함자)** [증명]: 피복의 합성에 대해 $P_F\mid P_G\mid P_H$; 균등분할의 세분에 대해 $P_{B'}\mid P_B\mid P_G$. 곧 $G\mapsto P_G$ 는 $\mathrm{Cov}$ (화살 $H\to G$) $\to(\mathbb Z[t],\mid)^{\mathrm{op}}$ 의 함자. 선형대수 쪽 해석: $G\mapsto M_G=(F^G,A_G)$ 는 $F[x]$-가군의 **반변** 함자이고 $f\mapsto P_f$ 는 단사 가군사상 ($A_HP_f=P_fA_G$). $P_G$ 는 가군 $M_G$ 의 지지(스펙트럼 다항식)이며 완전열 $0\to M_G\to M_H\to M_R\to0$ 에서 **곱셈적**이다.

**예 (R 의 형태).** $R_f=P_H/P_G$ 의 명시:
- 이중덮개 (부호 $\sigma$): $R=P_{G,\sigma}=\det(tA^\sigma-I)$ (부호 인접행렬). $G\times K_2$ 는 $\sigma\equiv-1$: $R=P_G(-t)$.
- $P_{G\times K_2}(t)=P_G(t)P_G(-t)$ **(부호 +)** [증명: $\det\begin{pmatrix}-I&tA\\tA&-I\end{pmatrix}=\det(I-t^2A^2)=\det(I-tA)\det(I+tA)=P_G(t)P_G(-t)$, $(-1)^{2n}=1$; $K_5$ 에서 sympy 로도 확인].
- 갈루아 피복 (군 $\Gamma_c$): $R=\prod_{\rho\ne1}P_\rho^{\dim\rho}$, $P_\rho=\det(tA_\rho-I)$, $A_\rho=(\rho(g_{uv}))$ 에르미트. 비자기쌍대 $\rho$ 는 $\bar\rho$ 와 짝지어 $P_\rho=P_{\bar\rho}$ ($A_{\bar\rho}=A_\rho^T$) 이므로 제곱으로 들어간다.
- $C_6\to K_3$: $R=-(t-1)^2(2t+1)$. $C_9\to K_3$: $R=Q_9^2$. $C_{18}\to C_6$: $R=(Q_9Q_9')^2$, $Q_9'=t^3+3t^2-1$. $C_{18}\to C_9$: $R=-(t-1)^2(2t+1)Q_9'^2$ (제곱 아님). $C_{18}\to K_3$: 제곱 아님. [계산 확인]

### 3. 곡선 사상이 생기는가 (임무 (2) 핵심)

**정리 3** [증명]. $P_G,P_H$ 가 (상수)$\times$(제곱) 이 아니라고 하자. 다음은 동치: (i) $R=P_H/P_G\in k(t)^{\times2}$ (=다항식 제곱); (ii) 쌍유리 사상 $C_G\to C_H$ 가 $t$-사영과 호환되게 존재; (iii) $t$-사영과 호환되는 비상수 사상 $C_H\to C_G$ 또는 $C_G\to C_H$ 가 존재. 증명: (iii) 이면 $k(t)$ 위 이차확대 $k(C_G)=k(t)(\sqrt{P_G})$ 가 $k(C_H)=k(t)(\sqrt{P_H})$ 에 들어가므로 같고 $P_G/P_H$ 가 제곱. (i)$\Rightarrow$(ii) 는 정리 1. $\square$

즉 **$R$ 이 제곱이 아니면 (사영 호환) 곡선 사상 자체가 없다**: 스펙트럼 관계 $P_G\mid P_H$ 는 곡선 사상을 주지 않고 $\Gamma$ 사이의 사상도 주지 않는다. 사영 비호환 사상 $C_H\to C_G$ 가 우연히 있을 수 있으나 그래프 구조에서 나오는 것이 아니다.

**정리 4 ($V_4$ 구조)** [증명 스케치; 아벨 부분 수준]. $R$ 이 제곱이 아니고 $P_G,R,P_GR$ 이 모두 제곱류가 아니면 $X=C_G\times_{\mathbb P^1_t}C_R$ ($k(X)=k(t)(\sqrt{P_G},\sqrt R)$) 는 $\mathbb P^1_t$ 위의 $V_4$-피복이고 세 이차 중간곡선이 $C_G,C_R,C_H$ ($\sqrt{P_GR}$). $H^0(X,\Omega)$ 를 $V_4$ 지표로 분해하면 자명 지표 부분은 $H^0(\mathbb P^1,\Omega)=0$, 나머지 세 지표 부분이 각각 $H^0(C_G,\Omega),H^0(C_R,\Omega),H^0(C_H,\Omega)$ 의 당김. 따라서 $g(X)=g_G+g_R+g_H$ 이고 $J(X)\sim J(C_G)\times J(C_R)\times J(C_H)$ (정규화의 야코비안, 동종). 대응 $\pi_{H*}\pi_G^*:J(C_G)\to J(C_H)$ 는 기저변환($\pi_{H*}\pi_G^*=g^*f_*$, $f_*L\in\mathrm{Pic}^0(\mathbb P^1)=0$) 으로 **영사상**. 그러므로 $J(C_H)$ 는 $J(C_G)$ 와 서로 다른 동형류 성분이며 일반적으로 어떤 사상도 강제되지 않는다. (Kani–Rosen 의 일반형은 [기억-미검증]; 위는 미분 분해에 의한 직접 논증.)

### 4. 제곱 피복 범주 위의 함자성 (임무 (4),(5))

**정의.** $\mathrm{Cov}_\square$: 대상은 유한 단순 그래프, 화살은 피복 $f:H\to G$ 중 $R_f=P_H/P_G=T_f^2$, $T_f\in k[t]$, $T_f(0)=1$ 인 것. ($R_f(0)=(-1)^{n_H-n_G}$; 이것이 $+1$ 이어야 한다. $-1$ 이면 $C_H$ 는 $C_G$ 의 $-1$ 꼬임이라 $k\ni\sqrt{-1}$ 이거나 기하적 함자.) $T_f(0)=1$ 은 $\iota^*=-1$ 의 부호 모호성(⟷ $T\to-T$) 을 제거한다 [증명: $\iota$ 는 $L$ 위에서 $x\mapsto\bar x\equiv x^{-1}$].

**정리 5** [증명]. (a) $\mathrm{Cov}_\square$ 는 합성에 닫힌다: $T_{gf}=T_gT_f$. (b) $\Gamma(f):=\nu_f^*:\Gamma_H\to\Gamma_G$ 는 $\Gamma(\mathrm{id})=\mathrm{id}$, $\Gamma(gf)=\Gamma(g)\Gamma(f)$: 곡선 사상 $\nu_{gf}=\nu_f\circ\nu_g$ ($w_F\mapsto T_gw_F\mapsto T_fT_gw_F$) 와 $\mathrm{Pic}$ 의 반변성 $(\nu_f\nu_g)^*=\nu_g^*\nu_f^*$. 즉 **$\Gamma:\mathrm{Cov}_\square\to\{\text{가환 대수군}\}$ 는 공변**이다 (피복 화살 $H\to G$ 에 $\Gamma_H\to\Gamma_G$; 곡선 쪽은 $C_G\to C_H$ 로 반대 방향이고 $\mathrm{Pic}^0$ 가 한 번 뒤집는다. 이것은 가군 $M_G\to M_H$ 가 한 번 뒤집은 방향과도 맞물린다). (c) 각 $\Gamma(f)$ 는 전사, 핵 $L(P_G,T_f)$ 는 연결 선형군 (정리 1 표), $\mathbb F_q$ 에서 $|\Gamma_G(\mathbb F_q)|\,\big|\,|\Gamma_H(\mathbb F_q)|$ 와 몫 $|L|$ 의 명시식.

**$\mathrm{Cov}_\square$ 의 원소 (임무 (4) 의 가족).**
- [증명] **홀수 위수 갈루아 피복**은 제곱: 군 $\Gamma_c$ 의 위수가 홀수이면 비자명 기약 실표현의 차원은 짝수 (홀수 위수군은 실수 지표가 자명한 것뿐: $g\sim g^{-1}$ 이면 $x g x^{-1}=g^{-1}$, $x$ 의 위수 홀수이므로 $x\in\langle x^2\rangle$ 가 $g$ 와 가환하여 $g=g^{-1}$, $g=1$; 실지표 수 = 실류 수 [브라우어 치환보조정리, 기억-미검증]). 고유공간 $E_\lambda\cap W^\perp$ 는 자명 성분이 없는 실표현이므로 짝수 차원. 따라서 $R=cT^2$, $T\in\mathbb Q[t]$ (가우스 보조정리로 $\mathbb Z[t]$), $c=R(0)/T(0)^2=+1$ ($m$ 홀수라 $R(0)=+1$). 예: $C_9\to K_3$, $C_{3^a}\to C_3$, $C_{18}\to C_6$ (이것은 3겹 $\mathbb Z_3$ 피복).
- [증명] $m$ 개 복사 $mG\to G$: $R=P_G^{m-1}$, $m$ 홀수이면 제곱 ($m=3$: $T=P_G$, $\Gamma_{3G}$ 는 $\Gamma_G$ 의 단위멱 $\dim\deg P_G$ 확대, 모든 근이 공통근). $m=2$ 이면 제곱 아님 (아래 반례).
- [계산 확인] **홀수 겹이라도 충분하지 않다**: $K_4$ 위 $S_3$-전압 (비갈루아 3겹 연결 피복, 전압 $(12)$, $(123)$ 사용) 에서 $R=-(t-1)(t+1)(t^3-5t^2+t+1)(3t^3-5t^2-t+1)$ — 제곱 아님. 이유: $\mathrm{Ind}_{S_2}^{S_3}1=1+\rho_2$ 에서 $\rho_2$ 의 중복도 1.
- 이중덮개: $R=P_{G,\sigma}$ 가 제곱이려면 부호 그래프의 스펙트럼이 모두 짝수 중복이어야 하나, 연결 이중덮개에서는 일반적으로 불가능 (§5 반례들).

### 5. 결정적 반례들: 전체 피복 범주에서 $\Gamma$ 는 함자가 아니다

**반례 A: 연결 6정점 그래프의 연결 이중덮개** [증명 + 계산 확인]. $G$: 정점 $0..5$, 간선 $01,02,03,04,05,12,13,14,15,25,34$ (11개, 차수열 $(5,5,3,3,3,3)$). 부호 $\sigma=-1$ 인 간선: $01,12,15,25$ 나머지 $+1$. $H$: 12정점, 22 간선, 연결, $H\to G$ 가 국소 전단사임을 확인 (코드 `r4_ce.py`). 정확한 인수분해 [계산 확인]:
$$P_G=(t-1)(t+1)^3(7t^2+2t-1),\qquad P_H=-(t-1)^2(t+1)^4(5t^2-1)^2(7t^2+2t-1),$$
$R=-(t-1)(t+1)(5t^2-1)^2$ (제곱 아님: $(t-1)(t+1)$ 홀수 중복).
- $\Gamma_G$: $S_0=(t-1)(t+1)(7t^2+2t-1)$ (제곱무인수, 판별식 $2^{17}$), $Q=t+1$ 공통근 → **$E:y^2=(t^2-1)(7t^2+2t-1)$ (종수 1) 의 $\mathbb G_a$ 확대**, $\dim2=p_a$ ✓.
- $\Gamma_H$: $S_0=-(7t^2+2t-1)$ 는 이차, 원뿔 → **$\Gamma_H$ 는 선형군** (차원 5 = $p_a$ ✓, 토러스 계수 4 + $\mathbb G_a$).
- 만약 전사 $\varphi:\Gamma_H\to\Gamma_G$ 가 있으면 선형부분군의 상은 선형이므로 $\Gamma_H^{\rm ab}\to\Gamma_G^{\rm ab}=E$ 전사 (체발레 구조정리, 기억-미검증); $\Gamma_H^{\rm ab}=0$ 이므로 모순. 또한 유한핵 사상 $\Gamma_G\to\Gamma_H$ 도 불가 (유한 핵이면 $\Gamma_G$ 가 아핀, 그러나 $E$ 몫이 있다). 즉 **어느 방향으로도 전사/동종이 없다**.
- $\mathbb F_p$ 위 확인 [계산 확인]: $p=19$ 에서 $|\Gamma_G|=418=2\cdot11\cdot19$ 이고 $|\Gamma_H|=2462400$, 나눗셈 불가 ($5\le p\le17$ 에서는 우연히 나누어 떨어짐: 5,7,11,13,17 에서 $30\mid120$, $56\mid22400$, …).

**반례 B: 완전 선형 경우, $K_5\to K_5\times K_2$** [증명 + 계산 확인]. $P_{K_5}=(t+1)^4(4t-1)$, $P_{K_5\times K_2}=-(t-1)^4(t+1)^4(4t-1)(4t+1)$ [계산 확인; $=P_{K_5}(t)P_{K_5}(-t)$]. $\Gamma_{K_5}$: $a=-1$, $m=2$, $c S_0(a)=-5$: $\Gamma_{K_5}=R^1_{\mathbb Q(\sqrt{-5})/\mathbb Q}\mathbb G_m\times U$ (차원 2). $\Gamma_{K_5\times K_2}$: $a=\pm1$, $m=2$, 값 $-(4a-1)(4a+1)\big|_{a=\pm1}=-15$: $\big(R^1_{\mathbb Q(\sqrt{-15})/\mathbb Q}\mathbb G_m\times U\big)^2$ (차원 4). **비자기 이유: $\Gamma_{G\times K_2}$ 의 $a$ 에서의 토러스를 정하는 값은 $S(a)S(-a)$ ($=-5\cdot3$) 이지 $S(a)$ 가 아니다.** 서로 다른 이차체의 노름1 토러스 사이 $\mathbb Q$-동형사상은 0 (지표군 위 갈루아 작용이 다른 부호 지표) 이므로 최대 토러스 몫 $T_{-15}^2\to T_{-5}$ 전사가 없고 $\Gamma_H\twoheadrightarrow\Gamma_G$ 가 $\mathbb Q$ 위에서 불가. 유한체 확인 [계산 확인]: $p=7$: $|\Gamma_G|=7\cdot6=42$, $|\Gamma_H|=(7\cdot8)^2=3136$, $42\nmid3136$; $p=17$: $306\nmid73984$; $p=19$: $380\nmid116964$; $p=29$: $812\nmid756900$. (p=11,13,23 에서는 우연히 나눔; $p=3$ 은 불량소수.)

**반례 C: 자명 이중덮개 $P_4\sqcup P_4\to P_4$** [증명 + 계산 확인]. $P_{P_4}=t^4-3t^2+1=(t^2-t-1)(t^2+t-1)$: $\Gamma_{P_4}=E$ (타원곡선, 매끈). $P_{2P_4}=P_{P_4}^2$: $C$ 는 $\mathbb P^1$ 두 장이 4점에서 붙은 곡선, $\Gamma_{2P_4}=\mathrm R_{K/\mathbb Q}\mathbb G_m/\mathbb G_m$ ($K=\mathbb Q[t]/P_{P_4}$) 토러스 (차원 3). $\mathrm{Hom}(E,\text{토러스})=0=\mathrm{Hom}(\text{토러스},E)$ 이므로 전사 불가. $p=11$: $\#E(\mathbb F_{11})=16$, $|\Gamma_{2P_4}|=10^4/10=1000$, $16\nmid1000$ ($p=5$ 는 $t^2-t-1$ 이 중근이라 불량소수라 제외; $p=7,13,19,29$ 는 우연히 나눔).

(반례 C 는 비연결 피복이 포함되지만 A 가 연결 그래프의 연결 피복이므로 연결 범주에서도 성립.)

**균등분할로의 이전.** 피복의 올 분할은 균등분할이고 몫 행렬이 $A_G$ 이므로 반례 A–C 는 (3) 에도 그대로 반례: $P_B=P_G\mid P_H$ 이지만 $\Gamma_H\not\twoheadrightarrow\Gamma_B$.

### 6. 이중덮개의 $\sigma$-고유분해 시험 (임무 (2) 후반)

$H$ 가 이분이면 (예: $G\times K_2$) $P_H(t)=F(u)$, $u=t^2$ ($F(u)=P_G(\sqrt u)P_G(-\sqrt u)=P_1(u)^2-uP_2(u)^2$, $P_G=P_1(t^2)+tP_2(t^2)$). $\sigma:(t,w)\mapsto(-t,w)$ 는 $C_H$ 의 자기동형 (이분 부호 변환 $\varepsilon A\varepsilon=-A$ 에서 옴; 피복의 덱 변환이 아니라 **이분성의 부산물**; 덱 변환은 $A_H$ 와 가환하므로 $C_H$ 위에 자명하게 작용). $V_4=\langle\sigma,\iota\rangle$, 몫: $C_H/\iota=\mathbb P^1_t$, $C_H/\sigma=E_1:w^2=F(u)$, $C_H/\sigma\iota=E_2:v^2=uF(u)$ ($v=tw$). [증명] 미분 $t^idt/w$ 위에서 $\sigma$ 는 $(-1)^{i+1}$, 따라서
$$J(C_H)\sim J(E_1)\times J(E_2)\quad(\text{종수 }\lfloor\tfrac{d-1}2\rfloor+\lfloor\tfrac d2\rfloor=g(C_H)).$$
**그러나 $E_1,E_2$ 는 $C_G$ 가 아니다.** 사슬: $X=C_G\times_{\mathbb P^1_t}C_G^-$ ($C_G^-:z^2=P_G(-t)\cong C_G$) 는 $\mathbb P^1_u$ 위 $D_4$-피복이고 $J(C_G)^2$ 는 2차원 기약표현 동형류 성분, $J(E_1),J(E_2)$ 는 1차원 지표 성분: 강제되는 사상 없음.
- [계산 확인, 결정적] 반례 A 의 $G$ ($G\times K_2$ 는 연결): $P_{G\times K_2}=(t-1)^4(t+1)^4(7t^2+2t-1)(7t^2-2t-1)$, $S_0=49t^4-18t^2+1$ (우함수), 아벨 부분 $\mathrm{Jac}\sim E_2:v^2=u(49u^2-18u+1)$ ($E_1$ 은 원뿔), 토러스 값 $S_0(\pm1)=32$. $E_G:y^2=(t^2-1)(7t^2+2t-1)$ 와 비교: $a_5(E_G)=0,\ a_5(E_2)=2$ (두 곡선 모두 5 에서 좋은 환원), 또 $a_{11}=-6$ vs $-4$, $a_{13}=0$ vs $2$ ⇒ **$E_G\not\sim E_2$ ($\mathbb Q$-비동종)**. 따라서 $\Gamma_{G\times K_2}\sim\Gamma_G\times\Gamma_G'$ 꼴로 갈라지지 않는다.
- 선형 부분에서도: $G\times K_2$ 의 $\pm a$ 토러스는 $S(a)S(-a)$ 로 결정되어 $\Gamma_G$ 의 것과 다르다 (반례 B).
- **성립하는 경우 ($K_3\times K_2=C_6$)**: $S(-a)=S(1)=1$ (제곱) 이라 우연히 $\Gamma_{C_6}\cong\Gamma_{K_3}^2$ ($\sigma$ 는 두 인자를 교환; $\sigma=+1$ 부분 $\cong T$, $\sigma=-1$ 부분 $\cong T$ 동종) [증명, 정리 1 로]. 이것은 곡선 사상에서 나오는 것이 아니라 수치적 우연이다.

### 7. 균등분할 몫 (임무 (3)) 판정
정리 2 에 의해 $P_B\mid P_G$. $R_\pi=P_G/P_B$ 가 제곱이면 정리 1 로 $\Gamma_G\twoheadrightarrow\Gamma_B$ (핵 선형). 일반적으로는 아니다 (올 분할 반례). 비대칭 $B$ 도 $\det(tB-I)$ 는 실계수·고윳값 실수이므로 곡선 $w^2=P_B$ 가 정의되고 위 모든 것이 그대로. [증명]/[계산 확인] 제곱인 비피복 예: $K_n$ 의 분할 $\{v\}|\text{나머지}$: $B=\begin{pmatrix}0&n-1\\1&n-2\end{pmatrix}$, $P_B=-((n-1)t-1)(t+1)$, $R=\pm(t+1)^{n-2}$ 이므로 $n$ 짝수일 때 제곱 ($K_4$: $\Gamma_{K_4}=\mathbb G_a\twoheadrightarrow\Gamma_B=1$, 핵 $\mathbb G_a$ ✓), $n=3$ 에서는 제곱 아님이지만 $\Gamma_B$ 가 자명이라 사상은 존재. 관찰: 사상이 존재하는 것과 정리 1 의 사상인 것은 다르다.

### 8. 약수성 표 ($|\Gamma_G(\mathbb F_p)|\mid|\Gamma_H(\mathbb F_p)|$)
| 쌍 $H\to G$ | 제곱? | 약수성 | 이유 |
|---|---|---|---|
| $C_9\to K_3$ | 예 | 항상 ($p=5..17$) | 정리 5 |
| $C_{18}\to C_6$ | 예 | 항상 | 정리 5 |
| $C_6\to K_3$ | 아니오 | 성립($36=6^2$) | 수치적 우연 (§6) |
| $Q_3\to K_4$ | 아니오 | 성립 | $p\mid p^2$, 자명 |
| $K_5\times K_2\to K_5$ | 아니오 | $p=7,17,19,29$ 에서 **불성립** | 토러스 $T_{-5}$ vs $T_{-15}$ |
| 6정점 반례 $H\to G$ | 아니오 | $p=19$ 에서 **불성립** | 아벨 몫 |
| $2P_4\to P_4$ | 아니오 | $p=11$ 에서 **불성립** | 아벨 vs 토러스 |
| $C_{18}\to C_3$ (6겹=2겹$\circ$3겹) | 아니오 | 성립 (우연) | $R=-(t-1)^2(2t+1)Q_9^2Q_9'^2$ |

합성 시험 [계산 확인]: $C_{18}\to C_6\to C_3$ 에서 $C_{18}\to C_6$ 은 제곱, $C_6\to C_3$ 은 아니고 합성 $C_{18}\to C_3$ 은 제곱 아님; $C_{18}\to C_9\to C_3$ 에서는 앞이 비제곱, 뒤가 제곱, 합성 비제곱. 곧 제곱성은 $\kappa(H)-\kappa(F)=(\kappa(H)-\kappa(G))+(\kappa(G)-\kappa(F))$ 의 $\mathbb F_2$-덧셈이라 **사슬의 모든 화살이 제곱이면 합성이 제곱, 한쪽만 비제곱이면 합성이 비제곱, 두 화살 모두 비제곱이면 합성이 제곱일 수 있다** (예: 두 번 이중덮개 $\sigma_1,\sigma_2$ 로 $\kappa$ 를 상쇄하는 경우는 여기서 탐색하지 않음 [추측]).

### 9. 판정 (임무 (5))
1. **$\Gamma$ 는 전체 피복 범주의 (공변·반변) 함자가 아니다** [증명: 반례 A–C]. 균등분할 범주도 마찬가지.
2. **$\Gamma$ 는 wide 부분범주 $\mathrm{Cov}_\square$ (피복 중 $P_H/P_G$ 가 제곱) 위에서 공변 함자**이며 전사·핵 연결 선형군을 갖는다 [증명]. 홀수 위수 갈루아 피복·홀수 겹 자명 피복 포함.
3. 전체 범주에서 성립하는 약한 함자성은 (a) $G\mapsto P_G$ ($\mathrm{Cov}\to(\mathbb Z[t],\mid)^{\rm op}$), (b) 쿠머류 $\kappa(G)\in k(t)^\times/k(t)^{\times2}$ ($f\mapsto[R_f]=\kappa(H)-\kappa(G)$, 1-코사이클형 함자 $\mathrm{Cov}\to B(\mathbb F_2\text{-벡터공간})$), (c) $\Gamma_G^{\rm ab}=J(\kappa(G))$ 는 $\kappa$ 만의 함수 (함자 $K\to\mathrm{Ab.Var}$ 는 이산범주 위에서만 의미). $\kappa(H)=\kappa(G)$ 일 때에만 정준 동형 $\Gamma_H^{\rm ab}\cong\Gamma_G^{\rm ab}$ 가 나오고 나머지 차이는 선형군 $L$ 이다.
4. **표수 2**: $w^2=P(t)$ 는 $k$ 에서 비분리 (기하적으로 $(w-\sqrt P)^2=0$ 의 비환원), 정의 자체가 다시 필요 ($w^2+hw=P$ 형 모델과 그래프 스펙트럼의 대응은 없음) → 본 정리 모두 $\mathrm{char}\ne2$.
5. 막힌 곳 (증명 장애물): (i) 비갈루아 피복에서 $R$ 이 제곱이 되는 필요충분조건(표현론적) 미해결 — 갈루아 아닌 경우 $R=\prod_\rho P_\rho^{\langle\mathrm{perm},\rho\rangle}$ 이고 제곱 판정에는 실수형 $\rho$ 의 중복도와 $P_\rho$ 자체의 제곱성이 모두 필요하다. (ii) $\mathbb Q$ 위에서 $\Gamma_H(\mathbb Q)\to\Gamma_G(\mathbb Q)$ 의 여핵 $H^1(\mathbb Q,L)$ 의 크기. (iii) 정리 4 의 $J(C_H)$ 와 $J(C_G),J(C_R)$ 의 관계를 프림형으로 정확히 쓰는 것 ($D_4$ 표현의 중복도 계산).

## 후속연구 지점
1. (우선순위 1) **$\mathrm{Cov}_\square$ 의 표현론적 특징화.** 무엇을: 피복 $H\to G$ (갈루아 아님 포함) 에서 $R_f=\prod_\rho P_\rho^{\langle\mathrm{perm},\rho\rangle}$ 가 제곱이 되는 조건. 왜: $\Gamma$ 가 함자인 범주의 정확한 경계. 시작: 전압 그래프 $\Rightarrow$ 부분군 지수 표현의 분해, 실수형/복소형/사원수형 구분, $P_\rho\in\mathbb Q[t]$ 의 제곱성 (반례 $K_4$/$S_3$ 의 $\rho_2$). 난점: $P_\rho$ 자체가 제곱이 되는 우연 (그래프별), 홀수 위수가 아닌 군.
2. (우선순위 2) **쿠머 범주 위의 올바른 함자 구성.** 무엇을: $\kappa(G)\in k(t)^\times/k(t)^{\times 2}$ 와 $V_4$-구조(정리 4) 를 사용해, 비제곱 피복에서 $J(C_H)$ 를 $J(C_G)$, $J(C_R)$ 로부터 프림형으로 기술; 이중덮개 $G\times K_2$ 에서 $D_4$-분해를 완성. 왜: $\Gamma$ 가 함자가 되지 않는 이유를 정량화하고 대신 어떤 (비정준) 관계가 남는지 규명. 시작: 반례 A 의 $E_G,E_2$ 에 대해 $D_4$ 표현의 중복도 표를 만들고 $\mathrm{Hom}(E_G,E_2)=0$ 증명($a_5$ 로 이미 비동종 [계산 확인]); 부호그래프 $P_{G,\sigma}$ 의 야코비안과 비교. 난점: $D_4$ 와 특이 모델 사이의 정규화 처리.
3. (우선순위 3) **$\mathbb Q$ 위 유리점과 $H^1(\mathbb Q,L)$.** 무엇을: $\Gamma_H(\mathbb Q)\to\Gamma_G(\mathbb Q)$ 의 여핵 = $\ker(\mathrm{Br}F\to\mathrm{Br}A)$ 의 계산. 왜: 정리 1 이 유한체에서만 전사이고 $\mathbb Q$ 에서는 깨질 수 있음. 시작: $C_9\to K_3$ 에서 $F=\mathbb Q(\zeta_9)^+$, $A=F(\sqrt{2a-1})$ 의 4원수 $(2a-1,\cdot)$. 난점: 대역적 브라우어군 계산.
4. (우선순위 4) **$\mathbb Z_3$-탑 $C_3\leftarrow C_9\leftarrow C_{27}\leftarrow\cdots$.** 무엇을: 모든 화살이 제곱 피복이므로 $\Gamma_{C_{3^k}}$ 는 전사 사영계를 이루고 핵 $L_k$ 는 토러스 (차원 $3^{k}-3^{k-1}$). 왜: 이웃한 층 위수비 $|L_k(\mathbb F_p)|$ 의 증가 규칙 (이와사와식 $\lambda,\mu$ 비슷한 구조인가) [추측/망상]. 시작: $\mathbb Q(\zeta_{3^k})^+$ 의 소수 분해와 $2a-1$ 의 제곱성 판정으로 $|L_k(\mathbb F_p)|$ 공식. 난점: 모든 근에서 $P_{K_3}(a)$ 의 제곱 여부가 소수 분해 + 이차 지표에 의존.
5. (우선순위 5) **표수 2 와 불량소수.** 무엇을: 표수 2 에서 $\det(tA-I)$ 로 곡선 대신 $w^2+hw=f$ 형 모델을 그래프 스펙트럼이 줄 수 있는지; 불량소수에서 $S_0$ 가 제곱무인수가 아니게 되는 경우의 $\Gamma$ 의 환원(네론 모델 유사). 왜: 정리 1 의 표수 가정 제거. 시작: 완전 그래프 $K_n$ 를 $\mathbb F_2$ 에서 대조. 난점: $P_G$ 가 어떤 아르틴–슈라이어 데이터도 정하지 않음.
