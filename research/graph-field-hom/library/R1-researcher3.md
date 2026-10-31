# [R1-researcher3] 퇴화 규칙·정수 계수 족·함자성 종합·k항 일반화·종합 의견

- 작성자·라운드·역할: researcher3 / R1 / 포메이션 I 분담 — 퇴화·일반 규칙, 정수 계수 족, 함자성. 수신: 대수검존
- 코드·계산: `rooms/researcher3/snf.py`, `lap.py` (sympy 없음, 정수 스미스 꼴을 직접 구현)

## 요약
1. 예비 정리 6 은 맞다 [증명]. 퇴화 규칙은 방향 그래프에서만 의미가 있다(무방향이면 비고립 정점이 모두 0). 정정 한 가지: 해석 (b) 에서는 $\ker B^TB \supsetneq \ker B$ 가 char $p$ 에서 생길 수 있다.
2. **핵심 도구 (새로운 정리)**: 정수 규칙 $R_{a,b}$ 에서 $F^G=\mathrm{Hom}_{\mathbb Z}(A_G,F)$, $A_G=\mathbb Z^V/\langle a\,u+b\,v : u\to v\rangle$ (유한생성 아벨군). 따라서 $\dim_{F}F^G=\mathrm{rank}\,A_G+\#\{\text{비틀림 불변인자 중 }\mathrm{char}F\text{ 의 배수}\}$ 이고, 체 사상 공변성·확대 불변성이 자동으로 나온다. 예비 정리 7 은 맞다(더 강하게: $F^G\otimes_F F'\cong F'^G$).
3. 모든 체에서 함자적인 직선 규칙은 "표수마다 소체 위의 점"으로 정해진 것뿐이며, 특성 사이에서 일관된(하나의 공식인) 것이 정확히 정수 계수 $[a:b]\in\mathbb P^1(\mathbb Q)$ 족이다 [증명].
4. 종합 의견: 규칙 하나를 고르라면 **방향 + 정수 이득 $\lambda=-a/b$ (예 $-2x+y=0$)** 과 *표수를 바꿔 읽는 것*, 그리고 불변량으로는 **해석 (b) 의 $\ker B^TB$ (라플라시안형)** 이 가장 풍부하다. 무방향 그래프에서는 직선 규칙의 $\dim\ker B$ 가 모두 약하다(§E).

---

## 본문

### 0. 공통 설정과 표기
방향 그래프(다중간선·루프 허용) $G=(V,E)$, 간선 $e:u\to v$. 규칙 $R\subset F^2$ 에 대해 $\mathrm{Hom}_R(G,F)=\{\varphi:V\to F\mid(\varphi(u),\varphi(v))\in R\ \forall (u\to v)\}$. 무방향 간선은 두 방향 호를 모두 가진 것으로 보면 $R\cap R^{T}$ 가 규칙이다(루프는 $\varphi(v)\in$ 대각선 $\cap R$). 정수 규칙은 $B=B_{a,b}$ (간선×정점, 행 $=a\,e_u+b\,e_v$). 직선은 $[a:b]$ 로 정해지며 $R_{a,b}$ 의 방향벡터는 $(b,-a)$. 이득 $\lambda:=-a/b$ (arc $u\to v$ 는 $\varphi(v)=\lambda\varphi(u)$). 기존 규칙은 $(a,b)=(1,1)$, $\lambda=-1$; $(1,-1)$ 은 $\lambda=1$ ($\varphi(u)=\varphi(v)$); $a=0$ 은 $\varphi(\text{head})=0$; $b=0$ 은 $\varphi(\text{tail})=0$.

### A. 퇴화 규칙 $\lambda=0$ ($R=\langle(1,0)\rangle$), $\lambda=\infty$ ($R=\langle(0,1)\rangle$)

**정리 A1** [증명] $R=\langle(1,0)\rangle=\{(x,0)\}$. 호 $u\to v$ 는 정확히 $\varphi(v)=0$ 을 요구하고 $\varphi(u)$ 에는 제약이 없다. 따라서 $F^G=\{\varphi:\ \varphi|_{\mathrm{Head}(G)}=0\}\cong F^{S(G)}$, $S(G)$ = 들어오는 호가 없는(입차수 0) 정점의 집합, 곧 $\dim F^G=|S(G)|$. 루프 $v\to v$ 는 $v$ 를 head 로 만들어 $\varphi(v)=0$ 을 강제한다(입차수 $\ge1$). 다중호는 효과 없음. $R=\langle(0,1)\rangle$ 는 $G$ 를 역방향으로 바꾼 것: $\dim=$ 출차수 0 인 정점(싱크) 수. **예비 정리 6 확인, 정정 없음.**

**무방향에서 무의미**: 무방향은 두 방향을 모두 가지므로 모든 비고립 정점이 head 가 되어 $\dim=$ 고립점 수. 대칭 직선이 되는 것은 $\lambda^2=1$ (예비 정리 2)뿐이므로 $\lambda=0,\infty$ 는 방향 그래프 전용이다 [증명].

**랭크·당김** [증명] $\mathrm{rank}\,B=\#\mathrm{Head}(G)=n-|S(G)|$ (서로 다른 head 마다 단위행). 호모 $f:G\to H$ (방향 보존)에서 $f^*\psi=\psi\circ f$, $F^H=F^{S(H)}$:
- $f^*$ 단사 $\iff S(H)\subset f(V(G))$ (모든 소스가 상에 들어 있음). ($\psi$ 가 $S(H)$ 에 지지되므로 $\psi\circ f=0\Rightarrow\psi|_{f(V)\cap S(H)}=0$.)
- $f^*$ 전사 $\iff$ $G$ 의 모든 소스 $s$ 에 대해 $f(s)\in S(H)$ 이고 $f^{-1}(f(s))=\{s\}$. (상 $=\mathrm{span}\{1_{f^{-1}(h)}:h\in S(H)\}$ 이고 $f^{-1}(S(H))\subset S(G)$ 가 자동.) 
- 차원 $|S|$ 가 개수만 보므로 풍부하지 않다: 방향 사이클·방향 경로의 구분은 소스 수 0 vs 1 뿐.

**고유벡터 (a)** $\mathrm{Aut}(G)$ 는 $F^G=F^{S(G)}$ 에 **소스들 위의 치환표현**으로 작용한다. 궤도 크기 $m$ 인 순환 작용은 $\mathrm{char}\nmid m$ 이고 $\mu_m\subset F$ 이면 고유값 $\zeta\in\mu_m$ 각각 한 번씩(푸리에). 고유벡터가 궤도 위의 문자 $(\zeta^i)$. 사이클·경로 대칭은 소스 위에서만 보인다(예: 소스 $s_1,\dots,s_m\to v$ 별모양 의 $S_m$ 대칭: 표준표현 + 자명표현).

**고유벡터 (b)** $B^TB=\mathrm{diag}(\mathrm{indeg}(v))$ (각 행 $=e_{head}$). 특성다항식 $\prod_v(x-\mathrm{indeg}(v))$, 최소다항식 $\prod_{d\in\{\mathrm{indeg}\bmod p\}}(x-d)$ — 항상 대각화 가능. $\ker B^TB=\{$ indeg $\equiv0\bmod p$ 인 정점 위 지지 $\}\supseteq\ker B$. **정정 포인트** [증명]: char $p>0$ 에서 입차수가 $p$ 의 양의 배수인 정점이 있으면 $\ker B^TB\supsetneq\ker B$ (예: 소스 3 개 $\to v$, $p=3$: $\ker B$ 차원 3, $\ker B^TB$ 차원 4). 따라서 (b) 에서 "$F^G=\ker B^TB$" 는 char 0 (또는 입차수가 $p$ 로 안 나뉠 때)만 성립; 일반 체에서 $F^G=\ker B\subseteq\ker B^TB$ — 유한체에서 $B^TB$ 는 정부호가 아니다.

### B. 정수 계수 족 $R_{a,b}$

**B0. 정규화** [증명] $g=\gcd(a,b)$ 이면 $R_{a,b}$ 는 $\mathrm{char}\nmid g$ 일 때 $R_{a/g,b/g}$, $\mathrm{char}\mid g$ 일 때 $F^2$. 즉 비서로소 쌍은 "표수 $\mid g$ 에서 규칙이 사라지는" 다른 규칙이므로 이하 $\gcd(a,b)=1$. 그러면 임의의 표수 $p$ 에서 $(a,b)\bmod p\ne(0,0)$ 이므로 $R_{a,b}$ 는 항상 *직선*이고(표수를 가리지 않고 직선 규칙이 정의되고 일관된다):
- $p\nmid ab$: 이득 $\lambda_p=-a/b\in\mathbb F_p^\times$;
- $p\mid a$: $\lambda=0$ (head $=0$);  $p\mid b$: $\lambda=\infty$ (tail $=0$);
- 표수 0: $a,b\ne0$ 이면 $\lambda\in\mathbb Q^\times$.
**퇴화는 소수 $p\mid ab$ 에서 일어나며**, 그곳에서 규칙이 A 절의 퇴화형으로 바뀐다.

**B1. 이득 그래프 차원 공식 (예비 정리 5 의 정수판, 증명 포함)** $\lambda\in F^\times$ 일 때 연결성분 $c$ 의 닫힌 걷기 $w$ 에 순수 지수 $n(w)=\#\text{정방향 호}-\#\text{역방향 호}$ 를 준다. $\varphi(\text{끝})=\lambda^{n(w)}\varphi(\text{시작})$ 이므로 닫힌 걷기에서 $\varphi(r)(1-\lambda^{n(w)})=0$. 
정의: $d_c:=\gcd\{n(w)\}$ = 사상 $\varepsilon:H_1(c;\mathbb Z)\to\mathbb Z$, $z\mapsto\sum_e z_e$ ($z_e$ 는 호 방향 기준 계수)의 상의 생성원($\ge0$, 나무면 $0$; 루프 하나가 있으면 $n=1$ 이라 $d_c=1$). $n$ 은 걷기 연결과 역걷기에 대해 가법이므로 닫힌 걷기 전체의 $n$ 값 집합은 부분군 $d_c\mathbb Z$ 다.
**정리 B1** [증명] $\lambda\in F^\times$ 이면 $\dim F^G=\#\{c:\ \lambda^{d_c}=1\}=\#\{c:\ \mathrm{ord}_F(\lambda)\mid d_c\}$ ($\mathrm{ord}=\infty$ 이면 $d_c=0$ 인 성분만; $d_c=0$ 은 항상 통과).
증명: 성분마다 $\varphi(r)=t$ 로 두면 임의 경로의 $\varphi(v)=\lambda^{n(\text{경로})}t$ 가 유일한 후보이고, 경로 선택에 무관할 필요충분조건이 모든 닫힌 걷기에서 $\lambda^{n}=1$ 이다. 그렇지 않으면 $t=0$ 이고 $\lambda$ 가 가역이므로 $\varphi\equiv0$ 이다. ∎ (researcher2 의 담당과 동일한 내용이라 증명은 간략히; 아래는 *정수성* 의 귀결.)

**정수 계수에서의 귀결** [증명] 표수 0 에서 $\lambda\in\mathbb Q^\times$ 의 위수는 $\lambda=1$ 이면 $1$, $\lambda=-1$ 이면 $2$, 그 외 $\infty$. 곧 표수 0 에서 정수 규칙은 **3 종류뿐** ($\lambda=1$: 성분 수; $\lambda=-1$ 기존 규칙: $d_c$ 짝수인 성분 수 — 무방향이면 이분 성분 수; 그 외: $d_c=0$ 인 성분 수 = "$\varepsilon\equiv0$" 인 성분). 표수 $p$ 에서는 $\lambda_p\in\mathbb F_p^\times$ 의 위수가 $p-1$ 의 임의 약수일 수 있다. $\lambda=-a/b$ 에서 $\lambda^d=1\iff p\mid(-a)^d-b^d$.
**유한 예외 소수** [증명]: $d_c\neq0$ 인 성분만 문제이므로 $\dim_{\mathbb F_p}F^G=\dim_{\mathbb Q}F^G$ 가 아닌 소수는 $\{p\mid ab\}\cup\{p\mid (-a)^{d_c}-b^{d_c},\ d_c\ne0\}$ 에 포함된다(유한 집합).

**B2. 보편 표현: $A_G$** [증명] 각 아벨군 $A$ 에 대해 $U(A)$ = 정점 집합 $A$, 호 $x\to y\iff ax+by=0$ 인 방향 그래프로 둔다. 그러면 
$$\mathrm{Hom}_{\mathrm{DiGraph}}(G,U(A))=\mathrm{Hom}_{\mathrm{Ab}}(A_G,A),\qquad A_G:=\mathbb Z^V\Big/\big\langle a\,u+b\,v:\ (u\to v)\in E\big\rangle=\mathrm{coker}(B^T).$$
(정점 $\mapsto$ 원소 대응, 관계가 정확히 호 조건.) $F^G=\mathrm{Hom}_{\mathbb Z}(A_G,F)=(A_G\otimes F)^\vee$. 스미스 꼴 $A_G\cong\mathbb Z^r\oplus\bigoplus_i\mathbb Z/d_i$ 로부터 
$$\boxed{\dim_F F^G=r+\#\{i:\ \mathrm{char}F\mid d_i\}\ (\mathrm{char}F=p>0),\qquad=r\ (\mathrm{char}F=0).}$$
따라서 **char 의존성 = $A_G$ 의 비틀림**. 이 틀로 이전 결과가 재해석된다:
- 기존 규칙 $(1,1)$: $A_G=\mathbb Z^{\#\text{이분 성분}}\oplus(\mathbb Z/2)^{\#\text{비이분 성분}}$ (비이분: $u=-v$ 와 홀수 닫힌 걷기가 $2u=0$ 을 주고 모든 정점이 $\pm u=u$). 그러므로 $\mathrm{char}\ne2$: 이분 성분 수, char 2: 전체 성분 수. 예비 정리 3 의 독립 확인 [증명]. 비틀림이 $\mathbb Z/2$ 하나라서 소수는 2 뿐.
- $\lambda=1$ $(1,-1)$: $A_G=\mathbb Z^{\#\text{성분}}$ (무비틀림): 모든 체에서 같음.
- 퇴화 $(0,1)$: $A_G=\mathbb Z^{S(G)}$ 무비틀림: 모든 체에서 $|S(G)|$.
- 방향 사이클 $C_n^{\to}$: $B$ 는 순환행렬 $aI+bP$, $\det=a^n-(-b)^n$, 스미스 꼴은 $A_{C_n}\cong\mathbb Z/(a^n-(-b)^n)$ ($\gcd(a,b)=1$) [계산 확인: $(a,b)\in\{(-2,1),(3,2),(1,1),(-3,1)\}$, $n\le4$ 일치; 증명은 아래]. 이때 $F^{C_n}\ne0\iff\mathrm{char}F\mid a^n-(-b)^n$ ($\lambda^n=1$ 과 동치: $a^n=(-b)^n\iff(-a/b)^n=1$ — $a,b$ 가 서로소이므로 정수 상 $\gcd$ 논증 포함).
  *증명 개요* [증명 스케치]: $A=\langle x_1..x_n\mid a x_i+b x_{i+1}=0\rangle$; $\gcd(a,b)=1$ 이므로 $s a+t b=1$ 로 $x_i$ 를 $x_{i+1}$ 와 한 개의 순환 생성원 $y$ 로 묶어 $A$ 가 순환군임을 보이고 위수는 $\det$ 의 절댓값. 순환성 부분은 다듬지 못했다(계산으로만 확인; 아래 후속연구 2).
- **트리에서도 비틀림이 생기는 예** [계산 확인 + 증명]: $(a,b)=(-2,1)$ ($\varphi(v)=2\varphi(u)$), 호 $0\to2,\ 1\to2$ (V자). $A_G=\langle x_0,x_1,x_2\mid x_2=2x_0=2x_1\rangle\cong\mathbb Z\oplus\mathbb Z/2$ (스미스 꼴 $[2]$, $\mathbb Q$-영공간 차원 1). 따라서 $\dim_{\mathbb Q}=1$, $\dim_{\mathbb F_2}=2$, $\dim_{\mathbb F_3}=\dim_{\mathbb F_5}=1$ (계산 일치). 소수 2 는 $p\mid a$ 의 퇴화 소수다 — 방향이 섞인 트리($\lambda\ne\pm1$)에서는 역방향 호가 $\lambda^{-1}$ 을 요구하여 $p\mid a$ 에서 정수 구조가 깨진다. 즉 **트리조차 "균형"이라는 판단이 표수 의존**.

**B3. 체 사상에 대한 공변성 (예비 정리 7 의 증명)** [증명] 체 사상 $\sigma:F\to F'$ 은 단위 보존 환사상이므로 정수에 대해 $\sigma(n\cdot1)=n\cdot1$ (소체 위의 항등). $(x,y)\in R_{a,b}(F)\Rightarrow a\sigma(x)+b\sigma(y)=\sigma(ax+by)=0$. 그러므로 $\sigma\times\sigma(R_F)\subset R_{F'}$, $\sigma_*\varphi:=\sigma\circ\varphi\in F'^G$. 이 사상은 $\sigma$-반선형이며 $F'$-선형 확장 $F^G\otimes_{F,\sigma}F'\to F'^G$ 이 **동형**: $B_{F'}=B_F\otimes_FF'$ 이고 $F'$ 는 $F$ 위 평탄(자유)하므로 $\ker$ 이 기저확장과 교환 [증명]. 곧 **$\dim_F F^G$ 는 표수에만 의존한다** (체의 크기·확대 차수에 무관). 공변함자 $(-)^G:\mathbf{Field}\to\mathbf{Set}$ 은 $\mathrm{Hom}_{\mathbb Z}(A_G,-)$ 의 제한이므로 자동 (B2).

**B4. "정수 계수 족에서만 일관된 함자인가?" 판정** [증명]
*주장.* 각 체 $F$ 에 직선 $R_F\subset F^2$ 를 대응시키는 규칙이 모든 체 사상 $\sigma$ 에 대해 $(\sigma\times\sigma)(R_F)\subset R_{F'}$ 를 만족한다(= $(-)^G$ 가 $\mathbf{Field}$ 전체에서 함자) $\iff$ $R_F=F\cdot\rho_{P(F)}$, 곧 $R_F$ 는 $F$ 의 소체 $P(F)$ 위에서 정의된 직선 $\rho_{P}\in\mathbb P^1(P)$ 의 확대. 
*증명.* ($\Leftarrow$) 위와 같다. ($\Rightarrow$) 포함 $\iota:P(F)\to F$ 에 대해 $\iota(R_P)\subset R_F$; 둘 다 직선이므로 $F\cdot R_P=R_F$. ∎ 
따라서 모든 체에서 함자적인 직선 규칙 족은 *표수마다 소체 위의 점* $\rho_0\in\mathbb P^1(\mathbb Q)$, $\rho_p\in\mathbb P^1(\mathbb F_p)$ (각각 독립 선택)이다. 이 중 **표수 사이에서 일관된**(= 하나의 공식이 모든 표수에서 같은 직선을 줌, $\rho_p=\rho_0\bmod p$ 이 모든 $p$ 에서) 규칙이 정확히 정수 계수 $[a:b]$ ($\gcd=1$) 이다. 반면 $\lambda\in F$ 를 "임의의 체 원소"로 두는 규칙 ($\lambda$ 가 $F$ 의 초월원소 등)은 짝 $(F,\lambda)$ 의 범주에서만 함자이며 $\sigma(\lambda)=\lambda'$ 를 요구한다. **결론**: 정수 계수 족 = 함자성이 전 체 범주에서 성립하고, *더 나아가* 환원 $\mathbb Z\to\mathbb F_p$ 와 호환(= $A_G$ 라는 하나의 아벨군이 모든 체의 $F^G$ 를 만든다)하는 유일한 족이다. 이것이 정수 족을 쓰는 이유다.

### C. 함자성 종합

1. **반변 $F^{(-)}$** [증명] 호모 $f:G\to H$ 에 대해 $f^*\psi=\psi\circ f$ 는 임의 규칙 $R$ 에서 잘 정의되고(호가 호로 가므로), $R$ 이 부분공간이면 $F$-선형; $(g f)^*=f^*g^*$, $\mathrm{id}^*=\mathrm{id}$.
2. **공변 $(-)^G$**: 정수 규칙에서 B3. 임의 규칙에서는 $\sigma^{\times2}(R_F)\subset R_{F'}$ 가 필요충분(⇐ 같고, ⇒ $G=K_2$ 이면 $F^G=R_F$).
3. **쌍함자성** [증명] 자연성 정사각형 $(\sigma\circ-)\circ f^*=f^*\circ(\sigma\circ-)$ 은 $\sigma\circ\psi\circ f$ 로 자명. 둘을 합쳐 $\mathbf{DiGraph}^{op}\times\mathbf{Field}\to\mathbf{Set}$, $(G,F)\mapsto F^G=\mathrm{Hom}(G,\mathbb F_R)$ (반변-공변 쌍함자).
4. **분리합** [증명] $F^{G\sqcup H}\cong F^G\times F^H$ (호모는 성분마다 독립). 더 일반으로 $F^{(-)}=\mathrm{Hom}(-,\mathbb F_R)$ 는 표현가능이므로 모든 쌍대극한을 극한으로 보낸다(분리합 → 곱, 몫(정점 합치기)·접착 → 올곱). 공집합 그래프: $F^\emptyset=0$. $\dim$ 가법.
5. **표현가능성** [증명] (i) 방향 그래프 범주에서 $F^G=\mathrm{Hom}(G,\mathbb F_R)$, $\mathbb F_R=(F,R)$. $R$ 이 부분군이면 $\mathbb F_R$ 은 범주적 곱(텐서 아닌 데카르트 곱: 호 $\iff$ 두 성분 모두 호)에 대한 **아벨군 대상**이다(덧셈이 $\mathbb F_R\times\mathbb F_R\to\mathbb F_R$ 호모 $\iff$ $R+R\subset R$); 스칼라곱이 호모 $\iff$ $R$ 이 부분공간(예비 정리 1 의 범주적 해석). (ii) 정수 규칙이면 B2 의 수반 $A_{(-)}\dashv U$: $F^G=\mathrm{Hom}_{\mathrm{Ab}}(A_G,F)$.
6. **당김의 단사/전사** [증명] $f^*=\mathrm{Hom}(f_*,F)=(f_*\otimes F)^\vee$ (정수 규칙). 유한차원 쌍대는 정확하므로: $f^*$ 단사 $\iff f_*\otimes F:A_G\otimes F\to A_H\otimes F$ 가 전사; $f^*$ 전사 $\iff f_*\otimes F$ 단사. 특히 $f$ 가 정점 전사이면 $f_*$ 전사이므로 *모든 체·모든 정수 규칙에서 $f^*$ 단사*. (역은 거짓: A 절의 소스 조건이 반례를 줌.) 포함 $G\hookrightarrow H$ 에 대한 제한 사상 $F^H\to F^G$ 의 전사성은 $A_G\to A_H$ 의 $\otimes F$ 단사성(= $G$ 의 관계가 $H$ 에서 새 관계를 만들지 않음)이다.
7. **곱 구조** [증명] 데카르트 곱 $G\times H$ 에서 점별곱 $(g,h)\mapsto\varphi(g)\psi(h)$ 가 호모가 되려면 $R\cdot R\subset R$ (성분별곱) 필요. 직선 $\langle(1,\lambda)\rangle$ 에서는 $\lambda xx'\overset{!}{=}\lambda^2xx'\iff\lambda\in\{0,1\}$ (그리고 $\infty$). 즉 $\lambda=0,1,\infty$ 에서 $F^G$ 는 점별곱에 대해 $F$-대수이고 $F^G\otimes F^H\to F^{G\times H}$ 가 자연 사상이다. $\lambda=-1$ 에서는 "홀수 함수 × 홀수 함수 = 짝수 함수": $F^G_{(-1)}\otimes F^H_{(-1)}\to F^{G\times H}_{(+1)}$ (대칭군 $\mathbb Z/2$-등급 구조). 기존 규칙이 *대수가 아님*은 이 점이 약점이자 특색.

### D. $R\subset F^k$ (초그래프) 로의 일반화
방향·순서가 있는 $k$-항 간선 $(v_1,\dots,v_k)$ 를 가진 초그래프 $H$, $\mathrm{Hom}_R(H,F)=\{\varphi:V\to F:(\varphi(v_1),\dots,\varphi(v_k))\in R\ \forall\text{간선}\}$.
**정리 D1** [증명] 모든 초그래프에서 $\mathrm{Hom}_R(H,F)$ 가 $F^V$ 의 $F$-부분공간 $\iff$ $R$ 이 $F$-부분공간. (⇐) 간선마다 선형사상 $F^V\to F^k$ (정점 중복이면 대각 삽입 $\delta_\pi$) 로의 $R$ 의 역상이므로 부분공간의 교집합. (⇒) 서로 다른 $k$ 정점으로 된 간선 하나만 있는 초그래프의 Hom $=R$. ∎ ($k=2$ 이면 예비 정리 1.)
**함자성**: $(\sigma^{\times k})(R_F)\subset R_{F'}$ 필요충분; $R$ 이 정수행렬의 핵 $R_F=\ker M_F$ 이면 자동. 상수차원 규칙에서는 B4 와 같이 $R_F=F\otimes_{P}R_P$ 가 강제된다 [증명: $F\otimes R_P\subset R_F$ 이고 차원이 같음]. 다만 차원이 변하는 규칙(예: 표수에 따라 선→평면)도 함자이므로 $k=2$ 직선 경우보다 "필요충분"이 약하다.
**표현**: $R=\ker M$, $M$ 정수행렬이면 $A_H=\mathbb Z^V/\langle M\cdot(v_1..v_k)\text{ 행들}\rangle$, $F^H=\mathrm{Hom}_{\mathbb Z}(A_H,F)$ — B2 가 그대로.
**예 (3-균등, $R=\{x+y+z=0\}$)** 
- $K_4^{(3)}$ (네 개의 삼각 간선): 제약행렬 $J-I$, $\det=-3$, $A=\mathbb Z/3$. $F^H$: 모든 정점 값 같음 $=t$, $3t=0$. $\dim=1$ ($\mathrm{char}=3$), 그 외 0 [증명 + 계산 확인: $\mathbb F_2,\mathbb F_3,\mathbb F_5$ 에서 $0,1,0$]. 기존 규칙의 홀수 사이클($\mathbb Z/2$)의 3-항 아날로그.
- 파노 평면(7 점 7 선): 스미스 꼴 $[2,2,6]$, $\det=24$, $A=(\mathbb Z/2)^3\oplus\mathbb Z/3$. $\dim_{\mathbb F_2}=3$ (해밍 코드의 핵에 대응), $\dim_{\mathbb F_3}=1$, 그 외 0 [계산 확인]. 소수 2, 3 에서만 살아 있고, 표수 0 에서는 $0$.
- 비고: 초그래프에서는 $k=2$ 의 정수 규칙보다 비틀림이 훨씬 다양한 소수에서 생겨 *표수 의존 불변량*이 풍부해진다(K_4^(3): 3, Fano: 2·3).

### E. 예제 종합 (직접 계산한 값)

| 예 | 규칙 | $\mathrm{rank}\,A_G$ / 비틀림 | 결과 |
|---|---|---|---|
| 방향 소스 3 개 → $v$ | head$=0$ | $\mathbb Z^3$ | $\dim=3$ 전 표수; $\ker B^TB$ 는 $p=3$ 에서 4 |
| 방향 사이클 $C_n^\to$ | head$=0$ | $0$ | $\dim=0$ |
| V자 $0\to2\leftarrow1$ | $(-2,1)$ | $\mathbb Z\oplus\mathbb Z/2$ | $\dim=1,\ 2,\ 1$ at $\mathbb Q,\mathbb F_2,\mathbb F_{3,5}$ [계산 확인] |
| 혼합 삼각형 $0\to1\to2,0\to2$ | $(-2,1)$ | $\mathbb Z/2$ ($d_c=1$) | $\dim=0$ ($p\ne2$), $1$ ($p=2$, 퇴화) |
| 같은 삼각형 | $(-3,2)$ | $\mathbb Z/6$ | $\dim=0$ 이나 $p=2,3$ 에서 1 (퇴화 소수) [계산 확인] |
| 같은 삼각형 | $(1,-1)$ ($\lambda=1$) | $\mathbb Z$ | 전 표수 1 |
| 방향 사이클 $C_n^\to$ | $(-2,1)$ | $\mathbb Z/(2^n-1)$ ($n=1..4$: 1,3,7,15) | $F^{C_n}\ne0\iff\mathrm{char}\mid2^n-1$ |
| 방향 사이클 $C_n^\to$ | $(3,2)$ | $\mathbb Z/(3^n-(-2)^n)$ ($5,5,35,65$) | 위와 동일 구조 |
| 무방향 $C_4$ vs $C_5$ | $(1,1)$ 기존 | $\mathbb Z$ vs $\mathbb Z/2$ | $\dim=1,1$ (char ≠ 2: $1$ vs $0$) |
| $P_5,C_6,Q_3,K_{3,3}$ | 모든 직선 규칙(무방향) | 모두 $\mathbb Z$ | $\ker B$ 차원 모두 1 — 구별 불가 [계산 확인] |
| 위 4 개 | 해석 (b), $\ker B^TB$ over $\mathbb F_2,\mathbb F_3,\mathbb F_5$ | $B^TB$ 스미스: P5 $[1^4]$; C6 $[1^4,6]$; Q3 $[1^4,2,8,24]$; K33 $[1,1,3,3,9]$ | $\dim\ker$: P5 $(1,1,1)$; C6 $(2,2,1)$; Q3 $(4,2,1)$; K33 $(1,4,1)$ — **네 개 모두 구별** [계산 확인] |
| $K_4^{(3)}$, Fano | $x+y+z=0$ | $\mathbb Z/3$; $(\mathbb Z/2)^3\oplus\mathbb Z/3$ | 상기 |

**공통 패턴 (예제에서 추출)**: (P1) 모든 정수 규칙에서 $F^G$ 의 차원 변동은 $A_G$ 의 비틀림 소수에서만 일어난다. (P2) 비틀림은 두 곳에서 온다: (i) 닫힌 걷기 불균형 $\lambda^{d_c}-1$ 의 소인수(순환 구조), (ii) $p\mid ab$ 퇴화(역방향 호에서 $\lambda^{-1}$ 이 정수가 아님). (P3) 무방향 직선 규칙은 성분 수·이분성 정도의 불변량만. 
**공통 장애물**: (O1) 직선 규칙은 *성분별로 최대 1 차원* — $\varphi(r)$ 하나가 성분 전체를 정함. 따라서 $\dim\ker B$ 는 성분 수 이하로 약하다. (O2) 비서로소 $(a,b)$ 의 처리, (O3) 일반 방향 그래프의 $A_G$ 순환성·위수 공식(트리에서 $\mathbb Z/2$ 같은 비순환 가능)의 일반증명이 미완.

### F. 종합 의견 (필수)

| 규칙/해석 | 불변량 풍부함 | 모든 체 함자성 | 고유구조 (Aut 표현) | 계산 가능성 |
|---|---|---|---|---|
| 기존 $x+y=0$ (무방향) | 약함: 이분 성분 수(+ char 2 에서 성분 수) | 예 (정수) | 성분 위 1 차원 문자(회전 $\pm1$) | 매우 쉬움(BFS) |
| $\lambda=1$ ($x=y$) | 성분 수만 (가장 약함) | 예, 무비틀림 | 성분들의 치환표현 | 매우 쉬움 |
| 퇴화 head$=0$ / tail$=0$ | 소스·싱크 수(방향 필요) | 예, 무비틀림 → 표수 불변 | 소스 위 치환표현(대칭 정보 풍부, 차원 정보 빈약) | 쉬움 |
| 정수 이득 $\lambda=-a/b$, $|\lambda|\ne1$, **방향 그래프** | 중간~풍부: $d_c$ (닫힌 걷기 불균형)의 약수 정보를 *표수를 바꿔* 읽어낸다 ($N_k=\#\{c:k\mid d_c\}$, $k=\mathrm{ord}_p(2)$; $k\ne1,6$ 모두 실현됨 — Zsigmondy [기억-미검증] → $\{d_c\}$ 거의 복원 [추측]) | **예, 가장 좋음** — 하나의 $A_G$ 가 모든 체를 일관 제어 | 방향 사이클 회전의 고유값이 $\lambda^{-1}$: 규칙 자체를 읽음 | 스미스 꼴(정수 행렬), 소형은 쉬움 |
| 임의 $\lambda\in F^\times$ | 위와 같되 체마다 다름 | 아니오: $\sigma(\lambda)=\lambda'$ 조건(짝 범주) | 같음 | 쉬움 |
| 일반 $R\subset F^k$ | 풍부(비틀림 소수 다양: Fano 2·3) | 정수 핵이면 예 | 임의 | 중간 |
| 해석 (b): $\ker B^TB$, $B^TB$ 의 스미스 꼴 | **가장 풍부**: 임계군/샌드파일군($P_5,C_6,Q_3,K_{3,3}$ 모두 구분) | $B^TB$ 도 정수 행렬이라 예 | 그래프 라플라시안이므로 Aut 표현 풍부 | 스미스 꼴, 쉬움~중간 |

**판단 (의견, [추측] 포함)**:
1. *차원만 보면* 무방향 직선 규칙은 모두 약하다([증명]: 성분당 최대 1 차원). 정말 풍부한 정보는 (i) 방향 그래프에서 정수 이득 + 표수 변화, (ii) 해석 (b) 의 $\ker B^TB$ 의 표수별 차원 / 스미스 꼴(라플라시안·임계군과 같은 대상)에서 나온다. 후자는 계산한 예에서 $P_5,C_6,Q_3,K_{3,3}$ 를 모두 구분했다(근거로 쓰지는 않고 동기 부여 정도; 스미스 꼴 $[1,1,3,3,9]$ 등은 군 구조이므로 결정적 구분이다). 
2. *함자성과 일관성*에서는 **정수 계수 족**이 유일하게 좋다 (B4, B2). 기존 규칙은 이 족의 한 점($\lambda=-1$)이며 비틀림이 $\mathbb Z/2$ 하나뿐이라 가장 가난하다.
3. *한 규칙을 꼽는다면*: 무방향 그래프 연구에는 $(1,1)$ 그대로 두되 (b) 의 라플라시안형 연산자를 보조하고, 방향 그래프 연구에는 $\lambda=-a/b$ ($a=-2,b=1$ 등) **하나의 정수 규칙을 모든 소수에서 읽는** 것을 권한다. $\lambda=0,\infty$ 퇴화형은 독립적 연구 가치가 낮다(소스 수) 하나 $p\mid ab$ 에서의 극한 거동으로서 필수 구성요소다.

---

## 후속연구 지점
1. **(최우선) 방향 그래프의 $A_G$ 일반 구조 정리**: 연결 방향 그래프에서 $A_G$ 의 비틀림을 $d_c$, $a$, $b$ 의 함수로 닫힌 식으로 쓰기. 이유: 이것이 "모든 소수·모든 체에서의 $\dim F^G$" 를 한 번에 결정. 시작: 나무 + 기저 사이클로 줄여 $A_G=\mathrm{coker}$ 를 블록 삼각화; 방향 사이클 $\mathbb Z/(a^n-(-b)^n)$ 의 순환성 증명($sa+tb=1$ 활용)부터. 난점: 역방향 호에서 $a$ 나 $b$ 의 비가역성으로 트리도 비순환($\mathbb Z\oplus\mathbb Z/2$).
2. **해석 (b) 의 $B^TB$ 스미스 꼴과 샌드파일/임계군의 관계를 정수 규칙 족에서 정리화**: $\lambda=1$ 은 라플라시안(임계군), $\lambda=-1$ 은 부호 없는 라플라시안; 일반 $(a,b)$ 에서 $M_{a,b}=a^2D^++b^2D^-+ab(A+A^T)$ 의 스미스 꼴. 이유: 계산상 $P_5,C_6,Q_3,K_{3,3}$ 를 가르는 유일한 후보. 시작: 알려진 결과(Biggs 등)를 [기억-미검증] 로 두고 소형 예에서 검증, $K_{3,3}$ 의 $[3,3,9]$ 같은 구조 증명. 난점: 정확한 선행 결과 확인(문주님께 논문 요청 가능), 방향 그래프로의 확장.
3. **$\{d_c\}$ 복원 가능성**: 한 정수 규칙 ($\lambda=2$)의 $\dim_{\mathbb F_p}$ 을 모든 $p$ 에서 모으면 방향 그래프의 성분별 불균형 gcd 의 멀티집합이 복원되는가(Zsigmondy 활용). 이유: 표수 변화를 쓴 "풍부함" 주장의 핵심. 시작: $N_k=\#\{c:k\mid d_c\}$ 에서 뫼비우스 반전, 예외 $k=1,6$ 처리. 난점: $k=6$ 의 모호성, 퇴화 소수 $p\mid ab$ 분리.
4. **Aut(G) 표현의 정수 구조**: $A_G\otimes F$ 를 $\mathbb Z[\mathrm{Aut}\,G]$-가군으로 보아 (a) 를 일반 증명; 사이클/경로 대칭 고유값 $\lambda^{\mp1}$, $(-1)^{\cdot}$ 의 공식. 시작: 방향 사이클 회전 고유값 $\lambda^{-1}$ (직접 계산됨)을 일반 사이클 순환군 작용으로. 난점: 성분 치환과 문자의 결합, 표수가 군 위수를 나눌 때 비반단순.
5. **$k$-항 규칙 및 곱 구조**: $R=\{x+y+z=0\}$ 의 Fano/ $K_n^{(3)}$ 비틀림 공식, 그리고 §C7 의 곱 구조 ($\lambda\in\{0,1,\infty\}$ 에서만 대수)가 $\lambda=-1$ 의 $\mathbb Z/2$-등급과 어떻게 연결되는지(예: 이분 그래프의 두 부분집합 지시함수). 난점: $k\ge3$ 에서 핵의 스미스 꼴을 조합적으로 해석하기.
