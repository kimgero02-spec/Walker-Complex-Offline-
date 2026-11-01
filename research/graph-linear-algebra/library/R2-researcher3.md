# [R2-researcher3] $\mathbb Q_p,\mathbb R,\mathbb Q$ 위의 $K_3$-행렬 궤도: ker$(H^1(E[2])\to H^1(SO_3))$, 2-Selmer 비교, 난점 해석 도구인가

- 작성자: researcher3 · 라운드: R2 · 역할: 연구원(포메이션 I 분담, 추측 2 담당)
- 코드: `rooms/researcher3/` (`lib.py` 국소 가해성·힐베르트 기호, `descent.py` 쿠머상·핵, `gsel.py` Selmer·$M(\delta)$ 구성, `final.py` `box.py` `cons.py` 상자 열거, `scan.py`, `loc2.py`)

## 요약
- 추측 2 의 앞 절반(궤도 ↔ $\ker(H^1(k,E[2])\to H^1(k,SO_3))$)을 **임의의 체 $k$ (표수 $\ne2$) 에서 증명**했다 [증명]. $H^1(k,SO_3)$ 는 "행렬식 2 인 삼변수 이차형식의 동형류"이고 $\mathbb Q_p$ 에서 하세 불변량 $\mathbb Z/2$, $\mathbb R$ 에서 부호 $(1,2)$/$(3,0)$ 이다. 사상은 $\delta\mapsto \mathrm{Tr}_{L/k}(-2\delta x^2/f'(\theta))$ 의 등방성 여부로 명시된다.
- 뒤 절반은 **그대로는 거짓**이다: 모든 장소에서 핵에 드는 클래스(=$\mathbb Q$-궤도)는 무한히 많고, Selmer 는 그중 "사차식 $u^2=f_M(a,b)$ 가 모든 곳에서 국소 가해"인 유한 부분집합이다. 쿠머상 $\subset$ 핵은 증명했다(점 $x_0$ 이면 $x=1$ 이 원뿔 위의 점). 분할 $f$ 에서 핵 지시함수 $\varepsilon$ 는 Tate 쌍 $\sum_i(\delta_i,\delta_i')$ 의 이차 정제이고 쿠머상은 그 위에서 0 인 라그랑지안이라는 Poonen–Rains 꼴 구조가 나온다 [증명(분할)].
- 구체 시험 [계산 확인]: $y^2=x^3-x$ 에서 직접 2-하강 $|\mathrm{Sel}_2|=4$ 이고, 정수 $M$ 상자 $|m_{ij}|\le5$ 의 30 개가 $\mathbb Q$-궤도 6 개를 이루며 사차식이 국소 가해인 4 개가 정확히 $\mathrm{Sel}_2$. 계수 1 곡선 $y^2=X(X-2)(X+4)$ 에서 $\dim\mathrm{Sel}_2=3$, 위수 무한 점 $(9/4,15/8)$ 와 꼬임점이 8 클래스를 모두 생성. 단 **정수 $M$ 은 2-진적으로 일부 클래스만 만난다**($\det A=2$ 라 $p=2$ 는 $SO(A)$ 의 나쁜 소수).
- 판정: Selmer 계산의 어려운 단계(원뿔 풀기, $L(S,2)$ 계산, 최소화·축소, 4-하강)는 **번역일 뿐 더 쉬워지지 않는다** (원뿔 풀기는 $M$ 찾기로 자리만 옮김). 얻는 것은 균일한 군표현 틀(BG 식 기하수론의 도구)과 "쿠머상 $\subset$ 핵" 의 짧은 증명 정도. $K_3$ 고유 부분은 정수 구조·$S_3$ 뿐이며 새로운 정리는 없다.

## 본문

### 0. 설정과 표기
$A=J-I$, $q_A(x)=2(xy+yz+zx)$, $\det A=2$. $k$: 표수 $\ne2$ 인 체. $f=t^3+a_1t^2+a_2t+a_3\in k[t]$ 제곱무인수, $L=k[t]/(f)=k[\theta]$ (3차 étale 대수), $E=E_f:\ w^2=2f(t)$. $X=2t,\ Y=2w$ 로 $Y^2=X^3+2a_1X^2+4a_2X+8a_3=8f(X/2)$, 즉 $E_f\cong\{Y^2=\prod(X-2\theta_i)\}$ (뒤틀림 없음; 오케스트레이터가 $\mathrm{Jac}(u^2=f_M)\cong\{w^2=\det(tA-M)\}$ 를 점 개수로 확인한 것을 전제).
$V_f=\{M\in\mathrm{Sym}_3:\ \det(tA-M)=2f(t)\}$. $N:=A^{-1}M$ 은 $q_A$ 에 대해 자기수반이고 $\mathrm{charpoly}(N)=f$.
**작용의 번역** [증명]: $PAP^T=A$ 이면 $A^{-1}PA=P^{-T}$ 이므로 $A^{-1}(PMP^T)=Q\,N\,Q^{-1}$, $Q:=P^{-T}$, 그리고 $Q^TAQ=A$ 이다. 즉 $O(A)$ 의 $M$ 위 작용은 $O(q_A)$ 가 자기수반 연산자 $N$ 에 하는 켤레작용과 같다 (BG 의 설정).

### 1. 지역(일반 체) 이론

**정리 A** (표수 $\ne2$, $f$ 제곱무인수) [증명]
1. (기점) $M_0(f)=\begin{pmatrix}0&1&0\\1&2(a_1+a_2+a_3+1)&a_2+2a_3\\0&a_2+2a_3&2a_3\end{pmatrix}\in V_f(k)$ (6 변수 아닌 3 변수 다항식 항등식 $\det(tA-M_0)=2f$, sympy 기호 확인 [계산 확인]; 정수 계수이므로 $V_f(\mathbb Z)\ne\emptyset$). 쿠스탄트 단면에 해당. 따라서 $V_f(k)\neq\emptyset$.
2. ($\bar k$ 위 이행성) $N\in V_f(\bar k)$ 는 서로 다른 고윳값 $\theta_i$ 를 가지므로 고유벡터 $v_i$ 는 $q_A$ 에 대해 서로 직교하고 $q_A(v_i)\ne0$ ($A$ 비퇴화). 정규화한 직교기저는 $O(q_A)(\bar k)$ 가 이행적으로 움직이고, $N$ 은 (기저, 고윳값) 으로 결정되므로 $V_f(\bar k)$ 는 하나의 $O$-궤도. $O=SO\times\{\pm1\}$ (차원 3, 홀수) 이고 $-I$ 는 $M\mapsto PMP^T$ 에 자명하게 작용하므로 **$O(A)(k)$-궤도 = $SO(A)(k)$-궤도**이며 $SO$ 도 $\bar k$ 에서 이행적.
3. (안정자군) $N$ 이 정칙이므로 중심화자 $=k[N]\cong L$. $Q\in k[N]$ 이 직교이려면 $Q^{*}=Q$ ($N$ 자기수반이므로 $N$ 의 다항식도 자기수반) 이므로 $Q^2=1$. 따라서 $\mathrm{Stab}_O=\{\varepsilon\in L:\varepsilon^2=1\}=R_{L/k}\mu_2$, $\det Q=N_{L/k}(\varepsilon)$ 이고
$$\mathrm{Stab}_{SO}(N)=\ker\big(N_{L/k}:R_{L/k}\mu_2\to\mu_2\big)\cong E_f[2].$$
(마지막 동형: 근 $2\theta_i$ 에 대응하는 꼬임점 $T_i\leftrightarrow\varepsilon$ 로 $\varepsilon_i=+1$, 나머지 $-1$. 차수 3 이 홀수여서 $R\mu_2=\mu_2\times\ker N$ 으로 갈라진다.)
4. (스킴 수준) 궤도사상 $SO(A)/\mathrm{Stab}\to V_f$ 는 동형이다: $\bar k$ 에서 직교기저로 $q=\sum x_i^2$, $N=\mathrm{diag}(\lambda_i)$ 로 잡으면 $T_NV_f=\{\text{대칭 }\delta N,\ \text{대각성분}=0\}$ (특성다항식의 미분은 $\delta\lambda_i=\delta N_{ii}$ 이고 $\lambda_i$ 가 서로 다르므로 3 개 계수가 독립), 궤도의 접공간 $\{[X,N]:X\ \text{반대칭}\}$ 도 같은 3 차원 공간. 전단사 + 접공간 동형 ⇒ 동형.
5. (코호몰로지) Serre, *Galois Cohomology* I.5.4 [기억-미검증, 표준] 에 의해, 기점 $M_0$ 를 고르면
$$SO(A)(k)\backslash V_f(k)\ \xleftrightarrow{\ 1:1\ }\ \ker\big(H^1(k,E_f[2])\to H^1(k,SO(A))\big).$$
∎

**$H^1$ 의 명시.**
- $H^1(k,E[2])=\ker\big(N:L^\times/L^{\times2}\to k^\times/k^{\times2}\big)$ [증명: $R\mu_2=\mu_2\times E[2]$ 의 분해와 Shapiro·Kummer].
- $H^1(k,SO(A))$: $H^1(k,O(q))$ = 같은 차원 이차형식의 동형류 (Serre III.1.2 [기억-미검증]); $O=SO\times\mu_2$ 이므로 $H^1(k,SO(A))$ = **행렬식이 $\det A=2$ (제곱류) 인 삼변수 형식의 동형류** [증명]. $k=\mathbb Q_p$: 하세 불변량 $\pm1$ (두 값 모두 3 변수에서 실현) ⇒ $\mathbb Z/2$ (기점 $=[q_A]$) [확인됨]. $k=\mathbb R$: $\det>0$ 이면 부호 $(3,0),(1,2)$ ⇒ $\mathbb Z/2$ (기점 $q_A$ 는 $(1,2)$). $k=\mathbb F_q$: 한 점 (Lang 과 일치). $k=\mathbb Q$: 하세–민코프스키 ⇒ $H^1(\mathbb Q,SO_3)\hookrightarrow\prod_vH^1(\mathbb Q_v,SO_3)$.
- 사상 $\delta\mapsto[\,\mathrm{Tr}_{L/k}(\lambda_0\delta x^2)\,]$, $\lambda_0=-2/f'(\theta)$ [증명]. 이유: $e\in V$ 가 순환벡터이면 $L\to V,\ g(\theta)\mapsto g(N)e$ 가 동형이고 $q_A(g(N)e,h(N)e)=\ell(gh)$, $\ell(g)=e^TAg(N)e=\mathrm{Tr}(\mu g)$. 오일러 항등식 $\mathrm{Tr}_{L/k}(g/f')=[\theta^2]\,(g\bmod f)$ 때문에 $\lambda_0=-2/f'$ 인 형식은 $\mathrm{Tr}(-2x^2/f')=-2[\theta^2](x^2)$ 로 **등방적**(벡터 $x=1$)이고 행렬식이 $2$ 이므로 $q_A$ 와 동형 (등방적 삼변수 형식은 행렬식으로 결정). 따라서 $M\mapsto\delta(M):=\mu/\lambda_0$ 가 위 1:1 대응을 준다.
  분할 $f$ ($L=k^3$) 에서는 더 간단히 [증명, 위와 같은 논증]: $\delta_i(M)\equiv-2\,q_A(v_i)\,f'(\theta_i)$ ($v_i$ = $\theta_iA-M$ 의 핵벡터). 핵 조건 ⇔ 대각형식 $\langle-2\delta_i/f'(\theta_i)\rangle$ 가 $k$ 위에서 등방적 ⇔ 힐베르트 기호 $(-ac,-bc)=1$.
- **따름 B** [증명]: $\delta(M)=0$ (기점 궤도) $\iff$ 사차식 $f_M(a,b)$ 가 $k$ 에서 근을 갖는다. ($\Rightarrow$: $f_{M_0}(1,0)=m_{11}=0$. $\Leftarrow$: 근 $(a:b)$ 에서 $e=P(a,b)$ 는 $q_A(e)=e^TMe=0$, 즉 $\ell(1)=\ell(\theta)=0$. 이때 $e$ 는 자동으로 순환적(고유성분 $c_i$ 중 하나나 둘만 0 이면 $\ell(1)=\ell(\theta)=0$ 이 $c_i^2q_i\ne0$ 과 모순)이고 $\ell(\theta^2)=:c\in k^\times$ 에서 $\mu=c/f'$, $\delta=-2c$. $N(\delta)=-8c^3$ 이 제곱이어야 하므로 $-2c\in k^{\times2}$ ⇒ $\delta=0$.) 고전의 "근을 가진 사차식 = $E$ 자신의 2-피복" 과 일치.

**정리 C** (사차식과 고전 구성의 일치) [증명 스케치 + 계산 확인]. $\delta=\delta(M)$ 의 고전 2-피복(캐셀스 구성) $\{\delta x^2=z(t-\theta)\}$ 를 쓰면: 조건 "$\theta^2$ 계수 $=0$" 은 $-\tfrac12\,\mathrm{Tr}(\lambda_0\delta x^2)\!\cdot\!(\ldots)=q_A(x)=0$ 이라는 **같은 원뿔**이고, $\delta x^2=c_0+c_1\theta$ 일 때 $u^2=-2c_1$ 은 $\theta$ 를 곱한 뒤의 $\theta^2$ 계수 $=x^TMx$ 이다. 즉 고전 2-피복 $=\{q_A(x)=0,\ u^2=x^TMx\}=C_M$, 이를 $P(a,b)$ 로 매개화한 것이 $u^2=f_M(a,b)$. 결론: $C_M(k)\ne\emptyset \iff \delta(M)\in\mathrm{Im}(E(k)/2E(k)\to H^1)$.
검증 [계산 확인]: 분할 $f$ 6 개($\theta=(0,2,-2),(0,1,3),(0,-1,4),(1,2,-3),(0,3,-5),(0,1,-1)$), 상자 $|m_{ij}|\le4$ 의 모든 $M$ 에 대해 $v\in\{\infty,2,3,5,S\}$ 에서 "사차식 국소 가해 $\Leftrightarrow\delta(M)\in\mathrm{Im}_v$" (쿠머상은 점 표본으로 생성, 크기가 기대값과 일치할 때 확정) 가 420 쌍 모두 성립. (이것은 위 증명의 항등식에 대한 점검이지 통계 증거가 아니다.)

### 2. 좋은 환원 소수와 $\mathbb Z_p$ 궤도 → $\mathbb F_p$ 궤도
$p$ 홀수, $p\nmid\mathrm{disc}(f)$ 이면 $SO(A)$ ($\det A=2$ 가 단위) 와 $V_f$ 는 $\mathbb Z_p$ 위 매끄럽다(위 정리 A.4 의 접공간 논증이 $\mathbb Z_p$ 위에서도 성립) [증명 구상]. 그러면:
(i) $V_f(\mathbb Z_p)\to V_f(\mathbb F_p)$ 전사 (헨젤). (ii) 환원이 $SO(\mathbb F_p)$ 로 켤레인 두 $M,M'$ 은 $SO(\mathbb Z_p)$ 켤레로 환원이 같다고 가정할 수 있고 (군의 매끄러움), 이때 이동자 스킴 $\mathrm{Tr}(M,M')$ 는 유한 étale 군 $\mathrm{Stab}(M)$ 의 토르소이며 $\mathbb F_p$-점(항등원)을 가지므로 $\mathbb Z_p$-점을 갖는다. 그러므로
$$SO(\mathbb Z_p)\backslash V_f(\mathbb Z_p)\cong SO(\mathbb F_p)\backslash V_f(\mathbb F_p)\cong H^1(\mathbb F_p,E[2])=E[2]/(\mathrm{Frob}-1),$$
크기 $|E[2](\mathbb F_p)|$ (마지막은 Lang: $H^1(\mathbb F_p,SO)=0$ — **추측 1 의 증명과 같은 논증**; 이는 researcher1 담당). 또 $H^1(\mathbb F_p,E[2])\hookrightarrow H^1(\mathbb Q_p,E[2])$ (불분기 부분) 이 쿠머상과 같으므로 [기억-미검증: 좋은 환원 홀수 $p$ 에서 $\mathrm{Im}=H^1_{\rm ur}$], **$\mathbb Z_p$-궤도 ↔ 불분기 클래스**: 서로 $\mathbb Q_p$ 켤레인 두 정수 $M$ 은 $\mathbb Z_p$ 켤레이다.
**그러나 $\mathbb Q_p$ 궤도는 더 많다** [계산 확인, 분할 $f=t^3-4t$]: 홀수 좋은 $p$ 에서 $|H^1|=16$, 핵(=$\mathbb Q_p$-궤도 수) $=10$, 쿠머상 $=$ 불분기 $=4$. 나머지 6 개 핵 클래스는 분기하는 클래스이며 $\mathbb Z_p$ 점으로 안 잡힌다.
**$p=2$**: $\det A=2$ 이므로 $SO(A)$ 가 $\mathbb Z_2$ 위 좋은 환원이 아니다. 이 논증은 적용 불가 (§4 관찰 참조).

**실수체** [증명]: 3 개의 실근 $\theta_1<\theta_2<\theta_3$ 이면 $\delta\in(\pm1)^3$, 곱 $+$, $|H^1|=4$. $\lambda_i=-2\delta_i/f'(\theta_i)$ 이고 $\mathrm{sgn}f'(\theta_i)=(+,-,+)$ 이므로 부호 $(1,2)$ 인 것은 $\delta=(+++),(+--),(--+)$ 세 개, $(-+-)$ 는 $(3,0)$. 핵 $=3$ (= $M$ 의 실 궤도 수; 고유벡터의 $q_A$ 부호가 정확히 하나만 $+$ 인 3 가지) — 계산과 일치. 쿠머상은 크기 2 ($E(\mathbb R)/2E(\mathbb R)=\mathbb Z/2$). 실근 1 개이면 $E[2]\cong\mathbb Z/2[\mathrm{Gal}]$ (유도가군) 이라 $H^1=0$, 궤도 1 개 ($\mathrm{Tr}_{\mathbb C/\mathbb R}$ 가 부호 $(1,1)$ 이라 자동으로 $(1,2)$).

### 3. 핵의 구조: 이차형식과 라그랑지안 (분할 $f$)
힐베르트 기호의 쌍선형성으로, $\lambda_i=c_i\delta_i$ 일 때 지시함수 $\varepsilon(\delta):=h(\mathrm{diag}\ \lambda)\,h(q_A)$ ($h$=하세 불변량) 는 $\varepsilon(\delta)=\sum_{i<j}(\delta_i,\delta_j)+(\text{선형})$ (가법 표기) 인 **이차함수**이다 [증명]. 그 극형식은 $\sum_{i\ne j}(\delta_i,\delta'_j)=\sum_i(\delta_i,\delta_i')$ ($\prod\delta'_j$ 가 제곱이므로) — 곧 국소 Tate 쌍 $\sum_i(\delta_i,\delta_i')$ [증명(분할); "이것이 $E[2]$ 의 Weil·cup 쌍과 같다" 는 [기억-미검증]].
쿠머상 위에서 $\varepsilon\equiv0$ [증명]: $P=(t_0,w_0)$ 에 대해 $\delta=2(t_0-\theta)$ 이고 $x=1$ 이 $\mathrm{Tr}(\lambda_0\delta x^2)=-4\mathrm{Tr}((t_0-\theta)/f')=-4[\theta^2](t_0-\theta)=0$ 을 준다. (꼬임점은 $E(\mathbb Q_v)$ 에서 인근 점의 클래스와 같으므로 마찬가지.)
**결론** (Poonen–Rains 꼴 [기억-미검증]): $H^1(\mathbb Q_v,E[2])$ 는 이차공간 $(H^1,\varepsilon)$ 이고 쿠머상은 (Tate 쌍의 라그랑지안이므로 [기억-미검증]) 그 안의 $\varepsilon$-전등방 부분공간, **핵 $=\{\varepsilon=0\}$**. $\dim H^1=2m$ 이면 라그랑지안이 있으므로 영점 수는 $2^{2m-1}+2^{m-1}$.
[계산 확인] 표 ($f=t^3-4t$): 

| $v$ | $\dim H^1$ | $\lvert H^1\rvert$ | 핵 | 쿠머상 | $2^{2m-1}+2^{m-1}$ |
|---|---|---|---|---|---|
| $\infty$ | 2 | 4 | 3 | 2 | 3 |
| 2 | 6 | 64 | 36 | 8 | 36 |
| 3, 5 | 4 | 16 | 10 | 4 | 10 |

따라서 (오케스트레이터의 추측 2 의 정정) **국소 궤도 수 $=\lvert\ker\rvert=2^{2m-1}+2^{m-1}$ 이지 $\lvert H^1\rvert/2$ 가 아니다.**

### 4. 구체 곡선과 2-Selmer 비교
**방법.** (a) 직접 2-하강: $\theta_i\in\mathbb Z$ 인 분할 $f$; $S=\{2\}\cup\{p\mid\mathrm{disc}\}$; 후보 $\delta=(d_1,d_2,d_3)$, $d_i\in\langle-1,S\rangle$, $\prod d_i\in\square$. 쿠머상 $\mathrm{Im}_v$ ($v\in S\cup\{\infty\}$) 는 $t=a/b$ ($|a|<120,\ b<40$) 의 점 $\{2f(t)\in\mathbb Q_v^{\times2}\}$ 와 꼬임점의 $\delta=(2(t-\theta_i))_i$ 로 생성하고, **생성된 부분군의 크기가 알려진 크기 ($\infty$: 2, 홀수 $p$: 4, $p=2$: 8) 와 일치**함을 확인했다 (§3 표). Selmer $=\{\delta:\delta\in\mathrm{Im}_v\ \forall v\in S\cup\infty\}$ (불분기 조건은 $S$ 밖에서 자동) — 이 계산은 행렬 $M$ 과 무관하다. (b) 행렬쪽: $V_f(\mathbb Z)$ 를 상자 $|m_{ij}|\le B$ 에서 전부 열거(numpy, 3 개 방정식 선별), 각 $M$ 의 $\mathbb Q$-궤도 불변량 $\delta(M)$ (§1) 로 분류, 사차식 $f_M$ 의 국소 가해성은 `solv_quartic` (원시 $(a,b)\bmod p^k$ 트리탐색 + $f$ 값의 정사각 판정; 양성 판정은 헨젤로 엄밀, 음성은 모든 가지가 결정적으로 음일 때만; 미결정이면 `None`) 와 실수(실근/부호) 로 판정.

**곡선 1: $f=t^3-4t$, $\theta=(0,2,-2)$, $E_f\cong y^2=x^3-x$** ($X=2t$, 척도 2).
- 직접 2-하강: $S=\{2\}$, $|\mathrm{Sel}_2|=4$, $\mathrm{Sel}_2=\{(1,1,1),(1,2,2),(-1,-1,1),(-1,-2,2)\}$ [계산 확인]. 기억: $E(\mathbb Q)\cong(\mathbb Z/2)^2$, 랭크 0, Sha 자명 ⇒ $|E(\mathbb Q)/2E|=4$ [기억-미검증] 와 일치.
- 행렬쪽 ($B=5$): $V_f(\mathbb Z)$ 에 30 개 $M$, $\mathbb Q$-궤도 6 개 (모두 전역 핵에 속함, 즉 모든 장소에서 $\varepsilon=0$): $\delta=(1,1,1)$ [6 M], $(1,2,2)$ [6], $(-1,-1,1)$ [6], $(-1,-2,2)$ [3] 은 $\infty,2$ 에서 가해 ⇒ 정확히 $\mathrm{Sel}_2$ 4 개; $(-1,1,-1)$ [6], $(-1,2,-2)$ [3] 은 $\infty$ 와 $2$ 모두에서 비가해 ⇒ Selmer 아님. 대표: $M=\begin{pmatrix}0&-2&0\\-2&0&2\\0&2&0\end{pmatrix}$, $f_M=4ab(a-b)(a+b)$ (근을 가짐 ⇒ 따름 B 로 자명 클래스 ✓).
- 전역 핵: $S$-단위 후보 16 개 중 12 개가 모든 장소에서 $\varepsilon=0$ (곧 12 개의 $\mathbb Q$-궤도 클래스가 있고 이 중 4 개만 Selmer). 일반적으로 $S$ 밖에서 분기하는 클래스까지 포함하면 $\mathbb Q$-궤도는 **무한히** 많다.
- 유리 (정수 아닌) $M$ 구성 `M_from_delta` (등거리사상 탐색): 핵의 12 개 중 7 개에 대해 성공, 모두 $\delta(M)=\delta$ 재확인; $(2,1,2),(2,2,1)$ 은 2 에서 비가해, $(-1,\cdot,\cdot)$ 중 둘은 $\infty$·2 에서 비가해. 나머지 5 개는 탐색 한계(작은 벡터)로 실패 — 존재는 이론(하세)이 보장.

**곡선 2 (랭크 1): $\theta=(0,1,-2)$, $f=t^3+t^2-2t$, $E_f\cong y^2=X(X-2)(X+4)$.**
- 점 $P=(9/4,\ 15/8)$: $\frac94\cdot\frac14\cdot\frac{25}4=\frac{225}{64}$ ✓. $X$ 가 정수가 아니므로 Nagell–Lutz (정수 계수 모델) 로 위수 무한 [증명, 표준 정리].
- $S=\{2,3\}$, $|\mathrm{Sel}_2|=8$. 꼬임점 3 개 + $P$ 의 클래스가 생성하는 부분군이 **정확히 8 개 = $\mathrm{Sel}_2$**. $\dim\mathrm{Sel}_2\ge2+\mathrm{rank}\ge3$ 이므로 랭크 $=1$, $E(\mathbb Q)/2E=\mathrm{Sel}_2$ (Sha[2]=0) [증명; 이 두 곡선에서 `Sel_2` 계산이 옳다는 조건하에]. ($\theta=(0,m,n)$, $1\le m\le8$, $-9\le n\le-1$ 72 개를 훑었을 때, 작은 탐색으로 비정수 $X$ 점이 발견되는 것과 $\dim\mathrm{Sel}_2\ge3$ 이 어긋난 적은 없었다: 부수적 점검일 뿐.)
- 8 개 클래스 모두에 대해 사차식이 $\infty,2,3$ 에서 가해인 **유리 $M$** 을 구성했다 [계산 확인] (예: $\delta=(1,2,2)$: $M=\begin{pmatrix}1/4&-1/2&-5/4\\-1/2&1&5/2\\-5/4&5/2&9/4\end{pmatrix}$; $(-2,-2,1)$: $\begin{pmatrix}33/16&-1/4&33/16\\-1/4&1&-1/4\\33/16&-1/4&33/16\end{pmatrix}$; $(2,6,3)$ 는 분모 100, $(-1,-6,6)$ 은 분모 4). 즉 **$\mathrm{Sel}_2\ni\delta\Rightarrow$ 모든 곳에서 가해인 $\mathbb Q$-궤도가 존재** (하세 + 정리 A) — 8/8.
- 정수 $M$ ($B=10$): 45 개 $M$, $\mathbb Q$-궤도 5 개; 가해 4 개 $(1,1,1),(-2,-1,2),(-1,-3,3),(2,3,6)\in\mathrm{Sel}_2$, 비가해 1 개 $(-2,3,-6)$ ($\infty,2,3$ 모두 비가해). $B=6$ 과 $B=10$ 의 궤도 집합은 같다.
- **관찰 (정수 구조의 한계)** [계산 확인, $B\le10$, 곡선 4 개: $\theta=(0,1,-2),(0,2,-2),(0,1,3),(0,-1,4)$]: 정수 $M$ 이 만나는 **2-진 클래스는 36 개 핵 클래스 중 4~6 개**뿐이고 쿠머상 8 개 중에서도 2~4 개만 닿는다. 이 때문에 위 8 개 중 4 개는 정수 $M$ 으로 안 잡힌다 (분모 $2^k$ 필요). 해석 [추측]: $\det A=2$ 라서 $p=2$ 에서 $SO(A)$ 가 나쁜 군이다. BG 는 행렬식 $\pm1$ 형식을 쓴다 [기억-미검증]. 따라서 $K_3$ 의 $A=J-I$ 의 $\mathbb Z$-구조는 Selmer 를 정수 궤도로 실현하는 "올바른 정수 구조"가 아닌 것으로 보이며, 이는 증명이 아닌 상자 한계 안의 관찰이다.

**한계.** 분할 $f$ (완전한 유리 2-꼬임) 만 시험; 기약 3 차식(체 $L$ 의 류군·단위군 필요)은 하지 않았다. $B\le10$. 점 탐색은 작은 높이. Sel 계산에서 불분기 조건이 $S$ 밖에서 자동이라는 것은 표준 사실로 사용 [기억-미검증].

### 5. 판정: 난점을 해석하는 도구인가

**(i) 고전 이론의 어려운 단계.** 2-하강의 실제 병목은 다음이다. (a) $L(S,2)$ 의 계산 (3 차체의 류군·단위군) — 비분할 $f$ 에서의 진짜 난점. (b) $\delta$ 가 주어졌을 때 2-피복 $C_\delta$ 를 **쓰는 것**: $\mathrm{Tr}(\delta x^2/f')$ 의 원뿔 위 유리점을 찾아야 한다 (등방성 판정은 하세 불변량이면 되지만 점 찾기가 필요). (c) 사차식의 최소화·축소 (점 탐색이 가능하도록). (d) 4-하강(Cassels–Tate 쌍, 4-피복).

**(ii) $G$-행렬의 말로 쉬워지는가.**
- (b) **번역일 뿐** [증명]. 고전 구성의 원뿔이 정확히 $q_A=0$ 이고 ($P(a,b)$ 가 이미 풀린 매개화), 고전 사차식이 $f_M$ 이다 (정리 C). 이 좌표계에서 원뿔 풀이는 사라진 것이 아니라 **$M(\delta)$ 를 찾는 단계로 이동**했다: $M(\delta)$ 는 $(L,\mathrm{Tr}(\lambda_0\delta x^2))\cong(\mathbb Q^3,q_A)$ 인 등거리사상이 필요하고 그것이 같은 원뿔점 찾기다. 실제로 내 구현에서도 이 탐색이 병목(곡선 1 에서 5 개 실패)이었다.
- (a) 영향 없음. $L^\times/\square$ 는 $A$ 와 무관한 대수.
- (c) $O(A)(\mathbb Q)\cong$ (본질적으로) $PGL_2(\mathbb Q)$ 가 $f_M$ 에 $GL_2$-변수변환으로 작용하므로 "$G$-소거 동치"는 **이진 사차식의 $GL_2$-동치**이고, $M\bmod A\leftrightarrow f_M$ ($\mathrm{Sym}^2(V_3)=1\oplus V_5$, 임의의 $SO_3\cong PGL_2$ 에서 성립) 이므로 축소 이론은 고전 것(Cremona 의 사차식 축소) 그대로다. 새 불변량 없음. 정수 $M$ 의 크기가 사차식 계수의 크기를 제어하는 것은 사실이지만 2-진 문제(§4 관찰)가 따라붙는다.
- (d) $K_3$ (3×3) 쌍 $(A,M)$ 은 **2-피복**(이진 사차식)에 대응한다. 오케스트레이터가 본 $K_4$ 쌍 (4×4, $\{x^TAx=x^TMx=0\}\subset\mathbb P^3$) 은 4 차 곡선, 즉 **4-피복의 표준 모델**이고 이진 사차식 $\det(tA-M)$ 가 그 아래 2-피복이다 [기억-미검증: Merriman–Siksek–Smart, Cremona–Fisher–Stoll]. 따라서 4-하강의 난점이 $K_4$ 에 있을 법하나, 고정된 $A=J-I$ (판별식 $-3$) 는 쌍의 연필에서 특정 원소를 고르는 제약이고 4-하강에서는 연필 전체에 $GL_2$ 도 작용시키는 것이 표준이다. $K_4$ 의 이 해석은 이번 라운드에서 시험하지 않았다 [추측].
- **얻는 것**: (1) 균일한 군표현 틀: 하나의 군 $SO(A)$ 와 공변량 공간에 모든 $E$ 의 2-피복이 함께 들어간다 (BG 가 평균 Selmer 크기 계산에 쓴 기하수론 틀 [기억-미검증]; 개별 곡선 계산과는 다른 용도). (2) 쿠머상 $\subset$ 핵의 한 줄 증명($x=1$) 과 $\varepsilon$ 이차형식 구조의 자연스러운 설명. (3) 정수 기점 $M_0(f)$ 가 다항식으로 명시됨.
- **판정**: "단지 번역" (4 개 단계 중 3 개) + 약간의 구조적 설명. Selmer 군 계산을 쉽게 하지 않는다. 전역 후보를 고르는 쪽 정보($L(S,2)$)는 번역하지 못한다. 이 대응은 새롭다고 주장하지 않는다 (고전 2-하강 = BG 의 $g=1$ 경우).

**$K_3$ 고유 vs 임의 비퇴화 $A$ 에서 성립.**
- 임의의 비퇴화 삼변수 $A$ (표수 $\ne2$) 에서 성립 [증명]: 정리 A.2–A.5 (이행성, 안정자군 $\cong$ 꼬인 $E[2]$ 형, 궤도 ↔ 핵), $H^1(SO)$ 의 이차형식 해석. (기점의 존재는 $q_A$ 등방성 필요; $K_3$ 에서는 $M_0$ 로 명시. 비등방 $A$ 는 $V_f(k)=\emptyset$ 일 수 있음 [추측].) 정리 C 의 구성도 $A$ 불문.
- $K_3$ 고유: (α) $\det A=2$: $E_f:w^2=2f$, 정수성에서 $p=2$ 가 나쁨 (§4 관찰); (β) $S_3\subset O(A)(\mathbb Z)$ 는 $\{0,-1,\infty\}$ 순열이며 $\mathbb Q$-궤도 집합에 **자명하게 작용**(같은 궤도)하므로 열거의 중복도($\le6$)만 설명한다. $S_3$-불변 $M=xI+yJ$ 는 $N=A^{-1}M$ 이 $\mathbf 1^\perp$ 에서 스칼라라 고윳값 중복 ⇒ $\Delta=0$ 이므로 **R1 의 "Aut-등변 행렬(오비탈 대수)" 은 특이 섬유 위에만 산다** [증명]; (γ) 정수 매개화 $P(a,b)$: $m_{11},m_{22},m_{33}=f_M(1,0),f_M(1,-1),f_M(0,1)$ 이고 정수 $M$ 은 $c_1,c_3$ 가 짝수인 사차식만 준다 [증명]; (δ) 레전드르 $\lambda$: $E$ 의 $\lambda$ 는 $t$-직선의 $(\theta_1,\theta_2,\theta_3,\infty)$ 교차비이고 $S_3$ 가 움직이는 $(a:b)$-직선의 세 점 $\{0,-1,\infty\}$ 와 다른 직선이다. 둘의 관계에 대한 결과는 얻지 못했다 [추측: 직접 관계 없음].

## 후속연구 지점
1. **Z-구조 교정**: $p=2$ 에서 정수 $M$ 이 쿠머상을 못 채우는 현상(2~4/8 만 닿음)의 원인 규명. 무엇을: $\det=\pm1$ 인 형식(예: $xz+y^2$ 의 짝)과 $A=J-I$ 의 $\mathbb Z_2$-격자 비교, 어느 정수 구조에서 $V_f(\mathbb Z_2)$ 의 클래스가 쿠머상과 일치하는지. 왜: BG 식 "Selmer = 정수 궤도" 대응이 $K_3$ 에서 성립하는지 결정. 시작 방법: $\mathbb Z_2$ 위 $M\bmod 2^k$ 열거 후 $\delta$ 의 2-진 클래스 수집, 형식 $\mathrm{diag}$ 대신 $H\oplus\langle d\rangle$ 로 같은 시험. 난점: 2-진 군스킴의 비매끄러움.
2. **기약 3 차식 시험**: $L$ 이 3 차체 또는 $\mathbb Q\times$ 이차체인 $f$ (예: $t^3-2t$ 꼴) 에서 같은 비교. 왜: 분할만으로는 Sha·류군 현상이 약하다. 시작: $L=\mathbb Q\times K$ 는 $\mathrm{Tr}_{K/\mathbb Q}$ 이차형식의 Gram $\begin{pmatrix}2\alpha&2\beta D\\2\beta D&2\alpha D\end{pmatrix}$ 로 하세 계산 가능. 난점: 3 차체 $L(S,2)$ 계산(류군).
3. **$\varepsilon$-이차형식의 일반 증명**: 비분할 $f$ 에서 극형식 $=$ Tate 쌍, 쿠머상이 라그랑지안이므로 핵 크기가 $2^{2m-1}+2^{m-1}$ 임을 증명(지금은 분할만 증명, 홀수·$p=2$ 계산 일치). 이어서 오케스트레이터의 추측 1(유한체)과 합쳐 "국소 궤도 수 공식" 정리화. 난점: Weil 쌍과 힐베르트 기호 쌍의 동일시(문헌 [기억-미검증]).
4. **$K_4$ = 4-피복**: $\{x^TAx=x^TMx=0\}$ 의 $A=J-I$ 고정 모델에서 $\mathbb Q_p$-궤도와 $E[4]$ 또는 Cassels–Tate 쌍의 관계. 왜: 이것만이 "난점(4-하강)을 건드릴 여지"가 있는 방향. 시작: $K_4$ 에서 정리 A 에 해당하는 안정자군($\mathrm{Stab}\cong E[2]$?)과 $H^1(SO_4)$ 계산. 난점: $SO_4$ 는 단순군이 아니고 4×4 쌍의 불변량이 사차식이라 $E$ 가 아니라 2-피복이 나옴.
5. **$M$ 과 사차식의 $O(A)(\mathbb Z)$ 정규형**: 정수 궤도에 대해 $S_3$ 까지 고려한 축소 정규형이 고전 Cremona 축소와 어떻게 다른지 (다르지 않다는 것을 증명). 난점: 정수군 $O(A)(\mathbb Z)$ 의 생성원 결정.
