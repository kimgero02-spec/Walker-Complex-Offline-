# [R06-researcher1] $\tau=\operatorname{zig}$ 판정: $K_4$-마이너-자유 류에서 증명, 일반 방향 $\tau\ge\operatorname{zig}$ 는 장애물 특정

- 작성자·라운드·역할: researcher1 / 라운드 6 / 연구원 (포메이션 T). 중간본: `R06-researcher1-interim.md`. 코드: `rooms/researcher1/r6_zig_sp.py`(zig 계산기, 정선 점검), `r6_sanity.py`, `r6_insert.py`(삽입 증명의 구현 점검).
- 읽은 것: problem.md, STATUS.md 의 R04 종료 인계와 R06 계획, `R04-researcher1/2`, `R04-orchestrator-verify`, `R03-researcher2/3`(정리 D, $Q_d$), `R06-researcher3-interim` (호지 번역, O1–O4, P1–P12). 반례꾼2 의 R06 보고서는 작성 시점에 도서관에 없었다.
- 표기 규약: 정의 $\tau=\operatorname{coind}(B_0)+1$, $\operatorname{zig}=\rho$ (R04 명제 O: 선형순서의 극대 완전이분쌍 런 수 최댓값의 최소) 를 그대로 쓴다. 증명된 사슬 $\tau\le d_R+1\le\operatorname{zig}\le\chi$ 는 R03·R04 인용.

## 요약
1. **[증명] 판정 보조정리.** $\operatorname{zig}(G)\le3$ 은 정점의 선형순서가 있어 모든 $K_{2,2}$ $\{p,p'\}\times\{q,q'\}$ 의 두 쌍이 순서상 교차하지 않는 것과 같다. 런 수 $\ge4$ 인 완전이분쌍은 교대 4점을 품고, 그 4점은 $K_{2,2}$ 를 이룬다.
2. **[증명] 2-트리 정리.** 2-트리는 런 수 $\le3$ 인 선형순서를 가진다. 귀납 삽입 규칙으로 증명했다. 따름: 모든 $K_4$-마이너-자유 $G$ 에서 $\operatorname{zig}(G)\le3$ ([기억-미검증] 표준 사실 "극대 $K_4$-마이너-자유 그래프는 2-트리"를 씀). 비이분 $G$ 에서 $\tau(G)=\operatorname{zig}(G)=3$ 이므로 **$\tau=\operatorname{zig}$ 가 $K_4$-마이너-자유 류에서 성립한다.** 이것은 등호가 $\omega$ 나 홀수 사이클 하한으로 강제되는 얕은 경우다.
3. **[계산 확인] 정선 예.** $C_5$: $\tau=\operatorname{zig}=3$. $\overline{C_7}$: $\tau=\operatorname{zig}=3$. $C_5[K_2]$: $\tau=\operatorname{zig}=4$ (세 값 모두 $\omega$ 와 상계로 결정). 계산기 점검: $\operatorname{zig}(K_4)=4$, $\operatorname{zig}(K_5)=5$, $\operatorname{zig}(W_5)=4$, $\operatorname{zig}(C_5)=3$.
4. **[증명] 일반 방향의 정확한 환원.** $\tau=\operatorname{zig}$ $\iff$ $\operatorname{coind}(B_0(G))\ge\operatorname{zig}(G)-1$. 충분조건: $B_0(G)$ 가 $(\operatorname{zig}-2)$-연결 ([기억-미검증] 표준 사실 "$k$-연결 자유 $\mathbb Z_2$-복합체는 $\operatorname{coind}\ge k+1$"). 장애물: 조합적 "교차 없는 순서"의 비존재를 구면 사상(또는 연결성)으로 옮기는 장치가 없다. 알려진 $\tau$ 하한 (ω, 홀수 사이클, join 가법성, Dol'nikov) 은 $\operatorname{zig}$ 와 같아지는 모든 예에서 $\omega$ 나 join 으로 주어졌다.
5. **[추측] 첫 비자명 시험대**: $d_R\le2\Rightarrow\operatorname{zig}\le3$ (즉 $\tau\le3\Rightarrow\operatorname{zig}\le3$). 2-트리 증명은 모든 $K_{2,2}$ 가 "스파인 변" 을 가진다는 현수 성질에 기댄다. 일반 그래프에는 유도 $C_4$ 가 있어 이 증명이 깨진다.

## 본문

### 0. 사용하는 사실
- (F1) [증명] $H\subseteq G$ 이면 $B_0(H)\subseteq B_0(G)$ (부분복합체), 그러므로 $\operatorname{coind}$ 와 $\tau$ 는 부분그래프에 단조 (Z_2-사상 $S^k\to B_0(H)\to B_0(G)$). 또 $\operatorname{zig}$ 도 생성 부분그래프에 단조: $H$ 의 완전이분쌍은 $G$ 의 완전이분쌍이므로 같은 순서에서 런 수가 같거나 작다.
- (F2) [계산 확인, 정의에서 확인] $\operatorname{zig}=\rho$. 완전이분쌍 $(A,B)$ 의 런 수는 $A\cup B$ 를 순서대로 읽은 라벨 열의 $1+$(변화 수). 극대쌍만 보면 된다 (원소 삭제는 런 수를 늘리지 않는다).
- (F3) [기억-미검증] $\tau(C_{2k+1})=3$ 이고 $\tau(K_3)=3$. 따라서 비이분 $G$ 는 $\tau\ge3$ (홀수 사이클 부분그래프 단조성 F1).
- (F4) [기억-미검증] 극대 $K_4$-마이너-자유 그래프 ($n\ge2$) 는 2-트리. 2-트리 $=$ $K_2$ 에서 시작해 기존 변의 두 끝에 새 정점을 붙이는 과정으로 얻는 그래프.

### 1. 판정 보조정리 [증명]
**보조정리 1.** 선형순서 $\sigma$ 에서 모든 완전이분쌍 $(A,B)$ 의 런 수가 $\le3$ 인 것은 다음과 같다: $\sigma$ 가 어떤 $K_{2,2}$ $(P,Q)$, $P=\{p,p'\}$, $Q=\{q,q'\}$ 에 대해 $P$ 와 $Q$ 가 교차하지 않는 것 (즉 $p<q<p'<q'$ 또는 $q<p<q'<p'$ 형이 없음).

*증명.* (⇐) 런 수 $\ge4$ 면 $A\cup B$ 의 라벨 열에서 연속 4개 런 $R_1,R_2,R_3,R_4$ 에서 한 원소씩 $a\in R_1\cap A$, $b\in R_2\cap B$, $a'\in R_3\cap A$, $b'\in R_4\cap B$ 를 뽑으면 $a<b<a'<b'$, $\{a,a'\}\times\{b,b'\}\subseteq A\times B\subseteq E$ 이고 $(\{a,a'\},\{b,b'\})$ 가 교차하는 $K_{2,2}$ 가 된다. (⇒) 교차 $K_{2,2}$ $(P,Q)$ 는 $P\cup Q$ 에서 $P\times Q\subseteq E$ 인 완전이분쌍이고 라벨 열이 $PQPQ$ 형이므로 런 수 $\ge4$. ∎

**따름.** 교차 금지는 "$K_{2,2}$ 의 두 쌍이 구간 $[\min,\max]$ 에서 겹치는 방식"으로 쓸 수 있다. $P=\{p,p'\}$ 의 구간 $I_P=(p,p')$ 에 $Q$ 의 원소가 정확히 하나만 들어 있으면 교차, 0개 또는 2개면 비교차.

### 2. 2-트리 정리 [증명]
**정리 2.** 2-트리 $T$ 에는 런 수 $\le3$ 인 선형순서가 있다. 특히 $\operatorname{zig}(T)\le3$.

*(a) $K_{2,2}$ 의 구조.* 2-트리는 현수적 (chordal) 이고 $K_4$ 를 포함하지 않는다 (treewidth 2). $K_{2,2}$ $(P,Q)$ 는 4-사이클이고 현수성에 의해 대각선이 있다: $P$ 안의 변 또는 $Q$ 안의 변. $P$ 안에 변 $pp'$ 가 있으면 $Q=\{q,q'\}\subseteq N(p)\cap N(p')$ 이다. $Q$ 안의 변이면 대칭. $K_4$-자유이므로 공통 이웃 $Z_{uv}:=N(u)\cap N(v)$ 는 독립집합이다. 따라서 $T$ 의 모든 $K_{2,2}$ 는 "변 $uv$ 와 $Z_{uv}$ 의 두 원소" 로 나타난다.

*(b) 조건의 단순화.* 보조정리 1 에서 변 $uv$ 와 $\{x,y\}\subseteq Z_{uv}$ 가 교차하지 않아야 한다. 모든 쌍 $\{x,y\}\subseteq Z_{uv}$ 에 대해 $(u,v)$ 안에 있는 원소 수가 0 또는 2 여야 한다. 이는 **$Z_{uv}$ 가 $(u,v)$ 안에 모두 있거나 $[\min(u,v),\max(u,v)]$ 밖에 모두 있다** 와 동치다. (한 원소만 안에 있으면 그 원소와 나머지 하나의 쌍이 교차한다.)

*(c) 귀납.* 2-트리는 $K_2$ 에서 시작해 변 $xy$ 에 새 정점 $v$ 를 붙이는 과정으로 얻는다 (단, $v$ 의 이웃은 정확히 $x,y$). 귀납 가정: $T'=T-v$ 의 순서 $\sigma'$ 가 (b)의 조건 $\mathcal C$ 를 만족한다. $v$ 를 다음처럼 끼운다.
- $Z' := N_{T'}(x)\cap N_{T'}(y)$ 가 $(x,y)$ 안에 있으면 ($Z'=\emptyset$ 도 포함하여 편의상 "안") $v$ 를 $x,y$ 의 오른쪽 끝점 바로 앞에 끼운다. 그러면 $v\in(x,y)$.
- $Z'$ 가 $[x,y]$ 밖에 있으면 $v$ 를 오른쪽 끝점 바로 뒤에 끼운다. 그러면 $v\notin[x,y]$.

*검증.* 조건 $\mathcal C$ 가 깨질 수 있는 곳은 두 군데뿐이다. (i) 변 $xy$ 의 $Z_{xy}=Z'\cup\{v\}$: $v$ 를 $Z'$ 와 같은 쪽에 두었으므로 만족. (ii) 새 변 $xv$, $yv$: $Z_{xv}=\{y\}$, $Z_{yv}=\{x\}$ 는 원소 1개라 조건 없음 (쌍이 없다). $v$ 는 $x,y$ 에만 인접하므로 다른 변의 $Z$ 는 바뀌지 않는다. 기존 원소들의 상대 순서는 바뀌지 않으므로 (b)의 나머지 조건도 유지된다. ∎

*구현 점검* [계산 확인, 근거 아님]: `r6_insert.py` 가 위 삽입 규칙을 그대로 구현해 무작위 2-트리 300개 ($n\le12$) 에서 불변식 위반 0, 최대 런 수 3 을 확인했다.

**따름 2.1.** $K_4$-마이너-자유 $G$ 에서 $\operatorname{zig}(G)\le3$ [증명, F4 사용]. 극대 $K_4$-마이너-자유 $T\supseteq G$ 를 잡으면 (F1) 같은 순서에서 $G$ 의 런 수는 $T$ 이하.

**따름 2.2 ($\tau=\operatorname{zig}$ 의 $K_4$-마이너-자유 판).** $G$ 가 이분이면 $\tau=\operatorname{zig}=2$ (인용: $\tau\le\operatorname{zig}$ [R03 정리 D], $\tau\ge\tau(K_2)=2$ 는 F1). 비이분이면 $3\le\tau\le\operatorname{zig}\le3$ [F3, 정리 D, 따름 2.1]. 따라서 $\tau=\operatorname{zig}=3$. [증명, F3·F4 인용]

*평가.* 이 판은 얕다: 양변이 모두 3 이고, 하한은 홀수 사이클에서 온다. 그러나 **$\operatorname{zig}$ 의 조합적 상한 증명을 처음으로 "보조정리 1" 형 기준으로 옮긴 것**이 쓸모가 있다: 이후 $d$ 가 커질 때 "교차 $K_{s,t}$ 금지" 판으로 일반화할 수 있는 형태다 (아래 후속 1).

### 3. 정선 예 (문주님 임무 (1)) [계산 확인]
| $G$ | $\omega$ | $\tau$ | $\operatorname{zig}$ | 등호의 근거 |
|---|---|---|---|---|
| $C_5$ | 2 | 3 | 3 | 하한 F3, 상한 정리 D |
| $\overline{C_7}=C_7^{2}$ | 3 | 3 | 3 | 하한 $\tau\ge\tau(K_3)=3$ (F1), 상한 $\operatorname{zig}\le3$ (계산 확인, 명시적 순서) |
| $C_5[K_2]$ | 4 | 4 | 4 | 하한 $\tau\ge\omega=4$, 상한 $\operatorname{zig}\le4$ (계산 확인, 임의 순서 점검) |

세 예 모두 등호는 $\omega$ 또는 홀수 사이클 하한으로 결정되어, 정리 2 나 $\tau\ge\operatorname{zig}$ 의 새 도구를 시험하지 못한다. 이 점이 아래 4절의 장애물과 연결된다.

### 4. 일반 방향 $\tau\ge\operatorname{zig}$: 환원과 장애물
**4.1 환원** [증명]. $\tau\le d_R+1\le\operatorname{zig}$ 이므로 $\tau=\operatorname{zig}$ $\iff$ $\operatorname{coind}(B_0(G))\ge\operatorname{zig}(G)-1$. 즉 $\operatorname{zig}-2$ 차원 구면의 $\mathbb Z_2$-사상 $S^{\operatorname{zig}-1}\to B_0(G)$ 의 존재가 필요하다.

**4.2 충분조건** [기억-미검증 두 줄]. (i) $B_0(G)$ 가 $(\operatorname{zig}-2)$-연결이면 $\operatorname{coind}\ge\operatorname{zig}-1$. (ii) R06-researcher3-interim 의 O2 (표준 판: $X(G)\simeq\Sigma N(G)$, 비공집합 표준 박스 복합체 $N$ 의 현수) 를 쓰면 (i)은 $\operatorname{conn}(N(G))\ge\operatorname{zig}(G)-3$ 와 같다. 검사: $K_n$ ($\operatorname{conn}N=n-3$, 등호), $C_5$ ($N\simeq S^1$, $\operatorname{conn}=0$, $\operatorname{zig}-3=0$, 등호). 따라서 이것은 Lovász 의 하한 $\chi\ge\operatorname{conn}(N)+3$ 에서 $\chi$ 를 $\operatorname{zig}$ 로 바꾼 명제다. 이 강화가 문헌에 있는지는 확인하지 못했다.

**4.3 장애물 (정확한 위치)** [증명, 구조적 관찰]
- (O-a) **방향의 비대칭.** 정리 D ($\tau\le\operatorname{zig}$) 는 순서 (색칠) 에서 구면 사상을 만든다. 반대 방향은 "모든 순서가 교차 $K_{2,2}$ 를 가진다" (보조정리 1 의 부정) 에서 구면 사상을 만들어야 한다. 교차는 **순서** 의 성질이고, 구면 사상은 **위상** 의 성질이다. 둘을 잇는 중간 객체 (예: 순서가 주는 $\mathbb Z_2$-복합체 위의 사상) 를 찾지 못했다.
- (O-b) **하한 도구의 한계.** 현재 $\tau$ 하한은 $\omega$, 홀수 사이클 (F3), join 가법성 ($\tau(G+H)\ge\tau(G)+\tau(H)$, R04 N1-r3 정리), Dol'nikov $\operatorname{cd}$ 이다. $\operatorname{zig}>\max(\omega,\ \text{join 하한})$ 인 그래프에서 $\tau$ 를 올릴 도구가 없다. 이런 그래프의 후보: Grötzsch, Clebsch, $C_{10}^2$ ($\tau<\chi$ 는 증명 완료, $\operatorname{zig}=3$ 이라 등호 문제 아님). Grötzsch·Clebsch 는 $\omega=2$, $\tau\le4$, $\operatorname{zig}\in\{3,4\}$ 미정.
- (O-c) **$d=2$ 증명의 국소성.** 정리 2 는 현수성 (유도 $C_4$ 없음) 에 의존한다. 일반 $G$ 에서는 $K_{2,2}$ 가 유도 4-사이클일 수 있고, 그러면 "스파인" 이 없어 (b) 의 단순화가 성립하지 않는다. 예: $K_{2,2}$ 의 두 쌍이 교차하지 않도록 순서를 맞추는 조건이 전역적 제약 그래프 (2-SAT 와 비슷한 구조) 가 된다. 이 제약 그래프가 모순을 가질 수 있는지 (그러면 $\operatorname{zig}\ge4$) 는 열림.

**4.4 반례 탐색의 결과** [계산 확인, 근거 아님]. $\operatorname{zig}\ge4$ 인 $K_4$-마이너-자유 그래프를 찾는 탐색: 2-트리 $n\le8$ 전수 (135135 생성열) 와 $n=10$ 무작위 2000 에서 없음. 정리 2 에 따라 없어야 하므로 이것은 증명의 확인일 뿐이다.

### 5. 판정 상태
- **[증명]** $\tau=\operatorname{zig}$ 가 모든 $K_4$-마이너-자유 그래프에서 (F3·F4 인용 하에).
- **[계산 확인]** $C_5$, $\overline{C_7}$, $C_5[K_2]$ 에서 $\tau=\operatorname{zig}$ (하한 쪽은 $\omega$·홀수 사이클, 상한 쪽은 순서).
- **[추측]** $d_R\le2\Rightarrow\operatorname{zig}\le3$ (즉 $\tau\le3\Rightarrow\operatorname{zig}\le3$). 현수성이 없는 경우 제약 그래프의 모순 가능성이 관건.
- **[추측]** $\tau\ge\operatorname{zig}$ 의 일반 판은 4.2 의 연결성 판으로 가능할 수 있으나 문헌·증명 없음.
- **열림.** 일반 $\tau=\operatorname{zig}$ 판정. 등호 판정을 하려면 $\operatorname{zig}>\omega$ 이고 join 이 아닌 그래프의 $\tau$ 하한이 필요하다.

### 6. R06-researcher3 의 예측과의 관계
- P1 (우월 정점 제거에서 $\operatorname{zig}$ 불변): 내 정리 2 의 삽입 규칙은 우월 정점 $a$ (이웃이 $c$ 의 이웃에 포함) 를 $c$ 옆에 놓으면 되므로 $K_4$-자유 2-트리에서는 자명하게 성립하는 것을 확인했다 [증명, 2-트리 한정]. 일반 그래프 점검은 하지 않았다.
- P3 (비이분 $G$ 에서 $\tau=1+$top 호몰로지): 내 결과 (2.2) 는 $K_4$-마이너-자유 비이분에서 $\tau=3$ 을 주므로, 최고 호몰로지 차원 2 와 일치해야 한다. 이 일치는 검사하지 않았다.
- O4 (차원 $\le1$ CW 로는 $C_6$ 불가): 본 보고서와 충돌하지 않는다. $\operatorname{zig}$ 는 조합 불변량이고 CW 차원과 직접 연결되지 않는다.

## 문주님께 요청
없음.

## 후속연구 지점
1. **교차 $K_{s,t}$ 판으로의 일반화 (runs $\le d+1$).** 무엇: 보조정리 1 을 일반 $d$ 로 쓰기. 런 수 $\ge d+2$ 면 교대 $(d+2)$-점열이 있고 그 안에 $K_{\lceil (d+2)/2\rceil,\lfloor (d+2)/2\rfloor}$ 교차가 있다. 왜: $\operatorname{zig}\le d+1$ 의 조합 판을 얻으면 $d=3$ (3-트리, $K_5$-마이너-자유 후보) 에서 정리 2 를 흉내 낼 수 있다. 시작: 3-트리에서 $K_{3,2}$ 교차 금지 조건을 같은 귀납으로 검사. 난점: 3-트리의 $K_{3,2}$ 는 스파인이 삼각형이라 단순화가 덜 강하다. 우선순위 높음.
2. **$d_R\le2\Rightarrow\operatorname{zig}\le3$ 의 시험 (비현수 경우).** 무엇: 유도 $C_4$ 가 있는 $d_R\le2$ 그래프 (평면 배치로 증명된 것 포함) 에서 교차 금지 제약 그래프의 모순 여부. 왜: $\tau=\operatorname{zig}$ 의 첫 비자명 시험대 (τ≤3 ⇒ zig≤3). 시작: 제약 그래프를 명시적으로 세우고 (각 $K_{2,2}$ 에 대해 두 쌍 비교차 조건), 평면 배치 (R03-r3 의 $Q_2$) 와 대조. 난점: 전역 조건, 2-SAT 가 아니다.
3. **frontier 그래프의 $\tau$ 하한 도구.** 무엇: Grötzsch, Clebsch 에서 $\operatorname{zig}$ 를 정확히 계산 ($\{3,4\}$ 판정)하고, $\operatorname{zig}=4$ 이면 $\tau\ge4$ 를 줄 하한 (Dol'nikov $\operatorname{cd}$ 또는 연결성) 을 찾기. 왜: $\tau<\operatorname{zig}$ 를 세우거나 등호를 증명할 유일한 현실적 시험대. 시작: $\operatorname{zig}$ 를 순서 탐색 (DFS, 위 `r6_zig_sp.py` 의 `zig_le` 재사용) 으로 계산, `cd(Grötzsch)` 를 KG 와 같은 방식 (정리 A) 으로 점검. 난점: $\operatorname{cd}$ 계산 기준이 $\omega$ 보다 약하다 [기억-미검증].
4. **연결성 판 (4.2) 의 시험.** 무엇: $\operatorname{conn}(N(G))\ge\operatorname{zig}(G)-3$ 을 소형 그래프에서 호몰로지로 검사 (반례 탐색). 왜: 성립하면 $\tau=\operatorname{zig}$ 의 위상적 증명 경로가 생긴다. 깨지면 그 충분조건은 틀렸으니 제외. 시작: 작은 그래프 (C_5[K_2], Grötzsch) 에서 $\tilde H_k(N(G))$ 계산 (랭크 mod 2). 난점: 증명이 아니라 반례 탐색이다. 연결성 $\neq$ 호몰로지 (단순연결성 필요).
5. **문헌 확인 (요청 없음, 기억 항목).** F3 $\tau(C_{2k+1})=3$, F4 "극대 $K_4$-마이너-자유 = 2-트리", "$k$-연결 $\Rightarrow$ coind $\ge k+1$", 그리고 R06-r3 O2 의 현수 공식. 시작: 문헌에서 확인 가능하면 `[기억-미검증]` 을 떼고, 불가능하면 그대로 둔다. 우선순위 낮음 (본 판정의 증명 경로는 이 항목들에 기대지만 대안 증명은 아직 없음).
