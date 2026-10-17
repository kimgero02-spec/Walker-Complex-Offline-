# [F-R11-final-B-review-2] F-R11 개정본 최종 검토 (형식주의자 B): 판정 **승인**

- 검토 대상: `F-R11-final-A-rev.md` (전체와 변경 절을 읽음). 기준: `F-R11-final-A.md`, 내 `F-R11-final-B-review.md`.
- 커밋하지 않았다.
- 태그: [증명] (이 검토에서 확인).

---

## 0. 판정

**승인.** 필수 1건 (𝒜^N 과 명제 N) 과 권고 2건 (|V(G)|≤2 정리, K_3 예) 이 모두 반영되었고, 반영 문장은 다른 절과 모순되지 않는다.

## 1. (1) 𝒜^N 과 명제 N 의 전단사

- 정의: $\mathcal A^N:=\{\mathfrak A\in\mathcal A:\ (N)\}$ (§1.2). (N) 은 $\mathfrak A$ 의 조각과 $G(\mathfrak A)$ 만 쓴다 [증명].
- 정방향 $U:\mathcal G^N\cap\{\partial=\varnothing\}\to\mathcal A^N$: $U\mathfrak B=\mathfrak A$ 는 (G0′),(G1)–(G4) 를 만족한다 (이 조건들은 ∂ 를 쓰지 않는다). 조각은 $(B,E_{\bullet\bullet})$ 의 성분이므로 $\mathfrak B$ 와 $\mathfrak A$ 에서 같고, $G(\mathfrak B)=G(\mathfrak A)$ (보조정리 1). 따라서 (N) 도 같다 [증명].
- 역 $\mathfrak A\mapsto(\mathfrak A,\varnothing)$: $E_{\circ\circ}:=D(\mathfrak A)$ 는 파생이므로 자동 정해진다. (G0)–(G4) 는 $\mathfrak A$ 의 조건과 $\partial=\varnothing\subseteq E_{\bullet\bullet}$ 로 성립한다. (N) 은 $\mathfrak A\in\mathcal A^N$ 에서 성립한다. 따라서 $(\mathfrak A,\varnothing)\in\mathcal G^N\cap\{\partial=\varnothing\}$ [증명].
- 두 합성: $U(\mathfrak A,\varnothing)=\mathfrak A$. 그리고 $\mathfrak B\in\mathcal G^N\cap\{\partial=\varnothing\}$ 에 대해 $(U\mathfrak B,\varnothing)=\mathfrak B$ 인데, $E_{\circ\circ}$ 가 $D$ 로 정해지는 것은 $\mathcal G$ 의 공리 (D5) 이므로 성립한다 [증명].
- **판정: 증명 맞다.** 역 사상이 $\mathcal G^N$ 에 드는 이유 (E∘∘ 파생, (N) 의 ∂-무관성) 가 본문에 쓰여 있다.

## 2. (2) §6.4 명제 N 행

- 행: "명제 N ((나) ↔ 𝒜^N, U 전단사) | 예: $\mathcal G^N\cap\{\partial=\varnothing\}\leftrightarrow\mathcal A^N$ | 해당 없음 (리본 ∩ (나) = ∅) | §5.2".
- §5.1 (나) := $\mathcal G^N\cap\{\partial=\varnothing\}$ 과 §5.2 명제 N 과 맞는다. 리본 행도 §5.2 item 4 (리본 ∩ (나) = ∅) 와 맞는다.
- §6.4 의 "명제 A0 (K_2 분해, 𝒢 에서만) | 예 (𝒢^N 에서는 차단)" 행과 §8.4 도 맞는다.
- **판정: 맞다.**

## 3. (3) |V(G)| ≤ 2 정리와 K_3 예

- **정리.** $|V(G)|\le2$ 이면 $|E(G)|\le1$. $\mathfrak B\in\mathcal G^N$ 이 $G$ 를 실현하면 (N2) 로 각 조각은 3 점 이상의 연결 그래프이므로 간선이 있다. 그 간선의 이미지는 루프가 아니므로 (G4) 와 $E(G)$ 의 크기로 $E(G)$ 의 유일한 간선이고, 따라서 $\varepsilon_K=E(G)$, (N3) 위반. $E(G)=\varnothing$ 이면 간선 이미지가 루프뿐이라 (G4) 위반. 두 경우 모두 모순 [증명]. 본문의 서술과 맞다.
- **K_3 예 (조각 두 개).** $P_1=a\text{–}b\text{–}c$, $P_2=a'\text{–}c'\text{–}x$, 흰 점 $w_a=\{a,a'\}$, $w_c=\{c,c'\}$, $w_b=\{b,x\}$. 이미지는 $ab,bc$ ($P_1$), $ac,cb$ ($P_2$) 이고 $K_3$ 이다 [증명]. (G1) 모든 흰 점이 두 포트. (G2) 각 검정 점이 한 흰 점에만. (G3) 경로는 평면. (G4) $a a'$, $c c'$, $bx$ 가 간선이 아니다. (N1) 2 조각, (N2) 3 점씩, (N3) $\varepsilon_{P_1}=\{ab,bc\}\subsetneq K_3$, $\varepsilon_{P_2}=\{ac,bc\}\subsetneq K_3$. 전부 성립 [증명].
- **판정: 맞다.**

## 4. 남은 미결 (본문에서 정의와 분리되어 있음)

- $|V(G)|\ge3$ 인 일반 $G$ 의 $\mathcal G^N$ 실현 존재 [추측] (§8.4, §9.2 7').
- (N) 아래 α 무관성 [추측] (§5.3).

둘 다 정의 본문과 구분되어 표시되었다 (미결 항목에만 있고, 정의 공리와 정리에는 쓰이지 않는다).

## 5. 결론

**승인.** A-rev 를 F-R11 최종본으로 확정하는 데 동의한다.

## 문주님께 요청

없음. 변경 가능 항목: D-1 (μ), D-2 (긴 호), D-6 (단면 ∅), D-10 (α), D-11 (비자명성 (N), 추천 (c)).

## 후속연구 지점

1. **(우선 1) 일반 $G$ ($|V|\ge3$) 의 $\mathcal G^N$ 실현 존재.** 이유: 모든 연결 $G$ 에 (N) 설명서가 있는지가 비자명성 조건의 공허성을 정한다. 시작: 간선마다 조각을 두되 조각을 최소 3 점으로 묶는 구성을 찾는다. 난점: 조각 최소 크기와 흰 점 포트 조건이 충돌할 수 있다.
2. **(우선 2) (N) 아래 α 무관성 (§5.3 미결).** 시작: K_2 구성을 3 점 조각 구성으로 바꾸어 실현 집합을 비교한다.
3. **(우선 3) 긴 호 판의 $b$, $\chi$ 엄밀화.** 시작: 길이 3 호 예에서 경계 순환과 $\chi$ 를 손으로 센다.
4. **(우선 4) 세 조각 접합 필요성.** 시작: 명제 B1 을 작은 조각 허용판으로 확장한다.
5. **(우선 5) Y 최소 예.** 시작: 3-연결 평면 $\mathfrak A$ 에서 파생 쌍이 한 면을 공유하지 않는 경우.
