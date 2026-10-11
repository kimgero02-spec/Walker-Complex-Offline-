# 연구 과제 (대수검존): Hadwiger 추측의 coindex 변형

## 배경 (출처 확인 수준을 구분해서 적는다)

**확인된 것 (웹 검색의 초록·요약 수준, 논문 원문은 읽지 못함)**
- Raphael Steiner, "Hadwiger's conjecture and topological bounds", European J. Combin. (2024.12), arXiv:2312.17130 (2023.12 게시).
- 위상적 색칠수 하한의 계층(Matoušek–Ziegler, Daneshpajouh–Meunier)이 Hadwiger 추측 또는 홀수 마이너 변형(Odd Hadwiger)의 반례를 줄 수 있는지 묻는다.
- 결과: (i) 위상적 하한이 $t$ 인 그래프는 $K_{\lfloor t/2\rfloor+1}$ 을 **홀수 마이너**로 가진다 (Simonyi–Zsbán 문제 해결). (ii) Dol'nikov–Kříž 하한이 $\ge t$ 이면 $K_t$ 마이너를 가진다. (iii) Odd Hadwiger 는 Kneser·Schrijver 그래프에서 성립한다.

**확인하지 못한 것**
- 논문이 coindex 형태의 명제를 직접 다루는지, 어떤 하한이 (i)의 "위상적 하한"에 해당하는지는 모른다. 원문 열람이 막혀 있다.
- 따라서 **논문 내용을 읽은 것처럼 쓰지 말 것.** 기억에 의존한 사실은 `[기억-미검증]` 으로 표시한다.

## 문제

Hadwiger 추측: $\chi(G)\ge t \Rightarrow G$ 가 $K_t$ 를 마이너로 가진다.
색칠수 $\chi(G)$ 대신 **coindex 기반 위상적 하한**을 쓴 명제의 참/거짓을 연구하라.

**작업 정의 (검증 필요)**: $B_0(G)$ 를 박스 복합체(두 복사본 $V\times\{1,2\}$ 위에서, 완전 이분 부분그래프 $A\times B\subseteq E$ 에 대응하는 단체들, $A$ 또는 $B$ 는 공집합 가능, $\mathbb Z_2$ 작용은 두 복사본 교환)라 하고
$$\tau(G):=\operatorname{coind}(B_0(G))+1 .$$
알려진 부등식 $\chi(G)\ge\tau(G)$ 가 성립한다고 기억한다. 점검: $\tau(K_n)=n$, $\tau(C_{2k+1})=3$, $\tau(K_2)=2$ 가 되는지 직접 확인하라 (안 되면 정의를 고치고 보고하라).

> **정정 (오케스트레이터)**: 처음에는 오프셋을 $+2$ 로 적었으나 틀렸다. researcher2(반례꾼)가 $K_1$ ($\tau=2>\chi=1$) 반례로 지적했고, 오케스트레이터가 $B_0(K_n)\cong S^{n-1}$ 을 직접 계산해 확인했다. 올바른 값은 $+1$ 이다. 아래 S6 의 다른 변형들의 오프셋도 같은 식으로 어긋났을 수 있으니 각자 검증할 것.

**검토할 명제들**
- **S1 (coindex-Hadwiger)**: $\tau(G)\ge t\Rightarrow K_t$ 마이너.
- **S2 (홀수 마이너)**: $\tau(G)\ge t\Rightarrow$ 홀수 $K_t$ 마이너.
- **S3 (Steiner 손실)**: $\tau(G)\ge t\Rightarrow$ 홀수 $K_{\lfloor t/2\rfloor+1}$ 마이너. (위상적 하한에 대해 알려진 결과로 기억. $\tau$ 에도 적용되는지 확인.)
- **S4 (Hajós형)**: $\tau(G)\ge t\Rightarrow K_t$ 의 세분(topological minor). 색칠수 버전은 $t\ge7$ 에서 거짓(Catlin 반례) — $\tau$ 버전은?
- **S5 (이머전)**: $\tau(G)\ge t\Rightarrow K_t$ 이머전. (색칠수 버전은 Abu-Khzam–Langston 추측.)
- **S6 (변형 비교)**: $\tau$ 를 $\operatorname{coind}(B)+1$, $\operatorname{ind}(B_0)+2$, $\operatorname{ind}(B)+1$, $\operatorname{conn}(B_0)+3$, $\operatorname{Hom}(K_2,G)$ 기반 하한, Dol'nikov–Kříž 하한으로 바꾼 명제들의 강도 비교 (어느 것이 어느 것을 함의하는가).

**구조적 관찰 (출발점)**: $\tau\le\chi$ 이므로 Hadwiger 추측이 참이면 S1 은 참이다. 따라서 S1 의 반례는 Hadwiger 추측의 반례다. S2·S4·S5 는 결론이 더 강해서 독립적으로 거짓일 수 있다. 각 명제를 **참(증명) / 거짓(명시적 반례) / 함의 관계 / 열림** 중 하나로 판정하고, 불가능하면 어디서 막히는지(장애물)를 밝혀라.

## 팀 구성: 포메이션 A
| 연구원 | 역할 |
|---|---|
| researcher1 | **연구원**: 예제 계산 → 공통 패턴·장애물 추출 → 이론 구조화 |
| researcher2 | **반례꾼**: 도서관과 알려진 주장을 공격적으로 반증 시도 |
| researcher3 | **망상꾼**: 틀에 매이지 않는 아이디어 창출 (검증 가능한 형태로) |

## 표기 규칙
`[증명]` `[계산 확인]` `[추측]` `[망상]` `[기억-미검증]` 중 하나를 모든 주장에 붙인다.
