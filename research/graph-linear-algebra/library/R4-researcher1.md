# [R4-researcher1] Γ_G 의 엄밀한 정의, 체에 대한 함자성, 구조정리와 위수 공식

- 작성자: researcher1 · 라운드: R4 · 역할: 연구원(포메이션 I 분담, 주제 = 함자성만). 수신: 대수검존
- 코드: `rooms/researcher1/r4_gamma.py` (인수분해·구조 자료·위수 공식 대 점 개수 대조), `r4_extra.py` (Kneser(6,2), $K_n$ 일반식, $P_4$ 바이어슈트라스 대조)

## 요약
- [증명] $P_G=(-1)^{\mathrm{null}A}\prod_{\lambda\ne0}(\lambda t-1)^{m_\lambda}$, $d=n-\operatorname{ord}_0\chi_A$. $C_G$ 는 "경계가 매끈한 유일한 사영 완비화"로 정의하면 모델에 무관하고 ($\mathbb P(1,1,\lceil d/2\rceil)$ 이 그것), $\Gamma_G:=\mathrm{Pic}^0_{C_G/F}$ 는 $1\to L\to\Gamma_G\to J(\tilde C)\to1$, $\tilde C:w^2=S_0$ ($S_0$=홀수 중복도 고윳값만 모은 제곱무인수 부분). 국소 기여: 중복도 $2k$ → $\mathbb G_m^{\rm tw}\times\mathbb U_{k-1}$, 홀수 $2k+1\ge3$ → $\mathbb U_k$, 1 → 없음 ($\mathbb U_j$=차원 $j$ 의 단위근기군; 표수 0 에서 $\mathbb G_a^j$).
- [증명] **연결 그래프는 항상 $C_G$ 가 기하적으로 기약**이다(페론 고윳값이 단순). $P_G$ 가 완전제곱인 경우(비연결 그래프에서만)는 "두 유리곡선이 만난 곡선"이고 $\Gamma_G=(F[t]/Q)^\times/F^\times$ ($P_G=cQ^2$), $c\equiv(-1)^{\mathrm{null}}$ 제곱류 (null 홀수이면 두 성분이 켤레).
- [증명] 체 사상 $F\to F'$ 에 대해 $\Gamma_G(F)\to\Gamma_G(F')$ 는 공변함자이고 **항상 단사**, 갈루아 하에서 $\Gamma_G(F)=\Gamma_G(F^{\rm sep})^{\rm Gal}$. $\mathbb Q\to\mathbb F_p$ 는 체 사상이 아니라서 함자성이 없고, 좋은 소수에서 정수 모델 $\mathcal P$ 로 $\mathcal P(\mathbb Z_p)\twoheadrightarrow\Gamma_G(\mathbb F_p)$ 가 있다 (분할 토러스가 있으면 $\Gamma_G(\mathbb Q_p)$ 전체에는 정의되지 않음). $K_3$ 는 $p=3$ 에서 꼬인 토러스 → $\mathbb G_a$ (가법 환원).
- [증명 + 계산 확인] 위수 공식 $|\Gamma_G(\mathbb F_q)|=|J(\tilde C)(\mathbb F_q)|\prod_{x}(\text{국소 인자})$ (아래 정리 4). $K_n$: $n$ 홀수 $q^{(n-3)/2}\bigl(q-(\tfrac{-n}{q})\bigr)$, $n$ 짝수 $q^{(n-2)/2}$. $K_3,K_4,K_5,C_5,P_4,K_{2,2,2},$ 페테르센, $Q_3$, $P_5$, $2K_2$, $2K_3$, $K_{3,3}$, $K_{2,2,2,2}$, Kneser(6,2) 를 소수 $q=5\sim23$ 에서 점 개수·바이어슈트라스와 대조 불일치 0. 부호 주의: $K_{2,2,2}$ 는 $K_3$ 와 $t\mapsto 2t$ 로 같지 않고 $(-1)^{\mathrm{null}}$ 때문에 $-1$-꼬임 ($q-(\tfrac3q)$).
- [증명] $g(\tilde C)=0$ (홀수 중복도 고윳값이 $\le2$ 개) 일 때 $\Gamma_G\cong T\times U$ 선형군; 분류표는 §6. 완전분해 가능 예: $K_n$, 완전다분, 페테르센, srg.

## 본문

### 0. 기호와 약속
$F$ 는 표수 $\ne2$ 인 체, $A=A_G\in\{0,1\}^{n\times n}$ 대칭(루프 허용), $\chi_A(x)=\det(xI-A)$. 모든 주장에 §표기 규칙을 붙인다.

**보조사실 0.1** [증명]. $P_G(t)=\det(tA-I)=(-1)^n t^n\chi_A(1/t)$. 따라서 $d:=\deg P_G=n-\operatorname{ord}_{x=0}\chi_A$ (대수적 중복도), 최고차계수 $c=(-1)^{\mathrm{null}}\prod_{\lambda\ne0}\lambda^{m_\lambda}$ ($\mathrm{null}$=0 의 중복도), $P_G(0)=(-1)^n$. $\mathbb Q$ 에서는 $A$ 가 실대칭이므로 $d=\operatorname{rank}A$. 표수 $p$ 에서는 $d_p=n-\operatorname{ord}_0(\chi_A\bmod p)\ge\operatorname{rank}_pA$ — **계수 아닌 대수적 중복도**로 $d$ 가 정해진다.

**보조사실 0.2 (부호)** [증명]. $\det(I-tA)=(-1)^nP_G$ 이므로 문주님 정의 $w^2=\det(tA-I)$ 와 $w^2=\det(I-tA)$ 는 $n$ 홀수일 때 $-1$-꼬임 관계. 토러스의 꼬임체가 달라진다(예: $K_3$: $\mathbb Q(\sqrt{-3})$ 대 $\mathbb Q(\sqrt3)$). 이 보고서는 문주님 정의 $\det(tA-I)$ 고정.

$\bar F$ 위에서 $P_G=c\prod_a(t-a)^{m_a}$, $a=1/\lambda$ 는 서로 다른 근(= 서로 다른 0 아닌 고윳값의 역수), $m_a=m_\lambda$. 근을 분류한다: $E$=짝수 중복도 근, $O_1$=중복도 1, $O_3$=홀수 $\ge3$. $S_0:=c\prod_{a\in O_1\cup O_3}(t-a)$ (제곱무인수, 구성상 $F$ 위 정의됨), $k_a:=\lfloor m_a/2\rfloor$, $Q:=\prod_a(t-a)^{k_a}$. 그러면
$$P_G=S_0\,Q^2 .$$
$s:=\deg S_0$ ($=|O_1|+|O_3|$ 개수; $s\equiv d\pmod2$). 정규화 곡선 $\tilde C:\ \tilde w^2=S_0(t)$, $\tilde w=w/Q$.

### 1. 정의의 엄밀화

**1.1 사영 모델과 무한원점** [증명]. 가중사영 $\mathbb P(1,1,e)$, $e=\lceil d/2\rceil$ 의 좌표 $(t:z:w)$, 방정식 $w^2=\hat P(t,z):=z^{2e-d}\prod(\lambda t-z)^{m_\lambda}\cdot(\pm)$ (차수 $2e$ 의 동차화). $z=0$ 에서: $d$ 짝수이면 $w^2=ct^{2e}$ 로 서로 다른 두 점 $(1:0:\pm\sqrt c)$ (둘 다 매끈, $c$ 가 제곱이 아니면 $F(\sqrt c)$ 위에서 켤레), $d$ 홀수이면 $w^2=z\cdot(\text{단위})$ 라 한 점 $(1:0:0)$ 이 매끈한 분기점. 즉 $\infty$ 는 중복도 $2e-d\in\{0,1\}$ 의 근으로 취급되고 **항상 매끈**하다. 따라서 $C_G$ 는 "두 겹 덮개 $C_G\to\mathbb P^1$ 이 분기하는 이진형식 $\hat P$ 의 홀수 중복도 점들(∞ 포함)"으로 통일된다.

**명제 1.2 (모델 독립성)** [증명]. $U_G:=\operatorname{Spec}F[t,w]/(w^2-P_G)$ 를 아핀 부분이라 하자. $U_G$ 를 조밀 열린집합으로 갖고 경계가 모두 $C$ 의 매끈점인 **고유(proper) 기하적 기약 또는 연결 축소 곡선**은 동형을 제외하고 유일하다.
증명: 경계점 $y$ 가 매끈하면 $\mathcal O_{C,y}$ 는 DVR 이고 정규화 $C^\nu$ 의 대응점의 국소환과 같다. 따라서 $C=U_G\cup\{C^\nu\text{의 경계점들의 DVR}\}$ 로 $C^\nu$ (= $U_G$ 의 정규화의 유일한 매끈 완비화) 와 $U_G$ 에서 복원된다. ∎
따름: 가중사영 $\mathbb P(1,1,e)$ 모델, $d$ 짝수일 때 $\mathbb P^1\times\mathbb P^1$ 모델 등 **경계가 매끈하기만 하면** 같은 $\mathrm{Pic}^0$ 를 준다. 반대로 $e'>e$ 인 $\mathbb P(1,1,e')$ 모델($w^2=z^{2(e'-e)}\hat P$)은 $\infty$ 에서 특이(마디/첨점)라 $\mathrm{Pic}^0$ 가 달라진다 — 이것은 "모델 선택"이 아니라 다른 곡선이다. 정수 모델의 소수 환원에서 이 현상이 실제로 생긴다 (§2.4).

**정의 1.3** [증명 가능한 정의]. $\Gamma_G:=\mathrm{Pic}^0_{C_G/F}$ = 픽 스킴 $\mathrm{Pic}_{C_G/F}$ 의 항등성분 ($\bar F$ 위에서 각 기약성분 위 차수 0 인 가역층의 군). $\Gamma_G(F):=\mathrm{Pic}^0_{C_G/F}(F)$ ($F$-점; $C_G(F)\ne\emptyset$ 이면 $\mathrm{Pic}^0(C_G)$ 와 같다. $d$ 홀수이면 $\infty$ 가 유리점; 유한체면 항상 같음 — 유한체 브라우어군 0).
- $d\ge1$ 이면 $C_G$ 는 기하적으로 연결·축소·고유이므로 $H^0(\mathcal O)=F$ 가 보편적이고 픽 스킴은 기저변환과 호환 [표준, 기억-미검증], 항등성분은 임의 체 확대와 호환 [SGA3, 기억-미검증]. $\Gamma_G$ 는 차원 $p_a=\lfloor(d-1)/2\rfloor$ 의 매끈한 연결 가환 대수군(곡선은 $H^2(\mathcal O)=0$ 이라 매끈).
- **$A=0$ ($d=0$)**: $P_G=(-1)^n$ 상수, $C_G=\operatorname{Spec}F[w]/(w^2-(-1)^n)$ (점 2개 또는 차수 2 점 1개), 1차원 이하 → $\Gamma_G=1$. ($p_a=\lfloor(0-1)/2\rfloor=-1=1-\chi(\mathcal O)$ 로 공식 일관.)
- **$d=1,2$, $P_G$ 제곱무인수**: $C_G$ 는 매끈한 원뿔곡선 ($\mathbb P^1$ 형), $\Gamma_G=1$.
- **$d=2$, $P_G=c(t-a)^2$**: 두 직선이 한 점에서 가로지르는 곡선, $p_a=0$, $\Gamma_G=1$.

**1.4 정규화와의 관계 (일반화 야코비안)** [증명 + 표준]. 정규화 $\pi:\tilde C\to C_G$ ($\tilde C$ 는 $s\ge1$ 일 때 $\tilde w^2=S_0$ 의 매끈 완비화, 종수 $\tilde g=\lceil s/2\rceil-1$). 층열 $1\to\mathcal O_C^\times\to\pi_*\mathcal O_{\tilde C}^\times\to\bigoplus_x\tilde{\mathcal O}_x^\times/\mathcal O_x^\times\to1$ 의 코호몰로지 열: $s\ge1$ ($\tilde C$ 연결, $H^0(\mathcal O^\times)=\bar F^\times$ 양쪽 동형) 이면
$$1\to L\to\Gamma_G\to J(\tilde C)\to1,\qquad L:=\prod_{x\in\mathrm{Sing}}\tilde{\mathcal O}_x^\times/\mathcal O_x^\times\ \ (\text{연결 선형군, }\dim L=\delta:=p_a-\tilde g).$$
(세르 일반화 야코비안과 같은 구성; 정규화 $\tilde C$ 위 계수 $\mathfrak m=\pi^*(\operatorname{div}Q)$ 의 $J_{\mathfrak m}(\tilde C)\twoheadrightarrow\Gamma_G$ 는 유니포텐트 핵을 갖는 전사이고 $m_a\ge5$ 홀수 또는 짝수 $\ge4$ 의 안쪽에서 핵이 생김 [기억-미검증, 이번 보고서에서 사용 안 함]).

**1.5 국소 계산 (핵심 보조정리)** [증명]. 특이점 $a$ (중복도 $m\ge2$), 국소 매개 $u=t-a$, $w^2=u^m U(u)$, $U(0)=:U_a\ne0$ (표수 $\ne2$ 이므로 $U$ 는 완비국소환에서 제곱이 있어 $w^2=u^mU_a$ 로 정규화 가능).
(a) $m=2k$: $\tilde{\mathcal O}_x=B[[u]]$, $B:=\kappa[\beta]/(\beta^2-U_a)$ ($\kappa$=점의 잉여체; $\bar F$ 위에서 $B=\bar F\times\bar F$, 두 가지), $\mathcal O_x=\{f\in B[[u]]:\ f\equiv\sigma f\bmod u^k\}$ ($\sigma:\beta\mapsto-\beta$; $w\mapsto u^k\beta$ 의 상). $f\mapsto f/\sigma f\bmod u^k$ 는 동형
$$\tilde{\mathcal O}_x^\times/\mathcal O_x^\times\ \cong\ \{g\in(B[u]/u^k)^\times:\ g\,\sigma(g)=1\},$$
차원 $k$. 상수부분이 노름 1 토러스 $R^1_{B/\kappa}\mathbb G_m$ (분할 $\Leftrightarrow U_a$ 가 $\kappa$ 에서 제곱), 나머지 $1+uB[u]/u^k$ 의 $\sigma$-역불변 부분이 차원 $k-1$ 유니포텐트군.
(b) $m=2k+1$, $k\ge1$: 단일가지, 정규화 매개 $v$ ($u=v^2$, $w=v^{2k+1}$), $\mathcal O_x=\bar F[[v^2,v^{2k+1}]]$. 반군 $\langle2,2k+1\rangle$ 의 간격 $1,3,\dots,2k-1$ ($k$ 개) → $\delta_x=k$, $\tilde{\mathcal O}_x^\times/\mathcal O_x^\times=(1+v\bar F[[v]])/(\cdots)$ 순수 유니포텐트 차원 $k$.
(c) $m=1$: 매끈, 기여 없음.
점검 [증명]: $\delta=\sum_{E}k_a+\sum_{O_3}k_a$, $d=s+2\delta$ 이므로 $p_a=\lfloor(d-1)/2\rfloor=\lfloor(s-1)/2\rfloor+\delta=\tilde g+\delta$ ✓ ($\tilde g=\lceil s/2\rceil-1=\lfloor(s-1)/2\rfloor$).

**1.6 짝수 중복도의 요약표** [증명]
| 근 $a$ 의 중복도 $m$ | $k=\lfloor m/2\rfloor$ | 국소 기여 $L_a$ | 곡선의 모양 |
|---|---|---|---|
| 1 | 0 | 없음 | 분기점 (매끈) |
| 2 | 1 | 1차원 토러스 (분할 여부 = $U_a$ 가 제곱인가) | 마디(node) |
| $2k\ge4$ | $k$ | 토러스 × $\mathbb U_{k-1}$ | 두 가지가 $u^k$ 로 접함 |
| 3 | 1 | $\mathbb G_a$ | 첨점(cusp) |
| $2k+1\ge5$ | $k$ | $\mathbb U_k$ (표수 0: $\mathbb G_a^k$) | $(2,2k+1)$-특이점 |
(과제의 "짝수 → 토러스, 홀수 $\ge3$ → $\mathbb G_a$" 는 $m=2,3$ 에서만 정확하다. $m\ge4$ 에서는 토러스에 $\mathbb U_{k-1}$ 이 덧붙고, 홀수 $m\ge5$ 에서는 $\mathbb G_a$ 하나가 아니라 $k$ 차원.)

**1.7 $P_G$ 가 완전제곱인 경우 ($s=0$)** [증명]. $P_G=cQ^2$, $Q=\prod(t-a)^{m_a/2}$. 이때 $c=(-1)^{\mathrm{null}}\bigl(\prod\lambda^{m_\lambda/2}\bigr)^2$ 이고 정수 그래프에서 $\prod\lambda^{m_\lambda/2}$ 는 갈루아 안정이라 유리수. 따라서 **$c$ 는 $\mathbb Q$ 에서 $(-1)^{\mathrm{null}}$ 제곱류**: $\mathrm{null}=n-d$ 가 짝수이면 두 성분이 유리적이고, 홀수이면 ($-1$ 이 제곱이 아닌 체에서) 서로 켤레이다 (예: $2K_2\sqcup K_1$: $P=-(t^2-1)^2$).
  곡선: 두 성분 $w=\pm\sqrt c\,Q(t)$ (각각 $\mathbb P^1$), 각 근 $a$ 에서 접촉 차수 $k_a=m_a/2$ 로 만난다. $\infty$ 에서는 서로 다른 두 점 ($d$ 짝수). $r:=$ 서로 다른 근 수, $p_a=\sum k_a-1=d/2-1$ ✓. 층열(1.4)에서 $H^0(\tilde C,\mathcal O^\times)=(\bar F^\times)^2$ 이므로 다중차수 0 의 군은
$$\Gamma_G(\bar F)=\Bigl(\prod_a(\bar F[u]/u^{k_a})^\times\Bigr)\Big/\bar F^\times=(\bar F[t]/Q)^\times/\bar F^\times ,$$
토러스 계수 $r-1$, 유니포텐트 차원 $\sum(k_a-1)=d/2-r$. $c$ 가 제곱이면 $\Gamma_G=R_{A/F}\mathbb G_m/\mathbb G_m$ ($A=F[t]/Q$). $c$ 가 비제곱이면 성분 교환이 군을 역원으로 보내므로 $\Gamma_G(\bar F)$ 위 갈루아 작용이 $\sigma(g)^{\varepsilon(\sigma)}$ ($\varepsilon$=이차지표): 국소 인자가 $(q^{f}-\chi_{q^f}(c))$ 로 일반 공식(정리 4)과 같고 $G_m^{\rm tw}=R^1_{K/F}\mathbb G_m$ ($K=F(\sqrt c)$) 로 나눈다.
  **연결 그래프는 이 경우를 만들지 못한다** [증명]: 연결이면 (루프 포함) 페론–프로베니우스 고윳값 $\lambda_1>0$ 이 단순이므로 $m_{\lambda_1}=1$ → $s\ge1$. 따라서 $s=0$ 은 비연결 그래프에서만, 예: $H\sqcup H$ ($P=P_H^2$, $Q=P_H$): $\Gamma_{H\sqcup H}=(F[t]/P_H)^\times/F^\times$. 예 $2K_2$: $P=(t^2-1)^2$, $\Gamma=\mathbb G_m$ ($|\Gamma(\mathbb F_q)|=q-1$ ✓), $2K_3$: $P=(2t-1)^2(t+1)^4$, $\Gamma=\mathbb G_m\times\mathbb G_a$-꼴 ($T$ 계수 1 = $r-1$, 유니 1, $|\Gamma|=q(q-1)$ ✓ 계산).
  "이분 그래프의 블록형 곡선": 이분이면 $P_G$ 는 우함수 ($DAD=-A$, $D$=부호 대각행렬이라 $P_G(-t)=P_G(t)$) 이지만 완전제곱을 강제하지 않는다 ($P_4,P_5$ 반례: 매끈 종수 1). 이분 $G$ 는 $C_G$ 에 자기동형 $\tau:(t,w)\mapsto(-t,w)$ 를 준다 [증명]; 몫 $C_G/\tau$ 는 $w^2=R(t^2)$ 꼴. 이것은 $G\times K_2$ 에서의 함자성 쪽이라 researcher2 에게 넘긴다.

**1.8 $\Gamma_G$ 는 스펙트럼 불변량이다** [증명]. $C_G$ 는 $\chi_A$ 만의 함수이므로 코스펙트럴 그래프는 같은 $\Gamma_G$ 를 준다 (Aut($G$) 는 자명하게 작용). $G\mapsto\Gamma_G$ 의 함자성(그래프 사상)은 이 라운드의 research2·3 몫.

### 2. 체 $F$ 에 대한 함자성 (표수 $\ne2$)

**2.1 구성** [증명]. 범주 $\mathbf{Fld}_{\ne2}$: 대상=표수 $\ne2$ 체, 사상=체 준동형 (자동으로 단사). 문주님의 $F\mapsto F^G$ 는 공변이고 $\phi:F\to F'$ 에 대해 $\phi^{G\square G}(A_G^F)=A_G^{F'}$ (0,1 보존). 즉 $F\mapsto(F^{G\square G},A_G^F)$ 는 점 있는 공변함자. 이어서 (i) $\det(tA-I)$: $\mathrm{Mat}_n(F)\to F[t]$ 는 자연변환, (ii) 다항식 $P\in F[t]$ ($P(0)\ne0$) $\mapsto\mathrm{Pic}^0$ ($C_P$) 는 체 확대에 대해 기저변환 호환. 따라서 $\phi:F\to F'$ 에 대해 $C_{G,F'}=C_{G,F}\times_{F}F'$ (가중사영 차수 $e$ 도 같음: 단사 $\phi$ 가 차수·최고차계수를 보존) → 당김 $\phi^*:\mathrm{Pic}(C_F)\to\mathrm{Pic}(C_{F'})$. 이것이 다중차수 0 을 보존하는 이유: 성분이 서로 켤레일 때 $F$-유리 가역층의 다중차수는 성분 교환에 불변이므로 $(a,a)$, 차수 0 이면 $(0,0)$. 합성에 대해 $(\psi\phi)^*\cong\phi^*\psi^*$ (표준 동형이고 동형류로 가면 등식). 그러므로
$$\Gamma_G:\ \mathbf{Fld}_{\ne2}\longrightarrow\mathbf{Ab}$$
는 공변함자 [증명]. $\Gamma_G(\phi)$ 는 군 준동형 (텐서곱 보존).

**2.2 단사성** [증명]. 군 스킴 $\Gamma$ 의 $F$-점에 대해 $\Gamma(F)\to\Gamma(F')$ 는 $\operatorname{Spec}F'\to\operatorname{Spec}F$ 가 스킴 범주의 에피사상(충실평탄)이라 임의 스킴 $X$ 에 대해 $X(F)\to X(F')$ 가 단사이다. ∎ (초월 확대 $F'=F(x)$ 에서도 성립; 대수 확대이면 상은 $F$-유리부분.)

**2.3 갈루아 고정점** [증명]. $F^{\rm sep}/F$ 갈루아, $\Gamma=\mathrm{Pic}^0_{C/F}$ 는 $F$ 위 군 스킴. 점 $y:\operatorname{Spec}F^{\rm sep}\to\Gamma$ 가 $\mathrm{Gal}$-불변이면 잉여체가 $(F^{\rm sep})^{\mathrm{Gal}}=F$ 에 담겨 $F$-점으로 내려온다 (갈루아 하강). 따라서
$$\Gamma_G(F)=\Gamma_G(F^{\rm sep})^{\mathrm{Gal}(F^{\rm sep}/F)},$$
$F$ 완전체이면 $F^{\rm sep}=\bar F$. 유한체: $\Gamma_G(\mathbb F_q)=\Gamma_G(\bar{\mathbb F}_q)^{\rm Frob_q}$. 또 일반 갈루아 확대 $F'/F$ 에서 $\Gamma_G(F)=\Gamma_G(F')^{\mathrm{Aut}(F'/F)}$. 갈루아 작용은 $\sigma\in\mathrm{Aut}(F')$ 에 대한 $\Gamma_G(\sigma)$ 로 주어져 (2.1) 의 함자성과 같은 것이다 ($\Gamma_G(F')\ni$ 점에 $\sigma$ 가 작용).

**2.4 같은 정수 그래프의 소수 환원과 $\mathbb Q$** [부분 증명]. $\mathbb Q\to\mathbb F_p$ 는 체 사상이 아니므로 함자성은 없다. 대신 $R=\mathbb Z_{(p)}$ 위 가중사영 모델 $\mathcal C:w^2=\hat P_G(t,z)$ (차수 $2e$, $e=\lceil d_{\mathbb Q}/2\rceil$ 고정).
- **차수 보존 소수** ($p\nmid c$ 이고 $p$ 홀수; 곧 $0$ 의 대수적 중복도 불변, $d_p=d$): $\mathcal C_{\mathbb F_p}$ 는 $C_{G,\mathbb F_p}$ (§1 의 내재적 곡선)와 같다. 그렇지 않으면 ($d_p\le d-2$ 이면) $\mathcal C_{\mathbb F_p}$ 는 $\infty$ 에서 중복도 $\ge2$ 로 특이하여 **내재적 $C_{G,\mathbb F_p}$ 와 다르다** ($d_p=d-1$ 이면 중복도 1 이라 매끈해 같다). 예: $K_{3,3}$, $p=3$: $\hat P=z^2-9t^2\equiv z^2$.
- **유형 보존 소수**: $p$ 홀수, $p\nmid c\cdot\mathrm{disc}(\mathrm{rad}\,P_G)$ (서로 다른 근이 서로 다른 채로 남고 중복도 불변). 이때 $\tilde{\mathcal C}$ 는 $R$ 위 매끈이고 $J(\tilde{\mathcal C})$ 는 아벨 스킴, 국소 인자 $\mathcal L$ 은 $R$ 위 군 스킴(토러스: $\delta_a=S_0(a)$ 가 $p$-단위이므로 비분기, 유니포텐트 부분은 같은 차수의 평활 군). 따라서 $R$ 위 매끈 가환 군 스킴 $\mathcal P$ (확장)가 있고 $\mathcal P_{\mathbb Q}=\Gamma_{G,\mathbb Q}$, $\mathcal P_{\mathbb F_p}=\Gamma_{G,\mathbb F_p}$. 헨젤: $\mathcal P(\mathbb Z_p)\to\Gamma_G(\mathbb F_p)$ 는 **군 준동형 전사**, 핵은 pro-$p$ (형식군) [증명 스케치; $\mathcal P$ 의 존재는 위 구성과 $\mathcal L$ 의 표준 매끈성을 기억에 의존: 기억-미검증].
- **$\mathcal P(\mathbb Z_p)=\Gamma_G(\mathbb Q_p)$ 인가?** $J$ 는 고유라 같지만 $\mathcal L$ 의 분할 토러스는 $\mathbb G_m(\mathbb Q_p)=\mathbb Z_p^\times\times p^{\mathbb Z}$ 가 $\mathbb G_m(\mathbb Z_p)$ 보다 커서 아니다 (지수 $\mathbb Z$ 의 무한). 환원사상은 $\Gamma_G(\mathbb Q_p)$ 의 부분군 $\Gamma^0_G(\mathbb Q_p)=\mathcal P(\mathbb Z_p)$ 위에서만 정의된다 (분할 토러스 없으면 전체). 이분은 세 가지 사실로 요약: (i) 군 준동형, (ii) $\mathbb Q$ 위 $\Gamma_G(\mathbb Q)$ 는 유한생성이 아니다 (토러스·$\mathbb G_a$ 점 때문에 — 예 $K_3$: $\Gamma(\mathbb Q)=\mathbb Q(\sqrt{-3})^\times/\mathbb Q^\times$ 는 무한생성) 이므로 마주르형 유한성은 $J$ 쪽에만 있다, (iii) 비분기 토러스는 $\mathbb Q_p$ 에서 컴팩트라 이때 전체에 정의.
- **나쁜 소수 예** [계산 확인]: $K_3$, $p=3$: $P\equiv2(t+1)^3$ → 첨점, $\Gamma(\mathbb F_3)=\mathbb G_a$, $|\Gamma|=3=q-(\tfrac{-3}{3})$ (크로네커 기호 $0$, 분기). $P_4$, $p=5$: $P\equiv(t-3)^2(t-2)^2$ 완전제곱 → $s=0$, $\Gamma=\mathbb G_m$, $|\Gamma(\mathbb F_5)|=4$ ✓ (타원곡선 $P_4$ 의 $j=148176/25$ 에서 $5$ 의 분모: 분할 곱셈 환원과 일치). $C_5$, $p=5$: $P\equiv 2(t-3)^5$, $\mathbb U_2$, 위수 $25$.

### 3. 구조정리

**정리 3 (구조)** [증명 (국소 부분 1.5, 대역 부분 1.4); $s\ge1$, $F$ 완전체]. $\Gamma_G$ 는 연결 가환 대수군이고
$$1\to T\times U\to\Gamma_G\to J(\tilde C)\to1 ,\qquad \tilde C:\ \tilde w^2=S_0(t).$$
- $J(\tilde C)$: 종수 $\tilde g=\lceil s/2\rceil-1$ 의 초타원곡선 $\tilde w^2=S_0$ 의 야코비안. $\tilde g=0$ 이면 자명. $F$ 위 정의됨(홀수 중복도 근들의 갈루아 안정집합).
- $T=\prod_{x\in E/\mathrm{Gal}}R_{\kappa_x/F}\bigl(R^1_{B_x/\kappa_x}\mathbb G_m\bigr)$: $x$ 는 짝수 중복도 근의 갈루아 궤도, $\kappa_x=F[t]/\pi_x$, $B_x=\kappa_x(\sqrt{\delta_x})$, $\delta_x=S_0(a_x)\in\kappa_x^\times/\square$. 계수 $t=|E|$ (기하 근 수).
- $U=\prod_{x}R_{\kappa_x/F}(\ldots)$ 유니포텐트, 차원 $u=\sum_{a\in E}(k_a-1)+\sum_{a\in O_3}k_a$; 표수 0 에서 $\mathbb G_a^u$.
- $p_a=\tilde g+t+u$ (§1.5 점검).
(F 가 완전체이면 연결 가환 선형군은 $G_s\times G_u$ 로 분해되므로 $L=T\times U$ 가 정확하다.)

**꼬임 데이터 (일반 식)** [증명]. 근 $a=1/\mu$ ($\mu$ 짝수 중복도 고윳값): $\delta_a=S_0(1/\mu)=(-1)^{\mathrm{null}}\prod_{\lambda\in O\,(\text{홀수 중복도 고윳값})}(\lambda-\mu)/\mu\equiv(-1)^{\mathrm{null}}\mu^{s}\prod_{\lambda\in O}(\lambda-\mu)$ (제곱류). 토러스 $T$ 의 지표격자는 $X(T)=\bigoplus_{a\in E}\mathbb Ze_a$, $\sigma\in\mathrm{Gal}(\bar F/F)$ 가 $\sigma e_a=\pm e_{\sigma a}$ (부호 $=\sigma(\sqrt{\delta_a})/\sqrt{\delta_{\sigma a}}$) 로 작용한다 (부호붙은 순열표현). 분해체는 $K_G=F\bigl(a,\sqrt{\delta_a}:a\in E\bigr)$. 소수 $p$ 가 $K_G$ 에서 비분기이면
$$|T(\mathbb F_p)|=\bigl|\det\bigl(p\cdot1-\rho(\mathrm{Frob}_p)\bigr)\bigr|,\qquad\rho:\mathrm{Gal}(K_G/\mathbb Q)\to GL_t(\mathbb Z)\ \text{(부호 순열)} .$$
예: $K_3$ ($a=-1$, $\delta=-3$): $\rho=\chi_{-3}$ (지표), $K_G=\mathbb Q(\sqrt{-3})$, $|T(\mathbb F_p)|=p-(\tfrac{-3}p)$. $K_{2,2,2}$ ($\mathrm{null}=3$ 홀수 → 부호 $-1$): $\delta=3$, $K_G=\mathbb Q(\sqrt3)$, $|\Gamma|=q-(\tfrac3q)$. $C_5$: 짝수 중복도 고윳값 $\mu=\frac{-1\pm\sqrt5}2$ 의 역수 $a=\frac{1\pm\sqrt5}2$, $\delta_a=2a-1=\pm\sqrt5$ → $K_G=\mathbb Q(5^{1/4},i)$ ($D_4$, 위수 8), $\rho$ = $D_4\subset GL_2(\mathbb Z)$ 부호순열행렬군 [증명]. 페테르센: $\delta=15$, $K_G=\mathbb Q(\sqrt{15})$.

**참고: 확장 부류** [기억-미검증 + 증명 스케치]. 토러스 확장 $1\to T\to\bullet\to J\to1$ 는 지표마다 $J^\vee(\bar F)\cong J(\bar F)$ 의 점 $[x_a^+-x_a^-]\in\mathrm{Pic}^0(\tilde C)$ ($x_a^\pm$ = $\tilde C$ 에서 마디 $a$ 를 덮는 두 점; 클러칭 가역층의 $G_m$-토서) 이 부류이다. 이 점이 비비틀림이면 확장은 분리 안 됨. 유니포텐트 확장은 $\mathrm{Ext}^1(J,\mathbb G_a)=H^1(J,\mathcal O)$ 의 원소로, 표수 0 에서 첨점이 있으면 비분리(예: 첨점 하나는 보편 벡터 확장 $E^\natural$ 형, [기억-미검증]). 따라서 "$\ltimes$" 가 아니라 비분리 확장이 일반적이다.

**정리 4 (위수 공식)** [증명; Lang]. $F=\mathbb F_q$, $q$ 홀수, $s\ge1$. $P_G$ 를 $\mathbb F_q[t]$ 에서 $P_G=c\prod\pi_x^{m_x}$ (기약 monic $\pi_x$, 차수 $f_x$), $k_x=\lfloor m_x/2\rfloor$, $\chi_x=\chi_q\bigl(\operatorname{Res}(\pi_x,P_G/\pi_x^{m_x})\bigr)\in\{\pm1\}$ ($=\chi_{q^{f_x}}(\delta_x)$ 노름). 그러면
$$\boxed{\ |\Gamma_G(\mathbb F_q)|=|J(\tilde C)(\mathbb F_q)|\ \prod_{m_x\text{ 짝수}}q^{f_x(k_x-1)}\bigl(q^{f_x}-\chi_x\bigr)\ \prod_{m_x\text{ 홀수}\ge3}q^{f_xk_x}\ }$$
$s=0$ (모든 $m_x$ 짝수, $c$ 제곱 $\chi_{q}(c)=1$): $|\Gamma_G(\mathbb F_q)|=\prod_xq^{f_x(k_x-1)}(q^{f_x}-\chi_x)/(q-\chi_q(c))$, 여기서 $\chi_x=\chi_{q^{f_x}}(c)$.
증명: 연결 군 $L$ 에 대해 $H^1(\mathbb F_q,L)=0$ (Lang) 이므로 $\Gamma(\mathbb F_q)\to J(\mathbb F_q)$ 전사, 핵 $L(\mathbb F_q)$. $L=\prod R_{\kappa_x/\mathbb F_q}(\cdot)$ 이므로 인자별: 토러스 부분 $|R^1_{B/\kappa}\mathbb G_m(\mathbb F_{q^f})|=q^f-\chi$, 유니포텐트는 $q^{f\cdot\dim}$. $s=0$ 은 $L$ 을 $\mathbb G_m^{\rm tw}$ 로 나누고 다시 Lang. ∎
$|J(\mathbb F_q)|$: $\tilde g=1$ 이면 $\#\tilde C(\mathbb F_q)$ (점 있는 곡선: 아핀 개수 + 무한원점 수: $s$ 짝수 $1+\chi_q(c)$, 홀수 1). $\tilde g=2$ 이면 $(N_1^2+N_2)/2-q$.

**귀결 [증명, $p_a=1$]**: 기약 $C_G$ 가 $p_a=1$ 이면 $\Gamma_G(\mathbb F_q)\cong C_G^{\rm sm}(\mathbb F_q)$ (연쇄·접선 군법칙) 이므로 $|\Gamma|=\#C_G(\mathbb F_q)-\#\mathrm{Sing}$ 이고 $K_3$ 마디 $q-(\frac{-3}q)$, $K_4$ 첨점 $q$ 를 준다.

**정리 5 ($K_n$)** [증명]. $P_{K_n}=(-1)^{n-1}((n-1)t-1)(t+1)^{n-1}$. $n$ 홀수: $m=n-1=2k$, $k=(n-1)/2$, $\delta=S_0(-1)=-n$, $\tilde g=0$. $\Gamma=R^1_{\mathbb Q(\sqrt{-n})/\mathbb Q}\mathbb G_m\times\mathbb U_{(n-3)/2}$, $|\Gamma(\mathbb F_q)|=q^{(n-3)/2}\bigl(q-(\tfrac{-n}q)\bigr)$. $n$ 짝수: $m=n-1=2k+1$, $k=(n-2)/2$, $\Gamma=\mathbb U_{(n-2)/2}$ ($\mathbb G_a^{(n-2)/2}$ 표수 0), $|\Gamma(\mathbb F_q)|=q^{(n-2)/2}$. ($n=3$: 꼬인 토러스, $n=4$: $\mathbb G_a$, $n=5$: 꼬인 토러스 × $\mathbb G_a$, $n=6$: $\mathbb G_a^2$.) 계산 확인: $n=3..8$, $q\in\{5,7,11,13,17\}$ ($q\nmid n$) 공식 대 인수분해 자료 일치. 가정 $q\mid n$ 일 때(크로네커 0)는 가법 환원이라 별도.

**3.5 검증표** [계산 확인; 정리 4 의 예측 대 (a) 점 개수 $N_1,N_2$ 로 구한 $H^1$ 의 프로베니우스 고윳값 ($\dim H^1=2\tilde g+t$ 가 $\le2$ 인 경우) (b) $P_4$ 는 바이어슈트라스 $Y^2=X^3-27\cdot21X+27\cdot162$ 의 $\#E(\mathbb F_q)$, $q=7..31$ 일치]. 소수 $q=5,7,11,13,17,19,23$ 에서 불일치 0.

| $G$ | $P_G$ | $s$ | $\tilde g,t,u$ | $\Gamma_G$ | $|\Gamma_G(\mathbb F_q)|$ |
|---|---|---|---|---|---|
| $K_3$ | $(2t-1)(t+1)^2$ | 1 | 0,1,0 | $R^1_{\mathbb Q(\sqrt{-3})}\mathbb G_m$ | $q-(\frac{-3}q)$ |
| $K_4$ | $-(3t-1)(t+1)^3$ | 2 | 0,0,1 | $\mathbb G_a$ | $q$ |
| $K_5$ | $(4t-1)(t+1)^4$ | 1 | 0,1,1 | $R^1_{\mathbb Q(\sqrt{-5})}\mathbb G_m\times\mathbb G_a$ | $q(q-(\frac{-5}q))$ |
| $C_5$ | $(2t-1)(t^2-t-1)^2$ | 1 | 0,2,0 | 2차원 꼬인 토러스 ($D_4$) | $q\equiv\pm1\ (5)$: $(q-\chi(\sqrt5))(q-\chi(-\sqrt5))$; $q\equiv\pm2$: $q^2-\chi_q(-5)$; $q=5$: $25$ |
| $P_4$ | $(t^2-t-1)(t^2+t-1)$ | 4 | 1,0,0 | 타원곡선 $Y^2=X^3-567X+4374$ ($I=21,J=-162$) | $\#E(\mathbb F_q)$ ($q=5$: 곱셈환원 $q-1=4$) |
| $K_{2,2,2}$ | $-(4t-1)(2t+1)^2$ | 1 | 0,1,0 | $R^1_{\mathbb Q(\sqrt3)}\mathbb G_m$ | $q-(\frac3q)$ |
| 페테르센 | $(t-1)^5(2t+1)^4(3t-1)$ | 2 | 0,1,3 | $R^1_{\mathbb Q(\sqrt{15})}\mathbb G_m\times\mathbb U_3$ | $q^3(q-(\frac{15}q))$ |
| $Q_3$ (정육면체) | $(t^2-1)^3(9t^2-1)$ | 4 | 1,0,2 | $E$ 의 $\mathbb G_a^2$ 확장, $E:\tilde w^2=(t^2-1)(9t^2-1)$ | $q^2\#E(\mathbb F_q)$ ($q=5$: 200, 7: 392, 11: 968, 13: 2704) |
| $P_5$ | $-(t^2-1)(3t^2-1)$ | 4 | 1,0,0 | 타원곡선 | $\#E(\mathbb F_q)$ |
| Kneser(6,2) | $-(t-1)^9(3t+1)^5(6t-1)$ | 3 | 1,0,6 | $E:\tilde w^2=-(t-1)(3t+1)(6t-1)$ 의 $\mathbb U_6$ 확장 (srg(15,6,1,3)) | $q^6\#E(\mathbb F_q)$ |
| $K_{2,2,2,2}$ | $-(6t-1)(2t+1)^3$ | 2 | 0,0,1 | $\mathbb G_a$ | $q$ |
| $K_{3,3}$ | $-(3t-1)(3t+1)$ | 2 | 0,0,0 | $1$ | $1$ |
| $2K_2$ | $(t^2-1)^2$ | 0 | —,1,0 | $\mathbb G_m$ | $q-1$ |
| $2K_3$ | $(2t-1)^2(t+1)^4$ | 0 | —,1,1 | $\mathbb G_m\times\mathbb G_a$ | $q(q-1)$ |
정직한 한계: (a) 점 개수 대조는 토러스·아벨 부분(프로베니우스 고윳값)을 독립적으로 확인하지만 $\dim H^1=0$ 인 경우 ($K_4$, $K_{2,2,2,2}$ 등) 에는 유니포텐트 인자 $q^u$ 를 독립 확인하지 못한다 — $q^u$ 는 §1.5 의 국소 계산에 의존 [증명이지만 점 개수와 독립 검증 안 함]. 다만 $p_a=1$ 첨점($K_4$)은 매끈점 수 $q$ 로 확인됨. (b) 소수 $q$ 만 시험, 소수 거듭제곱 미시험. (c) 좋지 않은 소수($q\mid$ 판별식 등)도 내재적 공식이 그대로 맞음 ($P_4$, $q=5$ 등).

### 4. 증명 시도 요약과 장애물
- 증명 완료: 보조사실 0.1, 명제 1.2(모델 독립성), 층열과 국소 계산 1.5, 정리 3 의 선형 부분, 정리 4 와 5, 함자성 2.1–2.3, 연결 그래프의 기하적 기약성.
- 장애물 1: 확장 부류($[x_a^+-x_a^-]$, $\mathrm{Ext}(J,\mathbb G_a)$)의 명시적 계산과 분리 조건 — §3 에서 스케치만. 장애물 2: 정수 모델 $\mathcal P$ 의 존재(매끈성·단일 스킴)를 라이노 이론에 기대지 않고 직접 구성하는 것 — $J$ 부분은 표준이지만 $\mathcal L$ 의 $R$-매끈성은 [기억-미검증]. 장애물 3: 차수가 2 이상 떨어지는 소수에서 $\Gamma_{G,\mathbb F_p}$ 와 특이 모델 $\mathcal C_{\mathbb F_p}$ 의 $\mathrm{Pic}^0$ 사이 정확한 핵(무한원점의 국소 기여) 계산.

### 5. 함자성 정리 모음
1. $F\mapsto\Gamma_G(F)$ 는 $\mathbf{Fld}_{\ne2}\to\mathbf{Ab}$ 공변함자, 단사 사상, 갈루아 고정점 성질. [증명]
2. 문주님 정의와의 양립: $(-)^G$ 의 공변성에서 $A_G$ 가 자연원소 → $P_G$ 자연 → $\Gamma_G$ 자연 (2.1). [증명]
3. $\Gamma_G$ 는 $\chi_A$ 의 함수 (스펙트럼 불변량), 코스펙트럴 그래프가 같은 군을 준다. [증명]
4. $\mathbb Q\to\mathbb F_p$ 는 함자성 밖. 정수 모델 $\mathcal P$ 가 있는 소수에서 $\mathcal P(\mathbb Z_p)\twoheadrightarrow\Gamma_G(\mathbb F_p)$, 차수 하락 소수(≥2)에서는 내재 정의와 정수 모델 특수섬유가 다르다. [증명 스케치 + 반례 $K_{3,3},p=3$]

### 6. 표준 모델이 없는 경우의 분류: $\tilde g=0$ (홀수 중복도 고윳값 $s\le2$)
$\tilde g=0\iff s\in\{1,2\}$ (기약) 또는 $s=0$ (기약 아님). 이때 $\Gamma_G=L$ 은 선형군 $T\times U$. 연결 그래프는 $s\ge1$ (페론 단순). 매개변수: $t=|E|$ (짝수 중복도 서로 다른 고윳값 수, 갈루아로 묶인 궤도), $u=\sum_E(m/2-1)+\sum_{O_3}(m-1)/2$, 관계 $d=s+2(t+u)$.

| 유형 ($s$; 짝수 $m$ 집합 $E$; 홀수 $\ge3$ 집합 $O_3$) | $\Gamma_G$ ($F$ 완전체, 표수 0 에서) | $|\Gamma(\mathbb F_q)|$ | 예 |
|---|---|---|---|
| $s\in\{1,2\}$, $E=\emptyset$, $O_3=\emptyset$ | $1$ ($d\le2$ 원뿔곡선) | $1$ | $K_2,P_3,C_4,K_{1,3},K_{a,b}$ |
| $E=\emptyset$, $O_3\ne\emptyset$ | $\mathbb G_a^{u}$ ($u=\sum_{O_3}(m-1)/2$) | $q^u$ | $K_{2j}$ ($u=j-1$), $K_{a\times r}$ $r$ 짝수 ($u=(r-2)/2$) |
| $E\ne\emptyset$, 모두 $m=2$, $O_3=\emptyset$ | 순수 토러스 $T$, 계수 $t$ | $\prod_x(q^{f_x}-\chi_x)$ | $K_3,K_{a\times3},C_5$ ($t=2$), $K_{2,2,2}$ 류 |
| $E\ne\emptyset$, 일부 $m\ge4$ 또는 $O_3\ne\emptyset$ | $T\times\mathbb G_a^{u}$ | $q^u\prod_x(q^{f_x}-\chi_x)$ | $K_5$ ($t{=}1,u{=}1$), 페테르센 ($t{=}1,u{=}3$) |
| $s=0$ (비연결, 쌍으로 나타나는 성분) | $(F[t]/Q)^\times/F^\times$: 토러스 계수 $r-1$, 유니 $d/2-r$ | $\prod q^{f(k-1)}(q^f-1)/(q-1)$ | $2K_2$ ($\mathbb G_m$), $2K_3$ ($\mathbb G_m\times\mathbb G_a$), $H\sqcup H$ |
| $A=0$ ($d=0$) | $1$ | $1$ | 간선 없는 그래프 |

강정칙그래프(srg) 에서 $P=\pm(kt-1)(rt-1)^f(st-1)^g$ (영고윳값 없을 때). 짝수/홀수 유형에 따라 [증명, 정리 3·1.6 의 직접 적용]:
| $(f,g)$ 의 홀짝 | $s$ | $\tilde g$ | $\Gamma_G$ |
|---|---|---|---|
| (짝, 짝) | 1 | 0 | $T^{2}\times U$, $t=2$, $u=(f/2-1)+(g/2-1)$ (예: $L(3)=K_3\square K_3$, Paley(9): 둘 다 $m=4$: $f=g=4$) |
| (홀, 짝) | 2 | 0 | $T\times U$, $t=1$, $u=\frac{f-1}2+\frac g2-1$ (페테르센 $f{=}5,g{=}4$) |
| (홀, 홀) | 3 | **1** | 타원곡선 $E:\tilde w^2=\pm(kt-1)(rt-1)(st-1)$ (유리 2-분점 완전) 의 $\mathbb U_{(f-1)/2+(g-1)/2}$ 확장 (Kneser(6,2): $f{=}9,g{=}5$, $u=6$) |
이 표는 정리 3 과 §1.6 의 직접 적용이다 [증명]. 개별 srg 로 검증한 것은 페테르센 (홀,짝) 과 Kneser(6,2) (홀,홀) 뿐이고 (짝,짝) 행은 검증하지 않았다.

### 7. 이번 라운드의 정정
- 과제 서술의 "짝수 → 토러스, 홀수 $\ge3$ → $\mathbb G_a$" 는 $m=2,3$ 만 정확, 일반은 §1.6 표.
- "$d=\operatorname{rank}A$" 는 표수 0 에서만; 소수 환원에서는 대수적 중복도 ($d_p\ge\operatorname{rank}_p$).
- 오케스트레이터 서술 "$P_H=P_GQ^2$ 이면 $\Gamma_H\to\Gamma_G$ 전사" 는 이 보고서의 범위 밖(research2 몫)이나, $S_0$ 가 같으면 $J(\tilde C)$ 가 같고 $L$ 이 커진다는 점은 §3 에서 확인 가능 (같은 $S_0$ ⇒ 같은 $J$).
- 부호 $(-1)^{\mathrm{null}}$: $K_{2,2,2}$ 와 $K_3$ 는 $t\mapsto2t$ 로 곡선이 같지 않고 $-1$-꼬임 (계산 확인).

## 후속연구 지점
1. **(최우선) 확장 부류의 명시적 계산과 분리 판정.** 무엇을: $\tilde g\ge1$ 이면서 $t\ge1$ 또는 $u\ge1$ 인 그래프(예: $Q_3$, Kneser(6,2))에서 $[x_a^+-x_a^-]\in J(\tilde C)$ 가 비틀림인지, $\mathrm{Ext}(J,\mathbb G_a)$ 부류가 영인지. 왜: $\Gamma_G$ 가 $T\times U\times J$ 로 갈라지는지(그리고 정수 점 구조) 결정. 시작: 초타원곡선에서 $x_a^+-x_a^-=2x_a^+-\text{(섬유류)}$ 을 문퍼드 표현으로 쓰고 2·$x$ 의 위수 확인; 난점: 비틀림 점의 위수 결정은 곡선별 계산, 일반 정리는 어려움.
2. **정수 모델과 환원 정리의 완결.** 무엇을: 유형 보존 소수에서 $\mathcal P$ 의 매끈성을 직접(라이노 없이) 구성, 차수 하락 소수($d_p\le d-2$)에서 $\mathcal C_{\mathbb F_p}$ 의 $\mathrm{Pic}^0$ 와 내재 $\Gamma_{G,\mathbb F_p}$ 사이 핵을 무한원점 국소 기여로 계산. 왜: "$\Gamma_G(\mathbb Q)$ 와 $\Gamma_G(\mathbb F_p)$ 의 관계"가 이번엔 스케치. 시작: 가중사영 $w^2=z^{2j}R$ 의 특이점 국소환($j\ge1$)을 §1.5 와 같이 계산; 난점: 이중 근이 $\infty$ 와 유한 근과 합칠 때 병합.
3. **체비샤프형 분포.** 무엇을: $K_G=F(a,\sqrt{\delta_a})$ 의 갈루아군과 $\rho$ 를 족(완전다분, srg, 케일리)에서 결정하고 $|\Gamma_G(\mathbb F_p)|$ 의 분포를 계산. 왜: 정리 3 의 "일반 식"이 구체적 분포 정리가 됨. 시작: $K_{a\times r}$ 은 $\mathbb Q(\sqrt{\pm r\cdot\text{무엇}})$; 난점: 일반 srg 의 $\delta_a$ 계산.
4. **소수 거듭제곱·표수 2.** 무엇을: $q=p^r$ ($p$ 소수 3 포함) 에서 유니포텐트 부분의 군 구조(위트 벡터형 여부), 표수 2 에서 $\Gamma_G$ 정의(아르틴–슈라이어 모델 $w^2+h w=P$). 왜: 문주님 정의는 모든 체; 표수 2 는 이번 범위 밖. 시작: $y^2+hy=f$ 형으로 $P_G$ 를 쓰기 위해 $\mathbb Z$ 위 격자 필요; 난점: $A$ 가 정수 대칭이지만 반정수 구조가 필요할 수 있음.
5. **$G$ 에 대한 함자성으로의 연결 (research2·3 와 합류).** 무엇을: $P_H=P_GQ^2$ 형이면 $S_0$ 가 같아 $J(\tilde C)$ 가 같고 $\Gamma_H\to\Gamma_G$ 의 핵이 어떤 $L$ 인가; 이분 $G$ 의 involution $\tau$ 와 $G\times K_2$ 의 관계. 왜: 이 보고서의 구조정리는 $S_0$-불변량(= "홀수 중복도 스펙트럼") 이 함자적 핵심임을 시사. 시작: $\tilde C$ 와 $(E,O_3,\delta)$ 의 변환 공식; 난점: 마이너 등 비피복에서는 깨짐.
