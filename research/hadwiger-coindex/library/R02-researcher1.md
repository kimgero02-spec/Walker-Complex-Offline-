# [R02-researcher1] 그림 1 화살표 검증 · cd ≤ τ 증명 시도 · S3 전이 · S4 시험대

- 작성자·라운드·역할: researcher1 / 라운드 2 / 연구원 (지점 1 + 지점 4)
- 읽은 자료: Steiner 2312.17130 **p.3 (정의 1, 그림 1 — 이미지로 판독), p.4 (정의 2–3, 정리 1), p.5 (정리 2–3, 문제 1), p.6 (정의 4, 정리 4 진술)**. 8–12쪽은 읽지 않음 (정리 2·3 증명은 이번 임무에 불필요). Norin–Steiner 2610.05291 은 이번 임무와 직접 관계 없어 생략.
- 중간 결과: `library/R02-researcher1-interim.md`. 반례꾼 R02-researcher2* 파일은 이 보고서 작성 시점에 도서관에 없었다 (반영 불가). 망상꾼 `R02-researcher3-interim.md` 와 최종 `R02-researcher3.md` 를 읽었다. 그쪽의 "τ 는 마이너 비단조 (C4 ≻ K3)" 는 R01 과 일치하며 수용했으나 나는 재확인하지 않았다. 그쪽 "덧셈형 Lemma 13 유사 보조정리 거짓 (K4)" 와 "S1-Radon t≤6" 은 이번 임무 결과와 독립이라 본문에 쓰지 않았다.

## 요약
1. **[계산 확인] 그림 1 해석 확정**: `cd(H) ≤ coind(B0(G))+1` 은 그림에 "≤" 로 직접 적혀 있고, 체인 $\tau\le\operatorname{ch-ind}(B_0)+1\le\operatorname{ind}(B_0)+1\le\operatorname{ind}(B)+2\le\operatorname{Xind}+2\le\operatorname{zig}\le\chi$ 가 같은 방향이다. 화살표 해석은 틀리지 않았다.
2. **[증명 스케치] 임의의 Kneser 표현에 대해 $\operatorname{cd}(\mathcal H)\le\tau(G)$.** 부호 집합 복합체에서 $B_0(G)$ 로 가는 등변 포셋 사상을 만들고, 그 정의역에서 "$\Lambda$" 를 떼어 내면 $\operatorname{cd}$ 가 쌍대(Alexander) 연결성으로 나온다. 외부 사실 3개를 인용했다 (§2).
3. **귀결 1 (지점 4 의 질문에 대한 답)**: $\operatorname{cd}\le\tau$ 이므로 Steiner 정리 3 은 τ 로 옮겨지지 않는다 (방향이 반대). 귀결 2: S1(τ 판)은 정리 3 의 모든 적용을 포함하는 **더 강한** 주장이다.
4. **귀결 3 (S3 가 닫힘, 문헌 체인 의존)**: $\tau\le\operatorname{zig}$ 이므로 정리 2 에서 S3 ($\tau\ge t\Rightarrow$ 홀수 $K_{\lfloor t/2\rfloor+1}$ 마이너) 가 나온다. R01 에서 "열림"이던 S3 가 이 체인으로 해결된다. 단 체인은 문헌 인용이라 [문헌 확인] 이다.
5. **지점 1 (S4 시험대)**: $\tau\le\chi$ 이므로 색칠 버전 S4($\chi$) 가 참이면 S4($\tau$) 도 참이다. 따라서 Catlin 반례 (τ=ω) 는 시험대가 못 되는 것이 아니라 **애초에 반례가 아니고**, S4($\tau$) 반례는 $t\ge5$ 에서만 가능하다. 또 $\tau\ge t$ 이고 $\omega<t$ 인 그래프가 시험대이며, 지금까지 그런 그래프의 구조는 알려지지 않았다.

---

## 본문

### 1. 그림 1 해석 [계산 확인: 이미지 판독, p.3]
- 그림 1 (p.3) 은 위에서 아래로 $\chi\ge\operatorname{zig}\ge\operatorname{Xind}(\operatorname{Hom}(K_2,G))+2\ge\operatorname{ind}(B)+2\ge\operatorname{ind}(B_0)+1\ge\operatorname{ch-ind}_{\mathbb Z_2}(B)+2=\operatorname{ch-ind}_{\mathbb Z_2}(B_0)+1$ 이고, 그 아래로 $\operatorname{coind}(B_0)+1$, $\operatorname{conn}_{\mathbb Z_2}(B)+3$ 등이 대각선 화살표로 연결된다.
- 대각선 기호는 작은 쪽을 가리킨다. 왼쪽의 $\operatorname{cd}(\mathcal H)\le\operatorname{coind}(B_0)+1$ 은 "≤" 기호 자체로 적혀 있다.
- 따라서 $\operatorname{cd}(\mathcal H)\le\tau(G)\le\operatorname{ch-ind}_{\mathbb Z_2}(B_0)+1\le\operatorname{ind}(B_0)+1\le\dots\le\operatorname{zig}(G)\le\chi(G)$ (단, $\tau\le\operatorname{zig}$ 는 대각선 체인 전체를 이용).
- 정의 확인: Steiner 정의 1 은 $B_0$ 면 = $X_1$, $X_2$ 가 서로 완전이분 (빈 쪽 허용). 우리 정의와 일치. $\tau(G)=\operatorname{coind}(B_0(G))+1$ 은 그림의 "coind(B₀(G))+1" 칸과 같다.
- 정의 3 (p.4): $\operatorname{cd}(\mathcal H)=\min\{|U|: (V\setminus U,\{e: e\cap U=\varnothing\})\text{ 는 2-색칠 가능}\}$. 정리 1 (Dol'nikov–Křı́ž): $\chi(G)\ge\operatorname{cd}(\mathcal H)$.

### 2. 정리 A: $\operatorname{cd}(\mathcal H)\le\tau(G)$ 증명 시도 [증명 스케치]

**설정.** $\mathcal H=(V,E)$, $\mathcal K G(\mathcal H)=G$, 모든 $e\in E$ 는 비공집합 ($N=|V|$). 간선은 서로소.

**단계 1 (부호 복합체).** $\Sigma$ = 부호 집합 $S\subseteq V^{\pm}$, $\{+v,-v\}\not\subseteq S$ 인 것들. 이것은 $\partial$(교차다면체) $\cong S^{N-1}$, 대척 $S\mapsto -S$ 가 자유 작용. $S^+$, $S^-$ 는 양/음 부분.

**단계 2 (사상).** $\Psi(S)=A(S)\times\{1\}\cup B(S)\times\{2\}$, $A(S)=\{e\in E: e\subseteq S^+\}$, $B(S)=\{e\in E: e\subseteq S^-\}$.
- 면 조건: $e\in A$, $f\in B$ 이면 $e\subseteq S^+$, $f\subseteq S^-$, $S^+\cap S^-=\varnothing$ 이므로 $e\cap f=\varnothing$, 즉 $e\sim f$ in $G$. 따라서 $\Psi(S)$ 는 $B_0(G)$ 의 면.
- 단조성: $S\subseteq S'\Rightarrow\Psi(S)\subseteq\Psi(S')$. 등변성: $\Psi(-S)=\operatorname{swap}\Psi(S)$.

**단계 3 (떼어 낼 부분).** $\Lambda=\{S\in\Sigma: S^+\text{ 과 }S^-\text{ 가 각각 } E \text{ 의 간선을 포함하지 않음}\}$. $\Lambda$ 는 부분복합체, 등변. $\Psi(S)=\varnothing\iff S\in\Lambda$.
- 이유: $\Psi(S)=\varnothing$ 인 꼭짓점 $S$ 를 두면 order complex 가 뿔(cone)이 되어 사상이 정의되지 않는다. **함정 확인**: $\Lambda$ 를 떼지 않으면 $K_3$ 에 쓸모없는 원소 $v_0$ 를 하나 더한 표현에서 $S^3\to S^2$ 등변 사상이 생겨 Borsuk–Ulam 에 모순된다. 따라서 $\Lambda$ 제거는 필수다.
- 그러므로 $\Psi:\ \Delta(F(\Sigma)\setminus F(\Lambda))\to\Delta(F(B_0))$ 가 등변 사상으로 정의되고 (사슬 $S_0\subsetneq\dots\subsetneq S_k$ 는 $\Psi(S_0)\subseteq\dots\subseteq\Psi(S_k)$ 로 간다), 따라서 $\operatorname{coind}(\Delta(F(\Sigma)\setminus F(\Lambda)))\le\operatorname{coind}(B_0)$.

**단계 4 ($\Lambda$ 의 크기).** $S\in\Lambda$ 라 하고 $U=V\setminus(S^+\cup S^-)$. $E_U=\{e: e\cap U=\varnothing\}$ 의 간선은 $e\subseteq S^+\cup S^-$ 이고, $S\in\Lambda$ 는 "$e\not\subseteq S^{\pm}$" 와 동치이므로 $(S^+,S^-)$ 는 $(V\setminus U,E_U)$ 의 진짜 2-색칠이다. 따라서 $U$ 는 "좋은" 집합. $\operatorname{cd}(\mathcal H)=c$ 이면 $|U|\ge c$, 즉 $|S|\le N-c$. 따라서 $\Lambda\subseteq\operatorname{skel}_{N-c-1}(\Sigma)$.

**단계 5 (연결성).** $|\Sigma|=S^{N-1}$ 에서 $X=|\Sigma|\setminus|\operatorname{skel}_{N-c-1}|$, $Y=|\Sigma|\setminus|\Lambda|\supseteq X$.
- 쌍대: $d=N-1$, $j=N-c-1$ 이면 $X$ 는 $(d-j-2)=(c-2)$-연결 (F2).
- (F3): $k$-연결인 자유 $\mathbb Z_2$-공간 $X$ 에는 등변 $S^{k+1}\to X$ 가 있다 (자유 $\mathbb Z_2$-CW 구조에서 $(k+1)$-셀의 경계 $S^k\to X$ 는 $\pi_k(X)=0$ 이라 늘 null-homotopic). 따라서 $S^{c-1}\to X\subseteq Y$.
- $Y\simeq_{\mathbb Z_2}\Delta(F(\Sigma)\setminus F(\Lambda))$ (F1). 따라서 $S^{c-1}\to Y\to B_0(G)$ 등변 사상이 있고 $\operatorname{coind}(B_0(G))\ge c-1$, 즉 $\tau(G)\ge c=\operatorname{cd}(\mathcal H)$. ∎ [증명 스케치]

**외부 사실 (인용)**: (F1) 단체복합체 $K$ 와 부분복합체 $L$ 에 대해 $|K|\setminus|L|\simeq\Delta(F(K)\setminus F(L))$ (반사영 구성은 대척 사상과 가환). (F2) $d$-구면의 삼각분할에서 $j$-골격의 여집합은 $(d-j-2)$-연결 (일반 위치, Alexander 쌍대). (F3) 위 연결성 ⇒ 등변 구면 사상 (장애물 이론).

**점검 (내가 한 것)**: $\operatorname{cd}$ 정의의 경계 조건 (빈 간선) 은 정리에서 $e\ne\varnothing$ 로 가정. $N=|V|$ 는 여분 원소를 포함하며, 여분 원소를 더해도 $\operatorname{cd}$ 와 $\tau$ 모두 불변인지 확인이 필요 (아래 장애물 1).

**장애물·약점 (반례꾼이 공격할 곳)**
- (O1) $\operatorname{cd}$ 는 여분 원소에 대해 $\Lambda$ 를 통해 불변인가? 증명의 $N$ 은 여분 원소를 세지만, $c$ 는 세지 않는다. 단계 5 는 $N$ 에 대해 성립하므로 결론은 여분 원소와 무관하게 옳아야 한다. 확인은 예 $K_3+v_0$ (c=3, τ=3) 에서 성립. 일반 증명은 미완.
- (O2) (F2) 의 정확한 형태 (일반 위치 연결성, 자유 구면 골격) 는 인용이며 직접 검증하지 않았다.
- (O3) Steiner 정의 1 에서 $X_1,X_2$ 는 완전이분 "쌍" 이지 $B$ 와의 공통 이웃 조건을 요구하지 않는다. $B_0$ 를 쓰는 본 증명은 그 정의와 맞다 (B 가 아님).

### 3. 귀결

**(a) 정리 3 의 τ 전이 불가 (지점 4 의 답).** $\operatorname{cd}(\mathcal H)\le\tau(G)$ 이므로 "$\tau(G)\ge t$" 는 "$\operatorname{cd}(\mathcal H)\ge t$" 를 주지 않는다. 정리 3 은 $\operatorname{cd}$ 쪽에만 쓸 수 있다. 화살표 방향이 맞고, 정리 3 의 τ 판은 **$\tau$ 가 $\operatorname{cd}$ 와 같아지는 표현이 존재한다는 추측 C 가 필요**하다 (§5).

**(b) S1(τ 판) 과 정리 3 의 관계.** $\{\exists\mathcal H:\operatorname{cd}(\mathcal H)\ge t\}\subseteq\{\tau(G)\ge t\}$ 이므로, S1 (τ 판) 은 정리 3 의 hypothesis 를 약화한 명제. 즉 S1 ⇒ 정리 3 (역은 추측 C 아래에서만).

**(c) S3 는 τ 에 대해 성립 [문헌 체인 의존].** 정리 2 (Steiner, p.5): $\operatorname{zig}(G)\ge t\Rightarrow$ 홀수 $K_{\lfloor t/2\rfloor+1}$ 마이너. 그림 1 체인에서 $\tau(G)\le\operatorname{zig}(G)$. 따라서 $\tau(G)\ge t\Rightarrow\operatorname{zig}(G)\ge t\Rightarrow$ 홀수 $K_{\lfloor t/2\rfloor+1}$ 마이너. 이것은 S3 그 자체다. R01 보고서의 "S3 열림" 판정을 **수정**한다 (R01 은 그림의 τ 위치를 확인하지 못했다고 했음).
- 주의: 체인의 각 부등식 (Matoušek–Ziegler, Daneshpajouh–Meunier) 은 그림에서 읽은 것이다. [문헌 확인: 원 문헌 미확인]

**(d) S4 와 색칠 버전.** $\tau\le\chi$ 이므로 "$\chi\ge t\Rightarrow K_t$ 세분" (색칠 Hajós) 이 참이면 "$\tau\ge t\Rightarrow K_t$ 세분" 도 참이다. 알려진 범위 (Dirac, $t=4$ [기억-미검증]; $t=5$ 는 Mader/Thomassen 계열 [기억-미검증]; $t\ge7$ 에서는 Catlin 반례로 색칠 버전 거짓 [R01 인용]) 에서, τ 판 S4 의 **새 반례 후보는 $t\ge5$ 이면서 $\tau\ge t$ 인 그래프** 뿐이다. Catlin 계열은 $\tau=\omega$ 이므로 S4 반례가 아니다 (R01 결론 확인).

### 4. 예제 표 (a)

| 그래프 $G$ | $n$ | $\chi$ | $\omega$ | $\tau$ (R01) | $\operatorname{cd}$ (계산한 표현) | 사용처 |
|---|---|---|---|---|---|---|
| $K_3$ (표준, 싱글톤 + 사적 원소) | 3 | 3 | 3 | 3 | 3 [계산 확인] | 귀결 (a) 의 등호 예 |
| $K(5,2)$ = Petersen (표준) | 10 | 3 | 2 | 3 | 3 [계산 확인] | 정리 A 의 등호 예, 추측 C 지지 |
| $K(6,2)$ (표준) | 15 | 4 | 3 | 4 | 4 [계산 확인] | 추측 C 지지 (Kneser 등호) |
| $S(6,2)$ (안정 집합, ground $[6]$) | 9 | 4 | 3 | 4 | 2 [계산 확인] | $\operatorname{cd}<\tau$ 확인 (정리 A 와 일관) |
| $S(7,2)$ (표준) | 14 | 5 | 3 | 5 | 3 [계산 확인] | $\operatorname{cd}<\tau$, 추측 C 반증 후보 (표준 표현 한정) |
| $S(8,3)$ (표준) | 16 | 4 | 2 | 4 | 0 [계산 확인] | 표준 표현이 타이트하지 않음 |
| $C_5[K_2]$ (Catlin 형, 극대 독립집합 표현) | 10 | 5 | 4 | 4 | 0 [계산 확인] | 정리 A 의 상한 4 와 일치 (5 는 불가) |
| $\overline{C_7}$ (아틀라스 #1170, $\tau<\chi$) | 7 | 4 | 3 | 3 | 1 (극대 독립집합, 선 표현 둘 다) [계산 확인] | S3 예시. 추측 C 반례 후보 |
| $\overline{C_5}=C_5$ (선 표현, 외곽 5-사이클 of $K(5,2)$) | 5 | 3 | 2 | 3 | 1 [계산 확인] | 추측 C 시험 (표준 표현 실패) |
| $C_5$ (극대 독립집합 표현) | 5 | 3 | 2 | 3 | 1 [계산 확인] | 같은 이유 |

- 모든 행에서 $\operatorname{cd}\le\tau\le\chi$ 가 성립 (계산 확인). 위반 0 은 근거가 아니라 정리 A 의 **등호 여부 점검** 용이다 (연구 원칙에 따라 전수 점검은 하지 않음).
- 계산 코드: `rooms/researcher1/cd_check.py`, `cd_kneser.py`, `cd_ind.py`, `cd_line.py`.

### 5. 추측과 증명 시도 (b)

**추측 C ($\tau$ 의 Kneser 도달성) [추측].** 모든 $G$ 에 대해 $\max_{\mathcal H:\,KG(\mathcal H)=G}\operatorname{cd}(\mathcal H)=\tau(G)$.
- 지지: Kneser $K(n,k)$ 에서 $\operatorname{cd}=n-2k+2=\tau$ (계산 확인, $(5,2),(6,2)$).
- 부정적 증거: 표준·극대 독립집합·선·외곽 사이클 표현에서 $\operatorname{cd}$ 가 $\tau$ 보다 훨씬 작다 (표 §4). 이것은 **표현 선택의 문제**인지 **추측 C 가 거짓인지** 구분하지 못한다. 전 표현 탐색은 불가능.
- 귀결: 추측 C ⇒ 정리 3 ⇒ S1 (τ 판) 을 얻는 경로 (정리 3 이 τ 로 옮겨진다). 추측 C 가 거짓이면 이 경로는 막힌다.
- 증명 시도: 정리 A 의 역방향 — $\tau\ge c$ 로부터 $\operatorname{cd}\ge c$ 를 얻는 표현 구성이 필요. 시도한 구성: 후보 ground $=V(B_0(G))$, $e_x=\{(x,1)\}\cup\dots$ — 간선-분리 조건을 만족하는 식을 찾지 못함. **장애물**: $\operatorname{cd}$ 는 "모든 작은 $U$ 가 나쁨" 이라는 조합적 조건인데, $\tau$ 는 위상적 높이라 이 조건을 직접 읽어낼 $\mathbb Z_2$-사상이 없다. $\Psi$ 의 역상이 필요하다.
- 반증 계획: 간선 수 적은 $\tau<\chi$ 그래프 ($\overline{C_7}$, 아틀라스 #878·#998·#1002·#1101) 에서 $\operatorname{cd}=3$ 인 표현을 찾으면 추측 C 지지. 찾지 못하면 기각 쪽.

**추측 S4-τ 시험 설계 [추측].** $t\ge5$, $\tau(G)\ge t>\omega(G)$, 그리고 $K_t$ 세분이 없는 $G$ 가 S4 반례. 조건을 만족하는 $G$ 탐색은 $\chi\ge t$ 이고 $K_t$ 세분 금지인 그래프 (Hajós 반례 구조) 를 찾는 것과 같다. 시험대는 Catlin 계열이 아니어야 한다 (τ=ω). 실제 탐색은 미실시 (구조 설계만).

**증명 시도 (S3-τ 체인) [증명 스케치, 문헌 의존].** 위 §3(c) 참조. 증명 자체는 정리 2 의 원 증명 (8–12쪽, 미독) 에 의존한다.

### 6. 결정적 계산 확인 (c)
- [계산 확인] 정규 Kneser: $\operatorname{cd}(K(5,2))=3$, $\operatorname{cd}(K(6,2))=4$ — 두 경우 모두 $=\tau$. 정리 A 의 등호 성립 확인 (Dol'nikov 타이트, 정리 3 의 Kneser 적용 대상과 일치).
- [계산 확인] $\operatorname{cd}(S(7,2)\text{ 표준})=3<5=\tau$: 정리 A 와 일관, 그리고 표준 표현에서는 τ 에 도달하지 않음을 보여 준다.
- [계산 확인] $\operatorname{cd}(\mathcal H_{\rm ind}(K_3))=3$ (싱글톤), 극대 독립집합 표현 $K_3$ 에서 $\operatorname{cd}=3=\tau$.
- 이 계산은 정리 A 를 **반증하지 않음** (모든 표현에서 $\operatorname{cd}\le\tau$). 증명의 등호 쪽만 확인했다.

### 7. 한계
- 정리 A 는 스케치다. (F1)–(F3) 인용 및 (O1) 여분 원소 불변성의 일반 증명이 남았다.
- 그림 1 체인은 이미지 판독. 원 문헌 (Daneshpajouh–Meunier 2023 survey) 은 미확인.
- Dirac/Mader/Thomassen 의 $t=4,5$ 결과와 Catlin 반례 범위는 [기억-미검증].
- 정리 2 증명 (8–12쪽) 은 읽지 않음.

## 문주님께 요청

1. **요청: Daneshpajouh–Meunier 2023 서베이 (그림 1 의 원 출처)** — 이유: 그림 1 체인 $\tau\le\operatorname{zig}$ 와 $\operatorname{ch-ind}$ 의 부등식이 그림에서만 확인됨. 귀결 (c) S3 가 이 체인에 의존. 긴급도: **있으면 좋음**. 없을 때의 대안: 그림 판독 + 정리 2 의 $\operatorname{zig}$ 정의로 $\tau\le\operatorname{zig}$ 를 직접 증명 시도 (Matoušek–Ziegler 의 $\operatorname{coind}$ 와 $\operatorname{zig}$ 비교 필요).
2. **요청: Dirac(1952), Mader/Thomassen 의 Hajós 결과 (t=4,5), Catlin(1979) 원문** — 이유: S4-τ 의 반례 범위 ($t\ge5$) 를 확정하기 위해. 긴급도: **있으면 좋음**. 없을 때의 대안: [기억-미검증] 로 두고 $t\le4$ 만 사용.

## 후속연구 지점

1. **추측 C 의 판정 (지점 4 연장).** 무엇을: $\max_{\mathcal H}\operatorname{cd}(\mathcal H)=\tau(G)$ 가 $\overline{C_7}$ (τ=3<χ=4) 에서 성립하는지 — 즉 $\operatorname{cd}(\mathcal H)=3$ 인 Kneser 표현이 있는지. 왜: 성립하면 정리 3 을 통해 τ 판 S1 의 경로가 열림; 기각되면 S1 은 정리 3 과 독립적 문제로 남음. 시작: $\overline{C_7}$ 의 Kneser 표현은 ground 를 작게 (예: 7 원소 위의 $k$-집합 족, $\overline{C_7}$ 의 교차 그래프) 잡아 $\operatorname{cd}$ 를 계산 (코드 `cd_check.py` 재사용), 그 후 "모든 표현 대신 교차-그래프로 나오는 표현만" 으로 제한해 시험. 난점: 표현 공간이 크고 전수 탐색은 연구 원칙에 어긋남 — 표현 구조 (대칭) 를 이용한 연역적 분류가 필요. 막힌 지점: 역방향 구성 (§5).
2. **정리 A 의 증명 완결 (지점 4 완결).** 무엇을: (O1) 여분 원소 불변성과 (F1)–(F3) 의 적용 조건을 정리로 완성. 왜: S1·S3 논의의 토대 ($\operatorname{cd}\le\tau$ 가 확정되면 정리 3 의 τ 판 불가가 확정). 시작: $\Lambda$ 의 골격 차수를 $N$ 대신 $|\bigcup E|$ 로 줄이는 축약을 시험. 난점: (F2) 의 일반 위치 주장을 직접 증명하는 것은 길다. 반례꾼이 $\Lambda$ 의 연결성 주장을 공격해 주면 좋다.
3. **S3 체인의 독립 증명 (지점 4 와 S3 연결).** 무엇을: $\tau\le\operatorname{zig}$ 를 그림 체인 없이 증명 (Steiner 정리 2 의 zig 정의와 $\operatorname{coind}(B_0)$ 의 구성 직접 비교). 왜: S3 가 이 체인에 의존하므로 독립 확인이 필요 (R01 에서 S3 가 열려 있었던 이유). 시작: Daneshpajouh–Meunier 서베이 요청 (§문주님께 요청 1) 이 오면 확인, 아니면 zigzag 를 $B_0$ 의 단체 경로로 옮기는 사상 시도. 난점: zig 와 coind 의 연결이 위상적이라 조합적 증명이 어려울 수 있음.
4. **S4-τ 시험대 구성 (지점 1 의 후속).** 무엇을: $t=5$ 에서 $\tau\ge5$, $\omega\le4$ 이고 $K_5$ 세분이 없는 그래프의 존재 여부 — 색칠 버전 ($\chi\ge5\Rightarrow K_5$ 세분) 이 참이면 불가능, 따라서 먼저 그 참을 확인. 왜: S4-τ 는 $t\ge5$ 에서만 새 정보를 준다. 시작: $\chi\ge5$ 인 소형 그래프에서 $K_5$ 세분 존재를 검사하고 (가지치기 탐색, $n\le 10$), $\tau\ge5$ 인 후보만 조사. 난점: $\tau\ge5$ 인 그래프는 R01 아틀라스 ($n\le7$) 에서 #1227 하나뿐이고 $\omega=4$ 였으므로 시험대가 작다. 더 큰 $n$ 에서 $\tau$ 계산이 필요하며 coind 계산기가 없다.
5. **Schrijver/Kneser 표현 타이트성 분류 (지점 4 의 부산물).** 무엇을: 표준 표현에서 $\operatorname{cd}$ 가 $\tau$ 와 같은 경우 ($K(n,k)$) 와 다른 경우 ($S(n,k)$) 의 조건 정리. 왜: 추측 C 의 긍정 예 (Kneser) 와 부정 예 (Schrijver 표준) 를 나누는 기준이 생기면 정리 3 의 적용 범위가 명확해진다. 시작: $S(n,k)$ 에서 $\operatorname{cd}$ 를 $n,k$ 에 대해 표로 계산 (소수 예), 패턴 추측 후 증명 시도. 난점: Schrijver 의 안정 조건이 $\operatorname{cd}$ 의 2-색칠 조건과 어떻게 얽히는지 연역적 연결이 불명확.
