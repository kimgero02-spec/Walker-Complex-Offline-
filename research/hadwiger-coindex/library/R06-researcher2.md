# [R06-researcher2] 반례꾼: $\tau=\operatorname{zig}$ 공격 대장 (C_9^3, Grötzsch, Clebsch 등의 방어와 frontier)

- 작성자·라운드·역할: researcher2 / 라운드 6 / 반례꾼 (포메이션 T). 코드: `rooms/researcher2/r06/` (`graphs.py`, `exactsep.py`, `homol.py`, `pi1.py`, `anneal.py`, `planar_cert.py`).
- 표기 기준: 계산 결과는 `[계산 확인]`, 기억에 의존한 표준 사실은 `[기억-미검증]`.
- 정의 확인: $\tau(G)=\operatorname{coind}(B_0(G))+1$ (빈 면 허용), $\operatorname{zig}(G)=\min_\sigma\max_{(A,B)}(\text{런 수})$ (극대 비공집합 완전이분쌍). 사용한 상계 도구: 아핀 배치 $y:V\to\mathbb R^d$ 에서 모든 완전이분쌍의 볼록껍질이 서로소이면 $\tau\le d+1$ (R03 인증서, 정확 유리수 LP 로 판정).

## 요약
1. **반례는 나오지 않았다.** 공격한 모든 그래프에서 $\tau=\operatorname{zig}$ 가 방어되었다. 방어 도구는 $\tau\ge\operatorname{conn}(N(G))+3$ (Lovász형 하한, [기억-미검증]) 과 $\omega$ 하한이다.
2. **$C_9^3$** (ω=4, χ=5, zig=5 [계산 확인]): $\mathbb R^3$ 배치 담금질 탐색은 실패(최선 위반 1쌍). 이웃 복합체 $N$ 은 $\tilde H_*(N;\mathbb F_p)$ 가 $p\le7$ 에서 $\tilde H_3$ 만 가지고 $\pi_1=1$ (Tietze 소거 성공) → $N$ 은 2-연결 → $\tau\ge5=\operatorname{zig}$. **방어.**
3. **Grötzsch** (ω=2, χ=4, zig=4 [계산 확인]): $\mathbb R^2$ 배치 담금질 탐색은 최선 1쌍 위반으로 고정됨(쌍 $\{6,8\}\times\{2,10\}$). $N$ 은 $\tilde H_2$ 만 가지고 $\pi_1=1$ → 1-연결 → $\tau\ge4=\operatorname{zig}$. **방어** (반례 후보 $d_R\le2$ 는 나오지 않음).
4. **Clebsch 그래프** (ω=2, χ=4): $N$ 의 $\mathbb F_2$ 호몰로지는 $\tilde H_2$ 만 (rank 31), $\pi_1=1$ → $\tau\ge4$, $\tau\le\operatorname{zig}\le\chi=4$ → $\tau=\operatorname{zig}=4$. **방어.** Mycielski $M(C_7)$ (zig=4 [계산 확인], $\tilde H_2$ 만, $\pi_1=1$) 도 같은 방식으로 **방어.**
5. **$C_5[K_3]$**: $\operatorname{zig}\le6$ (자연 순서, 런 수 6 확인), $\tau\le6$ (R^5 인증서 정확 검증: 10^1, 10^2, 10^3 배율 모두 위반 0), $\omega=6$ → $\tau=\operatorname{zig}=6$. **방어.**
6. **$C_n^2$ ($n=7..12$), $C_8^3$, $C_{11}^3$**: 등호 방어 또는 기존 결과와 일치 (zig 3,3,3,3,3,3; $C_8^3$: zig=ω=4; $C_{11}^3$: zig 5, 기존 τ=5).

## 공격 대장

| 대상 | 방법 | 결과 | 방어 이유 | 표기 |
|---|---|---|---|---|
| $C_9^3$ ($\chi=5$, $\omega=4$) | $\mathbb R^3$ 담금질 ($R=5$, 25000 스텝 × 여러 시드), 정확 분리 판정 | 반례 아님 (최선 위반 1) | $\tilde H_*(N;\mathbb F_p)=\tilde H_3$ ($p=2,3,5,7$), $\pi_1=1$ → 2-연결 → $\tau\ge5$ | [계산 확인] + [기억-미검증] (Lovász형 하한) |
| Grötzsch $M(C_5)$ ($\omega=2$, $\chi=4$, $\operatorname{zig}=4$) | $\mathbb R^2$ 담금질 ($R=3,6$; 6 시드 × 150k, 8 시드 × 12k) | 반례 아님 (최선 1 위반, 쌍 $\{6,8\}\times\{2,10\}$ 고정) | $\tilde H(N;\mathbb F_2)=\tilde H_2$, $\pi_1=1$ → 1-연결 → $\tau\ge4$ | [계산 확인] + [기억-미검증] |
| $M(C_7)$ (15 정점, $\operatorname{zig}=4$) | 순서 DFS (zig), $\tilde H(N)$, $\pi_1$ | 방어 | $\tilde H_2(N)$ 만, $\pi_1=1$ → $\tau\ge4=\operatorname{zig}$ | [계산 확인] + [기억-미검증] |
| Clebsch (16 정점, $\omega=2$, $\chi=4$) | $\tilde H(N)$, $\pi_1$ | 방어 | $\pi_1=1$, $\tilde H_2$ 만 → $\tau\ge4$; $\tau\le\operatorname{zig}\le\chi=4$ | [계산 확인] + [기억-미검증] |
| $C_5[K_3]$ ($\omega=6$) | 자연 순서 zig, R^5 인증서 | 방어 | $\tau\le6$ 와 $\omega=6$ 로 샌드위치 | [계산 확인] |
| $C_n^2$ ($n=7..12$), $C_8^3$, $C_{11}^3$ | zig DFS | 방어/일치 | $C_8^3$: $\operatorname{zig}=\omega=4$. $C_{11}^3$: 기존 $\tau=5$ 와 일치 | [계산 확인] |
| $d_R\le2\Rightarrow\operatorname{zig}\le3$ (researcher1 [추측]) | Grötzsch 에서 $d_R\le2$ 탐색 | 반례 없음 (실패는 $\tau=4$ 와 일관) | 반례가 되려면 $\tau\le3<\operatorname{zig}$ 인 그래프가 필요, 현재 없음 | [추측] 유지 |
| 연구원3 P3 ($\tau=1+\max\{k:\tilde H_k(X(G))\neq0\}$, 비이분) | Grötzsch ($X$ 최고 $\tilde H_3$ → 4), $C_9^3$ (→5), $C_5[K_2]$ (→4), $C_8^3$ (→4), $C_{11}^3$ (→5) | 전부 일치, 반례 없음 | 단, 상단 호몰로지는 $\operatorname{coind}$ 의 상계도 하계도 아니므로 증명 아님 | [추측] |
| 연구원3 P2/P4 ($C_6$) | $\tilde H(X(C_6))$ 계산 | $\tilde H_2\neq0$ 확인 (반증 재확인) | — | [계산 확인] |
| 번역 $X(G)\simeq\Sigma N(G)$, $\tau=\operatorname{coind}(N)+2$ | $K_1,K_2,C_5,C_6,C_5[K_2]$, Grötzsch 의 $\tilde H$ 대조 | 일치 (예: $C_5[K_2]$: $\tilde H_2(X)=\mathbb F_2$, $\tilde H_3(X)=\mathbb F_2^{10}$) | 표준 현수 공식 | [계산 확인] |
| 우월 정점 불변 (연구원3 O3) | 증명 읽기 | 반례 없음. 대응 $a\mapsto c$ 가 면을 면으로 보냄, $c\notin B$ 는 $a\not\sim c$ 에서 옴 | 올바름 | [증명] |
| 연구원1 보조정리 1 (런 $\ge4$ $\Leftrightarrow$ 교차 $K_{2,2}$) | 증명 읽기 | 올바름 | 교대 4점이 교차 $K_{2,2}$ 를 이룸 | [증명] |
| 연구원1 "$K_4$-마이너-자유 ⇒ $\tau=\operatorname{zig}=3$" | 2-트리 삽입 규칙 증명 확인, 부분그래프 단조성 | 방어 (부분그래프 ⊆ 2-트리 ⇒ zig 단조) | 단, "극대 $K_4$-마이너-자유 = 2-트리" 는 [기억-미검증] | [증명] (표준 사실 인용) |
| 호몰로지-이웃 복합체 연결 판 (연구원1 4.2): $\operatorname{conn}(N)\ge\operatorname{zig}-3$ ⇒ 등호 | $K_n$, $C_5$, $C_9^3$, Grötzsch 에서 조건 확인 | 충분조건으로 쓸 수 있음 (Lovász형). 반례 없음 | $\tau\ge\operatorname{conn}(N)+3$ 과 $\tau\le\operatorname{zig}$ | [기억-미검증] (부등식) + [계산 확인] |
| 방향 점검 (오케스트레이터 지시 (2)) | — | 주의: $\tau<\operatorname{zig}$ 반례는 $\tau$ 쪽은 **상계** (배치 또는 사상), $\operatorname{zig}$ 쪽은 **하계** (모든 순서 탐색 실패) 로 증명해야 한다. 지시문의 "$\tau$ 의 하한, zig 의 상한" 은 방향이 반대라서 쓸 수 없다 | — | [증명] |

## 본문 (핵심 계산)

### A. $\tau<\operatorname{zig}$ 반례 검사 절차
반례가 되려면 $\tau\le k<\operatorname{zig}$ 를 보여야 한다. (a) 상계: $y:V\to\mathbb R^{k-1}$ 에서 모든 극대 완전이분쌍의 볼록껍질이 서로소 (정확 판정: Fraction 단체법, `exactsep.py`, 2차원은 분리축 판정과 대조) [증명 도구]. (b) 하계: $\operatorname{zig}$ 를 모든 선형순서에 대한 최솟값으로 정확 계산 (`graphs.py` DFS, 독립 열거로 검증). 이 실험에서 (a) 는 어떤 후보에서도 성공하지 않았다.

### B. 호몰로지 판 (방어 도구)
- $N(G)$: 공통 이웃 복합체. $\tilde H_*(N;\mathbb F_2)$ 와 $\pi_1$ 을 계산 (`homol.py`, `pi1.py`). $\pi_1$ 은 스패닝트리 + 삼각형 관계 presentation 에 대해 Tietze 소거를 돌려 **모든 생성원이 사라지면** 자명군임을 보였다 (소거는 유효한 Tietze 변환이므로 성공 결과는 [증명]).
- $\tilde H$ 는 $p\in\{2,3,5,7\}$ 에서만 확인. 다른 소수의 꼬임은 배제하지 못했다 (Hurewicz 로 $\pi_2=H_2(\mathbb Z)$ 를 쓰는 $C_9^3$ 판정의 한계). [계산 확인, 제한 있음]
- $\operatorname{conn}(N)\ge\tau-3$ 를 쓴 등호 방어는 Lovász형 부등식 $\tau\ge\operatorname{conn}(N)+3$ 에 기댄다 (K_n, C_5 에서 등호, 표준). [기억-미검증]

### C. 미결 frontier
등호가 방어되지 않는 조건은 $\operatorname{zig}>\max(\omega,\operatorname{conn}(N)+3)$ 이다. 지금까지 검사한 그래프는 모두 이 조건을 피했다. 다음 후보: $\operatorname{zig}\ge5$, $\omega\le3$, $N$ 이 1-연결 이하인 그래프 (예: $C_{13}^3$, zig 계산 미완).

## 문주님께 요청
없음.

## 후속연구 지점
1. **frontier 족 탐색: $\omega\le3$ 이고 $\operatorname{conn}(N)\le\operatorname{zig}-4$.** 이유: 이것이 $\tau<\operatorname{zig}$ 가능한 유일한 방향. 시작: $C_{13}^3$, $C_{14}^3$ 의 zig 를 SAT 또는 가지치기로 계산 (현재 DFS 는 $T=4$ 기각에 400초 초과), 호몰로지 판 적용. 난점: zig 하계 계산 비용.
2. **$C_9^3$ 의 $\pi_2$ 직접 확인.** 이유: $\tau=5$ 방어가 $H_2(N;\mathbb Z)$ 의 소수 꼬임 (p≥11) 에 의존. 시작: 정수 호몰로지를 Smith 정규형으로 계산. 난점: 면 수 (소형이므로 쉬움).
3. **$\mathbb R^2$ 불가능성 증명 (Grötzsch).** 이유: $d_R(\mathrm{Grötzsch})\ge3$ 이 증명되면 "$d_R\le2\Rightarrow\operatorname{zig}\le3$" 과 결합해 $\tau$ 의 구조를 정리. 시작: 쌍 $\{6,8\}\times\{2,10\}$ 를 중심으로 한 위상 장애 (쌍 교차 수 홀짝) 를 찾기. 난점: 위상 논법 필요, 계산으로는 증명 불가.
4. **연결성 판의 문헌 확인.** 이유: $\tau\ge\operatorname{conn}(N)+3$ 은 본 보고서의 모든 방어가 기대는 부등식이다. 시작: Lovász 1978 / Matoušek 책의 해당 정리 번호 대조. 난점: 원문 접근 불가 시 [기억-미검증] 유지.
