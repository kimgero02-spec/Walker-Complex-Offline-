# [R4-researcher3] 분리합·곱·조인·여그래프·마이너에서 $\Gamma$ 의 함자성: 존재와 비존재의 경계

- 작성자·라운드·역할: researcher3 · R04 · 합집합·곱·조인·마이너의 함자성 (수신: 대수검존). 스크립트: `rooms/researcher3/r4/` (`g.py` 그래프·$P_G$, `a.py` 곱 예, `b.py` 여그래프 항등식, `d2.py` 정칙 그래프 탐색, `f.py` 점 개수, `h.py` 조인).

## 요약
1. **함자인 것은 $\Gamma$ 가 아니라 쿠머류 $\kappa(G)=[P_G]\in F(t)^\times/F(t)^{\times2}$ 이다.** $\kappa(G\sqcup H)=\kappa(G)+\kappa(H)$ 는 가법인데, 류에서 야코비안으로 가는 $J(\kappa)$ 는 가법이 아니다. 그래서 $\Gamma$ 는 $\sqcup\to\times$ 를 보존하지 않는다. 차원 공식은 $g(G\sqcup H)=g_G+g_H+1-|B_G\cap B_H|$ 이다. 반례: $\Gamma_{K_2\sqcup K_2}=\mathbb G_m$ (그런데 $\Gamma_{K_2}=1$), $\Gamma_{P_4\sqcup K_2}$ 는 2차원 (그런데 $1+0$). 차원이 같은 경우에도 $J(w^2=fg)$ 는 $E_f\times E_g$ 와 동종이 아니다. 예 (마름모 $\sqcup K_{1,2,2}$)에서는 2-분점 갈루아 가군은 같지만 $J$ 는 $\mathbb F_7$ 에서 단순하다.
2. **함자성이 실제로 성립하는 유일한 기제는 정리 A** 이다. $P_H=Q^2P_G$ ($Q\in F[t]$) 이면 유한 쌍유리 사상 $C_G\to C_H$, $(t,w)\mapsto(t,Qw)$ 가 있고 $\Gamma_H\twoheadrightarrow\Gamma_G$ (핵은 연결 선형군) 이다. 역도 $t$-선형 사상에 대해 성립한다. 예: $G\hookrightarrow G\sqcup 2H$, $C_3\hookrightarrow C_9$, $C_4\hookrightarrow C_8$, $C_5\hookrightarrow C_{15}$. 합집합·곱·여그래프·조인·마이너는 이 틀에 일반적으로 들어오지 않는다.
3. **곱**: $P_{G\times H}(t)=\prod_{\lambda\in{\rm spec}\,G}P_H(\lambda t)$, $P_{G\square H}(t)=\prod_\lambda \det(t(A_H+\lambda)-I)$ [증명]. $P_G,P_H$ 만으로는 결정되지 않고 $n_G,n_H$ 가 필요하다. $\Gamma_{G\square H}$ 는 $(\Gamma_G,\Gamma_H)$ 의 함수가 아니다 ($K_2$, $K_{1,3}$ 은 둘 다 $\Gamma=1$ 인데 $\Gamma_{K_2\square P_4}$ 는 3차원 아벨다양체, $\Gamma_{K_{1,3}\square P_4}$ 는 7차원). 프리즘 $K_3\square K_2$: $\Gamma=T_{15}$, $K_3$: $T_{-3}$ 이라 $\mathbb Q$ 위 사상이 0 뿐이다.
4. **여그래프**: 정칙 그래프에서 $P_{\bar G}(\tfrac{-t}{1+t})=-(1+t)^{-n}P_G(t)\tfrac{(n-k)t+1}{kt-1}$ [증명]. 곡선은 **분기점 하나(주고윳값)만 이동**한다. $\Gamma_{\bar G}\cong\Gamma_G$ 는 일반적으로 거짓이다 ($n=16$ 케일리 그래프에서 $j$ 가 다름). 비정칙 그래프에서는 $P_{\bar G}$ 가 $P_G$ 로 결정되지도 않는다 ($K_{1,4}$, $C_4\sqcup K_1$).
5. **마이너·부분그래프**: $\Gamma$ 는 함자가 아니다 (군의 종류가 어긋나 $\mathbb Q$ 위 사상이 0). 약한 단조성은 **유도부분그래프에서 $p_a$ 만** 성립한다 ($\mathrm{rank}$ 단조). 부분그래프·마이너에서는 $p_a$ 가 오르기도 내리기도 한다 ($P_4\subset C_4\subset K_4$, $C_4\to K_3$). 아벨 부분의 종수는 유도부분그래프에서도 단조가 아니다 ($P_4\subset C_5$).

## 본문

### 0. 규약과 도구

$P_G(t)=\det(tA_G-I)=\prod_{i=1}^n(\lambda_it-1)$ ($n$ 개 고윳값 전부, 0 포함 [증명]). $r=\mathrm{rank}A_G$, $\deg P_G=r$. $F$ 는 표수 0 의 체 (대부분 $\mathbb Q$). 점 $a=1/\lambda$ 에서 $P_G$ 의 중복도를 $m_G(a)$ 라 쓴다. $t=1/s$ 로 바꾸면 $C_G\cong\{v^2=(-1)^ns^{\,n\bmod 2}\chi_G(s)\}$ [증명: $w^2s^n=(-1)^n\chi_G(s)$ 에 $s^{2\lceil n/2\rceil-n}$ 곱함]. 따라서 분기점 집합은 $B_G:=\{\lambda\ne0:m(\lambda)\text{ 홀수}\}\cup\{0\text{ if }r\text{ 홀수}\}\subset\mathbb A^1_s$ (짝수 개, $\infty\notin B_G$) 이고, $g(\tilde C_G)=|B_G|/2-1=:g_G$ 이다.

**구조 사실** $[$기억-미검증: Rosenlicht–Serre$]$. $\Gamma_G$ 는 $1\to L_G\to\Gamma_G\to J(B_G)\to1$ 의 확장이다. $J(B)$ 는 $B$ 에서 분기하는 초타원곡선의 야코비안, $L_G$ 는 연결 선형군이다. 중복도 $m=2k$ 인 근은 $\mathbb T\times\mathbb G_a^{k-1}$ (토러스는 두 가지 $w=\pm(\ldots)\sqrt{u}$ 의 체 $F(\sqrt{u(a)})$ 로 꼬임), $m=2k+1$ 인 근은 $\mathbb G_a^k$ 를 준다. 합 $=p_a-g_G$ 는 모든 예에서 맞았다 ($K_3,K_4,C_5,Q_3,K_3\square K_3$ 등). 이하 이것을 쓰며 증명은 R1 몫이다.

**보조정리 L (Hom 소멸) [증명]** (i) 아핀군에서 완비군으로, 완비군에서 아핀군으로 가는 연결 군 사상은 0 이다 (연결상 이 완비이고 아핀이면 점). (ii) 표수 0 에서 토러스와 $\mathbb G_a$ 사이 사상은 0 이다 (토러스의 상은 토러스, $\mathbb G_a$ 의 상은 유니포텐트). (iii) $\mathrm{Hom}_F(T,T')=\mathrm{Hom}_{\mathrm{Gal}}(X(T'),X(T))$. 특히 계수 1 인 꼬인 토러스 $T_d$ (분해체 $F(\sqrt d)$) 는 $d\ne d'$ (제곱류) 이면 $\mathrm{Hom}_{\mathbb Q}(T_d,T_{d'})=0$.

**쿠머 틀 (관점 전환)**. 유한 차원 $F[x]$-가군 범주에서 $V\mapsto\chi_V$ 는 완전열에 대해 곱셈적이다. 그래서 $V=F^G$, $x=A_G$ 로 두면 $G\mapsto P_G\in F[t]$ 는 $\sqcup\to\times$ 의 모노이드 사상이다. 곡선 $C_G$ 는 **이차 쿠머 확대** $F(t)(\sqrt{P_G})$ 이고, 정규화와 $J(B_G)$ 는 $\kappa(G)=[P_G]\in F(t)^\times/F(t)^{\times2}\cong H^1(F(t),\mu_2)$ 만으로 결정된다. $\kappa$ 는 $\mathbb F_2$-벡터공간으로 가는 가법 함자, $J(\cdot)$ 는 그 위의 비가법 함수이다. 아래 모든 실패는 이 비가법성의 구체적 모습이다.

### 1. 함자성이 성립하는 곳: 정리 A

**정리 A [증명, 선형군 구조 부분은 기억-미검증]**. $P,P'\in F[t]$, $P'=Q^2P$ ($Q\in F[t]\setminus0$) 이면 $f_Q:C_P\to C_{P'}$, $(t,w)\mapsto(t,Qw)$ 는 $F$ 위의 유한 쌍유리 사상 (역: $w'\mapsto w'/Q$ 는 함수체에서) 이고 $f_Q^*:\ \mathrm{Pic}^0(C_{P'})\to\mathrm{Pic}^0(C_P)$ 는 전사이며 핵은 연결 선형군이다. $f_{Q'Q}=f_{Q'}\circ f_Q$ 이므로 $\Gamma$ 는 전순서 $G\preceq H\Leftrightarrow P_H/P_G\in F[t]^2$ 위의 **반변** 함자이다.

*증명.* $\nu=f_Q$ 에 대해 $O_{C_{P'}}\subset\nu_*O_{C_P}$ 이고 ($Qw$ 가 $w$ 의 다항식 배수) 몫층 $\mathcal Q=\nu_*O^\times/O'^\times$ 는 유한 지지이다. $1\to O'^\times\to\nu_*O^\times\to\mathcal Q\to1$ 의 긴 완전열에서 $H^1(\mathcal Q)=0$ 이므로 $\mathrm{Pic}\,C'\to\mathrm{Pic}\,C$ 가 전사이고 핵은 $\prod_p(O_{C,p}^\times/O_{C',p}^\times)/F^\times$ (연결 선형군) 이다. 유한 쌍유리 사상은 (다중)차수를 보존하므로 $\mathrm{Pic}^0$ 를 $\mathrm{Pic}^0$ 로 보낸다. 방향이 $C_P\to C_{P'}$ 이고 군 사상이 반대 방향인 점에 주의 ($C_{P'}$ 이 더 특이하다). $\square$

*역 (t-선형 사상) [증명 스케치]*. $t$-선으로 가는 사영과 호환되고 쌍유리인 $F$-사상 $C_P\to C_{P'}$ 은 $(t,w)\mapsto(t,Rw)$, $R\in F(t)$ 꼴이어야 하고 ($F(t)$ 위 이차 확대의 포함은 동치), $Rw$ 가 정칙이려면 $R\in F[t]$ 이어야 한다 ($w/B$ 는 정수적이지만 $k[t,w]/(w^2-P)$ 에 속하지 않는다). 따라서 $P'=R^2P$. 이 의미에서 정리 A 가 $t$-선형 함자성의 전부이다.

**중복도 해석.** $G\preceq H$ $\Leftrightarrow$ 모든 $a$ 에서 $m_H(a)\ge m_G(a)$, $m_H(a)\equiv m_G(a)\pmod2$, 상수비가 $F$ 의 제곱. 즉 **$H$ 는 $G$ 의 근들의 중복도를 짝수만큼 올린 것**이다. 오른쪽 상수에 의한 걸림: 고립점 $K_1$ 은 $P=-1$ 이라 $G\preceq G\sqcup K_1$ 은 $F\ni\sqrt{-1}$ 일 때만 성립한다.

**예 [계산 확인]** ($\mathtt q.py$, 비 $P_{C_b}/P_{C_a}$ 정확 인수분해).
- $C_3\preceq C_9$: 비 $=(t^3-3t^2+1)^2$. $C_4\preceq C_8$: 비 $=(2t^2-1)^2$. $C_5\preceq C_{15}$: 비 $=(t+1)^2(t^4+4t^3-4t^2-t+1)^2$.
- $C_3\not\preceq C_6$: 비 $=-(t-1)^2(2t+1)$ (상수 $-1$ 과 홀수 중복 근 $2t+1$). 3 이 6 을 나누는데도 피복 $C_6\to C_3$ 이 이 틀에 안 들어온다.
- $G\preceq G\sqcup 2H$ 모든 $H$ (단, $P_{2H}=P_H^2$). $G\preceq kG$ ($k$ 홀수).
  - 예: $P_{K_3\sqcup2K_2}=(t+1)^2(2t-1)(t^2-1)^2$, $\Gamma\twoheadrightarrow\Gamma_{K_3}=T_{-3}$.

### 2. 분리합 $G\sqcup H$

**2.1 [증명]** $P_{G\sqcup H}=P_GP_H$ (블록 대각), $B_{G\sqcup H}=B_G\,\Delta\,B_H$ (대칭차; $r$ 가 가법이라 $0$ 의 규칙도 일치). 따라서
$$g_{G\sqcup H}=g_G+g_H+1-|B_G\cap B_H|,$$
증명: $|B_{G\sqcup H}|=|B_G|+|B_H|-2|B_G\cap B_H|$ 이고 $g=|B|/2-1$. 둘 다 홀수 계수이면 $0\in B_G\cap B_H$ 이므로 보통 가법($|{\cap}|=1$)이지만, 그 외에는 **1 이 더 커지거나** 공통 분기점이 있으면 줄어든다. 산술종수 $p_a$ 는 $\deg=r_G+r_H$ 에서 $\lfloor(r_G+r_H-1)/2\rfloor$ 라 $r$ 가 모두 짝수이면 $p_a(G)+p_a(H)+1$ 이다.

**2.2 반례 (차원 불일치) [증명]**
- $K_2\sqcup K_2$: $P=(t^2-1)^2$. 곡선 $w^2=(t^2-1)^2$ 는 두 포물선 $w=\pm(t^2-1)$ 이 $t=\pm1$ 에서 만나는 가약 곡선. 다중차수 0 의 $\mathrm{Pic}^0=\mathbb G_m$. 그런데 $\Gamma_{K_2}=1$ ($P=1-t^2$, 원뿔). 따라서 $\Gamma_{K_2\sqcup K_2}\ne\Gamma_{K_2}^2$.
- $P_4\sqcup K_2$: $P=-(t^2-t-1)(t^2+t-1)(t^2-1)$, 차수 6 제곱무인수, 종수 2. $\Gamma_{P_4}\times\Gamma_{K_2}$ 는 1차원.
- $G\sqcup K_1$: $P=-P_G$, 즉 $\Gamma_{G\sqcup K_1}=\Gamma_G^{(-1)}$ ($-1$ 꼬임). $\Gamma_{K_1}$ 은 자명한데 $\Gamma_G$ 는 바뀐다. $P_4$ ($a_p=4,-4,-4,-4,8$ for $p=7,11,19,23,31$) 은 $-1$ 꼬임에서 부호가 반대 [계산 확인]이므로 $\mathbb Q$ 위에서 $\Gamma_{P_4\sqcup K_1}\not\cong\Gamma_{P_4}$ ($\mathbb Q(i)$ 위에서만 동형).
- 고립점의 개수는 $\Gamma$ 에서 $(-1)$ 꼬임의 홀짝으로만 남는다.

**2.3 차원이 같을 때도 실패: 클라인 덮개 [증명 + 기억-미검증(Kani–Rosen)]**. $f,g$ 서로소 제곱무인수라 하고 $X=\{u^2=f,v^2=g\}$ 로 두면 $V=(\mathbb Z/2)^2$ 가 작용하고 $X/V=\mathbb P^1$ 이며 세 몫곡선이 $C_f,\,C_g,\,D=C_{fg}$ ($w=uv$) 이다. $J(X)\sim J(C_f)\times J(C_g)\times J(D)$ [기억-미검증]. 점 개수는 초등적으로 $\#X(\mathbb F_q)=q+\sum\chi(f)+\sum\chi(g)+\sum\chi(fg)$ (+무한대 보정) 이므로 **프로베니우스 흔적에 대해** $a(X)=a(C_f)+a(C_g)+a(D)$ 가 증명된다 [증명]. 따라서
$$a_q(C_{fg})=a_q(X)-a_q(C_f)-a_q(C_g)$$
이고 $a_q(X)\ne0$ 이면 $a_q(C_{fg})\ne a_q(C_f)+a_q(C_g)$ 이다. 즉 $J(fg)$ 는 $J(f)\times J(g)$ 와 동종이 **아니다** (일반적으로).
- 직교성 [증명]: $x\in\pi_1^*J(C_f)\subset J(X)^{\sigma_1}$ 이면 $\sigma_3x=\sigma_2x$ 이므로 $D=X/\sigma_3$ 로의 노름 $(1+\sigma_3)x=(1+\sigma_2)x\in J(X)^V$ 이고 $J(X)^{V,0}$ 은 $J(X/V)=J(\mathbb P^1)=0$ 의 상. 따라서 $X$ 를 통한 대응이 만드는 $J(C_f)\to J(D)$, $J(C_g)\to J(D)$ 는 모두 **유한(비틀림)**. 즉 $t$-선 위의 표준 대응으로 얻는 자연 사상은 영 사상뿐이다.
- 군분해: 모든 $\overline{\mathbb Q}$ 위 종수 2 곡선은 $y^2=$ (육차식) $=f\cdot g$ (삼차식 둘의 곱) 이다. 모듈라이 공간이 3차원인데 $E_1\times E_2$ 와 동종인 종수 2 야코비안은 2차원 이하의 부분집합이므로 일반 $J(fg)$ 는 단순 [증명 (차원 세기), 분해 부분집합이 가산 개의 곡면이라는 사실은 기억-미검증].

**2.4 구체 예: 같은 2-분점, 다른 야코비안 [계산 확인 + 증명]**. $G=$ 마름모 $K_4-e$: $P_G=-(t+1)(4t^2+t-1)$ ($r=3$). $H=K_{1,2,2}$: $P_H=(2t+1)(4t^2+2t-1)$ ($r=3$). 두 곡선 모두 타원곡선이고 $r$ 이 홀수라 $0\in B_G\cap B_H$ 이므로 $g_{G\sqcup H}=1+1=2$ 로 차원이 맞는다.
- (a) **2-분점 갈루아 가군은 같다 [증명]**: $J(D)[2]=\{\text{짝수 부분집합 of 6 roots}\}/\langle\text{all}\rangle$. 부분군 $\mathrm{Ev}(R_f)\oplus\mathrm{Ev}(R_g)$ (차수 $2^2\cdot2^2$) 는 $\langle\text{all}\rangle=(R_f,R_g)$ 와 교집합이 0 (3 은 홀수) 이므로 $J(D)[2]$ 전체이고 $E_f[2]\oplus E_g[2]$ 와 갈루아 동형. $p=7,11,13$ 에서 프로베니우스 특성다항식의 mod 2 가 모두 $(x+1)^4$ 로 일치 [계산 확인].
- (b) **그래도 동종이 아니다 [계산 확인]**: 좋은 소수에서 ($\mathrm{disc}=2^{14}\cdot5\cdot17$).

| $p$ | $a_p(E_G)$ | $a_p(E_H)$ | 합 | $\mathrm{tr}$ Frob on $J(D)$ | 특성다항식 ($J(D)$) |
|---|---|---|---|---|---|
| 7 | 0 | −2 | −2 | 4 | $x^4-4x^3+10x^2-28x+49$ (기약) |
| 11 | −2 | 0 | −2 | 0 | $x^4+14x^2+121$ (기약) |
| 13 | −6 | 2 | −4 | 0 | $x^4+6x^2+169$ (기약) |

$J(D)$ 의 $\mathbb F_7$ 특성다항식이 $\mathbb Q$ 위 기약이므로 $J(D)_{\mathbb F_7}$ 는 **단순**. 따라서 $\mathbb Q$ 위의 모든 사상 $E\to J(D)$, $J(D)\to E$ ($E/\mathbb Q$ 는 7 에서 좋은 환원) 는 0 이다 [증명: 좋은 환원에서 $\mathrm{Hom}_{\mathbb Q}\hookrightarrow\mathrm{Hom}_{\mathbb F_7}$ 와 단순성]. 특히 $\Gamma_{G\sqcup H}$ 에서 $\Gamma_G\times\Gamma_H$ 로 가는 사상도 반대 방향도 없다.

**2.5 판정.** $G\mapsto\Gamma_G$ 는 $\sqcup\to\times$ 를 보존하지 않는다. lax (곱 → 합집합) 나 oplax 구조사상도 없다. 구조적 이유: 보존되는 것은 $\kappa$ 이고 $J(\kappa_1+\kappa_2)\perp J(\kappa_1),J(\kappa_2)$. 보존되는 부분 구조는 정리 A (§1) 의 $G\preceq G\sqcup H$ ($P_H$ 가 제곱) 뿐이다.

### 3. 곱: 데카르트 $\square$ 와 텐서 $\times$

**3.1 공식과 $\mathbb F^G$ 와의 대응 [증명]**. $F^{G\square H}=F^G\otimes F^H$ 위에서
$A_{G\square H}=A_G\otimes1+1\otimes A_H$ (크로네커 합 = 리 대수 표현 $\mathfrak{gl}(V)\oplus\mathfrak{gl}(W)\to\mathfrak{gl}(V\otimes W)$ 의 미분), $A_{G\times H}=A_G\otimes A_H$ (군 표현 $GL(V)\times GL(W)\to GL(V\otimes W)$). $\exp(A\otimes1+1\otimes B)=e^A\otimes e^B$ 이므로 $\square$ 는 $\exp$ 를 통해 $\times$ 와 같은 연산이 된다 (참고용; 대수적 수의 $\exp$ 는 단사 [린데만, 기억-미검증]). 고윳값 곱합 $\{\lambda_i+\mu_j\}$, $\{\lambda_i\mu_j\}$:
$$P_{G\times H}(t)=\prod_{\lambda\in{\rm spec}G}P_H(\lambda t),\qquad P_{G\square H}(t)=\prod_{\lambda\in{\rm spec}G}\det\big(t(A_H+\lambda I)-I\big)=\prod_\lambda(1-\lambda t)^{n_H}P_H\!\Big(\tfrac{t}{1-\lambda t}\Big).$$
(고윳값 $\lambda$ 에 대해 $\det(tA_H-(1-\lambda t)I)$.) 모두 $\overline{\mathbb Q}$ 위 인수분해로 증명 끝. 합성곱 형태: 고윳값 $\nu=\lambda+\mu$ 는 $t$-근 $a=1/\lambda$, $b=1/\mu$ 의 **병렬합** $ab/(a+b)$ 에 대응하고, $\times$ 는 $ab$ 에 대응한다. 0 고윳값(고립도 영공간)이 곱에 섞이므로 $n$ 이 필요하다.

**3.2 $P_G,P_H$ 만으로는 결정되지 않는다 [증명]**. $P_{2K_1}=P_{4K_1}=1$. 그런데 $2K_1\square K_2=2K_2$ ($P=(1-t^2)^2$) 이고 $4K_1\square K_2=4K_2$ ($P=(1-t^2)^4$) 이다. 따라서 공식에는 영공간 차원(홀짝 이상)이 필요하다.

**3.3 $\Gamma_{G\square H}$ 는 $(\Gamma_G,\Gamma_H)$ 의 함수가 아니다 [증명 + 계산 확인]**. $\Gamma_{K_2}=\Gamma_{K_{1,3}}=1$ (둘 다 원뿔).
- $K_2\square P_4$: $P=(t^2-3t+1)(t^2-t-1)(t^2+t-1)(t^2+3t+1)$, 차수 8 제곱무인수 $\Rightarrow$ 매끈한 종수 3 곡선, $\Gamma$ 는 3차원 아벨다양체.
- $K_{1,3}\square P_4$: $P=P_{P_4}^2\cdot(t^4-8t^3-7t^2+2t+1)(t^4+8t^3-7t^2-2t+1)$, 차수 16, $p_a=7$: 아벨 부분 3차원에 선형 부분 4차원 (마디 4개).
같은 입력 $(\Gamma_{K_2},\Gamma_{P_4})\cong(\Gamma_{K_{1,3}},\Gamma_{P_4})$ 가 서로 다른 군을 준다.

**3.4 쿠머류 대수 [증명]**. 고윳값 중 홀수 중복도 집합 $\mathfrak B_G\subset\mathbb A^1$ (0 포함, $|\mathfrak B_G|\equiv n$) 을 쓰면 $B_G=\mathfrak B_G\,\Delta\,(\{0\}\text{ if }n\text{ 홀수})$ 이고
$$\mathfrak B_{G\sqcup H}=\mathfrak B_G+\mathfrak B_H\ \text{(대칭차)},\quad \mathfrak B_{G\square H}=\mathfrak B_G*\mathfrak B_H\ \text{in }\mathbb F_2[(\overline{\mathbb Q},+)],\quad \mathfrak B_{G\times H}=\mathfrak B_G\cdot\mathfrak B_H\ \text{in }\mathbb F_2[(\overline{\mathbb Q},\cdot)].$$
(중복도의 홀짝은 $m_\nu=\sum_{a+b=\nu}m_am_b\equiv\#\{(a,b)\in\mathfrak B_G\times\mathfrak B_H\}$ 의 홀짝.) 곱에서는 분기점 집합이 두 집합의 **민코프스키 합 (mod 2)** 이 되어 항의 위치(아핀 구조)에 의존한다. $J(B)$ 는 $B$ 를 $\mathrm{PGL}_2$ 로 옮겨도 불변이지만 민코프스키 합은 그렇지 않으므로 $\Gamma_G$ 만으로 곱을 알 수 없다 (3.3 의 구조적 이유).

**3.5 구체 예 [계산 확인, 수식은 sympy 인수분해, 꼬임류는 마디의 접선 단위원 값]**

| 그래프 | 스펙트럼 | $P$ | 정규화 | $\Gamma$ |
|---|---|---|---|---|
| $K_2\square K_2=C_4$ | $2,0,0,-2$ | $-(2t-1)(2t+1)$ | 원뿔 | $1$ |
| $K_3\square K_2$ (프리즘) | $3,1,0^2,(-2)^2$ | $(t-1)(3t-1)(2t+1)^2$ | 원뿔, 마디 $t=-\tfrac12$ | $T_{15}$ (단위: $(t-1)(3t-1)|_{-1/2}=15/4$) |
| $K_3\square K_3$ (= $K_3\times K_3$, Paley 9) | $4,1^4,(-2)^4$ | $(t-1)^4(2t+1)^4(4t-1)$ | 원뿔, $A_3$ 두 개 | $T_3\times T_{-3}\times\mathbb G_a^2$ |
| $K_3\times K_2=C_6$ | $2,1^2,(-1)^2,-2$ | $-(t^2-1)^2(2t-1)(2t+1)$ | 원뿔, 마디 $t=\pm1$ | $T_{-3}\times T_{-3}$ |
| $P_3\square K_2$ | $\pm1\pm\sqrt2,\ldots$ | $-(t^2-1)(t^4-6t^2+1)$ | **종수 2 매끈** | 아벨 곡면 |
| $K_3$ (참고) | $2,-1^2$ | $(t+1)^2(2t-1)$ | 원뿔, 마디 | $T_{-3}$ |

- $P_3\square K_2$: 대칭 $t\mapsto-t$ 로 $J\sim E_1\times E_2$, $E_1:w^2=-(\tau-1)(\tau^2-6\tau+1)$, $E_2:u^2=-\tau(\tau-1)(\tau^2-6\tau+1)$ ($\tau=t^2,\ u=tw$). 불변량 $(I,J)=(28,-272)$ 와 $(28,272)$ 가 정확히 일치하므로 $E_2\cong E_1^{(-1)}$ [계산 확인]. 즉 $J\sim\mathrm{Res}_{\mathbb Q(i)/\mathbb Q}E_1$. 그런데 $\Gamma_{P_3}=\Gamma_{K_2}=1$: **자명한 두 인수의 데카르트 곱이 비자명한 아벨다양체를 만든다.**

**3.6 자연 사상 $\Gamma_G\times\Gamma_H\to\Gamma_{G\square H}$ 의 부재 [증명]**
- 프리즘: $\mathrm{Hom}_{\mathbb Q}(T_{-3},T_{15})=0=\mathrm{Hom}_{\mathbb Q}(T_{15},T_{-3})$ (보조정리 L (iii): 분해체 $\mathbb Q(\sqrt{-3})\ne\mathbb Q(\sqrt{15})$). $\Gamma_{K_2}=1$ 이라 $\Gamma_{K_3}\times\Gamma_{K_2}\to\Gamma_{K_3\square K_2}$ 은 영 사상뿐.
- $K_3\square K_3$: 군 $\Gamma_{K_3}^2=T_{-3}^2$ 에서 $T_{-3}$ 로의 사영은 있지만, 원소 $T_3$ 로 가는 사상은 영이고 대응 규칙이 없다. 토러스 문자군의 텐서곱 가설 $X(T_{G\square H})\overset?=X(T_G)\otimes X(T_H)$ 는 **거짓**: $X(T_{-3})\otimes X(T_{-3})=\mathbb Z$ (자명한 작용) 즉 분할 $\mathbb G_m$ 이 나와야 하는데, 실제 토러스 부분은 $T_3\times T_{-3}$ 로 분할 토러스가 없다.
- $K_3\times K_2=C_6$: $\Gamma_{C_6}\cong\Gamma_{K_3}\times\Gamma_{K_3}$ (갈루아 문자도 일치). 그러나 정규화 $w^2=1-4t^2$ 와 $w^2=2t-1$ 이 $t$-선에서 다른 이중덮개라 정리 A 의 사상이 아니다. [관찰] 일치는 $K_3$ 의 $P(t)P(-t)$ 구조에서 오는 우연일 수 있다.
- 마름모$\times K_2$ ($n=8$): $P=-(t^2-1)(4t^2-t-1)(4t^2+t-1)$ 이고 $J(D)\sim E_1\times E_2$ 로 분해, $E_2\cong E_G^{(-1)}$ ($(I,J)=(25,\pm182)$) 이고 $E_1$ 은 $E_G$ 와 다름 ($(I,J)=(145,-2162)$) [계산 확인]. 이는 $G$ 의 $P$ 에 $t$ 일차항이 없어서 ($\mathrm{tr}A_G=0$) 생기는 특수성일 수 있어 일반화하지 않는다. $J(D)\not\sim E_G^2$ ($\mathbb F_p$ 특성다항식이 $p=11,23,31$ 에서 $(x^2-a_px+p)$ 를 인수로 갖지 않음) [계산 확인].
- $G\square K_2$ 일반 ($n$ 짝수): $P_{G\square K_2}=P_G^{(1)}P_G^{(-1)}$ ($P^{(c)}(t)=(1+ct)^nP_G(\tfrac{t}{1+ct})$), 각 $C_G^{(\pm1)}\cong C_G$ (뫼비우스 $t\mapsto t/(1\pm t)$) 이므로 $C_{G\square K_2}$ 는 $C_G\times_{\mathbb P^1}C_G$ ($\psi_+,\psi_-$ 를 통한 섬유곱) 의 세 번째 몫이고, 2.3 의 직교성에 의해 표준 대응이 주는 $\Gamma^{ab}_G\to\Gamma^{ab}_{G\square K_2}$ 는 비틀림 [증명]. ($n$ 홀수이면 $(1+ct)$ 꼬임이 붙는다.)

**3.7 판정 (곱).** $\square,\times$ 에서 $\Gamma$ 는 함자가 아니다. 이유: (i) $P$ 는 $P_G,P_H$ 만의 함수가 아니다. (ii) 입력의 $\Gamma$ 가 같아도 출력이 다르다. (iii) 자명한 인수에서 비자명한 아벨다양체가 생긴다. (iv) 꼬임토러스의 분해체가 연산에 맞게 합성되지 않는다.

### 4. 여그래프와 조인

**4.1 정칙 그래프 [증명]**. $G$ 가 $k$-정칙 ($n$ 정점, 연결 아니어도 됨) 이면 $\mathrm{spec}\,\bar G=\{n-1-k\}\cup\{-1-\lambda:\lambda\ne\text{(주고윳값 하나)}\}$. 뫼비우스 변환 $\varphi(t)=-t/(1+t)$ (대합) 에 대해
$$P_{\bar G}\big(\varphi(t)\big)\,(1+t)^n=-\,P_G(t)\,\frac{(n-k)t+1}{kt-1}.$$
[증명] 비주 고윳값 $\lambda$ 의 인수: $(-1-\lambda)\varphi(t)-1=(\lambda t-1)/(1+t)$. 주고윳값 인수: $(n-1-k)\varphi(t)-1=-((n-k)t+1)/(1+t)$. 모두 곱하면 위 식. $\square$ $K_3,K_4,C_5,C_6,$ 페테르센, $Q_3,$ Paley 9, $K_{3,3}$ 에서 부호까지 정확히 확인 [계산 확인] ($\mathtt b.py$, `simplify(lhs+rhs)==0`).

**귀결 [증명]** $S_G:=P_G/(kt-1)$ 이라 두면 $n$ 짝수일 때 $C_{\bar G}\cong\{w^2=-S_G(t)\,((n-k)t+1)\}$, $C_G=\{w^2=S_G(t)(kt-1)\}$. 즉 **분기점 하나가 $1/k\mapsto-1/(n-k)$ 로 이동**한다. $n$ 홀수이면 점 $t=-1$ ($\varphi$ 의 극) 도 분기점이 된다. 특이점은 $\lambda=-1$ (중복도 $m$) 이 $\bar G$ 에서 영고윳값으로 바뀌어 **사라지고** ($t'=\infty$ 로 이동), $G$ 의 영고윳값이 $\bar G$ 의 $-1$ 고윳값으로 **새로 생긴다.**

**4.2 $\Gamma_{\bar G}\cong\Gamma_G$ 는 일반적으로 거짓 [계산 확인]**
- $K_n$: $\Gamma_{K_n}$ 은 선형군 ($n=3$: $T_{-3}$, $n=4$: $\mathbb G_a$), $\bar K_n=nK_1$ 은 $P=\pm1$ 로 자명.
- $K_3\to\bar K_3=3K_1$: $\Gamma$ 가 $T_{-3}$ 에서 자명군으로.
- $Q_3$ (정육면체, $n=8,k=3$): $P=(t^2-1)^3(9t^2-1)$, $\bar Q_3$: $(2t-1)(2t+1)^3(4t-1)$. 아벨 부분은 $\mathbb Q$ 위에서 동형: 두 정규화 $w^2=(t^2-1)(9t^2-1)$, $w^2=(4t^2-1)(4t-1)$ 의 불변량이 정확히 $(I,J)=(208,-4480)$ 로 같다 [증명: 기호 계산]. 이유: $n=2k+2$ 이고 스펙트럼이 대칭이면 이동한 점이 대칭 이미지로 돌아온다. 그런데 선형 부분: $\Gamma_{Q_3}=E\times\mathbb G_a^2$ (3차원), $\Gamma_{\bar Q_3}=E\times\mathbb G_a$ (2차원, $p_a=2$). **차원이 다르다.**
- **아벨 부분마저 다른 예** [계산 확인]: $n=16$, $X_{16}=\mathrm{Cay}(\mathbb Z_2^4,\{1,2,4,8,7\})$ (5-정칙, 이분, 스펙트럼 $\pm5,\pm3$ 단순, $\pm1$ 중복도 6). $B_G=\{\pm5,\pm3\}$ (타원곡선 $w^2=(9t^2-1)(25t^2-1)$, $j=13997521/225$). 여그래프 (10-정칙): 단순 고윳값 $10,4,-4,2$ 와 $-2$ (중복도 6), $0$ (중복도 6). $j=7189057/3969$. **$j$ 가 다르다.** 또한 $a_p$ 가 $p=11$ ($-4$ vs $4$), $p=17$ ($2$ vs $-6$) 에서 달라 동종도 아니다 ($p=13,29$ 에서 우연히 같음).

**4.3 비정칙 그래프에서는 $P_{\bar G}$ 가 $P_G$ 로 결정되지 않는다 [증명]**. $\chi_{\bar G}(x)=(-1)^n\chi_G(-x-1)\big(1+W_G(-x-1)\big)$, $W_G(y)=\mathbf 1^T(yI-A_G)^{-1}\mathbf 1=\sum_i\beta_i^2/(y-\lambda_i)$ ($\beta_i$ 주각). 따라서 주각이 필요하다. 예: $K_{1,4}$ 와 $C_4\sqcup K_1$ 은 동스펙트럼 ($\lambda^3(\lambda-2)(\lambda+2)$) 이고 $P=(2t-1)(2t+1)$ 로 같지만 여그래프는
- $\overline{K_{1,4}}=K_4\sqcup K_1$: $P=(t+1)^3(3t-1)$, $\Gamma=\mathbb G_a$.
- $\overline{C_4\sqcup K_1}=$ 나비: $P=-(t-1)(t+1)^2(4t^2+t-1)$, 접선 단위원 $=4$ (제곱) 이라 마디가 분할: $1\to\mathbb G_m\to\Gamma\to E\to1$, $E:w^2=-(t-1)(4t^2+t-1)$. 
**$\Gamma_{\bar G}$ 는 $P_G$ (따라서 $\Gamma_G$) 의 함수가 아니다.**

**4.4 조인 [증명]**. $G\vee H=\overline{\bar G\sqcup\bar H}$. 직접: $\chi_{G\vee H}(x)=\chi_G\chi_H\big(1-W_G(x)W_H(x)\big)$ (슈어 보수 + 행렬 행렬식 보조정리). 정칙 $G$ ($n_1,k_1$), $H$ ($n_2,k_2$) 이면
$$P_{G\vee H}(t)=P_GP_H-n_1n_2t^2\,\frac{P_GP_H}{(k_1t-1)(k_2t-1)}=S_GS_H\,q(t),\quad q=(k_1k_2-n_1n_2)t^2-(k_1+k_2)t+1.$$
즉 두 주고윳값 인수 $(k_1t-1)(k_2t-1)$ 이 이차식 $q$ 로 교체된다. $C_5\vee K_2$, $K_3\vee K_3=K_6$, $C_4\vee C_5$ 에서 확인 [계산 확인] ($\mathtt h.py$). 곡선은 $w^2=S_GS_Hq$ 이므로 $S_G\ne$ 제곱이면 §2.3 의 클라인 구조가 그대로 나타난다. $q$ 의 판별식은 $(k_1-k_2)^2+4n_1n_2>0$ 이라 $q$ 는 항상 제곱무인수이므로, $P_{G\vee H}/P_G$ 가 제곱이 되려면 $S_Hq\cdot(k_1t-1)^{-1}\cdots$ 꼴이 제곱이어야 하는데 일반적으로 아니다. 정리 A 의 사상은 일반적으로 없다 [추측: 모든 조인에서 없음 미증명]. 조인에서 $\Gamma$ 가 함자라는 근거는 없다.

**4.5 문주님의 "그래프와 여그래프" 질문과의 연결.** 여그래프는 $F^G$ 위에서 $A\mapsto J-I-A$ ($J=\mathbf 1\mathbf 1^T$) 인 **아핀** 변환이다. 주고윳값(= $\mathbf 1$ 방향) 하나만 $k\mapsto n-1-k$ 로 따로 이동하고 나머지는 $\lambda\mapsto-1-\lambda$. 이 방향이 곡선에서 보이는 것은 **일차 분기점 하나의 이동**이다. 결론: 정칙 그래프에서 $\Gamma_G$ 와 $\Gamma_{\bar G}$ 는 한 매개변수족 $\{w^2=S_G(t)\,(ct+1)\}_c$ 의 두 섬유이지 함자적 관계가 아니다. 동일한 섬유가 되는 것은 $\bar G$ 와 $G$ 가 동스펙트럼 (자기여: Paley 9, $C_5$) 이거나 대칭 때문의 우연 ($Q_3$) 뿐이다.

### 5. 부분그래프·마이너

**5.1 정리 (마이너에서 $\Gamma$ 는 함자가 아니다) [증명, 구조 사실 제외]**. 유도부분그래프이든 (생성) 부분그래프이든 마이너이든, $H\le G$ 인 쌍 중에는 $\mathbb Q$-군 사상 $\Gamma_H\to\Gamma_G$ 도 $\Gamma_G\to\Gamma_H$ 도 영 사상뿐인 쌍이 있다 (따라서 이 관계 전부에 걸친 함자 $\Gamma$ 는 존재하지 않는다). 다음 반례가 증명한다.
- **$K_3\subset K_4$ (유도).** $\Gamma_{K_3}=T_{-3}$ (꼬인 토러스, $|\Gamma(\mathbb F_q)|=q-(\tfrac{-3}q)$), $\Gamma_{K_4}=\mathbb G_a$ (첨점, $|\Gamma(\mathbb F_q)|=q$). 보조정리 L (ii): $\mathrm{Hom}(T_{-3},\mathbb G_a)=0=\mathrm{Hom}(\mathbb G_a,T_{-3})$.
- **$P_4\subset C_5$ (유도).** $\Gamma_{P_4}=E$ ($w^2=t^4-3t^2+1$, $j=148176/25$, $(I,J)=(21,-162)$), $\Gamma_{C_5}$: $P=(2t-1)(t^2-t-1)^2$, 마디 두 개가 $\mathbb Q(\sqrt5)$ 위 켤레라 $\Gamma_{C_5}=\mathrm{Res}_{\mathbb Q(\sqrt5)/\mathbb Q}(\text{rank-1 torus})$ (2차원 토러스). 보조정리 L (i): $\mathrm{Hom}(E,T)=0=\mathrm{Hom}(T,E)$.
- 두 반례 모두 $H\subset G$ 가 **유도**부분그래프 (정점 삭제) 이므로 가장 약한 형태의 포함에서도 함자성이 깨진다.
- 일반 원리: 모든 $\Gamma$ 는 선형군 $L$ 과 아벨다양체의 확장이라 군 사상은 $L\to L'$ 과 $A\to A'$ 로 갈라지고 ($A\to L'$, $L\to A'$ 는 0), 마이너 연산은 두 부분의 종류를 바꾼다.

**5.2 약한 단조성**
- **(M1) [증명]** 유도부분그래프 $H\le G$ 이면 $p_a(H)\le p_a(G)$. 이유: $\mathrm{rank}A_H\le\mathrm{rank}A_G$ (주부분행렬) 이고 $p_a=\lfloor(\mathrm{rank}-1)/2\rfloor$.
- **(M2) [증명]** 정점 하나 삭제로 $p_a$ 는 최대 1 줄어든다: $\mathrm{rank}A_G-2\le\mathrm{rank}A_{G-v}\le\mathrm{rank}A_G$ (행·열 삭제의 계수 변화 $\le2$) 이므로 $p_a(G)-1\le p_a(G-v)\le p_a(G)$.
- **(M3) [증명, 반례]** 부분그래프·마이너에서는 $p_a$ 가 단조가 아니다: $P_4\subset C_4$ (간선 삭제): $\mathrm{rank}\,4\to2$, $p_a:1\to0$ (내려감). $C_4\subset K_4$ (간선 추가): $2\to4$, $p_a:0\to1$ (올라감). $C_4\to K_3$ (간선 수축으로 마이너): $\mathrm{rank}\,2\to3$, $p_a:0\to1$. 따라서 $p_a$ 는 부분그래프 순서와 마이너 순서 어느 쪽에도 단조/반단조가 아니다.
- **(M4) [증명, 반례]** 아벨 부분의 종수 $g_G$ 는 유도부분그래프에서도 단조가 아니다: $P_4\subset_{\rm ind}C_5$ 에서 $g:1\to0$. 토러스 계수도 아니다: $K_3\subset_{\rm ind}K_4$ 에서 $1\to0$. 즉 (M1) 은 $\dim\Gamma$ 의 합 불변량으로만 성립하고 **어느 구성 성분도 단조가 아니다.** 
- **(M5)** 코시 인터레이싱에 따라 $G-v$ 의 고윳값이 $G$ 의 고윳값 사이에 끼므로 (실수 분기점이 서로 끼워짐) 두 곡선은 같은 $\mathbb P^1_s$ 위의 이중덮개로 비교되지만 분기점 집합은 포함 관계가 없다. 이를 사상으로 만드는 방법은 찾지 못함 [추측: 없다].

### 6. 판정표 (함자인 범주와 아닌 범주의 경계)

| 연산·범주 | $P$ 의 변화 | $\Gamma$ 의 함자성 | 근거 |
|---|---|---|---|
| 동형, 동스펙트럼 ($\mathrm{Aut}(G)$ 는 자명하게 작용) | $P$ 불변 | **함자** (이름만의 함자: $\Gamma_G$ 는 $P_G$ 에만 의존) | $P_G$ 의 정의 |
| 체 확대 $F'/F$ | 불변 | **함자** (R1) | 기저변환 |
| 중복도를 짝수만큼 올림: $P_H=Q^2P_G$ ($G\sqcup2H$, $kG$ ($k$ 홀수), $C_n\to C_{mn}$ (홀짝 일치) 등) | $P_H/P_G\in F[t]^2$ | **반변 함자**, $\Gamma_H\twoheadrightarrow\Gamma_G$, 핵 연결 선형군 | 정리 A |
| 일반 피복 $H\to G$ | $P_H=P_GR$, $R$ 일반 | 정리 A 의 조건 $R$ 이 제곱일 때만 (R2 담당) | 쿠머류 $\kappa(H)=\kappa(G)+\kappa(R)$ |
| 분리합 $G\sqcup H$ | $P_GP_H$ | $\sqcup\to\times$ **보존 안 함**; $\kappa$ 는 가법, $g=g_G+g_H+1-|B_G\cap B_H|$ | §2.1–2.4 |
| 고립점 추가 $G\sqcup K_1$ | $-P_G$ | $-1$ 꼬임 ($\mathbb Q(i)$ 위에서만 동형) | §2.2 |
| 데카르트곱 $\square$ | $\prod_\lambda P_{H+\lambda}$ | **아님** ($(\Gamma_G,\Gamma_H)$ 의 함수 아님, $n$ 필요) | §3.2–3.6 |
| 텐서곱 $\times$ (이분 이중덮개 포함) | $\prod_\lambda P_H(\lambda t)$ | **아님** (자연 사상 부재, 토러스 문자군 텐서곱 거짓) | §3.1,3.6 |
| 여그래프 (정칙) | 분기점 하나 이동 | **아님**; $Q_3$ 아벨 부분만 동형, $X_{16}$ 은 $j$ 다름 | §4.1–4.2 |
| 여그래프 (일반) | 주각 필요 | $P_{\bar G}$ 가 $P_G$ 로 결정 안 됨 | §4.3 |
| 조인 | $S_GS_Hq$ | **아님** | §4.4 |
| 유도부분그래프 | 차수 $r$ 단조 | $\Gamma$ 는 함자 **아님**; $p_a$ 만 단조 (M1, M2) | §5 |
| 부분그래프, 마이너 | 임의 | **함자 아님; $p_a$ 도 단조 아님** | §5 |

경계의 한 줄 요약: **$t$-선 위에서 정규화가 같은 곡선 사이(= $\kappa$ 같음, 중복도만 짝수만큼 다름)에서만 $\Gamma$ 는 함자이고, $\kappa$ 가 바뀌는 모든 연산($\sqcup,\square,\times$, 여그래프, 조인, 마이너)에서는 함자가 아니다.** 후자에서는 $J(\kappa_1+\kappa_2)$ 가 $J(\kappa_1),J(\kappa_2)$ 와 직교하는 새 야코비안이다.

### 7. 증명 시도와 장애물

증명한 것: 정리 A (사상 존재, 전사, 선형 핵, 역), 쿠머 가법성, 종수 공식, 직교성(§2.3), 곱 공식, 여그래프 항등식, 조인 공식, 마이너 반례의 Hom 소멸, (M1)–(M4), $J(fg)[2]\cong J(f)[2]\oplus J(g)[2]$ (홀-홀).
**장애물 1**: "$J(fg)$ 가 $J(f)\times J(g)$ 와 동종이 아니다" 의 **모든 그래프쌍**에서의 증명. 한 쌍(마름모, $K_{1,2,2}$) 에서는 $\mathbb Q$ 위 사상만 소멸 증명 ($\mathbb F_7$ 특성다항식이 기약). $\overline{\mathbb Q}$ 위 동종 여부는 미증명이다 (유한 확대 위에서 $\mathbb F_7$ 의 확대체 특성다항식이 계속 비분해인지 확인해야 함).
**장애물 2**: 정리 A 의 역 (임의의, $t$-선과 호환되지 않는 군 사상까지) 은 증명하지 않았다. 호환되는 쌍유리 사상으로만 증명.

## 문주님께 요청
없음 (이번 라운드는 문헌 없이 진행했고, 문헌에 의존한 부분은 모두 `[기억-미검증]` 로 표시).

## 후속연구 지점
1. **일반 단순성 판정: 갈루아군 $S_N$ 이면 $\mathrm{End}\,J=\mathbb Z$ 인가 (Zarhin 류 [기억-미검증]).** 왜: 이것이 되면 "$G,H$ 의 분기점 집합이 서로소이고 $\kappa_G\cdot\kappa_H$ 의 분해체의 갈루아군이 $S_{2g+2}$ 이면 $\Gamma^{ab}_{G\sqcup H}$ 단순 → 모든 연산($\sqcup,\square,\times$, 여, 조인)에서 비함자성이 반례 없이 증명된다. 시작: 스펙트럼의 최소다항식 갈루아군을 sympy 로 계산해 $\sqcup$, $\square$, $\times$ 에서 $S_N$/$A_N$ 판정 (소수 분해 모양 한 개로 충분), 그 뒤 Zarhin 판정 대입. 난점: 그래프 스펙트럼은 실수 대수적 정수이며 갈루아군이 작은 경우(순환·케일리)가 많음.
2. **정칙 그래프 여그래프의 한 매개변수족 해석과 분류.** 왜: $\{w^2=S_G(t)(ct+1)\}_c$ 의 두 섬유 $c=-k$ 와 $c=n-k$ ($t=-1/(n-k)$ 에서의 인수는 $(n-k)t+1$) 이 언제 동형·동종인지 (예: $n=2k+2$ 와 스펙트럼 대칭이면 동형, $Q_3$ 이 유일한 하이퍼큐브). 시작: 케일리 그래프 $\mathbb Z_2^a$ ($a=4,5$) 에서 $(G,\bar G)$ 의 $j$ 불변량 전수표를 만들고 (분류가 아니라 가설 형성용) 동형이 되는 조건을 명시적으로 증명. 난점: 위수 2 군은 중복도가 짝수라 분기점이 적음 → 다른 군 필요.
3. **$\square,\times$ 에서 꼬인 토러스의 분해체 공식.** 왜: 마디의 꼬임류는 $\mathbb Q(\sqrt{u(1/\nu)})$ 이고 ($K_3\square K_2\to\sqrt{15}$, $K_3\square K_3\to\sqrt3,\sqrt{-3}$) 고윳값의 산술 (판별식, 호프만 관계식) 로 닫힌 식을 얻을 수 있는지 불명. 시작: 해밍 그래프 $K_a\square K_b$ 의 스펙트럼 $\{(a-1)+(b-1), (a-1)-1,\ldots\}$ 에서 $u(1/\nu)=\prod_{\mu\ne\nu}(\mu/\nu-1)$ 의 제곱류를 $a,b$ 의 함수로 표로 만들고 증명. 난점: 중복도가 크면 $\mathbb G_a$ 계수도 같이 추적해야 함.
4. **정리 A 의 순서 구조 분류.** 왜: $G\preceq H$ ($P_H/P_G$ 제곱) 가 되는 그래프 쌍을 구성적으로 목록화 (순환 $C_n\preceq C_{mn}$, 쌍선형 등) 하면 R2 의 피복 결과와 합쳐 "$\Gamma$ 가 함자인 범주" 를 완전한 순서집합으로 기술할 수 있다. 시작: $P_{C_n}$ 의 $\cos$ 인수 구조로 $C_a\preceq C_b$ $\Leftrightarrow$ $a\mid b$ 이고 $a\equiv b\pmod2$ 임을 증명 (현재 $a,b\le 15$ 몇 쌍만 확인), 이어서 케일리 그래프의 몫(= 군 몫)으로 일반화. 난점: 상수 인자(-1)와 홀수 중복 근이 홀짝 조건으로 들어옴.
5. **약한 단조성의 정확한 판: 유도부분그래프에서 $L_G$ 와 $J(B_G)$ 의 각 성분에 대해 인터레이싱이 주는 정확한 부등식.** 왜: (M1)–(M4) 는 합차원만 단조임을 보였는데, 선형군의 총차원 $p_a-g_G$ 와 $g_G$ 사이의 "교환 규칙" (한 정점 삭제로 $g$ 가 감소하면 $p_a-g$ 가 증가한다 등) 이 있을 수 있다. 시작: $n\le 7$ 의 모든 그래프에서 유도부분그래프 쌍 $(H,G)$ 에 대해 $(p_a,g,p_a-g)$ 의 변화 표를 만들어 보존 법칙 가설을 세우고 인터레이싱으로 증명 (통계는 가설 형성용). 난점: 인터레이싱은 실수 구조만 주고 $\mathbb Q$ 구조를 주지 않음.
