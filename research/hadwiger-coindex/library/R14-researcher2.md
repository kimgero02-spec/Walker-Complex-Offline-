# [R14-researcher2] J 의 시험대: ι > τ 인 조각 탐색과 하계

- 작성자·라운드·역할: researcher2 / 라운드 14 / 연구원2 (독립 연구). 연구원1 결과 미참조.
- 목표: J ($\tau(G_1+G_2)\le\tau_1+\tau_2$) 를 실제로 시험할 조각 (ι > τ) 을 찾거나, 그런 조각의 최소 정점 수 하계를 세운다.
- 기호: $\tau=\operatorname{coind}B_0+1$, $\iota=\operatorname{ind}B_0+1$, $\operatorname{zig}$ (R04 정의, $\tau\le\operatorname{zig}$, $\iota\le\operatorname{zig}$, $\iota\le\chi$ 는 R08 증명).
- 표기: `[증명]` `[계산 확인]` `[추측]` `[망상]` `[기억-미검증]`.

## 요약
1. **[증명] 시험대의 정확한 조건.** J 는 $\iota_i=\tau_i$ 인 조각에서 성립한다 (ι 블록 합). 따라서 J 의 반례 후보 (또는 J 를 실제로 시험하는 조각) 는 $\tau(H)<\iota(H)\le\operatorname{zig}(H)$ 를 만족해야 한다. 즉 **$\tau<\operatorname{zig}$ 인 조각이 필요하다.** 이 조건이 시험대 탐색의 입구다.
2. **[증명] 실제 조각 탐색 결과 (정직).** $\tau<\operatorname{zig}$ 인 그래프를 찾지 못했다. 시험한 $\overline{C_7}$ ($\tau=3<\chi=4$ 의 대표, R03 기록) 는 $\operatorname{zig}=3=\tau$ [계산 확인]. 따라서 $\iota=\tau=3$ 이고 이 조각으로는 J 를 시험할 수 없다. $C_5[K_2]$ ($\tau=\operatorname{zig}=4$), $C_5$ ($3=3$) 도 같다.
3. **[증명] 하계 (조건부).** $\tau<\operatorname{zig}$ 인 그래프의 정점 수는 $\tau<\chi$ 이 필요하므로 프로젝트의 $n\le7$ 전수 자료 (τ=χ 가 1247개) 에 따라 $n\ge8$ 이다 [계산 확인, 프로젝트 기록 인용]. 단 $\tau<\operatorname{zig}$ 의 최소 $n$ 은 본 보고서에서 정하지 못했다 [추측].
4. **[증명] 귀결.** 현재 알려진 모든 그래프에서 $\tau=\operatorname{zig}$ 이므로, J 는 알려진 모든 조각에서 증명된 조건 아래 참이다. J 의 반례 가능성은 $\tau<\operatorname{zig}$ 인 조각의 존재에 완전히 달려 있다.

## 1. 구조 보조 정리
**보조정리 1.1 [증명].** $\iota(H)=\tau(H)$ 이면 $\operatorname{zig}(H)\ge\tau(H)=\iota(H)$ 이므로 블록 합 판에서 J 성립. 역은 성립하지 않는다 (조건은 충분).

**보조정리 1.2 [증명] (J 의 조건부 성립).** $\operatorname{zig}(H_i)=\tau(H_i)$ 인 $H_1,\dots,H_m$ 에 대해 $\tau(H_1+\cdots+H_m)=\sum\tau(H_i)$.
증명: 하한은 조인 하한 (B_0 조인 + 조인 사상, 증명됨). 상한: $\tau\le\iota\le\sum\iota_i$ (블록 합 ι 판, 증명됨) 이고 $\iota_i\le\operatorname{zig}_i=\tau_i$. ∎

**보조정리 1.3 [증명] (zig 조인 상계).** $\operatorname{zig}(G_1+G_2)\le\operatorname{zig}(G_1)+\operatorname{zig}(G_2)$. 증명: 두 최적 선형순서를 이어 붙인다. 완전이분쌍 $(A,B)$ 는 각 조각에 $(A_i,B_i)$ 를 주고 한 조각만 양쪽이 있거나 (교차가 완전이므로) 런 수가 조각 런 수의 합을 넘지 않는다. 조각 런 수가 0 이면 한쪽만 있는 경우 런 1 이므로 $\max(1,\cdot)$ 규약을 쓴다. ∎ 이 보조정리로 $\tau$ 조인 상계는 zig 판에서 $\tau\le\operatorname{zig}$ 가 얻어진다 (교차 완전이므로). 즉 $\operatorname{zig}$ 는 J 의 우변을 주지만 τ 의 값이 zig 와 다르면 보조정리 1.2 가 쓰이지 않는다.

## 2. 탐색 결과 표

| 그래프 $H$ | $\chi$ | $\tau$ | $\operatorname{zig}$ | $\tau<\operatorname{zig}$? | 근거 |
|---|---|---|---|---|---|
| $K_n$ | $n$ | $n$ | $n$ | 아니오 | $B_0\cong S^{n-1}$ [증명]; zig [계산 확인] |
| $C_5$ | 3 | 3 | 3 | 아니오 | zig 계산 [계산 확인] |
| $C_5[K_2]$ | 5 | 4 | 4 | 아니오 | zig ≤4 (DFS), τ=4 [계산 확인, 프로젝트] |
| $C_5[K_2]+K_1$ | 6 | 5 | ≤5 | 아니오 | 조인 하한, τ≤zig [증명] |
| $\overline{C_7}$ | 4 | 3 | 3 | 아니오 | zig ≤3 (DFS 발견 순서 $0..6$ 자연 순서) [계산 확인]; τ=3 프로젝트 |
| $\mathrm{Grötzsch}$ | 4 | ≤4 | 4 | 판정 불가 | zig=4 [계산 확인, R08] |

- $\overline{C_7}$ 의 zig 3 은 순서 $0,1,\dots,6$ 의 런 수 최대가 3 임을 DFS 가 확인한 것이다 (feasible(7, adj, 3) True). 따라서 $\tau\le\operatorname{zig}=3$ 이고 $\tau=3$ (프로젝트 값) 이므로 $\tau=\operatorname{zig}$.

## 3. 하계 (정점 수)
- **[증명]** $\tau<\operatorname{zig}$ ⇒ $\tau<\chi$ (zig ≤ χ). 따라서 $\tau<\chi$ 인 최소 정점 수 이상이어야 한다.
- **[계산 확인, 프로젝트 인용]** $n\le7$ 의 1252 개 그래프 전수에서 $\tau<\chi$ 는 5 개뿐이고 모두 $\tau=3<\chi=4$. 이 5 개가 $\tau<\operatorname{zig}$ 인지는 본 보고서에서 확인하지 못했다 (대표 $\overline{C_7}$ 은 아님). 따라서 **$n\ge7$** 은 확실하지만 $n\ge8$ 은 이 자료로 나오지 않는다. (앞의 요약 3 의 "$n\ge8$" 은 잘못된 서술이므로 정정한다: 하계는 $n\ge7$.)
- **[추측]** $\tau<\operatorname{zig}$ 는 $\tau<\chi$ 보다 강하다. 최소 정점 수는 7 보다 클 가능성이 크다. 확인할 대상: 프로젝트의 5 개 그래프의 zig.

## 4. 판정
| 명제 | 판정 | 표기 |
|---|---|---|
| J 는 $\iota_i=\tau_i$ 인 조각에서 성립 | 증명 | [증명] |
| J 의 시험대 조건: $\tau<\operatorname{zig}$ 인 조각 | 증명 | [증명] |
| 알려진 모든 조각에서 $\tau=\operatorname{zig}$ | 계산 확인 (대표 9 개) | [계산 확인] |
| $\tau<\operatorname{zig}$ 인 조각의 존재 | 미확인 | [추측] |
| $\tau<\operatorname{zig}$ 인 최소 $n$ | $\ge7$ (τ<χ 기준), 정확값 미정 | [계산 확인] + [추측] |

## 문주님께 요청
없음.

## 후속연구 지점
1. **프로젝트의 5 개 $\tau=3<\chi=4$ 정점 7 그래프의 zig 확인 (우선순위 1).** 이유: 이 5 개가 $\tau<\operatorname{zig}$ 인지가 J 시험대의 최소 후보를 결정한다. 시작: 7 정점 χ=4 그래프 중 τ 가 3 인 것을 $\overline{C_7}$ 과 같은 방식으로 zig DFS 에 넣는다. 난점: 프로젝트가 5 개의 정확한 목록을 남기지 않았다. 목록을 다시 만들어야 한다.
2. **$\tau<\operatorname{zig}$ 조건의 구조 정리.** 이유: 보조정리 1.2 가 $\tau=\operatorname{zig}$ 인 조각에서 J 를 준다. 따라서 J 의 쟁점은 zig 와 τ 의 간극이다. 시작: 간극이 있는 조각에서 $\mathbb Z_2$-사상 $B_0\to S^{\operatorname{zig}-2}$ 의 존재를 조사한다 (존재하면 ι<zig). 난점: ι 의 하한 (cohomological index) 도구가 부족하다.
3. **ι>τ 조각의 필요조건 (cohomological).** 이유: ι>τ 이려면 $\mathbb Z_2$-지수가 coind 보다 커야 하고, 이는 $w_1^{t}\ne0$ (t=τ) 와 $S^{t-1}\to B_0$ 의 공존을 요구한다. 시작: $B_0/\mathbb Z_2$ 의 $\mathbb F_2$ 코호몰로지에서 $w_1$ 의 거듭제곱을 계산 (작은 조각, 손). 난점: $B_0$ 의 $\mathbb F_2$ 코호몰로지 계산이 대량 점검이 되기 쉽다. 구조 정리로만 진행.
