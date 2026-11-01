# [F-R10-N-turn1-A] 기본 정의 𝔅 (다) 의 확정 형식화, 𝔄 (나) 를 특수 경우로 두기, 미합의 항목 입장

- 작성: 형식주의자 A (포메이션 N, 1턴, 논검객 갑 과제). 근거: `F-R8-formal-A.md`, `F-R9-dialogue-A.md`, 그리고 합의 항목 (R9). 형식주의자 B 산출물은 이 문서에서 쓰지 않았다.
- 표기: $B$ 검정, $J$ 흰, $V=B\sqcup J$. $E_{\bullet\bullet}\subseteq\binom B2$, $E_{\bullet\circ}\subseteq B\times J$, $E_{\circ\circ}\subseteq\binom J2$, $\partial\subseteq E_{\bullet\bullet}$. 포트 $N(w)$, 조각 $\mathcal P$ (= $(B,E_{\bullet\bullet})$ 의 연결성분), $P_K$.
- 태그: [증명] (이 문서에서 확인), [추측] (미확인).

---

## 1. 기본 정의 (다): 𝔅

### 1.1 튜플
$$\mathfrak B=(B,\;J,\;E_{\bullet\bullet},\;E_{\bullet\circ},\;E_{\circ\circ},\;\partial).$$
- $E_{\circ\circ}$ 는 **파생 성분**이다. 데이터가 아니다: $E_{\circ\circ}:=D(\mathfrak B)$ (정의 1.3). 튜플에 적는 것은 읽기 편의를 위한 것이며, 자유도는 없다.
- $\partial$ 는 경계 표시 (일반층에서는 임의, 리본층에서는 (R1)).
- 망각 $U\mathfrak B:=(B,J,E_{\bullet\bullet},E_{\bullet\circ})$ (이것이 접합 그래프 $\mathfrak A$ 이다).

### 1.2 공리 (일반층 $\mathcal G$)
- **(D0) 자료형.** $B\cap J=\emptyset$, 두 집합 유한. $E_{\bullet\bullet}\subseteq\binom B2$, $E_{\bullet\circ}\subseteq B\times J$, $\partial\subseteq E_{\bullet\bullet}$.
- **(D1) 포트.** $\forall w\in J:\ |N(w)|\ge2$. (상한 없음, 일반층 $\mu=\infty$.)
- **(D2) 엄격 류.** $\forall x\in B:\ |W(x)|\le1$, $W(x):=\{w:x\in N(w)\}$. 블록 분할 $[\cdot]:B\to\pi$, $\pi:=\{N(w)\}_{w\in J}\cup\{\{x\}:x\notin\bigcup N(w)\}$.
- **(D3) 조각 평면.** $\forall K\in\mathcal P:\ P_K$ 는 평면.
- **(D4) 고리 금지.** $\forall w,\ \forall x,y\in N(w):\ xy\notin E_{\bullet\bullet}$. (합의 R9.)
- **(D5) 파생 흰–흰 간선.** $E_{\circ\circ}=D(\mathfrak B)$ (정의 1.3).

### 1.3 파생 성분
$$K_F(w,w'):=\{K\in\mathcal P:\ \exists x\in N(w)\cap V(K),\ x'\in N(w')\cap V(K),\ xx'\in F\},$$
$$D(\mathfrak B):=\{\{w,w'\}\subseteq J:\ |K_{E_{\bullet\bullet}}(w,w')|\ge2\}.$$
- 이 정의는 $\partial$ 를 쓰지 않는다. 그래서 $D(\mathfrak B)$ 는 $U\mathfrak B$ 의 함수이다 (합의 R9: "흰–흰 간선은 파생").
- 리본층에서는 §3 의 (R5) 와 함께 $D=D_\partial$ 가 된다 (명제 2).

### 1.4 조립
$$G(\mathfrak B):=\operatorname{simp}\bigl(\widehat G(\mathfrak B)\bigr),\qquad \widehat G(\mathfrak B):=\mathfrak B/\{S_w\}_{w\in J}, \quad S_w=\{w\}\cup N(w).$$
구체적으로: 정점 $\pi$, 변 $\{[x],[y]\}$ ($xy\in E_{\bullet\bullet}$). 파생 흰–흰 간선 $ww'$ 의 상은 $\{N(w),N(w')\}$ 인데, 이것은 $xx'$ 의 상과 같으므로 조립에 새 변을 주지 않는다 (명제 1). 따라서 $G(\mathfrak B)=G(U\mathfrak B)$ [증명].

### 1.5 색칠 읽기
$\mathfrak A^{(t)}$ 와 $a_t$ 는 $U\mathfrak B$ 에서만 정의한다. 정리 A ($\chi(G)=\min\{t+1:a_t\le t+1\}$) 와 정리 B 는 $U\mathfrak B$ 에 대해 말한다 [증명, F-R6 보조정리 3, 4].

### 1.6 두 평면성 (이름 고정)
- **𝔄-평면성.** 단순 그래프 $\mathfrak A:=U\mathfrak B$ (정점 $V$, 변 $E_{\bullet\bullet}\cup E_{\bullet\circ}$) 가 평면이다.
- **𝔅-평면성.** 단순 그래프 $\mathfrak B^\flat:=(V,\ E_{\bullet\bullet}\cup E_{\bullet\circ}\cup E_{\circ\circ})$ 가 평면이다.
- **관계.** $\mathfrak A\subseteq\mathfrak B^\flat$ 이므로 𝔅-평면성 ⟹ 𝔄-평면성 [증명]. 흰 별 축약은 연결 부분그래프의 수축이므로 𝔄-평면성 ⟹ $G(\mathfrak B)$ 평면성 [증명]. 따라서 **𝔅-pl ⟹ 𝔄-pl ⟹ $G$-pl**.
- 두 평면성은 $E_{\circ\circ}\neq\emptyset$ 일 때만 갈릴 수 있다 (명제 1 (iii)). 어떤 설명서 평면성을 쓰는 정리인지 항상 이름으로 적는다.

---

## 2. 리본층 $\mathcal R\subseteq\mathcal G$ (합의 R9 적용)

조건 (μ=2, 단면은 공유 흰 점 집합으로 정의):
- **(R0) 두 포트.** $\forall w:\ |N(w)|=2$, 두 포트는 서로 다른 조각 $P,Q$ 에 있다.
- **(R1) 원판 조각.** $\forall K$: $P_K$ 2-연결, $\partial\cap E(P_K)=E(C_K)$ 인 사이클 $C_K$, $C_K$ 는 어떤 평면 매장의 바깥면 경계. 모든 포트 $x\in N(w)\cap V(K)$ 는 $x\in V(C_K)$.
- **(R2) 쌍 크기.** $\forall\{w,w'\}$: $|K_\partial(w,w')|\in\{0,2\}$.
- **(R3) 단면.** 단면은 공유 흰 점 집합 $\sigma(\mathfrak B):=\{w\in J:\ \exists w':\ \{w,w'\}\in D\}$ 이다. 리본층에서 $\sigma=J$ (단면 $\emptyset$ 금지).
- **(R4) 다중 링크.** $\forall w\ \exists!\ w':\ \{w,w'\}\in D_\partial$.
- **(R5) 단순 몫.** $m(\beta,\gamma):=\#\{xy\in E_{\bullet\bullet}:[x]=\beta,[y]=\gamma\}\ge2$ ⟹ $\{\beta,\gamma\}=\{N(w),N(w')\}$ 이고 $\{w,w'\}\in D_\partial$, $m=|K_\partial(w,w')|$.

**명제 2.** 리본 (R0)–(R5) 아래 $D=D_\partial$ 이고, 흰 점마다 호 (짝) 가 정확히 하나다 [증명: (R5) 에서 공유 간선은 모두 경계, (R4) 에서 짝은 유일].

---

## 3. (나) 를 특수 경우로 두기

### 3.1 (나) 의 정의
$$\mathcal A\text{-(나)}:=\{\mathfrak B\in\mathcal G:\ \partial=\emptyset\}.$$
여기서 $E_{\circ\circ}=D(\mathfrak B)$ 는 자동으로 얻는다.

### 3.2 명제 N (정확히 (나) 와 같은가)
(i) **일대일.** 사상 $U:\{\mathfrak B\in\mathcal G:\partial=\emptyset\}\to\mathcal A$ 는 전단사이고 역은 $\mathfrak A\mapsto(\mathfrak A,\emptyset)$ 이다 [증명: $E_{\circ\circ}$ 는 $\mathfrak A$ 의 함수이고 $\partial=\emptyset$ 이다].

(ii) **조립.** $G(\mathfrak B)=G(U\mathfrak B)$ [증명, §1.4].

(iii) **색칠.** $a_t$ 와 정리 A, B 는 $U\mathfrak B$ 에서 같다 [증명].

(iv) **평면성.** 𝔄-평면성은 $U$ 에 대해 같다 [정의]. 𝔅-평면성은 $D(\mathfrak A)\neq\emptyset$ 이면 𝔄-평면성보다 강할 수 있다 (반례가 있는지는 Y 예로 확인해야 함, 미확인).

(v) **"$E_{\circ\circ}=\emptyset$ 인 𝔅" 과의 관계 (정정).** 질문하신 "$E_{\circ\circ}=\emptyset$ 이고 $\partial=\emptyset$ 인 𝔅" 은 (나) 와 **같지 않다**. 정확히는
$$\{\mathfrak B:\ \partial=\emptyset,\ E_{\circ\circ}=\emptyset\}=\{\mathfrak B:\ \partial=\emptyset,\ D(\mathfrak A)=\emptyset\}\cong\{\mathfrak A:\ \text{공유 간선 없음}\}\subsetneq\mathcal A.$$
이유: $E_{\circ\circ}=D(\mathfrak A)$ 이고, 공유 간선이 있는 $\mathfrak A$ (예: $E_1\cap E_2\neq\emptyset$ 인 $\mathfrak A_{12}$) 는 $E_{\circ\circ}\neq\emptyset$ 을 가진다 [증명]. 따라서 "$E_{\circ\circ}=\emptyset$" 을 (나) 의 조건으로 쓰면 공유 간선을 가진 $\mathfrak A$ 가 빠진다. 명제 N (i) 가 맞는 특수 경우 진술이다: **(나) = $\{\mathfrak B:\partial=\emptyset\}$ (파생 $E_{\circ\circ}$ 는 자동)**.

(vi) **리본과의 관계.** $\partial=\emptyset$ 인 리본은 없다 ((R1) 에서 사이클이 필요) [증명]. 따라서 리본층은 (나) 의 어떤 부분집합과도 겹치지 않는다. 리본층에서 $\mathfrak A$ 를 되찾으려면 $\partial$ 를 함께 적어야 한다.

---

## 4. 미합의 항목에 대한 나의 입장 (한 줄씩)

1. **리본 μ=2 와 단면 ∅ 금지의 동치 여부.** 입장: **동치 아님** (B 의 판단 맞음). 차이는 다중도다. (R3) 는 "각 흰 점이 짝을 가짐" 이고 (R4) 는 "짝이 정확히 하나" 이므로, (R0)+(R3) 만으로는 두 짝을 허용하는 $\mu=2$ 구성이 남는다 [증명].
2. **세 조각 접합이 필요한 $G$ 의 존재.** 입장: **미결** [추측]. 일반층 $\mu=\infty$ 를 기본값으로 두고, 존재 여부는 후속 1 로 넘긴다.
3. **Y 예 재현.** 입장: **미확인**. 구조상 Y 는 $\mathfrak A$-평면이지만 $\mathfrak B$-비평면인 예 (또는 역) 를 줄 수 있다는 것만 말할 수 있다 [추측]. Y 를 직접 그리지 않았다.

---

## 5. 요약 (1턴)

- 기본 정의: (다) $\mathfrak B=(B,J,E_{\bullet\bullet},E_{\bullet\circ},E_{\circ\circ},\partial)$, $E_{\circ\circ}=D(\mathfrak B)$ 파생, 공리 (D0)–(D5), 리본 (R0)–(R5).
- 평면성 이름: 𝔄-평면성, 𝔅-평면성, 관계 𝔅-pl ⟹ 𝔄-pl ⟹ $G$-pl.
- (나): $\{\mathfrak B:\partial=\emptyset\}$ 와 일대일. "$E_{\circ\circ}=\emptyset$ 과 $\partial=\emptyset$" 로 쓰면 공유 간선 없는 $\mathfrak A$ 만 남으므로 이 조건은 정정이 필요하다.
- 미합의: 동치 아님 (차이는 다중도), 세 조각 접합 반례 미결, Y 미확인.

## 문주님께 요청
없음. 단, (나) 의 조건 문구는 "$E_{\circ\circ}=\emptyset$" 대신 "$\partial=\emptyset$" 로 정정할 것을 오케에 제안한다 (§3.2 (v)).

## 후속연구 지점

1. **(우선 1) 세 조각 접합이 필요한 $G$ 의 결정적 반례.** 이유: μ 를 일반층에서 ∞ 로 둔 근거가 이 반례의 유무에 달려 있다. 시작: 한 정점이 세 조각에 걸린 $\mathfrak A$ 를 모든 $\alpha=1$ 표현 공간에서 비교한다. 난점: 표현 공간이 커서 완전 탐색이 어렵다.
2. **(우선 2) Y 재현과 𝔅-평면성의 정보량.** 이유: $E_{\circ\circ}\ne\emptyset$ 일 때 𝔅-평면성이 𝔄-평면성보다 강한지가 정의의 실질을 정한다. 시작: $D(\mathfrak A)\neq\emptyset$ 인 작은 $\mathfrak A$ 에서 두 평면성을 비교하는 표를 만든다. 난점: 파생 간선이 평면 매장을 강제하는 방식을 정리해야 한다.
3. **(우선 3) 리본 (R4) 의 다중도 조건이 정말 필요한가.** 이유: 다중도 (정확히 하나) 가 빠지면 두 짝 구성이 들어온다. 시작: 두 짝을 허용한 리본 판에서 조립 $G$ 가 어떻게 바뀌는지, 그리고 정리 Mix 가 깨지는지 확인한다. 난점: 정리 Mix 의 전제 (호 분해 유일성) 를 다시 증명해야 한다.
