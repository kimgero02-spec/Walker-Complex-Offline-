# [R1-researcher3] (G□G)-행렬의 행렬식: 실패한 후보들과 Aut-등변 인수분해

- 작성자: researcher3 · 라운드: R1 · 역할: 연구원(포메이션 I 분담, 과제 3)

## 요약
- 예비 관찰 5 재확인 [계산 확인]. 더 강하게, 부분집합 Leibniz 합 $\sum_{\sigma\in S}$ 꼴은 $S\neq S_n$ 이면 **어떤 경우에도** 곱셈적일 수 없다 [증명]($P_\tau$, $\tau\notin S$ 논증). 이 한 줄이 순열 제한형·사이클 덮개형 후보 전부를 처리한다.
- 예비 관찰 6 재확인, 일반 정리 증명 [증명]: $\Gamma\le S_V$, 표수 $\nmid|\Gamma|$, 분해체이면 $\det M=\prod_i \det(M_i)^{d_i}$ ($d_i$=기약표현 차수, $M_i$=$m_i\times m_i$ 다중도 공간 위의 작용). Frobenius 군행렬식 인수분해의 치환가군판이다. $C_4,C_5,C_6,P_4,P_5,K_{1,3}$, 페테르센 모두 검증.
- 판정 [증명+계산]: "간선이 연결되는" 행렬식은 **Aut 를 통해서만** 들어오고, 그 결과는 새 함수가 아니라 $\det$ 의 부분대수 제한과 그 **정제(det_ρ)** 이다. 일반 det 는 Aut 자명(비대칭 그래프)일 때 복원되며, 간선 없음 $I_n$ 에서는 복원되지 **않는다**($\mathrm{Aut}=S_n$).

## 본문

### 0. 기호
$V=V(G)$, $n=|V|$, $\Gamma=\mathrm{Aut}(G)\le S_n$, $\mathcal C(G)=\mathrm{End}_\Gamma(F^V)=\{M: M(\sigma u,\sigma v)=M(u,v)\}$. 오비탈 행렬(=$V\times V$ 위 $\Gamma$-궤도의 지시행렬)이 $\mathcal C(G)$ 의 기저이므로 $\dim\mathcal C=$ 오비탈 수 [증명, 임의 표수].

### 1. 실패한 후보들

**1.1 Aut-합** $D_\Gamma(M)=\sum_{\sigma\in\Gamma}\mathrm{sgn}(\sigma)\prod_u M(u,\sigma u)$.
- 재확인 [계산 확인]: $C_4$(|Aut|=8), $P_4$(|Aut|=2), $K_{1,3}$(|Aut|=6) 에서 임의 정수행렬 $M,N$ 로 $D(MN)\ne D(M)D(N)$ (예: $C_4$: 181440 vs −216000). 등변 행렬끼리로 제한해도 $P_4$ 는 실패(318160 vs 0), $C_4$ 는 5/5 실패(첫 시도의 일치는 우연).
- **정리 1 [증명]** $S\subsetneq S_n$, $\mathrm{id}\in S$ 일 때 $f_S(M)=\sum_{\sigma\in S}\mathrm{sgn}(\sigma)\prod_u M(u,\sigma u)$ 는 곱셈적이 아니다.
  증명: $\tau\notin S$ 를 잡고 순열행렬 $P_\tau$ 를 보면 $\prod_u (P_\tau)(u,\sigma u)\neq0\iff\sigma=\tau$ 이므로 $f_S(P_\tau)=0$. 곱셈적이면 $f_S(I)=1$ 이어야 하고 $1=f_S(P_\tau P_\tau^{-1})=f_S(P_\tau)f_S(P_\tau^{-1})=0$, 모순. ∎
  (확인 [계산]: $C_4$ 에서 $\tau=(0\,1)$, $D_\Gamma(P_\tau)=0$, $\det=-1$.)
- 이유(구조) [증명 스케치]: $(MN)$ 의 항을 전개하면 중간 인덱스 $v_u$ 가 임의의 **함수** $V\to V$ 이다. 전체 $S_n$ 합에서는 행 반대칭성으로 비단사 함수가 소거되지만, 합을 부분집합에 제한하면 그 소거가 깨진다.
- 일반 군행렬식·immanant 와의 차이 [기억-미검증]: immanant $\sum_{\sigma\in S_n}\chi(\sigma)\prod M(u,\sigma u)$ 는 **모든** $S_n$ 에 대해 합하고 지표 $\chi$ 로 무게를 줄 뿐이어서 $\chi=\mathrm{sgn}$ 일 때만 곱셈적이라 알려져 있다. 부분군 합은 무게 대신 **지지집합**을 줄이므로 정리 1 이 막는다. 곱셈성을 되살리는 정확한 틀은 Frobenius 군행렬식(§2의 특수 경우)로, 그것은 $|\Gamma|\times|\Gamma|$ 행렬(군 자신 위의 작용)의 행렬식이지 $V$ 위 합이 아니다.

**1.2 허용 순열을 간선으로 제한(사이클 덮개)**: $f_G(M)=\sum_{\sigma:\ \sigma(u)\in N[u]\ \forall u}\mathrm{sgn}\,\sigma\prod M(u,\sigma u)$.
- 복원: $G=K_n$(루프 포함 완전)이면 일반 det [증명]. 간선 없음이면 $\prod_u M(u,u)$(대각곱) — 일반 det 가 **아님**. 즉 이 후보에서 "완전 = 기본 det" 이고 간선이 없을수록 퇴화한다.
- 곱셈성: $C_4$, $P_4$ 에서 정수행렬로 $f_G(MN)\ne f_G(M)f_G(N)$ [계산 확인] (예 $C_4$: 154659 vs −25272). 일반적으로 정리 1 (허용 집합이 $S_n$ 이 아니므로) [증명].
- 부호: 일반 sgn 을 쓰면 정의는 되지만 곱셈성이 없다.
- **정리 2 [증명]** (지지 제한 대수) $R\subseteq V\times V$ 반사적 관계, $\mathrm{Mat}_R=\{M:\mathrm{supp}\,M\subseteq R\}$ 라 하자. $\mathrm{Mat}_R$ 가 곱에 닫힘 $\iff R$ 이행적. 증명: $E_{uv}E_{vw}=E_{uw}$ 이므로 닫힘이면 $(u,v),(v,w)\in R\Rightarrow(u,w)\in R$; 역은 자명. $R=$ "$u=v$ 또는 $u\sim v$" 가 이행적이면 $G$ 는 완전그래프들의 서로소 합이고, $\det$ 는 성분별 블록 행렬식의 곱으로 붕괴한다. 이는 예비 관찰 4(연결성분 붕괴)의 행렬식판이다.

**1.3 충돌 그래프/독립집합 합** (내가 구체화한 정의 [해석]): $Z_G(M)=\sum_{S\ \text{독립}}\det M[S,S]$.
- $I_n$ 이면 $\det(I+M)$, $K_n$ 이면 $1+\mathrm{tr}M$. 어느 쪽도 $\det M$ 이 아니다(최고차 항만이 $\det M$ 이고 $I_n$ 에서만 나타남).
- 곱셈성 실패 [증명, 반례]: $G=K_2$, $W$=교환행렬: $Z(W)=1$, $Z(W^2)=Z(I)=3\neq1\cdot1$. 정규화 $Z/Z(I)$ 도 $1/3$ vs $1/9$ 로 실패.
- 이유: $Z_G(M)=\mathrm{tr}(P\,\Lambda M)$ ($P$=독립집합 기저로의 사영, $\Lambda M$=외적 거듭제곱 작용)는 **트레이스형(선형범함수)** 이다. 곱셈성은 **지표형**(군 준동형 $GL\to F^\times$)의 성질이므로 구조적으로 불가능.

**1.4 근본 장애 [기억-미검증 + 증명 일부]** $M_n(F)$ 전체에서 곱셈적인 사상 $f:\mathrm{Mat}_n(F)\to F$ 는 $\varphi\circ\det$ ($\varphi$:F의 곱셈적 함수) 꼴이라 알려져 있다(대수군 $GL_n$ 의 다항 지표는 $\det^k$; $[GL_n,GL_n]=SL_n$). 따라서 **전체 $F^{G\square G}$ 위에서 $G$ 에 의존하는 곱셈적 행렬식은 존재하지 않는다**. 그래프 의존 행렬식은 반드시 **진부분대수** 위에 정의해야 한다. 정리 1·2 는 이것의 초등적 증명 가능한 사례들이다.

### 2. 유력 후보: $\mathcal C(G)$ 위의 행렬식

**정리 3 [증명]** $\Gamma\le S_V$ 유한군, $\mathrm{char}F\nmid|\Gamma|$, $F$ 가 $\Gamma$ 의 분해체(모든 기약표현이 절대기약)라 하자. $F^V\cong\bigoplus_i\rho_i\otimes W_i$ ($\rho_i$ 기약, 차수 $d_i$, $W_i=\mathrm{Hom}_\Gamma(\rho_i,F^V)$, $\dim W_i=m_i$). 그러면
1. $\mathcal C\cong\bigoplus_i\mathrm{Mat}_{m_i}(F)$, $M\mapsto(M_i)$ (대수 동형).
2. $\det M=\prod_i\det(M_i)^{d_i}$.
3. $\dim\mathcal C=\#\text{오비탈}=\sum m_i^2$, $\ n=\sum m_id_i$. $\mathcal C$ 가 가환 $\iff$ 모든 $m_i=1$(다중도 1).
증명: Maschke 로 완전가약, Schur 보조정리로 $\mathrm{End}_\Gamma(\rho_i\otimes W_i)=1\otimes\mathrm{End}(W_i)$ 이고 서로 다른 $i$ 사이 Hom 은 0. $M$ 은 $\bigoplus 1_{d_i}\otimes M_i$ 로 작용하고 $\det(1_d\otimes X)=\det(X)^d$. 3은 $\dim\mathrm{End}_\Gamma=\langle\chi,\chi\rangle=\sum m_i^2$ 및 기저 비교. ∎
- 따름 [증명]: $M\in\mathcal C$ 가역 $\iff$ 모든 $M_i$ 가역. $\det$ 은 $\mathcal C^\times=\prod GL_{m_i}$ 의 지표 $\prod\det(M_i)^{d_i}$ 이고, 이 군의 지표 전체는 $\prod\det(M_i)^{k_i}$ ($k_i\in\mathbb Z$)로 **정제**된다. 이 $\det_i(M):=\det(M_i)$ (= $M$ 이 다중도 공간 $\mathrm{Hom}_\Gamma(\rho_i,F^V)$ 에 하는 일의 행렬식)가 "간선(→Aut)이 만드는 새 행렬식들"이다.
- 특수 경우: $V=\Gamma$(정칙표현)이면 $m_i=d_i$ 이고 정리 3 은 Frobenius 군행렬식 인수분해와 같다 [증명, 정리 3의 직접 적용].
- 가정이 필요한 이유: (a) 표수가 $|\Gamma|$ 를 나누면 Maschke 실패, 이 경우 $\mathcal C$ 는 반단순이 아닐 수 있다. 다항식 항등식 $\det M=\prod(\cdot)^{d_i}$ 자체는 $\mathbb Z$ 위에서 성립하면 모든 $p$ 로 환원되지만, 기약표현 해석은 잃는다 [추측; $C_4$, $p=2$ 에서 인수들이 모두 $(x+z)$ 로 합쳐지는 것을 손으로 확인, 약한 근거]. (b) 분해체가 아니면 $\mathcal C=\bigoplus\mathrm{Mat}_{k}(D)$ 가 되고 $\det_i$ 는 기약 약분노름(reduced norm)이 된다. 예: $C_5$ 를 $\mathbb Q$ 위에서 보면 두 2차원 기약표현이 $\mathbb Q(\sqrt5)$ 위 켤레라 하나로 합쳐진다.

**예제 표** (모두 정수 임의 등변 행렬로 $\det$ 일치 확인함 [계산 확인]; 오비탈 수는 직접 계산; 인수 모양은 정리 3 으로 도출 [증명])

| 그래프 | $\Gamma$ (|Γ|) | 오비탈 수 | $F^V$ 분해 ($d_i$; $m_i$) | $\det M$ 모양 |
|---|---|---|---|---|
| $C_4$ | $D_4$ (8) | 3 | $1,1,2$ ; 모두 1 | $\lambda_0\lambda_2\,\lambda_1^2$ |
| $C_5$ | $D_5$ (10) | 3 | $1,2,2$ ; 모두 1 | $(x{+}2y{+}2z)\,q^2$, $q=x^2{-}x(y{+}z){-}y^2{-}z^2{+}3yz$ ($\mathbb Q$ 위 기약) |
| $C_6$ | $D_6$ (12) | 4 | $1,1,2,2$ ; 모두 1 | $\lambda_0\lambda_3\lambda_1^2\lambda_2^2$, $\lambda_k=x{+}2y\cos\frac{\pi k}{3}{+}2z\cos\frac{2\pi k}{3}{+}w(-1)^k$ |
| $P_4$ | $\mathbb Z_2$ (2) | 8 | $1(m{=}2),\ 1'(m{=}2)$ | $\det M_+\cdot\det M_-$ (2×2 둘), **비가환** |
| $P_5$ | $\mathbb Z_2$ (2) | 13 | $1(m{=}3),1'(m{=}2)$ | $\det M_+(3{\times}3)\det M_-(2{\times}2)$ ; $13=9+4$ |
| $K_{1,3}$ | $S_3$ (6) | 5 | 자명($m{=}2$), 표준 2차원($m{=}1$) | $\det\!\begin{pmatrix}M_{cc}&3M_{cl}\\M_{lc}&M_{ll}+2M_{ll'}\end{pmatrix}\cdot(M_{ll}-M_{ll'})^2$ ; $5=4+1$ |
| 페테르센 | $S_5$ (120) | 3 | $1,4,5$ ; 모두 1 | $(x{+}3y{+}6z)(x{-}2y{+}z)^4(x{+}y{-}2z)^5$ |

($C_4$: $M=xI+yA+zA_2$, $\lambda_0=x{+}2y{+}z$, $\lambda_2=x{-}2y{+}z$, $\lambda_1=x{-}z$ — 예비 관찰 6 독립 재확인 [증명+계산 확인]. 지수 2 는 $D_4$ 의 2차원 기약표현 차수. 페테르센은 $F^{10}=\mathbf 1\oplus\mathbf 4\oplus\mathbf 5$ (2-부분집합 치환표현), $A$ 의 고유값 $3,-2,1$ 의 중복도 $1,4,5$ 와 정확히 일치한다.)

**공통 패턴·장애물** [증명된 정리 3 의 해석]
- (패턴 1) 가환(다중도 1, 즉 Gelfand 쌍/결합스킴) 경우 $\det=\prod\lambda_i^{d_i}$ ($\lambda_i$=오비탈 계수의 선형형식=결합스킴의 지표표). 지수 $d_i$=기약표현 차수.
- (패턴 2) 정점궤도가 여러 개이거나 $\Gamma$ 가 작으면 $m_i>1$ 로 비가환 블록(P_4, P_5, 별)이 생기며, 인수는 선형이 아닌 $m_i\times m_i$ 행렬식이다. 대칭이 적을수록 인수분해는 덜 일어나고 $\Gamma=1$ 이면 $\mathcal C=\mathrm{Mat}_n$, 인수분해는 자명(=일반 det).
- (장애물) 분해체 문제($C_5$ 의 $\sqrt5$), 모듈러 표수, 그리고 $m_i,d_i$ 를 구하려면 $\Gamma$ 의 지표표가 필요하다(일반 그래프에 대한 폐쇄형 공식은 없다).

**인접·라플라시안과 특성다항식** [증명]
- $A_G\in\mathcal C(G)$ ($\sigma\in\mathrm{Aut}$ 이므로 $A(\sigma u,\sigma v)=A(u,v)$). 차수행렬 $D$ 는 궤도 상수 대각이므로 $\mathcal C$ 에 속하고, 따라서 라플라시안 $L=D-A\in\mathcal C$. 일반으로 $\mathcal C$ 는 $I,J,A,\bar A,D$ 와 이들로 생성한 대수를 포함.
- $\det(xI-A_G)=\prod_i\det(xI_{m_i}-A_i)^{d_i}$ (정리 3 을 $xI-A\in\mathcal C[x]$ 에 적용). 즉 특성다항식은 $\Gamma$-기약 성분의 인수분해이고 근의 중복도가 $d_i$ 의 배수 구조를 가진다. 확인 [계산]: 별 $K_{1,3}$: 자명 성분 $A_{\rm triv}=\begin{pmatrix}0&3\\1&0\end{pmatrix}$, 표준 성분 $A=0$ → $(x^2-3)\,x^2$ ✓. 페테르센: $(x-3)(x+2)^4(x-1)^5$ ✓.
- 의의: 간선 정보가 있는 쪽은 $\det$ 이 아니라 **어떤 원소를 넣느냐($A_G$)** 이다. 함수 $\det|_{\mathcal C}$ 는 $\Gamma$ 만 안다.

### 3. 한계: 간선 정보는 Aut 로만 들어온다
- **정리 4 [증명]** $\mathcal C(G)$ 와 $\det|_{\mathcal C}$ 는 치환군 $\Gamma\le S_V$ 에만 의존한다. 따라서 $\mathrm{Aut}(G)=\mathrm{Aut}(G')$(같은 $V$ 위) 인 그래프는 구분되지 않는다. $\mathrm{Aut}(\bar G)=\mathrm{Aut}(G)$ [증명: 자기동형은 인접·비인접을 모두 보존]이므로 $G$ 와 여그래프는 항상 같다. 예: $I_n$ vs $K_n$($S_n$), $C_7$ vs $\overline{C_7}$ (둘 다 $D_7$, 차수 2 vs 4로 비동형), 페테르센 vs 그 여그래프($S_5$).
- 반대 극단 [증명]: 비대칭 그래프(Aut 자명; 6정점에 존재함을 $\{01,12,23,34,45,14,02\}$ 로 확인 [계산 확인]) 는 모두 $\mathcal C=\mathrm{Mat}_n$, 일반 det, 서로 다른 비대칭 그래프끼리 구분 불가.
- 즉 정보량은 $\Gamma$ 의 크기에 **반비례**한다: 대칭이 클수록 인수분해 풍부(그러나 간선 정보는 $\Gamma$ 로 압축되어 소실), 대칭이 없으면 간선 정보가 있어도 det 에 반영 불가.
- 세분 방향 [기억-미검증]: Aut 대신 $A_G$ 가 생성하는 최소 결맞음 대수(Weisfeiler–Leman 폐포 $W(G)$)를 쓰면 $W(G)\subseteq\mathcal C(G)$ 이고 비대칭 그래프에서도 일반 det 보다 작은 대수가 나올 수 있다. 단 $W(I_n)=W(K_n)=\mathrm{span}\{I,J\}$ 로 $I_n$/$K_n$ 은 여전히 구분되지 않으므로 **쌍 $(W,A_G)$** 로 보아야 한다. 이 경우 $W$ 가 Aut-궤도대수와 다른(비Schurian) 예는 있다고 알려져 있다.

### 4. 판정
- "간선이 연결되는 행렬식"을 **$(G\square G)$-행렬 전체 위의 곱셈적 함수**로 정의하는 것은 불가능에 가깝다(§1.4; 정리 1 은 순열·사이클덮개·독립집합 후보의 구체적 실패를 증명).
- 가장 자연스러운 정의 (제안, [추측-정의]): $\det_G:=\det|_{\mathcal C(G)}$ 와 그 정제 $\{\det_\rho\}_{\rho\in\widehat{\mathrm{Aut}G},\ \rho\subset F^V}$. 곱셈적이고 [증명], 일반 det 를 인수로 포함($\det=\prod\det_\rho^{d_\rho}$)하며 간선은 Aut 를 통해 정확히 $\Gamma$ 의 표현론으로 나타난다.
- 일반 det 포괄성: Aut 자명 그래프에서만 $\mathcal C=\mathrm{Mat}_n$ 로 복원. "간선 없음에서 복원" 은 **성립하지 않음**($I_n$ 은 $\Gamma=S_n$, 인수분해 $\det=(x+(n-1)y)(x-y)^{n-1}$ 꼴: $M=xI+yJ'$). 일반 det 를 포괄하려면 군을 매개변수로 하는 $\det_\Gamma$ 의 족(Γ=1 이 일반 det)으로 읽어야 하며, 이는 "간선"보다 "대칭"의 이론이다.
- 문주님 정의와의 정합성: 문주님 관찰 (iii) "간선은 Aut 를 통해서만 들어온다" 의 행렬식 버전이 정확히 이 결과이다. 새 정보(인수분해)는 실재하나 간선 자체는 $\Gamma$ 이상을 전하지 못한다.

## 후속연구 지점
1. **(최우선) $\det_\rho$ 의 대수군 해석과 정제 지표 완전 분류**: $\mathcal C^\times=\prod GL_{m_i}$ 의 다항 지표 전체($\prod\det_i^{k_i}$)를 정리로 정착시키고, 비분해체(실수/유리수)에서 기약 약분노름으로 바꾼 정확한 진술을 쓴다. 시작: $C_5$ 의 $\mathbb Q$ 사례를 일반화(Galois 궤도 합). 난점: 반단순 대수의 Schur 지수(지수>1 인 경우).
2. **표수 $p\mid|\mathrm{Aut}|$ 에서의 행태**: $\det M=\prod(\cdot)^{d_i}$ 가 $\mathbb Z$ 위 항등식인 점을 이용해 환원 후 인수가 어떻게 합쳐지는지($C_4$, $p=2$; $K_{1,3}$, $p=3$) 소수의 예로 구조를 보고 정리화한다. 난점: 비반단순 $\mathcal C$ 의 Jacobson 근기와 $\det$ 의 관계.
3. **Aut 를 넘어서는 정보: $(W(G),A_G)$ 쌍**: Weisfeiler–Leman 폐포 위 $\det$ 정제가 비대칭 그래프의 간선 정보를 살리는가? 비Schurian 예와 $I_n$/$K_n$ 분리용 보조 데이터(에지 색) 설계. 시작: 작은 비대칭 그래프 몇 개에서 $W(G)$ 를 손으로 계산. 난점: $W$ 가 곧 $\mathrm{Mat}_n$ 로 무너지는 경우가 많을 것.
4. **곱셈성 불가능 정리의 엄밀화**: §1.4 의 "$\mathrm{Mat}_n(F)$ 위 곱셈적 사상은 $\varphi\circ\det$" 를 문헌 없이 초등 증명(기본행연산으로 $GL_n$ 의 교환자, $n\ge2$, 작은 유한체 예외 포함). 정리 1·2 와 연결해 "G 의존 곱셈적 det 는 진부분대수에서만" 을 정리로 격상. 난점: $|F|=2$, $n=2$ 같은 예외.
5. **오비탈 대수 쪽 응용**: 거리정칙 그래프 등 결합스킴에서 $d_i$=고유값 중복도와 오비탈 계수 선형형식(지표표)의 관계를 정리하고, 조합적 의미(라플라시안 $L$ 의 $\det$ 정제 = 나무 개수 공식과의 연결 여부)를 탐색. 난점: 비가환($m_i>1$) 경우에는 지표표가 행렬값이 된다.
