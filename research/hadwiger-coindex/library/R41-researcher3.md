# [R41-researcher3] 자유 Z_2 nerve 를 주는 덮개 (짝 덮개 = genus 덮개) 와 τ ≤ g(k) 판정, 그리고 R11 반례의 정정

- 작성자·역할: researcher3 (망상꾼). 무인 6라운드 중 1. 한 번만 보고. 계산 없음 (증명 스케치, 표준 사실은 [기억-미검증]).
- 표기: $X=B_0(G)$ (자유 $\mathbb Z_2$, 고정 비공집합 면 없음), $\operatorname{coind}X=\max\{n: S^n\to X\}$, $\operatorname{ind}X=\min\{n: X\to S^n\}$ (등변 사상), $\tau=\operatorname{coind}+1\le\iota=\operatorname{ind}+1$. Krasnosel'skii genus $\gamma(X)=\min\{m: X\to\mathbb R^m\setminus0 \text{ 홀수 사상}\}=\operatorname{ind}X+1$ [기억-미검증, 표준].

## 0. 실패 기준 (먼저)
- **(F) 자유 nerve 정리:** 짝 덮개 (아래 정의) 가 $m$ 쌍이면 nerve 는 자유이고 $\dim\le m-1$, 따라서 $\tau\le m$. 실패 = $m$ 쌍 짝 덮개가 있는데 $\tau>m$ 인 예.
- **(G) 블록 상계:** 블록 $k$ 개에서 $\tau\le\sum_i\iota(G[V_i])$. 실패 = 이 부등식이 깨지는 예.
- **(C) 비교:** (G) 가 χ 색 논법 $\sum\chi_i$ 보다 엄밀히 좋은 경우가 있다. 실패 = 모든 블록에서 $\iota_i=\chi_i$.

## 1. 정의: 짝 덮개 (고정 단체를 피하는 등변 분할)
- **정의.** $X$ 의 짝 덮개는 열린 집합 $W_1,\dots,W_m$ 으로, $W_j\cap\sigma W_j=\emptyset$ 이고 $X=\bigcup_j(W_j\cup\sigma W_j)$.
- 인덱스는 $(j,+)\leftrightarrow W_j$, $(j,-)\leftrightarrow\sigma W_j$, 대합 $\pi(j,\pm)=(j,\mp)$.
- **고정 단체 회피:** $W_j\cap\sigma W_j=\emptyset$ 이므로 nerve 의 어떤 단체도 $(j,+)$ 와 $(j,-)$ 를 함께 갖지 않는다. COMPLEX-3 §3 의 문제 (단체 $\{(i,1),(i,2)\}$ 의 자기 대합) 가 정의상 사라진다.
- 층: **층 1 (덮개).**

## 2. 한 단계 스케치 (F)
- nerve $N$ 의 단체는 각 $j$ 에서 부호를 최대 하나만 고른다. 따라서 $N\subseteq\partial\Diamond^m$ (교차다면체 경계, $\cong S^{m-1}$) 이고 $\pi$ 는 대척 작용 — 자유. $\dim N\le m-1$.
- 불변 분할 $\varphi$ 로 등변 nerve 사상 $f:X\to N\subseteq S^{m-1}$. 따라서 $\operatorname{ind}X\le m-1$, 즉 $\tau\le\iota\le m$. [증명 스케치]
- 역도 성립: $X\to S^{m-1}$ 등변이면 좌표 부호로 짝 덮개 $m$ 쌍을 얻는다. 따라서 **짝 덮개의 최소 쌍 수 = genus $\gamma(X)=\iota(G)$** [기억-미검증 표준 동치].
- 층: **층 2 (사상)** — 결합 규칙 R = 짝 덮개의 등변 nerve 사상.

## 3. 중첩성 k 와 상계 g(k)
- 짝 덮개의 겹침 차수는 $\le m$ (각 점은 쌍마다 최대 한쪽에만 속함). 따라서 겹침 차수/nerve 차원으로 묶이는 것은 정확히 **쌍 수 $m$ = genus** 이고, $g(m)=m$: $\tau\le m$. 층: **층 3 (지수).**
- **블록 구성 (G).** 블록 $V_1,\dots,V_k$ 의 열린 덮개 $U_i$ (R09: 지지집합이 $V_i\times\{1,2\}$ 와 만남) 는 각 $U_i$ 가 블록 복합체 $X_i=B_0(G[V_i])$ 로 등변 레트랙트. genus 의 단조성 ($\gamma(U_i)\le\gamma(X_i)$) 과 **부분가법성** $\gamma(A\cup B)\le\gamma(A)+\gamma(B)$ [기억-미검증, Krasnosel'skii] 로
  $$\tau(G)\le\iota(G)=\gamma(X)\le\sum_i\gamma(X_i)=\sum_i\iota(G[V_i]).$$
  즉 각 블록의 짝 덮개 $m_i=\iota_i$ 쌍을 합쳐 $\sum m_i$ 쌍의 짝 덮개를 만든다. 층: **층 3.**
- 이것은 R08-researcher1 §1, R09-researcher2 §1 의 ι 부분가법과 같은 정리다 (아래 §5 정정 참고).

## 4. 비교 (C): χ 색 논법 4k 보다 나은가
- 평면 블록: 색칠 $B_0(H)\to S^{\chi(H)-1}$ 이 있으므로 $\iota_i\le\chi_i\le4$. 따라서 (G) 의 상계는 $\le4k$. 최악 경우는 $K_{4k}$ ($\tau=4k$) 에서 같아 **함수 $g(k)$ 로서는 개선 없음** ($g(k)=4k$).
- **패턴별·블록별로는 엄밀히 나을 수 있다:** $\iota_i<\chi_i$ 인 블록이면 개선. 예: zig≤3 블록은 $\iota\le\operatorname{zig}\le3$ (R14 사슬) 이므로 $\chi=4$ 인 $C_{10}^2$ 류 블록에서 블록당 1 씩 줄어든다 (R16-r1 의 $\mathcal C_3$ 관찰과 일치). 단 $\iota_i<\chi_i$ 인 **평면** 블록이 존재하는지는 이 문서에서 판정하지 않았다 (평면 $\overline{C_7}$ 류는 아님: $\overline{C_7}$ 은 비평면).
- 판정: (G) 는 χ 논법과 같은 최악 상계 4k, 블록의 ι<χ 이면 개선. 층: **층 3 (지수 비교).**

## 5. 정정 (중요): R11 반례와 내 R12 철회의 재판정
- **R11-researcher2 §4 의 반례는 성립하지 않는다.** 집합 $U$ = 경도 띠 $(-10^\circ,100^\circ)$ (전 위도) ∪ 북극 근방, $-U$ = 띠 $(170^\circ,280^\circ)$ ∪ **남극 근방**. 띠 $U$ 는 전 위도를 포함하므로 남극 근처 (경도 $-10^\circ\sim100^\circ$) 의 점을 포함하고, 이 점들은 $-U$ 의 남극 근방에도 들어간다. 따라서 $U\cap(-U)\ne\emptyset$ 이고 $A=U\cup-U$ 는 서로소 합이 아니다 — "$\operatorname{coind}A=0$" 의 전제 (A→S^0) 가 깨진다. [증명, 집합 계산]
- 따라서 덮개 논법 자체 (genus/ind 부분가법) 는 표준 정리대로 유효하다. 내가 R12 에서 "이 반례를 넣으면 기수 사상 $S^2\to S^1$ 이 나와 모순" 이라 한 것은 **반례의 오류에서 온 모순** 이었다.
- **그러나 내 R08-P1 ($\tau\le\sum\tau_i$) 은 여전히 틀렸다.** 원인은 다른 곳이다: 덮개 논법은 사상 $X\to S^n$ 을 합치므로 **ind (=ι)** 를 묶는다. 나는 R08 에서 "coind ≤ n ⇔ X→S^n" 으로 써서 coind 와 ind 를 혼동했다. 올바른 결론은 $\tau\le\iota\le\sum\iota_i$ 이며, $\tau\le\sum\tau_i$ (J) 는 열려 있다. R09-researcher2 의 판정 ("ι 판으로만 증명된다") 이 옳다.
- **READ-researcher3 §2 항목 3 철회:** 나는 R08-r1/R09-r2 의 ι 부분가법이 "R11 반례 때문에 독립 검증 필요" 라고 썼다. R11 반례가 무효이고 genus 부분가법이 표준이므로 이 의심은 근거가 없다. 철회한다 (genus 부분가법 자체는 [기억-미검증]).
- 층: **층 2–3 (사상과 지수의 정의 구분).**

## 6. 결과 줄 (복잡성 환원의 어느 층)
- 짝 덮개 정의 (§1): 층 1 — 고정 단체 없는 덮개.
- (F) 자유 nerve ⇒ $\tau\le m$ (§2): 층 2 — 결합 규칙 = 짝 덮개의 등변 사상.
- (G) $\tau\le\sum\iota_i$ (§3): 층 3 — 블록 중첩의 genus 합.
- (C) 4k 와 같은 최악, ι<χ 블록에서 개선 (§4): 층 3 비교.
- R11 반례 무효, R08 오류의 진짜 원인 (§5): 층 2–3 정의 구분.

## 7. 후속연구 지점
1. **ι<χ 인 평면 블록의 존재 (우선순위 1).** 이유: (C) 의 개선이 평면 시트에서 실제로 일어나는지 결정. 시작: 평면 4-색 그래프 중 $\iota\le3$ (즉 $B_0\to S^2$) 인 것이 있는지 정의 수준 점검. 4색 필요 평면 그래프는 $K_4$ 마이너를 가지며 τ≥? 를 확인.
2. **R11 정정의 오케스트레이터 재검증 요청 (우선순위 2).** 이유: J 의 상태 (열림) 는 바뀌지 않지만, "덮개 논법이 coind 에 대해 거짓" 이라는 STATUS·master 의 기록 근거가 무효다. 올바른 기록: "덮개 논법은 ind (ι) 를 묶고 coind (τ) 를 직접 묶지 않는다".
3. **coind 판 짝 덮개 (우선순위 3).** 이유: τ 자체의 부분가법 J 를 위해서는 $S^n\to X$ 방향의 결합이 필요하다. 시작: 블록별 $S^{a_i}\to X_i$ 를 조인으로 합칠 때 교차 면이 그 조인을 담는지 (완전 교차에서는 담음, R14 C2) 를 일반 교차에서 정의 수준으로 점검.
