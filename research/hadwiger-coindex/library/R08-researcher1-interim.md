# [R08-researcher1-interim] 중간: 정점 시트의 ι-버전과 τ 부분가법 ⟺ 조인 상계

- 작성자·라운드·역할: researcher1 / R08 / 연구원1 (정의 설계). 최종본: `R08-researcher1.md` (작성 예정). 검증 요청 대상: 연구원2.
- 표기: 모든 주장에 [증명] [계산 확인] [추측] [망상] [기억-미검증] 중 하나. 두 업로드 논문은 인용만.

## 검증을 부탁하는 주장 (연구원2 는 여기를 공격)
1. **[증명] 포함 보조정리.** 정점 분할 $V=\bigsqcup V_i$ 에 대해 $B_0(G)\subseteq B_0(G[V_1])*\cdots*B_0(G[V_k])$ ($\mathbb Z_2$-동변 부분복합체). 근거: 면 $(A,B)$ 의 제한 $(A\cap V_i,B\cap V_i)$ 는 $G[V_i]$ 의 쌍이다.
2. **[증명] ι 부분가법.** $\iota(G):=\operatorname{ind}(B_0G)+1$ 이라 하면 $\iota(G)\le\sum_i\iota(G[V_i])$. 근거: 각 $f_i:B_0(G[V_i])\to S^{n_i}$ 의 조인 $*f_i$ 를 1 에 제한. $*S^{n_i}=S^{\sum n_i+k-1}$.
3. **[증명] $\tau\le\iota\le\chi$.** $\operatorname{coind}\le\operatorname{ind}$ (Borsuk–Ulam). $\iota\le\chi$: 진색칠 $c$ 에 대해 $(v,1)\mapsto e_{c(v)}$, $(v,2)\mapsto -e_{c(v)}$ 는 $0\notin\operatorname{conv}$ 이므로 $\mathbb Z_2$-사상 $B_0\to S^{\chi-1}$. $\iota\le\operatorname{zig}$ 는 R04 모멘트 사상 (인용).
4. **[증명] 조인.** $B_0(G_1+G_2)=B_0(G_1)*B_0(G_2)$ 이므로 $\tau(G_1+G_2)\ge\tau_1+\tau_2$ (조인 of 구면 사상, $S^p*S^q=S^{p+q+1}$) 와 $\iota(G_1+G_2)\le\iota_1+\iota_2$.
5. **[증명] 동치.** τ 의 정점-분할 부분가법 $\forall V$: $\tau(G)\le\sum\tau(G[V_i])$ 는 조인 상계 $J$: $\tau(G_1+G_2)\le\tau_1+\tau_2$ 와 동치. (⇐: 교차 간선 추가는 $B_0$ 를 키우므로 단조.)
6. **[증명] 충분조건.** 모든 조각이 $\tau=\operatorname{zig}$ (또는 $\tau=\chi$) 이면 부분가법 성립 (zig 부분가법 + $\tau\le\operatorname{zig}$). 이 경우는 사실상 자명하다. 비자명 부분은 $\iota<\operatorname{zig}$ 인 조각.
7. **[계산 확인] 작은 값.** $\operatorname{zig}$ 상계 (무작위 탐색): $K_5$ 5, $K_6$ 6, $K_{3,3}$ 2, $C_5[K_2]$ 4 (τ=4 와 일치). $C_{10}(1,2)$ 와 $C_{10}(3,4,5)$ 는 zig 3. $C_5[K_2]$ 는 두 개의 유도 이분 조각으로 나뉘지 않음 (전수, 1024 색칠).
8. **[계산 확인] 간선 분할 반례.** $K_6=\text{oct}\cup PM_3$: $\tau=6>3+2$. 따라서 간선 분할 (A) 에서 τ 합 법칙 거짓.

## 연구원2 에게
- 1, 2 의 증명(특히 "ind 의 조인 부등식" 적용 부분)과 3 의 $0\notin\operatorname{conv}$ 논법을 검산해 달라.
- 5 의 동치와 $J$ 가 **열린 문제**임을 확인해 달라 (나는 $J$ 를 증명하지 못했다. $\operatorname{coind}$ 의 조인 상계가 일반 자유 $\mathbb Z_2$-복합체에서 성립하는지 불명).
- 반례 탐색 방향: $\tau(G_1+G_2)>\tau_1+\tau_2$ 가 되려면 $\iota_i>\tau_i$ 인 조각이 필요하다 ($\iota$ 와 $\tau$ 간극). 간극이 있는 그래프가 있는지.
