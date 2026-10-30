# [R01-researcher3-interim] 망상 목록 + C5[K2] 판정 시도: 선형 "Radon-free 임베딩" 인증서

- 작성자: researcher3 (망상꾼) / 라운드 1 / 중간 보고. 오프셋은 $\tau=\operatorname{coind}(B_0)+1$ 로 통일 (오케스트레이터 정정 반영; 내 코드는 처음부터 $K_n\to n$ 이 되도록 +1 로 검증).

## 핵심 도구: 그래프 Radon 정리와 인증서 $d_R(G)$ [증명 스케치 + 계산]
정의: $d_R(G)$ = 최소 $d$ 로서, $y:V\to\mathbb R^d$ 가 존재해 **G 의 모든 완전이분 부분그래프** $A\times B\subseteq E$ ($A,B\neq\emptyset$ 서로소) 에 대해 $\operatorname{conv}(y_A)\cap\operatorname{conv}(y_B)=\emptyset$.
- **[증명 스케치] 상한 인증서**: 이런 $y$ 가 있으면 $f(a^1)=(y_a,1),\ f(b^2)=-(y_b,1)$ 의 단체별 선형 확장이 $B_0(G)\to S^{d}$ 의 $\mathbb Z_2$-사상 (분리 초평면 $\Leftrightarrow$ 각 단체의 상이 열린 반공간에 놓임). 따라서 $\operatorname{coind}\le\operatorname{ind}\le d$, 즉 $\tau(G)\le d_R(G)+1$.
- **[증명 스케치, Borsuk–Ulam] 반대방향**: $\tau(G)\ge d+2$ 이면 모든 $y:V\to\mathbb R^d$ 는 Radon 쌍 (완전이분 $K(A,B)$ 위에서 볼록포가 교차) 을 가진다. $G=K_n$ 이면 정확히 Radon 정리. ("그래프 Radon 정리")
- 유용성: $\operatorname{coind}$ 는 계산 불가에 가깝지만 (호몰로지 하한 $\tau_h$ 는 부분그래프 단조가 아님 → 쓸모 제한), **하한 = 부분그래프 최대 $\tau_h$ (진짜 $\tau$ 는 단조), 상한 = $d_R+1$ (LP 마진 탐색)** 으로 $\tau$ 를 샌드위치할 수 있다.
- **[계산 확인]** 연결 7정점 무작위 40개 그래프에서 (하한 = 상한) 이 **40/40** 일치 → 거기서 $\tau$ 는 정확히 결정되고 전부 $\tau=\omega$ 또는 $\chi$ 와 일치(아래 참조). 코드: rooms/researcher3/{b0lib,radon,tight}.py

## 반례꾼 요청에 대한 직접 결과: Catlin형 $C_5[K_2]$ 의 $\tau$
- **[계산 확인]** $C_5[K_2]$ (10정점, $\chi=5,\ \omega=4$): $\mathbb R^3$ 에서 모든 50개 극대 완전이분쌍이 마진 $0.036>0$ 으로 분리되는 배치 발견 (rooms/researcher3/c5k2_d3.npy). 따라서 $\tau\le4$. $K_4\subseteq C_5[K_2]$ 와 단조성으로 $\tau\ge\omega=4$. **$\tau(C_5[K_2])=4<\chi=5$.**
  (부동소수 LP, 허용오차 $10^{-7}$; 반례꾼이 정확 유리수 검증으로 재확인 요청.)
- **[계산 확인]** $C_5[K_3]$ (15정점, $\chi=8,\omega=6$): $d=5$ 배치 발견 → $\tau\le6=\omega$, 즉 $\tau=6$. 
- 귀결: Catlin 계열은 $\tau=\omega$ 로 위상 하한에 **보이지 않는다** → **S4 의 시험대로 부적합** (τ=4 이므로 K_4 세분이 있으면 충분, 실제 있음). S4 반례 후보는 $\tau>\omega$ 이면서 Hajós 가 실패하는 그래프여야 함.
- $C_7[K_2]$ ($\chi=5$, $\omega=4$) 는 탐색 중 (결과는 최종 보고서).

## 아이디어 목록 (모두 [망상], 검증 방법 명시)
| # | 한 줄 주장 | 반증 방법 | 상태 |
|---|---|---|---|
| 1 | $\tau(G)\le d_R(G)+1$ 이고 소규모에서 등호 (인증서 정확성) | 무작위 그래프에서 하한(부분그래프 $\tau_h$ 최댓값) vs $d_R+1$ | 7정점 40/40 일치 [계산 확인] |
| 2 | Catlin형 $C_5[K_m]$ 은 $\tau=\omega=2m$ ($m\ge2$) | $d_R=2m-1$ 배치 탐색 | $m=2,3$ [계산 확인], $C_7[K_2]$ 진행 |
| 3 | $d_R(G)\le\mu(G)$ (Colin de Verdière 수) — 고유벡터 임베딩이 Radon-free | 평면 그래프는 $d_R\le3$, 외평면 $\le2$ 인지 탐색 | 진행 |
| 4 | $\tau(G/e)\ge\tau(G-e)$ [증명: $B_0(G-e)\to B_0(G/e)$ 가 단체사상, 루프 없음] | — | [증명] |
| 5 | $\tau(G)\le\tau(G-v)+1$ 은 $\operatorname{ind}$ 버전에서 성립: $u^1\mapsto +,u^2\mapsto-$ 로 $B_0(G)\to B_0(G-u)*S^0$ | coind 버전은 ind–coind 차이 때문에 불명 | [증명 스케치] |
| 6 | $\tau_h$ 는 간선 삭제로 2 이상 오르내림 (비단조) — 아틀라스에서 15+ 사례 | 이미 관찰 | [계산 확인]; 그러므로 $\tau_h$ 가 아닌 단조 하한을 써야 함 |
| 7 | S1-Radon: 모든 $K_t$-마이너-자유 그래프는 $\mathbb R^{t-2}$ 에 Radon-free 배치를 가짐 ($d_R\le t-2$) ⇒ S1 | 마이너-자유 그래프족(Wagner $V_8$, 평면+ 등)에서 $d_R$ 직접 탐색 | 미시험 |
| 8 | 산술적 상한: $\tau\le\chi_f$ 는 거짓 (Kneser $KG(9,2)$: $\tau=7>9/2$) | [기억-미검증] Lovász 공식 $\tau(KG(n,k))=n-2k+2$ | 비교용 |
| 9 | 순서 행렬체(oriented matroid) 완화: 회로 $(C^+,C^-)$ 중 $C^+\times C^-\subseteq E$ 인 것이 없는 acyclic OM 의 최소 rank 가 $\tau$ 를 샌드위치 | 균일 OM 로 $d_R$ 보다 작은 값이 나오는 그래프 탐색 | 미시험 |
| 10 | 이머전 연산(lift) 한 번에 $\tau$ 는 1 이하로만 떨어진다 (S5 귀납 가능성) | 아틀라스에서 lift 전후 $\tau$ (단조 하한/상한 샌드위치) 비교 | 미시험 |
| 11 | Grötzsch/Mycielskian: $\tau$ 가 $\omega$ 보다 크고 $d_R$ 로 정확히 결정 | $d_R$ 탐색 | 진행 |
| 12 | 확률적: 가우시안 $y\in\mathbb R^d$ 가 Radon-free 일 확률이 $d$ 에서 상전이 | $G=K_n,C_5,$ Petersen 에서 $d$ 별 몬테카를로 | 미시험 |

## 반례꾼에게 공격 요청
1. #1: $\tau=d_R+1$ 이 깨지는 그래프 (하한<상한 인 소규모 그래프) — 있다면 coind–ind 간극의 구체 예.
2. $C_5[K_2]$ 배치의 정확 유리수 검증, 및 #2 ($C_5[K_m]$ 에서 $\tau=\omega$) 반증.
3. #7: 마이너-자유인데 $d_R\ge t-1$ 인 그래프.
