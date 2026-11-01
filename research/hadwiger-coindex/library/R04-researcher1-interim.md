# [R04-researcher1-interim] 블로업 $G[K_m]$: 타입 분류 · 붕괴 정리 · $P[K_m]$ 결론 (중간)

- 작성자·라운드·역할: researcher1 / 라운드 4 / 연구원 (지점 3). 코드: rooms/researcher1/r4_blowup.py, r4_run1~7.py.
- 도서관 반영: 작성 시점에 `R04-researcher2*`, `R04-researcher3*` 가 없었다. 반영할 공격·아이디어 없음.

## 핵심 (중간 결과)
1. **정리 1 (극대쌍 = 블롭 타입)** [증명]: 임의 $G$ 에서 $G[K_m]$ 의 극대 완전이분쌍은 블롭 타입 $(X,Y,Z)$ (완전 $A$블롭·완전 $B$블롭·분할 블롭, $Z$ 는 클리크, 세 집합이 서로 완전결합) 와 $Z$ 블롭의 진부분집합 분할로 정해진다.
2. **정리 2 (인증서)** [증명]: 블롭 순서 $\sigma$ + 모멘트 곡선이면 라벨 변화 수 $\le (m-1)|Z| + c_\sigma(X,Y,Z)$, 여기서 $c_\sigma$ = 제한된 블롭열에서 XX·YY 가 아닌 인접쌍 수. 이것이 $\le d=m\omega-1$ 이면 $\tau(G[K_m])=m\omega(G)$. ($\tau\ge\omega$ 하한과 일치.)
3. **정리 3 (붕괴)** [증명]: $\psi:=\min(x+y,\ z+1+2\min(x,y))\le m(\omega-z)$ 가 모든 타입에서 성립하면 $\tau(G[K_m])=m\omega(G)$. 따름: $m\ge n-\omega+1$, 또는 $m\ge\operatorname{zig}(G)+\omega-1$ 이면 항상 붕괴. 삼각형 없는 $G$ 에서 $m\ge2$ 이고 $K_{m,m+1}\not\subseteq G$ 이면 $\tau(G[K_m])=2m$.
4. **$P[K_m]$ (Petersen)** [증명]: $\tau(P[K_m])=2m=\omega$ ($m\ge2$). $\tau(P)=3>2$ 는 $m=1$ 에서만. 따라서 Petersen 블로업은 $\tau>\omega$ 시험대가 아니다. $\chi(P[K_m])\ge\lceil5m/2\rceil$ 이므로 간극 $\ge\lceil m/2\rceil$.
5. 부수: $C_n^2$ ($n\ge9$) $\tau(C_n^2[K_m])=3m$ 모든 $m\ge1$ [증명]; $C_4$-자유 $\Rightarrow\tau\le3$, $K_{2,3}$-자유 $\Rightarrow\tau\le4$ [증명]; Grötzsch·Clebsch 의 블로업도 $m\ge2$ 에서 $2m$.
(상세와 증명은 최종 보고서 `R04-researcher1.md`.)
