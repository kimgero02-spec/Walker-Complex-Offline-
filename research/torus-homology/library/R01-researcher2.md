# [R01-researcher2] 토러스 $T^n$ 호몰로지의 일반 구조: 세 가지 유도, 패턴, 코호몰로지 환, 일반화

- 작성자: researcher2 (패턴 추출·이론 구조화) / 라운드: 1 / 임무: $H_k(T^n;\mathbb Z)\cong\mathbb Z^{\binom nk}$ 의 다중 유도, $n\le 4$ 표와 패턴, 코호몰로지 환, 일반화 방향

## 요약
1. **[증명]** $H_k(T^n;\mathbb Z)\cong\mathbb Z^{\binom nk}$ 를 (a) 곱 CW 구조(셀 $\binom nk$ 개, 셀룰러 경계 0), (b) 퀴네트 공식(자유 가군이므로 Tor 소멸)+귀납, (c) $T^2$ 마이어-비토리스 로 각각 유도했다.
2. **[계산 확인]** $S^1$ 을 정점 2·변 2 의 CW(경계사상 **비자명**)로 잡아 체인 텐서곱으로 $T^n$ ($n\le4$) 를 만들고 스미스 표준형으로 계산: 셀 수는 $2^n\binom nk$ 이지만 호몰로지는 $(1,4,6,4,1)$ 등 정확히 $\binom nk$, 비틀림 없음.
3. 패턴: 포앵카레 다항식 $P_{T^n}(t)=(1+t)^n$, $\chi=P(-1)=0$, 비틀림 없음, $\binom nk=\binom n{n-k}$ (푸앵카레 쌍대성).
4. **[증명 스케치]** $H^*(T^n;\mathbb Z)\cong\Lambda_{\mathbb Z}[x_1,\dots,x_n]$, $\deg x_i=1$; $T^2$ 에서 $\langle x_1\smile x_2,[T^2]\rangle=\pm1$, 즉 $x_1\smile x_2$ 가 $H^2$ 의 생성원(기본류의 쌍대).
5. 일반화: $\Sigma_g$ 는 비틀림 없음·쌍대성 유지, $(1+t)^n$ 곱구조와 $\chi=0$ 은 깨짐($\chi=2-2g$). 렌즈 공간 $L(p,q)$ 는 $\chi=0$·쌍대성 유지, 비틀림 없음은 깨짐($H_1=\mathbb Z/p$). "모든 차수 1 류의 곱이 기본류를 생성"은 $K(\mathbb Z^n,1)$ 인 닫힌 다양체 = $T^n$ 을 특징짓는 성질이라는 추측/관찰.

## 본문

### 1. 세 가지 유도

#### (a) 곱 CW 구조 — [증명]
$S^1=e^0\cup e^1$, 셀룰러 체인 $C_*(S^1)$: $\mathbb Z\xleftarrow{0}\mathbb Z$ ($\partial e^1=v-v=0$).
곱 CW 구조에서 $T^n$ 의 $k$-셀은 $e^{\varepsilon_1}\times\cdots\times e^{\varepsilon_n}$, $\varepsilon_i\in\{0,1\}$, $\sum\varepsilon_i=k$ 이므로 정확히 $\binom nk$ 개 (부분집합 $I\subset\{1,\dots,n\}$, $|I|=k$ 와 일대일: $e_I$).
곱 셀의 셀룰러 경계는 라이프니츠 규칙
$$\partial(e_a\times e_b)=\partial e_a\times e_b+(-1)^{\dim e_a}e_a\times\partial e_b$$
를 따른다 (즉 $C_*(X\times Y)\cong C_*(X)\otimes C_*(Y)$, Hatcher Prop. 3B.1 류). 각 인수의 경계가 0 이므로 모든 $\partial_k=0$, 따라서 $H_k=C_k\cong\mathbb Z^{\binom nk}$. $\square$

대안(곱 공식 없이): $T^2$ 는 정사각형 $aba^{-1}b^{-1}$ 으로 붙이므로 $\partial e^2=a+b-a-b=0$. 일반 $T^n$ 은 $n$-큐브 $[0,1]^n$ 의 대면 동일시이고, 각 $k$-면 $e_I$ 의 경계에서 $x_j=0$ 면과 $x_j=1$ 면이 같은 셀로 동일시되며 부호가 반대로 나타나 상쇄된다.

#### (b) 퀴네트 공식 — [증명]
PID $\mathbb Z$ 위에서 자연스러운 분할 완전열
$$0\to\bigoplus_{i+j=k}H_i(X)\otimes H_j(Y)\to H_k(X\times Y)\to\bigoplus_{i+j=k-1}\operatorname{Tor}(H_i(X),H_j(Y))\to0.$$
$X=T^{n-1}$, $Y=S^1$ 로 귀납. $H_*(S^1)=\mathbb Z,\mathbb Z$ 는 자유(따라서 평탄) 가군이므로 $\operatorname{Tor}(A,\mathbb Z)=0$ 이 모든 $A$ 에 대해 성립 — **Tor 항이 사라지는 이유는 한쪽 인수 $S^1$ 의 호몰로지가 비틀림 없는 자유 가군이기 때문**이다 (귀납 가정으로 $T^{n-1}$ 쪽도 자유이므로 이중으로 성립). 따라서
$$H_k(T^n)\cong H_k(T^{n-1})\oplus H_{k-1}(T^{n-1})\cong\mathbb Z^{\binom{n-1}k+\binom{n-1}{k-1}}=\mathbb Z^{\binom nk}$$
(파스칼 항등식). 같은 논법이 포앵카레 다항식의 곱셈성 $P_{X\times Y}=P_XP_Y$ 를 준다(어느 한쪽이 비틀림 없을 때 $\mathbb Z$ 계수에서도 성립). $\square$

#### (c) $T^2$ 의 마이어-비토리스 — [증명]
$T^2=S^1_a\times S^1_b$ 를 두 번째 인수 방향으로 두 열린 원기둥 $U,V\simeq S^1$ 로 덮으면 $U\cap V\simeq S^1\sqcup S^1$.
$$0\to H_2(T^2)\xrightarrow{\ \partial\ }H_1(U\cap V)\xrightarrow{\ \Phi_1\ }H_1(U)\oplus H_1(V)\to H_1(T^2)\xrightarrow{\ \partial\ }H_0(U\cap V)\xrightarrow{\ \Phi_0\ }H_0(U)\oplus H_0(V)\to H_0(T^2)\to0$$
- $H_1(U\cap V)=\mathbb Z^2$ (두 성분의 $a$-원 $\alpha_1,\alpha_2$), $\Phi_1(\alpha_i)=(\alpha,-\alpha)$ ⇒ $\Phi_1=\begin{pmatrix}1&1\\-1&-1\end{pmatrix}$, 랭크 1, $\ker\Phi_1=\langle\alpha_1-\alpha_2\rangle\cong\mathbb Z$, $\operatorname{coker}\Phi_1\cong\mathbb Z$ (비틀림 없음: 상이 원시벡터 $(1,-1)$ 로 생성).
- $\Phi_0=\begin{pmatrix}1&1\\-1&-1\end{pmatrix}$ 역시 $\ker\Phi_0\cong\mathbb Z$.
- 따라서 $H_2(T^2)\cong\ker\Phi_1\cong\mathbb Z$ ($H_2(U)=H_2(V)=0$), 그리고 $0\to\operatorname{coker}\Phi_1(\cong\mathbb Z)\to H_1(T^2)\to\ker\Phi_0(\cong\mathbb Z)\to0$ 이 분할(자유 몫)되어 $H_1(T^2)\cong\mathbb Z^2$, $H_0\cong\mathbb Z$. $\square$
(기하적 의미: $H_1$ 의 생성원은 $a$ 와, $\ker\Phi_0$ 를 들어올린 $b$-원. $H_2$ 생성원 $\alpha_1-\alpha_2$ 의 상은 기본류.)
일반화: 같은 덮개로 $T^n=T^{n-1}\times S^1$ 에 MV 를 쓰면 $\Phi$ 가 $(x,x)\mapsto$ 형태로 짧은 완전열 $0\to H_k(T^{n-1})\to H_k(T^n)\to H_{k-1}(T^{n-1})\to0$ 이 나온다 (이는 사실상 Wang 열/퀴네트와 동일).

#### (d) 계산 검증 — [계산으로 확인]
`rooms/researcher2/tor.py`: $S^1$ 을 정점 2·변 2 의 CW 로 잡아 $\partial_1\neq0$ 인 체인복합체를 만들고, 부호 $(-1)^p$ 를 넣은 텐서곱으로 $T^n$ 체인복합체 구성($\partial^2=0$ 확인) 후 sympy 스미스 표준형.

| $n$ | 셀 수 $(c_0,\dots,c_n)$ | $H_*$ 랭크 | 비틀림 |
|---|---|---|---|
| 1 | (2,2) | (1,1) | 없음 |
| 2 | (4,8,4) | (1,2,1) | 없음 |
| 3 | (8,24,24,8) | (1,3,3,1) | 없음 |
| 4 | (16,64,96,64,16) | (1,4,6,4,1) | 없음 |

셀 수 $2^n\binom nk$ 와 무관하게 결과가 $\binom nk$ — CW 구조 선택에 대한 불변성의 실례.

### 2. 표와 패턴

| $n$ | $H_0$ | $H_1$ | $H_2$ | $H_3$ | $H_4$ | $P(t)$ | $\chi$ |
|---|---|---|---|---|---|---|---|
| 1 | $\mathbb Z$ | $\mathbb Z$ | | | | $1+t$ | 0 |
| 2 | $\mathbb Z$ | $\mathbb Z^2$ | $\mathbb Z$ | | | $(1+t)^2$ | 0 |
| 3 | $\mathbb Z$ | $\mathbb Z^3$ | $\mathbb Z^3$ | $\mathbb Z$ | | $(1+t)^3$ | 0 |
| 4 | $\mathbb Z$ | $\mathbb Z^4$ | $\mathbb Z^6$ | $\mathbb Z^4$ | $\mathbb Z$ | $(1+t)^4$ | 0 |

추출된 패턴 (모두 [증명]):
1. **이항계수/파스칼**: $b_k(T^n)=\binom nk$, $b_k(T^n)=b_k(T^{n-1})+b_{k-1}(T^{n-1})$ — 퀴네트 분해의 직접 반영.
2. **포앵카레 다항식** $P_{T^n}(t)=(1+t)^n$ — $P$ 의 곱셈성과 $P_{S^1}=1+t$.
3. **오일러 지표 0**: $\chi=P(-1)=0$ ($n\ge1$). 독립 근거: $S^1$ 이 $T^n$ 에 고정점 없이 작용 / 항등 사상과 호모토픽한 고정점 없는 이동 ⇒ 레프셰츠 수 $=\chi=0$.
4. **비틀림 없음**: 모든 $H_k$ 자유 (셀룰러 경계 0).
5. **쌍대성 대칭** $b_k=b_{n-k}$: $T^n$ 은 닫힌 가향 $n$-다양체이므로 $H_k\cong H^{n-k}$; 비틀림 없으므로 $H^{n-k}\cong\operatorname{Hom}(H_{n-k},\mathbb Z)$ 와 결합해 $H_k\cong H_{n-k}$.
6. 총 랭크 $\sum_k b_k=2^n$ (부분집합 개수), $H_1(T^n)=\pi_1^{ab}=\mathbb Z^n$ (이미 아벨).

### 3. 코호몰로지 환 — [증명 스케치]
**정리.** $H^*(T^n;\mathbb Z)\cong\Lambda_{\mathbb Z}[x_1,\dots,x_n]$, $x_i=p_i^*(\theta)$, $\theta\in H^1(S^1)$ 생성원, $p_i:T^n\to S^1$ 사영.

스케치: (i) 코호몰로지 퀴네트(유한형·비틀림 없음)로 교차곱 $H^*(T^{n-1})\otimes H^*(S^1)\xrightarrow{\times}H^*(T^n)$ 은 **환** 동형이고, $a\times b=p_1^*a\smile p_2^*b$. (ii) $H^*(S^1)=\Lambda[\theta]$ ($\theta^2\in H^2(S^1)=0$). (iii) 차수 1 원소의 등급 교환성: $x_i\smile x_j=-x_j\smile x_i$, 그리고 $x_i\smile x_i=p_i^*(\theta\smile\theta)=0$ (정수 계수에서도 성립 — 등급 교환성만으로는 $2x^2=0$ 이지만 자연성으로 0). (iv) 귀납적으로 $\Lambda[x_1..x_{n-1}]\otimes\Lambda[x_n]\cong\Lambda[x_1..x_n]$ (등급 텐서곱). 기저 $x_I=x_{i_1}\smile\cdots\smile x_{i_k}$, $i_1<\dots<i_k$, 은 셀 $e_I$ 의 쌍대 코체인에 해당: $\langle x_I,e_J\rangle=\pm\delta_{IJ}$.

**$T^2$ 에서 $x_1\smile x_2$.** $H^2(T^2)\cong\mathbb Z$ 이고 $x_1\smile x_2=p_1^*\theta\smile p_2^*\theta=\theta\times\theta$. $\langle\theta\times\theta,[S^1]\times[S^1]\rangle=\langle\theta,[S^1]\rangle^2=1$ (부호 관례 $(-1)^{\deg\cdot\deg}$ 는 차수 0 쌍에서 무해) 이고 $[T^2]=[S^1]\times[S^1]$ 이므로 $\langle x_1\smile x_2,[T^2]\rangle=1$. 즉 $x_1\smile x_2$ 는 기본류의 쌍대 $[T^2]^*$ 로 $H^2$ 를 생성. 동치 표현: 캡곱 $(x_1\smile x_2)\frown[T^2]=$ 점의 류; 교차 이론 관점 $a\cdot b=\pm1$ (두 생성 원의 횡단 교차 1점). 단체 계산(정사각형을 두 삼각형으로 나눠 알렉산더-휘트니 공식 적용)은 Hatcher Ex. 3.7 의 표준 계산과 일치.
일반 $n$: $x_1\smile\cdots\smile x_n$ 이 $[T^n]$ 의 쌍대이며, 컵곱 쌍 $H^k\times H^{n-k}\to H^n\cong\mathbb Z$, $x_I\smile x_{I^c}=\pm x_{1..n}$ 은 유니모듈러 — 푸앵카레 쌍대성의 대수적 모습(이는 [증명]: 기저 $\{x_I\}$ 와 $\{x_{I^c}\}$ 가 부호 순열 행렬로 짝지어짐).

### 4. 일반화 방향

| 성질 | $T^n$ | $\Sigma_g$ ($g\ge2$) | $L(p,q)$ | 근거 |
|---|---|---|---|---|
| 비틀림 없음 | O | O | **X** ($H_1=\mathbb Z/p$) | 셀룰러 계산 [증명; tor.py 로 $p=2,3,5$ 확인] |
| 푸앵카레 쌍대성 $b_k=b_{n-k}$ | O | O | O ($\mathbb Z$ 계수 랭크 $(1,0,0,1)$; 비틀림은 $T_1\cong T_{n-2}$ 형태로 짝지음) | 닫힌 가향 다양체 [증명] |
| $\chi=0$ | O | **X** ($2-2g$) | O | 홀수 차원 닫힌 다양체는 $\chi=0$ [증명] |
| $P(t)$ 가 $(1+t)$ 의 거듭제곱 | O | **X** ($1+2gt+t^2$) | **X** ($1+t^3$) | 직접 계산 |
| 코호몰로지 환 = 외대수(차수 1 생성) | O | **X**: $H^1$ 의 컵곱 쌍이 심플렉틱 ($a_i b_i=[\Sigma]^*$, $a_ia_j=0$ 등) 이고 $H^1\wedge H^1\to H^2$ 의 핵이 $\binom{2g}{2}-1$ 차원 | **X**: $\mathbb Z/p$ 계수로 $H^*(L;\mathbb F_p)=\Lambda[x]\otimes\mathbb F_p[y]/(y^2)$ ($p$ 홀수), $y=\beta x$ | 표준 결과 [문헌 수준 증명] |
| $K(\pi,1)$ (비구면) | O ($\pi=\mathbb Z^n$) | O ($\pi$ 곡면군) | X (보편 피복 $S^3$) | |

관찰과 추측:
- **[증명]** $T^n$ 의 모든 핵심 패턴은 "$S^1$ 의 호몰로지가 자유 + 곱 구조"의 결과이므로, $H_*(X)$ 가 자유인 유한 CW $X$ 에 대해 $X\times S^1$ 로 반복해도 비틀림 없음·$P$ 곱셈성·$\chi=0$ 이 유지된다 (예: $\Sigma_g\times S^1$, $P=(1+2gt+t^2)(1+t)$, $\chi=0$).
- **[근거 있는 추측/알려진 결과]** "닫힌 가향 $n$-다양체 $M$ 이 $H^1$ 의 원소들의 컵곱으로 0 이 아닌 최고차 류를 만든다"는 조건은 커플 길이(cup-length) $=n$ 을 뜻하며 $\mathrm{cat}(M)\ge n$ 의 하한을 준다. 비구면 다양체 중 $H^*=\Lambda[H^1]$ 이면 $\pi_1$ 이 $\mathbb Z^n$ 처럼 보인다; 실제로 $\pi_1\cong\mathbb Z^n$ 인 닫힌 비구면 다양체는 $T^n$ 과 호모토피 동치 ($K(\pi,1)$ 의 유일성 — 이 부분은 [증명]). 더 강한 위상 강성(위상동형)은 보렐 추측의 알려진 경우.
- **[추측]** 라운드 2 후보: (i) 평탄 다양체(예: 클라인 병 $K$, $H_1=\mathbb Z\oplus\mathbb Z/2$; 3차원 Hantzsche–Wendt 다양체 $H_1=(\mathbb Z/4)^2$)에서 "유한 피복이 $T^n$ 인데 비틀림이 생기는" 현상 — 전이(transfer) 사상으로 $H_*(M;\mathbb Q)\cong H_*(T^n;\mathbb Q)^{G}$ 이므로 유리 베티수는 $\binom nk$ 이하임 [전이 논법 자체는 증명]. (ii) 렌즈 공간 $L(p,q)$ 는 호몰로지·환으로는 $p$ 만 보이고 $q$ 는 링킹 형식 $\pm q^{-1}/p$ (또는 레이데마이스터 비틀림)에서 처음 보임 — 호몰로지 패턴만으로 분류가 깨지는 첫 사례.

### 남은 질문
1. (a) 의 "곱 셀의 경계 = 라이프니츠 규칙"을 셀 부착사상 수준에서 명시적 차수 계산으로 검증할 것 (researcher3 검증 후보).
2. $\mathbb Z/m$ 계수, 그리고 $H^*(T^n;\mathbb Z)$ 의 스틴로드 연산(모두 자명한가: $Sq^1 x=0$, 차수 1 생성원이므로 $Sq^i$ 는 카르탄 공식으로 결정) 정리.
3. 평탄 다양체·$\Sigma_g$ 의 표를 researcher1 의 예제 계산과 교차 확인.

참고 파일: 계산 스크립트 `rooms/researcher2/tor.py`, 노트 `rooms/researcher2/notes.md`.
