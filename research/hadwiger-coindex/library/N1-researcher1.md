# [N1-researcher1] $\tau=\operatorname{zig}$ 반례 탐색: 반례 없음, 막는 구조는 "w 의 정수 승격"과 "사슬 상계"

- 작성자·라운드·유파: 논객 갑 (researcher1) / R05 제1초식 (블라인드 입론) / 반례·구성 중심.
- **다른 논객의 N1-*, N2-*, N3-* 파일은 읽지 않았다.** library 의 R01–R04 보고서·STATUS·problem 만 읽었다. 코드: rooms/researcher1/n1_*.py.

## 결론
**미결 (반례 구성 실패).** $\tau(G)<\operatorname{zig}(G)$ 인 그래프를 찾지 못했다. 세 방향을 시도했다: (a) 평면 Radon-free 배치가 순서 인증서보다 나은지, (b) 선형 순서가 아닌 위상적 상계(농도 개념 사슬의 차원, 그리고 원 $S^1$ 로의 등변사상의 정확한 판정법), (c) 소형 그래프에서 정확 계산. 어느 것도 $\tau<\operatorname{zig}$ 를 주지 않았고, $\tau\le3$ 수준에서는 "$\tau\le3\iff\operatorname{zig}\le3$" 이 소규모 전체에서 성립함을 정확한 판정으로 확인했다. 부산물: **$\tau(C_8^2)=3$** (R04 열린 문제 해결). 위상 쪽 상계를 주는 정확한 기준(정리 B)이 새 도구다.

## 증명 또는 구성

### 0. 설정
$\mathcal C$ = 두 변이 모두 비공집합인 닫힌 쌍 $(A,B)$ ($B=\mathrm{CN}(A)$, $A=\mathrm{CN}(B)$) 의 poset ($A$ 로 정렬; $(A,B)\mapsto(B,A)$ 가 순서 역전 대합 $\sigma$). $B(G)\simeq_{\mathbb Z_2}\Delta(\mathcal C)$, $B_0(G)\simeq_{\mathbb Z_2}\operatorname{susp}B(G)$ [기억-미검증: 표준 Galois 연결 논법과 R02/R03 에서 쓴 사실; 아래 정리 B·사슬 상계의 출발점]. $\sigma$ 는 단체에 자유 작용한다 [증명: 불변 단체는 $A_1\subseteq B_1$ 인 닫힌 쌍을 요구, 루프 없음].

### 1. 평면 Radon-free 배치는 순서 인증서를 못 이긴다 (소형에서)  [계산 확인, 근거 아님]
$d_R\le2$ 이려면 평면 점 배치에서 모든 극대 완전이분쌍의 두 껍질이 서로소여야 한다. $\operatorname{zig}\ge4$, $K_4$-없음, 연결, 정점 6–7 개인 모든 그래프(아틀라스, 17개 가량)에서 국소 탐색으로 그런 평면 배치를 찾지 못했다(모두 $W_5\subseteq G$ 이거나 같은 형태). 탐색 실패는 비존재 증명이 아니다. 이론적 이유: $C_4$-자유이면 조건은 "각 $v\notin\operatorname{conv}N(v)$" 뿐이라 정리 K 로 이미 $\operatorname{zig}\le3$ 이고, $W_{2k+1}$ 은 R04-r3 이 $d_R=3$ 증명. 일반 $d_R<\min\{d:Q_d\}$ 는 열려 있다.

### 2. 정리 B (정확한 판정): $\tau\le3$ 의 위상적 충분조건 [증명, (0) 가 [기억-미검증] 인 한도에서]
$X=B(G)$ 에 자유 대합이 있고 $Y=X/\mathbb Z_2$, $w\in H^1(Y;\mathbb Z_2)$ 를 덮개의 분류 클래스라 하자. 등변사상 $X\to S^1$ 이 있다 $\iff$ 사상 $Y\to S^1=RP^1$ 로 $w$ 가 당겨져 나온다 $\iff$ $w$ 가 $H^1(Y;\mathbb Z)$ 의 한 클래스의 mod 2 환원이다 ($[Y,S^1]=H^1(Y;\mathbb Z)$ 이고 $z\mapsto z^2$ 덮개의 당김은 mod 2 환원이 정한다) $\iff$ 정수 Bockstein $\beta(w)=0\in H^2(Y;\mathbb Z)$ $\iff$ $w$ 가 $H_1(Y;\mathbb Z)$ 의 꼬임부분군 위에서 0. 그러면 $\operatorname{coind}B(G)\le1$ 이고 $B_0\simeq\operatorname{susp}B$ 이므로 $\operatorname{coind}B_0\le2$, 즉 $\tau\le3$. 이 기준은 $Y$ 의 2-골격만 쓴다 (차원 무관).
**구현** (n1_bock.py): $\Delta(\mathcal C)/\sigma$ 의 셀 복합체(방향 부호 $(-1)^{k(k-1)/2}$ 포함), 코사이클 flip(간선이 두 시트를 잇는가) 의 Bockstein $\beta$ 를 정수 격자 소속 판정으로 검사. 양성 대조: $\overline{C_7}$ 에서 True, $K_4$·Grötzsch 에서 False, ℓ=3 인 연결 그래프 아틀라스(정점 4–7) 전체 511개에서 **(zig, Bockstein=0) 가 (2,T)12, (3,T)341, (4,F)158 로 완전히 갈린다** — $\operatorname{zig}\le3$ 과 $\tau\le3$ (정리 B 판정) 이 이 범위에서 일치. 무작위 정점 8–10 개 연결 그래프 중 $\operatorname{zig}\ge4$ 인 2429개 모두 Bockstein $\neq0$ (통계, 근거 아님). 반례(=zig$\ge4$, Bockstein=0)는 발견되지 않음.
**의미**: $\tau<\operatorname{zig}=4$ 인 반례는 $w$ 가 정수로 승격되는 $B(G)/\mathbb Z_2$ 를 요구한다. $H_1(Y;\mathbb Z)$ 에 $w$ 가 0 이 아닌 꼬임 원소가 없다는 것. 증명 방향(참)을 위해선 "이것이 $Q_2$ 를 낳는다"는 것을 보이면 된다.

### 3. 사슬 상계 $\tau\le\ell+1$ (선형이 아닌 위상 상계) 와 그 한계 [증명 (0) 한도]
$\ell$ = $\mathcal C$ 의 최장 사슬 길이이면 $\dim B(G)=\ell-1$, $\operatorname{coind}B\le\ell-1$, 따라서 $\tau\le\ell+1$. $K_n$ ($\ell=n-1$), $C_5$ ($\ell=2$), $K_2$ ($\ell=1$) 일치. 이 상계는 순서에서 나오지 않는다. 그러나 **정점 $\le7$ 의 모든 그래프(1245개)와 정점 8–9 의 무작위 400개에서 $\operatorname{zig}\le\ell+1$** (격차 $\ell+1-\operatorname{zig}\in\{0,1,2,3\}$ 전부 $\ge0$) [계산 확인, 근거 아님]. 즉 사슬 차원은 지금까지 zig 보다 나쁘다. $\operatorname{zig}\le\ell+1$ 이 정리이면 사슬 상계는 반례를 못 만든다(증명 시도: 닫힌 쌍의 사슬 길이를 순서의 교대 수로 바꾸는 단계에서 막힘 — 사슬의 $a_i$/$b_j$ 비인접성($j<i$)을 순서 위치로 옮겨야 하는데 선택이 쌍마다 달라 전역 순서가 안 나옴).

### 4. 부산물: $\tau(C_8^2)=3$ [증명 + 계산 확인]
순서 $(0,1,2,3,6,4,7,5)$ 에서 $C_8^2$ 의 **모든** 완전이분쌍(극대 아님 포함, 닫힘 코드와 무관하게 직접 열거)의 런 수 $\le3$. 따라서 $\operatorname{zig}\le3$, $\tau\le d_R+1\le3$, 삼각형이 있어 $\tau\ge3$: $\tau(C_8^2)=\operatorname{zig}(C_8^2)=3<\chi=4$. (R04 가 $\{3,4\}$ 로 둔 것의 해결; R04 의 "탐색한 순서들" 은 이 순서를 못 찾았던 것.)

## 약점 자가 진단
1. 정의 (0) 의 $B(G)\simeq\Delta(\mathcal C)$, $B_0\simeq\operatorname{susp}B$ 의 등변 동치는 기억·표준 논법이고 이 보고서에서 증명하지 않았다. 정리 B 의 "$\Rightarrow\tau\le3$" 와 사슬 상계는 이에 의존한다(양방향 일치 실험은 이 모델이 올바른 방향임을 시사하나 증명 아님).
2. $\operatorname{coind}B_0\le2$ 이면서 $\operatorname{coind}B\ge2$ 인 경우(현탁이 index 를 낮춤)는 정리 B 가 못 본다: 반례가 거기에 있을 수 있다. 이 방향 반례는 $\mathbb Z_2$-사상 $B_0(G)\to S^2$ 를 직접 줘야 한다.
3. 검증은 $\tau\le3$ vs $\operatorname{zig}\le3$ (d=2) 수준뿐이다. $d\ge3$ ($\tau\le4$, $S^2$ 로의 사상) 에서는 장애 이론이 훨씬 복잡해 판정기를 못 만들었다.
4. 정점 $\le7$ 연결 그래프의 일치는 근거가 아니다(연구 원칙). 상계 방향의 구조적 이유는 아직 일반 증명이 없다.
5. 평면 Radon 탐색은 국소 탐색이다. 실패는 증명이 아니다.

## 후속연구 지점
1. **$\tau\le3\Rightarrow Q_2$ (zig$\le3$) 의 증명 시도 (정리 B 를 출발점으로).** 왜: $d=2$ 가 첫 비자명 사례이고 정리 B 가 위상 쪽 조건을 정확한 대수 조건("$w$ 의 꼬임 위 0")으로 바꿔 준다. 시작: $w$ 가 꼬임에서 0 이면 $H_1(Y;\mathbb Z)$ 의 비꼬임 클래스로 순서를 만드는 방법(닫힌 쌍의 poset 의 선형 확장과 간선 방향). 난점: poset 선형 확장과 런 수의 연결; $K_4$-마이너/odd cycle 로의 대응.
2. **$\operatorname{zig}\le\ell+1$ 증명 또는 반례.** 왜: 사슬 상계가 순서 상계를 이기는지가 위상 쪽에서 가장 단순한 비순서 상계의 한계 판정. 시작: 닫힌 쌍의 poset 을 선형 확장해 정점 순서를 유도(정점 $v$ 를 $v\in A$ 인 최소 닫힌 쌍의 위치로). 난점: 쌍마다 다른 선택.
3. **$d=3$ 판정기:** $B(G)\to S^2$ 의 등변사상 존재 (2-골격의 Bockstein 다음 장애: $\mathbb Z_2$-Postnikov의 $k$-불변량, $H^3(Y;\pi_2 \text{꼬임})$). 왜: $\tau\le4<\operatorname{zig}$ 반례 탐색 확장. 난점: 계산 가능한 형태가 없음.
4. **현탁이 index 를 낮추는 경우(약점 2).** $B_0(G)\to S^2$ 이면서 $B(G)\not\to S^1$ 인 $G$ 를 찾는 것 — 반례의 가장 가능성 있는 위치. 시작: $B_0$ 의 2-골격의 직접 장애(위 Bockstein 을 $B_0$ 에 대해 $S^2$ 로 확장), 정점 $\le7$ 에서 모든 $\operatorname{zig}=4$ 그래프 대상.
5. **$d_R$ vs $\min\{d:Q_d\}$ 구조 정리.** 평면 배치에서 순서를 만드는 일반 절차(예: 배치의 한 점을 고른 각순서)와 그 실패 반례. 평면에서 $K_4$ 없음 + zig 4 인 그래프 족(정점 8–9)을 우선 점검.
