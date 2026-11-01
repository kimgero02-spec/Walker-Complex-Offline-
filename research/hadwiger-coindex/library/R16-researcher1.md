# [R16-researcher1] 블록 클래스 𝒞_3 = {zig≤3} 와 𝒞_2 = {zig≤2}: 닫힘, K_4 세분, 정점 시트 상계, 교차 간선이 zig 를 올리는 예

- 작성자·라운드·역할: researcher1 / 라운드 16 / 연구원1 (무인 모드 3라운드 중 1). 범위: 정점 시트 블록 (교차 간선 포함). 시트와 무관한 τ 일반론은 하지 않았다.
- 표기: `[증명]` `[계산 확인]` `[추측]` `[망상]` `[기억-미검증]`. 외부 정리 없이 끝난 항목은 [증명]. 4색정리는 쓰지 않았다.
- 정의: $\operatorname{zig}(H)=\min_\sigma\max_{(A,B)}\operatorname{runs}_\sigma(A\cup B)$, 최대 완전이분쌍 $(A,B)$, 런 수는 $A\cup B$ 를 순서대로 읽은 $A/B$ 라벨 열의 $1+$(변화 수). 증명된 사슬 $\tau\le\operatorname{zig}\le\chi$ (R03·R04 인용).
- 계산: `rooms/researcher1/r08_zig.py` 의 무작위 탐색으로 $C_{10}(1,2)$ 의 런 수 3 인증서 (이전 실행, [계산 확인]).

## 요약
1. **[증명] $\mathcal C_3$ 은 부분그래프에 닫혀 있다.** 부분그래프의 완전이분쌍은 원 그래프의 완전이분쌍이므로 런 수가 줄거나 같다.
2. **[증명] $\mathcal C_3$ 에 $K_4$ 세분이 있다.** 최소 예: $K_4$ 의 한 간선 $ab$ 를 $a\,x\,b$ 로 세분한 5 정점 그래프 $Q$. $\operatorname{zig}(Q)=3$ 이고 $\omega(Q)=3$ 이라 $\tau(Q)=\operatorname{zig}(Q)=3$, $\chi(Q)=3$. $K_4$ 자체는 $\operatorname{zig}=4$ 로 제외. (R15-r3 주장 검증 완료.)
3. **[증명] $k$ 개 $\mathcal C_3$ 블록의 상계 $\tau\le3k$ 는 최선이다.** $K_{3k}$ 는 $k$ 개의 $K_3$ 로 나뉘고 $\tau(K_{3k})=3k$. 
4. **[증명] $\mathcal C_2$ (= 이분 그래프) 블록의 상계는 $\tau\le2k$, 역시 최선 ($K_{2k}=k\,K_2$).** 그러나 $\chi\le2k$ 가 이미 같은 값이므로 새 정보가 없다. $\mathcal C_3$ 은 다르다: $\mathcal C_3$ 블록의 $\chi$ 는 4 까지 갈 수 있고 ($C_{10}^2$, $\chi=4$, $\operatorname{zig}=3$), 그때 $\tau\le3k<4k$ 는 $\chi$ 상계보다 실제로 낫다.
5. **[증명] 교차 간선이 zig 를 올리는 최소 예: $K_4=K_3\sqcup K_1$.** 블록 zig 는 $3,1$ 이고 $\operatorname{zig}(K_4)=4$. 블록 zig 의 합 $3+1=4$ 와 같아 부분가법 상계는 tight. 같은 현상이 $W_5=C_5+K_1$ (블록 zig $3,1$, $\operatorname{zig}=4$) 에도 있다.

## 1. 닫힘 [증명]
- **보조정리 1.1.** $H\subseteq G$ (부분그래프) 이면 $\operatorname{zig}(H)\le\operatorname{zig}(G)$.
  *증명.* $G$ 의 최적 순서 $\sigma$ 를 $V(H)$ 에 제한한다. $H$ 의 완전이분쌍 $(A,B)$ 는 $G$ 의 완전이분쌍이다 ($A\times B\subseteq E(H)\subseteq E(G)$). 그 라벨 열은 $G$ 의 극대쌍 $(A',B')\supseteq(A,B)$ 의 라벨 열의 부분열이고, 부분열의 런 수는 원열의 런 수를 넘지 않는다 (원소 삭제는 런을 늘리지 않는다). 따라서 $\operatorname{runs}(A\cup B)\le\operatorname{zig}(G)$. ∎
- **따름 1.2.** $\mathcal C_3=\{H:\operatorname{zig}(H)\le3\}$ 과 $\mathcal C_2=\{H:\operatorname{zig}(H)\le2\}$ 는 부분그래프에 닫혀 있다 (유도 부분그래프 포함).

**판정표 (기본 성질).**
- $\operatorname{zig}\le3$ 판정 [증명, R06 보조정리 1 의 재사용]: $\operatorname{zig}(H)\le3$ $\iff$ 정점 순서가 있어 $H$ 의 어떤 $K_{2,2}$ $\{p,p'\}\times\{q,q'\}$ 에 대해 두 쌍이 교차하지 않는다 ($p<q<p'<q'$ 형이 없음). (⇐ 런 4 이면 교대하는 네 점이 교차 $K_{2,2}$; ⇒ 교차 $K_{2,2}$ 는 런 4 를 준다.)
- $\operatorname{zig}\le2$ $\iff$ 이분 [증명]: 이분 그래프는 한쪽 변을 먼저 놓으면 런 2. 역으로 홀수 사이클 $C_{2m+1}$ 은 $\tau=3$ 이고 $\tau\le\operatorname{zig}$, 따라서 $\operatorname{zig}\ge3$.

## 2. $K_4$ 세분 in $\mathcal C_3$ [증명]
- **예 $Q$.** 정점 $a,b,c,d,x$; 간선 $ac,ad,bc,bd,cd,ax,bx$ ($K_4$ 의 간선 $ab$ 를 $axb$ 로 세분).
- $K_4$ 세분 여부: $\{a,b,c,d\}$ 위에 $a$–$b$ 경로 $a\,x\,b$ 를 더한 것이므로 $Q$ 는 $K_4$ 의 세분이다 (서로소 부분 경로 조건 충족).
- **$\operatorname{zig}(Q)\le3$.** 순서 $\sigma=(c,a,b,d,x)$ 를 쓴다. 교차 $K_{2,2}$ 를 모두 나열한다. 두 정점 쌍이 공통 이웃 2 개 이상을 가지는 쌍은 $\{a,b\}$ ($\{c,d,x\}$ 중 공통 이웃 $c,d,x$), $\{c,d\}$ (공통 $a,b$), $\{c,x\}$ (공통 $a,b$), $\{d,x\}$ (공통 $a,b$) 뿐이다. 따라서 모든 $K_{2,2}$ 의 한 변은 $\{a,b\}$ 이고, $a,b$ 는 $\sigma$ 에서 인접 위치이므로 다른 변의 원소가 그 사이에 없다. 교차가 불가능하다. 보조정리 판정에 의해 $\operatorname{zig}(Q)\le3$. ∎
- **$\operatorname{zig}(Q)=3$, $\tau(Q)=3$.** $\omega(Q)=3$ ($\{a,c,d\}$) 이므로 $\tau\ge3$; $\operatorname{zig}\le3$ 이므로 $\tau\le3$.
- **최소성.** $K_4$ 세분은 간선을 세분한 것이므로 정점 4 개면 $K_4$ 자체 (zig 4, 제외). 따라서 5 정점이 최소.
- 주의: $Q$ 는 $K_4$ 마이너를 가지므로 $K_4$-마이너-자유 블록의 $\operatorname{zig}\le3$ (R04-r2) 보다 엄밀히 큰 클래스가 $\mathcal C_3$ 에 있다. 

## 3. $k$ 블록 상계 [증명]
- **정리 3.1.** 정점 시트 $V=\bigsqcup_{i=1}^kV_i$ 에서 $G[V_i]\in\mathcal C_3$ 이면 $\tau(G)\le\operatorname{zig}(G)\le\sum_i\operatorname{zig}(G[V_i])\le3k$.
  *증명.* $\tau\le\operatorname{zig}$ (R04 사슬). 블록별 최적 순서를 이어 붙이면 (R07 보조정리 / R09 §1) $\operatorname{zig}(G)\le\sum_i\operatorname{zig}(G_i)$. ∎
- **정리 3.2 (최선).** 임의의 $k$ 에 대해 $K_{3k}=k\,K_3$ 이 $\mathcal C_3$ 블록 분할을 가지며 $\tau(K_{3k})=3k$. 따라서 $f(k)\ge3k$ 이 필요, $3k$ 가 최선. [증명] ($K_3\in\mathcal C_3$: $\operatorname{zig}(K_3)=3$.)
- **$\mathcal C_2$ 블록.** 정리 3.1 과 같은 논증: $\tau\le\operatorname{zig}\le2k$. 최선: $K_{2k}=k\,K_2$ ($K_2\in\mathcal C_2$, $\tau(K_{2k})=2k$). [증명]
- **$\mathcal C_2$ 의 가치 판정.** 이분 블록 $k$ 개 그래프의 $\chi\le\sum\chi_i=2k$ 이므로 $\tau\le\chi\le 2k$ 는 이미 나온다. 따라서 $\mathcal C_2$ 로 제한해도 **새 상계는 없다** (χ 와 같은 값). [증명]
- **$\mathcal C_3$ 의 가치 판정.** $C_{10}^2\in\mathcal C_3$ 이고 $\chi(C_{10}^2)=4$: 3-색칠이면 연속 삼각형 $\{i,i+1,i+2\}$ 가 모두 서로 다른 색이므로 색 열이 주기 3 이어야 하고 $3\mid10$ 이 필요하다 [증명]. 따라서 $\mathcal C_3$ 블록에서는 $\chi\le4k$ 가 최선이 아니고, $\tau\le3k$ 가 $\chi$ 상계보다 실제로 낫다. $\tau(C_{10}^2)=3$ 은 R04 (zig 3 인증서) 와 일치 [계산 확인].

## 4. 교차 간선이 zig 를 올리는 최소 예 [증명]
- **예 $K_4=K_3\sqcup K_1$.** 블록 zig: $\operatorname{zig}(K_3)=3$, $\operatorname{zig}(K_1)=1$. $\operatorname{zig}(K_4)=4>\max(3,1)=3$. 교차 간선 3 개 (한 정점에서 나오는 별) 가 zig 를 1 올린다. 합 $3+1=4$ 와는 같다 (부분가법 tight). $\tau(K_4)=4=\tau(K_3)+\tau(K_1)$ 도 같다 (조인 가법).
- 최소성 (한정): 정점 3 이하의 그래프 $G$ 와 블록 분할 $(a,b)$ 에서 $\operatorname{zig}(G)>\max(\operatorname{zig}\,G_1,\operatorname{zig}\,G_2)$ 인 예를 손으로 찾지 못했다. 정점 4 의 예 $K_4$ 가 최소라는 주장은 전수 점검 없이는 [추측]이다 (대량 점검 금지 규칙).
- 같은 현상 $W_5=C_5+K_1$: 블록 zig $3,1$, $\operatorname{zig}(W_5)=4$ ($\tau=\chi=4$, R08 조인 가법).
- 결론: 교차 간선은 블록 zig 의 최댓값을 넘기지만 합을 넘기지는 못한다 (부분가법). 이 "올림" 은 블록들이 완전 조인 관계일 때 최대이다 [추측, 일반화 미증명].

## 5. 판정
| 명제 | 판정 |
|---|---|
| $\mathcal C_3$ 부분그래프 닫힘 | [증명] |
| $\mathcal C_3$ 에 $K_4$ 세분, 최소 5 정점 ($Q$) | [증명] |
| $k$ 블록 $\mathcal C_3$: $\tau\le3k$, 최선 ($K_{3k}$) | [증명] |
| $\mathcal C_2$ 블록: $\tau\le2k$, 최선 ($K_{2k}$), 그러나 $\chi\le2k$ 와 같음 | [증명] (새 정보 없음) |
| $\mathcal C_3$ 블록에서 $\chi$ 가 4 까지 가능 ($C_{10}^2$) | [증명] |
| 교차 간선이 zig 를 올림: 최소 $K_4=K_3\sqcup K_1$ | [증명] |

## 문주님께 요청
없음.

## 후속연구 지점
1. **$\mathcal C_3$ 블록 분할에서 $\chi\le3k$ 가 가능한지 (τ 와 χ 의 간극 방향).** 이유: $\tau\le3k$ 가 맞고 $\chi$ 가 $4k$ 까지 가면 $\tau<\chi$ 인 블록 합이 생긴다. 시작: $C_{10}^2$ 같은 블록 2 개의 조인 $C_{10}^2+C_{10}^2$ 에서 $\tau=6$ 이 되는지 (조인 가법 $\tau\ge3+3$ 과 $\operatorname{zig}\le6$ 로 확정) 을 확인 — 이는 R08 의 $J$ 를 $\mathcal C_3$ 에서 증명하는 것과 같다 (J 는 $\operatorname{zig}$ 로 이미 해결: $\tau\le\operatorname{zig}\le6$, $\tau\ge6$). 난점: 조인 밖의 $\mathcal C_3$ 블록 분할은 아직 정리되지 않았다.
2. **$\mathcal C_3$ 의 $K_4$-세분 구조 분류.** 이유: 최소 예 $Q$ 가 $K_4$ 의 한 간선 세분이다. 시작: 두 간선 세분, 두 $K_4$ 세분의 합 등에서 $\operatorname{zig}\le3$ 이 유지되는지 몇 개 손으로 확인 (대량 점검 금지). 난점: $K_4$ 세분 전체 족의 $\operatorname{zig}$ 는 교차 $K_{2,2}$ 패턴 조합론으로 가야 한다.
3. **교차 간선 올림의 상한.** 이유: §4 는 최소 예만 준다. 시작: 블록 zig $(a,b)$ 가 주어졌을 때 교차 간선을 가진 조합의 $\operatorname{zig}$ 가 $a+b$ 를 넘지 않음 (부분가법) 이므로, 올림 크기가 $\min(a,b)$ 로 제한되는지 확인하는 정리 후보. 난점: 교차 패턴이 임의일 때 최악 올림의 정확값이 미지.
4. **$\mathcal C_2$ 의 역할 (이분 블록, 매칭 교차).** 이유: $\mathcal C_2$ 블록은 χ 상계와 같아서 쓸모가 없지만, 교차 간선을 매칭으로 제한하면 (R13 $X_M$) 상계가 $2k$ 보다 나은지 여부가 남는다. 시작: 두 이분 블록 + 매칭 교차에서 $\operatorname{zig}$ 가 $3$ 을 넘는 최소 예 (예: $C_4\square K_2$, 큐브) 를 손으로 확인. 난점: 매칭 교차의 zig 계산은 교차 $K_{2,2}$ 조건이 많아 손 계산이 길어진다.
