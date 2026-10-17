# [R06-researcher3-interim] 이산 호지 이론으로 본 $\tau=\operatorname{zig}$: 번역 · 후보 도구 · 예측 목록 (중간)

- 작성자·라운드·역할: researcher3 / 라운드 6 / 망상꾼 (분야: 이산 호지 이론). 코드: `rooms/researcher3/r06_*.py`.
- 목적: 반례꾼2 가 이 목록을 공격할 수 있게 먼저 올린다. 시험 결과는 최종 보고서 `R06-researcher3.md` 에 있다.
- 표기: 모든 주장에 `[증명]` `[계산 확인]` `[추측]` `[망상]` `[기억-미검증]` 중 하나.

## 0. 핵심 관찰 (반례꾼 공격 우선 대상)
- **O1 [증명]** 박스 복합체 (빈 면 허용 버전) $X(G)=B_0^{\emptyset}(G)$ 의 면 $(A,B)$ 는 $A\subseteq V_1$, $B\subseteq V_2$, $A\times B\subseteq E$. 두 복사본 내부의 모든 쌍은 항상 간선이므로 $X(G)$ 는 1-골격 $H(G)$ 의 클리크 복합체 (flag) 다. 여기서 $H(G)^c$ 는 $V_1\cup V_2$ 위의 이분 그래프 $a_1\sim b_2 \iff (a=b$ 또는 $ab\notin E)$ 이다. 따라서 $X(G)=\operatorname{Ind}(H^c)$.
- **O2 [기억-미검증 (일반 보조정리), 계산 확인 (8개 그래프)]** 이분 그래프의 독립 복합체 $\operatorname{Ind}$ 는 이웃 복합체의 현탁과 호몰로지 동치: $X(G)\simeq\Sigma N(G)$, 여기서 $N(G)=\{\sigma\subseteq V:\ \sigma\text{ 는 공통 이웃을 가짐}\}$ (Lovász 의 이웃 복합체). 8개 그래프 ($K_1,\dots,K_4,P_3,C_5,C_6,C_5+$pendant) 에서 $\tilde H_k(X)\cong\tilde H_{k-1}(N)$ 확인. 따라서 $\tau(G)=\operatorname{coind}(N(G))+2$.
- **O3 [증명]** 우월 정점 (dominated vertex, $N(a)\subseteq N(c)$, $a\ne c$) 제거에서 $\operatorname{zig}$ 와 $\tau$ 는 둘 다 불변: 사상 $\varphi:X(G)\to X(G-a)$, $a_i\mapsto c_i$ 가 $\mathbb Z_2$-동변 단체 사상이고 포함 $\iota$ 와 $\varphi\iota=\mathrm{id}$. 따라서 $\operatorname{coind}$ 가 같다. $\operatorname{zig}$ 는 삽입 논증 (a 를 c 옆에 놓기) 으로 불변. **반례꾼 공격 요청: 이 $\varphi$ 의 동변성·단체성 (특히 $a\in A$ 와 $c\in B$ 가 동시에 생기는 경우) 을 깨 보라.**
- **O4 [계산 확인, 반증된 순진한 번역]** 호몰로지 차원으로 $\operatorname{zig}$ 를 읽는 번역은 깨진다: $C_6$ 에서 $\operatorname{zig}=2$ 인데 $\tilde H_2(X(C_6))\cong\mathbb Z^2\ne0$. 따라서 $\operatorname{zig}-1$ 차원 CW 모델을 찾는 이산 모스 접근은 $C_6$ 에서 불가능 (증명: 차원 $\le1$ 인 CW 복합체는 $\tilde H_2=0$).

## 1. 번역 사전 (초안)
| 문제 쪽 | 이산 호지 쪽 | 어긋나는 점 |
|---|---|---|
| 박스 복합체 $B_0(G)$ (빈 면 허용) | $\operatorname{Ind}(H^c)$, 클리크 복합체 $\mathrm{Cl}(H)$ | 표준 $B_0$ (비공집합) 과 $\Sigma$ 만큼 어긋남 |
| 면 $(A,B)$ 의 차원 $|A|+|B|-1$ | 단체 차원, 사슬 $C_k$ | 없음 |
| 대칭 $x_1\leftrightarrow x_2$ | 이분 그래프 $H^c$ 의 자기동형, 부호 있는 순열 | 자유 작용 (면이 자기 자신으로 가지 않음) |
| $\operatorname{coind}$ (Z_2-지표) | 조화 코사이클의 부호 분해 $\ker L_k^{\pm}$ | 실수 계수 부호 분해는 $\operatorname{coind}$ 를 못 줌 (아래 T3). $\mathbb F_2$ 에는 직교 분해 없음 |
| 런 수 $r(X,Y;\sigma)$ | 0/1 라벨의 전변동 $\|\delta f\|_1+1$ (경로 위) | $L^1$ 량이지 $L^2$ 가 아님 |
| $\operatorname{zig}=\min_\sigma\max r$ | 경로 위 부호 변화 수 (Sturm 류) | 호몰로지 차원과는 무관 (O4) |
| 라플라시안 $L_k$, 조화류 $\cong \tilde H^k$ | 호지 분해 | 조화 차원은 호몰로지 차원일 뿐, 쌍대 지표가 아님 |
| 이산 모스 임계 셀 | 독립 복합체의 매칭 트리 (Bousquet-Mélou–Linusson–Nevo) | 임계 차원 $\ge$ 최고 호몰로지 차원 (O4 때문에 $\operatorname{zig}$ 상계는 불가) |

## 2. 가져온 도구 (이 팀이 쓰지 않은 것 표시 ★)
1. ★ 독립 복합체와 이웃 복합체의 현탁 (Barmak / Nagel–Reiner 류) [기억-미검증]. 대응: O1–O2.
2. ★ 동변 우월 정점 사상 (Engström 의 fold 보조정리의 동변 판) [증명, 자체 증명]. 대응: O3.
3. ★ 실수 이산 호지 분해와 대칭 부호 분해 (조화 코사이클의 $\pm$ 분해) [계산 확인]. 대응: T3 (패리티 현상).
4. ★ 조화 차원 상계와 CW 모델 차원 (호몰로지의 최고 차원은 셀 차원의 하한) [증명]. 대응: O4.
5. 이산 모스 매칭 트리 (독립 복합체) [기억-미검증]. 대응: 셀 상계 시도 (반증됨, O4).
6. 경로 위 부호 변화의 Sturm 진동 정리 (Jacobi 행렬 고유벡터의 부호 변화 = 고유값 번호) [기억-미검증]. 대응: 런 수 = 부호 변화 수 (아직 연결 못 함, [망상]).

## 3. 반증 가능한 예측 (10개 이상, 시험 방법 포함)
| # | 한 줄 주장 | 분야의 이유 | 검증 (작은 예) | 기대 |
|---|---|---|---|---|
| P1 | 우월 정점 $a$ 에 대해 $\operatorname{zig}(G)=\operatorname{zig}(G-a)$ | O3 | $C_5$+pendant, $P_4$, $K_{1,3}$+간선, $C_7$+pendant | 성립 |
| P2 | $\operatorname{zig}(G)\ge 1+\max\{k:\tilde H_k(X(G))\ne0\}$ | 호몰로지 상계 | $C_6$ | **거짓** ($\operatorname{zig}=2$, $\tilde H_2\ne0$) |
| P3 | 비이분 $G$ 에서 $\tau(G)=1+\max\{k:\tilde H_k(X(G))\ne0\}$ | 구의 호몰로지 패턴 | $K_3,K_4,K_5,C_5,C_7,\overline{C_7},C_5[K_2]$ (top 3), $W_5$ (top 3 $\Rightarrow\tau=4$) | 성립 예상, 전부 일치 |
| P4 | 이분 $G$ 에서는 P3 가 깨진다 (추가 $\tilde H$ 성분) | $N(G)$ 가 두 성분으로 갈라짐 | $C_6$ ($\tau=2$, top $=2$) | **$C_6$ 에서 깨짐** |
| P5 | 실수 부호 분해에서 $X(K_n)$ 의 반대칭 조화 최고차원 류는 $n$ 이 홀수일 때만 | 실사영공간의 부호 패턴 | $K_2,\dots,K_6$, $K_7$ | $K_2..K_6$ 확인, $K_7$ 은 예측 (반대칭) |
| P6 | 실수 부호 분해 지표 $r^-(G)=\max\{k:\ker L_k^-\ne0\}$ 는 $\tau-1$ 과 같다 | 구의 상계 | $K_4$ ($\tau-1=3$ 인데 $r^-$ 은 $k=3$ 에서 $\ker L^-=0$) | **거짓** (반증됨) |
| P7 | $X(C_6)$ 의 $\mathbb Z_2$-CW 모델 차원은 $\ge2$ | $\tilde H_2\ne0$ | 호몰로지 계산 | 성립 (증명) |
| P8 | $\overline{C_7}$: $\operatorname{zig}=3$, 최고 $\tilde H$ 차원 $=2$ | P3 | 계산 | 확인 |
| P9 | 최소 반례 $G$ (τ≠zig) 는 우월 정점이 없다 | O3 | 논리 | 증명 (O3 에서 따름) |
| P10 | $\operatorname{zig}(\text{Petersen})=3$ | 상계 탐색 | 국소 탐색 | 상계 3 확인 (하계는 미확인) |
| P11 | $C_5[K_3]$ 의 최고 $\tilde H$ 차원 $=5$ (P3 로 $\tau=6$) | P3 의 $C_5[K_m]$ 예측 | $n=15$ 계산 필요 | 미시험 [추측] |
| P12 | 독립 복합체의 매칭 트리에서 $\operatorname{zig}$ 상계 (임계 차원 $\le\operatorname{zig}-1$) | 모스 이론 | $C_6$ | **거짓** (P2 에서 따름) |

## 4. 시험 계획 (무엇을 먼저)
- 시험 1 (P1, P2, P3, P5): 위 계산 스크립트 (`r06_t1.py`, `r06_t2.py`, `r06_t3.py`, `r06_hodge.py`).
- 시험 2 (P7, P10): 증명 및 국소 탐색.
- 시험 3 (P11): 차원 15 계산은 희소 행렬 랭크가 필요 (미실행).

## 5. 반례꾼에게 부탁
1. O3 의 $\varphi$ 가 단체 사상인지, 동변인지 공격 (특히 $a\in A$ 이고 $c\in A$ 인 면).
2. P3 를 $K_t$ 개수나 $\overline{C_7}$ 에서 깨는 비이분 그래프 찾기 (호몰로지 쪽 반례 = $\tau$ 쪽 반례가 아님을 주의).
3. O2 의 현탁 보조정리 원문 확인 요청 (오케스트레이터에게 문헌 확인 요청 가능).
