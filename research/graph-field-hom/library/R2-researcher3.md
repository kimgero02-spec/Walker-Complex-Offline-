# [R2-researcher3] 환 사상에 대한 함자성·평탄성(Tor 정리), 당김의 환 위 조건, A_G 와 임계군

- 작성자·라운드·역할: researcher3 / R2 / 포메이션 I 분담 — 환 확장의 함자성·평탄성, $A_G$ 와 임계군. 수신: 대수검존
- 계산: `rooms/researcher3/r2_tables.py` (R1 의 `snf.py` 재사용; 정수 스미스 꼴 직접 구현, sympy 없음). 계산은 표 채우기와 증명 확인에만 썼다.

## 요약
1. **Tor 정리 [증명]**: 정수 규칙 $(a,b)$, 환 사상 $R\to R'$ 에 대해 자연 사상 $\theta:R^G\otimes_RR'\to R'^G$ 의 핵과 쌍대핵은 정확히 $\ker\theta\cong\mathrm{Tor}_2^R(Q,R')$, $\mathrm{coker}\,\theta\cong\mathrm{Tor}_1^R(Q,R')$ ($Q=\mathrm{coker}(B_R:R^V\to R^E)$). 따라서 $\theta$ 가 동형 $\iff$ 두 Tor 가 0. 모든 $R'$ 에서 동형 $\iff Q$ 평탄 $\iff A_G\otimes R$ 사영(projective). $R=\mathbb Z$ 면 $\iff$ $R'$ 에서 $A_G$ 의 지수(exponent) $e$ 가 비영인자. 깨지는 예: $\mathbb Z\to\mathbb Z/2$, $\mathbb Z/4\to\mathbb Z/2$ (사상이 영사상), $\mathbb Z\to\mathbb Z[1/2]$ 는 동형.
2. **당김 $f^*$ [증명]**: $f^*=\mathrm{Hom}(A_f,R)$. 단사 $\iff\mathrm{Hom}_{\mathbb Z}(C_f,R)=0$ ($C_f=\mathrm{coker}A_f$, "상과 만나지 않는 성분의 상대 $A$"). 체의 조건 "모든 균형 성분이 상과 만난다"는 환에서 "$C_f$ 가 유한군이고 지수가 $R$ 에서 비영인자"로 바뀐다. 기존 규칙에서는 비이분 성분이 상을 안 만나도 $R[2]=0$ 이면 괜찮고, $\mathbb Z/4,\mathbb Z/6$ 에서는 $R[2]\ne0$ 이라 새 현상이 생긴다. 전사성은 $\mathrm{Ext}^1_{\mathbb Z}(C_f,R)$ 이 장애.
3. **임계군 [증명]**: $L=B^TB$ 에 대해 $0\to \mathbb Z^E/(\mathrm{im}B+\ker B^T)\to\mathrm{coker}(B^TB)\to A_G\to0$ 은 완전열이고, 무방향 $L$ 규칙에서 $A_G=\mathbb Z^c$ 는 자유이므로 이 열은 쪼개져 **임계군 $K(G)=\mathbb Z^E/(\text{cut}+\text{cycle})$** 이다. $\mathbb Z/N$ 위 $F^G$ 자체($=\mathrm{Hom}(A_G,\cdot)$)는 $K$ 를 **전혀 못 본다**.
4. **불가능 정리 [증명]**: $p\nmid ab$ 이면 연결 그래프의 $A_G\otimes\mathbb Z_{(p)}$ 는 **순환군**이다. 그러므로 어떤 정수 이항 규칙·방향으로도 $\dim_{\mathbb F_p}F^G\le c(G)$ ($p\nmid ab$). $K_{3,3}$ 의 $K=\mathbb Z/3\oplus\mathbb Z/3\oplus\mathbb Z/9$ (3-계수 3)는 이항 간선 규칙으로 읽을 수 없다. 읽으려면 **조화(별, closed-neighborhood) 규칙** $\deg(v)\varphi(v)=\sum_{w\sim v}\varphi(w)$ 가 필요하고, 그러면 $(\mathbb Z/N)^G_{\rm harm}\cong(\mathbb Z/N)^c\oplus K^\vee$ ($\mathrm{exp}K\mid N$) 로 $K$ 가 복원된다 (표 4 개 그래프에서 확인).

---

## 본문

### 0. 설정
유한 방향 그래프 $G=(V,E)$ (다중간선·루프 허용), 정수 규칙 $(a,b)$, $B=B_{a,b}\in\mathbb Z^{E\times V}$ (행 $=a\,e_u+b\,e_v$), $A_G=\mathrm{coker}(B^T:\mathbb Z^E\to\mathbb Z^V)$. 환 $R$ (가환, 1 포함)에 대해 $R^G=\{\varphi:V\to R\mid a\varphi(u)+b\varphi(v)=0\}=\ker B_R=\mathrm{Hom}_{\mathbb Z}(A_G,R)=\mathrm{Hom}_R(A_G\otimes R,R)$ [증명: 정의대로; 관계가 호 조건]. 스미스 꼴 $A_G\cong\mathbb Z^r\oplus\bigoplus_i\mathbb Z/d_i$, $d_1|d_2|\cdots|d_k=:e$ (지수). $\mathrm{Hom}(\mathbb Z/d,R)=R[d]:=\{x:dx=0\}$ 이므로
$$R^G\cong R^r\oplus\bigoplus_iR[d_i].\tag{0.1}$$
R1 의 체 공식 $\dim=r+\#\{i:p\mid d_i\}$ 는 $R=F$ 일 때 $F[d]=F$ ($p|d$) 또는 $0$.

### 1. 함자성과 평탄성

**1.1 공변성 [증명].** 환 사상 $\sigma:R\to R'$ (단위 보존)은 정수 위에서 항등이므로 $\sigma(a x+b y)=a\sigma(x)+b\sigma(y)$. 호 조건이 보존되어 $\sigma_*\varphi=\sigma\circ\varphi\in R'^G$, 곧 $(-)^G=\mathrm{Hom}_{\mathbb Z}(A_G,-)$ 의 제한으로 공변함자 $\mathbf{CRing}\to\mathbf{Mod}$ ($\sigma_*$ 는 $\sigma$-반선형). 일반 규칙 $S_R\subset R\times R$ 에서는 $\sigma^{\times2}(S_R)\subset S_{R'}$ 가 필요충분 ($G=K_2$ 로 $\Rightarrow$). 정수 규칙은 자동.
선형화: $\theta=\theta_{R\to R'}:R^G\otimes_RR'\to R'^G$, $\varphi\otimes r'\mapsto r'\cdot\sigma\circ\varphi$.

**1.2 정리 (Tor 정리) [증명].** $M:=\mathrm{im}\,B_R\subset R^E$, $Q:=\mathrm{coker}\,B_R=R^E/M$ ($=\mathrm{coker}(B)\otimes_{\mathbb Z}R$; $A_G\otimes R$ 의 "전치" $\mathrm{Tr}$), $K:=R^G=\ker B_R$. 그러면 $R'$ 가 임의의 $R$-대수일 때
$$\ker\theta\ \cong\ \mathrm{Tor}^R_1(M,R')\ \cong\ \mathrm{Tor}^R_2(Q,R'),\qquad \mathrm{coker}\,\theta\ \cong\ \mathrm{Tor}^R_1(Q,R').$$
*증명.* (i) $0\to K\to R^V\to M\to0$ 에 $-\otimes R'$ 를 걸면 $\mathrm{Tor}_1(R^V,R')=0$ 이므로 $0\to\mathrm{Tor}_1(M,R')\to K\otimes R'\xrightarrow{\alpha}R'^V\to M\otimes R'\to0$ 완전. $\theta$ 는 $\alpha$ 의 공역 제한이므로 $\ker\theta=\ker\alpha\cong\mathrm{Tor}_1(M,R')$. (ii) $0\to M\xrightarrow{j}R^E\to Q\to0$ 에서 $0\to\mathrm{Tor}_1(Q,R')\to M\otimes R'\xrightarrow{j\otimes1}R'^E$ 완전, 곧 $\ker(j\otimes1)\cong\mathrm{Tor}_1(Q,R')$. $R'^G=\ker(R'^V\to M\otimes R'\to R'^E)$ 이고 $R'^V\to M\otimes R'$ 는 전사이므로 $R'^G/\mathrm{im}\,\alpha\cong\ker(j\otimes1)$. (iii) $R^E$ 가 평탄하므로 $\mathrm{Tor}_1(M,-)=\mathrm{Tor}_2(Q,-)$. ∎

**1.3 따름정리 [증명].**
- (a) $R'$ 평탄 $\Rightarrow\theta$ 동형 (Tor 소멸). 평탄이 아니어도 동형일 수 있다 (아래).
- (b) 다음은 동치: (i) 모든 $R$-대수 $R'$ 에서 $\theta_{R'}$ 동형; (ii) $\mathrm{Tor}_1^R(Q,-)=0$, 곧 $Q$ 평탄; (iii) $Q$ 사영; (iv) $A_G\otimes R$ 사영. (iii)⇒(iv): $M$ 이 $R^E$ 의 직합수이고 $R^V\to M$ 이 쪼개지므로 $B^T=(R^E\to M^*\hookrightarrow R^V)$ 의 상이 직합수. (iv)⇒(iii) 쌍대로 같다. (i)⇒(iv)는 $R'=R\oplus N$ (자명 확대)로 모든 $R$-가군 $N$ 에서 $\mathrm{Hom}(A_R,-)$ 가 오른쪽완전해짐 $\Rightarrow$ 사영.
- (c) **$R=\mathbb Z$**: $Q_{\mathbb Z}=\mathbb Z^s\oplus\bigoplus\mathbb Z/d_i$ (B 와 $B^T$ 의 스미스 꼴이 같다), $\mathrm{Tor}_2^{\mathbb Z}=0$, $\mathrm{Tor}_1(\mathbb Z/d,R')=R'[d]$. 따라서 $\theta:\mathbb Z^G\otimes R'=R'^r\hookrightarrow R'^G=R'^r\oplus\bigoplus R'[d_i]$ 는 항상 단사이고
$$\theta\text{ 전사(동형)}\iff R'[e]=0\ (e=\text{지수}),\quad\text{즉 } e \text{ 가 } R' \text{ 의 비영인자}.$$
특히 모든 $R'$ 에서 동형 $\iff A_G$ 무비틀림 ($e=1$).
- (d) $R$ 이 체 (또는 $R'$ 이 $R$ 위 자유) 이면 항상 동형. R1 의 체 사상 정리는 이 특수경우.
- (e) 사영 $R=\prod R_i$ (CRT, 예 $\mathbb Z/6=\mathbb Z/2\times\mathbb Z/3$): $R^G=\prod R_i^G$ [증명: $\mathrm{Hom}(A,\prod R_i)=\prod\mathrm{Hom}(A,R_i)$].

**1.4 구체 예 (모두 직접 계산).** 규칙 $(1,1)$ ($x+y=0$), $G=C_3$ (삼각형): $A_G=\mathbb Z/2$, $e=2$, $B$ 의 스미스 꼴 $[1,1,2]$.
1. $\mathbb Z\to\mathbb Z/2$: $\mathbb Z^G=0$, $(\mathbb Z/2)^G=\mathbb Z/2=\{0,1\}$ (상수). $0\otimes\to\mathbb Z/2$ 는 단사이나 전사 아님; coker $=\mathbb Z/2=\mathrm{Tor}_1(\mathbb Z/2,\mathbb Z/2)$ ✓. 일반: $\mathbb Z\to\mathbb Z/n$ 동형 $\iff\gcd(e,n)=1$.
2. $\mathbb Z\to\mathbb Z[1/2]$: 평탄이므로 모든 $G$ 에서 동형. $\mathbb Z\to\mathbb Z/3$ 는 $G=C_3$ 에서 $e=2$ 비영인자 ⇒ 동형 ($0\to0$). 그러나 $e=3$ 인 $G$ (예: 방향 $C_2$, 규칙 $(-2,1)$, $A=\mathbb Z/3$) 에서는 깨진다: $\mathbb Z^G=0$ 이나 $(\mathbb Z/3)^G=\mathbb Z/3$.
3. **$\mathbb Z/4\to\mathbb Z/2$, $G=C_3$**: $R=\mathbb Z/4$, $R^G=\mathrm{Hom}(\mathbb Z/2,\mathbb Z/4)=\{0,2\}$ (상수 2: $2+2=4=0$ ✓), $R^G\otimes\mathbb Z/2=\mathbb Z/2$, $R'^G=\{0,1\}=\mathbb Z/2$. $\theta(2\otimes1)=\overline 2=0$: **$\theta$ 는 영사상**(단사도 전사도 아님). Tor 정리 확인: $Q=\mathbb Z/2$ ($\mathbb Z/4$-가군), 주기 분해 $\cdots\xrightarrow2\mathbb Z/4\xrightarrow2\mathbb Z/4\to\mathbb Z/2$ 에서 $\mathrm{Tor}_n^{\mathbb Z/4}(\mathbb Z/2,\mathbb Z/2)=\mathbb Z/2$ ($n\ge0$): $\ker\theta=\mathrm{Tor}_2=\mathbb Z/2$, $\mathrm{coker}\,\theta=\mathrm{Tor}_1=\mathbb Z/2$ ✓ ($\mathbb Z/2\xrightarrow0\mathbb Z/2$). 이 예에서 $\mathbb Z/2$ 는 $\mathbb Z/4$ 위 평탄이 아니다.
4. **환원 사상 자체(텐서 없이)의 전사성 [증명]**: $0\to I\to R\to R/I\to0$ 에서 $R^G\to(R/I)^G\to\mathrm{Ext}^1_{\mathbb Z}(A_G,I)\to\mathrm{Ext}^1_{\mathbb Z}(A_G,R)$ 완전; $\mathrm{Ext}^1(\mathbb Z/d,I)=I/dI$. 예 3: $I=2\mathbb Z/4\cong\mathbb Z/2$, $\mathrm{Ext}^1(\mathbb Z/2,I)=I/2I=\mathbb Z/2\to R/2R=\mathbb Z/2$ 가 영사상이라 $(R/I)^G\to I/2I$ 가 전사: 환원 $R^G\to R'^G$ 는 영 ✓ (위와 일치). 무비틀림 $A_G$ 는 $\mathrm{Ext}^1=0$ 이라 환원이 언제나 전사.
5. 환 위 자기 확대 $\mathbb Z/4\to\mathbb Z/4[x]$ 등 평탄 확대는 (a) 에 의해 동형.

> 요지 [증명]: 체에서 "$\dim$ 이 표수만으로 정해진다"(R1 B3)는 체 위 모든 확대가 자유라서였다. 환에서는 평탄성(=$Q$ 의 Tor 소멸)이 정확한 조건이며, 정수 환 $\mathbb Z$ 에서 출발하면 조건은 "$A_G$ 의 지수가 $R'$ 의 비영인자"로 아주 구체적이다.

### 2. $R^{(-)}$ 의 반변성, 곱·합, 당김 $f^*$

**2.1 [증명]** $R^{G\sqcup H}\cong R^G\times R^H$ (호모는 성분마다 독립; $A_{G\sqcup H}=A_G\oplus A_H$). $R^\emptyset=0$. 환 사상에 대해 자연. $R^{(-)}=\mathrm{Hom}(-,(R,S_R))$ 이 표현가능이므로 쌍대극한 $\to$ 극한 (몫·접착 $\to$ 올곱).

**2.2 당김 $f^*$.** 방향 보존 호모 $f:G\to H$ 는 $A_f:A_G\to A_H$, $v\mapsto f(v)$ 를 준다 (관계 $au+bv$ 가 $H$ 의 관계로 감). $f^*\psi=\psi\circ f=\mathrm{Hom}(A_f,R)(\psi)$. $I=\mathrm{im}A_f$, $\mathcal K=\ker A_f$, $C_f:=A_H/I=\mathbb Z^{V(H)}\big/\big(\langle a\,x+b\,y: x\to y\in E(H)\rangle+\langle f(v)\rangle\big)$ ("상을 $0$ 으로 놓은 $H$ 의 상대 $A$").

**정리 2.A (단사) [증명].** $\ker f^*=\mathrm{Hom}(A_H/I,R)=\mathrm{Hom}_{\mathbb Z}(C_f,R)$. 따라서 $f^*$ 단사 $\iff\mathrm{Hom}_{\mathbb Z}(C_f,R)=0$. $C_f=\mathbb Z^{r'}\oplus\bigoplus\mathbb Z/d'_j$ 로 쓰면 이는 $R\ne0$ 일 때 **$r'=0$ 이고 $R[d'_{\max}]=0$** 과 동치 ($R[d'_j]\subset R[d'_{\max}]$).
- 체: $C_f$ 유한이고 $\mathrm{char}\nmid|C_f|$-지수. 직선 규칙의 연결 성분별 해석: 상을 만나는 성분은 $C=0$ (값이 $\lambda$-곱으로 전파되어 모두 $0$), 안 만나는 성분은 자기 $A$ 가 그대로 나옴.
- **규칙 $x=y$** ($\lambda=1$): 안 만나는 성분 $\Rightarrow C=\mathbb Z\Rightarrow\mathrm{Hom}=R\neq0$. 조건은 체와 똑같이 "모든 성분이 상과 만난다" — 환에서 달라지지 않음.
- **규칙 $x+y=0$**: 안 만나는 이분 성분 $\Rightarrow C=\mathbb Z$ (단사 깨짐); 안 만나는 비이분 성분 $\Rightarrow C=\mathbb Z/2$ (깨짐 $\iff R[2]\ne0$). 곧 **$f^*$ 단사 $\iff$ H 의 모든 이분 성분이 $f(G)$ 와 만나고, (상과 안 만나는 비이분 성분이 있으면) $2$ 가 $R$ 의 비영인자.** 체에서는 $\mathrm{char}\ne2$ 에서 이분 성분만 조건. 환에서 새로운 점: $R=\mathbb Z/4,\mathbb Z/6,\mathbb Z/2$ 는 $R[2]\neq0$ ⇒ 비이분 성분도 만나야 한다; $\mathbb Z,\mathbb Z/3,\mathbb Z[1/2]$ 에서는 불필요. (예: $G=\emptyset\to H=C_3$: $R^\emptyset=0$ 인데 $R^H=R[2]$, $\mathbb Z/6$ 에서 $\{0,3\}\ne0$ 이므로 단사 실패.)
- 충분조건: $f$ 가 정점 전사이면 $A_f$ 전사, $C_f=0$, 모든 $R$ 에서 단사 [증명].

**정리 2.B (전사) [증명].** $f^*$ 는 $\mathrm{Hom}(A_H,R)\xrightarrow{\rm res}\mathrm{Hom}(I,R)\hookrightarrow\mathrm{Hom}(A_G,R)$ 의 합성이고 (둘째는 $\mathcal K$ 에서 0 인 사상만 포함), 첫 사상의 쌍대핵은 $\mathrm{Ext}^1(C_f,R)$ 로 들어간다 ($\mathrm{Hom}(A_H,R)\to\mathrm{Hom}(I,R)\to\mathrm{Ext}^1_{\mathbb Z}(C_f,R)$ 완전). 따라서
$f^*$ 전사 $\iff$ (i) 모든 $\varphi\in R^G$ 가 $\mathcal K$ 를 죽이고, (ii) $\mathrm{Hom}(I,R)\to\mathrm{Ext}^1(C_f,R)$ 가 영사상. $C_f$ 가 자유(또는 모든 불변인자가 $R$ 의 단위)이면 (ii) 는 자동. 체 위 "$A_G\otimes F\to A_H\otimes F$ 단사"는 R1(C6)이며, 환에서는 $\mathrm{Tor}$ 와 $\mathrm{Ext}$ 의 두 항이 나뉜다.

**2.3 예 (전사가 깨지는 가장 단순한 예) [증명].** 규칙 $(-2,1)$ ($\varphi(v)=2\varphi(u)$), $H$ = 호 $x\to y$, $G$ = 점 $\{y\}$, $f:y\mapsto y$. $A_H=\langle x,y|y=2x\rangle=\mathbb Z$, $A_G=\mathbb Z$, $A_f=\times2$. $R^H=R$ (값 $t=\varphi(x)$, $\varphi(y)=2t$), $R^G=R$, $f^*=\times2:R\to R$. 따라서 $f^*$ 단사 $\iff 2$ 비영인자, 전사 $\iff2$ 가 단위. $\mathbb Z$: 단사만; $\mathbb Z[1/2]$, $\mathbb Z/3$: 동형; $\mathbb Z/2$: 영사상; $\mathbb Z/4$: 영도 아닌 $\times2$ 로 단사·전사 둘 다 아님; $\mathbb Z/6$: $\mathbb Z/2\times\mathbb Z/3$ 분해로 한 쪽은 영, 한 쪽은 동형. ($C_f=\mathbb Z/2$, $\mathrm{Ext}^1(\mathbb Z/2,R)=R/2R$ 가 전사성의 장애 — 정리 2.B ✓.)
또 $(1,1)$, $K_2\hookrightarrow C_3$: $f^*:R[2]\hookrightarrow R$ 항상 단사, 전사 $\iff2R=0$.

### 3. $A_G$ 와 임계군

**3.0 표기.** 무방향 그래프 $G$ ($n$ 정점, $m$ 간선, $c$ 성분)에 임의 방향을 줘 부호 결합행렬 $N=B_{1,-1}\in\mathbb Z^{E\times V}$ (행 $e_u-e_v$), 부호 없는 $N_+=B_{1,1}$. $L=N^TN$, $Q=N_+^TN_+$. 규칙 $x=y$ ($a=1,b=-1$) 와 $x+y=0$.

**3.1 정리 (일반 정수 행렬 $B$) [증명].** $B\in\mathbb Z^{E\times V}$ 에 대해
$$0\to T\to\mathrm{coker}(B^TB)\to\mathrm{coker}(B^T)=A_G\to0,\qquad T=\mathbb Z^E\big/(\mathrm{im}B+\ker B^T)$$
가 완전하다.
*증명.* $\mathrm{im}(B^TB)=B^T(\mathrm{im}B)\subset\mathrm{im}B^T$ 이므로 $\mathrm{coker}(B^TB)=\mathbb Z^V/B^TB\mathbb Z^V\twoheadrightarrow\mathbb Z^V/B^T\mathbb Z^E=A_G$, 핵 $=B^T\mathbb Z^E/B^T(B\mathbb Z^V)\cong\mathbb Z^E/(B\mathbb Z^V+\ker B^T)$ (제1동형: $B^T:\mathbb Z^E\to B^T\mathbb Z^E$ 의 핵이 $\ker B^T$). ∎

**3.2 따름 (L 규칙) [증명].** $B=N$: $A_G=\mathbb Z^V/\langle u-v\rangle=\mathbb Z^c$ 는 자유이므로 열이 쪼개져 $\mathrm{coker}L\cong\mathbb Z^c\oplus T$, 그리고 $T$ 는 유한(핵에 비틀림만 가능: 차수 계산으로 $\mathrm{rank}L=n-c$). 따라서
$$K(G):=\mathrm{tors}\,\mathrm{coker}L\ \cong\ T=\mathbb Z^E/(\text{cut 격자}\ \mathrm{im}N+\text{cycle 격자}\ \ker N^T),$$
고전적인 "임계군 $=\mathbb Z^E/(\text{cut}\oplus\text{flow})$" 표현이다 [기억-미검증: 알려진 정리(Bacher–de la Harpe–Nagnibeda)와 일치하는 것으로 보이나 문헌은 확인하지 않음; 위 증명은 독립적]. $|K|=$ 신장나무 수 (R1 에서 $P_5:1$, $C_6:6$, $Q_3:384$, $K_{3,3}:81$ 일치). 해석: cycle 격자 $\to$ 그 쌍대 $=\mathbb Z^E/\text{cut}$ 로 가는 교차형식(Gram) 의 쌍대핵이 $K$.
- 부호 없는 $Q$: $A_G=\mathbb Z^b\oplus(\mathbb Z/2)^{nb}$ ($b$ = 이분 성분 수, $nb$ = 비이분 성분 수). 이분 성분에서는 $Q\sim L$ (부호 변환 $\mathrm{diag}\pm1$ 로 합동). 비이분 성분에서는 열이 쪼개지지 않을 수 있다: 삼각형 $C_3$: $\mathrm{coker}Q=\mathbb Z/4$, $A=\mathbb Z/2$, $T=\mathbb Z/2$ (비분할); $C_5$: $\mathbb Z/4$ (표 4); $K_4$: $[2,2,12]$, $A=\mathbb Z/2$, $|T|=24$ [계산 확인].

**3.3 $F^G$ 로 읽기: 쌍대 완전불변량 [증명].** 
(a) $L$ 규칙의 $R^G=\mathrm{Hom}(\mathbb Z^c,R)=R^c$: **임계군 정보 0** (환과 무관).
(b) 조화 규칙: $R^G_{\rm harm}:=\ker(L_R)=\mathrm{Hom}_{\mathbb Z}(\mathrm{coker}L,R)=R^c\oplus\mathrm{Hom}(K,R)$ (3.2). 이는 R1 의 "해석 (b)" ($\ker B^TB$)이며 규칙으로 쓰면 별(star) 관계 $\deg(v)\varphi(v)=\sum_{w\sim v}\varphi(w)$ ($R\subset R^{N[v]}$ 의 $k$ 항 부분가군; R1 D 절의 초그래프 규칙).
(c) 정확열 $0\to R^G\to R^G_{\rm harm}\xrightarrow{N}\mathrm{Bic}_R\to0$, $\mathrm{Bic}_R:=\mathrm{im}N_R\cap\ker N_R^T$ (R-쌍순환/bicycle), 그리고 $\mathrm{Bic}_R\cong\mathrm{Hom}(K,R)$: $\mathrm{Hom}(-,R)$ 를 3.1 에 걸면 $\mathrm{Ext}^1(\mathbb Z^c,R)=0$ 이라 정확 [증명]. 체 $\mathbb F_p$: $\dim\mathrm{Bic}=\mathrm{rank}_pK$ — 고전적 쌍순환 공간 [기억-미검증 문헌, 위 증명은 독립].
(d) **복원**: $e=\exp K$, $e\mid N$ 이면 $\mathrm{Hom}(K,\mathbb Z/N)\cong K$ (비정규 동형), 따라서 $(\mathbb Z/N)^G_{\rm harm}\cong(\mathbb Z/N)^c\oplus K$ 이고 $c$ 를 알므로 유한 아벨군의 정리(Krull–Schmidt)로 $K$ 가 결정된다. 모든 $N$ 을 쓰면 $|{\rm Hom}(K,\mathbb Z/N)|$ 만으로도 $K$ 가 결정된다 [증명: $p$-부분의 각 $p^k$-수 $\sharp\{i:p^j\mid k_i\}$]. 곧 **환 $\mathbb Z/N$ 은 체가 못 하는 일을 한다**: $\mathbb F_p$ 는 $p$-계수만, $\mathbb Z/p^k$ 는 $p$-부분 전체를 본다.

**3.4 불가능 정리: 이항 규칙은 $K$ 를 읽지 못한다 [증명].** $G$ 연결, $\gcd(a,b)=1$, $p\nmid ab$. 호 $u\to v$ 가 $au+bv=0$ 을 주고 $a,b\in\mathbb Z_{(p)}^\times$ 이므로 $v=-(a/b)u$, $u=-(b/a)v$ 가 $A_G\otimes\mathbb Z_{(p)}$ 에서 성립. 연결이므로 한 정점 $r$ 이 모든 생성원을 $\mathbb Z_{(p)}$-배수로 생성 ⇒ **$A_G\otimes\mathbb Z_{(p)}$ 순환군**. 따라서 
- $\dim_{\mathbb F_p}F^G\le c(G)$ (모든 이항 정수 규칙, 모든 방향, $p\nmid ab$); 
- $\mathbb Z/p^k$ 위 $R^G$ 도 성분당 순환 가군.
무방향 대칭 규칙은 더 약해서 $A_G=\mathbb Z^c$ 또는 $\mathbb Z^b\oplus(\mathbb Z/2)^{nb}$. $K_{3,3}$ 의 $K=\mathbb Z/3^2\oplus\mathbb Z/9$ 의 3-부분은 순환이 아니므로 $G$ 자체에서 이항 규칙으로는 불가능. $p\mid ab$ 인 퇴화 소수에서는 비순환이 생기나 (V자 $A=\mathbb Z\oplus\mathbb Z/2$) 그 값은 소스·싱크 수 등 방향 정보이지 $K$ 가 아니다.
*가능한 우회와 장애물:* 이항 규칙만 쓰려면 $G$ 에서 자연스럽게 만든 보조 그래프 $\Gamma(G)$ 의 **성분 수**가 $K$ 의 순환 인수 개수가 되도록 해야 한다 (성분당 순환이므로). 그런 함자적 $\Gamma$ 는 알지 못한다 [추측: 호몰로지 덮개 $\Gamma_N\to G$ 로 가능할 수 있으나 정수 이득 없이는 이항 규칙이 안 된다 — 열린 문제].

### 4. 표 (직접 계산: 스미스 꼴 → (0.1) 로 $\mathrm{Hom}(\cdot,R)$)
$A$ = 표시 군, $\gcd$ 규칙 $\mathrm{Hom}(\mathbb Z/d,\mathbb Z/n)=\mathbb Z/\gcd(d,n)$. 모든 값은 `r2_tables.py` 에서 [계산 확인], 이론적 근거는 (0.1).

**표 1. 이항 규칙 $x=y$ ($a=1,b=-1$) 와 $x+y=0$ ($a=b=1$): $R^G$**

| $G$ | $A_G$ ($x=y$) | $A_G$ ($x+y=0$) | $R=\mathbb Z$ | $\mathbb Z/2$ | $\mathbb Z/3$ | $\mathbb Z/4$ | $\mathbb Z/6$ |
|---|---|---|---|---|---|---|---|
| $P_5$ | $\mathbb Z$ | $\mathbb Z$ | $\mathbb Z$ | $\mathbb Z/2$ | $\mathbb Z/3$ | $\mathbb Z/4$ | $\mathbb Z/6$ |
| $C_6$ | $\mathbb Z$ | $\mathbb Z$ | 동일 | 동일 | 동일 | 동일 | 동일 |
| $Q_3$ | $\mathbb Z$ | $\mathbb Z$ | 동일 | 동일 | 동일 | 동일 | 동일 |
| $K_{3,3}$ | $\mathbb Z$ | $\mathbb Z$ | 동일 | 동일 | 동일 | 동일 | 동일 |
| $C_5$ | $\mathbb Z$ | $\mathbb Z/2$ | $0$ | $\mathbb Z/2$ | $0$ | $\mathbb Z/2$ | $\mathbb Z/2$ |
| $K_4$ | $\mathbb Z$ | $\mathbb Z/2$ | $0$ | $\mathbb Z/2$ | $0$ | $\mathbb Z/2$ | $\mathbb Z/2$ |

(앞 네 그래프는 이분 연결이라 두 규칙 모두 $R^G=R$; $x=y$ 에서는 $C_5,K_4$ 도 $R$. $x+y=0$ 의 $C_5,K_4$ 행만 위 표값: $\mathrm{Hom}(\mathbb Z/2,R)=R[2]$.) 요점: 네 그래프를 **전혀 구분하지 못한다**. $\mathbb Z/4$ 에서 $C_5$ 는 $R[2]=\{0,2\}$ (환 특유: $\mathbb F_2$ 와도 $\mathbb Z/3$ 과도 다름), $\mathbb Z/6$ 은 CRT 로 $\mathbb Z/2\times 0$.

**표 2. 조화(Laplacian) 규칙 $R^G_{\rm harm}=\mathrm{Hom}(\mathrm{coker}L,R)$**; $\mathrm{coker}L=\mathbb Z\oplus K$ (연결 그래프, $c=1$)

| $G$ | $K(G)$ (스미스 꼴) | $\mathbb Z/2$ | $\mathbb Z/3$ | $\mathbb Z/4$ | $\mathbb Z/6$ | $\mathbb Z/9$ |
|---|---|---|---|---|---|---|
| $P_5$ | $0$ | $\mathbb Z/2$ | $\mathbb Z/3$ | $\mathbb Z/4$ | $\mathbb Z/6$ | $\mathbb Z/9$ |
| $C_6$ | $[6]$ | $(\mathbb Z/2)^2$ | $(\mathbb Z/3)^2$ | $\mathbb Z/4\oplus\mathbb Z/2$ | $(\mathbb Z/6)^2$ | $\mathbb Z/9\oplus\mathbb Z/3$ |
| $Q_3$ | $[2,8,24]$ | $(\mathbb Z/2)^4$ | $(\mathbb Z/3)^2$ | $(\mathbb Z/4)^3\oplus\mathbb Z/2$ | $\mathbb Z/6\oplus(\mathbb Z/2)^2\oplus\mathbb Z/6$ | $\mathbb Z/9\oplus\mathbb Z/3$ |
| $K_{3,3}$ | $[3,3,9]$ | $\mathbb Z/2$ | $(\mathbb Z/3)^4$ | $\mathbb Z/4$ | $\mathbb Z/6\oplus(\mathbb Z/3)^3$ | $\mathbb Z/9^2\oplus(\mathbb Z/3)^2$ |
| $C_5$ ($L$) | $[5]$ | $\mathbb Z/2$ | $\mathbb Z/3$ | $\mathbb Z/4$ | $\mathbb Z/6$ | $\mathbb Z/9$ |
| $K_4$ ($L$) | $[4,4]$ | $(\mathbb Z/2)^3$ | $\mathbb Z/3$ | $(\mathbb Z/4)^3$ | $\mathbb Z/6\oplus(\mathbb Z/2)^2$ | $\mathbb Z/9$ |

($Q_3$ 의 $\mathbb Z/4$ 칸 $=\mathrm{Hom}(\mathbb Z\oplus\mathbb Z/2\oplus\mathbb Z/8\oplus\mathbb Z/24,\mathbb Z/4)=\mathbb Z/4\oplus\mathbb Z/2\oplus\mathbb Z/4\oplus\mathbb Z/4$.) **네 그래프 $P_5,C_6,Q_3,K_{3,3}$ 는 $\mathbb Z/2,\mathbb Z/3$ 두 칸의 조합만으로 이미 구분된다** (차수: $P_5$: 2,3 / $C_6$: 4,9 / $Q_3$: 16,9 / $K_{3,3}$: 2,81). $\mathbb Z/4$ 만으로는 $P_5$ 와 $K_{3,3}$ 이 같다. 가장 깔끔한 것은 $\mathbb Z/9$ (또는 $\mathbb Z/N$, $N$ 가 지수의 배수) 하나로 $K$ 를 복원.

**표 3. 방향 예, 규칙 $(-2,1)$ ($\varphi(v)=2\varphi(u)$)**

| $G$ | $A_G$ | $\mathbb Z$ | $\mathbb Z/2$ | $\mathbb Z/3$ | $\mathbb Z/4$ | $\mathbb Z/6$ |
|---|---|---|---|---|---|---|
| V자 $0\to2\leftarrow1$ | $\mathbb Z\oplus\mathbb Z/2$ | $\mathbb Z$ | $(\mathbb Z/2)^2$ | $\mathbb Z/3$ | $\mathbb Z/4\oplus\mathbb Z/2$ | $\mathbb Z/6\oplus\mathbb Z/2$ |
| 방향 $C_2$ | $\mathbb Z/3$ | $0$ | $0$ | $\mathbb Z/3$ | $0$ | $\mathbb Z/3$ |
| 방향 $C_3$ | $\mathbb Z/7$ | $0$ | $0$ | $0$ | $0$ | $0$ |
| 혼합 삼각형 | $\mathbb Z/2$ | $0$ | $\mathbb Z/2$ | $0$ | $\mathbb Z/2$ | $\mathbb Z/2$ |

(V자와 방향 $C_n$ 은 R1 의 계산 값, 방향 $C_2$: $2^2-1=3$ 이론 일치. 혼합 삼각형은 R1 표.)

### 5. 판정과 공통 패턴

**공통 패턴.** (P1) 모든 정수 이항 규칙에서 $R^G=R^r\oplus\bigoplus R[d_i]$; 환이 바꾸는 것은 비틀림 부분 $R[d_i]$ 뿐이며, 이는 $\gcd(d_i,\mathrm{char/exponent})$ 로 읽힌다. (P2) 환 사상의 어긋남은 정확히 $\mathrm{Tor}_{1,2}^R(Q,R')$ (정리 1.2); $R=\mathbb Z$ 면 $R'[e]$. (P3) 당김의 장애는 상대군 $C_f$: 단사는 $\mathrm{Hom}$, 전사는 $\mathrm{Ext}^1$.
**공통 장애물.** (O1) 이항 규칙에서는 $A_G\otimes\mathbb Z_{(p)}$ 가 성분당 순환 ($p\nmid ab$): 풍부한 $p$-군 구조(임계군)가 구조적으로 안 들어온다 (정리 3.4). (O2) 임계군의 정보는 $\mathrm{coker}(B^TB)$ — 두 번 합성 — 에 있고 $A_G=\mathrm{coker}B^T$ 는 첫 합성만 본다.

**판정.**
1. **정수 이항 규칙 + 임의 환**: 임계군 복원 **불가** [증명, 정리 3.4]. 환 $\mathbb Z/p^k$ 로 올려도 성분당 순환이라 달라지지 않는다. 환은 $A_G$ 의 비틀림을 더 세밀히 읽어주지만 ($\mathbb F_p$ 는 $p\mid d$ 여부만, $\mathbb Z/p^k$ 는 $\gcd(d,p^k)$) $A_G$ 가 이미 빈약하다.
2. **필요한 확장**: (i) $k$-항 별 규칙(조화 함수) $\deg(v)\varphi(v)=\sum\varphi(w)$ — $R^G_{\rm harm}=\mathrm{Hom}(\mathrm{coker}L,R)$ 가 $R=\mathbb Z/N$ ($\exp K\mid N$) 로 $K$ 를 복원 [증명, 3.3(d); 4 개 그래프에서 표 2 확인]. 함자성은 환 위에서 R1·위 §1 이 그대로 적용된다 ($L$ 은 정수 행렬; 같은 Tor 정리, $Q\to \mathrm{coker}L^T$). 단점: 그래프 호모 $f$ 로 당겨지지 않는다 (조화 사상이 필요) [추측: 조화 사상(harmonic morphism)에서는 당김이 되고 임계군과 자연 사상을 준다 — 문헌 미확인]. (ii) 이항 규칙을 고수하려면 $K$ 를 성분 수로 인코딩하는 함자적 보조 그래프 $\Gamma(G)$ 가 필요 — 알려지지 않음.
3. 증가한 $\mathbb Z/N$ 은 $R^G=\mathrm{Hom}(A_G,R)$ 가 $\mathrm{Hom}(-,\mathbb Q/\mathbb Z)$ 와 같은 일을 하게 만든다 ($N\to\infty$): 이 때 $\mathrm{Hom}(A,\mathbb Q/\mathbb Z)$ 는 Pontryagin 쌍대로 $A$ 의 완비 불변량. 다만 조화 규칙의 $A=\mathrm{coker}L$ 이어야 한다.

### 6. 증명 시도 정리와 막힌 곳
- 시도 완료(막힘 없음): Tor 정리 1.2, 1.3(b)-(e), 정리 2.A·2.B, 정리 3.1, 3.4. 
- 막힌 곳: (1) 방향 사이클 $A_{C_n}$ 의 순환성 일반 증명은 이번에도 하지 않았다(R2 researcher2 담당). 3.4 는 $p\nmid ab$ 에서 순환성을 *일반 연결 그래프* 로 준다(그러면 $C_n$: $p\nmid ab$ 에서 순환; $p\mid ab$ 에서도 사이클은 한 생성원 소거로 순환일 것이나 증명 미완) [추측]. (2) 정리 2.B (전사)의 깨끗한 필요충분(예: $\mathcal K$ 조건 (i) 의 그래프적 해석) 미완. (3) 조화 사상에 대한 당김과 $K(G)\to K(H)$ 함자성: 문헌 확인 없이는 [추측].

## 문주님께 요청
- (낮음) 조화 사상(harmonic morphism)과 임계군의 함자성(Baker–Norine 류) 논문이 있으면 열람하고 싶다. 없을 때의 대안: 당김이 되는 최소 조건을 직접 도출(후속연구 3).

## 후속연구 지점
1. **조화 규칙의 함자성 (높음)**. 무엇을: 별 규칙 $\mathrm{Hom}(\mathrm{coker}L,R)$ 이 어떤 그래프 사상(조화 사상: 정점·간선 사상으로 각 정점에서 다중도 $m_f(v)$ 만큼 국소적으로 균일)에 대해 당김이 되는지, $K(H)\to K(G)$ 또는 그 반대의 자연 사상과 단사/전사 조건. 왜: 이항 규칙은 $K$ 를 못 읽고(정리 3.4), 조화 규칙은 읽지만 당김이 약점. 시작 방법: $f$ 가 정점 $v$ 에서 $\deg$ 보존 조건을 만족할 때 $\varphi\circ f$ 의 조화성을 직접 계산; 간선 수축·분리합·사이클 덮개 3 가지 예로 정리 유도. 난점: 일반 호모에서 깨짐; 다중도를 가군 계수에 넣어야 할지.
2. **Tor 정리의 $K$ 버전과 쌍순환 가군 구조 (중)**. 무엇을: $\mathrm{Bic}_R\cong\mathrm{Hom}(K,R)$ 이 환 사상에 대해 어떻게 변하는지 ($\mathbb Z/p^k\to\mathbb Z/p^j$) 와 $K$ 의 지수를 읽는 최소 $N$. 왜: 3.3 의 응용; 임계군 알고리즘 (Smith 대신 $\ker L$ over $\mathbb Z/N$). 시작: $\mathbb Z/N\to\mathbb Z/N'$ 에 정리 1.2 적용 ($Q$ = coker $L$-쌍대). 난점: $L$ 이 대칭이라 $Q\cong\mathrm{coker}L_R$ 이 되어 Tor 계산이 임계군 자체에 의존.
3. **이항 규칙에서 순환성의 정밀화 (중)**. 무엇을: $p\mid ab$ 인 소수에서 $A_G\otimes\mathbb Z_{(p)}$ 의 구조(소스·싱크·루프로 결정)와 임의 연결 방향 그래프의 $A_G$ 의 완전한 분류 (비틀림 최대 순환 인수 수). 왜: 정리 3.4 의 날카로움(최소 필요 소수 집합)과 방향 사이클 순환성 (R1 후속연구 1). 시작: $p\mid a$ 에서 $v\equiv0$ 전파, 사이클 한 생성원 소거. 난점: 퇴화 소수에서 가지가 많아 비순환 정도를 센다.
4. **보조 그래프 $\Gamma(G)$ 로 $K$ 를 인코딩 (낮음, 탐색)**. 무엇을: 이항 규칙의 성분 수로 $K$ 의 순환 인수 수를 읽을 수 있는 자연 구성 (호몰로지 $\mathbb Z/N$-덮개 등). 왜: 이항 규칙의 함자성이 깨끗하므로 조화 규칙과 경쟁 가능. 시작: $C_6$ 의 $\mathbb Z/6$-덮개 성분 수 등 소형 예. 난점: 정수 이득 없이 덮개를 구성하려면 voltage 데이터가 필요하고 정의에 비자연적 선택이 들어간다 [추측].
5. **정리 2.B (전사)의 그래프적 판정 (낮음)**. 무엇을: $f^*$ 전사의 필요충분을 $C_f$ 와 $\mathcal K$ 에 대한 그래프 조건 (성분·이분성·순환 구조)으로 번역. 왜: 체 위 R1 C6 결과의 환 확장 완성. 시작: 예 2.3 의 $\times2$ 일반화(경로 길이 $k$ 인 $x\to\cdots\to y$ 에서 $2^k$). 난점: 인수가 $\mathcal K$ 와 $\mathrm{Ext}^1$ 두 곳에서 나와 서로 간섭.
