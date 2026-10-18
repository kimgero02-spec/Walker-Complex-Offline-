# [R10-researcher3] 흰 점 장애의 불 코사이클 정식화와 블록 수준의 색칠 부등식

- 작성자·라운드·역할: 연구원3 · R10 · 구조 조각가 (범주·장애 이론·블록 구조)
- 근거: problem.md, library/R07-researcher3.md, R08-researcher3.md, R09-researcher3.md, 교재 정의 0 (평면 그래프), 정의 1.1 (평면분해, 고립점 허용, 같은 조각 반복 허용), 예 1.3, 정의 2.1, 2.3. R08 정리 R8-1, 따름 R8-5, R09 정리 2.4, 계 2.5, 명제 1.1–1.5 는 인용만 하고 다시 증명하지 않는다. 교재 밖 문헌은 쓰지 않았다.
- 계산 확인 코드: `rooms/researcher3/r10_obs.py` (§1.5 보편 반례의 $L$ 집합과 AND 규칙), `r10_blk.py` (§2 예의 $b,r,\chi$). 계산은 예의 값을 확인하는 데만 쓰고 근거로 쓰지 않는다.

## 요약
- **(1) 흰 점 선택은 불 모노이드 $\mathbb B=(\{0,1\},\wedge)$ 값 1-코체인이다.** $\Phi\in L(\sigma)$ 는 흰 점 지표 $\varepsilon_\Phi\in\mathbb B^{W(D')}$ 로 완전히 정해지고 (정리 1.1), 합성은 $\varepsilon_{\Phi\Phi'}=\varepsilon_{\Phi'}\wedge\varepsilon_\Phi$ (AND 규칙) 이다. 함자 올림 = 허용 집합 안의 곱셈적 코체인 (1-코사이클) 이다. [증명]
- **(2) 장애의 값.** 선택 $\Lambda$ 의 결함 $\delta_\Lambda(\sigma,\tau)$ 는 불 2-코사이클 항등식을 만족하고 (명제 1.3), 선택과 무관한 장애 $\omega(\pi)(v)=\alpha(\pi)(v)\wedge\zeta(\pi)(v)$ ("어떤 인수분해는 흰 점을 살리도록, 다른 인수분해는 죽이도록 강제") 가 $\ne0$ 이면 함자가 없다 (정리 1.4). R09 명제 1.1 은 $\omega(\pi)(u)=1$ 인 경우이다. 최대 선택은 언제나 lax 함자이다 (명제 1.2). [증명]
- **(3) 보편성과 0 이 되는 조건.** 점이 하나라도 있는 모든 $G$ 에서 $\mathcal R_{\rm adm}(G)$ 의 $\omega\ne0$ 이다 (정리 1.6, $K_1$ 조각 구성). 반대로 $\zeta$ 가 소 (prime) 이면 최대 함자, $\alpha$ 가 소이면 최소 함자가 존재한다 (정리 1.5). 흰 점-포화 부분범주 $\mathcal R_{\rm sat}\supsetneq\mathbf{Ref}_{\rm inj}$ 위에서 모두-흰 올림은 엄밀한 함자이다 (R09 명제 1.2 의 확장). [증명]
- **(4) 블록 수준의 색칠.** $\chi(G)$ 는 블록 함자 $\theta$ 에 대해 불변 ($\mathrm{Col}_q$ 의 극한이 자연 동형), 국소 상계 $b(D)=\max\chi(\beta)$ 는 $\theta$ 를 따라 단조 증가, 간극 $\chi(G)-b(D)$ 는 단조 감소한다. 새 부등식: $\chi(G)\le b(D)+r(D)$, 여기서 $r(D)=\beta_1(I(D))$ 는 블록–허브 접속 그래프의 사이클 수이고 $r(D)=\beta_1(G)+\sum_e(\mu(e)-1)-\sum_\beta\beta_1(\beta)$. $r=0$ 이면 $\chi=b$ 이고 $G$ 평면. $K_4=(K_4-uv)\cup K_2$ 와 $K_4$ 의 분해 $(P_1,03,12)$ 에서 등호. [증명] [계산 확인]
- $r$ 는 $\theta$ 를 따라 일반적으로 단조가 아니다 ($K_4$ 의 세 분해에서 $3\to2\to3$). 변-분할 분해 사이에서는 단조 감소이다. [증명] [계산 확인]

## 본문

### 0. 규약

- R09 §0 의 기호를 그대로 쓴다. $D=(P_k)$, $\mathfrak M(D)$, 복사점 $(v,k)$, 흰 점 $w_v$, $W(D):=\{v:|F_D(v)|\ge2\}$, $\mu_D$, 정련 $\sigma:D'\to D$, $L(\sigma)$.
- $\mathcal R_{\rm adm}$: 올림 가능한 정련 ($L(\sigma)\ne\varnothing$) 의 부분범주. 합성에 닫혀 있다 (R08 따름 R8-5). 항등은 단사이므로 들어 있다 (R08 계 (i)). 올림 불가능한 정련 (R08 예 3.3) 이 있으면 $\mathbf{Ref}$ 전체에서는 함자가 자명하게 없으므로, 공정한 무대는 $\mathcal R_{\rm adm}$ 이다. 이 보고의 불가능성 결과는 모두 $\mathcal R_{\rm adm}$ 안에서 성립하므로 R09 명제 1.1 보다 강하다.
- $\sigma:D'\to D$ 에 대해 $\Gamma'$ 는 R08 §0 의 그래프 ($W(D')$ 위, $\mu'\ge2$ 인 변). 점 $v\in W(D')$ 가 **불순** $\Leftrightarrow$ $\sigma$ 가 $\Pi'(v)$ 위에서 상수가 아님.
- 성분 $K$ (Γ′ 의 연결 성분) 의 판정 (R08 정리 R8-1): (α) 모두 순수, (β) 모든 $v\in K$ 에 $|F_D(v)|\ge2$, 모든 변에 $\mu_D\ge2$.

### 1. 흰 점 선택의 합성 불일치를 장애로 (임무 1)

#### 1.1 흰 점 지표 좌표

**정의.** $\Phi\in L(\sigma)$ 에 대해 $\varepsilon_\Phi:W(D')\to\{0,1\}$, $\varepsilon_\Phi(v)=1\iff\Phi(w'_v)$ 가 흰 점.

**정리 1.1 (좌표화).** $\sigma\in\mathcal R_{\rm adm}(D',D)$ 에 대해 $\Phi\mapsto\varepsilon_\Phi$ 는 $L(\sigma)$ 에서
$$\mathrm{Adm}(\sigma):=\{a\in\mathbb B^{W(D')}:\ a\text{ 는 }\Gamma'\text{ 의 각 성분에서 상수};\ K\text{ 에 불순 점이 있으면 }a|_K\equiv1;\ K\text{ 가 (β) 를 어기면 }a|_K\equiv0\}$$
로 가는 전단사이다. 특히 각 성분은 **강제 1** (불순 점 포함), **강제 0** (모두 순수이고 (β) 위반), **자유** (모두 순수이고 (β) 성립) 중 하나이고, $L(\sigma)\cong\{0,1\}^{\#\text{자유 성분}}$ 은 불 격자이다 (torsor 가 아니다). [증명]

*증명.* R09 계 2.5 에 의해 $\Phi\in L(\sigma)$ 의 복사점 부분은 $(v,j)\mapsto(v,\sigma j)$ 로 고정이고, 흰 점 $p_v=\Phi(w'_v)$ 만 남는다. R08 정리 R8-1 의 증명에서 $p_v\in\{w_v,(v,\kappa(v))\}$ 이고 복사점 값은 순수 점에서만, 그것도 $(v,\kappa(v))$ 하나뿐이다. 그러므로 $p_v$ 는 $\varepsilon_\Phi(v)$ 로 정해지고, 사상은 단사이다. 상의 조건: 성분 상수는 R09 (H4) 의 혼합 불가에서, 불순 ⟹ 1 은 R08 보조명제 1.3 (b) 에서, (β) 위반 ⟹ 0 은 $E_{11}$ 정의 ($\mu_D\ge2$) 와 $w_v$ 의 존재 조건 ($|F_D(v)|\ge2$) 에서 나온다. 전사는 R8-1 충분성 증명의 구성을 성분마다 독립하게 하는 것이다. 마지막으로 불순 점이 있는 성분은 $\sigma\in\mathcal R_{\rm adm}$ 이므로 (β) 를 만족한다 (R8-1 필요성). □

**보조명제 1.2a (AND 규칙).** $\tau:D''\to D'$, $\sigma:D'\to D$, $\Phi'\in L(\tau)$, $\Phi\in L(\sigma)$ 이면 $v\in W(D'')$ 에서
$$\varepsilon_{\Phi\Phi'}(v)=\varepsilon_{\Phi'}(v)\wedge\tilde\varepsilon_\Phi(v),\qquad \tilde\varepsilon_\Phi(v):=\begin{cases}\varepsilon_\Phi(v)&v\in W(D')\\0&v\notin W(D')\end{cases}.$$
[증명] $\varepsilon_{\Phi'}(v)=0$ 이면 $w''_v\mapsto(v,j)\mapsto(v,\sigma j)$ 이므로 복사점, 값 0. $\varepsilon_{\Phi'}(v)=1$ 이면 $w''_v\mapsto w'_v$ 이고 (그러므로 $v\in W(D')$) 그 다음 값은 $\varepsilon_\Phi(v)$. □ [계산 확인: r10_obs.py 의 두 합성쌍]

해석: 흰 점 정보는 $\mathbb Z_2$ 레이블이 아니라 **흡수 원소 0 을 가진 $\mathbb Z_2$**, 즉 불 모노이드 $(\{0,1\},\wedge)$ 값이다. "다중 접합점 $v$" 라는 기록은 한 번 복사점으로 떨어지면 되살릴 수 없다. 이것이 problem.md 의 $\mathbb Z_2$ 홀로노미와의 차이점이다: 홀로노미는 군 값이라 되돌릴 수 있지만 흰 점 지표는 비가역이다.

**따름 1.2b (함자 = 곱셈적 코체인).** 부분범주 $\mathcal C\subseteq\mathcal R_{\rm adm}$ 위의 함자 올림 $\Lambda$ (각 $\sigma$ 에 $L(\sigma)$ 의 원소) 는 다음을 만족하는 $\varepsilon:\mathrm{Mor}\,\mathcal C\to\mathbb B^{W(\cdot)}$ 와 일대일이다:
(Z1) $\varepsilon(\sigma)\in\mathrm{Adm}(\sigma)$; (Z2) $\varepsilon(\sigma\tau)=\varepsilon(\tau)\wedge\tilde\varepsilon(\sigma)$.
항등에서는 (Z1) 이 $\varepsilon(\mathrm{id})\equiv1$ 을 강제한다 (항등은 단사이므로 $W$ 의 모든 점이 불순). [증명] 정리 1.1 의 단사성과 보조명제 1.2a 에서. 이 (Z2) 가 "1-코사이클 조건" 이다 (계수는 군이 아니라 불 모노이드).

**주의 (계수계의 비함자성).** $D\mapsto W(D)$ 에 제한사상 $\tau^\natural a:=\tilde a|_{W(D'')}$ 을 주면 $(\sigma\tau)^\natural\ne\tau^\natural\sigma^\natural$ 이다. 두 쪽은 정확히
$$\Delta(\sigma,\tau):=\bigl(W(D'')\cap W(D)\bigr)\setminus W(D')$$
에서 다르다 (양 끝에서는 접합점인데 중간에서는 아닌 점). R09 예 1.0 의 $(\sigma'',\tau'')$ 에서 $\Delta=\{u,v\}$. [증명: 정의를 펼친 것] 이 비함자성이 아래 장애의 기하적 원천이다: $v\in\Delta(\sigma,\tau)$ 이면 $\tau$ 의 어떤 올림도 $w''_v$ 를 복사점으로 보내야 한다 ($D'$ 에 $w'_v$ 가 없음).

#### 1.2 lax 함자와 결함 2-코체인

$\mathrm{Adm}(\sigma)$ 는 성분별 곱이므로 최댓값 $\varepsilon_{\max}(\sigma)$ (자유 성분을 모두 1) 이 있다. 이에 해당하는 올림을 $\Lambda_{\max}(\sigma)$ 라 한다.

**명제 1.2 (최대 선택은 lax 함자).** $L(\sigma)$ 위에 $\Phi\le\Psi\iff\varepsilon_\Phi\le\varepsilon_\Psi$ (점별) 로 순서를 주면, 합성은 양쪽에서 단조이고 (AND 규칙), $\Lambda_{\max}(\sigma)\Lambda_{\max}(\tau)\le\Lambda_{\max}(\sigma\tau)$, $\Lambda_{\max}(\mathrm{id})=\mathrm{id}$ 이다. 즉 $\Lambda_{\max}$ 는 국소 포셋 2-범주로 가는 정규 lax 함자이다. [증명] 단조성: $\varepsilon_{\Phi\Phi'}=\varepsilon_{\Phi'}\wedge\tilde\varepsilon_\Phi$ 는 두 인자에 대해 단조. 비교: 왼쪽은 $L(\sigma\tau)$ 의 원소 (R08 따름 R8-5) 이고 오른쪽은 그 최댓값. 국소 포셋이므로 정합 조건은 자동이다. □

R09 명제 1.5 (집합값 $\mathcal L$ 은 lax) 를 원소값으로 바꾼 것이다. 이제 엄밀성의 실패를 값으로 잰다.

**정의 (결함).** 임의의 선택 $\Lambda$ 에 대해
$$\delta_\Lambda(\sigma,\tau):=\varepsilon(\sigma\tau)\oplus\bigl(\varepsilon(\tau)\wedge\tilde\varepsilon(\sigma)\bigr)\in\mathbb Z_2^{W(D'')}.$$
$\Lambda$ 가 함자 $\iff\delta_\Lambda\equiv0$. $\Lambda=\Lambda_{\max}$ 이면 $\varepsilon(\sigma\tau)\ge\varepsilon(\tau)\wedge\tilde\varepsilon(\sigma)$ 이므로 $\delta=\varepsilon(\sigma\tau)\wedge\neg(\varepsilon(\tau)\wedge\tilde\varepsilon(\sigma))$.

**명제 1.3 (불 2-코사이클 항등식).** $D'''\xrightarrow{\tau}D''\xrightarrow{\sigma}D'\xrightarrow{\rho}D$ 에서 $\Lambda=\Lambda_{\max}$, $x=\varepsilon(\tau)$, $c=\varepsilon(\rho\sigma\tau)$, $z=\tilde\varepsilon(\rho)$ ($W(D''')$ 로 당긴 것), $\delta=\delta_{\Lambda_{\max}}$ 라 하면 $W(D''')$ 위에서
$$\delta(\rho,\sigma\tau)\ \vee\ \bigl(c\wedge z\wedge\delta(\sigma,\tau)\bigr)\;=\;c\wedge\neg(x\wedge y\wedge z)\;=\;\delta(\rho\sigma,\tau)\ \vee\ \bigl(c\wedge x\wedge\tau^\natural\delta(\rho,\sigma)\bigr),$$
($y=\tilde\varepsilon(\sigma)$). [증명] 가운데 식은 3-단계 총결함이다. 왼쪽 등식: $a:=\varepsilon(\sigma\tau)\ge x\wedge y$. $a\wedge z=0$ 이면 $x\wedge y\wedge z=0$ 이므로 가운데는 $c$, 왼쪽 첫 항 $\delta(\rho,\sigma\tau)=c\wedge\neg(a\wedge z)=c$. $a\wedge z=1$ 이면 첫 항은 0 이고 가운데는 $c\wedge\neg(x\wedge y)=c\wedge a\wedge\neg(x\wedge y)=c\wedge\delta(\sigma,\tau)$, $z=1$. 오른쪽 등식도 $b:=\varepsilon(\rho\sigma)\ge y\wedge z$ 로 같은 두 경우 나눔 ($x=1$ 이 $v\in W(D'')$ 를 보장해 $\tau^\natural$ 이 문제없다). □
이것은 아벨 경우의 $\rho\cdot o(\sigma,\tau)-o(\rho\sigma,\tau)+o(\rho,\sigma\tau)-o(\rho,\sigma)=0$ 에 해당하는 불 판본이다. 빼기가 없으므로 "∨ 분해" 꼴이 된다. [증명]

**장애물 A1 (코호몰로지 류가 없다).** 아벨 이론에서는 선택을 바꾸면 $o$ 가 코경계만큼 바뀌어 $[o]\in H^2$ 가 선택과 무관하다. 여기서는 $\mathbb B$ 에 역원이 없어 "코경계만큼 바뀐다" 가 성립하지 않는다 (선택을 1→0 으로 바꾸면 그것을 거치는 모든 합성이 0 으로 흡수된다). 그래서 $[\delta]$ 를 류로 정의하지 못했다. 대신 아래 1.3 에서 선택과 무관한 국소 불변량 $\omega$ 를 만든다.

#### 1.3 선택과 무관한 장애 $\omega$

부분범주 $\mathcal C\subseteq\mathcal R_{\rm adm}$ 를 고정한다. $\pi\in\mathcal C(D'',D)$ 의 인수분해 $F=(\sigma_r,\dots,\sigma_1)$ ($\sigma_i:D_{i-1}\to D_i$, 모두 $\mathcal C$ 안) 의 상 $\mathrm{Im}_F:=\{\Phi_r\cdots\Phi_1:\Phi_i\in L(\sigma_i)\}\subseteq L(\pi)$ 로 둔다. $v\in W(D'')$ 에 대해
- $\alpha_{\mathcal C}(\pi)(v)=1$ ⟺ 어떤 $F$ 에서 $\mathrm{Im}_F$ 의 모든 원소가 $\varepsilon(v)=1$ (**살림 강제**),
- $\zeta_{\mathcal C}(\pi)(v)=1$ ⟺ 어떤 $F$ 에서 $\mathrm{Im}_F$ 의 모든 원소가 $\varepsilon(v)=0$ (**죽임 강제**),
- $\omega_{\mathcal C}(\pi)(v):=\alpha_{\mathcal C}(\pi)(v)\wedge\zeta_{\mathcal C}(\pi)(v)$.

**보조명제 1.3a (국소 판정).** AND 규칙과 $L(\sigma_i)$ 들의 독립성에서 [증명]:
$\alpha(\pi)(v)=1$ ⟺ 어떤 $F$ 에서 모든 $i$ 에 $v\in W(D_i)$ 이고 $v$ 의 $\Gamma_{i-1}$-성분이 $\sigma_i$ 에서 강제 1 (불순 점 포함).
$\zeta(\pi)(v)=1$ ⟺ 어떤 $F$ 에서 어떤 $i$ 가 $v$ 에서 강제 0 (그 성분이 (β) 위반, 또는 $v\notin W(D_i)$).
($\varepsilon_{\rm 합성}(v)=\bigwedge_i\varepsilon_i(v)$ 이고 각 $\varepsilon_i(v)$ 의 허용 집합이 독립이므로, 합성이 항상 0 ⟺ 어떤 인자의 허용 집합이 $\{0\}$, 항상 1 ⟺ 모든 인자의 허용 집합이 $\{1\}$.) 또한 $\alpha(\pi),\zeta(\pi)$ 는 $\Gamma''$ 의 성분에서 상수이다 ($\mathrm{Im}_F\subseteq L(\pi)$ 의 원소는 정리 1.1 에 의해 성분 상수). [증명]

**정리 1.4 (장애).** $\mathcal C$ 위에 함자 올림이 있으면 $\omega_{\mathcal C}\equiv0$. 대우로, 어떤 $\pi,v$ 에서 $\omega_{\mathcal C}(\pi)(v)=1$ 이면 함자 올림은 없다. 더 정확히, 임의의 함자 $\Lambda$ 는 $\alpha\le\varepsilon_\Lambda\le1-\zeta$ 를 만족한다. [증명] 함자이면 모든 인수분해 $F$ 에 대해 $\Lambda(\pi)=\Lambda(\sigma_r)\cdots\Lambda(\sigma_1)\in\mathrm{Im}_F$. 살림 강제하는 $F$ 로 $\varepsilon_{\Lambda\pi}(v)=1$, 죽임 강제하는 $F'$ 로 $=0$. 둘 다이면 모순. □

**R09 명제 1.1 의 재기술.** 예 1.0 에서 $F=(\sigma,\tau)$ (중간 $D_3$) 는 두 인자 모두 $u$ 에서 불순이므로 살림 강제, $F'=(\sigma'',\tau'')$ (중간 $D_0$) 는 $u\notin W(D_0)$ 이므로 죽임 강제. 따라서 $\omega(\pi)(u)=1$ 이 "장애의 값" 이다. 결함으로 읽으면 $\delta_{\Lambda_{\max}}(\sigma'',\tau'')(u)=1$ (최대 선택 $\varepsilon_{\max}(\pi)(u)=1$ 인데 $\varepsilon(\tau'')(u)=0$) 이고, 다른 어떤 선택도 $(\sigma,\tau)$ 쪽에서 결함 1 을 낸다. [증명] (R09 의 증명 (i)–(iv) 를 정리 1.1 의 언어로 옮긴 것.)

**홀로노미 읽기.** 두 인수분해 $F,F'$ 은 $\pi$ 를 대각선으로 갖는 사각형을 이룬다. 두 쪽 모두 강제될 때 $\mathrm{hol}_{F,F'}(v):=\varepsilon_F(v)\oplus\varepsilon_{F'}(v)\in\mathbb Z_2$ 를 그 사각형의 홀로노미라 하면, $\omega(\pi)(v)=1$ ⟺ 어떤 사각형의 홀로노미가 1. 함자 올림은 "평탄 접속" 이고 $\omega$ 는 그 곡률이다. 단, 강제되지 않는 인수분해에서는 홀로노미가 정의되지 않는다 (불 계수의 대가). [증명: 정의]

#### 1.4 장애가 0 이 되는 조건

**정리 1.5 (충분 조건).** $\mathcal C\subseteq\mathcal R_{\rm adm}$ 에서
(P) **죽임의 소성**: $\zeta(\sigma\tau)(v)=1\Rightarrow\zeta(\tau)(v)=1$ 또는 $v\notin W(D')$ 또는 $\zeta(\sigma)(v)=1$,
이 성립하면 $\varepsilon:=1-\zeta$ 는 함자 올림 $\Lambda_\zeta$ 를 주고, 이것은 **최대** 함자이다. 쌍대로
(P*) **살림의 소성**: $\alpha(\sigma\tau)(v)=1\Rightarrow\alpha(\tau)(v)=1$ 이고 $\alpha(\sigma)(v)=1$,
이 성립하면 $\varepsilon:=\alpha$ 는 **최소** 함자를 준다. 어느 경우든 $\omega\equiv0$ 이다.

*증명.* (P) 의 경우. (Z1): 성분 상수는 보조명제 1.3a. $v$ 가 $\pi$ 에서 불순이면 $L(\pi)$ 의 모든 원소가 1 이고 $\mathrm{Im}_F\subseteq L(\pi)$ 이므로 어떤 $F$ 도 죽임 강제하지 못해 $\zeta=0$, $\varepsilon=1$ ✓. 성분이 (β) 위반이면 자명 인수분해 $F=(\pi)$ 가 죽임 강제하므로 $\varepsilon=0$ ✓. 나머지 (자유) 는 두 값 모두 허용 ✓. (Z2): 보여야 할 것은 $\zeta(\sigma\tau)=\zeta(\tau)\vee\bigl([v\notin W(D')]\vee\zeta(\sigma)\bigr)$. "⊇": $\tau$ 의 죽임 강제 인수분해 뒤에 $\sigma$ 를 붙이면 $\sigma\tau$ 의 죽임 강제 인수분해 (AND 의 흡수). $\zeta(\sigma)(v)=1$ 이면 $\sigma$ 의 것 앞에 $\tau$ 를 붙인다. $v\notin W(D')$ 이면 $(\sigma,\tau)$ 자체가 죽임 강제. "⊆" 가 (P) 이다. 최대성은 정리 1.4 의 $\varepsilon_\Lambda\le1-\zeta$. (P*) 의 경우도 같다: 불순 ⟹ 자명 인수분해가 살림 강제 ⟹ $\alpha=1$; (β) 위반 ⟹ $L(\pi)$ 의 원소가 모두 0 이고 $\mathrm{Im}_F\ne\varnothing$ 이므로 살림 강제 불가 ⟹ $\alpha=0$; "⊇" 는 이어붙이기 ($\alpha(\tau)(v)=1$ 이 $v\in W(D')$ 를 보장), "⊆" 가 (P*). □

**따름 1.5a (흰 점-포화 부분범주).** $\sigma$ 가 **포화** ⟺ $\Gamma'$ 의 모든 성분이 (β) 를 만족 (즉 $W(D')\subseteq W(D)$ 이고 $\mu'(e)\ge2\Rightarrow\mu_D(e)\ge2$). 포화 정련은 합성에 닫힌 부분범주 $\mathcal R_{\rm sat}$ 를 이루고, 그 위에서 모두-흰 올림 ($\varepsilon\equiv1$) 은 엄밀한 함자이다. $\mathbf{Ref}_{\rm inj}\subsetneq\mathcal R_{\rm sat}$ 이므로 R09 명제 1.2 의 확장이다. [증명] 닫힘: $v\in W(D'')\Rightarrow v\in W(D')\Rightarrow v\in W(D)$, 그리고 $\mu''\ge2\Rightarrow\mu'\ge2\Rightarrow\mu_D\ge2$. 항등은 포화. $\mathcal R_{\rm sat}$ 안의 인수분해에는 강제 0 인자가 없으므로 $\zeta\equiv0$, (P) 가 자명. 진포함: R09 예 1.0 의 $\pi=(1,1):D_2\to D_1$ 은 단사가 아니지만 포화 ($u,v\in W(D_1)$, $\mu_{D_1}(uv)=2$). R08 계 (i) 이 단사 ⟹ 포화를 준다. □
(이것은 R09 후속 4 "단사를 국소 조건으로 약화" 의 답의 한 형태이다: 필요한 것은 단사가 아니라 $W$ 와 $\mu\ge2$ 의 보존이다.)

**따름 1.5b (순수 부분범주).** $\mathcal R_{\rm pure}^+$ := 항등 + "$W(D')$ 의 모든 점이 순수인 정련". 합성에 닫혀 있고 (순수 $\tau$ 뒤의 합성은 $\Pi''(v)$ 위에서 상수), 비항등 사상에 모두-복사 올림 ($\varepsilon\equiv0$), 항등에 $\mathrm{id}$ 를 주면 엄밀한 함자이다. [증명] 비항등 순수 $\tau$ 와의 합성은 비항등이다 ($|\Pi''(v)|\ge2$ 를 상수로 보내므로 항등일 수 없다; $W(D'')=\varnothing$ 이면 흰 점이 없어 문제없음). (Z2) 는 $0=0\wedge\cdot$ 와 항등 쪽의 $1\wedge a=a$. 모든 성분이 (α) 이므로 (Z1). □

**의미.** $\omega=0$ 은 "점 $v$ 가 다중 접합점이라는 기록이 정련 경로에 무관하다" 는 뜻이다. 장애는 접합 기록을 **보존하는 경로** (포화) 와 **지우는 경로** (중간에 $v$ 를 한 조각에만 두는 분해를 거침, 즉 $\Delta\ne\varnothing$) 가 같은 정련 안에 공존할 때 생긴다. 두 종류를 섞지 않는 부분범주 (포화만, 또는 순수만) 에서는 엄밀한 함자가 있다.

#### 1.5 보편성: 장애는 모든 $G$ 에 있다

**정리 1.6.** $V(G)\ne\varnothing$ 인 모든 그래프 $G$ 에서 $\omega_{\mathcal R_{\rm adm}(G)}\ne0$. 따라서 $\mathcal R_{\rm adm}(G)$ (그리고 $\mathbf{Ref}(G)$) 위의 함자 올림은 없다.

*증명.* 점 $u$ 를 고른다. $S$ := $u$ 와 그 이웃, $u$ 에 닿는 변 전부 (별, 평면). $U:=(\{u\},\varnothing)$ ($K_1$, 평면; 교재 정의 1.1 은 고립점과 조각 반복을 허용). $R$ := $u$ 에 닿지 않는 변 하나씩의 $K_2$ 조각과, 나머지 점의 $K_1$ 조각들의 목록. 분해
$$D_2=(S,U,R),\ D_3=(S,U,U,R),\ D_1=(S,U,R),\ D_0=(S,R)$$
는 모두 $G$ 의 평면분해이다. 정련: $\tau:D_2\to D_3$ ($S\mapsto S$, $U\mapsto U_1$, $R$ 항등), $\sigma:D_3\to D_1$ ($S\mapsto S$, $U_1\mapsto S$, $U_2\mapsto U$, $R$ 항등), $\tau'':D_2\to D_0$ ($S,U\mapsto S$), $\sigma'':D_0\to D_1$ (포함). $\sigma\tau=\sigma''\tau''=:\pi$ ($S,U\mapsto S$). 
- 어떤 분해에서도 두 조각이 공유하는 변이 없다 ($U$ 는 변이 없고 $R$ 의 변은 서로 다르며 $S$ 와 겹치지 않는다. $D_3$ 의 $U_1,U_2$ 도 변이 없다). 그러므로 모든 $\Gamma$ 가 변이 없고, 네 정련 모두 올림 가능하다 (R08 계 (ii)). 
- $u$ 의 조각 집합: $D_2$ 에서 $\{S,U\}$, $D_3$ 에서 $\{S,U_1,U_2\}$, $D_1$ 에서 $\{S,U\}$, $D_0$ 에서 $\{S\}$. 
- $\tau$ 단사 ⟹ $u$ 불순. $\sigma$ 는 $\{S,U_1,U_2\}\mapsto\{S,S,U\}$ 로 불순. 그러므로 $F=(\sigma,\tau)$ 는 $u$ 를 살림 강제. 
- $u\notin W(D_0)$ 이므로 $F'=(\sigma'',\tau'')$ 는 죽임 강제. 
따라서 $\omega(\pi)(u)=1$. □

[계산 확인] $G=K_4$, $u=0$ 에서 $|L(\tau)|=|L(\sigma)|=|L(\tau'')|=|L(\sigma'')|=1$, $|L(\pi)|=2$, 두 인수분해가 $w_0$ 를 각각 $w_0$ 와 $(0,S)$ 로 강제 (r10_obs.py). 참고: $U$ 대신 $S$ 를 두 번 쓰면 이웃 점이 불순이 되어 $\tau''$ 가 올림 불가능해진다 (같은 파일의 첫 시도에서 $|L(\tau'')|=0$). $K_1$ 조각이 결합을 끊는 역할을 한다.

**해석.** 장애는 그래프의 성질이 아니라 **분해 범주의 성질**이다. 고립점 조각이 허용되는 한 모든 $G$ 에 있다. 함자적 설명서를 원하면 대상 또는 사상을 제한해야 한다 (포화, 순수, 단사) — 이것이 R09 의 "전체 정련 범주에서 불가능" 의 정확한 범위다.

### 2. 블록 함자 $\theta$ 와 색칠수·평면성 (임무 2)

#### 2.0 기호
- $\mathcal B(D)$: 블록 (R09 §0). $b(D):=\max_{\beta}\chi(\beta)=\max_k\chi(P_k)$ (그래프의 $\chi$ 는 성분별 최댓값). $\mathrm{gap}(D):=\chi(G)-b(D)\ge0$ (R07 따름 5.2(a)).
- **허브** $W_B(D):=\{v:\ v$ 가 두 개 이상의 블록에 속함$\}$. 같은 조각의 두 블록은 점을 공유하지 않으므로 $W_B(D)=W(D)$. [증명]
- **접속 그래프** $I(D)$: 이분 그래프, 점 = 블록 $\sqcup$ 허브, 변 = $(v,\beta)$, $v\in V(\beta)$. $r(D):=\beta_1(I(D))=|E(I)|-|V(I)|+c(I)$.
- 블록 수준 대상 $D^{cc}$ 는 평면분해이다 (R09 §0). 위 불변량은 모두 $D^{cc}$ 에만 의존한다. 그러므로 R09 예 2.6 의 성분 분할 사상 (정련 아님) 은 블록 수준에서 동형 $D'^{cc}\cong D^{cc}$ 이고 $b,r,\mathrm{gap}$ 을 보존한다. [증명]

#### 2.1 $\chi$ 는 θ-불변, 국소량만 움직인다

**명제 2.1 (극한의 자연 동형).** $\mathrm{Col}^{B}_q(D):=\{(c_\beta)_\beta:\ c_\beta\in\mathrm{Col}_q(\beta),\ $ 공유점에서 일치$\}$ 로 두면, 블록 사상 $\theta:D'\to D$ 의 제한 $r_\theta:(c_\beta)\mapsto(c_{\theta\beta'}|_{\beta'})$ 은 잘 정의된 전단사이고, $\mathrm{Col}^B_q:\mathbf{Blk}^{op}\to\mathbf{Set}$ 는 상수 함자 $\mathrm{Col}_q(G)$ 와 자연 동형이다. [증명] R07 정리 5.1 을 평면분해 $D^{cc}$, $D'^{cc}$ 에 쓰면 두 집합은 모두 $\mathrm{Col}_q(G)$ 와 같고 ($c\mapsto(c|_\beta)$), $r_\theta$ 는 이 동일시에서 항등이다 ($c|_{\theta\beta'}|_{\beta'}=c|_{\beta'}$). □
**뜻.** $\chi$ 의 $H^0$ 장애 (호환족의 부재) 는 θ 에 의해 동형으로 옮겨진다. 블록 함자는 $\chi$ 를 바꿀 수 없다. 바뀌는 것은 국소 상계와 접착 복잡도이다.

**명제 2.2 (단조성).** $\mathbf{Blk}(D',D)\ne\varnothing$ 이면 $b(D')\le b(D)$, 따라서 $\mathrm{gap}(D')\ge\mathrm{gap}(D)$. 특히 정련 $\sigma$ 마다 (θ_σ 를 통해) 성립하고, $\mathrm{gap}$ 은 함자 $\mathbf{Blk}\to(\mathbb Z_{\ge0},\ge)$ 이다. [증명] $\beta'\subseteq\theta\beta'$ 는 준동형이므로 $\chi(\beta')\le\chi(\theta\beta')\le b(D)$ (R07 명제 5.3). □
즉 **거칠게 할수록 간극은 줄어든다**. $\mathrm{gap}(D')=0\Rightarrow\mathrm{gap}(D)=0$.

#### 2.2 접착 사이클 수 $r(D)$

**보조명제 2.3 (오일러 공식).** $r(D)=\beta_1(G)+\sum_{e\in E}(\mu_D(e)-1)-\sum_{\beta\in\mathcal B(D)}\beta_1(\beta)$.
*증명.* $G^\sharp$ := 블록의 서로소 합에서 같은 점의 복사들을 동일시한 다중그래프 (변은 중복 유지). $|V(G^\sharp)|=|V|$, $|E(G^\sharp)|=\sum_\beta|E(\beta)|=|E|+\sum_e(\mu(e)-1)$ (한 조각의 변은 그 조각의 블록 하나에만 있으므로 블록 중복도 = $\mu$), $c(G^\sharp)=c(G)=c(I)$. 또 $\sum_\beta|V(\beta)|=|V|+\sum_{v\in W_B}(\deg_I v-1)=|V|+|E(I)|-|W_B|$. 그러므로 $\sum_\beta\beta_1(\beta)=|E(G^\sharp)|-|V|-|E(I)|+|W_B|+|\mathcal B|$ 이고 $\beta_1(G^\sharp)-\sum\beta_1(\beta)=|E(I)|-|W_B|-|\mathcal B|+c(I)=r(D)$. $\beta_1(G^\sharp)=\beta_1(G)+\sum_e(\mu(e)-1)$. □

**명제 2.4 (나무 접착).** $r(D)=0$ 이면 $\chi(G)=b(D)$ 이고 $G$ 는 평면이다.
*증명.* ($\chi$) 성분마다 $I$ 가 나무이다. 뿌리 블록에서 BFS 로 블록을 차례로 칠한다. 블록 $\beta$ 에 부모 허브 $v$ 를 통해 도달하면 $\beta$ 의 다른 점은 아직 칠해지지 않았다 (이미 칠해진 블록과 다른 허브를 공유하면 $I$ 에 사이클). $\beta$ 를 $b(D)$ 색으로 칠한 뒤 색을 치환해 $v$ 의 색을 맞춘다 (치환은 진짜 색칠을 보존). 모든 $G$ 의 변은 어떤 블록 안에 있으므로 결과는 진짜 색칠. [증명] (평면) 같은 귀납으로 1-합을 반복한다. 각 블록은 평면 조각의 부분그래프이므로 평면 (그림의 제한). 1-합의 평면성에는 "평면 그래프는 주어진 점이 바깥면 경계에 오도록 그릴 수 있다" 를 쓴다 [기억-미검증: 교재 제0장 정의로 이 사실을 확인하지 않음]. □
STATUS 의 "1-합에서는 $\chi=\max$" ([기억-미검증] 로 적혀 있던 것) 는 명제 2.4 의 $\chi$ 부분으로 증명된다.

**정리 2.5 (허브 가로지름 상계).** $U\subseteq W_B(D)$ 가 $I(D)-U$ 를 숲으로 만들면
$$\chi(G)\ \le\ \max_{\beta}\chi(\beta-U)\ +\ \chi(G[U])\ \le\ b(D)+\chi(G[U]).$$
특히 $\chi(G)\le b(D)+r(D)$, 즉 $\mathrm{gap}(D)\le r(D)$.
*증명.* $D_U$ := 블록 $\beta-U$ 들의 연결 성분 전체 (평면, 합이 $G-U$). $D_U$ 의 허브는 $W_B(D)\setminus U$ 에 있고 ($\beta-U$ 의 서로 다른 성분은 점을 공유하지 않으므로, 두 $D_U$-블록에 속한 점은 두 $D$-블록에 속함), 사상 $(v,\gamma)\mapsto(v,\beta(\gamma))$ 는 $I(D_U)\to I(D)-U$ 의 변-단사 준동형이다. $I(D_U)$ 의 사이클은 숲 $I(D)-U$ 안의 닫힌 트레일 (변 반복 없음) 로 가는데, 숲에는 길이 양의 닫힌 트레일이 없다. 따라서 $r(D_U)=0$ 이고 명제 2.4 로 $\chi(G-U)=b(D_U)=\max\chi(\beta-U)$. $U$ 에 새 색 $\chi(G[U])$ 개를 쓰면 상계. 마지막: 이분 그래프 $I$ 의 모든 사이클은 허브를 지나고, 사이클 위의 점 하나를 지우면 $\beta_1$ 이 1 이상 준다 ($\beta_1(I-v)=\beta_1(I)-\deg v+1+(c(I-v)-c(I))$, 사이클 위의 점이면 $c(I-v)-c(I)\le\deg v-2$). 그러므로 $|U|\le r(D)$ 인 가로지름이 있고 $\chi(G[U])\le|U|$. □

**평면성 쪽 귀결.** $G$ 가 비평면이면 모든 평면분해에서 $r(D)\ge1$ (명제 2.4 의 대우). $r=1$ 로 이미 비평면일 수 있다: $K_5=(K_5-e)\cup K_2$ 는 $r=1$. 따라서 $r$ 은 평면성의 "0 판정" 만 주고 종수의 정확한 상계인지는 미확인 (후속 3). [증명] [계산 확인]

#### 2.3 θ 를 따라 $r$ 은 어떻게 움직이나

**명제 2.6 (변-분할 분해에서는 단조).** $D',D$ 가 모두 변-분할 ($\mu\equiv1$) 이고 $\mathbf{Blk}(D',D)\ni\theta$ 이면 $r(D)\le r(D')$. [증명] $\mu\equiv1$ 이면 $\beta$ 의 각 변 $e$ 는 정확히 하나의 $D'$-블록 $\beta'$ 에 있고 $\theta\beta'\supseteq\beta'\ni e$ 이므로 $\theta\beta'=\beta$. 따라서 $E(\beta)=\bigsqcup_{\theta\beta'=\beta}E(\beta')$. 변이 서로소인 부분그래프 $H_i$ 의 합 $H$ 에 대해 $\beta_1(H)-\sum\beta_1(H_i)$ 는 $H_i$ 들의 접속 그래프의 $\beta_1$ (보조명제 2.3 의 계산과 같음) 이므로 $\ge0$. 그러므로 $\sum_\beta\beta_1(\beta)\ge\sum_{\beta'}\beta_1(\beta')$ 이고 (변 없는 블록은 $\beta_1=0$), 보조명제 2.3 에서 $\mu$ 항이 0 이므로 $r(D)\le r(D')$. □

**일반적으로는 단조가 아니다 (예 2.7).** 중복 조각이 $\sum(\mu-1)$ 을 늘리기 때문이다. 극단 예: 평면 $G$ 의 $(G)\to(G,G)$ 는 블록 사상이고 $r$ 이 $0\to|V|-1$ 로 늘어난다. [증명]

#### 2.4 예

**예 2.7 ($K_4=C_4\cup C_4$, 교재 예 1.3, 블록 수준).** $P_1=0\text{-}1\text{-}3\text{-}2\text{-}0$, $P_2=0\text{-}3\text{-}1\text{-}2\text{-}0$, 공유 변 $13,02$ ($\mu=2$). 세 분해와 정련
$$D'=(\text{6 개의 }K_2)\ \longrightarrow\ D'''=(P_1,\{03\},\{12\})\ \longrightarrow\ D=(P_1,P_2).$$
($D'''$ 의 두 $K_2$ 는 $P_2$ 에 들어가고 $P_1$ 은 $P_1$ 로.)

| 분해 | $b$ | $r$ | $\chi(K_4)$ | gap | $b+r$ | 공식 $\beta_1(G)+\sum(\mu-1)-\sum\beta_1$ |
|---|---|---|---|---|---|---|
| $D'$ (변 6) | 2 | 3 | 4 | 2 | 5 | $3+0-0$ |
| $D'''$ | 2 | 2 | 4 | 2 | **4 (등호)** | $3+0-1$ |
| $D$ | 2 | 3 | 4 | 2 | 5 | $3+2-2$ |

[계산 확인] (r10_blk.py) [증명: 보조명제 2.3 으로 손계산 일치]
- gap 은 $2,2,2$ 로 명제 2.2 와 맞다 (단조 비증가). $r$ 은 $3\to2\to3$ 으로 단조가 아니다. $D'\to D'''$ 는 변-분할 사이라 명제 2.6 대로 감소, $D'''\to D$ 는 $\mu=2$ 인 변 2개가 생겨 증가.
- 정리 2.5 의 첫 부등식은 세 분해 모두에서 등호가 되도록 $U$ 를 고를 수 있다: $D$ 에서 $U=\{1,2,3\}$ ($I=K_{2,4}$, 허브 하나만 남김): $\max\chi(\beta-U)=1$, $\chi(G[U])=\chi(K_3)=3$, 합 4. $D'''$ 와 $D'$ 에서 $U=\{0,1\}$: $\max\chi(\beta-U)=2$ (블록 $P_1-U\ni$ 변 $23$, 또는 블록 $23$), $\chi(G[U])=2$, 합 4. [증명: 손계산]
- $D$ 의 $\mathfrak M$ 에는 $E_{11}$ (변 $13,02$ 위) 이 있지만, 블록 수준 불변량은 $E_{11}$ 을 $\sum(\mu-1)$ 항으로만 본다. 흰 점 장애 (§1) 와 색칠 부등식 (§2) 은 서로 다른 층에 있다.

**예 2.8 (R09 예 2.6, 성분 분할).** $G=ab\sqcup cd$, $D'=(Q_1)$, $D=(P_1,P_2)$. $D'^{cc}=D^{cc}$ 이므로 $b=2$, $r=0$ (허브 없음), $\chi=2$, gap 0, $G$ 평면 — 명제 2.4 의 자명한 경우. $\mathbf{Ref}(D',D)=\varnothing$ 이지만 $\mathbf{Blk}$ 에서는 동형이라 모든 블록 불변량이 같다. [증명] [계산 확인]

**예 2.9 (STATUS 최소 예와 $K_5$).** $K_4=(K_4-uv)\cup K_2$: $b=3$, $r=1$, $\chi=4=b+r$ (등호). $K_5=(K_5-e)\cup K_2$: $b=4$, $r=1$, $\chi=5=b+r$ (등호), 비평면. 이 두 예는 "공유 점 2개, 한 조각에서만 변" 의 간극 1 이 정확히 접착 사이클 1 개에서 온다는 것을 보인다. [계산 확인] [증명: $\chi$ 값은 클릭 수와 $K_n-e$ 의 $(n-1)$-색칠]

### 3. 장애물 (정직하게)

- **O1 (불 계수의 코호몰로지 류).** 명제 1.3 은 코사이클 항등식을 주지만, 선택을 바꿀 때의 변화가 코경계로 쓰이지 않아 $H^2$ 류를 정의하지 못했다 (장애물 A1). $\omega$ 는 그 대용인 국소 불변량이다.
- **O2 ($\omega\equiv0$ 의 충분성).** 필요조건 ($\omega\equiv0$) 과 충분조건 ((P) 또는 (P*)) 사이가 비어 있다. 함자는 "샌드위치" $\alpha\le\varepsilon\le1-\zeta$ 안의 곱셈적 $\varepsilon$ 인데, $\omega\equiv0$ 이어도 그런 $\varepsilon$ 이 없는 부분범주가 있는지 모른다 [추측: 있다. 세 인수분해가 서로 다른 성분 결합으로 충돌하는 경우].
- **O3 (1-합 평면성).** 명제 2.4 의 평면성 부분은 "주어진 점을 바깥면에" 라는 고전 사실을 쓴다 [기억-미검증]. $\chi$ 부분은 이것 없이 증명됨.
- **O4 ($r$ 과 종수).** $r$ 은 $\theta$ 를 따라 단조가 아니며 (예 2.7), $K_5$ 에서 $r=1$ 로 비평면이 되므로 "$r\ge$ 종수" 같은 관계가 있다면 중복도 보정이 필요하다. 시도하지 못했다.
- **O5 (교재 밖 의존).** O3 하나뿐. 4색정리는 쓰지 않는다.

## 문주님께 요청

없음.

## 후속연구 지점

1. **$\omega\equiv0$ 이지만 함자가 없는 부분범주 (또는 그 불가능성 증명).** 무엇을: 장애물 O2 의 샌드위치 문제를 판정. 왜: $\omega$ 가 완전한 장애인지 (H¹ 형 장애의 "값" 이 충분한지) 가 §1 의 핵심 미결이다. 시작 방법: Γ′ 에 변이 있는 (성분 결합이 있는) 작은 분해 셋을 골라 (P) 와 (P*) 가 둘 다 깨지는 부분범주를 만들고, 곱셈적 $\varepsilon$ 의 존재를 손으로 판정. 증명 쪽은 "$\varepsilon:=1-\zeta$ 가 실패하는 최소 쌍" 에서 다른 선택이 반드시 다른 사각형에서 $\omega=1$ 을 만든다는 귀류를 시도. 난점: 부분범주를 정할 때 인수분해 전체를 통제해야 한다.
2. **포화·순수 부분범주의 쌍 구조와 설명서 정의.** 무엇을: 정련을 포화 부분과 순수 부분의 합성으로 쓰는 분해 ($\sigma=\sigma_{\rm sat}\circ\sigma_{\rm pure}$ 꼴 인수분해) 가 존재·유일한지 판정. 왜: 존재·유일하면 $\mathcal R_{\rm adm}$ 이 두 엄밀 함자의 "분해 체계" (factorization system) 를 갖고, 함자 올림을 이 체계에 맞춰 정의할 수 있다 — 장애를 정의 수준에서 없애는 방법. 시작 방법: 정리 1.6 의 $\pi$ 가 $D_0$ 을 거치는 (순수 후 포화) 인수분해와 $D_3$ 를 거치는 것 중 어느 쪽이 표준인지, 직교성 (lifting property) 을 확인. 난점: 순수 사상은 항등을 포함하지 않아 범주론의 표준 분해 체계 공리를 그대로 쓸 수 없다.
3. **$r(D)$ 의 중복 보정판과 종수.** 무엇을: $r^\flat(D):=\beta_1(G)-\sum_\beta\beta_1(\beta)$ (보조명제 2.3 에서 $\mu$ 항을 뺀 것) 또는 변-분할로 줄인 분해에서 $\min_D r$ 이 $G$ 의 종수·$\chi$ 와 어떤 부등식을 갖는지. 왜: $\chi\le b+r$ 이 평면 조각에서 얼마나 sharp 한지, 그리고 θ-단조인 보정 불변량이 있는지가 블록 함자의 쓸모를 정한다. 시작 방법: R04 의 평면 +2 반례 ($C_9$ + 잎 30개) 에서 잎을 하나씩 합치는 정련 사슬로 $b,r$ 을 추적하고, $\mathrm{gap}=2$ 가 어느 단계의 사이클에서 오는지 찾는다. 난점: $r$ 이 커서 $b+r$ 상계가 매우 느슨하므로, 정리 2.5 의 첫 부등식 ($\chi(G[U])$ 판) 을 써야 한다.
4. **블록 수준과 흰 점 수준의 결합: $\mathfrak M$ 의 블록 몫.** 무엇을: $\mathfrak M(D)$ 에서 $E_{00}$-성분 (블록) 을 한 점으로 수축한 그래프가 $I(D)$ 에 $E_{11}$ 의 상을 더한 것과 같은지, 그리고 R08 수축 상계가 이 몫에 대해 $\chi(\mathfrak M)$ 과 $b,r$ 을 잇는지 확인. 왜: 임무 1 (흰 점) 과 임무 2 (블록) 가 같은 그래프의 두 층이므로, 한 그림에서 두 장애를 동시에 읽을 수 있는지 시험. 시작 방법: 예 2.7 의 $D$ 에서 수축을 손으로 계산. 난점: 블록은 $\mathfrak M$ 에서 연결이지만 $\chi(\mathfrak M[\beta])=\chi(\beta)$ 이므로 계 R8-8 의 항이 $\sum(\chi(\beta)-1)$ 로 커져 상계가 느슨해진다.
