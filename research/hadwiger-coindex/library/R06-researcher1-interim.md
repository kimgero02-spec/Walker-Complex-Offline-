# [R06-researcher1-interim] 중간: $\operatorname{zig}\le3$ 의 $K_{2,2}$ 판정과 $K_4$-마이너-자유 류의 $\tau=\operatorname{zig}$

- 작성자·라운드·역할: researcher1 / 라운드 6 / 연구원. 최종본: `R06-researcher1.md`. 코드: `rooms/researcher1/r6_zig_sp.py`, `r6_sanity.py`, `r6_insert.py`.
- 표기: 모든 주장에 `[증명]` `[계산 확인]` `[추측]` `[망상]` `[기억-미검증]` 중 하나.

## 핵심 (중간)
1. **[증명] 판정 보조정리.** $\operatorname{zig}(G)\le3$ $\iff$ 정점의 선형순서가 있어 어떤 $K_{2,2}$ $\{p,p'\}\times\{q,q'\}$ 도 두 쌍이 교차(인터리브)하지 않는다. (런 수 $\ge4$ 인 완전이분쌍은 교대 4점을 품는다.)
2. **[증명] 2-트리 정리.** 2-트리 $T$ 마다 런 수 $\le3$ 인 선형순서가 있다. 증명: 변 $uv$ 의 공통 이웃 $N(u)\cap N(v)$ 가 $(u,v)$ 구간 안이나 밖에 모두 같은 쪽에 있으면 충분하고, 2-트리 귀납으로 새 정점 $v$ (변 $xy$ 에 부착) 를 $Z'=N(x)\cap N(y)$ 의 쪽에 맞춰 $x,y$ 바로 옆에 끼우면 된다.
3. **[증명] 결과.** 극대 $K_4$-마이너-자유 그래프가 2-트리라는 표준 사실 [기억-미검증] 을 쓰면, 모든 $K_4$-마이너-자유 $G$ 에서 $\operatorname{zig}(G)\le3$. 비이분이면 $\tau(G)\ge3$ (홀수 사이클) 이므로 $\tau=\operatorname{zig}=3$.
4. **[계산 확인] 구현 점검** (증명의 삽입 규칙을 그대로 구현, 무작위 2-트리 300개, $n\le12$): 최대 런 수 3, 불변식 위반 0. 이것은 증명의 구현 점검이며 근거가 아니다.
5. **[계산 확인] 예제 (정선 점검).** $C_5$: $\tau=\operatorname{zig}=3$. $\overline{C_7}$: $\tau=\operatorname{zig}=3$ ($\omega=3$). $C_5[K_2]$: $\tau=\operatorname{zig}=4$ ($\omega=4$). 계산기 점검: $\operatorname{zig}(K_4)=4$, $\operatorname{zig}(K_5)=5$, $\operatorname{zig}(W_5)=4$.
6. **열린 것.** $\tau\ge\operatorname{zig}$ 의 일반 방향은 여전히 열림. 장애물: 위상적 하한 (구면 사상) 과 조합적 순서 사이의 연결이 없다. 자세한 것은 최종본.

## 인계
- 최종본에서 $\tau\ge\operatorname{zig}$ 의 충분조건 (연결성 판) 과 $d=2$ 일반 판 ($d_R\le2\Rightarrow\operatorname{zig}\le3$) 을 정리한다.
