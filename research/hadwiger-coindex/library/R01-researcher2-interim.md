# [R01-researcher2-interim] 정의 오프셋 오류: $\tau=\operatorname{coind}(B_0)+2$ 는 틀렸고 $+1$ 이어야 한다

- 작성자: researcher2 (반례꾼) / 라운드 1 / 중간 보고

## 요약
- **[증명]** problem.md 의 $\tau=\operatorname{coind}(B_0)+2$ 는 $\chi\ge\tau$ 를 깨뜨린다. 반례: $G=K_1$. $B_0(K_1)$ 은 두 점 $S^0$, $\operatorname{coind}=0$, $\tau=2>\chi=1$. 일반적으로 $B_0(K_n)$ 은 $n$-교차다면체의 경계 $S^{n-1}$ (반대칭 작용), $\operatorname{coind}=n-1$ 이므로 $+2$ 면 $\tau(K_n)=n+1$.
- **올바른 정의**: $\tau(G):=\operatorname{coind}(B_0(G))+1$. [증명: $B_0(K_n)=S^{n-1}$ 에서 $\tau(K_n)=n$.] 같은 값이 $\operatorname{coind}(B(G))+2$ ($B_0\simeq\Sigma B$ 이므로) [기억-미검증].
- 따라서 S6 목록의 "$\operatorname{coind}(B)+1$, $\operatorname{ind}(B_0)+2$" 도 오프셋이 한 칸씩 어긋나 있을 가능성이 크다. 올바른 표준형은 $\chi\ge \operatorname{ind}(B_0)+1\ge\operatorname{coind}(B_0)+1$, $\chi\ge\operatorname{ind}(B)+2$ [기억-미검증].
- **[계산 확인]** $+1$ 정의에서 호몰로지 연결도 기반 하한 $\tau_h:=\min\{d:\tilde H_d(B_0;\mathbb F_2)\ne0\}+1$ 로 $K_1..K_5\to1..5$, $K_2\to2$, $C_5,C_7\to3$, $C_4,K_{3,3},P_3\to2$, 공집합 간선 그래프 $\to1$. 아틀라스(정점 $\le7$, 1252개) 전부 $\tau_h\le\chi$, $\tau_h\le$ Hadwiger 수. 코드: rooms/researcher2/b0.py (내 방, 열람 불가일 수 있으니 값만 신뢰).
