# [R1-researcher2] 방향 + 이득 λ 규칙: 차원 정리의 증명, 감김 gcd, 순환 분류, 스위칭, 표현, 함자성

- 작성자·라운드·역할: researcher2 · R1 · 포메이션 I 분담, 규칙 $R_\lambda=\langle(1,\lambda)\rangle$ ($\lambda\in F^\times$, 간선 $u\to v \Rightarrow \varphi(v)=\lambda\varphi(u)$) 담당
- 코드: `rooms/researcher2/gain.py` (GF(p) 랭크, 증명 단계 확인용 소수 예만 사용)

## 요약
- 예비 정리 5 는 **옳다**. 체 F 의 어떤 $\lambda\in F^\times$ 에서도(위수 무한 포함, 루프·다중간선·양방향 쌍 포함) 성립하며 증명을 아래에 썼다. [증명]
- 정리를 정련했다. 연결성분 C 마다 **감김 gcd** $\omega(C)\in\mathbb Z_{\ge0}$ 를 두면 $\dim F^G=\#\{C:\ \mathrm{ord}(\lambda)\mid\omega(C)\}$ 이고, $\mathrm{rank}\,B=n-\dim$. 또 이것은 "C 가 방향 사이클 $\vec C_k$ 로 가는 호모를 가짐"과 동치다. [증명]
- $\vec C_n$ 은 $k\mid n$ 일 때만 dim 1. 혼합 사이클은 $k\mid(f-b)$ 일 때 1. $\lambda=-1$ 에서는 방향이 무관하며 기존 규칙과 같다. 위수 $k\ge3$ 에서 균형 방향의 개수는 $|\mathrm{Hom}(G,C_k)|/k$ 다 (k=3 이면 3-채색). [증명]
- $B^TB$ 의 커널은 $\ker B$ 보다 **크다**(예: $\mathbb Z_5$, $\lambda=2$, $\vec C_4$: 2 대 1). 유한체에서는 이차형식이 등방이기 때문이다. 예비 가정 "ker B^TB = F^G"는 **거짓**. [계산 확인]+[증명]
- 함자성: 점 찍힌 체의 범주 $(F,\lambda)\to(F',\lambda')$ 위에서 (−)^G 는 공변이며 $F^G\otimes_F F'\cong F'^G$ (기저변환). 판정: 기존 규칙보다 정보는 풍부하나(순환 길이 mod k, 방향, 3-채색까지) 방향 데이터가 필요하고 자연스러운 정의역이 무방향 그래프가 아니다.

## 본문

### 0. 설정과 기호
방향 다중그래프 $G=(V,A)$ (루프·평행·반평행 호 허용), $n=|V|$. 호 $a=(u\to v)$ 에 대해 $B_\lambda$ 의 행은 $b_a=e_v-\lambda e_u$ ($\in F^V$). $F^G=\ker B_\lambda$. 이득 그래프 용어: 호 a 의 이득 $\lambda$, 역방향 통과 시 $\lambda^{-1}$.
걸음(walk) W 의 **감김** $w(W)=\#\text{정방향 호}-\#\text{역방향 호}\in\mathbb Z$. 이득 $g(W)=\lambda^{w(W)}$. 감김은 걸음의 연접에 대해 가법적이고, 역걸음은 부호가 바뀐다.
성분 C 의 **감김 gcd** $\omega(C)=\gcd\{w(W): W\text{가 C 의 닫힌 걸음}\}\in\mathbb Z_{\ge0}$ (닫힌 걸음이 감김 0 뿐이면 $\omega=0$). $k=\mathrm{ord}(\lambda)\in\mathbb Z_{\ge1}\cup\{\infty\}$. 관례: $\infty\mid m \iff m=0$.

### 1. 정리 1 (예비 정리 5 의 증명과 정련) [증명]
**정리 1.** 임의의 체 F, $\lambda\in F^\times$, 방향 다중그래프 G 에 대해
$$\dim F^G=\#\{\text{성분 }C:\ \lambda^{w(W)}=1\ \forall\text{ 닫힌 걸음 }W\subset C\}=\#\{C:\ \mathrm{ord}(\lambda)\mid\omega(C)\}.$$
또한 균형 성분은 $\varphi_C(x)=\lambda^{s(x)}$ (s 는 아래) 하나로 생성된다. $\mathrm{rank}\,B_\lambda=n-\dim F^G$.

**증명.** $F^G$ 는 성분들의 직합이므로 연결 G 만 본다. 기준점 r 을 잡는다. 임의의 정점 x 에 대해 r 에서 x 로 가는 걸음 P 를 택하면, 호를 따라 $\varphi(\text{head})=\lambda\varphi(\text{tail})$, 역으로 $\varphi(\text{tail})=\lambda^{-1}\varphi(\text{head})$ (λ 가 가역이므로 가능)이므로 $\varphi(x)=\lambda^{w(P)}\varphi(r)$. 따라서 $\varphi\mapsto\varphi(r)$ 는 단사 선형사상 $F^G\hookrightarrow F$, $\dim\le1$.
(i) 모든 닫힌 걸음에서 $\lambda^w=1$ 이면, $s(x):=w(P)$ 가 P 의 선택에 대해 $\mathrm{ord}(\lambda)$ 를 법으로 잘 정의되고(두 걸음 P,P' 의 차 $P\cdot\bar P'$ 는 닫힌 걸음), $\varphi_C(x)=\lambda^{s(x)}$ 는 모든 호에서 $\varphi(v)=\lambda\varphi(u)$ 를 만족한다(P 를 u 까지 간 걸음 + 호 a 로 잡으면 $s(v)=s(u)+1$). 따라서 $\dim=1$.
(ii) 어떤 닫힌 걸음 W (r 기점으로 평행이동 가능; r 까지의 걸음을 앞뒤로 붙이면 감김 불변)에서 $\lambda^{w}\ne1$ 이면 $\varphi(r)=\lambda^{w}\varphi(r)$, F 가 체이므로 $\varphi(r)=0$ ⇒ $\varphi=0$, $\dim=0$.
닫힌 걸음의 감김 집합은 $\omega\mathbb Z$ 의 부분집합으로 gcd 가 $\omega$ 이고(가법군 준동형 $H_1\to\mathbb Z$ 의 상이 $\omega\mathbb Z$, 닫힌 걸음의 감김은 사이클 기저 감김의 정수결합이므로), $\lambda^{w}=1\ \forall w\iff\lambda^{\omega}=1\iff k\mid\omega$. 랭크는 랭크-영도 정리. ∎

**특수 경우 확인.**
- 루프 $u\to u$: 감김 1, 균형 ⟺ $\lambda=1$ ($B$ 의 행이 $(1-\lambda)e_u$). 방향이 반대여도 $\lambda^{-1}=1$ 이므로 동치.
- 평행 호 둘 $u\to v$, $u\to v$: 닫힌 걸음의 감김 0, 영향 없음 (행이 같음).
- 반평행 쌍 $u\to v$, $v\to u$: 닫힌 걸음 $u\to v\to u$ 의 감김 2. 균형 ⟺ $\lambda^2=1$ ($\lambda=\pm1$). 이는 R 이 대칭 ⟺ $\lambda^2=1$ (예비 정리 2) 과 일치: 무방향 간선은 반평행 쌍이므로 $\lambda\ne\pm1$ 이면 K₂ 조차 $F^{K_2}=0$.
- 고립점: 닫힌 걸음 감김 0 ($\omega=0$), 항상 기여 1. 위수 무한(예: $\lambda=2\in\mathbb Q$)이면 균형 ⟺ $\omega(C)=0$ ⟺ 호의 높이 함수 $s:C\to\mathbb Z$ 가 존재 ($s(v)=s(u)+1$).
- 따라서 예비 정리 5 에 정정할 점은 없고, "ord(λ) 의 배수"를 "ord(λ) 가 $\omega(C)$ 의 약수"로 읽으면 위수 무한도 포함한다.

**따름 1 (호모 해석).** 위수 k (유한) 의 λ 에 대해 성분 C 가 균형 ⟺ 방향 사이클 $\vec C_k$ 로의 디그래프 호모 $s:C\to\vec C_k=(\mathbb Z_k,\ x\to x+1)$ 가 존재 ⟺ $k\mid\omega(C)$. [증명: 위 s 의 $s \bmod k$.] 그러므로 디그래프 $F_\lambda=(F,\ x\to\lambda x)$ 는 $\{0\}$ (루프) $\sqcup\ \frac{q-1}{k}$ 개의 $\vec C_k$ 로 갈라지고($|F|=q$), 균형 성분은 호모 $k\cdot\frac{q-1}k=q-1$ 개 + 0 = $q$ 개를 가진다. 문주님의 정의와 같은 말이며 $|\mathrm{Hom}|=q^{\dim}$ 의 원인이다. 주의: $F_\lambda$ 를 **무방향** 그래프(대칭폐포)로 보면 호모는 선형이 아니고 이 모든 결과가 깨진다. 방향이 본질적이다.

**고전 용어와의 관계.** [기억-미검증] 이득 그래프(Zaslavsky의 gain graph / biased graph)에서 사이클의 이득이 1 이면 균형. 이득 군을 $F^\times$ 에 넣은 "프레임 행렬"의 열 $e_v-g\,e_u$ 가 프레임 매트로이드를 표현하고, 그 랭크는 $n-(\text{균형 성분 수})$. 위 정리 1 은 이득이 $\lambda$ 로 상수인 경우에 이 사실을 독립적으로 증명한 것이다 (B 의 행 = 프레임 행렬의 열). $\lambda=1$ 은 사이클 매트로이드(그래프 매트로이드), $\lambda=-1$ 은 모든 간선이 음인 부호그래프(균형 ⟺ 이분)로, 부호 결합행렬 $\partial$ 과 비부호 결합행렬 $|\partial|$ 의 두 얼굴이다. 정리 1 은 일반 이득 $g:A\to F^\times$ 에도 그대로 성립한다(균형 ⟺ 모든 닫힌 걸음 이득 1, 증명 동일).

### 2. 사이클의 완전 분류 [증명]
$C_n$ ($n\ge1$; n=1 은 루프, n=2 는 다중간선 쌍) 의 호 방향을 임의로 주고, 한 방향으로 한 바퀴 돌 때 정방향 호 f 개, 역방향 b 개 ($f+b=n$). 유일한 사이클의 닫힌 걸음은 그 사이클의 반복이므로 $\omega=|f-b|=|n-2b|$.
**정리 2.** $\dim F^{C_n}(\lambda)=1$ ⟺ $k\mid(n-2b)$ ($k=\infty$ 이면 $n=2b$); 아니면 0.
- 방향 사이클 $\vec C_n$ (b=0): dim 1 ⟺ $k\mid n$ ⟺ $\lambda^n=1$. 예: $\mathbb Z_5$, λ=2 (k=4): n=4,8,12 에서만 1. $\mathbb Z_7$, λ=2 (k=3): n=3,6,9,… ; λ=3 (k=6): n=6,12. $\mathbb Z_{13}$, λ=2 (k=12): n=12; λ=5 (k=4): n=4,8,12. (표는 gain.py 로 n=1..14 확인 [계산 확인])
- k=1 (λ=1): 모든 방향에서 1. k=2 (λ=−1, char≠2): $n-2b\equiv n$, 즉 **방향 무관, n 짝수일 때만 1**. 기존 규칙과 정확히 같음.
- k≥3: 각 사이클에서 b=0 과 b=1 이 모두 균형이려면 $k\mid n$ 이고 $k\mid n-2$, 따라서 $k\mid2$. 곧 k≥3 이면 사이클을 가진 모든 연결 그래프에서 **불균형 방향이 존재**한다.
- 혼합 방향 삼각형: n=3, b∈{0,1,2,3}, $w\in\{3,1,-1,-3\}$. 균형 ⟺ $k\mid3$ (b=0,3 이 방향 3-사이클), 즉 k∈{1,3}. 추이적 삼각형(1→2, 2→3, 1→3, b=1)은 $|w|=1$ 이므로 균형 ⟺ **k=1**. 곧 λ≠1 이면 $F^{T}=0$ ($T$=추이 토너먼트).
- 균형 방향의 개수 $N(n,k)=\sum_{b:\,k\mid n-2b}\binom nb$. 예: $N(4,4)=8$, $N(4,3)=6$, $N(6,3)=22$, $N(6,12)=20$, $N(5,3)=10$ (Z7 λ=2 등으로 계산 확인 [계산 확인]).

### 3. 방향 부여와 스위칭 (질문 iii)
**정리 3 (스위칭).** $\theta:V\to F^\times$ 에 대해 이득 $g'(u\to v)=\theta(v)g(u\to v)\theta(u)^{-1}$ 이면 $\varphi\mapsto\theta\varphi$ 는 $F^{G,g}\cong F^{G,g'}$ 동형이며 모든 닫힌 걸음의 이득을 보존한다. [증명: 한 줄.]
- "정점 v 의 모든 간선을 λ 배" = $\theta(v)=\lambda^{\pm1}$ 로 스위치. 상수 이득 λ 의 클래스를 벗어날 수 있으나 dim 은 같다.
- **싱크/소스 뒤집기.** 싱크 v (모든 호가 v 로 들어옴)의 모든 호를 반대로 하면 $\theta(v)=\lambda^{-2}$ 로 스위칭한 것과 같다(들어오는 호의 이득 $\lambda\theta(v)=\lambda^{-1}$). 소스는 $\theta(v)=\lambda^{2}$. 따라서 싱크/소스 뒤집기는 $F^G$ 의 **동형을 보존**한다. 일반 정점 뒤집기는 $\lambda^4=1$ 일 때만 스위칭과 일치한다 (나가는 호 이득 $\lambda/\theta=\lambda^3$ 이 $\lambda^{-1}$ 이어야 함). [증명]
- 싱크/소스 뒤집기는 모든 사이클의 감김을 불변으로 둔다. [기억-미검증] Pretzel 정리: 연결 그래프의 두 방향이 싱크/소스 뒤집기로 서로 옮겨짐 ⟺ 모든 사이클에서 감김이 같음. (역방향은 증명하지 않음.) 이를 받아들이면 dim 은 방향 클래스(=감김 함수 $H_1\to\mathbb Z$)만의 함수.
- 나무에서는 모든 방향이 동치 (사이클 없음, $\omega=0$), dim = 성분 수. 방향에 의존하는 dim 은 사이클이 있어야 한다.
- 위수 k≥3, 연결 G 에 대해 **정리 4** [증명]: 균형 방향의 개수 $=|\mathrm{Hom}(G,C_k)|/k$ ($C_k$ 는 k-사이클 그래프, 단 k=3 이면 $K_3$, 곧 $|\{\text{올바른 3-채색}\}|/3$). 근거: 균형 방향 o ⟺ $s:V\to\mathbb Z_k$ 가 있어 호 $u\to v$ 마다 $s(v)-s(u)=1$. k≥3 이면 $1\ne-1$ 이므로 s 는 $s(v)-s(u)=\pm1$ 인 $C_k$-호모이고 s 로부터 방향이 복원된다(호 $u\to v$ ⟺ $s(v)=s(u)+1$). 같은 방향을 주는 s 는 상수 평행이동 k 개 뿐. 루프가 있으면 둘 다 0. 확인: $C_5$, k=3 → 30/3=10 ✓; $C_6$ → 66/3=22 ✓; $C_3$ → 6/3=2 ✓; $K_4$ → 0.
- 귀결: 위수 3 인 λ (Z₇ 의 2,4; Z₁₃ 의 3,9 등)에서 "어떤 방향에 대해 $\dim F^G$ 가 성분 수만큼 크다" ⟺ G 가 3-채색 가능. 이것은 NP-완전한 성질이다. 곧 방향을 고르는 최적화의 계산 난이도가 높다. 반대로 **방향이 주어졌을 때** dim 은 BFS 와 gcd, 곧 다항시간.
- $\lambda=-1$ 은 $\mathrm{Hom}(G,C_2)$ 이야기와 달리 모든 방향이 균형이거나(이분) 아무것도 아님. k=2 에서 방향 정보가 사라지는 이유는 $\lambda=\lambda^{-1}$.

### 4. 당김 $f^*$ 의 랭크 (연구할 양 2) [증명]
방향 다중그래프 호모 $f:G\to H$ (호→호) 는 성분을 성분으로 보낸다. 닫힌 걸음의 감김을 보존하므로 $\omega(H\text{-성분 }D)\mid\omega(C)$ for $f(C)\subset D$. 따라서 D 균형 ⇒ C 균형.
**정리 5.** $f^*:F^H\to F^G$, $\varphi\mapsto\varphi\circ f$ 의 랭크는 $\#\{\,D\ \text{균형 성분 of }H:\ \exists C\subset G,\ f(C)\subset D\}$. 균형 D 의 기저 $\varphi_D$ 는 D 위에서 어디서나 0 이 아니므로 $f^*\varphi_D=\sum_{C\to D}\varphi_D(f(r_C))\,\varphi_C$ (각 계수 ≠0; $\varphi_C(r_C)=1$ 정규화). 서로 다른 D 의 상은 서로소 지지를 가져 독립.
- 단사 ⟺ H 의 모든 균형 성분이 어떤 G 성분의 상을 포함한다.
- 전사 ⟺ G 의 모든 균형 성분 C 가 H 의 **균형** 성분으로 가고, 서로 다른 균형 성분 C, C' 은 서로 다른 H-성분으로 간다. (불균형 D 로 가는 균형 C 는 상에 없음.)
- 위 구조는 기존 규칙과 같은 모양이며, 단지 "이분 성분"이 "$\mathrm{ord}(\lambda)\mid\omega$ 인 성분"으로 바뀐다. - 예: $\vec C_{12}\to\vec C_4$ 는 호모 (i↦i mod 4) 이고 k=4 에서 $f^*:F\to F$ 는 동형, k=12 에서는 $F^{\vec C_4}=0$ 이라 영사상이며 $F^{\vec C_{12}}=F$ 가 상에 없음 (전사 아님). 반변성의 구체 사례.

### 5. 자기동형 표현 (연구할 양 3(a)) [증명]
Aut(G) 를 호 방향을 보존하는 자기동형군으로 둔다 (역전은 이득을 $\lambda^{-1}$ 로 바꾸므로 $\lambda^2\ne1$ 이면 자기동형이 아님). $\sigma\cdot\varphi=\varphi\circ\sigma^{-1}$.
**정리 6.** $F^G\cong\bigoplus_{[C]}\mathrm{Ind}_{\mathrm{Stab}(C)}^{\mathrm{Aut}(G)}\chi_C$ (직합은 균형 성분의 Aut-궤도 대표 C 에 대해). 여기서 $\chi_C:\mathrm{Stab}(C)\to\langle\lambda\rangle\subset F^\times$, $\chi_C(\sigma)=\lambda^{w(r\to\sigma^{-1}r)}$ 은 일차 지표. 곧 **단항 표현**이고 순열표현에 지표를 꼬은 것.
증명: 균형 C 에서 $\sigma\varphi_C\in F\varphi_C$ 이고 r 에서 평가하면 계수 $\varphi_C(\sigma^{-1}r)$. σ 가 성분들을 섞으므로 직합은 궤도별 유도표현. ∎
- 예: $\vec C_n$ ($k\mid n$), 회전 $\rho:i\mapsto i+1$, $\varphi_C(i)=\lambda^i$ 이면 $(\rho\varphi)(i)=\varphi(i-1)=\lambda^{-1}\varphi(i)$. 곧 고유값 $\lambda^{-1}$ (k 차 원시근), $\mathrm{Aut}=\mathbb Z_n$ 에서 $\chi(\rho)=\lambda^{-1}$ 이며 위수 k, 핵 $\langle\rho^k\rangle$ 은 자명하게 작용.
- 대조: 기존 규칙 ($\lambda=-1$) 의 이분 성분 위 지표는 $\pm1$ (부분집합 $V_1\leftrightarrow V_2$ 를 바꾸는지 여부) 이다. 곧 위수 ≥3 지표는 새로운 정보이다.
- 푸리에 분해: $\vec C_n$ 에서 $\mu_n\subset F$, $\mathrm{char}\nmid n$ 이면 $F^V=\bigoplus_{\lambda\in\mu_n}F^{\vec C_n}(\lambda)$ (회전의 고유공간 분해 = 이산 푸리에 변환) [증명: 회전은 반단순]. 그리고 서로 다른 λ 에 대한 $F^G(\lambda)$ 는 호가 있는 정점에서 겹치지 않는다($(\lambda-\mu)\varphi(u)=0$).
- 반사 $\tau:i\mapsto -i$ 는 호를 뒤집으므로 자기동형이 아니다. $\varphi_C\circ\tau=\lambda^{-i}$ 는 $\lambda^{-1}$ 규칙의 해로 $F^G(\lambda)$ 밖에 있다 ($\lambda^2\ne1$). 이득 $\lambda\leftrightarrow\lambda^{-1}$ 의 대칭이 별도 구조를 이룬다. $F^{G^{op}}(\lambda)=F^G(\lambda^{-1})$.

### 6. 연산자 $B^TB$ (연구할 양 3(b)) [계산 확인]+[증명]
$B^TB=\sum_a b_a^Tb_a$, 성분: 대각 $(B^TB)_{vv}=\mathrm{indeg}(v)+\lambda^2\,\mathrm{outdeg}(v)$ (루프는 $(1-\lambda)^2$), 비대각 $(u,v)$: $-\lambda(m_{uv}+m_{vu})$ ($m_{uv}$ = u→v 호 수). 대칭행렬 (켤레 없는 전치).
**주의 (정정).** $\ker B\subseteq\ker B^TB$ 이나 유한체에서는 **진부분집합일 수 있다**: $x\in\ker B^TB$ ⟺ $y=Bx\in\ker B^T$ 이고, $y\ne0$ 이어도 $B^Ty=0$ 가능 (행공간이 자기직교 부분을 가짐). 이는 $b_a\cdot b_a=1+\lambda^2=0$ (λ²=−1: $\mathbb Z_5$ 의 2, 3; $\mathbb Z_{13}$ 의 5, 8) 같은 등방 행에서 쉽게 생긴다.
**정리 7 (방향 사이클).** $B=S-\lambda I$ ($S$ 는 순환 이동), $B^TB=(S^{-1}-\lambda)(S-\lambda)=(1+\lambda^2)-\lambda(S+S^{-1})$, 순환행렬. $\mathrm{char}\nmid n$ 이면 고유벡터는 $(\zeta^i)$, $\zeta^n=1$ (대수적 폐포), 고유값 $(\zeta-\lambda)(\zeta^{-1}-\lambda)$. 따라서
- $\lambda^n\ne1$: $\ker=0$.
- $\lambda^n=1,\ \lambda^2\ne1$: $\zeta=\lambda$ 와 $\zeta=\lambda^{-1}$ 둘 다 영 ⇒ $\dim\ker B^TB=2>1=\dim\ker B$. 추가된 벡터 $(\lambda^{-i})$ 는 **반대 방향 규칙의 해**: $\ker(B^TB)=F^G(\lambda)\oplus F^G(\lambda^{-1})$.
- $\lambda=\pm1$ ($\lambda^n=1$): $\zeta=\lambda$ 하나, 차원 1 (같음).
- $\mathrm{char}=p\mid n$ (λ=1 이어야 함): $B^TB=-S^{-1}(S-1)^2$, $(S-1)$ 은 크기 n 의 단일 유르단 블록에 (S=x^n−1 의 $(x-1)^{p^a\cdots}$) 의해 커널 2 차원 (예: p=7, n=7, λ=1: 2). 이때 $B^TB$ 는 **반단순이 아니다**.
계산 확인: $\mathbb Z_5$, λ=2, $\vec C_4$: ker B=1, ker B^TB=2; $\mathbb Z_7$, λ=2, $\vec C_3,\vec C_6$: 1 대 2; λ=3, $\vec C_6$: 1 대 2; λ=6(=−1): 항상 같음; λ=1, n=7=p: 1 대 2. [계산 확인]
**결론.** 일반 그래프에서 $\ker B^TB=\ker B\oplus$(역방향 해들)에 가깝게 보이나 일반 증명은 얻지 못함 [추측: 방향 사이클·나무를 넘는 일반 그래프에서 $\ker B_\lambda^TB_\lambda\supseteq F^G(\lambda)+F^G(\lambda^{-1})$ 이 성립하는가는 열려 있음; 이 포함 자체도 일반적으로 거짓일 가능성이 있어 검증 필요]. 복소수/실수 위에서는 에르미트형 $B^*B$ 가 양반정부호라 $\ker B^*B=\ker B$ 이지만 유한체는 이차형식이 등방이라 이 논법이 실패한다 — 그래서 유한체에서는 "라플라시안 스펙트럼" 대신 **B 자체의 랭크/커널**을 써야 한다. 이득 라플라시안 $D-A_g$ 와의 관계는 [기억-미검증].

### 7. 함자성 (질문 v) [증명]
**점 찍힌 체의 범주** $\mathsf{Fld}_*$: 대상 $(F,\lambda)$, $\lambda\in F^\times$; 사상 $\sigma:F\to F'$ 체 사상(단사)으로 $\sigma(\lambda)=\lambda'$. 디그래프 범주 $\mathsf{Dig}$ (호모).
- $(F,\lambda)\mapsto(-)^G_\lambda$ : $\sigma_*:F^G\to F'^G$, $\varphi\mapsto\sigma\circ\varphi$. 호 조건 $\varphi(v)=\lambda\varphi(u)$ ⇒ $\sigma\varphi(v)=\sigma(\lambda)\sigma\varphi(u)=\lambda'\sigma\varphi(u)$ ✓. $\sigma(\lambda)=\lambda'$ 이 **필요충분**(G 에 호가 하나 있고 $\varphi(u)\ne0$ 이 될 수 있는 경우; K₂ 로 충분). $F$-선형이 아니라 $\sigma$-반선형이며 단사.
- $\sigma$ 가 체 확대이면 $F^G\otimes_FF'\cong F'^G$ [증명: B 는 F 위의 행렬이고 $\ker(B\otimes F')=\ker B\otimes F'$ (평탄성)]. 따라서 **dim 은 점 찍힌 체 사상에 대해 불변**: $\dim F^G$ 는 $(G,\mathrm{ord}\lambda)$ 만의 함수 (정리 1 과 일관). 체의 특성은 오직 "위수 k 가 존재하는가"(k 가 p 와 서로소, $k\mid q-1$) 로만 들어온다.
- $\mathsf{Dig}^{op}\times\mathsf{Fld}_*\to\mathsf{Vect}$ 쌍함자: $F^{(-)}$ 반변 (정리 5), $(-)^G$ 공변. 자연성: $F^H\to F^G$ 와 $\sigma_*$ 는 가환.
- 분리합: $F^{G\sqcup H}=F^G\times F^H$ ✓ (모든 λ). 곱: 디그래프의 텐서곱 $G\times H$ 에서 닫힌 걸음은 두 사영의 닫힌 걸음이며 감김이 같다 (두 좌표가 동시에 전진·후진). $G\times H\to G,\ H$ 가 호모이므로 정리 5 로 $F^G,F^H\to F^{G\times H}$ 가 있다. 곱 위의 dim 은 별도 연구 필요 [추측: $\omega(G\times H)$ 는 $\omega(G),\omega(H)$ 의 gcd 로 표현될 가능성; 증명 못 함].
- **범주 구조**: 점 찍힌 환 $(\mathbb Z[t^{\pm1}],t)$ 가 환 범주의 시작 대상이며, 체 범주에는 시작 대상이 없다. $\mathbb Z[t^{\pm}]$ 위의 가족 $B_t$ 의 섬유 차원은 닫힌 집합 $V(t^{\omega(C)}-1)$ 에서 점프한다 ($\omega=0$ 이면 모든 곳). λ 가 $\pm1$ 이면 모든 체에서 정의되고 모든 체 사상에 호환(점 찍을 필요 없음). 따라서 $\lambda=\pm1$ 만이 **체의 범주 위의 함자**이며 나머지는 $\mathsf{Fld}_*$ 위에서만 함자이다. $\lambda=-1$ 은 char 2 에서 $\lambda=1$ 과 붕괴 (dim 이 이분 성분 수에서 성분 수로 점프; 기존 규칙의 "나쁜 환원").
- 같은 위수의 λ, λ' (예: $\mathbb Z_7$ 의 2 와 4, 3 과 5) 의 $F^G$ 는 차원이 같지만 $F^V$ 안의 서로 다른 부분공간 (갈루아 켤레, 사상 $x\mapsto x^j$ 는 비선형).

### 8. 예제 요약 ($\mathbb Z_7$, λ=2 (k=3) 를 대표로)
| 그래프(방향) | ω | dim (k=1) | (k=2) | (k=3) | (k=6) |
|---|---|---|---|---|---|
| 방향 경로 $P_5$ / 나무 | 0 | 1 | 1 | 1 | 1 |
| $\vec C_3$ | 3 | 1 | 0 | 1 | 0 |
| $\vec C_6$ | 6 | 1 | 1 | 1 | 1 |
| $\vec C_4$ | 4 | 1 | 1 | 0 | 0 |
| $C_4$ 교대 (b=2) | 0 | 1 | 1 | 1 | 1 |
| 추이 삼각형 | 1 | 1 | 0 | 0 | 0 |
| 루프 한 개 | 1 | 1 | 0 | 0 | 0 |
| 반평행 K₂ | 2 | 1 | 1 | 0 | 0 |
| $\vec C_3\sqcup\vec C_4$ | 3, 4 | 2 | 1 | 1 | 0 |
| $K_4$ (임의 방향) | 홀수 사이클 포함 | 1 | 0 | 0 (3-채색 불가, 정리 4) | 0 |

(열은 k=ord λ, 예: $\mathbb Z_7$ 의 1, 6, 2, 3. 앞 행들은 정리 1·2 에서 직접. $K_4$ 행은 비이분(k=2 → 0)과 정리 4(k=3 → 균형 방향 없음)의 결론이며 따로 계산하지 않았다. $K_{3,3}$ 은 이분이라 k=2 에서 방향과 무관하게 1, k≥3 에서는 방향에 따라 다르며 균형 방향 수는 $|\mathrm{Hom}(K_{3,3},C_k)|/k$ 로 주어지나 계산하지 않았다.)

**공통 패턴.** (1) 모든 값이 성분 단위로 0/1, 합으로 결정. (2) 불균형의 원인은 항상 어떤 사이클의 감김이 k 의 배수가 아닌 것 하나. (3) 방향이 cycle 의 감김만으로 들어온다. **공통 장애물.** (1) 방향 선택: 무방향 그래프의 불변량이 되려면 방향을 모두 합산/최적화해야 하고 k=3 에서 NP-완전. (2) $B^TB$ 형 연산자는 유한체에서 B 의 정보를 잃거나 더한다. (3) λ²≠1 이면 무방향 그래프에 정의되지 않는다.

### 9. 자기 공격 (반례 탐색)
- "dim 이 방향과 무관"? 거짓: $\vec C_4$ 와 교대 $C_4$ 가 k=3 에서 0 대 1. (k=2 에서만 무관, 증명됨.)
- "정리 1 은 char 가 k 와 관계 있으면 깨진다"? λ 는 F 안의 원소이므로 ord(λ) 는 항상 char 와 서로소 (λ=1 이면 k=1). 깨지지 않음.
- "위수 무한 λ 도 동일"? 성립 (ω=0 인 성분만). $\mathbb Q$ 에서 λ=2 이면 $\vec C_n$ 은 항상 0, 교대 $C_4$ 는 1 [증명].
- "ker B^TB = F^G" : 거짓 (정리 7 의 반례).
- 반평행 쌍: 예비 정리 5 서술에서 "정방향−역방향 간선수" 로 이미 처리됨; 감김 2.
- 대칭폐포로 보는 오해: 위에서 지적.

## 후속연구 지점
1. **방향 클래스(감김 함수)와 무방향 불변량의 설계** — 무엇을: $Z(G;k)=\sum_{o}q^{\dim F^{G,o}(\lambda)}$ 또는 균형 방향 수 $|\mathrm{Hom}(G,C_k)|/k$ 가 P₅, C₆, Q₃, K₃,₃ 등을 구분하는지. 왜: 문주님 쟁점(약한 불변량) 해소. 시작: 정리 4 + $\mathrm{Hom}(G,C_k)$ 의 Lovász 이론(호모 수가 그래프를 결정). 난점: k=2 는 방향이 사라져 약하고, k≥3 은 NP-완전.
2. **Pretzel 정리의 증명과 방향 클래스 분류** — 싱크/소스 뒤집기 동치 ⟺ 사이클 감김 함수 일치. 왜: dim 이 방향 클래스의 함수임을 완전하게 만듦. 시작: 정리 3 의 스위칭 + 순환 수(circulation) 논증. 난점: 일반 증명 기억 불확실 [기억-미검증].
3. **$\ker B^TB$ 의 일반 구조** — $\ker B_\lambda^TB_\lambda$ 가 $F^G(\lambda)\oplus F^G(\lambda^{-1})$ 와 어떤 관계인가 (정리 7 의 일반화/반례). 왜: 연구할 양 3(b) 를 닫음. 시작: 이중 커버 $G\sqcup G^{op}$, 평행 호가 있는 예. 난점: 등방 벡터의 일반 처리, 비반단순 경우(char | n).
4. **다중 이득 규칙 (Cayley 디그래프)** — 호마다 서로 다른 이득 $\lambda_s$ 를 가진 라벨 호 (Cay(A,S), 푸리에 분해의 일반화). 왜: $F^V=\bigoplus_\chi F^G(\chi)$ 가 일반 아벨군으로 확장되는지 보고, 정리 6 의 표현론을 구조화. 시작: $\mathbb Z_n^2$ 격자. 난점: 호마다 이득이 다르면 감김 gcd 가 다변수 격자 문제가 됨.
5. **텐서곱·함수 호모 객체** — $\omega(G\times H)$, $F^{G\times H}$ 와 $F^G\otimes F^H$ 의 관계. 왜: 문주님의 곱 호환성 항목. 시작: 닫힌 걸음의 사영(감김 일치) 을 이용한 정리 증명 시도. 난점: 곱의 성분 구조(연결성)가 복잡.
