# [R04-researcher1] 블로업 $G[K_m]$ 의 상한 정리와 붕괴: $\tau(P[K_m])=2m=\omega$ ($m\ge2$)

- 작성자·라운드·역할: researcher1 / 라운드 4 / 연구원 (지점 3). 중간본: R04-researcher1-interim.md. 코드: rooms/researcher1/r4_blowup.py (타입 열거·전개·유리수 정확 검증), r4_run1~8.py.
- 도서관 공격·아이디어 반영: 시작 시 `R04-researcher2-interim.md` 를 읽었다(정리 2 검증, 사실 F 제거, R03 정리 무반례). 내 지점을 공격하지 않았다. `R04-researcher3*` 는 작성 중·끝 직전 두 번 확인했을 때 **없었다.** 끝 직전에 다시 확인한 결과는 맨 아래 "도서관 확인 기록".

## 요약
1. **정리 1** [증명]: 임의의 $G$ 에서 $G[K_m]$ 의 극대 완전이분쌍은 블롭 타입 $(X,Y,Z)$ (완전 $A$블롭, 완전 $B$블롭, 분할 블롭; $Z$ 는 클리크) 와 $Z$ 블롭의 분할로 정해진다. R03 의 (P)(Q) 분류의 일반형이다.
2. **정리 2·3 (상한 = 붕괴 정리)** [증명]: 블롭 순서 $\sigma$ 와 모멘트 곡선으로 라벨 변화 수 $\le(m-1)|Z|+c_\sigma$. 이것이 $m\omega-1$ 이하이면 $\tau(G[K_m])=m\,\omega(G)$. 따름: $m\ge\min(n-\omega+1,\ \operatorname{zig}(G)+\omega-1)$ 이면 **어떤 $G$ 든** $\tau(G[K_m])=m\omega(G)$. 삼각형 없는 $G$ 에서 $m\ge2$, $K_{m,m+1}\not\subseteq G$ 이면 $\tau(G[K_m])=2m$.
3. **$P[K_m]$ (Petersen)** [증명]: $\tau(P[K_m])=2m=\omega$ 가 모든 $m\ge2$ 에서 성립한다. $\tau(P)=3>2=\omega$ 는 $m=1$ 에서만. **Petersen 블로업은 $\tau>\omega$ 시험대가 못 된다.** $\chi(P[K_m])\ge\lceil5m/2\rceil$ 이므로 $\chi-\tau\ge\lceil m/2\rceil$. 같은 붕괴가 Grötzsch·Clebsch·$C_n^2$ ($n\ge9$) 에서도 일어난다.
4. 부산물 [증명]: $K_{s,s}$-자유 $\Rightarrow\tau\le2s-1$ (따라서 $C_4$-자유 $\Rightarrow\tau\le3$, $K_{2,3}$-자유 $\Rightarrow\tau\le4$); $\tau(C_n^2)=3$ ($n\ge9$), 즉 $\chi=4$ 인 $C_{10}^2,C_{11}^2$ 에서 $\tau<\chi$; $\operatorname{zig}(G)=\rho(G)$ (선형순서 모멘트 인증서의 최적값, R03-r3 의 $Q_d$ 와 같은 것).
5. 장애물 [증명]: 인증서가 $m\omega$ 에 닿으려면 $\operatorname{zig}(G)\le m\omega$ 가 필요하다. 또 $m<\tau(G)/\omega$ 이면 $\tau(G[K_m])\ge\tau(G)>\omega(G[K_m])$ 이지만 이는 $G\subseteq G[K_m]$ 의 자명한 단조성이라 새 정보가 없다.

## 본문

### 0. 정의·오프셋 점검 (먼저 검증)
- $\tau(G)=\operatorname{coind}(B_0(G))+1$. $K_1,K_2,K_3$: $B_0(K_n)\cong S^{n-1}$ 이므로 $\tau=1,2,3$ (R01·R03 확인) [증명, 인용]. 이 보고서의 틀로 재확인: $K_n[K_m]=K_{nm}$ 이고, 타입은 $X\sqcup Y\sqcup Z$ 가 모든 블롭을 덮는 분할이며 $z=n$ 인 타입의 변화 수는 $n(m-1)+(n-1)=nm-1=d$ → $\tau\le nm$, 하한 $\omega=nm$ [증명]. $m=1$: $K_3$ 의 극대쌍 $\{a\}\times\{b,c\}$ 는 라벨 열 A B B 형 변화 $\le2=d$ 로 $\tau\le3$.
- 인증서 건전성 [증명, R01/R03 인용]: $y:V\to\mathbb R^d$ 가 모든 극대 완전이분쌍을 엄격 분리하면 $\tau\le d+1$.
- 보조정리 G′ (Gale 보조정리의 역 포함) [증명]. $P,Q\subset\mathbb R$ 서로소 유한, $t$ 순서 라벨 열의 런 수를 $r$ 이라 하면 $\gamma_d(P)=\{(t,\dots,t^d)\}$ 와 $\gamma_d(Q)$ 가 아핀 초평면으로 엄격 분리됨 $\iff r\le d+1$. ($\Leftarrow$: R03 보조정리 G. $\Rightarrow$: 분리 초평면 $w\cdot x=c$ 는 곡선 위에서 차수 $\le d$ 다항식 $p(t)=w\cdot\gamma(t)-c$, $P$ 에서 $>0$, $Q$ 에서 $<0$. 런 경계마다 부호가 바뀌므로 서로 다른 실근이 $r-1$ 개 이상, 따라서 $r-1\le\deg p\le d$.) 이 역방향은 R03-r3 이 378개 라벨링으로 점검한 것의 증명이다.
- $[기억-미검증]$ 목록: (i) $\operatorname{cd}(KG(n,k))=n-2k+2$ (Dol'nikov), (ii) $\chi(P[K_m])=\lceil5m/2\rceil$ 정확값(아래 하한만 사용), (iii) Mycielski 연산이 위상 하한을 1 올린다, (iv) $\tau(W_5)=4$, (v) 지그재그 정의의 규약(색 순서로 한 변씩 번갈아). (v) 는 R03 오케스트레이터 재도출과 같은 규약을 썼다. 이 보고서의 정리들은 (i)–(iv) 에 의존하지 않는다(예제 표의 참고 열에서만 언급).

### 1. 정리 1: 극대 완전이분쌍의 블롭 타입 분류 [증명]
$G$ 임의, $V(G[K_m])=V\times[m]$, $(u,s)\sim(v,t)$ 는 $u=v,s\ne t$ 이거나 $uv\in E(G)$. 블롭 $K^u=\{u\}\times[m]$.
**타입.** 서로소 블롭 집합 $(X,Y,Z)$ 가 *유효*하다 ⇔ $X,Y,Z$ 가 쌍마다 $G$ 에서 완전결합(서로 다른 블롭이 모두 인접)이고 $Z$ 는 $G$ 의 클리크, 그리고 $X\cup Z\ne\emptyset\ne Y\cup Z$. $Z\ne\emptyset$ 이면 $m\ge2$.
**정리 1.** $(A,B)$ 가 $G[K_m]$ 의 극대 완전이분쌍(두 변 모두 비공집합)이면 유효한 타입 $(X,Y,Z)$ 가 있어 $A\cup B=\bigcup_{u\in X\cup Y\cup Z}K^u$, $u\in X\Rightarrow K^u\subseteq A$, $u\in Y\Rightarrow K^u\subseteq B$, $u\in Z\Rightarrow K^u=A_u\sqcup B_u$ (둘 다 비공집합). 역으로 유효 타입과 $Z$ 블롭 분할마다 완전이분쌍이 얻어진다.
*증명.* $A_u=A\cap K^u$, $B_u=B\cap K^u$ (서로소: 한 점은 자기와 인접하지 않는다). $I=\{u:A_u\ne\emptyset\}$, $J=\{u:B_u\ne\emptyset\}$. 완전이분이므로 $u\in I$, $v\in J$, $u\ne v$ 이면 $uv\in E$. $X=I\setminus J$, $Y=J\setminus I$, $Z=I\cap J$ 로 둔다. 서로 다른 $u,u'\in Z$ 는 $u\in I,u'\in J$ 라서 인접: $Z$ 는 클리크. 나머지 완전결합도 같다. 극대성: $u\in Z$ 에서 $x\in K^u\setminus(A_u\cup B_u)$ 가 있으면 $x$ 는 $B_u$ 와 같은 블롭 안에서 인접, $B_v$ ($v\ne u$, $v\in J$) 와는 $uv\in E$ 라서 인접이므로 $A$ 에 추가 가능 — 모순. $u\in X$ 에서 $K^u\not\subseteq A$ 인 점 $x$ 도 $B$ 전체와 인접하여 추가 가능 ($B\cap K^u=\emptyset$, 다른 블롭은 $uv\in E$). $Y$ 도 대칭. ∎
(R03 정리 A: $C_n[K_m]$, $n\ge5$ 에서 $Z$ 는 블롭 1~2개, (P)=$Z=\{i\}$ 또는 $Z=\{i\},Y=\emptyset$ 형, (Q)=$Z=\{i,i+1\}$. $n=4$ 에서는 $X=\{0,2\}$, $Y=\{1,3\}$ 형이 추가된다.)
[계산 확인] 구현 점검: 타입 전개와 폐포 brute force 의 쌍 집합이 **동일**: $P[K_1]$(10), $P[K_2]$(60), $\overline{C_7}[K_2]$(140), $C_9^2[K_1]$(18), $C_9^2[K_2]$(180), $W_5[K_2]$(103), $W_5[K_3]$(1007), Grötzsch$[K_2]$(83). 증명은 위와 같고 이것은 구현 점검이다.

### 2. 정리 2: 블롭 순서 인증서 [증명]
$\sigma$ 를 $V(G)$ 의 선형순서로, 블롭 $u$ 의 위치를 $\operatorname{pos}(u)$ 로 하자. 정점 $(u,s)$ 를 모멘트 곡선 $\gamma_d(t)$ 의 $t=\operatorname{pos}(u)m+s+1$ 에 놓는다(블롭 안 순서는 임의). 타입 $(X,Y,Z)$ 의 블롭들을 $\sigma$ 순서로 읽은 문자열 $w\in\{X,Y,Z\}^*$ 에서
$$c_\sigma(X,Y,Z)=\#\{\text{인접 문자쌍 } (w_i,w_{i+1})\notin\{XX,YY\}\}.$$
**정리 2.** 쌍의 라벨 열(각 점 $A/B$)의 변화 수 $\le(m-1)|Z|+c_\sigma$. 따라서 모든 유효 타입에서 $(m-1)|Z|+c_\sigma\le d$ 이면 $\tau(G[K_m])\le d+1$.
*증명.* $X,Y$ 블롭 안은 라벨이 일정 → 안쪽 변화 0. $Z$ 블롭 안은 점 $m$ 개 → $\le m-1$. 블롭 사이 경계에서 변화는 $XX,YY$ 쌍이 아니면 최대 1. 보조정리 G′ 와 건전성. ∎
**표기.** $D_\sigma(m)=\max_{\text{유효 타입}}\big((m-1)z+c_\sigma\big)$, $\tau(G[K_m])\le 1+\min_\sigma D_\sigma(m)$.

**명제 O (zig 와의 관계)** [증명]. $\rho(G):=\min_\sigma\max_{\text{완전이분쌍}}(\text{런 수})$ 라 하자. 그러면 $\rho(G)=\operatorname{zig}(G)$ [규약 (v)]. (한 방향: 진색칠을 색 순서로 읽으면 같은 색 점은 같은 변이므로 색류를 연속 배치한 선형순서의 런 수는 지그재그 길이와 같다 → $\rho\le\operatorname{zig}$. 반대: 단사 색칠(순서 자체)은 진색칠이므로 $\operatorname{zig}\le\rho_\sigma$ 모든 $\sigma$.) 따라서 R03-r3 의 $Q_d$ 는 $\operatorname{zig}\le d+1$ 이고, 정리 2 는 $\tau\le\operatorname{zig}$ (R03-r2 §D) 의 블로업 판이다. 또 $Z=\emptyset$ 타입은 $G$ 의 완전이분쌍과 같은 변화 수를 가지므로 **인증서가 $m\omega$ 에 닿으려면 $\operatorname{zig}(G)\le m\omega(G)$ 가 필요**하다.

### 3. 정리 3: 붕괴(상한이 $\omega$ 와 일치) [증명]
$\omega=\omega(G)$. 유효 타입의 크기 $x=|X|,y=|Y|,z=|Z|$ 에 대해
$$\psi(X,Y,Z):=\min\big(x+y,\ z+1+2\min(x,y)\big).$$
**보조 부등식.** 어떤 순서에서도 $c_\sigma\le\min(x+y+z-1,\ 2z+2\min(x,y))=\psi+z-1$. (문자 $x+y+z$ 개의 인접쌍 수 $\le x+y+z-1$. $Z$ 를 포함하는 인접쌍 $\le2z$, $XY$ 인접쌍은 소수 쪽 문자마다 이웃이 둘뿐이라 $\le2\min(x,y)$.)
**정리 3.** $m\ge1$ 이고, $|Z|<\omega$ 인 모든 유효 타입(단 $m=1$ 이면 $Z=\emptyset$ 만)에서 $\psi\le m(\omega-z)$ 이면 $\tau(G[K_m])=m\,\omega(G)$.
*증명.* $z<\omega$: $(m-1)z+c\le mz+\psi-1\le m\omega-1$. $z=\omega$: $Z$ 와 완전결합인 블롭이 있으면 $Z$ 에 추가해 클리크가 $\omega+1$ — 모순, 그래서 $X=Y=\emptyset$ 이고 $c=\omega-1$, 변화 $\le(m-1)\omega+\omega-1=m\omega-1$. $d=m\omega-1$ 로 정리 2, 하한 $\tau\ge\omega(G[K_m])=m\omega$ (부분그래프 $K_{m\omega}$). ∎
**단조성.** $z<\omega$ 에서 $\psi\le m(\omega-z)$ 는 $m$ 에 대해 단조 → $m=2$ 에서 성립하면 모든 $m\ge2$ 에서 성립한다.
**따름 3a.** $m\ge n-\omega+1$ ⇒ $\tau(G[K_m])=m\omega$. ($\psi\le x+y\le n-z\le m(\omega-z)$, $k=\omega-z$ 로 $(n-\omega+1)k-(n-\omega+k)=(n-\omega)(k-1)\ge0$.)
**따름 3b.** $m\ge\operatorname{zig}(G)+\omega-1$ ⇒ $\tau(G[K_m])=m\omega$. ($\sigma$ 를 zig 최적 순서로. 타입의 $Z$ 를 모두 $A$ 쪽에 붙인 $G$ 의 완전이분쌍 $(X\cup Z,Y)$ 의 변화 $\le\operatorname{zig}-1$ 이고 $c_\sigma$ 와의 차는 $Z$ 를 포함하는 비변화 쌍 $\le2z$. 그러면 $(m-1)z+c\le(m+1)z+\operatorname{zig}-1\le m\omega-1$ 은 $z\le\omega-1$ 에서 $m\ge\operatorname{zig}+\omega-1$ 일 때 성립.)
**해석** [증명]. $\lim_m\tau(G[K_m])/m=\omega(G)$, 반면 $\tau(G[K_m])\le\chi(G[K_m])$ 이고 $\chi(G[K_m])\ge m\chi_f(G)$. 곧 위상적 하한은 $\chi_f$ 를 배수로 따라가지 못한다: 블로업이 위상적 과잉 $\tau-\omega$ 를 흡수한다. 즉 $\tau$ 가 곱셈적이 아니다 ($\tau(C_5)=3$, $\tau(C_5[K_m])=2m<3m$).
**하한 쪽 창** [증명]: $G\subseteq G[K_m]$ 라서 $\tau(G[K_m])\ge\max(m\omega,\tau(G))$. 붕괴 임계 $m^*(G)$(인증서가 처음 $m\omega$ 에 닿는 $m$)는 $\lceil\operatorname{zig}(G)/\omega\rceil\le m^*\le\min(n-\omega+1,\operatorname{zig}+\omega-1)$ (아래 한계는 명제 O, 위 한계는 따름 3a·3b). Kneser $KG(3k-1,k)$ ($\omega=2$, $\tau\ge\operatorname{cd}=k+1$ [기억-미검증 (i)]) 에서는 $m^*\ge(k+1)/2$ 로 임계가 비유계다.

### 4. 삼각형 없는 그래프와 Petersen [증명]
**정리 T.** $G$ 가 삼각형이 없고 변이 있으며 $m\ge2$, $K_{m,m+1}\not\subseteq G$ 이면 $\tau(G[K_m])=2m$ (모든 순서에서 인증서가 작동).
*증명.* $\omega=2$. $z=2$: $Z$ 는 변 $\{u,v\}$ 이고 공통이웃이 없으므로 $\psi=0$. $z=1$: $Z=\{u\}$, $X\cup Y\subseteq N(u)$, $X$–$Y$ 가 완전결합이면 $u$ 와 삼각형 → $\min(x,y)=0$, $\psi\le\min(x,\,2)\le2\le m$. $z=0$: $K_{x,y}\subseteq G$, $\psi=\min(x+y,1+2\min(x,y))$. $\min(x,y)\le m-1$ 이면 $\psi\le2m-1$. $\min\ge m$ 이면 $K_{m,m+1}\not\subseteq G$ 때문에 $x=y=m$, $\psi=2m$. 모두 $\psi\le m(2-z)$. 정리 3. ∎
**Petersen $P=KG(5,2)$** (girth 5: $K_{2,2}$ 도 없음). $K_{2,3}\not\subseteq P$ 이므로 모든 $m\ge2$ 에서 **$\tau(P[K_m])=2m$**.
- 직접 확인(독립 점검 아님, 구현 점검): $P[K_2]$ 극대쌍 60 개(= 변 15 × 2 + 정점 10 × 2 + 별 10)를 폐포로 전수 열거해 타입 전개와 일치시키고, 임의 순서 3 개에서 모멘트 곡선 $\mathbb R^3$ 위 유리수 정확 분리 다항식 검사: 최대 변화 3 $=2m-1$, 실패 0.
- $m=1$: 별 $K_{1,k}$ 만 있어 런 $\le3$ ⇒ $\tau(P)\le3$, 하한 $\tau(P)\ge3$ ($\operatorname{cd}(KG(5,2))=3$, 정리 A [증명, R03] + Dol'nikov [기억-미검증 (i)]; 또는 R02 의 $\tau(P)=3$).
- $\chi(P[K_m])\ge\lceil10m/4\rceil=\lceil5m/2\rceil$ ($\alpha(P)=4$). $m$ 짝수이면 $\{a,b\}\times[m/2]$ 로 $5m/2$ 색 구성이 있다 [증명]. 따라서 $\chi-\tau\ge\lceil m/2\rceil$.

### 5. 정리 K: 블로업이 아닌 직접 상한 [증명]
**정리 K.** $G$ 에 $K_{s,s}$ 가 없으면 $\tau(G)\le2s-1$. 더 정확히 $\tau(G)\le\max_{K_{x,y}\subseteq G}\min(2\min(x,y)+1,\ x+y)$.
*증명.* 임의의 순서. 완전이분쌍 $(A,B)$, $|A|=x\le|B|=y$ 의 라벨 열 런 수는 $\le2x+1$ 이고 $\le x+y$. 보조정리 G′ 와 건전성. ∎
따름: $C_4$-자유 $\Rightarrow\tau\le3$ (girth $\ge5$ 포함). 이웃복합체가 별들의 1점 접착이라 그래프와 호모토피 동치라는 사실과 정합 [기억-미검증 추론]. $K_{2,3}$-자유 $\Rightarrow\tau\le4$ (별과 $K_{2,2}$ 만). Grötzsch(최대 공통이웃 2, [계산 확인]) 와 Clebsch(16정점 5-정규, 공통이웃 $\le2$) 가 이에 해당: $\tau\le4$. Grötzsch·Clebsch 의 $[K_m]$ 은 정리 T 로 $m\ge2$ 에서 $2m$. [계산 확인] Grötzsch$[K_2]$: 83 쌍, 임의 순서, 최대 변화 3, 실패 0. Clebsch: 극대 타입 112, $m=2$ 168 쌍 임의 순서 최대 변화 3, 실패 0 (이 경우 brute force 폐포는 32정점이라 하지 않았고 타입 전개로만 검사 — 분류는 정리 1 의 증명에 의존).
의미: 차수·지름과 무관하게 $K_{s,s}$-자유 그래프는 색칠수가 아무리 커도 위상 하한은 $2s-1$ 을 못 넘는다. S1 은 이런 그래프에서 $t\le2s-1$ 만 말하게 된다 (어휘적으로 약한 명제).

### 6. 순환 거듭제곱 $C_n^2$ [증명]
**정리 C2.** $n\ge9$ 이면 $\tau(C_n^2[K_m])=3m$ ($m\ge1$). 특히 $\tau(C_n^2)=3$. $\chi(C_n^2)=4$ ($3\nmid n$) 인 $C_{10}^2,C_{11}^2$ 에서 $\tau<\chi$.
*증명.* $m=1$: 순서 $0,\dots,n-1$ 에서 완전이분쌍의 라벨에 $a_1<b_1<a_2<b_2$ (또는 $A,B$ 교환) 가 없음을 보인다(런 $\ge4$ ⇔ 길이 4 교대 부분열). 있다고 하자. $b_2-a_1\ge3$ 이고 $(a_1,b_2)$ 인접이므로 원형 거리 $\le2$ → $b_2-a_1\ge n-2$. 나머지 세 쌍 $(a_1,b_1),(b_1,a_2),(a_2,b_2)$ 의 선형 차는 각각 $\le(b_2-a_1)-2\le n-3$ 이라 $\le2$ 여야 한다. 합 $b_2-a_1\le6<n-2$ ($n\ge9$) — 모순. 그래서 런 $\le3$, $\tau\le3$.
$m\ge2$: $C_n^2$ ($n\ge9$) 의 클리크는 연속 3점에 포함. $z=3$: $\psi=0$. $z=2$: $Z=\{u,u+1\}$ 의 공통이웃 $\{u-1,u+2\}$ 는 서로 비인접 → $\min(x,y)=0$, $\psi\le2\le m$; $Z=\{u,u+2\}$: 공통이웃 $\{u+1\}$, $\psi\le1$. $z=1$: $N(u)$ 는 경로 $u-2,u-1,u+1,u+2$ 를 유도 ($n\ge9$) → $Y=\emptyset$ 이면 $\psi\le2$, 아니면 별 $K_{1,\le2}$ 라 $\psi\le3\le2m$. $z=0$: $K_{x,y}$ 는 $K_{1,4}$($\psi=3$)·$K_{2,2}$($\psi=4$)뿐($K_{2,3}$ 없음) $\le3m$ ($m\ge2$). 정리 3. ∎
[계산 확인] $n=9..12$, $m=1..4$ 에서 인증서 값이 $3m$. $n=9$: $m=1$ (18쌍), $m=2$ (180쌍) 폐포 brute force 와 일치, 자연 순서 유리수 정확 검사 실패 0.
$n=8$: $m=1$ 에서 $\{0,4\}\times\{2,6\}$ 가 런 4 를 주고 탐색한 순서들도 $\ge4$ ($\tau(C_8^2)\in\{3,4\}$ 열림); $m\ge2$ 는 $6,9,12$.

### 7. 예제 표
(인증서 값 = $1+\min_\sigma D_\sigma(m)$ 에서 얻은 $\tau$ 상한. "정확"= 하한 $\max(m\omega,\tau(G))$ 과 일치.)
| $G$ | $\omega$ | $\tau(G)$ | $m=1$ | $m=2$ | $m=3$ | 쓰임 |
|---|---|---|---|---|---|---|
| $K_n$ | $n$ | $n$ | $n$ | $2n$ | $3n$ | 오프셋 점검 ($K_1,K_2,K_3$) |
| $C_n$, $n\ge5$ | 2 | 3 | 3 | 4 | 6 | R03 재증명(정리 T) |
| Petersen | 2 | 3 | 3 | 4 정확 | 6 정확 | **지점 2**: $\tau>\omega$ 시험대 탈락 |
| Grötzsch | 2 | $\le4$ | $\le4$ | 4 정확 | 6 정확 | 정리 K·T |
| Clebsch | 2 | $\le4$ | $\le4$ | 4 정확 | 6 정확 | 정리 K·T |
| $W_5$ | 3 | $\le4$ | 4 | 6 정확 | 9 정확 | 허브+원: $m\ge2$ 붕괴 (정확 검증 $m=2,3$) |
| $\overline{C_7}=C_7^2$ | 3 | 3 | 3 | 6 정확 | 9 정확 | R02 값 재현 |
| $C_n^2$, $n\ge9$ | 3 | 3 | 3 | 6 | 9 | 정리 C2, $C_{10}^2$: $\tau<\chi$ |
| $C_9^3$ | 4 | $\le5$ | 5 | 8 | 12 | [계산 확인], 일반 증명 안 함 |
| 이분 $G$ (경로, 사다리, 격자, $K_{a,b}$) | 2 | 2 | 2 | 4 | 6 | $\chi$ 상한으로 자명; **순서 선택의 예**: 사다리 층별 순서 $m=1$ 인증서 3, 이분 순서면 2 |
**관찰(순서)**: 이분 순서에서는 $D_\sigma(m)=2m-1$ 로 $\chi$-상한을 재현한다. 일반으로 색류 순서의 인증서가 $\chi$-상한이다 ($Q_{\chi-1}$). 블로업에서 처음으로 좋은 순서의 존재가 아니라 $m$ 이 클 때 **순서와 무관하게** 작동하는 것이 정리 3 이다.

### 8. 결론 (c): $P[K_m]$ 과 S4·S5
- $\tau(P[K_m])=2m=\omega$ ($m\ge2$) [증명]. Dol'nikov–Kříž 하한은 정리 A 로 $\operatorname{cd}\le\tau=2m$ 이라 $\omega$ 이상을 줄 수 없다 — 하한 쪽에서 더 시도할 여지가 없다 (상한이 이미 맞는다).
- S4 ($K_t$ 세분)·S5 ($K_t$ 이머전), $t=\tau$: $K_{2m}\subseteq P[K_m]$ 부분그래프이므로 **자명하게 성립**. 반례를 줄 수 없다. 일반화: $m\ge m^*(G)$ 이면 $\tau=m\omega$ 이고 $K_{m\omega}\subseteq G[K_m]$ 이므로 S1·S2(홀수 마이너)·S4·S5 모두 자명. 이전 라운드의 Catlin 계열($\tau=\omega$)이 시험대가 못 된 이유도 이 붕괴로 설명된다.
- 블로업의 $\tau>\omega$ 사례는 $m<\tau(G)/\omega$ 일 때뿐이고 이것은 $G\subseteq G[K_m]$ 의 단조성이다 (예: $G=KG(11,4)$, $m=2$). 새 시험대가 아니다.
- 새로 필요한 것: $\tau(G)>\omega(G)$ 이면서 $G$ 자체가 S4/S5 시험 대상인 그래프. 정리 K 의 대우로 시험 가능 범위가 좁혀진다: $\tau(G)\ge2s$ 이면 $K_{s,s}\subseteq G$ 이고, $\tau\ge5$ 이면 $K_{2,3}\subseteq G$, $\tau\ge6$ 이면 $K_{3,3}\subseteq G$.

### 9. (보조) 모멘트 사상의 상에서 읽기 [증명 일부, 나머지 추측]
보조정리 G′ 에서 모멘트 사상 $g_d:B_0(G)\to\mathbb R^{d+1}$, $g_d(a^1)=(\gamma_d(t_a),1)$, $g_d(b^2)=-(\gamma_d(t_b),1)$ 의 영점은 정확히 순서 $\sigma$ 에서 런 수가 $\ge d+2$ 인 완전이분쌍의 면에서 나온다 [증명]. 곧 영점 ↔ 길이 $\ge d+2$ 지그재그. Steiner 정리 2 (5쪽; R04-r2 가 증명 검토 중) 가 지그재그 길이 $t$ 에서 홀수 마이너 $K_{\lfloor t/2\rfloor+1}$ 를 준다. 따라서 "$\tau\ge t$ ⇒ 영점 존재 ⇒ 지그재그 ⇒ 홀수 마이너 $K_{\lfloor t/2\rfloor+1}$" 가 S3(τ판)의 모멘트 사상 해석이다. S1 ($K_t$ 마이너, 반 줄지 않는 값) 에는 못 간다: 영점이 주는 정보는 교대 *경로* 하나와 그 완전이분 구조로, 클리크 쪽 변이 생기려면 같은 변의 두 점 사이의 연결이 필요한데 영점은 그것을 주지 않는다 [추측]. 반대로 정리 A 의 $\Phi:S^{c-1}\to B_0(G)$ (모멘트 곡선) 의 상은 $\operatorname{cd}$ 최소 집합 $U$ 의 구조를 읽게 한다. S1 에 필요한 "수축으로 클리크를 만드는" 정보는 이 두 사상 어디서도 직접 나오지 않는다 [추측]. 시간상 이 이상 시도하지 못했다.

### 10. 장애물 정리 (요청: R03-r1 §8 의 "차수 ≥3 에서 변화 수 초과" 점검)
- 초과는 실재한다: 사다리의 층별 순서(차수 3)에서 $m=1$ 인증서가 3($>\chi=2$), $C_7^2$ 의 자연 순환 순서에서 $m=1$ 인증서가 5($>\tau=3$). 순서를 고르면(이분 순서; $C_7^2$ 은 순서 탐색) 고쳐진다. 즉 장애물은 $\tau$ 가 아니라 **인증서의 순서 의존**이다.
- $m$ 이 크면 초과는 사라진다 (정리 3): 임계 $m^*\le\min(n-\omega+1,\operatorname{zig}+\omega-1)$.
- 인증서가 원리적으로 $m\omega$ 보다 크게 나오는 영역은 $m<\operatorname{zig}(G)/\omega$ 뿐이고 (명제 O) 그 영역의 진짜 $\tau$ 는 하한 $\max(m\omega,\tau(G))$ 와 인증서 사이에서 **열려 있다.** 이 창에서 상·하한이 어긋나는 그래프의 존재 여부가 S4/S5 시험대로 가능한 마지막 후보다.
- 수치 탐색(참고, 근거 아님): 정점 8–9 개 임의의 삼각형 없는 비이분 그래프 300개에서 $m=2$ 인증서가 4 를 넘는 사례를 지역 탐색으로 못 찾았다. 못 찾은 것은 비존재 증명이 아니다.

### 11. 참고한 논문 쪽 번호
Steiner 정리 2 (zig ⇒ 홀수 마이너) 5쪽을 SRC 요약 경유로 인용했을 뿐 새로 읽은 쪽 없음. 이 보고서의 정리 1–3, T, K, C2 는 논문 내용을 쓰지 않는다.

### 12. 도서관 확인 기록
- 시작 시: R04-researcher2-interim 읽음(내 지점 공격 없음). R04-researcher3 없음.
- 끝 직전: `R04-researcher2.md` (최종본) 를 읽었다. 정리 2 자립 검증, Dirac 귀납, R03 정리 공격이 전부이고 내 지점(블로업 타입·붕괴)에 대한 공격은 없다. 다만 그쪽 "$\overline{C_7}$ 에서 보조정리 5 색칠의 지그재그가 4 로 zig=3 보다 크다"는 관찰은 내 명제 O(zig=ρ=색칠 중 최소)와 모순이 없다(zig 는 최소 색칠에 대한 값). `R04-researcher3*` 는 끝까지 도서관에 **없었다.** 반영할 망상꾼 아이디어 없음.

## 후속연구 지점
1. **창 $\lceil\operatorname{zig}/\omega\rceil\le m<m^*$ 에서 $\tau(G[K_m])$ 의 진짜 값.** 무엇: $\tau(G[K_m])>\max(m\omega,\tau(G))$ 이거나 인증서와 하한이 어긋나는 $(G,m)$ 의 존재. 왜: S4/S5 의 유일한 남은 블로업 시험대. 시작: $\operatorname{zig}(G)$ 가 큰 삼각형 없는 그래프(Mycielski $M^3(K_2)$, $KG(8,3)$)의 $m=2,3$ 에서 정리 3 의 위반 타입을 찾고(어느 $\sigma$ 도 $D_\sigma>m\omega-1$), 그 타입이 위상적 하한에 실제 기여하는지 (등변사상의 존재/비존재) 본다. 난점: coind 하한 계산기가 없다. 하한은 $\operatorname{cd}$ 또는 호몰로지뿐.
2. **$\tau(C_8^2)\in\{3,4\}$ 판정과 $C_n^k$ ($k\ge3$) 일반화.** 왜: $\tau<\chi$ 의 연속 족에서 값이 정리 C2 의 증명 기법(교대 부분열 금지)으로 얻어지는지 시험. 시작: $C_n^k$ 에서 길이 $2k$ 교대 부분열을 금지하는 같은 거리 논증(정리 C2 의 거리 논증을 $2k$ 길이 교대 부분열에 맞춰 일반화), $C_9^3$ 인증서 5 를 증명으로 승격. 난점: $k\ge3$ 에서 타입이 복잡, $\tau=\omega$ 인지 불명.
3. **정리 3 의 비-완전 블롭 일반화 $G[H]$.** 무엇: 블롭을 $K_m$ 대신 $H$ 로 바꿀 때의 극대쌍 분류 (블롭 안의 완전이분 $\operatorname{biclique}(H)$ 가 추가). 왜: Catlin 반례는 비완전 합성도 포함하는 족. 시작: $H=\overline{K_m}$ (독립 블롭, $G[\overline{K_m}]\to G$ 준동형 동치) 와 $H=C_5$. 난점: 블롭 안의 순서가 $\operatorname{zig}(H)$ 에 걸린다.
4. **정리 K 의 정밀화.** 무엇: $K_{s,s}$-자유 ⇒ $\tau\le2s-1$ 의 최적성(그래프 족이 이 값에 닿는가)과 $K_{s,t}$-자유 ($s<t$) 판. 왜: $\tau$ 가 작은 큰 $\chi$ 그래프 족을 만드는 도구이고 S1 의 비자명 범위를 줄인다. 시작: $s=3$ 에서 $K_{3,3}$-자유이며 $\tau=5$ 인 그래프(예: $K_5$ 포함)와 $\tau=4$ 상한의 다른 후보. 난점: 하한은 $\chi\ge\tau$ 와 $\omega$ 뿐.
5. **[기억-미검증] 재확인.** (i) $\operatorname{cd}(KG(n,k))=n-2k+2$, (ii) $\chi(P[K_m])=\lceil5m/2\rceil$ 정확값 ($m$ 홀수 구성), (iii) 지그재그 규약의 대조(Steiner 원문 3–4쪽), (iv) $\tau(W_5)=4$ (join 공식). 시작: (ii) $m$ 홀수에서 $5$ 점 순환 $\lceil5m/2\rceil$-다중색칠(분수색칠 $5/2$ 의 라운딩), (iii) 원문 쪽수 확인. 난점: (iv) 는 join 에서 coind 가 합쳐지는지 증명 필요.
