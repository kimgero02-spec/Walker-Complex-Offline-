# [R01-researcher1] 예제 표·패턴·장애물·명제 계층 ($\tau=\operatorname{coind}(B_0)+1$)

- 작성자: researcher1 / 라운드 1 / 역할: 연구원

## 요약
1. **정의 [증명+계산 확인]**: $\tau=\operatorname{coind}(B_0)+2$ 는 $K_2$ 에서 $B_0(K_2)=S^1$, $\tau=3>\chi$ 로 틀림. 올바른 정의는 $+1$ ($K_n\to n$, $C_{2k+1}\to3$, $K_2\to2$). S6 의 다른 변형도 오프셋이 어긋나 있어 아래에서 교정.
2. **정확값 [계산 확인]**: 정점 $\le7$ 인 1252개 그래프 전부 $\tau$ 정확 결정. 1247개는 $\tau=\chi$, 5개(#878,#998,#1002,#1101,#1170=$\overline{C_7}$)는 $\tau=3<\chi=4$. Catlin형 $C_5[K_2]$ 는 $\tau=4<\chi=5$ (SW 높이로 독립 확인; researcher3 Radon 인증서와 일치).
3. **패턴**: 모든 예제에서 $\tau\le\min(\chi,h)$ (h = 최대 완전 마이너 크기), 즉 S1 위반 없음. S2·S4·S5 도 $\tau>\omega$ 인 15개 그래프에서 성립 확인. 모든 예제에서 $\tau\in\{\omega,\chi\}$ 거나 Kneser/Schrijver/Mycielski 처럼 $\tau=\chi$.
4. **계층**: $S(\chi)=$Hadwiger $\Rightarrow S(\tau)=$S1 $\Rightarrow$ (더 약한 위상 하한 버전들). 증명된 것은 $\tau\le\chi$ 로부터의 자명한 함의와 $\chi\le6$ 범위뿐; S1 자체는 열림.
5. **장애물**: coind 는 호몰로지 하한(비단조)과 SW 높이 상한(코호몰로지 환 필요, 크기 폭발)으로만 샌드위치 가능; $\tau=\omega\ll\chi$ 인 Catlin 계열은 위상 하한에 "안 보이고", 반대로 $\tau$ 가 큰 그래프(Kneser 등)는 완전 마이너가 훨씬 커서 S1 의 타이트한 시험이 안 됨.

## 본문

- 오프셋은 $\tau=\operatorname{coind}(B_0)+1$ (오케스트레이터 정정). 내 계산도 독립적으로 $+2$ 가 $\tau(K_2)=3>\chi$ 를 준다는 것을 확인했다.

### 1. 정의 점검과 τ 의 샌드위치 도구
- 하한: $\operatorname{coind}\ge \operatorname{conn}+1$, conn 은 (모듈로 $p=2,3,32003$ 환원 호몰로지 소멸) + ($\pi_1$ 자명: 스패닝 트리 + Tietze 소거로 증명된 경우만 인정). 또 **부분그래프 단조성** $\tau(H)\le\tau(G)$ ($H\subseteq G$) 와 비이분이면 $\ge3$, 간선 있으면 $\ge2$.
- 상한: $\tau\le\chi$ 및 **SW 높이** $\operatorname{coind}\le h(B_0)\le\operatorname{ind}$ ($h=\max\{k:w_1^k\ne0\in H^k(B_0/\mathbb Z_2;\mathbb F_2)\}$). 정점튜플 단체집합 모델(정규화 코체인)로 $B_0$ 에서 직접 계산 (sw2.py). 큰 그래프용으로 $B_0\simeq_{\mathbb Z_2} B(G)*S^0$ [기억-미검증, Csorba] 모델도 썼고 $K_n,C_5$ 등에서 직접 $B_0$ 값과 일치 확인.

### 2. 예제 표 ($\tau$ 는 정확값일 때만 단일 수치)
| 그래프 | $n$ | $\chi$ | $\omega$ | 최대 $K_s$ 마이너 $s$ | $\tau$ | 근거 |
|---|---|---|---|---|---|---|
| $K_n$, $n=2..6$ | n | n | n | n [증명] | **n** | $B_0(K_n)$=십자다면체 경계 $S^{n-1}$ [증명]; 호몰로지+$\pi_1$ 자명 [계산 확인] |
| $C_5,C_7,C_9$ | 5,7,9 | 3 | 2 | 3 [증명] | **3** | $B_0\simeq S^2$ (연결도 1, $\pi_1$ 자명) + $\chi=3$ [계산 확인] |
| Petersen $KG(5,2)$ | 10 | 3 | 2 | 5 (정확) | **3** | 하한 3(비이분), SW $h=2$ [계산 확인] |
| $KG(6,2)$ | 15 | 4 | 3 | $\ge4$ | **4** | $B(G)$ 연결도 1 ⇒ $\tau\ge4$ (현탁 관계 [기억-미검증]) [계산 확인] |
| Schrijver $SG(6,2)$ | 9 | 4 | 3 | 5 (정확) | **4** | $B_0$ 연결도 2 [계산 확인] |
| $SG(7,2)$ | 14 | 5 | 3 | $\ge5$ | **5** | $B$ 연결도 2 (현탁 [기억-미검증]) [계산 확인] |
| $SG(8,3)$ | 16 | 4 | 2 | $\ge4$ | **4** | $B\simeq_H S^2$, 연결도 1 [계산 확인] |
| Grötzsch ($M_4$) | 11 | 4 | 2 | $\ge6$ (명시적 가지집합 검증) | **4** | $B_0$ 호몰로지 $S^3$, 연결도 2, $\pi_1$ 자명 [계산 확인] |
| Mycielski $M_5$ | 23 | 5 | 2 | 미계산 | **5** | $B$ 연결도 2 ⇒ $\tau\ge5$ [계산 확인; 현탁 기억-미검증] |
| 보완 $\overline{C_7}$ (아틀라스 #1170) | 7 | 4 | 3 | 5 | **3** ($<\chi$) | 하한 3, 직접 $B_0$ 에서 SW $h=2$ [계산 확인] |
| 아틀라스 #878,#998,#1002,#1101 | 7 | 4 | 3 | 4,4,4,4 | **3** ($<\chi$) | 위와 동일 [계산 확인] |
| Catlin형 $C_5[K_2]$ | 10 | 5 | 4 | 6 (정확) | **4** ($<\chi$) | 하한 $\omega=4$ (단조), 상한 SW $h=3$ ($w_1^4=0$, $B*S^0$ 모델). researcher3 의 Radon 인증서 및 오케스트레이터 검증과 **독립적으로 일치** [계산 확인] |

### 3. 정점 ≤7 그래프 1252개 전수 [계산 확인]
- $\chi$, Hadwiger 수(정확, 수축 탐색), $\tau$ 하한(호몰로지·$\pi_1$·부분그래프 단조) 계산. 1247개에서 하한=$\chi$ ⇒ $\tau=\chi$. 나머지 5개(#878,#998,#1002,#1101,#1170, 모두 $\chi=4$)는 SW 높이 2 로 $\tau=3$. 즉 **정점≤7 에서 $\tau<\chi$ 는 정확히 이 5개** (모두 $\tau=3$, $\chi=4$).
- 위반 0건: $\tau\le\chi$, $\tau\le$ Hadwiger 수 (S1), 홀수 $K_5$ (#1227 이 유일한 $\tau=5>\omega=4$; 홀수 마이너 존재 확인), $\tau>\omega$ 인 15개 그래프(τ=4 14개 + τ=5 1개)에 대해 $K_\tau$ 세분(S4)과 약이머전(S5) 존재 확인.
- 주의: researcher2 가 지적한 대로 호몰로지 하한 $\tau_h$ 는 단조가 아니다; 단조화(부분그래프 최댓값)가 필수. 처음 $\tau_h$ 만 쓰면 73개가 미결정이었으나 단조화로 5개로 줄었다.

### 4. 정의 점검 상세 (S6 오프셋 교정) [K_n, C_5 로 확인]
$B_0(K_n)$=십자다면체 경계 $S^{n-1}$ [증명], $B(K_n)\simeq S^{n-2}$, $B_0(C_5)\simeq S^2$, $B(C_5)\simeq S^1$ (호몰로지 [계산 확인]). 여기서 $\operatorname{ind}=\operatorname{coind}=\dim$ (구면). 변형별 값:

| 변형 | $K_n$ | $C_5$ | 판정 |
|---|---|---|---|
| $\operatorname{coind}(B_0)+1$ | $n$ | 3 | 표준, 타이트 |
| $\operatorname{coind}(B_0)+2$ (problem 원안) | $n+1$ | 4 | **오류** ($>\chi$) |
| $\operatorname{coind}(B)+2$ | $n$ | 3 | 올바름 ($=\tau$ 와 같거나 약함) |
| $\operatorname{coind}(B)+1$ | $n-1$ | 2 | 유효하지만 한 칸 약함 → $+2$ 가 표준 |
| $\operatorname{ind}(B_0)+1$ | $n$ | 3 | 올바름 |
| $\operatorname{ind}(B_0)+2$ | $n+1$ | 4 | **오류** |
| $\operatorname{ind}(B)+2$ | $n$ | 3 | 올바름 |
| $\operatorname{ind}(B)+1$ | $n-1$ | 2 | 한 칸 약함 |
| $\operatorname{conn}(B_0)+2$ | $n$ | 3 | 올바름 |
| $\operatorname{conn}(B_0)+3$ (problem 원안) | $n+1$ | 4 | **오류** |
| $\operatorname{conn}(\mathrm{Hom}(K_2,G))+3=\operatorname{conn}(B)+3$ | $n$ | 3 | 올바름 |

### 5. 패턴과 명제별 판정
- **[증명]** 단조성: $H\subseteq G\Rightarrow B_0(H)\subseteq B_0(G)$ ($\mathbb Z_2$-부분복합체) $\Rightarrow \tau(H)\le\tau(G)$. 따라서 $\tau\ge\omega$. (researcher3 의 #4: $\tau(G/e)\ge\tau(G-e)$ 도 단체사상으로 옳음을 확인.)
- **관찰 [계산 확인]**: $\tau=\chi$: $K_n$, 홀수 사이클, Kneser, Schrijver, Mycielski (Grötzsch, $M_5$), 아틀라스의 1247개. $\tau=\omega<\chi$: Catlin형 $C_5[K_2]$ (R3: $C_5[K_3]$ 도). $\omega<\tau<\chi$ 인 사례는 이 규모에서 발견되지 않음: 모든 예제에서 $\tau=\chi$ 또는 $\tau=\omega$ (후자: 아틀라스 5개 $\tau=\omega=3<\chi=4$, $C_5[K_2]$).
- **[추측]** $\tau(C_5[K_m])=2m$ ($m\ge2$) — $m=2$ 내 계산, $m=3$ 은 R3. Catlin 반례들은 위상 하한에 안 보임.

| 명제 | 판정 | 근거 |
|---|---|---|
| S1 | **열림**. $\chi\le6$ 범위에서는 참 ($\tau\le\chi$ + Hadwiger $t\le6$ [기억-미검증: Robertson–Seymour–Thomas]) [증명 modulo 인용]. 아틀라스·표의 모든 예제에서 성립 [계산 확인] | Hadwiger $\Rightarrow$ S1 [증명] |
| S2 | 열림. $t\le4$ 는 Catlin [기억-미검증] + $\tau\le\chi$. $t=5$ 유일 시험 그래프 #1227 ($\tau=5>\omega=4$)에서 홀수 $K_5$ 마이너 확인 [계산 확인] | |
| S3 | 열림. S2 $\Rightarrow$ S3 [증명, $\lfloor t/2\rfloor+1\le t$]. 위상 하한 $t$ 에서의 Steiner (i) 가 $\tau$ 에도 적용되는지는 정의 확인 불가 [기억-미검증]; $\tau$ 가 "위상적 하한" 계층에 속한다면 적용될 것 [추측] | |
| S4 | 열림, 반례 없음. $\tau>\omega$ 인 15개 그래프에서 $K_\tau$ 세분 존재 [계산 확인]. Catlin 반례(큰 $\chi/\omega$)는 $\tau\approx\omega$ 라 시험대가 못 됨. **S4 반례 후보는 $\tau>\omega$ 이면서 $K_\tau$ 세분이 없는 그래프** | |
| S5 | 열림. $\tau\ge t$ 인 15개에서 약이머전 존재 [계산 확인]. $t\le7$ 에서 색칠수 이머전 추측의 알려진 결과 [기억-미검증] + $\tau\le\chi$ 로 참일 것 | |
| S6 | 아래 계층 | |

### 6. 이론 구조화 (계층)
기호 $S(\beta)$ := "$\beta(G)\ge t\Rightarrow K_t$ 마이너". **[증명]** $\beta\le\beta'$ (모든 $G$) 이면 $S(\beta')\Rightarrow S(\beta)$ (가설이 더 강해짐). 표준 부등식열 (Matoušek–Ziegler [기억-미검증], $B_0\simeq_{\mathbb Z_2}\Sigma B$ 가정):
$$\operatorname{conn}(B)+3=\operatorname{conn}(B_0)+2\ \le\ \operatorname{coind}(B)+2\ \le\ \underbrace{\operatorname{coind}(B_0)+1}_{\tau}\ \le\ \operatorname{ind}(B_0)+1\ \le\ \operatorname{ind}(B)+2\ \le\ \chi .$$
또 $\tau\le h(B_0)+1$ (SW 높이, $\operatorname{coind}\le h\le\operatorname{ind}$). 따라서
$$\text{Hadwiger}=S(\chi)\Rightarrow S(\operatorname{ind}(B)+2)\Rightarrow S(\operatorname{ind}(B_0)+1)\Rightarrow S(\tau)=\text{S1}\Rightarrow S(\operatorname{coind}(B)+2)\Rightarrow S(\operatorname{conn}+\cdot).$$
Dol'nikov–Kříž: Steiner (ii) 는 $S(\mathrm{DK})$ [기억-미검증]. DK $\le\tau$ 라면 [방향 불확실, 기억-미검증] S1 $\Rightarrow S(\mathrm{DK})$ 이므로 **S1 은 Hadwiger 와 알려진 Steiner (ii) 사이**; $\tau$ 가 DK 보다 엄밀히 클 수 있는지(그리고 그때 S1 이 새로운 정보인지)가 핵심. 계산: 정점≤7 에서 $\tau<\chi$ 인 5개는 $S(\tau)$ 가 $S(\chi)$ 보다 엄밀히 약한 가설 집합을 줌을 보여 준다 (이들은 $\chi\ge4$ 지만 $\tau\ge4$ 가 아님).
**증명된 부분**: 위 함의열(부등식열 인용 전제), 단조성, $\chi\le6$ 에서의 S1/S5(인용 전제). **열린 부분**: S1 전체, 모든 S2–S5.

### 7. 공통 장애물
1. **계산**: coind 정확 계산 불가. 하한(호몰로지)은 비단조라 단조화 필요, 상한(SW)은 정점튜플 모델이 $C_5[K_2]$ 에서도 $k=4$ 에 28만 튜플 — $\ge12$ 정점이면 폭발. Radon 인증서(R3)가 대안.
2. **예제의 타이트함 부족**: S1 의 진짜 시험은 "$\tau\ge t$ 인데 마이너 $K_t$ 가 아슬아슬한" 그래프인데, $\tau>\omega$ 인 예제(Kneser/Schrijver/Grötzsch)는 완전 마이너가 $\tau$ 보다 훨씬 크고(예: Grötzsch $h\ge6$, $\tau=4$), 마이너가 아슬아슬한 건 $K_t$ 를 포함하는 경우뿐. Catlin형처럼 $h\approx\chi$ 인 그래프는 $\tau=\omega$.
3. **이론**: $\tau$ 가 minor-monotone 인지 알 수 없음 (단조성은 부분그래프에서만 증명). S1 증명엔 "$\tau\ge t\Rightarrow$ 수축으로 $\tau$ 를 유지하며 줄이기" 같은 보조정리가 필요하나 $\tau(G/e)$ 상한/하한이 없다.
4. **인용**: Csorba 현탁 동형, MZ 부등식열, DK 와 $\tau$ 의 대소 모두 [기억-미검증]. 직접 $B_0$ 로 확인한 것은 $K_n,C_5,C_7,C_9$, Petersen, SG(6,2), Grötzsch, 5개 7정점 그래프이고 $KG(6,2),SG(7,2),SG(8,3),M_5,C_5[K_2]$ 의 일부는 $B$ 또는 $B*S^0$ 모델에 의존.

### 8. 도서관 교차 검증
- R2: 정의 오류·$\tau_h$ 비단조 지적 확인(내 데이터 일치: 단조화 전 73개 미결정). 아틀라스 위반 0 일치. 그의 "$C_5[K_2]$ 4 또는 5" 는 **4** 로 결정.
- R3: $\tau(C_5[K_2])=4$ 를 코호몰로지 방법으로 독립 확인; Kneser 공식 $\tau=n-2k+2$ 는 $KG(5,2),KG(6,2)$ 와 일치. 아이디어 #7(마이너-자유 ⇒ Radon-free) 는 미시험.

### 9. 남은 질문
$\tau>\omega$ 이면서 $\tau<\chi$ 인 그래프 존재? ($\tau\in(\omega,\chi)$ 사례 없음); $\tau(C_5[K_m])=2m$; DK 와 $\tau$ 의 관계; $\tau$ 의 minor-단조성; 아틀라스 밖(8정점 이상) 전수.
