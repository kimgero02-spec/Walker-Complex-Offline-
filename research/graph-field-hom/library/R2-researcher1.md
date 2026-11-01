# [R2-researcher1] 무방향 규칙의 환 확장: 대칭 부분가군 분류, $R^G$ 구조정리, 판정

- 작성자: researcher1 / 라운드: R2 / 역할: 연구원(포메이션 I 분담, 무방향 규칙의 환 확장)
- 코드: `rooms/researcher1/r2_ring.py` (순수 Python. $\mathbb Z/n$ 의 대칭 부분가군을 전부 열거해 분류 정리의 개수와 맞춰 보고, 각 규칙·소형 그래프에서 $|R^G|$ 를 정리 3 의 공식과 대조. 증명 단계의 확인용이며 근거는 아래 증명이다.)

## 요약

1. [증명] 모든 $G$ 에서 $\mathrm{Hom}_S(G,R)$ 가 $R$-가군 $\iff$ $S\subset R\times R$ 가 $R$-부분가군. 무방향이면 $S$ 는 **Goursat 삼조** $(I,J,\theta)$ 와 일대일 대응한다: $I\subset J$ 아이디얼, $\theta$ 는 $J/I$ 의 $R$-가군 자기동형이고 $\theta^2=1$, $S=\{(x,y)\in J^2:\ \bar y=\theta\bar x\}$. 체에서는 $I\in\{0,J\}$, $J\in\{0,F\}$, $\theta=\pm1$ 이라 4종이 된다. 환에서 새로 생기는 것은 (a) 합동 규칙 $I\ne0,J$, (b) 지지집합 $J\ne R$, (c) $\theta\neq\pm1$ (예: $\mathbb Z/8$ 의 $y=3x$, $\mathbb Z/12$ 의 $y=5x$), (d) 비순환 $J/I$ 의 비스칼라 $\theta$. $\mathbb Z/4,\mathbb Z/6,\mathbb Z/8,\mathbb Z/9$ 에서 각각 7, 12, 15, 9 개 [증명]+[계산 확인].
2. [증명] **구조정리**: 연결성분 중 간선이 있는 이분 성분은 $S\oplus I^{n_C-2}$, 비이분 성분(루프 포함)은 $J_\theta\oplus I^{n_C-1}$ 를 기여하고, 고립점은 $R$ 이다. 여기서 $J_\theta=\{x\in J:\theta\bar x=\bar x\}$. 특히 $x+y=0$ 규칙은 $R^G\cong R^{b}\oplus R[2]^{\,c-b}$ ($R[2]=\{r:2r=0\}$). $\mathbb Z/4$ 에서 $K_3$ 는 $\{0,2\}$ 를 기여한다. 체에서는 $R[2]\in\{0,R\}$ 이라 "0 아니면 전부" 였던 것이, $2$ 가 영인자이면서 $0$ 이 아닌 환에서는 중간 가군이 된다. 하나의 규칙으로 $b$ 와 $c$ 를 둘 다 읽는다 ($\mathbb Z/4$: $(\mathbb Z/4)^b\oplus(\mathbb Z/2)^{c-b}$).
3. [증명] 기저변환 $R^G\otimes R'\to R'^G$: $\Delta$ 는 항상 동형, $x+y=0$ 은 $R[2]\otimes R'\to R'[2]$ 가 동형일 때(예: $R'$ 평탄)만. 깨짐: $\mathbb Z\to\mathbb Z/2$ ($K_3$: $0\to\mathbb Z/2$, 전사 실패), $\mathbb Z/4\to\mathbb Z/2$ ($K_3$: $\mathbb Z/2\to\mathbb Z/2$ 가 **영사상**), $\mathbb Z\to\mathbb Z/4$ 합동 규칙 $x\equiv y\ (2)$ 의 $K_2$ (전사이나 단사 실패).
4. 판정: **해소하지 못한다.** 구조정리에 의해 모든 가환환과 모든 대칭 부분가군 규칙에서 $R^G$ 의 동형류는 (고립점 수, 각 성분의 정점 수 $n_C$, 이분 여부)만의 함수다. 따라서 $C_6$ 와 $K_{3,3}$ 뿐 아니라 $P_6$ 까지 모든 환·모든 규칙에서 동형이다 [증명]. 원인은 목표 그래프 $\Gamma_S(R)$ 가 완전이분그래프·루프 달린 완전그래프·고립점의 분리합이기 때문이다(정리 5). 환 확장이 주는 이득은 성분 통계를 더 선명히 읽는 것(특히 char 2 붕괴 해소)뿐이다.

## 본문

### 0. 설정

그래프 $G=(V,E)$ 는 루프·다중간선 허용 무방향. $n=|V|$, $c$=성분 수, $b$=이분 성분 수(간선 없는 고립점은 이분으로 센다), $i$=고립점 수, 간선이 있는 성분 수 $c'=c-i$, 그중 이분 $b'=b-i$, $n'=n-i$. $R$ 은 가환환(단위원 있음), 규칙은 $S\subset R\times R$, $\mathrm{Hom}_S(G,R)=\{\varphi:V\to R\mid \forall uv\in E:(\varphi u,\varphi v)\in S\}$. 무방향이므로 $S$ 는 대칭이어야 규칙이 의미가 있다(간선 $uv=vu$). 기호: $\Delta_I=\{x-y\in I\}$, $\Delta^-_I=\{x+y\in I\}$, $\Delta=\Delta_0$, $\Delta^-=\Delta^-_0$.

### 1. 정리 1 (가군 조건의 필요충분) [증명]

**정리 1.** 대칭 $S\subset R^2$ 에 대해, 모든 $G$ 에서 $\mathrm{Hom}_S(G,R)$ 가 $R^V$ 의 $R$-부분가군 $\iff$ $S$ 가 $R^2$ 의 $R$-부분가군.

증명. ($\Leftarrow$) $\varphi,\psi\in\mathrm{Hom}$, $r\in R$ 이면 간선 $uv$ 에서 $(\varphi u+r\psi u,\varphi v+r\psi v)=(\varphi u,\varphi v)+r(\psi u,\psi v)\in S$. $0\in S$ 이므로 영함수도 포함. 이것은 부분가군 조건 그대로다.
($\Rightarrow$) $G=K_2$ (정점 $u,v$, 간선 하나)에서 $R^V=R^2$ 이고 $\mathrm{Hom}_S(K_2,R)=S$ 이므로 $S$ 가 $R^2$ 의 부분가군이어야 한다. $\square$

참고. 루프 $uu$ 는 $(x,x)\in S$ 를 요구하며 $\{(x,x)\}\cap S$ 는 다시 부분가군이므로 정리 1 에 추가 조건이 필요 없다. 부분가군 대신 부분군만 요구하면 $\mathrm{Hom}$ 은 아벨군이 된다(R1 에서 $\mathbb F_4$, Frobenius 꼬임이 이 경우).

### 2. 정리 2 (대칭 부분가군의 분류: Goursat 삼조) [증명]

**정리 2.** $R^2$ 의 대칭 부분가군 $S$ 는 삼조 $(I,J,\theta)$ 와 일대일 대응한다. $I\subset J$ 는 $R$ 의 아이디얼, $\theta\in\mathrm{Aut}_R(J/I)$, $\theta^2=\mathrm{id}$, 그리고
$$S=S(I,J,\theta)=\{(x,y)\in J\times J:\ \bar y=\theta(\bar x)\ \text{in } M:=J/I\}.$$

증명. $S$ 가 주어졌다고 하자. $J:=\pi_1(S)$ (첫 사영의 상). 대칭이므로 $\pi_2(S)=\pi_1(\tau S)=J$ ($\tau$=교환). $I:=\{x:(x,0)\in S\}$. 대칭에 의해 $\{y:(0,y)\in S\}=I$. $I\subset J$ 는 정의에서 즉시. $\theta:J\to J/I$ 를 $(x,y)\in S$ 일 때 $x\mapsto\bar y$ 로 정의한다. 잘 정의됨: $(x,y),(x,y')\in S$ 이면 $(0,y-y')\in S$ 이므로 $y-y'\in I$. $R$-선형. 핵: $\bar y=0$ 이면 $(x,y)\in S$, $y\in I$ 이고 $(0,y)\in S$ 이므로 $(x,0)\in S$, 즉 $x\in I$. 따라서 $\theta$ 는 $J/I\to J/I$ 단사이고, $\pi_2(S)=J$ 이므로 전사. 대칭성: $(x,y)\in S\Rightarrow(y,x)\in S$ 이므로 $\theta(\bar y)=\bar x$, 곧 $\theta^2=1$. 역으로 $(I,J,\theta)$ 가 주어지면 위 $S$ 는 부분가군이고 대칭이며 $\pi_1 S=J$, $\{x:(x,0)\in S\}=I$ ($\theta$ 가 단사이므로), 위 구성이 $\theta$ 를 복원한다. $\square$

**체에서의 환원 [증명].** $F$ 체: 아이디얼은 $0,F$ 뿐. $(I,J)\in\{(0,0),(0,F),(F,F)\}$; $(0,0)\to S=0$, $(F,F)\to S=F^2$, $(0,F)$ 이면 $M=F$, $\theta\in F^\times$, $\theta^2=1\Rightarrow\pm1$: $\Delta,\Delta^-$. R1 의 4종과 일치하고, char 2 에서 $\theta=1=-1$ 이 합쳐진다.

**따름 2a (순환형 = 비틀린 대각선) [증명].** $J=R$ 이면 $\theta$ 는 $R/I$ 의 자기동형이므로 곱셈 $u\in R/I$ 이고, $u^2=1$ in $R/I$:
$$S_{u,I}=\{(x,y):\ y\equiv ux \pmod I\},\qquad u^2\equiv1 \pmod I.$$
$u=1$: 합동 규칙 $\Delta_I$, $u=-1$: $\Delta^-_I$.
**따름 2b (곱환) [증명].** $R=R_1\times R_2$ 이면 멱등원 $e_1,e_2$ 로 $S=e_1S\oplus e_2S$ 이고 각각은 $R_i^2$ 의 대칭 부분가군이다. 즉 $S=S_1\times S_2$. 그래서 $\mathbb Z/n$ 은 소거듭제곱으로 환원된다.
**따름 2c (소거듭제곱) [증명].** $R=\mathbb Z/p^k$: 아이디얼은 $(p^a)$, $0\le a\le k$. $J=(p^a)$, $I=(p^b)$, $a\le b$, $J/I\cong\mathbb Z/p^m$ ($m=b-a$), $\mathrm{Aut}=(\mathbb Z/p^m)^\times$ 에서 $\theta^2=1$ 의 해 개수: $p$ 홀수 이면 $m\ge1$ 에서 2개($\pm1$), $m=0$ 에서 1개. $p=2$ 이면 $m=0,1$ 에서 1, $m=2$ 에서 2 ($\pm1$), $m\ge3$ 에서 4 ($\pm1,\ 2^{m-1}\pm1$).

**구체 열거 (모두; $[S]$ 는 규칙, 코드로 개수 대조: 7, 12, 15, 9 [계산 확인]).**

*$R=\mathbb Z/4$ (7개)* $(a,b,\theta)$: 
(0,0): $S=R^2$ (제약 없음) · (0,1): $x\equiv y\ (2)$ (이때 $\equiv x+y\in(2)$ 와 같음) · (0,2,+): $x=y$ · (0,2,−): $x+y=0$ · (1,1): $S=2R\times2R$ · (1,2): $S=\{(0,0),(2,2)\}$ · (2,2): $S=0$.
체와 비교: 체에서는 $0,\Delta,\Delta^-,F^2$ 만 있었다. $\mathbb Z/4$ 에서 새 것은 $x\equiv y\ (2)$, $2R\times2R$, $\{(0,0),(2,2)\}$ 세 개.

*$R=\mathbb Z/6\cong\mathbb F_2\times\mathbb F_3$ (12개 = 3×4)* 따름 2b 에 의해 인수별 규칙의 곱: $\mathbb F_2$ 쪽 $\{0,\Delta,F^2\}$ ($\Delta=\Delta^-$), $\mathbb F_3$ 쪽 $\{0,\Delta,\Delta^-,F^2\}$. 새 것은 인수마다 다른 규칙을 고르는 것, 예: ($\mathbb F_2$ 에서 $F^2$, $\mathbb F_3$ 에서 $\Delta^-$) 는 $\{x+y\in(2)\}\cap$… 곧 합동 규칙 $x+y\equiv0\ (3)$ (코드 출력의 $|S|=12$ 두 개: $x\pm y\in\{0,3\}$), ($\mathbb F_2$ 에서 $\Delta$, $\mathbb F_3$ 에서 $0$) 은 $\{(0,0),(3,3)\}$.

*$R=\mathbb Z/8$ (15개)*: $m=0$ ($I=J$, 곧 $S=J\times J$): 4개, $m=1$: 3개, $m=2$ ($\theta=\pm1$): 2쌍 4개, $m=3$ ($\theta\in\{1,7,3,5\}$): 4개. 예: $y=3x$, $y=5x$ ($3^2=5^2=1$ in $\mathbb Z/8$) 는 환에서만 있는 **비$\pm1$ 대각선**이다. 코드 출력에서 $\{(1,3),(3,1),\dots\}$ 와 $\{(1,5),(5,1),\dots\}$ 로 확인.

*$R=\mathbb Z/9$ (9개)*: $m=0$: 3개, $m=1,2$: 각각 $\theta=\pm1$ 인 쌍 $(0,1),(0,2),(1,2)$ 이 6개. 비$\pm1$ 대각선 없음 (홀수 소수 거듭제곱의 순환군).
*$R=\mathbb Z/12$*: $u\in\{1,5,7,11\}$, $u^2=1$. $y=5x$ 는 $\mathbb Z/4$ 에서 $\Delta$, $\mathbb Z/3$ 에서 $\Delta^-$ ($5\equiv1\bmod4$, $\equiv-1\bmod3$) : 혼합형. [증명, 곱환]

*$R=\mathbb Z$*: 아이디얼 $(a)$, $J=(a)$. $I=(am)$ ($m\ge1$) 이면 $J/I\cong\mathbb Z/m$, $\theta=u$, $u^2\equiv1\ (m)$. $I=0$ 이면 $J/I\cong\mathbb Z$, $\theta=\pm1$. 따라서 $S=a\cdot\{y\equiv ux\ (m)\}$ ($a\ge0$ 은 배율, $m=0$ 이면 $y=\pm x$). 비$\pm1$ 인 $u$ 는 $m$ 에 비자명 제곱근 1 이 있을 때: $y\equiv 3x\ (8)$, $y\equiv5x\ (12)$ 등.

*$R=\mathbb Z[\varepsilon]/(\varepsilon^2)$*: $J=R$, $I=0$: $u=a+b\varepsilon$, $u^2=a^2+2ab\varepsilon=1$ 이면 $a=\pm1$, $2ab=0\Rightarrow b=0$: $\pm1$ 뿐. $I=(2\varepsilon)$: $u=1+k\varepsilon$ 는 $u^2=1+2k\varepsilon\equiv1$ 이므로 모든 $k$ 가 가능: $y\equiv(1+\varepsilon)x\ \bmod 2\varepsilon$ 은 **무한 족의 단일 예**. 또 $J=(\varepsilon)\cong\mathbb Z$ (R 의 작용은 $\varepsilon\mapsto0$), $I=0$: $\theta=\pm1$: $\{(k\varepsilon,\pm k\varepsilon)\}$.
*$R=\mathbb F_2[\varepsilon]/(\varepsilon^2)$*: $I=0,J=R$, $u=1+\varepsilon$, $u^2=1$: $y=(1+\varepsilon)x$ 가 체 $\mathbb F_2$ 의 $\Delta=\Delta^-$ 와 다른 새 규칙(표수 2 인데도).
*$R=F[x,y]/(x,y)^2$ ($F$ 홀수 표수)*: $J=\mathfrak m=Fx\oplus Fy$ (R 의 작용은 0), $I=0$, $\theta$ = $x\leftrightarrow y$ 교환. $S=\{(\alpha x+\beta y,\beta x+\alpha y)\}$ 는 **스칼라가 아닌 $\theta$** (비순환 $J/I$)인 규칙이며, $R$ 의 원소 $u$ 의 곱으로는 쓸 수 없다.

**공통 패턴 [증명].** 규칙의 모든 변형은 세 가지 자유도로 환원된다. (a) 합동 정도 $I$ (체: $0$ 이나 $J$ 만), (b) 지지집합 $J$ (체: $0$ 이나 $F$ 만), (c) 접착 자기동형 $\theta$ (체: $\pm1$ 만). 환에서 새로 생기는 것은 이 세 축이 체 이상으로 풀리는 것이 전부다. 또 $2$ 가 가역이면 $M=M_+\oplus M_-$ ($\theta=\pm1$ 고유가군, 사영자 $(1\pm\theta)/2$)로 분해되어 "$\Delta$ 와 $\Delta^-$ 의 합성" 형태가 되고, $2$ 가 가역이 아니면 분해가 깨져 $\theta$ 가 진정한 새 정보를 가진다.

**진정한 환 효과의 요약 [증명 완료한 범위].** 정수 위에서 함자적으로 모든 환에서 같은 규칙으로 읽히려면 $(u,m)\in\mathbb Z\times\mathbb N$, $m\mid u^2-1$ 인 정수형 $y\equiv ux\pmod{mR}$ 이어야 한다: $u^2=1$ 이 모든 $R$ 에서 대칭이려면 $\mathbb Z$ 에서 $u=\pm1$ 이어야 하고, 합동을 허용하면 $m\mid u^2-1$ 로 충분하다.

### 3. 정리 3 (구조정리) [증명]

$G$ 의 간선 있는 성분 $C$ 를 $n_C=|V(C)|$ 로 쓴다. 비이분 성분이란 홀수 닫힌 걷기(루프 포함)가 있는 성분.

**정리 3.** $S=S(I,J,\theta)$, $M=J/I$, $J_\theta:=\{x\in J:\theta\bar x=\bar x\}$ ($I\subset J_\theta\subset J$, $J_\theta/I=M^\theta$). 그러면 $R$-가군으로
$$\mathrm{Hom}_S(G,R)\ \cong\ R^{\,i}\ \oplus\ S^{\,b'}\ \oplus\ J_\theta^{\,c'-b'}\ \oplus\ I^{\,n'-b'-c'}.$$
유한환이면 $|\mathrm{Hom}_S(G,R)|=|R|^i\,|S|^{b'}\,|J_\theta|^{c'-b'}\,|I|^{n'-b'-c'}$ ($|S|=|M||I|^2$, $|J_\theta|=|M^\theta||I|$).

증명. 성분별로 분리된다($\mathrm{Hom}_S(G\sqcup H)=\mathrm{Hom}_S(G)\times\mathrm{Hom}_S(H)$). 고립점은 제약이 없어 $R$. 이제 $C$ 가 간선을 가진 연결 성분이라 하자. 간선 끝점은 모두 $J$ 에 들어가야 하고, 클래스 $\bar\varphi:V(C)\to M$ 는 간선마다 $\bar\varphi(v)=\theta\bar\varphi(u)$ 를 만족한다. 뿌리 $r$ 에서 걷기 길이 $d$ 를 따라 $\bar\varphi(w)=\theta^{d}\bar\varphi(r)$ 가 강제되고 $\theta^2=1$ 이라 $d$ 의 홀짝만 중요하다.
- (비이분) 홀수 닫힌 걷기가 있으면 그 걷기를 뿌리까지 이어 $\theta\bar\varphi(r)=\bar\varphi(r)$. 그러면 $\theta^d\bar\varphi(r)=\bar\varphi(r)$ 이므로 $\bar\varphi$ 는 $C$ 위에서 **상수** $x\in M^\theta$. 역으로 $x\in M^\theta$ 의 상수 클래스는 모든 간선(루프 포함)에서 $(\bar x,\bar x)=(\bar x,\theta\bar x)$ 를 만족한다. 따라서 $\mathrm{Hom}_C=\{\varphi:V(C)\to J:\ \varphi(v)-\varphi(r)\in I\ \forall v,\ \overline{\varphi(r)}\in M^\theta\}$, 사상 $\varphi\mapsto(\varphi(r),(\varphi(v)-\varphi(r))_{v\ne r})\in J_\theta\times I^{n_C-1}$ 은 $R$-선형 동형.
- (이분, 간선 있음) 색 $p(v)\in\{0,1\}$ 로 $\bar\varphi(v)=\theta^{p(v)}x$ ($x=\bar\varphi(r)\in M$ 임의). 이 식은 모든 간선(양 끝 색이 다름)에서 조건을 만족하며 그 외 조건은 없다. 간선 $rs$ 를 하나 고르고 $\varphi\mapsto(\varphi(r),\varphi(s),(\varphi(v)-\varphi(r))_{p(v)=0,v\ne r},(\varphi(w)-\varphi(s))_{p(w)=1,w\ne s})$. 첫 두 성분은 $(\varphi r,\varphi s)\in S$ 를, 나머지는 $I$ 의 원소를 준다. $R$-선형 동형 $\mathrm{Hom}_C\cong S\oplus I^{n_C-2}$.
각 성분을 모으면 정리의 식이다. $\square$

**정리 3 의 검증 [계산 확인].** $R=\mathbb Z/4,\mathbb Z/6,\mathbb Z/8,\mathbb Z/9$ 의 대칭 부분가군 전부(7+12+15+9=43개)와 그래프 $K_2,P_3,K_3,C_4,$ 루프+$K_2$, $K_3\sqcup K_2\sqcup\bullet,\ C_6,K_{3,3},P_6$ (가능한 범위)에서 $|\mathrm{Hom}|$ 이 위 식과 모두 일치(불일치 0). 또 $n\le8$ 에서 $C_6,K_{3,3},P_6$ 의 $\mathrm{Hom}$ 의 원소위수 분포가 모든 규칙에서 같음. (이 점검은 증명의 확인이다.)

**정리 4 ($x+y=0$ 규칙; 비이분 성분의 기여 = $R[2]$) [증명].** $S=\Delta^-$ ($I=0,J=R,\theta=-1$) 에서 $M=R$, $J_\theta=R[2]:=\{r\in R:2r=0\}$ 이고
$$R^G_{\Delta^-}\ \cong\ R^{\,b}\ \oplus\ R[2]^{\,c-b}.$$
(고립점은 이분으로 센다.) 더 직접적으로: 비이분 성분 $C$ 에서 $\varphi\mapsto\varphi(r)$ 은 $\mathrm{Hom}_C\to R[2]$ 동형이며 역은 $t\mapsto$ **상수함수 $t$**.
증명(정리 3 에서 따로 풀면). 걷기 $r\to w$ 를 따라 $\varphi(w)=(-1)^d\varphi(r)$. 홀수 닫힌 걷기가 있으면 $\varphi(r)=-\varphi(r)$, $2\varphi(r)=0$. 그러면 $\varphi(w)=(-1)^d\varphi(r)=\varphi(r)$ ($2\varphi(r)=0$ 이므로 부호 무관), 연결이라 $\varphi$ 는 상수 $t\in R[2]$. 역으로 상수 $t\in R[2]$ 는 $t+t=2t=0$ 이라 모든 간선을 만족. 단사·전사. 이분 성분은 $t$ 가 임의의 $R$ 원소: $\varphi(w)=(-1)^{p(w)}t$. $\square$

**따름 (체와의 차이) [증명].** $R[2]=\mathrm{Ann}(2)$ 는 $2\cdot:R\to R$ 의 핵이다. $R[2]=0\iff2$ 가 비영인자, $R[2]=R\iff 2=0$. 체에서는 둘 중 하나뿐이다: 홀수 표수면 비이분 성분이 0 기여, 표수 2 면 전부 기여 ($R1$ 의 $b\leftrightarrow c$ 도약). 환에서 $2$ 가 **0 이 아닌 영인자**이면 $R[2]$ 는 $0$ 과 $R$ 사이의 중간 가군이 되어 비이분 성분이 절반만 살아남는다.

| $R$ | $R[2]$ | $x+y=0$ 에서 $R^G$ |
|---|---|---|
| 체, 표수 $\ne2$; $\mathbb Z$; $\mathbb Z/9$; $\mathbb Z[\varepsilon]$ | $0$ | $R^b$ |
| 표수 2 의 환 ($\mathbb F_2,\mathbb F_4,\mathbb F_2[\varepsilon]$) | $R$ | $R^c$ ($\Delta^-=\Delta$) |
| $\mathbb Z/4$ | $\{0,2\}\cong\mathbb Z/2$ | $(\mathbb Z/4)^b\oplus(\mathbb Z/2)^{c-b}$ |
| $\mathbb Z/8$ | $\{0,4\}\cong\mathbb Z/2$ | $(\mathbb Z/8)^b\oplus(\mathbb Z/2)^{c-b}$ |
| $\mathbb Z/6$ | $\{0,3\}\cong\mathbb Z/2$ | $(\mathbb Z/6)^b\oplus(\mathbb Z/2)^{c-b}$ |
| $\mathbb Z/2^k$ | $2^{k-1}\mathbb Z/2^k\cong\mathbb Z/2$ | $(\mathbb Z/2^k)^b\oplus(\mathbb Z/2)^{c-b}$ |

예. $K_3$: $\mathbb Z/4$ 에서 $\{(0,0,0),(2,2,2)\}$ (상수 $\{0,2\}$), $\mathbb Z/6$ 에서 $\{0,3\}$ 상수 두 개 ($\mathbb Z/6=\mathbb F_2\times\mathbb F_3$: $\mathbb F_2$ 쪽은 $\Delta$ 로 1차원, $\mathbb F_3$ 쪽은 0). $C_6$: $\mathbb Z/4$ 에서 $\{t(+,-,+,-,+,-)\}\cong\mathbb Z/4$. $K_3\sqcup K_2$ : $\mathbb Z/2\oplus\mathbb Z/4$ (위수 8), $\mathbb Z/4$ 에서 이 모듈의 인수($\mathbb Z/4$ 개수=$b$, $\mathbb Z/2$ 개수=$c-b$)로부터 **$b$ 와 $c$ 를 모두** 읽는다 (유한생성 $\mathbb Z/4$-가군의 구조정리).

**$2$ 가 가역일 때와의 비교.** $2$ 가 가역이면 $R[2]=0$, $\theta=-1$ 에서 $M^\theta=0$, 비이분 성분의 기여는 $I^{n_C}$ ($J=R$ 일 때): 합동 규칙 $\Delta^-_I$ 도 "비이분 성분이 $R$ 부분을 잃고 $I$ 부분만 남기는" 모양이 된다. 예 $\mathbb Z/9$, $x+y\in(3)$, $K_3$: $\{0,3,6\}^3$ (27개).

**정리 4′ (합동 규칙, 일반 $u$) [증명].** $S_{u,I}$ 에서 (정리 3, $J=R$) 이분 성분은 $R\oplus I^{n_C-1}$ ($S\cong R\oplus I$), 비이분 성분은 $\{x\in R:(u-1)x\in I\}\oplus I^{n_C-1}$ (루프 포함, 홀수 닫힌 걷기에서 $u^{\mathrm{odd}}\equiv u$). 예: $\mathbb F_2[\varepsilon]$, $u=1+\varepsilon$, $I=0$: 이분 성분은 $R$ (위수 4), 비이분은 $\{x:\varepsilon x=0\}=(\varepsilon)$ (위수 2) — **표수 2 인데도 이분성이 보이는** 규칙이다.

### 4. 정리 5 (목표 그래프의 모양) [증명]

$\Gamma_S(R)$: 정점집합 $R$, $x\sim y\iff(x,y)\in S$. $\mathrm{Hom}_S(G,R)=\mathrm{Hom}_{\mathrm{graph}}(G,\Gamma_S(R))$.

**정리 5.** $\Gamma_S(R)$ 는 분리합으로 분해된다: (i) $x\notin J$ 인 $|R\setminus J|$ 개의 고립점(루프 없음); (ii) $\theta\bar m\ne\bar m$ 인 각 쌍 $\{m,\theta m\}\subset M$ 에 대해 두 잉여류 $m,\theta m$ ($I$ 의 평행이동) 사이의 완전이분그래프 $K_{|I|,|I|}$; (iii) 각 $m\in M^\theta$ 에 대해 잉여류 위의 **루프 달린 완전그래프** (루프 포함 모든 쌍이 간선).
증명. $x\in J$ 의 이웃은 $\{y\in J:\bar y=\theta\bar x\}$, 곧 잉여류 $\theta\bar x$ 전체. $\theta\bar x\ne\bar x$ 이면 $x$ 의 클래스 $m$ 과 $\theta m$ 이 서로의 이웃 전체. $\theta\bar x=\bar x$ 이면 자기 클래스가 이웃 전체(자기 자신 포함). $\square$

체의 경우(R1): $\Delta^-$ 는 루프 달린 한 점 $\{0\}$ 과 $K_2$ $(q-1)/2$ 개, $\Delta$ 는 루프 달린 점 $q$ 개. 정리 5 의 특수 경우다.

**따름 5 ($\mathrm{Hom}$ 개수) [증명].** 연결 $C$ (간선 있음) 에서 $\#\mathrm{Hom}(C,\Gamma)=\sum$ (성분별): 이분이면 완전이분 성분으로 $2|I|^{n_C}$ 개씩 $\times$ 쌍 수 $(|M|-|M^\theta|)/2$, 루프 클리크로 $|I|^{n_C}\times|M^\theta|$ 개 (이분 $C$ 도 루프 달린 클리크로는 간다): 합 $|M||I|^{n_C}$. 정리 3 의 위수 $|S||I|^{n_C-2}=|M||I|^{n_C}$ 와 일치. 비이분이면 루프 클리크로만: $|M^\theta||I|^{n_C}=|J_\theta||I|^{n_C-1}$ ✓.

### 5. 환 사상에 대한 공변성과 기저변환 (임무 3)

**공변성 조건 [증명].** 환 사상 $f:R\to R'$ 와 규칙 $S_R\subset R^2$, $S_{R'}\subset R'^2$ 에 대해 $f_*:\varphi\mapsto f\circ\varphi$ 가 $\mathrm{Hom}_{S_R}(G,R)\to\mathrm{Hom}_{S_{R'}}(G,R')$ 을 정의 $\iff$ $(f\times f)(S_R)\subset S_{R'}$ (필요: $K_2$ 에서 $\mathrm{Hom}=S$, 충분: 간선별). 이때 $f_*$ 는 $f$-반선형(즉 $R$-선형 사상 $R^G\to R'^G$). 정수형 규칙 $\Delta_{mR},\Delta^-_{mR},S_{u,mR}$ ($m\mid u^2-1$) 는 모든 $f$ 에서 성립한다. 예: $y\equiv 3x\ (8)$ 은 $\mathbb Z\to\mathbb Z/8$ 에서 $y=3x$ 가 되고 $\mathbb Z/8\to\mathbb Z/4$ 에서는 $y=-x$, 즉 $\Delta^-$ 로 간다. 한편 "$y=3x$ in $\mathbb Z/8$" 을 $\mathbb Z/4$ 의 규칙 $y=3x$ 로 읽으면 같은 것 ($3=-1$) 이지만 $\mathbb Z/16$ 에서 $y=3x$ 는 대칭이 아니다 ($9\ne1$). 따라서 정수 $u$ 로 정의된 비틀린 대각선은 $m\mid u^2-1$ 일 때만 함자적으로 일관된다.

**기저변환 사상.** $\beta:R^G\otimes_RR'\to R'^G$, $\varphi\otimes r'\mapsto r'\cdot f\circ\varphi$.

**정리 6 [증명].**
(a) $\Delta$ : 모든 $f$ 에 대해 $\beta$ 는 동형 ($R^G=R^{\pi_0}$, 자유).
(b) $\Delta^-$ : $\beta$ 는 $R'^b\oplus(R[2]\otimes R')^{c-b}\to R'^b\oplus R'[2]^{c-b}$ 이고 첫 성분은 동형이다. $G$ 가 비이분 성분을 가질 때 ($c>b$) $\beta$ 가 동형 $\iff$ $\beta_2:R[2]\otimes R'\to R'[2]$ ($r\otimes r'\mapsto r'f(r)$) 가 동형. 충분조건: $R'$ 가 $R$ 위 평탄 ($0\to R[2]\to R\xrightarrow{2}R$ 정확열에 $\otimes R'$ 하면 $R[2]\otimes R'=\ker(2:R'\to R')$).
(c) $\Delta_I\to\Delta_{I'}$ ($f(I)\subset I'$): $K_2$ 에서 $R^G=S\cong R\oplus I$, $\beta=\mathrm{id}_{R'}\oplus(I\otimes R'\to I')$. 동형 $\iff I\otimes_RR'\to I'$ 동형.
증명. 정리 3, 4 와 $\otimes$ 의 가법성. $\square$

**구체 계산 (깨지는 예) [증명]+[계산 확인].**
1. $\mathbb Z\to\mathbb Z/2$, 규칙 $x+y=0$, $G=K_3$: $\mathbb Z^G=0$ ($\mathbb Z[2]=0$), $0\otimes\mathbb Z/2=0$. 그러나 $(\mathbb Z/2)^{K_3}=\{000,111\}$. $\beta$ 는 단사이나 **전사가 아니다**. 이유: 비평탄 ($\mathbb Z/2$ 는 $\mathbb Z$ 위 평탄하지 않음), $R[2]\otimes R'=0\to R'[2]=\mathbb Z/2$.
2. $\mathbb Z/4\to\mathbb Z/2$, $x+y=0$, $G=K_3$: $R^G=\{000,222\}\cong\mathbb Z/2$, $R^G\otimes\mathbb Z/2\cong\mathbb Z/2$ (생성원 $222\otimes1$), $\beta(222\otimes1)=222\bmod2=000$. 그러므로 $\beta=0:\mathbb Z/2\to\mathbb Z/2=\{000,111\}$, **단사도 전사도 아니다**. 이 예는 $R[2]\otimes R'$ 와 $R'[2]$ 의 크기가 같은데도 사상이 동형이 아닐 수 있음을 보인다.
3. $\mathbb Z\to\mathbb Z/4$, 규칙 $x\equiv y\ (2)$ ($I=2\mathbb Z\mapsto I'=2\mathbb Z/4$), $G=K_2$: $\mathbb Z^G=S=\langle(1,1),(0,2)\rangle\cong\mathbb Z^2$, $\otimes\mathbb Z/4=(\mathbb Z/4)^2$ (위수 16), $(\mathbb Z/4)^G=\{x\equiv y\ (2)\}$ 위수 8. $\beta$ 는 전사이나 단사가 아니다: $(0,2)\otimes2\mapsto(0,4)=0$. ($I\otimes R'=\mathbb Z/4\to I'\cong\mathbb Z/2$ 이므로.)
4. 성공 예: $\mathbb Z\to\mathbb Q$, $x+y=0$: $0\to0$ ✓ (평탄). $\mathbb Z/9\to\mathbb Z/3$, $x+y=0$: $R[2]=0=R'[2]$ ✓.
5. 공변성 조건 $(f\times f)(S_R)\subset S_{R'}$ 가 깨지는 예: $f:\mathbb Z\to\mathbb Z/4$, $S_R=\{y\equiv3x\ (8)\}$, $S_{R'}=\Delta^-_{(0)}$ ($y=-x$) 는 $3\equiv-1\pmod4$ 이므로 성립하나, $S_{R'}=\Delta$ ($y=x$) 로 읽으면 $(1,3)\mapsto(1,3)\notin\Delta$ 로 실패. 즉 규칙의 짝짓기를 정수형으로 고정해야 한다.

### 6. 판정 (임무 4): 환 확장이 무방향 규칙의 정보 빈약함을 해소하는가

**정리 7 [증명] (아니오).** 임의의 가환환 $R$ 과 임의의 대칭 부분가군 $S\subset R^2$ 에 대해 $R$-가군 $\mathrm{Hom}_S(G,R)$ 의 동형류는 $G$ 의 다음 자료만으로 결정된다: $i$ (고립점 수), 간선 있는 각 성분의 $(n_C,\ \text{이분 여부})$. 특히 $C_6$, $K_{3,3}$, $P_6$ (모두 연결·이분·정점 6개) 는 **모든 환·모든 무방향 가군 규칙에서** 동형인 $R^G$ 를 준다.
증명. 정리 3 에서 직접. $\square$ 
[계산 확인] $\mathbb Z/4,\mathbb Z/6,\mathbb Z/8$ 의 모든 대칭 규칙에서 $C_6,K_{3,3},P_6$ 의 $\mathrm{Hom}$ 의 위수 분포가 같음.

**원인 (구조적).** 정리 5 에 의해 $\Gamma_S(R)$ 는 "완전이분 $\sqcup$ 루프 클리크 $\sqcup$ 고립점" 이다. 이런 목표 그래프로의 호모는 성분의 크기·이분성만 센다. 즉 부분가군 조건이 목표를 **단순한 그래프**로 강제하며, 환을 키워도 $K_{|I|,|I|}$ 의 크기 $|I|$ 와 $|M|$ 이 달라질 뿐 목표의 모양이 같다. 일반 그래프 $\Gamma$ 로의 호모 수는 $G$ 를 동형류까지 결정한다는 Lovász 정리 [기억-미검증]가 있어도 이는 $\Gamma$ 를 모든 그래프에서 움직일 때의 이야기이고, 단일 $\Gamma=\Gamma_S(R)$ 로는 위 한계가 있다.

**환 확장이 실제로 주는 것 (해소된 부분).**
1. **char 2 붕괴의 해소.** $\mathbb Z/4$ 등에서는 한 규칙 $x+y=0$ 이 $b$ 와 $c$ 를 모두 준다 (정리 4). 체에서는 $\Delta$ 와 $\Delta^-$ 를 곱 $G\times K_2$ 로 결합해야 얻던 정보였다 (R1 정리 C).
2. **정수 위 평탄성 실패의 정량화.** $R[2]\otimes R'\to R'[2]$ 의 실패가 기저변환 실패의 전부다 (정리 6).
3. **구조의 풍부함.** $I\ne0$ 인 합동 규칙에서는 $R^G$ 에 비틀림 $I^{n_C-1}$ 이 나타나 $n_C$ (성분 크기)를 가군 구조로 읽는다. 체에서는 성분 크기가 안 보였다 ($\dim=1$).
이 셋 모두 여전히 **성분 통계** $(i,\{(n_C,\text{이분})\})$ 안에서다. 국소 구조(사이클 길이, 차수, 지름)는 못 본다.

**무엇이 정보를 줄 수 있는가 [추측/증명 혼합].** (i) 방향이 있는 규칙: 일반 Goursat $(I,J,I',J',\theta:J/I\xrightarrow{\sim}J'/I')$ 에서 $\Gamma$ 는 방향 완전이분 호의 분리합이고, 닫힌 걷기의 감김수 $\omega(C)$ 와 $\theta$ 의 위수가 정보 [증명 스케치: 정리 2 와 같은 증명, 비대칭 사영]. 이는 R1 의 이득그래프 정보이며 $C_6$ vs $K_{3,3}$ 는 방향이 주어지면 구분이 가능한지가 별개 문제 (researcher2 영역). (ii) 부분가군이 아닌 대칭 부분집합 (예: $\mathbb Z/n$ 위 Cayley 그래프의 연결집합) 은 $\mathrm{Hom}$ 이 가군이 아니게 되나 $|\mathrm{Hom}|$ 은 풍부한 불변량 (Lovász 유형) [기억-미검증]. 즉 "가군이라는 구조"와 "정보량" 은 상충하며, 문주님의 가군 정의가 정보를 막는 정확한 원인이다 [증명: 정리 5 가 이를 부분가군 ⟹ 단순 목표로 요약].

### 7. 증명 시도에서 막힌 곳 (장애물)

1. **비순환 $J/I$ 의 $\theta^2=1$ 완전 열거.** 정리 2 는 분류를 삼조로 정확히 주지만, 임의의 가환환에서 $\{\theta\in\mathrm{Aut}_R(M):\theta^2=1\}$ 의 개수 공식은 $M$ 의 구조에 의존한다 ($\mathbb Z/2^m$ 의 $m\ge3$ 이 4, $m=2$ 가 2 등은 순환일 때만 다룸). $M=\mathbb Z/2^a\oplus\mathbb Z/2^b$ 등에서 이 수의 닫힌 식은 미완.
2. **정리 3 의 자연성.** 동형 $\mathrm{Hom}_C\cong S\oplus I^{n_C-2}$ 는 뿌리·간선 선택에 의존한다. 그래프 사상 $f:G\to H$ 에 대한 $f^*$ 의 행렬을 이 분해로 쓴 공식은 하지 않았다 (R1 의 $\Delta^-$ 의 $f^*$ 랭크 공식을 환에서 어떻게 일반화하나).
3. **Aut 표현.** $\mathrm{Aut}(G)$ 가 $R^G$ 에 작용할 때 비이분 성분에서는 상수함수 $R[2]$ 위에 자명하게 작용하는데 이분 성분에서는 부호 지표 $\varepsilon(\sigma)=\pm1$ ($R1$ 6절). 환에서 $\theta\ne\pm1$ 일 때 지표 $\theta^{\varepsilon}$ 가 어떻게 되는지($\theta$ 의 위수 2 조건에서 $\theta^{\pm1}=\theta$) 는 미작성.

## 문주님께 요청

없음. (선택) 규칙을 가군 조건에서 풀어 "대칭 부분집합 $\Gamma\subset R\times R$" 을 허용할지(정리 7 의 마지막 문단: 가군이면 정보가 성분 통계로 갇힘)에 대한 결정은 R3 이후 방향 설정에 도움이 된다. 긴급도 낮음, 없을 때의 대안: 가군 정의 그대로 유지.

## 후속연구 지점

1. **우선순위 1: 방향 있는 환 규칙 (비대칭 Goursat) 에서 $R^G$ 의 구조정리.** 무엇을: $S=S(I,J,I',J',\theta)$, $\theta:J/I\to J'/I'$ 에서 정리 3 의 방향 판. 감김수 $\omega(C)$ 와 $\theta$ 의 위수로 $R^G$ 를 쓰기, 특히 $R=\mathbb Z/N$ 에서 $A_G$ 와의 관계 (researcher2·3 의 정수 이득 규칙과 연결). 왜: 무방향은 정리 7 로 닫혔고 정보는 방향/이득 쪽에 있음. 시작: 정리 2 의 증명에서 대칭 사용을 지우고 $\pi_2(S)=J'$ 로 일반화, 방향 사이클 $\vec C_n$ 에서 $\theta^n=\mathrm{id}$ 조건을 닫힌 걷기마다 적기. 난점: $\theta$ 가 순환이 아닐 때 $\theta^k=1$ 조건의 해가 가군 $M[\theta^k-1]$ 로 일반화되어 정리 4 의 $R[2]$ 가 $M[\theta^{\omega}-1]$ 로 바뀜.
2. **우선순위 2: 정리 3 의 자연성 ($f^*$ 의 행렬)과 함자 $G\mapsto R^G_S$ 의 완전 불변량.** 무엇을: $f:G\to H$ 에 대해 $f^*:R^H\to R^G$ 를 분해 $S\oplus I^{n_C-2}$ 로 쓰기, 그래프 범주에서 $G\mapsto R^G$ 의 동형류를 결정하는 자료(성분 통계)를 정리 7 의 함자 판으로 확인. 왜: $C_6$ vs $K_{3,3}$ 가 객체 수준에서 못 구분되는 것은 증명됐으나, 사상(예: $C_6\to K_{3,3}$ 의 호모 개수)까지 보면 구분되는지 판단. 시작: Yoneda 관점에서 $\Gamma_S(R)$ 를 고정한 함자 $\mathrm{Hom}(-,\Gamma)$ 의 자연변환군. 난점: 자연성 계산이 뿌리 선택에 의존.
3. **우선순위 3: 합동 규칙의 $I$-진 필터와 정수 위 극한.** 무엇을: $\mathbb Z/p^k$ 와 $k\to\infty$ ($\mathbb Z_p$, $\mathbb Z$) 에서 $\Delta^-_{p^j}$, $S_{u,p^j}$ 가 정수형 규칙의 사영극한과 어떻게 이어지는지; $R^G$ 의 $2$-진 비틀림 $R[2]$ 가 $R=\mathbb Z/2^k$ 에서 항상 $\mathbb Z/2$ 임을 이용해 $k$ 에 관한 극한이 정수 위 $b$ 만 남기는지. 왜: 정리 4 의 $b,c$ 읽기와 정수 위 평탄성 실패의 극한 이해. 시작: $\mathbb Z/2^{k+1}\to\mathbb Z/2^k$ 에서 정리 6(b) 의 $\beta_2$ 계산. 난점: 반사영계 $\varprojlim^1$ 처리.
4. **우선순위 4: 비순환 $J/I$ 와 스칼라 아닌 $\theta$ 의 예제 확대.** 무엇을: $R=F[x,y]/\mathfrak m^2$, $\mathbb Z/4\times\mathbb Z/2$ 위의 $M$ 에서 $\theta$ 의 비스칼라 예를 모두 열거하고 정리 3 의 $J_\theta$ 가 $\theta$ 의 고유가군으로 어떻게 쪼개지는지 ($2$ 가 가역이면 $M_+\oplus M_-$). 왜: 정리 2 의 (d)항이 실제로 새로운 $R^G$ 구조를 주는지 점검. 난점: 가환환에서 비스칼라 $\theta$ 의 예는 비반단순 가군에서만 의미 있음.
5. **우선순위 5: 이분 이중덮개 정리 C 의 환 일반화.** 무엇을: $R^{G\times K_2}_\Delta$ 와 $R^G_\Delta\oplus R^G_{\Delta^-}$ 의 관계를 $2$ 가 가역이 아닐 때 (분해가 깨지므로 정확열) 로 정리하기. 왜: 정리 4 의 $b,c$ 정보와 $G\times K_2$ 의 $c+b$ 가 환에서 어떻게 만나는지. 시작: $R=\mathbb Z/4$, $K_3\times K_2=C_6$ 에서 $\psi_\pm=\psi(\cdot,0)\pm\psi(\cdot,1)$ 의 상 계산. 난점: $\tfrac12$ 불가능.
