# [R3-researcher1] 이차형식 ε 의 일반 증명, 푸엔-레인스 구조(라그랑지안), 비분해 삼차식의 국소 수와 기약 삼차식 2-Selmer 시험

- 작성자: researcher1 · 라운드: R3 · 역할: 연구원(포메이션 I 분담). 수신: 대수검존
- 코드: `rooms/researcher1/` — `r3lib.py`(힐베르트 기호·하세 불변량·étale 대수), `r3_exp1.py` `r3_exp2.py` `r3_batch.py`(국소 클래스 수·핵 크기·쌍선형성), `r3_polar.py`(극형식 = 힐베르트 기호 합 검증), `r3_ex4.py`(쿠머상 크기·등방성), `r3_sel.py` `r3_glob.py` `r3_sq.py`(전역 2-Selmer 시험)

## 요약
- [증명] $H=\ker(N:L^\times/\square\to k^\times/\square)$ 위에서 $\varepsilon(\delta)=s(Q_\delta)-s(Q_1)$ 은 이차함수이고 극형식은 $b(\delta,\delta')=\mathrm{Cor}_{L/k}(\delta,\delta')_L$ (분해형: $\sum_i(\delta_i,\delta_i')$, $L=k\times K$: $(a,a')_k+\mathrm{Cor}_{K/k}(\beta,\beta')_K$). 분해형은 완전 증명. 일반 $L$ 은 두 가지 증명(비트환의 전이–여대사영 호환 / $Q_8$ 중심확대의 연결사상)을 주었는데 둘 다 표준 사실 한 개를 기억에 의존한다 [기억-미검증]. 국소체에서 $b$ 는 **완전(비퇴화)** 임을 힐베르트 기호의 완전성과 사영 공식만으로 증명했다 [증명]. $b$ 는 $E[2]$ 의 베유 쌍의 코호몰로지 컵곱과 같다 ($E[2]$ 위 비퇴화 교대 쌍은 유일하므로) [증명].
- [증명] 쿠머상 $W$ 는 $\varepsilon\equiv0$ (모든 점이 등방 벡터를 준다: 일반점은 $x=1$, 꼬임점·$\infty$ 는 명시 벡터), 따라서 $b|_W=0$. 국소체에서 $|W|^2=|H|$ 이므로 $W=W^\perp$ **라그랑지안**(최대 등방)이고 $\varepsilon$ 은 쌍곡형(Arf 불변량 0)이다. 홀수 좋은 환원 $p$ 에서 $W=H^1_{\rm ur}$ 를 초등적으로 증명했다.
- [증명] (3) 모든 국소체 $\mathbb Q_p$ 에서 $\dim H=2m$, $m=(r-1)+[p=2]$ ($r$=$L_p$ 의 체 인수 수), $|\ker\varepsilon|=2^{2m-1}+2^{m-1}$ — 분해되지 않는 경우도 **항상 쌍곡형** (비등방 불가): 홀수 $p$ 에서 기약 1, (1)(2)형 3, 분해 10; $p=2$ 에서 기약 3, (1)(2)형 10, 분해 36; $\mathbb R$: 3, 1. 부수 결과: $W$ 가 아닌 $W$-잉여류는 $\ker\varepsilon$ 과 정확히 절반씩 만난다.
- [계산 확인] (1) 극형식 = 힐베르트 기호 합: 분해형 $p=2,3,5,7,\infty$, (1)(2)형 $p=3,5,7,11$ 에서 쌍 수백 개 불일치 0. 국소 수 (3) 표와 일치 ($p=2,3,5,7,23,\infty$). (4) 기약 삼차식 3개: $t^3-2$ (Sel$_2$=1, 핵 교집합 2), $t^3+t^2-2t-1$ (Sel$_2$=2, 핵 교집합 3, 위수 무한 점 $(-1,1)$ 이 Sel 원소를 생성), $t^3-t-1$ (Sel$_2$=1, 핵 교집합 3). **핵의 교집합 $\ne$ Selmer** 임을 구체 사례로 확인.

## 본문

### 0. 설정과 표기
$k$ 표수 $\ne2$, $f=t^3+a_1t^2+a_2t+a_3$ 제곱무인수, $L=k[\theta]$, $N=N_{L/k}$. $\lambda_0=-2/f'(\theta)$, $Q_\delta(x)=\mathrm{Tr}_{L/k}(\lambda_0\delta x^2)$ ($x\in L$, 3변수). $H=\ker(N:L^\times/L^{\times2}\to k^\times/k^{\times2})$ ($=H^1(k,E_f[2])$, R2 증명; 정확한 정의는 이 핵이며 $(L^\times/\square)_{N=1}$ 과 같다). $\mathrm{Br}_2:=\mathrm{Br}(k)[2]$; 국소체에서 $\mathrm{Br}_2=\{\pm1\}$ 이고 곱셈 표기, 일반체에서는 가법 표기.

**보조사실 F0** [증명]. $[L:k]=3$ 이 홀수이므로 $N(\mathrm{res}\,a)=a^3\equiv a$. 따라서 $N$ 은 전사이고 $L^\times/\square=\mathrm{res}(k^\times/\square)\oplus H$ (직합), $\dim H=\dim L^\times/\square-\dim k^\times/\square$.

**보조사실 F1** [증명]. 모든 $\delta\in H$ 에 대해 $\det Q_\delta\equiv2$ (제곱류). 이유: 기저 $1,\theta,\theta^2$ 에서 $\det\mathrm{Tr}(c\theta^{i+j})=N(c)\,\mathrm{disc}(f)$ (R2). $c=\lambda_0\delta$: $N(\lambda_0)=-8/N(f'(\theta))$, $N(f'(\theta))=-\mathrm{disc}(f)$ (삼차: $\mathrm{disc}=(-1)^{3}N(f')$) 이므로 $N(\lambda_0)\equiv 2\,\mathrm{disc}(f)$, $N(\delta)\equiv1$, 곧 $\det\equiv2\,\mathrm{disc}(f)^2\equiv2$.

**정의.** $\varepsilon(\delta):=s(Q_\delta)-s(Q_1)\in\mathrm{Br}_2$ ($s$=하세–비트 불변량 $\prod_{i<j}(a_i,a_j)$). 이는 $e_2(Q_\delta-Q_1)$ 와 같다: 두 형식의 차원·행렬식이 같으므로 $s(Q\perp -Q')$ 의 보정항들이 모두 $(\dim,\det)$ 의 함수여서 상쇄되기 때문 [증명 스케치]. $Q_{\delta u^2}\cong Q_\delta$ 이므로 $\varepsilon$ 은 류 $\delta\in H$ 의 함수. 국소체에서 (차원, 행렬식, 하세 불변량)이 3변수 형식을 결정하므로 $\varepsilon(\delta)=0\iff Q_\delta\cong Q_1\cong q_A$ ⟺ 궤도가 존재(R2 정리 A) 이다.

### 1. $\varepsilon$ 은 이차함수, 극형식은 힐베르트–베유 쌍

**정리 1** [증명(분해형), 증명(일반형: 아래 두 증명, 각각 표준 사실 하나에 의존)]. $\delta,\delta'\in H$ 에 대해
$$b(\delta,\delta'):=\varepsilon(\delta\delta')-\varepsilon(\delta)-\varepsilon(\delta')=\mathrm{Cor}_{L/k}\big((\delta,\delta')_L\big)\in\mathrm{Br}_2 .$$
특히 $\varepsilon(1)=0$, $b$ 는 쌍가법·대칭·**교대**($b(\delta,\delta)=0$)이므로 $\varepsilon$ 은 $\mathbb F_2$-벡터공간 $H$ 위의 이차함수(Br$_2$-값)이고 극형식이 $b$ 이다. $L=\prod F_i$ 이면 $b=\sum_i\mathrm{Cor}_{F_i/k}(\delta_i,\delta_i')_{F_i}$; 국소체에서는 $\prod_i(\delta_i,\delta_i')_{F_i}$ (각 $F_i$ 의 힐베르트 기호).

*증명 (a) 분해형 $L=k^3$, 임의 체* [증명, 자기완결]. $Q_\delta=\langle c_1\delta_1,c_2\delta_2,c_3\delta_3\rangle$, $c_i=-2/f'(\theta_i)$. 가법 표기로 $\varepsilon(\delta)=\sum_{i<j}[(c_i,c_j)+(c_i,\delta_j)+(\delta_i,c_j)+(\delta_i,\delta_j)]-s(Q_1)=\sum_{i<j}(\delta_i,\delta_j)+(\text{$\delta$ 에 대해 선형})$. 이차 부분의 극형식은 $\sum_{i\ne j}(\delta_i,\delta_j')=(\prod\delta_i,\prod\delta'_j)+\sum_i(\delta_i,\delta_i')$, 그런데 $\prod\delta_i\in\square$ 이므로 첫 항은 0. 따라서 $b=\sum_i(\delta_i,\delta_i')$. 교대성: $\sum(\delta_i,\delta_i)=\sum(\delta_i,-1)=(\prod\delta_i,-1)=0$. ∎(a)

*증명 (b) 일반형, 방법 I (비트환과 전이)* [증명, 단 ★ 는 기억-미검증]. $s_*:W(L)\to W(k)$ 를 범함수 $s(x)=\mathrm{Tr}(\lambda_0x)$ 로 만든 샤를라우 전이라 하면 $Q_\delta=s_*\langle\delta\rangle$. $W(L)$ 에서 $\langle\delta\delta'\rangle-\langle\delta\rangle-\langle\delta'\rangle+\langle1\rangle=(\langle\delta\rangle-\langle1\rangle)(\langle\delta'\rangle-\langle1\rangle)=\langle\langle\delta,\delta'\rangle\rangle$ (2-폴리스터 형식, $I^2(L)$). $s_*$ 가법이므로 $Q_{\delta\delta'}-Q_\delta-Q_{\delta'}+Q_1=s_*\langle\langle\delta,\delta'\rangle\rangle$, 그리고 $e_2\langle\langle a,b\rangle\rangle=(a,b)$. ★ **$e_2\circ s_*=\mathrm{Cor}_{L/k}\circ e_2$ on $I^2(L)$** (전이와 여대사영의 호환; $s=\mathrm{Tr}(\lambda_0\cdot)$ 의 $\lambda_0$ 는 상관없다: $(\langle\lambda_0\rangle-1)\varphi\in I^3$ 이고 $s_*(I^3)\subset I^3$ 이므로 $e_2$ 에서 사라진다). ∎(b-I)

*증명 (b) 방법 II ($Q_8$ 중심확대)* [증명 구상, ★★ 는 기억-미검증]. $\mathrm{Stab}_{SO(A)}(N)\cong E[2]$ (R2) 를 $\mathrm{Spin}(A)=SL_2$-형 군으로 올리면 중심확대 $1\to\mu_2\to\tilde E\to E[2]\to1$ 이고 $\tilde E\supset Q_8$ (클라인 4군 $\{\mathrm{diag}(\pm1)\}$ 의 $\mathrm{Spin}_3$ 속 원상), 군 확대의 교환자 쌍은 $E[2]$ 위 비퇴화 교대쌍, 제곱사상은 $x\mapsto\tilde x^2\in\mu_2$. 연결사상 $\partial:H^1(k,E[2])\to H^2(k,\mu_2)$ 는 상쌍곱 계산으로 $\partial(x+y)=\partial x+\partial y+(x\cup_{\rm comm}y)$ (코사이클 $\tilde x_\sigma\tilde y_\sigma$ 의 재배열에서 교환자가 컵곱으로 나온다). ★★ $\partial_A:H^1(k,SO(A))\to H^2(k,\mu_2)$ 가 하세–비트 불변량의 차 $s(\cdot)-s(q_A)$ 와 같다 (Serre). 그러면 $\varepsilon=\partial$ 이고 $b=$ 컵곱($E[2]$ 의 교환자 쌍). ∎(b-II)

*일반형에서 분해형으로의 환원(보조)* [증명]. $L$ 이 체이면 $[L:k]=3$ 이 홀수여서 $\mathrm{Res}:\mathrm{Br}_2(k)\to\mathrm{Br}_2(L)$ 이 단사 ($\mathrm{Cor}\circ\mathrm{Res}=3$). $L\otimes_kL=L\times K'$ ($K'$=L 위 이차 étale) 이므로 정리 1 은 $L=k\times K$ 형만 보이면 충분하다. 이 형은 $K$ 가 분해되면 (a) 와 같고, 분해되지 않을 때만 이차체의 전이–여대사영 호환 (★ 의 $[K:k]=2$ 경우)이 필요하다.

**정리 2 (b 는 베유 쌍의 컵곱)** [증명]. $E[2]\hookrightarrow R_{L/k}\mu_2$ 를 $\{\epsilon\in\{\pm1\}^3:\prod\epsilon_i=1\}$ 로 두면 $E[2]$ 위 갈루아 불변 비퇴화 교대쌍은 **유일** ($\mathbb F_2^2$ 위 비영 교대쌍은 하나뿐)하므로 베유 쌍 $e_2$ = 내적 $\sum x_iy_i|_{\text{합이 0}}$. 내적 쌍 $R\mu_2\otimes R\mu_2\to R\mu_2\xrightarrow{\ \rm Cor\ }\mu_2$ 에서 시반레 보조정리(Shapiro)로 $H^1(k,R\mu_2)=L^\times/\square$ 위 컵곱이 $\mathrm{Cor}_{L/k}(\delta\cup\delta')=b$ 이다. ∎

**정리 3 (국소 완전성)** [증명; 표준 사실: 국소체 $F$ 의 힐베르트 기호가 $F^\times/\square$ 위 완전, $(a,\beta)_F=(a,N_{F/k}\beta)_k$ ($a\in k$) ★★★ 기억-미검증이지만 표준]. $k$ 가 국소체이면 $b$ 는 $H$ 위 **비퇴화**.
증명: $P(\delta,\delta')=\sum_i(\delta_i,\delta'_i)_{F_i}$ 는 $L^\times/\square=\bigoplus F_i^\times/\square$ 위 완전 쌍. 사영 공식으로 $P(\mathrm{res}\,a,\delta)=(a,N\delta)_k$ 이므로 $H=(\mathrm{res}\,k^\times/\square)^\perp$. 완전 쌍에서 $H^\perp=\mathrm{res}(k^\times/\square)$, 그리고 $H\cap\mathrm{res}(k^\times/\square)=0$ (F0). 따라서 $b=P|_H$ 의 근기는 0. ∎

**수치 확인 (극형식)** [계산 확인; 코드 `r3_polar.py`]. $\varepsilon$ 를 하세 불변량으로 직접 계산하고(3×3 Gram 의 대각화) $b$ 를 힐베르트 기호 합과 비교:
- 분해형: $t^3-4t$ ($p=2,3,5,\infty$ 각 200쌍), 근 $(1,2,-3)$ ($p=3,5,7,\infty$ 각 150), 근 $(0,1,3)$ ($p=2,3,5,\infty$ 각 150): **불일치 0**.
- (1)(2)형 $L=\mathbb Q\times K$ (홀수 $p$, $K$ 의 힐베르트 기호는 길들인 기호로 계산): $t^3-3t$ ($K=\mathbb Q(\sqrt3)$, $p=3,5,7$), $t(t^2-2)$ ($p=3,5$), $(t-1)(t^2+1)$ ($K=\mathbb Q(i)$, $p=3,7,11$) 각 300쌍: **불일치 0**.
- 모든 유형 ($p=2,3,5,7,23,\infty$; 분해·(1)(2)·기약)에서 $b$ 의 쌍선형성 $b(\delta,\delta'\delta'')=b(\delta,\delta')b(\delta,\delta'')$, 대칭성, 교대성 위반 0 (각 150~300 삼중).
(이는 정리의 확인이지 근거는 아니다.)

### 2. 쿠머상은 라그랑지안 (푸엔-레인스 구조)

$W:=\mathrm{im}\big(E(k)/2E(k)\hookrightarrow H\big)$, $\delta(P)=2(t_0-\theta)$ ($P=(t_0,w_0)$, $w^2=2f(t)$), $\delta(O)=1$ (R2: 단사 준동형).

**정리 4 (W 는 전등방)** [증명]. 모든 $P\in E(k)$ 에서 $Q_{\delta(P)}$ 는 등방 벡터를 가지며, 행렬식이 $2$ 인 3변수 등방형식은 $\langle1,-1,-2\rangle$ 으로 결정되므로 $Q_{\delta(P)}\cong Q_1$, 곧 $\varepsilon(\delta(P))=0$ ($Q_1$ 도 등방). 등방 벡터:
- $t_0\notin\{\theta_i\}$ 인 점: $x=1$ (R2). $Q(1)=-4\,\mathrm{Tr}\big((t_0-\theta)/f'\big)=-4[\theta^2](t_0-\theta)=0$.
- 꼬임점 $T_1$ ($\theta_1\in k$): 성분 $\delta=(2f'(\theta_1);\,2(\theta_1-\theta_2),\,2(\theta_1-\theta_3))$. $d_j=\theta_1-\theta_j$ 라 하면 $Q/(-4)=x_1^2+(x_3^2-x_2^2)/(d_3-d_2)$ (대입 정리). 벡터 $x=(1;\ (1+d_3-d_2)/2,\ -(d_3-d_2-1)/2)$ 가 영을 준다. 이 벡터는 근 $\theta_2\leftrightarrow\theta_3$ 교환에 대해 갈루아 불변이므로 $L=k\times K$ 일 때도 $k$-유리 벡터이다.
- $O$: $\delta=1$.
모든 점이 위 셋 중 하나이므로 증명 끝. 따름: $W$ 는 부분공간이므로 $b(w,w')=\varepsilon(w+w')-\varepsilon(w)-\varepsilon(w')=0$, 곧 $b|_W=0$. ∎

**정리 5 (최대 등방 = 라그랑지안)** [증명; 지수 공식 ★★★★ 는 표준이나 기억-미검증]. $k$ 가 $\mathbb R$ 이거나 $p$-진체($[k:\mathbb Q_p]=n$, $L=\prod_{i=1}^rF_i$) 이면 $\dim H=2m$, $\dim W=m$, $m=(r-1)+n[p=2]$, $W=W^\perp$, $\varepsilon$ 은 쌍곡형.
증명: (i) $\dim H$: $\dim F^\times/\square=2+n_F[p=2]$ ($p$-진 $F$), 합 $\sum n_{F_i}=3n$ 이므로 $\dim L^\times/\square=2r+3n[p=2]$, F0 에 의해 $\dim H=2r+3n[p=2]-2-n[p=2]=2(r-1)+2n[p=2]$. (ii) $\dim W$: 지수 공식 $|E(k)/2E(k)|=|E[2](k)|\cdot|2|_k^{-1}$ ($E(k)$ 의 열린 부분군 $\cong(\mathcal O_k,+)$ 에서 오고 $|E[2](k)|=2^{r-1}$) 으로 $|W|=2^{r-1}\cdot 2^{n[p=2]}$; 그래서 $|W|^2=|H|$. (iii) 정리 4: $b|_W=0$ 이고 정리 3: $b$ 비퇴화이므로 $W\subset W^\perp$, $\dim W^\perp=\dim H-\dim W=m=\dim W$, 곧 $W=W^\perp$. (iv) $\varepsilon|_W=0$ 인 $m$ 차원 부분공간을 가진 비퇴화 이차공간은 쌍곡(= $m$ 개 쌍곡평면의 합)이다. $\mathbb R$: 3 실근이면 $\dim H=2$, $E(\mathbb R)/2E(\mathbb R)=\mathbb Z/2$ ($m=1$); 1 실근이면 $H=0$. ∎

**정리 6 (좋은 환원에서 W = 비분기)** [증명]. $p$ 홀수, $p\nmid\mathrm{disc}(f)$ ($E$ 좋은 환원). $L_p=\prod F_i$ 모두 비분기, 균일화원소 $p$. $H^1_{\rm ur}=\{\delta: \text{모든 성분의 값매김이 짝수}\}$. 단위류는 성분당 $\mathbb Z/2$ (비제곱 단위의 노름은 비제곱) 이고 $N=1$ 조건 한 개 ⇒ $\dim H_{\rm ur}=r-1=m$. $P=(t_0,w_0)$: $\sum_iv_i(t_0-\theta_i)=v(2f(t_0))=2v(w_0)$ 가 짝수이고 $\theta_i\not\equiv\theta_j$ 이므로 한 $i$ 만 $v_i>0$ 일 수 있고(그러면 $v_i=2v(w_0)$ 짝수) $t_0$ 가 비정수이면 $v_i=v(t_0)$ 가 모두 같고 $3v(t_0)$ 가 짝수 ⇒ 각각 짝수. 꼬임점도 같다. 따라서 $W\subset H_{\rm ur}$, 차원이 같아 $W=H_{\rm ur}$. 따름: 이 $p$ 에서 정수 $M$ 의 $\mathbb Z_p$-궤도 ↔ $W$, 그리고 $\varepsilon|_{H_{\rm ur}}=0$ 이 대각화(단위 계수)에서 직접 보인다. ∎

**수치 확인 (정리 4·5)** [계산 확인; `r3_ex4.py`] 쿠머상 표본($t_0\in\mathbb Q$ 격자, 헨젤 해상도 충분)에서 $(|H|,|W|)$ 와 $\varepsilon|_W$, $b|_W$:

| $f$ | $p$ | $\lvert H\rvert$ | $\lvert W\rvert$ | $\varepsilon\vert_W$ | $b\vert_W$ |
|---|---|---|---|---|---|
| $t^3-4t$ (분해) | 3 | 16 | 4 | 0 | 0 |
| 〃 | 5 | 16 | 4 | 0 | 0 |
| 〃 | 2 | 64 | 8 | 0 | 0 |
| 〃 | $\infty$ | 4 | 2 | 0 | 0 |
| $t^3-3t$ ((1)(2)) | 7 / 3 / 2 | 4 / 4 / 4 | 2 / 2 / 2 | 0 | 0 |
| $t^3-t-1$ ((1)(2), 23 은 판별식) | 23 | 4 | 2 | 0 | 0 |
| $t^3-2$ (기약) | 7 / 2 | 1 / 4 | 1 / 2 | 0 | 0 |
| $t^3+t+1$ (비분기 기약) | 2 | 4 | 2 | 0 | 0 |
| $t^3-t-1$ (실근 1) | $\infty$ | 1 | 1 | 0 | 0 |

$|W|=|H|^{1/2}$ 가 전부 성립. (표본 크기가 이론값을 넘지 않으므로 표본이 이론 크기에 도달하면 확정.)

### 3. 분해되지 않는 경우의 국소 수 (임무 3)

**정리 7** [증명(정리 5 로부터)]. $p$-진체 $k$ 에서 $f$ 제곱무인수, $r$=$L$ 의 체 인수 수. 그러면
$$\dim H=2m,\quad m=r-1+n[p=2],\qquad |\ker\varepsilon|=2^{2m-1}+2^{m-1},$$
$\varepsilon$ 은 항상 **쌍곡형 (Arf 0)**. 즉 $L$ 이 체이든 $k\times K$ 이든 비등방형(아르프 불변량 1)은 일어나지 않는다. $SO(A)(k)$-궤도 수 $=|\ker\varepsilon|$ (R2).

| 유형 ($L_p$) | $E[2](k)$ | $p$ 홀수: $m$, $\lvert H\rvert$, $\lvert W\rvert$, $\lvert\ker\varepsilon\rvert$ | $k=\mathbb Q_2$: $m$, $\lvert H\rvert$, $\lvert W\rvert$, $\lvert\ker\varepsilon\rvert$ | $\mathbb R$ |
|---|---|---|---|---|
| 분해 $k^3$ ($r=3$) | $(\mathbb Z/2)^2$ | 2, 16, 4, 10 | 3, 64, 8, 36 | 3 실근: $m=1$, 4, 2, 3 |
| 1차 × 이차체 ($r=2$) | $\mathbb Z/2$ | 1, 4, 2, **3** | 2, 16, 4, **10** | $\mathbb R\times\mathbb C$ (=기약 1 실근 유형): $H=0$ |
| 기약 ($r=1$) | 0 | 0, 1, 1, **1** | 1, 4, 2, **3** | 1 실근: $m=0$, 1, 1, 1 |

[계산 확인; `r3_batch.py` `r3_exp2.py`] 하세 불변량을 직접 계산한 $H$ 의 류 수(서명 분리)와 핵: $t^3-4t$: $p=3,5$ → 16, 10; $p=2$ → 64, 36; $p=\infty$ → 4, 3. $t^3-3t$ ((1)(2)): $p=3,5,7$ → 4, 3; $p=2$ → 16, 10. $t^3-2$: $p=3,7$ → 1, 1; $p=5$ ((1)(2)) → 4, 3; $p=2$ (분기 기약) → 4, 3. $t^3+t+1$: $p=5$ → 1, 1; $p=3$ ((1)(2)) → 4, 3; $p=2$ (비분기 기약) → 4, 3. $t^3-t-1$: $p=23$ → 4, 3; $p=3,\infty$ → 1, 1. $t^3+t^2-2t-1$: $p=7$ → 1, 1; $p=\infty$ (실근 3) → 4, 3. 이론값과 전부 일치.
- 홀수 $p$ 에서 기약 → $H=0$: $|\ker\varepsilon|=1$ — 곧 $p$-진적으로 $\det$ 이 기약인 $K_3$-행렬은 $O(A)(\mathbb Q_p)$-동치류가 단 하나. 홀수 $p$, 1차×이차: 3 개 중 2 개가 쿠머상($E(\mathbb Q_p)/2E(\mathbb Q_p)=\mathbb Z/2$), 1 개는 $\ker\varepsilon\setminus W$.

**따름 8 (핵의 잉여류 구조)** [증명]. $w\in W$, $\delta\in H$: $\varepsilon(\delta+w)=\varepsilon(\delta)+b(\delta,w)$ (정리 4). $\delta\notin W=W^\perp$ 이면 $b(\delta,\cdot)|_W\ne0$ 이므로 잉여류 $\delta+W$ 의 정확히 절반 ($2^{m-1}$ 개)이 $\ker\varepsilon$ 에 든다. $W$ 자체는 전부. 합산: $2^m+(2^m-1)2^{m-1}=2^{2m-1}+2^{m-1}$ ✓. 따라서 이중 정리 7 의 개수 공식을 개수만으로 재증명한다.
해석 [추측, 정합적]: $H/W\cong H^1(k,E)[2]$ 의 각 비자명 원소 $T$ 위의 2-피복들 중 절반은 $M$ 으로 실현되는 사차식 $u^2=f_M(a,b)$ 의 2-피복이다. 이는 사차식 $u^2=g(a,b)$ 가 이미 차수 2 인 사영사상 $(a:b)$ 를 가져 지표가 $2$ 로 나뉘는 것과 일치한다. $\ker\varepsilon\setminus W$ 에 속하는 $M$ 은 "국소 점이 없는 사차식"에 대응한다.

**전역 구조 (푸엔-레인스 틀)**. 전역체 $\mathbb Q$ 에서 $\delta\in H(\mathbb Q)$ 면 $\varepsilon(\delta)\in\mathrm{Br}_2(\mathbb Q)$ 이고 상반성 $\sum_v\mathrm{inv}_v=0$ 으로 $\sum_v\varepsilon_v(\delta)=0$ [증명]. 좋은 홀수 $p$ 에서 $\varepsilon_p|_{H_{\rm ur}}=0$ (정리 6) 이므로 $q:=\sum_v\varepsilon_v$ 는 제한 곱 $\prod'H_v$ 위의 이차형식이고 $H(\mathbb Q)$ 는 그 전등방 부분공간이며 $\prod W_v$ 도 전등방 (정리 4). Selmer $=H(\mathbb Q)\cap\prod W_v$ — 두 라그랑지안의 교집합이라는 푸엔-레인스의 구조 [기억-미검증: 전역 쪽이 최대 등방이라는 것은 인용]. **여기서 $W_v\subsetneq\ker\varepsilon_v$** 이므로 G-행렬의 "모든 곳에서 궤도 존재" ($\bigcap_v\ker\varepsilon_v$) 는 Selmer 보다 일반적으로 크다 (아래 4절 구체 사례).

### 4. 기약 삼차식 곡선의 2-Selmer 군 시험 (임무 4)

**방법.** $E_f:w^2=2f(t)\cong Y^2=X^3+2a_1X^2+4a_2X+8a_3$ ($X=2t,Y=2w$). $L=\mathbb Q[\theta]$ 의 유수 1 ($|{\rm disc}|$ 가 작아 민코프스키 한계 $<2$ + 2 위의 소아이디얼 주아이디얼) 임을 확인한 체만 사용했다 [증명]. $S$=$\{2\}\cup\{p\mid\mathrm{disc}(f)\}$, $L(S,2)$=⟨−1, 단위군 생성원, $S$ 위 소아이디얼의 생성원⟩ (유수 1 이므로 $L(S,2)=\{\text{$S$-단위}\}/\square$). $H(S)=\ker(N:L(S,2)\to\mathbb Q^\times/\square)$ 를 선형대수로 구한 뒤 각 $\delta\in H(S)$ 에 대해
- $\varepsilon_v(\delta)$ ($v\in S\cup\{\infty\}$): 3×3 Gram 의 하세 불변량,
- $\delta\in W_v$ 여부: $W_v$ 를 $t_0\in\mathbb Q$ 격자 ($2f(t_0)\in\mathbb Q_v^{\times2}$) 의 쿠머상 표본으로 얻고, **류 비교는 $b$-서명(정리 3: $b$ 비퇴화이므로 유한 시험 원소들과의 $b$ 값이 류를 결정)** 으로 했다. $|W_v|$ 가 이론값 $2^m$ 에 도달함을 매번 확인 (아래 표).
Selmer $=\{\delta\in H(S):\delta\in W_v\ \forall v\in S\cup\{\infty\}\}$; G-행렬 쪽 비교량 $\mathrm{Orb}:=\{\delta\in H(S):\varepsilon_v(\delta)=0\ \forall v\}$ (모든 장소에서 국소 궤도 존재).

**결과** [계산 확인; 코드 `r3_glob.py`].

| 곡선 | $E:Y^2=\dots$ | $S$ | $L(S,2)$ 생성원 | $\lvert H(S)\rvert$ | $\lvert\mathrm{Orb}\rvert$ | $\lvert\mathrm{Sel}_2\rvert$ | $\lvert W_v\rvert$ (이론과 일치) |
|---|---|---|---|---|---|---|---|
| (a) $f=t^3-2$ | $X^3-16$ | 2,3 | $-1,\theta,\theta-1,\theta+1$ | 2 | 2 | **1** | $\infty$:1, 2:2, 3:1 |
| (b) $f=t^3+t^2-2t-1$ | $X^3+2X^2-8X-8$ | 2,7 | $-1,\theta,\theta+1,2,\theta-2$ | 4 | 3 | **2** | $\infty$:2, 2:2, 7:1 |
| (c) $f=t^3-t-1$ | $X^3-4X-8$ | 2,23 | $-1,\theta,2,\pi_1,\pi_2$ | 4 | 3 | **1** | $\infty$:1, 2:2, 23:2 |

($\pi_1=-6+6\theta-\theta^2$, $\pi_2=-4-5\theta-3\theta^2$: 노름 $\pm23$ 인 서로 비동반 원소 — 23 은 $P^2Q$ 로 분해.)

- **(a)** 후보 $\{1,\theta-1\}$. $\theta-1$ ( $\mathbb Q(\sqrt[3]2)$ 의 기본단위의 역 ) 은 모든 곳에서 $\varepsilon_v=0$ (궤도 존재) 이지만 $p=2$ 에서 $\notin W_2$ ⇒ $\mathrm{Sel}_2=0$ (랭크 0, $Ш[2]=0$, 단위군 가정 하에). **G-행렬 쪽에는 궤도가 2 개, Selmer 는 1 개.**
- **(b)** 3 실근. $\mathrm{Sel}_2=\{1,-(\theta+1)\}$. $E(\mathbb Q)[2]=0$ 이므로 $\dim\mathrm{Sel}_2=1=$ 랭크 $+\dim Ш[2]$. 점 $P=(X,Y)=(-1,1)$ ($t_0=-1/2$, $2f(t_0)=1/4$) 이 곡선 위에 있고 $2P=(81/4,757/8)$ 가 비정수 ⇒ 나겔–루츠로 위수 무한 [증명]. 쿠머상 $\delta(P)=-1-2\theta$ 와 $-(\theta+1)$ 의 비 $(1+2\theta)/(1+\theta)$ 가 $L$ 에서 제곱임을 $R(X^2)$ 의 삼차 인수 존재로 확인 [계산 확인] ⇒ $\delta(P)$ 가 Selmer 의 비자명 원소. 따라서 **랭크 1, $Ш[2]=0$**. 원소 $\theta$ 는 $\varepsilon_v=0$ ($\forall v$) 인데 $W_\infty,W_2$ 에 없음 ⇒ 궤도는 있으나 Selmer 아님; 원소 $-\theta(\theta+1)$ 등은 $\varepsilon_\infty=\varepsilon_2=1$ (이로써 $\sum\varepsilon_v=0$ 상반성을 보인다).
- **(c)** $\mathrm{Orb}=\{1,\ \theta,\ -\theta\pi_1\pi_2\}$ (3 개) 이지만 $\mathrm{Sel}_2=\{1\}$: $\theta\notin W_2$, $-\theta\pi_1\pi_2\notin W_{23}$ (이 원소는 $W_\infty,W_2$ 에는 든다). 원소 $(1,0,0,1,1)=-\pi_1\pi_2$ 는 $\varepsilon_2=\varepsilon_{23}=1$ 로 상반성 확인.
- **일치 판정**: 세 곡선 모두 **Selmer $\ne$ 핵 교집합**, 그리고 Selmer $\subset$ 핵 교집합. G-행렬 언어에서 Selmer 를 얻으려면 "궤도 존재($\varepsilon_v=0$)"에 더해 "사차식 $u^2=f_M(a,b)$ 가 모든 곳에서 국소 가해"(≡ 원뿔 $\{e^TAe=0\}$ 위에서 $e^TMe$ 가 제곱이 되는 벡터의 존재, $\delta_v\in W_v$)가 필요하다. 이는 R2 의 정정 (뒤 절반은 그대로는 거짓) 과 일치하며 이제 이유가 정리 5·따름 8 로 설명된다: $\ker\varepsilon_v$ 는 $W_v$ 의 $2^{m}$ 배보다 큰 이차곡면, $W_v$ 는 그 속의 라그랑지안.

**한계(정직)**.
1. $L(S,2)$ 의 완전성은 (i) 유수 1 (증명됨), (ii) 단위군 생성원이 전체라는 가정 위에 있다. (a) 단위 $\theta-1$, (b) $\theta,\theta+1$ (레귤레이터 $\det\begin{pmatrix}\log1.247&\log0.445\\\log2.247&\log0.555\end{pmatrix}\approx0.5256$ 가 $\mathbb Q(\zeta_7)^+$ 의 알려진 값과 일치), (c) $\theta$ (플라스틱수, 레귤레이터 $\log1.3247\approx0.281$) 은 **기억-미검증**의 알려진 값과 일치하는 점검이다. 따라서 $|\mathrm{Sel}_2|$ 는 "이 가정 하의 정확한 값"이고, (b) 의 하한(랭크 $\ge1$, 점 제시)은 가정 없이 증명됨.
2. $W_v$ 판정은 쿠머상 표본이 이론 크기 $2^m$ 에 도달할 때만 확정으로 썼다(전부 도달). 정수 $M$ 의 구성($M(\delta)$)은 이번에 하지 않았다: 여기서의 G-행렬 쪽 판정은 이론(정리 A: 궤도 ↔ $\ker\varepsilon$)에 의존하며 개별 $M$ 을 만들어 사차식을 푼 것은 아니다.
3. 곡선 3개, 소수 $\le23$ 만 시험. 비효율적이라 $Ш$ 가 있는 예·큰 클래스수 체는 시험하지 못했다.
4. 샘플링 시행착오: 초기 표본 추출기가 희귀 류(한 성분에서만 $p$ 로 나뉘는 원소)를 놓쳐 류 수가 과소 계산되었다. 인수-지향 표본(인수 모듈로 $p$ 가 나누는 원소 포함)으로 고쳐 이론값과 일치시켰다. 즉 류 수 계산은 근거가 아니라 정리 7 의 확인용이다.

## 후속연구 지점
1. **일반형 정리 1 의 완전한 증명 (우선순위 최상)**. 무엇을: ★ ($e_2\circ s_*=\mathrm{Cor}\circ e_2$ on $I^2$, 이차체 전이의 경우) 또는 ★★ ($\partial_A$ = 하세–비트 차) 를 직접 증명. 왜: 일반 $L$ 에서의 유일한 기억 의존 고리. 시작 방법: $K=k(\sqrt D)$, $\mathrm{Tr}_{K/k}\langle c\rangle=\langle \mathrm{Tr}\,c,\ \mathrm{Tr}\,c\cdot DN(c)\rangle$ (계산해 둠: Gram $2\begin{pmatrix}u&vD\\vD&uD\end{pmatrix}$) 를 이용해 $\varphi=\langle\langle\beta,\beta'\rangle\rangle$ 에 대해 직접 하세 불변량을 계산하고 $\mathrm{Cor}_{K/k}(\beta,\beta')$ ($=$ 노름 사상으로 쓴 사원수 대수의 여대사영 공식)와 비교. 난점: $\mathrm{Tr}\,c=0$ 인 경우와 곱 $\beta\beta'$ 의 트레이스 처리.
2. **$M(\delta)$ 의 구성과 정수 구조**. 무엇을: $\delta\in\ker\varepsilon_v\setminus W_v$ 에 대응하는 $M$ 이 주는 사차식이 정확히 "국소 점이 없는 사차식" 임을 보이고(따름 8 의 해석), $\ker\varepsilon\setminus W$ 의 절반 잉여류 구조를 사차식의 degree-2 약수류 선택과 일치시킴. 왜: G-행렬 언어에서 Selmer 의 추가 조건을 군표현 불변량으로 번역. 시작: $E(\mathbb Q_p)$ 의 $p$-진 구조로 $\delta$ 를 직접 $M$ 에 대응시켜 $f_M$ 의 국소 가해성을 판정 (이번엔 하지 않음). 난점: 등거리사상 탐색의 병목(R2 와 동일), $p=2$ 에서 $\det A=2$.
3. **푸엔-레인스 전역 부분의 정리화**: $H(\mathbb Q)$ 가 $\prod'(H_v,\varepsilon_v)$ 에서 최대 등방임을 $K_3$ 틀에서 증명하고 Sel$_2$ 의 차원 홀짝(랭크 홀짝 예측, $Ш$ 홀짝 평균)과 연결. 왜: 라그랑지안 교집합의 차원 홀짝 정리(두 라그랑지안의 교집합 차원 홀짝 불변)를 G-행렬 불변량으로 읽을 수 있는지. 시작: 이번에 얻은 $\varepsilon_v$ 의 표(정리 7)를 모든 $v\in S\cup\infty$ 에 넣고 $\dim(\mathrm{Sel}_2)$ 홀짝을 위상(Arf) 정보로 계산. 난점: 전역 최대 등방성(Poitou–Tate)의 기억 의존.
4. **큰 예 · 비자명 Ш**: 유수 > 1 인 3차체(예: 판별식 $-199$, $-283$ 등 $h>1$) 에서 $L(S,2)$ 를 구하고 $\mathrm{Orb}$ 와 Sel$_2$ 크기 비교, $Ш[2]\ne0$ 인 곡선에서 $\mathrm{Orb}\supsetneq\mathrm{Sel}_2$ 의 여분이 어떻게 나뉘는지. 난점: 류군·단위군 계산 도구 부재(수론 패키지 없음).
5. **$K_4$ 와의 연결**: 4-피복에서 $\varepsilon$ 의 대응물(예: $H^1(k,E[4])$ 위의 이차형식 또는 카셀스–테이트 쌍)이 $\det A_4=-3$ 에서 어떻게 나타나는지. R3-researcher2 의 $K_4$ 궤도 수 불일치(원인 규명)와 합쳐 볼 것. 난점: 이차형식이 아닌 사차 불변량.
