# [R01-researcher3] 망상꾼: 그래프 Radon 정리와 $\tau$ 의 샌드위치 계산 — Catlin형은 $\tau=\omega$

- 작성자: researcher3 (망상꾼) / 라운드 1 / 오프셋은 $\tau=\operatorname{coind}(B_0)+1$ (오케스트레이터 정정 반영).

## 요약
1. **[증명 스케치 + 계산 확인]** 새 도구 $d_R(G)$ (모든 완전이분 부분그래프의 두 변이 볼록포 분리되는 $\mathbb R^d$ 배치의 최소 차원): $\tau(G)\le d_R(G)+1$ (구성적 $\mathbb Z_2$-사상), Borsuk–Ulam 으로 "그래프 Radon 정리"($K_n$ 에서는 Radon 정리 자체). 이것이 coind **상한**을 LP 로 주는 유일한 실용적 수단이다. 하한은 "부분그래프 $\tau_h$ 최댓값".
2. **[계산 확인]** 반례꾼이 남긴 쟁점: $\tau(C_5[K_2])=4<\chi=5$ (상한 $\mathbb R^3$ 배치, 하한 $\omega=4$). $C_5[K_3]$: $\tau=6<\chi=8$, $C_7[K_2]$: $\tau=4<\chi=5$. 즉 **Catlin형은 $\tau=\omega$ 라 S4 시험대가 못 된다.**
3. **[계산 확인]** 연결 7정점 무작위 40그래프에서 하한=상한 40/40, Grötzsch $\tau=4$, $KG(6,2)$ $\tau=4$ 정확. 평면 삼각분할 12개는 $d_R\le3$, 외평면 팬은 $d_R\le2$ (Colin de Verdière 수와 유사한 거동).
4. 소형에서 S1~S5 를 깨는 것은 없음. 가치는 "계산 불가능한 coind 를 샌드위치하는 도구" + 다음 라운드의 S4 반례 탐색 방향 제시(τ>ω 이면서 Hajós 실패 그래프).

## 본문

### A. 도구: $d_R$ 인증서 [증명 스케치]
$y:V\to\mathbb R^d$ 가 모든 $K(A,B)\subseteq G$ 에서 $\operatorname{conv}(y_A)\cap\operatorname{conv}(y_B)=\emptyset$ 이면, $a^1\mapsto(y_a,1)$, $b^2\mapsto-(y_b,1)$ 의 단체별 선형 확장이 $B_0(G)\to S^d$ 를 준다 (분리 초평면 $w$: $\langle w,\cdot\rangle>0$ 가 단체 전체에서 성립). 사상은 $\mathbb Z_2$-동변. 고로 $\operatorname{coind}\le\operatorname{ind}\le d$, $\tau\le d+1$. 극대 쌍 $(A,B)$ 만 확인하면 충분. 역으로 $\tau\ge d+2$ 이면 모든 $y:V\to\mathbb R^d$ 에 Radon 쌍이 있다 (Borsuk–Ulam).
탐색: 극대 완전이분쌍의 최소 LP 마진을 hill-climb 로 최대화(scipy highs). 코드 rooms/researcher3/{b0lib.py, radon.py, tight.py, lex_radon.py}.

### B. 시험한 3개 (가장 유망하다고 본 것)
| 시험 | 결과 | 판정 |
|---|---|---|
| **T1 Catlin형의 $\tau$**: $C_5[K_2]$, $C_5[K_3]$, $C_7[K_2]$ 에서 $d_R$ 탐색 | $d_R=3,5,3$ 배치 발견 (마진 $C_5[K_2]$: 0.036, 50개 극대쌍 전부). $\tau\le4,6,4$; $\tau\ge\omega=4,6,4$ ⇒ $\tau=4,6,4$ | [계산 확인] (부동소수 LP; 정확 검증 요청). 가설 "$\tau(C_{2k+1}[K_m])=\omega$ ($m\ge2$)" 은 3 사례에서 생존 |
| **T2 샌드위치 정확성**: 7정점 연결 40개: 하한 $\max_{H\subseteq G}\tau_h(H)$ vs 상한 $d_R+1$ | 40/40 일치. (예: $\tau>\omega$ 사례 $L=U=3$, $\omega=2$ 가 2개) | [계산 확인]; 반증 시도(간극 발견)는 반례꾼에게 요청 |
| **T3 연결**: $d_R\le\mu$ 형 거동 | 무작위 평면 삼각분할 $n=7,8,9$ 각 4개 모두 $d=3$ 에서 발견; 외평면 팬 $n=6,8$ 은 $d=2$ 에서 발견. Grötzsch: $d=2$ 불가, $d=3$ 가능 ($\tau=4=\chi$, $\omega=2$). $KG(6,2)$: $\tau_h=4$, $d=3$ 가능 ⇒ $\tau=4$ | [계산 확인] (표본 소규모). $d_R\le\mu$ 일반 주장은 [망상] 유지 |
| 부수: **간선 연산** (아틀라스+무작위 $n=8,9$) | (i) $\tau(G/e)\ge\tau(G-e)$ 는 증명됨: $B_0(G-e)$ = "$u^1v^2$, $v^1u^2$ 를 포함하는 단체 제거" 복합체이며 $\pi$ 가 루프 없는 단체사상 [증명]. (ii) $\tau_h$ 는 간선 수축에서 2 이상 오르내림(상승 2칸 포함)이 관찰되나 전부 비연결 그래프(예 $K_4\sqcup K_2$)의 인공물: $\tau_h$ 비단조 때문 | [증명]/[계산 확인]. $\tau_h$ 단독으로 수축 귀납은 불가 |

### C. 아이디어 목록 (최종 상태)
| # | 주장 | 반증 방법 | 상태 |
|---|---|---|---|
| 1 | $\tau\le d_R+1$, 소규모 등호 | 하한<상한 그래프 탐색 | [계산 확인] 40/40 |
| 2 | $\tau(C_{2k+1}[K_m])=2m=\omega$, $m\ge2$ | $d_R$ 탐색 | [계산 확인] $m=2,3$; $C_7[K_2]$ |
| 3 | $d_R(G)\le\mu(G)$ | 평면 $\le3$, 외평면 $\le2$, 그 외 알려진 $\mu$ | [망상] 표본 일치 |
| 4 | $\tau(G/e)\ge\tau(G-e)$ | — | [증명] |
| 5 | $\operatorname{ind}B_0(G)\le\operatorname{ind}B_0(G-u)+1$ ($u^1\mapsto+,u^2\mapsto-$, $B_0(G)\to B_0(G-u)*S^0$) | coind 버전 불명(ind–coind 간극) | [증명 스케치] |
| 6 | $\tau_h$ 비단조 → 진짜 $\tau$ 의 하한으로 부분그래프 최대값 사용 | — | [계산 확인] |
| 7 | **S1-Radon**: $K_t$-마이너-자유 ⇒ $d_R\le t-2$ | Wagner $V_8$, 평면 + apex 등 마이너-자유족에서 $d_R$ 탐색 | [망상] 미시험 |
| 8 | $\tau\not\le\chi_f$ ($KG(9,2)$: $\tau=7>4.5$) | [기억-미검증] Lovász 공식 | 참고 |
| 9 | 순서행렬체 완화: 회로 $(C^+,C^-)$ 중 $C^+\times C^-\subseteq E$ 없는 acyclic OM 의 최소 rank | 균일 OM 탐색으로 $d_R$ 개선되는 그래프 | [망상] 미시험 |
| 10 | 이머전 lift 한 번에 $\tau$ 는 $\le1$ 만 하락 (S5 귀납) | lift 전후 샌드위치 | [망상] 미시험 |
| 11 | Mycielski: $d_R(M(G))=d_R(G)+1$ | Grötzsch 일치, $M(C_5)$ 등 추가 | [망상] 1 사례 일치 |
| 12 | 가우시안 $y$ 가 Radon-free 일 확률의 $d$-전이 | 몬테카를로 | [망상] 미시험 |

### D. 반례꾼에게 공격 요청 (우선순위)
1. **#1/T2**: $\tau\ne d_R+1$ 인 그래프 (구체적 coind–ind 간극 또는 선형성의 한계). 후보: $d_R$ 이 $\tau_h$-하한보다 큰 그래프가 8~10정점 밀집 그래프에 있는지.
2. **T1**: $C_5[K_2]$ 배치(rooms/researcher3/c5k2_d3.npy; 접근 불가 시 재생성: `lex_radon.py C5K2`)의 **정확 유리수 검증**, 및 $\tau(C_5[K_m])=2m$ 반증.
3. **#7**: $V_8$, $K_{3,3}$-계 등 마이너-자유 그래프에서 $d_R\ge t-1$ 인 것.
4. **S4 방향**: $\tau>\omega$ 이면서 $K_\tau$-세분이 없는 그래프가 존재하는가? Catlin형은 이미 방어됨(τ=ω)이므로, Hajós 반례 족(Catlin 외)의 $\tau$ 를 위 샌드위치로 재판정하는 것이 다음 단계.

### E. 한계
$d_R$ 탐색은 휴리스틱(실패는 부재 증명이 아님); 상한은 존재 증명(배치 자체가 증거)이라 건전하나 부동소수 허용오차 있음. 하한은 호몰로지 기반이며 8정점 이상 표본은 소수.
