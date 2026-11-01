# [R2-researcher1] 추측 1 의 일반 증명: 유한체 위 K₃-행렬 섬유의 궤도 수 = |E[2](F_q)|
- 작성자: researcher1 / 라운드: R2 (포메이션 I 분담) / 역할: 추측 1 증명 (수신: 대수검존)
- 코드: rooms/researcher1/run_r2.py (q=3,5,7 전수 확인은 증명의 단계 확인용일 뿐, 근거 아님)

## 요약
- [증명] 추측 1 은 q 홀수(표수 3 포함), f 제곱무인수일 때 참이다. 두 가지 독립 증명: (A) 기하적 증명 — F̄ 위 이행성, 안정자 = E[2], 유리점 존재, Lang; (B) 초등 증명 — 궤도 ↔ {c ∈ L^×/L^{×2} : Nm(c)·disc(f) ≡ 2 (제곱류)}, Lang 불필요.
- [증명] 궤도 불변량이 명시된다: 궤도 ↔ c ∈ L^×/L^{×2} (L=F_q[t]/f). 개수 = 2^{r−1} (r = f 의 기약인수 수) = 1+#근 = |E[2](F_q)|.
- [증명] 정정: 섬유 크기는 모든 제곱무인수 f 에서 q(q²−1) (F₅: 120, F₇: 336, F₃: 24). STATUS 의 "섬유 크기 145" 는 비제곱무인수 f 25개의 섬유 크기이다 (아래 5절). 궤도 크기 = q(q²−1)/|E[2](F_q)|.
- [증명] 유리점은 다항식 단면으로 직접 구성: $M(a,b,c)=\begin{pmatrix}2c&b+2c&0\\ b+2c&2(a+b+c+1)&1\\0&1&0\end{pmatrix}$ 가 $f=t^3+at^2+bt+c$ 를 준다 (임의의 환에서, 표수 무관).
- 막힌 곳 없음. 문헌 의존은 [기억-미검증] 로 표시 (SO₃ 연결성, |O₃(F_q)|=2q(q²−1)).

## 본문

### 0. 설정과 기초 사실
$F$ 는 체, $\mathrm{char}\,F\neq 2$, $A=J-I$, $\det A=2\neq0$ (표수 3 에서도 $2\ne0$ 이므로 A 는 비퇴화). $V=F^3$ 위 쌍선형형식 $\langle x,y\rangle=x^TAy$. $O_A=\{Q: Q^TAQ=A\}$.
- [증명] **작용의 번역.** 문제의 작용 $M\mapsto PMP^T$ ($PAP^T=A$) 는 $N=A^{-1}M$ 에서 $N\mapsto Q^{-1}NQ$ ($Q=P^{-T}\in O_A$) 이다. 풀이: $PAP^T=A$ 에서 $PA=AP^{-T}$, 따라서 $PMP^T=PAN P^T=A\,P^{-T}NP^{T}$, 즉 $N\mapsto Q^{-1}NQ$ ($Q=P^{-T}$). 그리고 $P\mapsto P^{-T}$ 는 군 $\{PAP^T=A\}$ 와 $O_A$ 사이의 동형. 따라서 O(A)-궤도 = $O_A$-켤레 궤도.
- [증명] $M$ 대칭 ⟺ $N$ 이 $\langle,\rangle$ 에 관해 자기수반 ($AN=M$ 대칭). $\det(tA-M)=\det A\det(t-N)=2\,\chi_N(t)$ 이므로 $S_f=\{M:\chi_{A^{-1}M}=f\}$ = 특성다항식이 $f$ 인 자기수반 $N$ 들의 집합 (M↔N 전단사).
- [증명] **f 제곱무인수 ⟹ 모든 $N\in S_f$ 는 정칙 반단순.** 유한체는 완전체이므로 $F_q$ 위 제곱무인수 ⟺ $\bar F_q$ 위 서로 다른 근 3개 $\lambda_1,\lambda_2,\lambda_3$ (분리가능). 최소다항식 = 특성다항식 = f 이므로 N 은 순환(cyclic)이다.
- 기호: $L=F[t]/(f)=F[\theta]$ (étale 3차원 대수, $\theta$=t 의 상), $R=\{\lambda_i\}$ 근집합, $L\otimes\bar F=\bar F^R$.
- **$E[2]$ 의 정확한 정의.** $E:\ w^2=f(t)$ (또는 $2f$; 2배 뒤틀림은 $E[2]$ 를 바꾸지 않는다: $-1$ 이 $E[2]$ 에서 자명). $E[2](\bar F)=\{0\}\cup\{P_i=(\lambda_i,0)\}$, 군법칙 $P_1+P_2=P_3$. 군스킴 $\mathcal R=\mathrm{Res}_{L/F}\mu_2$ 는 $\mathcal R(\bar F)=\{x\in L\otimes\bar F: x^2=1\}=\{\pm1\}^R$, 노름 $\mathrm{Nm}:\mathcal R\to\mu_2$ = 성분곱. $\mathcal R^{1}:=\ker\mathrm{Nm}=\{\varepsilon\in\{\pm1\}^R:\varepsilon_1\varepsilon_2\varepsilon_3=1\}$ (위수 4). 사상 $\iota:E[2]\to\mathcal R^1$, $0\mapsto(+,+,+)$, $P_i\mapsto\varepsilon^{(i)}$ ($i$ 번째만 $+$, 나머지 둘 $-$). [증명] $\iota$ 는 군 동형: $\varepsilon^{(1)}\varepsilon^{(2)}=(-,-,+)=\varepsilon^{(3)}$. 갈루아 작용은 양쪽 모두 근의 치환으로만 작용하므로 (±1 은 고정) $\iota$ 는 갈루아 동변 (갈루아 가군 동형). **이것이 "E[2] 와 갈루아 가군으로 동형" 의 정확한 뜻.**
- [증명] $|E[2](F_q)|=1+\#\{F_q\text{-근}\}=2^{r-1}$, $r$ = 기약인수 수 (r=3: 근 3개 → 4; r=2: 근 1개 → 2; r=1: 근 0개 → 1).

### 1. (A-1) $S_f(\bar F)$ 는 하나의 $SO(A)(\bar F)$-궤도 — [증명]
$N\in S_f(\bar F)$, 고유벡터 $v_i$ ($Nv_i=\lambda_iv_i$). 자기수반성: $\lambda_i\langle v_i,v_j\rangle=\langle Nv_i,v_j\rangle=\langle v_i,Nv_j\rangle=\lambda_j\langle v_i,v_j\rangle$, $\lambda_i\ne\lambda_j$ ⟹ $\langle v_i,v_j\rangle=0$ ($i\neq j$). 형식이 비퇴화이고 $v_i$ 들이 기저이므로 $\langle v_i,v_i\rangle\ne0$. $\bar F$ 대수적 닫힘 ⟹ $\langle v_i,v_i\rangle=1$ 로 정규화 (제곱근; 표수 홀수 불필요한 단계, 표수≠2 는 비퇴화에서 이미 사용). $N'$ 도 같은 $f$ 이면 정규직교 고유기저 $v_i'$; $T:v_i\mapsto v_i'$ 는 등거리이고 $TNT^{-1}=N'$. $\det T=-1$ 이면 $T\to -T$ (n=3 홀수이므로 $\det(-T)=+1$). 따라서 $SO(A)(\bar F)$ 가 이행적. 또한 $S_f\ne\emptyset$ (3절). ∎
- 차원 점검: $\dim S_f=6-3=3=\dim SO_3$ ✓ (안정자가 유한).

### 2. (A-2) 안정자군 — [증명]
**$O_A$ 안정자.** $T\in O_A$, $TN=NT$. 정칙 N 의 가환자 = $F[N]$ (순환), $\bar F$ 위에서는 정규직교 고유기저에서 대각행렬 $\mathrm{diag}(\varepsilon_i)$. $T^TAT=A$ ⟺ $\varepsilon_i^2=1$. 따라서 $\mathrm{Stab}_{O_A}(N)=\{\pm1\}^3=\mathrm{Res}_{L/F}\mu_2(\bar F)$ (위수 8). 스킴으로도: $F[N]^\times\ni x$ 는 $N$ 의 다항식이라 자기수반 ($x^*=x$), 그러므로 $x\in O_A\iff x^2=1$. 즉 $\mathrm{Stab}_{O_A}(N)=\{x\in L: x^2=1\}=\mathrm{Res}_{L/F}\mu_2$ ($L\cong F[N]$ 가 $F$-구조까지 일치; $\mu_2$ 는 표수≠2 에서 étale 이라 기약·매끄러움 문제 없음).
**$SO$ 안정자.** $V$ 는 $L$ 위 자유 가군 (순환) 이므로 $\det(T)=\mathrm{Nm}_{L/F}(x)$. 따라서
$$\mathrm{Stab}_{SO(A)}(N)=\ker(\mathrm{Nm}:\mathrm{Res}_{L/F}\mu_2\to\mu_2)=\mathcal R^1\ \cong\ E[2]\quad(\text{0절의 }\iota).$$
**$O=SO\times\{\pm1\}$.** $n=3$ 홀수: $\det(-I)=-1$, $-I\in O_A$ 중심. $O_A=SO\times\{\pm I\}$ (F-점에서도: $T\mapsto(\det T\cdot T,\det T)$). $-I$ 는 $N\mapsto(-I)^{-1}N(-I)=N$ 로 자명 작용 (원래 식으로는 $M\mapsto(-I)M(-I)^T=M$). ⟹ $O(F_q)$-궤도 = $SO(F_q)$-궤도. ∎

### 3. (A-3) 유리점 존재 — [증명] (명시적 단면)
$f=t^3+at^2+bt+c$, $a,b,c\in F$ (임의의 $F$, 임의의 표수≠2 — 사실 정수 항등식).
$$M(a,b,c)=\begin{pmatrix}2c&b+2c&0\\ b+2c&2(a+b+c+1)&1\\0&1&0\end{pmatrix},\qquad \tfrac12\det(tA-M(a,b,c))=t^3+at^2+bt+c.$$
유도: 희소 패턴 $[[p_0,p_1,0],[p_1,p_2,1],[0,1,0]]$ 에서 sympy 로 $\tfrac12\det(tA-M)=t^3+(\tfrac{p_0}2-p_1+\tfrac{p_2}2-1)t^2+(p_1-p_0)t+\tfrac{p_0}2$ 를 얻고 (삼각 연립), $p_0=2c$, $p_1=b+2c$, $p_2=2(a+b+c+1)$ 로 푼다. 손으로 전개해도 확인 가능한 삼각 구조. [계산 확인] F₃,F₅,F₇ 의 모든 $f$ (27,125,343 개)에 대해 $M(a,b,c)\in S_f$.
(이 단면은 "Kostant 단면" 의 구체형: $M\mapsto A^{-1}M$ 이 Hessenberg/동반행렬형을 닮은 3모수 족.) 제곱무인수 가정 불필요 — 모든 $f$ 에서 $S_f(F)\ne\emptyset$. ∎

### 4. (A-4) Lang 정리로 궤도 ↔ $H^1$ — [증명, Lang 은 인용]
$G=SO(A)$ ($F_q$ 위 연결 매끄러운 군; 연결성은 $SO_n$ 연결성의 표준 사실 [기억-미검증], $n=3$ 이면 $\bar F$ 위 $SO(A)\cong SO_3\cong PGL_2$). Frobenius $\Phi$. $x_0=N_0\in S_f(F_q)$ (3절), $H=\mathrm{Stab}_G(x_0)(\bar F)\cong\mathcal R^1(\bar F)$ ($\Phi$ 작용 포함, 2절).
- 사상 $\kappa$: $x\in S_f(F_q)$ ⟹ 1절로 $x=gx_0$ ($g\in G(\bar F)$); $\Phi x=x$ 이므로 $\Phi(g)x_0=gx_0$, 즉 $h:=g^{-1}\Phi(g)\in H$. $g\to gb$ ($b\in H$) 이면 $h\to b^{-1}h\Phi(b)$. $H$ 가 가환이므로 $H$ 에 덧셈 표기: $h\to h+(\Phi-1)b$. 따라서 $\kappa(x)\in H/(\Phi-1)H=H^1(F_q,H)$ (갈루아군 $\hat{\mathbb Z}$ 의 코호몰로지는 프로베니우스 켤레류).
- 단사: $\kappa(x)=\kappa(y)$ ($x=gx_0,y=g'x_0$). $g$ 를 $gb$ 로 바꿔 $h=h'$ 로 맞추면 $\Phi(g'g^{-1})=g'h'h^{-1}g^{-1}=g'g^{-1}$, 즉 $g'g^{-1}\in G(F_q)$ 이고 $x\mapsto y$. 
- 전사 (**Lang–Steinberg**, $G$ 연결 ⟹ $g\mapsto g^{-1}\Phi(g)$ 가 $G(\bar F)$ 위 전사): $h\in H$ 에 $g^{-1}\Phi(g)=h$ 인 $g$ 를 잡고 $x=gx_0$; $\Phi x=\Phi(g)x_0=ghx_0=x$ ⟹ $x\in S_f(F_q)$, $\kappa(x)=[h]$.
- 이로써 $\#\{SO(F_q)\text{-궤도}\}=|H/(\Phi-1)H|$. 유한 가환군의 준동형 $\Phi-1$ 에 대해 $|H/\mathrm{im}|=|\ker|$ 이므로 $=|H^{\Phi}|=|E[2](F_q)|$. 2절의 $O=SO\times\pm1$ 로 $O(F_q)$-궤도 수와 같다.
- (동치 서술) 정확열 $1\to\mathrm{Stab}\to SO\to X\to1$ 에서 $\ker(H^1(F_q,\mathrm{Stab})\to H^1(F_q,SO_3))=H^1(F_q,\mathrm{Stab})$ ($H^1(F_q,SO_3)=0$ by Lang). 위는 스킴론(몫 $G/H\cong X$) 없이 점 단위로 쓴 같은 논증이다. 참고: $O$ 로 쓰면 $H^1(F_q,O)=H^1(\mu_2)=\mathbb Z/2\ne0$ 이고 $H^1(\mathrm{Stab}_O)=H^1(E[2])\times H^1(\mu_2)$ 의 두번째 성분이 상쇄되어 같은 결과.
**가정 점검.** (i) 표수≠2: A 비퇴화, $\mu_2$ étale, $\det A=2$ 가역; 표수 2 에서는 $A=J-I$ 가 3×3 에서 $\det=2=0$ 이라 퇴화. (ii) 표수 3: 위 어느 단계도 3 의 가역성을 쓰지 않는다 (눌린 삼차식 $X^3+pX+q$ 와 정리 1 의 $I=-12p$ 만 3 에서 퇴화; 본 증명은 $f$ 를 눌리지 않은 채로 둔다). [계산 확인] q=3: 1,2,4 궤도 확인. (iii) 제곱무인수 필수 (정칙반단순성). (iv) 연결성(Lang): $SO_3$ 연결; $O_3$ 는 비연결이라 직접 못 쓴다.

### 5. 두번째 증명 (B): 초등, Lang 불필요 — [증명]
**정리 B.** $F=F_q$, $q$ 홀수, $f$ 제곱무인수. 사상
$$\{O_A(F)\text{-궤도 on }S_f(F)\}\ \longrightarrow\ \{c\in L^\times/L^{\times2}:\ \mathrm{Nm}(c)\cdot\mathrm{disc}(f)\equiv 2\ \mathrm{mod}\ F^{\times2}\}$$
는 전단사. 우변의 크기 $=2^{r-1}=|E[2](F_q)|$.
증명.
1. N 이 순환이므로 $(V,\langle,\rangle,N)\cong(L,B,\theta)$ ($L$-가군 동형, 순환벡터 $v_0\mapsto1$). N 자기수반 ⟹ $B(x,y)=B(1,xy)=\ell(xy)$, $\ell=B(1,\cdot)$. 대각합형식 $(x,y)\mapsto\mathrm{Tr}_{L/F}(xy)$ 는 비퇴화 ($L$ 이 F 위 분리가능 ⟸ 완전체) 이므로 $\ell=\mathrm{Tr}(c\,\cdot)$ 인 $c\in L$ 이 유일하고, $B$ 비퇴화 ⟺ $c\in L^\times$. 즉 $B=B_c:=\mathrm{Tr}(c\,xy)$.
2. 삼중쌍 $(L,B_c,\theta)\cong(L,B_{c'},\theta)$ 인 동형 (θ 와 가환 ⟹ $L$-선형 ⟹ 곱셈 $u\in L^\times$) 이 존재 ⟺ $c'=cu^{2}$. 따라서 {같은 $(F^3,A)$ 위의 $N\in S_f(F)$ 의 $O_A(F)$-켤레류} ↔ $\{c\in L^\times/L^{\times2}: (L,B_c)\cong(F^3,A)\}$. (켤레류=등거리 동형류; $M\mapsto N$ 번역은 0절.)
3. 형식의 판별식: 기저 $1,\theta,\theta^2$ 에서 $\det(\mathrm{Tr}(c\theta^{i+j}))=\mathrm{Nm}(c)\det(\mathrm{Tr}(\theta^{i+j}))=\mathrm{Nm}(c)\,\mathrm{disc}(f)$ ($\mathrm{disc}(f)=\prod_{i<j}(\lambda_i-\lambda_j)^2\neq0$).
4. **유한체 위 비퇴화 삼차 이차형식은 판별식(∈F^×/F^{×2})으로 분류된다** [증명 스케치: 대각화 $\langle a_1,a_2,a_3\rangle$. 이진형식 $\langle a,b\rangle$ 은 1 을 표현 ($ax^2$ 와 $1-by^2$ 의 값집합이 각각 $(q+1)/2$ 개라 비둘기집) ⟹ $\langle a,b\rangle\cong\langle1,ab\rangle$. 두 번 적용하면 $\langle a_1,a_2,a_3\rangle\cong\langle1,1,a_1a_2a_3\rangle$.] 그러므로 $(L,B_c)\cong(F^3,A)$ ⟺ $\mathrm{Nm}(c)\mathrm{disc}(f)\equiv\det A=2$ (제곱류). 이것이 우변 조건.
5. 크기: $L=\prod_{k=1}^rF_{q^{d_k}}$, $L^\times/L^{\times2}\cong(\mathbb Z/2)^r$. $\mathrm{Nm}:L^\times/L^{\times2}\to F^\times/F^{\times2}\cong\mathbb Z/2$ 는 전사 ($F_{q^d}^\times\to F^\times$ 노름이 전사이므로). 전사 준동형의 임의의 올의 크기 $=2^{r-1}$ (특히 비어있지 않음 — 이것이 (3)의 또 다른 증명). ∎
- 따름: 안정자 $\mathrm{Stab}_{O_A}(N)(F_q)=\{u\in L^\times:u^2=1\}=(\mathbb Z/2)^r$ 위수 $2^r$.
- (4절과의 일치) 우변은 $\ker(\mathrm{Nm})\subset L^\times/L^{\times2}$ 의 토서이고 $H^1(F_q,\mathrm{Res}\,\mu_2)=L^\times/L^{\times2}$, 정확열 $1\to E[2]\to\mathrm{Res}\,\mu_2\xrightarrow{\mathrm{Nm}}\mu_2\to1$ 에서 $\mathrm{Nm}:(L^\times)[2]\to\{\pm1\}$ 전사(어느 모양에서도 홀수 크기 프로베니우스 궤도가 있다) ⟹ $H^1(F_q,E[2])\cong\ker(L^\times/L^{\times2}\to F^\times/F^{\times2})$ [증명]. 고전적 2-하강의 "$x-\theta$" 사상과 같은 모양 [기억-미검증].

### 6. (5) 궤도 크기와 섬유 크기 — [증명 + 계산 확인]
$|O_A(F_q)|=2q(q^2-1)$ [기억-미검증: $SO_3(F_q)\cong PGL_2(F_q)$, 위수 $q(q^2-1)$. 모든 삼차 형식이 서로 스칼라배이므로 $SO$ 는 형식에 무관]. 궤도 크기 = $|O_A(F_q)|/|\mathrm{Stab}_O(F_q)|=2q(q^2-1)/2^{r}$. 궤도 수 $2^{r-1}$ ⟹
$$|S_f(F_q)|=2^{r-1}\cdot\frac{2q(q^2-1)}{2^r}=q(q^2-1)\quad(\text{모든 제곱무인수 }f).$$
(안정자가 가환이므로 코호몰로지 뒤틀림 $\mathrm{Stab}_c$ 도 모두 $E[2]$ 와 같은 가군 — 궤도 크기가 궤도마다 같은 이유.) 근 구조별 ($r$=3,2,1 ↔ 근 3,1,0 ↔ 궤도 4,2,1) 궤도 크기:
| q | 근3 (4궤도) | 근1 (2궤도) | 근0 (1궤도) | 섬유 |
|---|---|---|---|---|
| 3 | 6,6,6,6 | 12,12 | 24 | 24 |
| 5 | 30×4 | 60,60 | 120 | 120 |
| 7 | 84×4 | 168,168 | 336 | 336 |
[계산 확인] 위 표는 run_r2.py 로 $O(A)(F_q)$ (반사 생성) 궤도를 전부 세어 얻은 결과와 일치 (제곱무인수 f: q=3: 18, q=5: 100 (근0:40, 근1:50, 근3:10), q=7: 294 (112,147,35); 어긋남 0). 개수 확인: $\#\{\text{제곱무인수 monic 삼차}\}=q^3-q^2$.
**정정 (STATUS/Bridge).** "섬유 크기 145" 는 제곱무인수 f 에 대해서는 틀렸다 (120). 145 는 **비제곱무인수 f 25개 전부**의 섬유 크기이다: [계산 확인] q=3,5,7 에서 모든 비제곱무인수 f 의 섬유 크기 = $q^3+q^2-q$ (33, 145, 385; 개수 $q^2$ 개). 무결성 점검: $(q^3-q^2)q(q^2-1)+q^2(q^3+q^2-q)=q^6=|\mathrm{Sym}_3(F_q)|$ ✓ (q=5: 12000+3625=15625). 비제곱무인수에서의 일반 증명은 안 했다 [추측].

### 7. 단계별 가정 일람
| 단계 | 쓰는 가정 | 위반 시 |
|---|---|---|
| 번역 M↔N | A 가역 | — |
| 이행성(1) | f 서로 다른 근, A 비퇴화, 표수≠2 | 근 겹침: 비반단순/비정칙 N 이 생겨 다궤도 |
| 안정자(2) | N 정칙반단순, 표수≠2 (μ₂ étale) | 표수 2: A 퇴화 |
| 유리점(3) | 없음 (임의 f) | — |
| Lang(4) | SO₃ 연결·매끄러움 (표수≠2), 유한체 | O₃ 직접은 불가; 비유한체는 $H^1(k,SO_3)\ne0$ |
| 방법 B | 유한체: 형식이 판별식으로 분류, 노름 전사 | $\mathbb Q_p,\mathbb Q$ 에서는 하세 불변량이 추가 조건 |
표수 3: 모든 단계 통과 (q=3 확인). $G=O(A)$ 전체의 작용이 아니라 F_q-점의 작용이므로 $SO$ 와 구분 없음 (2절).

## 후속연구 지점
1. **$\mathbb Q_p$, $\mathbb Q$ 로의 이행 (researcher3 와 연계; 우선순위 최상).** 방법 B 가 그대로 확장된다: 궤도 ↔ $\{c\in L^\times/L^{\times2}: (L,B_c)\cong(k^3,A)\}$. 조건은 판별식 $\mathrm{Nm}(c)\mathrm{disc}(f)\equiv2$ 에 **하세–비트 불변량 일치** 가 추가 (유한체에서는 자동). 이것이 $\ker(H^1(k,E[2])\to H^1(k,SO_3)=\mathbb Z/2)$ 의 초등적 정체여야 한다. 시작: $\mathrm{Tr}(c\,xy)$ 의 비트 불변량을 $c$ 의 $L^\times/L^{\times2}$ 성분들의 힐베르트 기호로 계산. 난점: 비트 불변량의 $c$-의존 공식(노름/판별식 성분들의 힐베르트 기호 곱).
2. **비제곱무인수 $f$ 의 궤도 분류와 섬유 크기 $q^3+q^2-q$ 의 증명.** 왜: 6절에서 [계산 확인] 된 균일성이 이론적으로 설명되지 않았다 (전체합 $q^6$ 로 consistency 만 확인). 시작: Jordan 형 (이중근: 반단순 $\mathrm{diag}$ 형 vs 영멱, 삼중근: $\lambda I$ + 정칙멱영) 별로 $A$-자기수반 연산자와 안정자(통상 $\mathbb G_a$ 포함) 계산; $\lambda A$ 이동으로 $\lambda=0$ 환원. 난점: 비정칙 N 에서는 순환성 불성립, 안정자가 비가환/비reductive.
3. **점 개수 ↔ 궤도 합산식 (Bhargava–Gross 형 평균).** $\sum_f|S_f|=q^6$ 과 $|S_f|=q(q^2-1)$ 로부터 ($q^3-q^2$ 개 제곱무인수) 기하적 해석과 $K_3$ 의 사차식 모듈러 공간 $\mathrm{Sym}_3/A$ 의 원뿔 매개화와의 일치 검증. 난점: 문헌 비교는 기억 의존.
4. **$K_4$ (또는 일반 $n$) 로의 일반화.** 본 증명은 $n$ 에 대한 구조만 썼다: 방법 B 는 $A$ 가 $n$차 비퇴화이면 $L=F[t]/f$ ($\deg f=n$), $B_c$, 판별식 $\mathrm{Nm}(c)\mathrm{disc}(f)\equiv\det A$ 로 그대로 (궤도 수 $=2^{r-1}$). $n$ 짝수이면 $O=SO\times\pm1$ 분해가 깨지고 $-1\in SO$ 가 자명 작용 → 안정자/궤도 수 변경. 시작: $n=4$, $A=J-I$ ($\det=-3$), 표수 3 에서 퇴화. 난점: 안정자 $\mathrm{Res}\,\mu_2$ 의 $\det$ 조건이 $n$ 짝수에서 다름.
5. **궤도 불변량 $c$ 의 구체적 계산 검증.** 임의의 $M$ 에서 $c(M)\in L^\times/L^{\times2}$ 를 명시적으로 (예: $c=\ell(\cdot)$ 의 $v_0$ 선택에 의존하지 않는 형태) 뽑는 알고리즘 구현 후 궤도 분리 확인 (증명은 이미 있으므로 구현 점검용). 난점: $v_0$ 선택의 정규화.
