# [R2-researcher2] 정수 이득 규칙의 $A_G$ 구조: 방향 사이클 순환성, Pretzel 정리(절단 뒤집기), 환 위의 표

- 작성자·라운드·역할: researcher2 · R2 · 포메이션 I 분담, 정수 규칙 $R_{a,b}$ 의 $A_G$ 구조 담당
- 코드: `rooms/researcher2/ag.py`(스미스 꼴), `ag2.py`(단일 근 공식), `tab.py`(표), `tree.py`, `theta.py`, `pretzel.py`. 계산은 증명 단계 확인과 표 채우기에만 썼다.

## 요약
1. **방향 사이클** [증명]: $\gcd(a,b)=1$ 이면 $A_{\vec C_n}\cong\mathbb Z/N_n$, $N_w:=a^w-(-b)^w$ (순환성은 $(n-1)$-소행렬 $a^{n-1}$, $b^{n-1}$ 두 개로 증명). $g=\gcd(a,b)>1$ 이면 $A_{\vec C_n}\cong(\mathbb Z/g)^{n-1}\oplus\mathbb Z/(gN'_n)$. 혼합 방향 사이클은 $|\det|=|ab|^{\min(f,r)}|N_{|f-r|}|$ 이고 **원천 수 $s=1$ 일 때만 순환**, $s\ge2$ 이면 $p\mid ab$ 에서 $p$-랭크가 $s$ (비순환). $R=\mathbb Z/m$ 위에서는 $R^{\vec C_n}\cong\mathbb Z/\gcd(N_n,m)$.
2. **Pretzel 정리**: R1 에 적힌 "싱크/소스(정점) 뒤집기" 형태는 **거짓**이다 (반례: 원천·싱크가 하나도 없는 방향 그래프의 다리 뒤집기). 올바른 형태는 **방향 절단(dicut) 뒤집기**이고, 역방향(감김 함수가 같으면 절단 뒤집기로 옮겨짐)을 **증명했다** [증명]. 귀결: $A_G\otimes\mathbb Z[1/ab]$ 와 $\dim F^G$ ($\lambda$ 가 단위인 모든 환)는 방향의 "감김 함수 클래스"만의 함수. 정수 위의 $A_G$ 전체는 그렇지 않다(V 대 역V: $\mathbb Z\oplus\mathbb Z/2$ 대 $\mathbb Z$).
3. **일반 구조** [증명 + 추측]: 연결 성분 $C$ 마다 $A_C\cong[\mathbb Z\ \text{또는}\ \mathbb Z/N_{\omega_C}]\oplus T_a\oplus T_b$. 비틀림의 세 출처: (I) 순환 불균형 $N_\omega$ (소수 $\nmid ab$, 방향 클래스만 의존), (II) 합류 $T_a$ ($p\mid a$, 들어오는 호가 2개 이상인 정점), (III) 분기 $T_b$ ($p\mid b$). $p$-랭크 정리: $p\mid a$ 이면 $\operatorname{rank}_pT_a(C)=\#\text{원천}(C)-[\omega_C=0]$, $p\mid b$ 이면 싱크로 같은 식 [증명].
4. **환 위의 표** ($a=-2,b=1$; $\mathbb Z/4,\mathbb Z/6,\mathbb Z,\mathbb Q$) 16개 그래프를 채웠다(§5). $\mathbb Z/6=\mathbb Z/2\times\mathbb Z/3$ 의 CRT 로 교차 검증([증명]: $\mathbb F_2$ 에서는 $\lambda=0$, $\mathbb F_3$ 에서는 $\lambda=-1$).
5. **판정**: 환 확장은 체의 "0/1 (성분 단위)" 정보를 $v_p(\lambda^{\omega}-1)$, 곧 **감김 gcd $\omega$ 자체**와 합류 구조까지 올린다. 기존 규칙 $a+b=0$ 은 "$\omega$ 가 짝수인가"만 읽는다. $R=\mathbb Q/\mathbb Z$ 를 쓰면 $R^G$ 가 $A_G$ 의 쌍대(완전 불변량)다.

## 본문

### 0. 약속과 준비
- 방향 다중그래프 $G=(V,A)$, 호 $u\to v$ 마다 관계 $a\,x_u+b\,x_v=0$. $A_G=\mathbb Z^V/\langle a\,u+b\,v\rangle$, $R^G=\mathrm{Hom}(A_G,R)$. $\lambda:=-a/b$ (즉 $x_v=\lambda x_u$). 특별히 말하지 않으면 $\gcd(a,b)=1$, $ab\ne0$.
- 성분 $C$ 의 감김 gcd $\omega_C$ (R1 정의), $N_w:=a^w-(-b)^w$ ($w\ge0$, $N_0=0$). $\lambda^w-1=\pm N_w/b^w$ 이므로 $\mathbb Z[1/ab]$ 에서 $(\lambda^w-1)=(N_w)$.
- **보조정리 0** [증명]: (i) $A_G(a,b)=A_G(-a,-b)$. (ii) $A_{G^{op}}(a,b)=A_G(b,a)$ (호를 뒤집으면 관계가 $b\,x_v+a\,x_u$ 로 역할 교환). 따라서 "$p\mid b$" 의 모든 결과는 "$p\mid a$" 결과에 $G^{op}$ 를 대입해서 나온다. (iii) $\gcd(a,b)=g$, $a=ga'$, $b=gb'$ 이면 제약행렬이 $gM'$ 이므로 스미스 꼴이 $g\cdot\mathrm{Smith}(M')$: 불변인자가 전부 $g$ 배.
- 소수 $p$ 에서의 국소화 $A_{(p)}:=A_G\otimes\mathbb Z_{(p)}$. 비틀림의 $p$-준소부분은 $A_{(p)}$ 의 비틀림.

### 1. 방향 사이클의 $A_G$ [증명]

**정리 1.** $\vec C_n$ ($n\ge1$; 호 $i\to i+1 \bmod n$), $\gcd(a,b)=1$ 이면 $A_{\vec C_n}\cong\mathbb Z/N_n$ ($N_n=0$ 이면 $\mathbb Z$, $|N_n|=1$ 이면 0). 일반 $g=\gcd(a,b)$ 이면
$$A_{\vec C_n}\cong(\mathbb Z/g)^{\,n-1}\oplus\mathbb Z/(g\,N'_n),\qquad N'_n=a'^n-(-b')^n$$
($n=1$ 이면 앞 항 없음; $N'_n=0$ 이면 마지막 항이 $\mathbb Z$).

**증명.** 관계 행렬 $M=aI+bP$ ($P$ 순환 이동, 행 $i$ = $a e_i+b e_{i+1}$). 라이프니츠 전개에서 순열 $\mathrm{id}$ 와 $n$-사이클 두 개만 살아남아 $\det M=a^n+(-1)^{n-1}b^n=a^n-(-b)^n=N_n$.
$(n-1)$-소행렬 두 개: (i) 행 $0$, 열 $0$ 을 지우면 행 $i\ (\ge1)$ 이 열 $i$ 에 $a$, 열 $i+1$ 에 $b$ 를 가지는 상삼각 이중대각 행렬 — 행렬식 $a^{n-1}$ (행 $n-1$ 의 $b$ 는 지운 열 $0$ 에 있다). (ii) 행 $n-1$, 열 $0$ 을 지우면 행 $i\ (\le n-2)$ 가 열 $i+1$ 에 $b$, 열 $i$ 에 $a$ ($i\ge1$) 를 가지는 하삼각 행렬 — 행렬식 $b^{n-1}$. 스미스 꼴의 $d_1\cdots d_{n-1}$ 은 $(n-1)$-소행렬들의 gcd 이고 이것은 $\gcd(a^{n-1},b^{n-1})=1$ 의 약수이므로 $d_1=\dots=d_{n-1}=1$, $d_n=|N_n|$. 일반 $g$ 는 보조정리 0(iii) 에 $M'$ 의 결과를 대입. ∎

**환 번역.** $R=\mathbb Z/m$: $\mathrm{Hom}(\mathbb Z/N,\mathbb Z/m)=\mathbb Z/\gcd(N,m)$ 이므로 ($\gcd(a,b)=1$)
$$(\mathbb Z/m)^{\vec C_n}\cong\mathbb Z/\gcd(a^n-(-b)^n,\ m)\quad(m=0\text{ 이면 }N_n=0\text{ 일 때 }\mathbb Z,\text{ 아니면 }0).$$
$g>1$: $(\mathbb Z/\gcd(g,m))^{n-1}\oplus\mathbb Z/\gcd(gN'_n,m)$. 소수 거듭제곱 $m=p^e$, $p\nmid ab$: $\mathbb Z/p^{\min(e,\,v_p(N_n))}$. 체($e=1$)에서는 $p\mid N_n$ 일 때 1차원이므로 R1 정리 2 와 같고, 환에서는 **$v_p(N_n)$ 가 보인다**. 예: $\lambda=2$ ($a=-2,b=1$), $n=6$: $N=63=3^2\cdot7$, $\mathbb Z/9$ 위에서 $\mathbb Z/9$, $\mathbb F_3$ 위에서는 차원 1 [계산 확인: $2^6-1=63$]. ($v_p(2^n-1)=v_p(2^k-1)+v_p(n/k)$, $k=\mathrm{ord}_p2$, 홀수 $p$ — 승수 올리기 보조정리 [기억-미검증].)

**정리 2 (혼합 방향 사이클).** $C_n$ 의 호 중 한 바퀴 방향으로 정방향 $f$ 개, 역방향 $r$ 개 ($f+r=n$), 원천(두 호의 꼬리) $s$ 개 = 싱크 $s$ 개. $\gcd(a,b)=1$.
(i) $\det=a^fb^r-(-1)^na^rb^f$, $|\det|=|ab|^{\min(f,r)}\,|N_{|f-r|}|$. [증명: 행 $i$ = $p_ie_i+q_ie_{i+1}$ 에서 $(p_i,q_i)=(a,b)$ 또는 $(b,a)$; 정리 1 과 같은 전개; $(-1)^n=(-1)^{f-r}$.]
(ii) $p\nmid ab$ 이면 $A_{(p)}$ 는 순환 $\mathbb Z_{(p)}/(N_{|f-r|})$ (정리 5 의 특수 경우).
(iii) $p\mid a$ 이면 $\dim_{\mathbb F_p}A\otimes\mathbb F_p=s$, $p\mid b$ 이면 $s$ (모든 호가 $\bmod p$ 에서 머리=0 또는 꼬리=0 이 됨; 정리 6).
(iv) 따라서 $s=1$ 이면 $A\cong\mathbb Z/(|ab|^{\min(f,r)}N_{|f-r|})$ 순환 ($f=r$ 이면 $\mathbb Z$), $s\ge2$ 이고 $|ab|>1$ 이면 **비순환**.
(v) 단 $\gcd(a,b)=g>1$ 은 보조정리 0(iii) 로 환원.
[계산 확인: $(a,b)\in\{(-2,1),(-3,1),(2,3),(-6,5),(-4,9),(1,1),(-2,-3)\}$, $n\le7$, 모든 $2^n$ 방향에 대해 $\det$ 과 $p=2,3,5$ 의 $p$-랭크 일치. 증명 단계 확인용.] 예: 교대 $C_4$ ($s=2$, $a=-2,b=1$): $A=\mathbb Z\oplus\mathbb Z/2$ 비순환. 추이 삼각형(0→1→2, 0→2; $f=2,r=1,s=1$): $|\det|=2\cdot|N_1|=2\cdot1=2$, $A=\mathbb Z/2$ [계산 확인].
$R=\mathbb Z/m$ 번역: $s=1$ 이면 $\mathbb Z/\gcd(|ab|^{\min}N_{|f-r|},m)$.

### 2. Pretzel 정리 (R1 에서 남은 부분)

**R1 의 두 문장을 분리한다.**
(A) "성분의 기여 = 1 $\iff$ $C$ 가 $\vec C_k$ ($k=\mathrm{ord}\lambda$) 로의 호모를 가진다": **이미 양방향 증명됨** [증명]. ($\Rightarrow$: $s \bmod k$. $\Leftarrow$: 호모는 닫힌 걸음의 감김을 보존하고 $\vec C_k$ 의 닫힌 걸음의 감김은 $k$ 의 배수이므로 $k\mid\omega_C$.) 환 $R$ 에서는 "기여 1"이 "기여 $\mathrm{Ann}_R(\lambda^{\omega}-1)$" 로 바뀐다(정리 4).
(B) R1 [기억-미검증] Pretzel: "두 방향이 싱크/소스 뒤집기로 옮겨짐 $\iff$ 모든 사이클의 감김 일치". 미해결은 ($\Leftarrow$). **아래에서 (B) 가 정점 뒤집기로는 거짓임을 보이고 절단 뒤집기 형태로 증명한다.**

**정리 3 (Pretzel, 절단 뒤집기)** [증명]. $G$ 연결 무방향 다중그래프(루프 허용), $o,o'$ 두 방향. 다음은 동치.
(1) 모든 닫힌 걸음 $W$ 에서 $w_o(W)=w_{o'}(W)$.
(2) $o'$ 는 $o$ 에서 유한 번의 **방향 절단 뒤집기**로 얻어진다. 방향 절단 = 정점 집합 $S$ 로, $\delta(S)$ 의 모든 호가 $S$ 로 들어오거나 모두 $S$ 에서 나가는 경우; 뒤집기 = $\delta(S)$ 의 모든 호를 반대로.
(3) (정점 뒤집기 = $S=\{v\}$ 가 싱크/소스인 경우는 (2) 의 특수한 경우이며, (1)⇒"정점 뒤집기만으로" 는 **거짓**.)

*증명 (2)⇒(1).* 닫힌 걸음은 $S$ 에 들어가는 횟수와 나오는 횟수가 같다. 절단 호가 모두 $S$ 로 향하면, 들어갈 때 $+1$, 나올 때 $-1$ 이고 뒤집으면 반대 부호이므로 변화량은 $-2(\#\text{들어감})+2(\#\text{나옴})=0$.
*증명 (1)⇒(2).* 기준 방향에 대해 호 $e=(u\to v)$ ($o$ 의 방향) 마다 $t(e)=w_o(e)-w_{o'}(e)\in\{0,2\}$ (같으면 0, 다르면 2). (1) 에 의해 $t$ 는 모든 닫힌 걸음에서 합이 0 이므로 $t=\delta(2h)$ 인 함수 $h:V\to\mathbb Z$ 가 있다($h(\text{root})=0$ 에서 경로 따라 적분; 연결이므로 잘 정의): **모든 $o$-호 $u\to v$ 에서 $h(v)-h(u)\in\{0,1\}$ 이고, $=1$ 이면 그 호는 $o'$ 에서 반대 방향.** $h$ 가 상수이면 $o=o'$. 상수가 아니면 $M=\{h=\max h\}$ 로 두자. $M\ne V$ 이고 연결이므로 $\delta(M)$ 은 비어 있지 않다. $M$ 의 정점 $v$ 에서 나가는 호 $v\to u$ 는 $h(u)-h(v)\ge 0$, $h(v)$ 최대이므로 $u\in M$. 따라서 $\delta(M)$ 의 모든 호는 $M$ 으로 **들어오는** 호, 곧 $\delta(M)$ 은 방향 절단이다. 이를 뒤집어 $o_1$ 을 얻는다. $o_1$ 과 $o'$ 에 대한 새 함수는 $h_1=h-\mathbf 1_M$ 이다 (절단 호 $u\to v$, $h(v)-h(u)=1$ 이 $v\to u$ 로 바뀌면 $h_1(u)-h_1(v)=0$, 나머지 호는 불변). $\Phi=\sum_v(h(v)-\min h)$ 가 $|M|\ge1$ 만큼 감소하고 $\min h$ 는 유지($\max h-1\ge\min h$). 유한 번 뒤 $h$ 상수. ∎ [계산 확인: `pretzel.py` 가 무작위 연결 다중그래프 300개에서 절단 뒤집기로 만든 $o'$ 에 대해 이 알고리즘이 정확히 $o'$ 에 도달 — 증명 단계 확인용.]

**정점 뒤집기가 부족한 반례** [증명]. 방향 삼각형 $K=\{k_1\to k_2\to k_3\to k_1\}$ 와 $L=\{l_1\to l_2\to l_3\to l_1\}$ 를 다리 $l_1\to k_1$ 로 이은 $o$. 모든 정점이 들어오는 호와 나가는 호를 모두 가지므로 싱크도 원천도 없고, 정점 뒤집기는 불가능하다. 그러나 다리를 뒤집은 $o'$ 는 다리가 어떤 사이클에도 놓이지 않으므로 모든 감김이 같고, $\delta(K)$ 를 뒤집어 얻는다. 곧 R1 [기억-미검증] 서술은 정정해야 한다.

**$F^G$, $A_G$ 에의 귀결.**
**정리 3′ (스위칭)** [증명]. 방향 절단 $\delta(S)$ (모두 $S$ 로 들어옴)을 뒤집는 것은 $\theta=\lambda^{-2}\mathbf 1_S+\mathbf 1_{V\setminus S}$ 에 의한 스위칭 $x\mapsto\theta x$ 이다(들어오는 호의 새 이득 $\theta(v)\lambda=\lambda^{-1}$, $S$ 내부 호는 $\theta(v)\lambda\theta(u)^{-1}=\lambda$). $\lambda$ 가 단위인 환 $R$ 에서 $R^{G,o}\cong R^{G,o'}$. 정수에서는 $A_G(o)\otimes\mathbb Z[1/ab]\cong A_G(o')\otimes\mathbb Z[1/ab]$.
**따름.** 그러므로 $\dim F^G$ ($\lambda\in F^\times$) 와 $A_G\otimes\mathbb Z[1/ab]$ 는 **감김 함수 $w:H_1(G)\to\mathbb Z$ 만의 함수**, 곧 정리 3 의 동치류의 함수. 반면 $p\mid ab$ 에서는 아니다: V ($0\to2\leftarrow1$) 와 역V ($2\to0,\ 2\to1$) 는 감김 함수가 같은데 ($H_1=0$, 단 서로 절단 뒤집기 동치), $a=-2,b=1$ 에서 $A=\mathbb Z\oplus\mathbb Z/2$ 대 $\mathbb Z$ (뒤집기가 $\theta=\lambda^{-2}$, $\lambda=2$ 가 $\mathbb Z$ 에서 단위가 아니기 때문).

**정리 4 (환 위의 방향 이득 규칙)** [증명]. $R$ 가환환, $\lambda\in R^\times$, 규칙 $x_{\rm head}=\lambda x_{\rm tail}$. 그러면 $R^G\cong\bigoplus_{C}\mathrm{Ann}_R(\lambda^{\omega_C}-1)$. $R=\mathbb Z/m$ 이면 성분 기여는 $\mathbb Z/\gcd(\lambda^{\omega_C}-1,m)$.
*증명.* 성분 하나, 신장 나무 $T$, 근 $r$, 나무 경로의 감김 $s(v)$ 라 하면 $\lambda$ 가 단위이므로 $x_v=\lambda^{s(v)}x_r$ (역방향 호는 $\lambda^{-1}$). 나무 밖 호 $e$ 가 $(\lambda^{c_e}-1)x_r=0$ ($c_e$ = 기본 사이클 감김) 을 준다. $(\lambda^c-1,\lambda^d-1)=(\lambda^d-1,\lambda^{c-d}-1)$ ($\lambda^c-1-\lambda^{c-d}(\lambda^d-1)=\lambda^{c-d}-1$) 이므로 유클리드 호제법으로 아이디얼 $(\lambda^{c_e}-1)_e=(\lambda^{\gcd c_e}-1)=(\lambda^{\omega}-1)$. $\mathrm{Ann}_{\mathbb Z/m}(c)\cong\mathbb Z/\gcd(c,m)$. ∎
$R$ 이 체이면 $\mathrm{Ann}$ 은 $R$ 또는 0: R1 정리 1. 여기서 **성분의 기여가 0/1 에서 "아이디얼 $\mathrm{Ann}(\lambda^\omega-1)$" 로 일반화**되고, 영인자가 있는 환에서만 새 정보가 생긴다.

### 3. 일반 그래프의 $A_G$

**정리 5 ($ab$ 와 서로소인 부분)** [증명]. 임의의 방향 다중그래프, $\gcd(a,b)$ 임의: $A_G\otimes\mathbb Z[1/ab]\cong\bigoplus_C\ \mathbb Z[1/ab]/(N_{\omega_C})$ ($\omega_C=0$ 이면 자유 $\mathbb Z[1/ab]$).
*증명.* $\mathbb Z[1/ab]$ 에서 $a,b$ 는 단위이고 $A\otimes\mathbb Z[1/ab]=(\mathbb Z[1/ab])^G$ 를 대표하는 가군이다(관계가 $x_{\rm head}=\lambda x_{\rm tail}$ 과 동치). 정리 4 의 증명에서 $\mathrm{Hom}$ 대신 직접 $\mathrm{coker}$ 로 읽으면: 나무로 소거하고 남은 관계 $b\,\lambda^{s(v)}(\lambda^{c_e}-1)x_r$ 들. 아이디얼은 $(\lambda^\omega-1)=(N_\omega)$. ∎
- **$\gcd(a,b)=1$ 이면 $N_w$ 는 $ab$ 와 서로소**($p\mid a\Rightarrow N_w\equiv-(-b)^w\not\equiv0$). 따라서 비틀림의 $ab$-서로소 부분은 정확히 $\bigoplus_{C:\omega_C>0}\mathbb Z/N_{\omega_C}$ 이고, 어느 성분의 $\omega_C$ 도 $N_\omega$ 의 크기 순서로 복원된다($|N_w|$ 는 $w$ 에 대해 증가).

**정리 6 ($p$-랭크)** [증명]. $\gcd(a,b)=1$, 성분 $C$. $\mathrm{rank}_p:=\dim_{\mathbb F_p}A_C\otimes\mathbb F_p$ 는
- $p\nmid ab$: $[p\mid N_{\omega_C}]$ ($\omega_C=0$ 이면 1),
- $p\mid a$: $\#\{v\in C:\ \text{들어오는 호 0}\}$ (원천 수),
- $p\mid b$: $\#\{v\in C:\ \text{나가는 호 0}\}$ (싱크 수).
*증명.* $p\mid a$: $\bmod p$ 에서 관계는 $b\,x_{\rm head}=0$, 곧 머리가 되는 정점이 모두 0; 자유로운 것은 원천. $p\mid b$ 는 보조정리 0(ii). $p\nmid ab$: 정리 5. ∎
**따름 (비틀림 랭크)** [증명]. $p\mid a$ 이면 $A_C$ 의 $p$-비틀림 랭크는 $\#\text{원천}(C)-[\omega_C=0]$, $p\mid b$ 이면 $\#\text{싱크}(C)-[\omega_C=0]$. (자유 부분이 $\omega=0$ 일 때 1 이고 $N_\omega$ 는 $p$ 와 서로소.) 특히 $\omega_C=0$ 인 성분에서 $T_a=0\iff$ 원천이 정확히 하나; $\omega_C\ne0$ 인 성분에서 $T_a=0\iff$ 원천 없음. 높이 함수가 있으면 최솟값 정점이 원천이므로 $\omega=0$ 이면 원천 수 $\ge1$ 로 일관.

**명제 7 (별 그래프, 나무의 최소 예)** [증명]. 싱크 $y$ 에 원천 $x_1,\dots,x_d$ 가 들어오는 별: $A\cong\mathbb Z\oplus(\mathbb Z/a)^{d-1}$. 반대로 원천 하나에서 $d$ 개가 나가면 $A\cong\mathbb Z\oplus(\mathbb Z/b)^{d-1}$.
*증명.* 기저 $(x_1,y,z_i=x_i-x_1)$ (단모듈러). 관계 $ax_i+by=az_i+(ax_1+by)$ 이므로 $A=\mathbb Z^2/(a,b)\oplus(\mathbb Z/a)^{d-1}$ 이고 $\gcd(a,b)=1$ 이면 $\mathbb Z^2/(a,b)\cong\mathbb Z$. ∎ (V: $a=-2$ 에서 $\mathbb Z\oplus\mathbb Z/2$, R1 researcher3 의 예와 일치.)

**명제 8 (단일 근 공식)** [증명]. $b=1$, $\lambda=-a\in\mathbb Z$ (또는 $\mathbb Z_{(p)}$, $p\mid a$ 이고 $b$ 가 단위인 국소화), 방향 그래프의 모든 정점이 정점 $s$ 에서 도달 가능하다고 하자. $L_v$ = $s$ 에서 $v$ 로의 걸음 길이 집합, $m_v=\min L_v$, $g_v=\gcd\{\ell-m_v:\ell\in L_v\}$. 그러면 $A_G$ 는 순환 $\mathbb Z/D$,
$$D=\gcd_{v:\ g_v>0}\ \lambda^{m_v}(\lambda^{g_v}-1)\quad(\text{모든 }g_v=0\text{ 이면 }A=\mathbb Z).$$
*증명.* 모든 $x_v=\lambda^{\ell}x_s$ 이므로 $x_s$ 가 생성원. 임의의 $m$ 에 대해 $\mathrm{Hom}(A,\mathbb Z/m)=\{c\in\mathbb Z/m:\ (\lambda^{\ell}-\lambda^{\ell'})c=0\ \forall v,\ \ell,\ell'\in L_v\}=\mathrm{Ann}_{\mathbb Z/m}(D)$. 한편 $A\cong\mathbb Z/N$ 이면 $\mathrm{Hom}(A,\mathbb Z/m)\cong\mathbb Z/\gcd(N,m)$. 모든 $m$ ($m=ND$ 포함)에서 $\gcd(N,m)=\gcd(D,m)$ 이므로 $N=D$. ($\gcd_i\lambda^{m}(\lambda^{d_i}-1)=\lambda^m(\lambda^{\gcd d_i}-1)$.) ∎ [계산 확인: 단일 원천 무작위 방향 그래프 400개, $\lambda\in\{2,3,-2,4,6,5,-3\}$ 에서 일치 — 증명 단계 확인용.]
**해석.** $\lambda$-부분(= $p\mid a$ 부분)의 지수는 $v_p(\lambda)\cdot\min\{m_v:\ g_v>0\}$: **"서로 다른 길이의 걸음으로 도달되는 정점까지의 최단 거리"**. $\lambda$ 와 서로소인 부분은 $\gcd_v(\lambda^{g_v}-1)=\lambda^{\omega}-1$. 방향 사이클 $\vec C_n$: $L_v=\{d+kn\}$, $D=\lambda^n-1$ ✓ (정리 1).

**따름 9 (세타 그래프, 모두 $u\to v$)** [증명 스케치 + 계산 확인]. 경로 길이 $p_1\le p_2\le p_3$, $d=\gcd(p_2-p_1,p_3-p_1)$, $N_d\ne0$: $A\cong\mathbb Z/\big((ab)^{p_1}N_d\big)$ 순환. ($p\nmid ab$: 정리 5, $\omega=d$. $p\mid a$: 원천 $u$ 하나, 명제 8 의 국소 판, $u$ 가 길이 $p_1,p_2,\dots$ 로 $v$ 에 도달하므로 지수 $v_p(a)p_1$. $p\mid b$: 보조정리 0(ii)로 싱크 $v$ 하나, 같은 지수. CRT.) [계산 확인: $(a,b)\in\{(-2,1),(2,3),(-3,2),(-2,-3)\}$, 경로 길이 9세트; $N_d=0$ 인 퇴화($\lambda=1$ 등)는 자유 $\mathbb Z$.]

**유니사이클릭·나무 붙이기** [증명]. 새 정점 $y$ 를 호 $x\to y$ 로 붙이면($y$ 는 머리) $A_{G'}\otimes\mathbb Z[1/b]\cong A_G\otimes\mathbb Z[1/b]$ (소거); $y\to x$ 로 붙이면($y$ 는 꼬리) $\mathbb Z[1/a]$ 에서 불변. 곧 **잎을 붙여도 비틀림이 새로 생기는 곳은 $a$ 또는 $b$ 의 소인수뿐**. 따라서 사이클에 아웃-나무(들어오는 호가 하나)만 붙인 유니사이클릭에서는 $T_a=0$, 원천 수·싱크 수가 $T_a,T_b$ 를 정한다: 방향 사이클 $+$ 나가는 나무에서는 $A\cong\mathbb Z/N_n\oplus T_b$ ($T_b$ 의 $p$-랭크 = 싱크 수). [계산 확인: 삼각형 $\vec C_3$ + 꼬리 $2\to3\to4$: $a=-2,b=1$ 에서 $A=\mathbb Z/7$.]

**일반 구조 추측** [추측; 증명된 부분은 위 정리들]. 연결 성분 $C$, 방향 $o$, $\gcd(a,b)=1$:
$$A_C\ \cong\ \underbrace{\mathbb Z\ \text{or}\ \mathbb Z/N_{\omega_C}}_{\text{(I) 순환 불균형, 방향 클래스만}}\ \oplus\ T_a(C,o,a)\ \oplus\ T_b(C,o,b),$$
$T_a$ 는 $a$ 의 소인수 $p$ 에서만, 랭크 $\#\text{원천}-[\omega=0]$ (증명됨), 정확한 군은 방향 $o$ 에 의존(정리 3′ 아래 V/역V). **추측 T**: $T_a\cong\bigoplus_iZ/\lambda^{e_i}$ 형 ($\lambda=-a/b$, $e_i$ 는 $(C,o)$ 의 조합적 불변량, $a$ 의 값에 무관). 근거: 나무 `tree.py` 에서 $a=-2$ 와 $a=-6$ 일 때 인자가 $[2,4]\leftrightarrow[6,36]$, $[2,2]\leftrightarrow[6,6]$ 처럼 지수 패턴이 같다(예 1개: 다중 나무에서 $[2,4]$ 는 합류 정점 하나에 세 경로의 길이 1,2,2: 단순 곱 $\mathbb Z/2\oplus\mathbb Z/2$ 가 아님). 이 증거는 소수의 예이므로 근거로 쓰지 않고, 증명 방향(단일 근 공식의 다중 원천 판)은 후속연구 1순위.

**공통 패턴과 장애물.** 패턴: (P1) 비틀림은 (I) 닫힌 걸음 불균형, (II) 합류($p\mid a$), (III) 분기($p\mid b$) 세 곳에서만 나온다. (I) 은 감김 클래스에만 의존, (II)(III) 는 방향의 세부(원천·싱크·최단 거리)에 의존. (P2) 모든 경우 "근에서 걸음 길이로 읽는다"(명제 8): 비틀림 = 같은 정점에 서로 다른 길이로 도달 시 생기는 $\lambda^\ell-\lambda^{\ell'}$. (P3) 다중 원천에서는 원천 사이의 "관계 나무"가 생기고 행렬이 나무꼴이 된다. 장애물: (O1) 다중 원천 $T_a$ 의 정확한 군 구조(최대 소행렬 gcd 는 계산되나 불변인자 분해는 경로 길이 조합에 의존), (O2) $\gcd(a,b)>1$ 의 혼합 그래프 일반식.

### 4. (참고) 정리 6 이 R1 결과와 만나는 곳
$p\mid a$ 에서 $\dim_{\mathbb F_p}\mathbb F_p^G=\#\text{원천}$ 은 R1 researcher3 의 퇴화형 ($R=\langle(1,0)\rangle$, $\dim$ = 들어오는 호 없는 정점 수)과 정확히 일치하고, 정리 5·6 은 한 $A_G$ 가 **"비퇴화 소수에서는 감김 클래스, 퇴화 소수에서는 원천/싱크 수"** 를 동시에 담고 있음을 보인다.

### 5. 표: $a=-2$, $b=1$ ($x_{\rm head}=2x_{\rm tail}$), $R^G=\mathrm{Hom}(A_G,R)$
$A_G$ 는 스미스 꼴로 계산했고(`tab.py`) $\mathrm{Hom}(\mathbb Z/N,\mathbb Z/m)=\mathbb Z/\gcd(N,m)$, $\mathrm{Hom}(\mathbb Z^f,R)=R^f$ 로 읽었다 [계산 확인]. 이 중 사이클·별·세타는 위 정리로 손으로 얻어진다.

| 그래프 (방향) | $A_G$ | $\mathbb Z/4$ | $\mathbb Z/6$ | $\mathbb Z$ | $\mathbb Q$ | 손으로 구하는 근거 |
|---|---|---|---|---|---|---|
| $\vec C_3$ | $\mathbb Z/7$ | 0 | 0 | 0 | 0 | 정리 1: $N=-8+1$ |
| $\vec C_4$ | $\mathbb Z/15$ | 0 | $\mathbb Z/3$ | 0 | 0 | $N=15$ |
| $\vec C_6$ | $\mathbb Z/63$ | 0 | $\mathbb Z/3$ | 0 | 0 | $N=63$ |
| 반평행 $K_2$ ($\vec C_2$) | $\mathbb Z/3$ | 0 | $\mathbb Z/3$ | 0 | 0 | $N=4-1$ |
| 루프 | 0 | 0 | 0 | 0 | 0 | $x=2x\Rightarrow x=0$ |
| 합류 V ($0\to2\leftarrow1$) | $\mathbb Z\oplus\mathbb Z/2$ | $\mathbb Z/4\oplus\mathbb Z/2$ | $\mathbb Z/6\oplus\mathbb Z/2$ | $\mathbb Z$ | $\mathbb Q$ | 명제 7 |
| 분기 역V ($2\to0,2\to1$) | $\mathbb Z$ | $\mathbb Z/4$ | $\mathbb Z/6$ | $\mathbb Z$ | $\mathbb Q$ | 명제 7 ($b=1$) |
| 방향 경로 $P_3$ | $\mathbb Z$ | $\mathbb Z/4$ | $\mathbb Z/6$ | $\mathbb Z$ | $\mathbb Q$ | 단일 근, $g_v=0$ |
| 교대 경로 $0\to1\leftarrow2\to3$ | $\mathbb Z\oplus\mathbb Z/2$ | $\mathbb Z/4\oplus\mathbb Z/2$ | $\mathbb Z/6\oplus\mathbb Z/2$ | $\mathbb Z$ | $\mathbb Q$ | 정리 6: 원천 2, 비틀림 랭크 1 |
| 교대 $C_4$ | $\mathbb Z\oplus\mathbb Z/2$ | $\mathbb Z/4\oplus\mathbb Z/2$ | $\mathbb Z/6\oplus\mathbb Z/2$ | $\mathbb Z$ | $\mathbb Q$ | 정리 2: $s=2$, $f=r$ |
| 추이 삼각형 | $\mathbb Z/2$ | $\mathbb Z/2$ | $\mathbb Z/2$ | 0 | 0 | 정리 2: $|ab|^1N_1=2$ |
| 세타 (길이 1,2,3) | $\mathbb Z/2$ | $\mathbb Z/2$ | $\mathbb Z/2$ | 0 | 0 | 따름 9: $2^1(2^1-1)$ |
| 세타 (길이 2,3,4) | $\mathbb Z/4$ | $\mathbb Z/4$ | $\mathbb Z/2$ | 0 | 0 | $2^2(2^1-1)$ |
| 세타 (길이 2,2,2) | $\mathbb Z$ | $\mathbb Z/4$ | $\mathbb Z/6$ | $\mathbb Z$ | $\mathbb Q$ | $d=0$ |
| $\vec C_3$ + 꼬리 | $\mathbb Z/7$ | 0 | 0 | 0 | 0 | 잎 붙이기 |
| 분리합 $\vec C_3\sqcup$ V | $\mathbb Z\oplus\mathbb Z/14$ | $\mathbb Z/4\oplus\mathbb Z/2$ | $\mathbb Z/6\oplus\mathbb Z/2$ | $\mathbb Z$ | $\mathbb Q$ | $A_{G\sqcup H}=A_G\oplus A_H$, CRT |

**교차 검증 (CRT)** [증명]: $\mathbb Z/6=\mathbb Z/2\times\mathbb Z/3$, $R^G=(\mathbb F_2)^G\times(\mathbb F_3)^G$. $\mathbb F_2$ 에서 $\lambda=0$ (머리=0): 차원 = 원천 수. $\mathbb F_3$ 에서 $\lambda=-1$: 기여 1 $\iff$ 성분이 이분(감김 짝수). 예: 합류 V: $2$ 원천 $\to(\mathbb Z/2)^2$, 이분 $\to\mathbb Z/3$: 합 $\mathbb Z/6\oplus\mathbb Z/2$ ✓. $\vec C_4$: 원천 0, 이분 $\to\mathbb Z/3$ ✓. 추이 삼각형: 원천 1, 비이분 $\to\mathbb Z/2$ ✓. $\mathbb Z/4$ 열: $V$ 에서 $|\mathrm{Hom}|=8$: $x_0,x_1\in\mathbb Z/4$, $x_2=2x_0=2x_1$ 이므로 $x_0-x_1\in\{0,2\}$, $4\cdot2=8$ ✓.

### 6. 판정: 환으로 확장하면 기존 규칙 $a+b=0$ 보다 무엇이 풍부한가
(1) **정보량.** 체 위에서 $a=1,b=1$ 규칙($\lambda=-1$)은 "$\omega_C$ 가 짝수인가"(이분성)만 읽고($\mathbb Z/2$ 하나만 비틀림, $A_G=\mathbb Z^{\rm 이분}\oplus(\mathbb Z/2)^{\rm 비이분}$), $\lambda=1$ 은 성분 수만 읽는다. 정수 이득 $\lambda=2$ 규칙의 $A_G$ 는 $\bigoplus_C\mathbb Z/(2^{\omega_C}-1)$ (정리 5) 를 담고 있어 **감김 gcd $\omega_C$ 전체**(그리고 이 크기가 $\omega$ 에 대해 증가하므로 곱 $\prod(2^{\omega_C}-1)$ 로 거의 복원)를 읽는다. 환 $\mathbb Z/p^e$ 는 소수 $p$ 마다 $v_p(2^{\omega}-1)$ 를 읽고, $\mathbb Q/\mathbb Z$ (또는 원군 $\mathbb T$) 위에서는 $R^G=\mathrm{Hom}(A_G,\mathbb Q/\mathbb Z)$ 가 $A_G$ 의 퐁트랴긴 쌍대(완전 불변량)다. 체만 쓰면 소수마다 한 비트, 환을 쓰면 정수 하나.
(2) **구조.** 체에서는 성분당 $\dim\le1$ 이었으나(R1 researcher3 의 O1) 환에서는 합류·분기(정리 6 따름)로 $R^G$ 가 한 성분에서도 높은 길이/계수를 가진다: V 에서 $\mathbb Z/4\oplus\mathbb Z/2$. 곧 "차원이 성분 수를 못 넘는" 약점이 사라진다(환에서의 길이는 $\mathrm{rank}\,T_a$ 만큼 커진다).
(3) **함자성.** 정수 계수이므로 모든 환 사상 $R\to R'$ 에 대해 공변이며 $R^G=\mathrm{Hom}(A_G,R)$ 로 하나의 대상 $A_G$ 가 모든 환의 $R^G$ 를 만든다 (R2 researcher3 의 평탄성 과제와 연결). $\lambda=-a/b$ 로 쓴 임의 $\lambda$ 규칙은 $\lambda$ 가 단위인 환에서만 방향 불변(스위칭)이 되고, $p\mid ab$ 에서 방향 의존성이 생긴다는 점이 정수 규칙의 새 현상이다(표의 V/역V).
(4) **나쁜 점.** 방향 데이터가 필요하고, 방향을 무방향 불변량으로 만들려면 합산/최적화가 필요(R1: $k=3$ 에서 NP-완전 [기억-미검증 수준]). $\gcd(a,b)>1$ 이거나 $p\mid ab$ 인 소수에서는 방향 클래스를 넘는 세부 구조(원천/싱크)에 의존해 일반 공식이 닫혀 있지 않다(추측 T). 기존 규칙은 방향 없이 무방향 그래프에 쓰이며 $\mathbb Z/2$ 하나로 깔끔한 것이 장점이다.
**결론**: 환 확장의 새 정보는 "$\omega$ 의 값 자체 + 합류 구조"이며, 기존 규칙이 보던 것(이분성)은 $\omega$ 의 짝홀로 그 안에 포함된다. 정보 풍부성에서는 환·정수 이득이 확실히 우월하고, 대가는 방향 의존과 $p\mid ab$ 의 복잡성이다.

## 문주님께 요청
- 없음. (선택: 이득 그래프 · biased graph 의 고전 결과 중 "방향 사이클 뒤집기" 정리의 출처가 필요하면 논문 목록을 주시면 R3 에 대조하겠다. Pretzel 정리는 위에서 직접 증명했으므로 필수는 아니다.)

## 후속연구 지점
1. **다중 원천 $T_a$ 의 정확한 군 구조 (추측 T 의 증명)** — 무엇을: 단일 근 공식(명제 8)을 원천이 여럿인 방향 그래프로 확장해 $T_a\cong\bigoplus\mathbb Z/\lambda^{e_i}$ 와 $e_i$ 의 조합적 정의(경로 길이·최소 소행렬)를 구한다. 왜: $A_G$ 의 마지막 미결 조각(정리 6 은 랭크만 줌)이고, 이것이 닫혀야 "모든 소수·모든 환 위의 $R^G$" 가 완전 결정된다. 시작: 나무($ω=0$)에서 관계 나무 $S$ 위의 가중 행렬의 최대 소행렬 gcd = $\gcd_{s_0}\prod_e\lambda^{\text{(원단 가중)}}$ 를 증명하고 $[2,4]$ 예를 이론화. 난점: 불변인자(군 구조) 대 위수(최대 소행렬)의 차, 가중이 근 선택에 의존.
2. **방향 절단 동치류의 수와 무방향 불변량** — 무엇을: 연결 그래프의 방향 동치류(정리 3) = 감김 함수 $H_1\to\mathbb Z$ (실현 가능한 것)의 수를 $\mathrm{Hom}(G,C_k)$/흐름 다항식으로 세고, $Z(G;a,b)=\sum_{\text{클래스}}|A_G\otimes\mathbb Z[1/ab]|$ 가 $C_6$, $K_{3,3}$, $Q_3$ 을 구분하는지 본다. 왜: 무방향 그래프의 불변량이 되어야 문주님의 "가장 나은 규칙" 판정에 쓸 수 있다. 시작: 정리 3 의 $h$ 증명을 이용해 클래스 수 = (방향 수)/(절단 뒤집기 궤도) 계산, 작은 그래프 손 계산. 난점: 실현 가능한 감김 함수의 특성화, 일반 그래프에서 계산 복잡도.
3. **$\gcd(a,b)>1$ 과 혼합 사이클의 완전 분류** — 무엇을: 정리 2 의 $s\ge2$ 사이클에서 $s\times s$ 행렬(경로 길이 $l_j,m_j$)의 스미스 꼴을 구한다. 왜: 유니사이클릭 $A_G$ 를 닫는다. 시작: 행 $\lambda^{l_j}e_j-\lambda^{m_j}e_{j+1}$ 의 $(s-1)$-소행렬이 단항식이라는 점. 난점: 지수들의 순서 의존, $a,b$ 가 둘 다 합성수일 때의 CRT.
4. **$A_G$ 와 임계군/라플라시안 $M_{a,b}$ 의 연결** — 무엇을: 방향 사이클 $\mathbb Z/N_n$ 이 $\mathbb Z[x]/(x^n-1)$ 의 어떤 몫(순환 그래프 임계군 $\mathbb Z/n$ 등)에 대응하는지, 비순환 $T_a$ 가 R2 researcher3 의 평탄성/임계군 과제와 어떻게 만나는지. 왜: STATUS 후보 2·3. 시작: $\mathbb Z[t^{\pm1}]$ 위 $A_G(t)$ 를 만들고 $t=\lambda$ 특수화로 보기. 난점: $t$ 가 단위가 아닐 때 평탄성이 깨짐.
5. **$R=\mathbb Q/\mathbb Z$ 와 쌍대성, 텐서곱 $G\times H$** — 무엇을: $\mathrm{Hom}(A_G,\mathbb Q/\mathbb Z)$ 를 "표준 값환"으로 하는 정리 정리, 곱그래프에서 $\omega(G\times H)=\gcd(\omega_G,\omega_H)$ 추측 증명 (R1 후속연구 5). 왜: 완전 불변량과 곱 호환성을 한 번에. 시작: 곱의 닫힌 걸음이 두 사영의 닫힌 걸음이라는 사실. 난점: 곱의 성분 구조(연결성) 비자명.
