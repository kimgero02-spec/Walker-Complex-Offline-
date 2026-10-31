# [N1-researcher3] 판정 {STMT: τ=zig}: 위상 지표 사슬로의 환원, 조인 닫힘, 어긋남이 생길 수 있는 세 곳

- 작성자·라운드·유파: researcher3 (논객 병) / R05 제1초식(블라인드 입론) / 위상·구조 중심.
- **블라인드 확인**: `library/` 의 `N1-*`, `N2-*`, `N3-*` 파일은 열지도 읽지도 않았다. 읽은 것은 problem.md(앞부분), STATUS.md(R03·R04 인계, R05 계획), `SRC-steiner-2312.17130.md`, `R04-researcher1.md`(전문), R03·R04 판정 표와 보고서 중 `d_R`·Q_d 관련 줄(grep), 내 방의 이전 코드(`b0lib.py` 등). 이 라운드에서 R03·R04 보고서 전문을 모두 정독하지는 않았다.
- 코드(전부 내 방 `rooms/researcher3/`): `n1_q2.py`(Q₂ 판정), `n1_dr2.py`(평면 배치 탐색), `n1_w5.py`, `n1_rho.cpp`/`n1_rho1.cpp`(ρ=zig 정확 계산, 전 순열), `n1_circ.py`, `n1_circulant.py`.
- 규약: $B_0$, $\tau$, $\operatorname{zig}=\rho$ 는 problem.md·R04 명제 O 그대로. Steiner Figure 1 의 사슬은 문주님 지시에 따라 검증 없이 인용한다.

## 결론

**미결** (부분 결과로 **조인에 대해 조건부 닫힘**). 반례도 증명도 얻지 못했다. 얻은 것은 세 가지다. (1) STMT 는 "Steiner 그림 1 의 모든 위상 하한이 zig 와 같다"와 동치이고, 따라서 **모든 그래프에서 $\operatorname{coind}(B_0)=\operatorname{ind}(B_0)$ 이어야** 한다. 즉 STMT 가 깨질 수 있는 곳은 정확히 세 군데(coind↔ind, ind↔$d_R$, $d_R$↔zig)뿐이다. (2) 조인에 대해 $\tau(G+H)\ge\tau(G)+\tau(H)$, $\operatorname{zig}(G+H)\le\operatorname{zig}(G)+\operatorname{zig}(H)$ 를 증명했다. 그래서 간극 $\operatorname{zig}-\tau$ 는 조인에서 부가법적으로 **줄기만** 하고, $\tau=\operatorname{zig}$ 인 그래프의 조인은 다시 $\tau=\operatorname{zig}$ 이다. 이로써 $\tau(W_5)=4>\omega(W_5)=3$ 이 증명된다. (3) 무조건 (d) 는 막힌다. $\tau(K_1+G)=\tau(G)+1$ 의 상한이 $\operatorname{coind}(\Sigma X)\le\operatorname{coind}(X)+1$ 이라는 미지의 위상 사실에 걸리기 때문이다. 만든 모든 계산은 증명의 보조 또는 반례 탐색용이며 근거로 쓰지 않는다.

## 증명 또는 구성

### A. 환원: STMT 는 위상 지표 사슬 전체의 일치와 동치 [증명, Steiner 그림 1 인용]

사슬(그림 1 과 R04 부산물): 
$$\tau=\operatorname{coind}(B_0)+1\ \le\ \operatorname{ind}(B_0)+1\ \le\ d_R+1\ \le\ \operatorname{zig}.$$
첫 부등식은 정의, 둘째는 $d_R\le d$ 이면 분리 초평면들에서 $\mathbb Z_2$-사상 $B_0(G)\to S^{d}$ 가 나오기 때문(R04 인증서 건전성), 셋째는 R04-r2/r1 의 $d_R\le\operatorname{zig}-1$. (그림 1 의 $\operatorname{ind}(B_0)+1\le\operatorname{zig}$ 와도 일치.)
**명제 A.** STMT $\iff$ 모든 $G$ 에서 위 사슬의 네 값이 같다. 특히 STMT $\Rightarrow$ $\operatorname{coind}(B_0(G))=\operatorname{ind}(B_0(G))$ ($\forall G$). 
*증명.* 사슬이 단조 증가라 양 끝이 같으면 가운데도 같다. ∎
**따름.** $\operatorname{coind}(B_0(G))<\operatorname{ind}(B_0(G))$ 인 그래프 하나가 곧 STMT 의 반례다 (그때 $\tau<\operatorname{ind}(B_0)+1\le\operatorname{zig}$). 마찬가지로 $\operatorname{ind}(B_0)+1<d_R+1$ 이거나 $d_R+1<\operatorname{zig}$ 인 그래프도 반례다. 세 간극 중 하나라도 열리면 거짓이다.

### B. 순서 쪽과 위상 쪽을 같은 틀에 놓기 (구조 설명, (c)) [증명]

R04 §9(보조정리 G′)에 따라, 선형순서 $\sigma$ 와 $d\ge1$ 에 대해 모멘트 사상 $g^\sigma_d:B_0(G)\to\mathbb R^{d+1}$ 은 $\mathbb Z_2$-사상이고 영점은 "런 수 $\ge d+2$ 인 극대 완전이분쌍"에서만 생긴다. 따라서
$$\operatorname{zig}(G)\le d+1\iff \exists\sigma:\ g^\sigma_d\ \text{가 영점이 없다}\ (\text{즉 }B_0\to S^d\text{ 인 "모멘트형" }\mathbb Z_2\text{-사상이 있다}).$$
반면 $\operatorname{ind}(B_0)\le d\iff$ **임의의** $\mathbb Z_2$-사상 $B_0\to S^d$ 가 있다. 그러므로 $\operatorname{zig}$ 는 "모멘트형 사상만 허용한 지수"이고 $\operatorname{ind}$ 는 "모든 사상을 허용한 지수"이다. $\tau\le\operatorname{zig}$ 가 쉬운 이유: $\operatorname{coind}(B_0)\ge d+1$ 이면 $S^{d+1}\to B_0$ 와 $B_0\to\mathbb R^{d+1}\setminus0$ 의 합성이 Borsuk–Ulam 에 걸려 영점이 생긴다. 이 논법은 **어떤 사상이든** 영점을 가지게 하므로 사용하는 위상 정보는 coindex 뿐이다. 역방향(STMT)이 요구하는 것은 반대 방향의 "표현 정리"이다: 아무 사상 $B_0\to S^d$ 가 있으면 모멘트형 사상도 있다. 연결성에서 지그재그를 읽는 Simonyi–Tardos 논법(`[기억-미검증]`, 원문 없음)은 정확히 이쪽(위상 → 모든 진색칠의 지그재그)이며, 그것이 우리가 아는 방향이다. 순서에서 위상을 읽는 방향의 반대(위상 → 순서)는 어디에도 증명이 없다. 이것이 STMT 의 본질이다.
**$d=1,2$ 에서 상태.** $d=1$: $\operatorname{ind}(B_0)\le1\iff$ 이분 $\iff\operatorname{zig}\le2$ [증명, R02: $d_R\le1\iff$ 이분, $\tau\ge3$ 비이분]. $d=2$: "$\mathbb Z_2$-사상 $B_0\to S^2$ 가 있으면 $\operatorname{zig}\le3$" 가 첫 비자명 경우이고, 이는 "$\operatorname{ind}(B_0)\le 2 \Rightarrow$ 길이 4 교대 사이클 $x_1<x_2<x_3<x_4$ (간선 12,23,34,14) 를 피하는 순서가 있다" 와 같다 (런 수 $\ge4$ 인 쌍은 그 안에 교대 4-사이클 $K_{2,2}$ 를 품기 때문). 증명하지 못했다. 알려진 충분조건은 $K_4$-마이너-자유(R04-r2)뿐이고, $\overline{C_7}$ 처럼 $K_4$ 마이너가 있어도 성립하는 경우는 개별 구성이다.

### C. 조인: 닫힘과 부가성 [증명]

**보조정리 C1.** $B_0(G+H)=B_0(G)*B_0(H)$ (심플리셜 복합체로서의 조인, $\mathbb Z_2$ 는 대각 작용). 
*증명.* $G+H$ 의 완전이분쌍 $(A,B)$ 는 $A=A_G\cup A_H$, $B=B_G\cup B_H$ 로 쓰이고, 가로지르는 쌍은 모두 간선이므로 조건은 $A_G\times B_G\subseteq E(G)$, $A_H\times B_H\subseteq E(H)$ 뿐이다(한 변이 공집합이어도 됨). 이것이 조인의 단체 정의 $\sigma\cup\tau$ ($\sigma\in B_0(G)\cup\{\emptyset\}$, $\tau\in B_0(H)\cup\{\emptyset\}$)와 같다. 교환 작용은 성분마다 교환이다. ∎

**정리 C2 (τ 의 초가법성).** $\tau(G+H)\ge\tau(G)+\tau(H)$. 
*증명.* $\mathbb Z_2$-사상 $S^a\to B_0(G)$, $S^b\to B_0(H)$ ($a=\operatorname{coind}B_0(G)$, $b=\operatorname{coind}B_0(H)$) 의 조인은 $S^a*S^b\cong S^{a+b+1}$ (대각 대척 작용) 에서 $B_0(G)*B_0(H)$ 로의 $\mathbb Z_2$-사상이다. 따라서 $\operatorname{coind}B_0(G+H)\ge a+b+1$, 즉 $\tau(G+H)-1\ge(\tau(G)-1)+(\tau(H)-1)+1$. ∎

**정리 C3 (zig 의 준가법성).** $\operatorname{zig}(G+H)\le\operatorname{zig}(G)+\operatorname{zig}(H)$ (간선 없는 그래프는 $\operatorname{zig}=1$ 로 둔다). 
*증명.* $\rho$ 로 쓴다 (R04 명제 O). $\sigma_G$, $\sigma_H$ 최적 순서를 이어 붙인 순서 $\sigma$ 를 쓴다. $G+H$ 의 극대 완전이분쌍 $(A,B)$ (양변 비공집합) 에서 $B_G\ne\emptyset$ 이면 $A_G$ 는 $B_G$ 의 $G$ 안 공통이웃 전체이고 $B_G$ 도 $A_G$ 의 공통이웃 전체이므로 $(A_G,B_G)$ 는 $G$ 의 극대쌍이다. $A_G\ne\emptyset$ 일 때도 대칭. 어느 한 변이 $G$ 쪽에서 공집합이면 다른 변이 $V(G)$ 전체이므로 $G$ 쪽 런은 1. 어느 경우든 $G$-쪽 런 수 $\le\rho(G)$, $H$-쪽도 마찬가지, 이어 붙인 순서의 런은 두 부분 합 이하이다. ∎

**따름 C4.** $\tau(G)=\operatorname{zig}(G)$ 이고 $\tau(H)=\operatorname{zig}(H)$ 이면 $\tau(G+H)=\operatorname{zig}(G+H)=\tau(G)+\tau(H)$. 
*증명.* $\tau(G)+\tau(H)\le\tau(G+H)\le\operatorname{zig}(G+H)\le\operatorname{zig}(G)+\operatorname{zig}(H)=\tau(G)+\tau(H)$. ∎
**간극 부가성.** $\operatorname{gap}(G):=\operatorname{zig}(G)-\tau(G)\ge0$ 이면 $\operatorname{gap}(G+H)\le\operatorname{gap}(G)+\operatorname{gap}(H)$. 조인으로는 간극을 만들 수 없다.

**(d) 의 답.** 
- $K_1$: $B_0(K_1)=S^0$, $\tau(K_1)=1=\operatorname{zig}(K_1)$. 따라서 $\tau(K_1+G)\ge\tau(G)+1$ (무조건) 이고 $\operatorname{zig}(K_1+G)\le\operatorname{zig}(G)+1$ (무조건). 
- 조건부: $\tau(G)=\operatorname{zig}(G)$ 이면 $\tau(K_1+G)=\operatorname{zig}(K_1+G)=\tau(G)+1$. 
- **무조건 등식은 증명 못 함**, 막힌 지점은 둘이다. (i) $\tau(K_1+G)\le\tau(G)+1$ 은 $\operatorname{coind}(\Sigma X)\le\operatorname{coind}(X)+1$ ($X=B_0(G)$, $\Sigma$ = 자유 현탁 $=*S^0$) 과 같다. $\operatorname{ind}$ 는 $\operatorname{ind}(\Sigma X)\le\operatorname{ind}X+1$ 이 알려져 있어 $\operatorname{coind}=\operatorname{ind}$ 일 때만 닫힌다 (`[기억-미검증]`, Matoušek). (ii) $\operatorname{zig}(K_1+G)\ge\operatorname{zig}(G)+1$ 은 순서만으로는 증명하지 못했다. 최악 쌍이 $v$ 의 삽입 위치에서 런 경계에 걸리면 $v$ 가 런을 늘리지 않을 수 있어서이다 (내가 시도한 회전·반전 논법은 병목이 짝수 길이 지그재그에서 남는다). 흥미로운 역: $\operatorname{zig}(K_1+G)\le\operatorname{zig}(G)$ 인 $G$ 가 있다면 그것 자체가 $\tau(G)<\operatorname{zig}(G)$ 인 반례이다 (대우: $\tau(G)=\operatorname{zig}(G)$ 이면 $\operatorname{zig}(K_1+G)=\operatorname{zig}(G)+1$). 이것은 **탐색 가능한 반례 신호**이다. 정점 $\le6$ 인 모든 그래프 207개에서 $\operatorname{zig}(K_1+G)=\operatorname{zig}(G)+1$ 이었다 (`n1_rho.cpp`, 전 순열 정확 계산) — 이것은 근거가 아니라 탐색에서 신호가 안 나왔다는 기록이다.
- $d_R(K_1+G)\le d_R(G)+1$ [증명]: $G$ 의 배치를 초평면 $\{x_{d+1}=0\}$ 에 두고 $v=(0,\dots,0,1)$. $v$ 를 포함한 쪽의 볼록 껍질과 초평면의 교점은 $v$ 없는 쪽 껍질뿐이므로 분리가 보존된다.

**$\tau>\omega$ 인 작은 그래프** [증명]. $\tau(C_5)=3$ (R01 이래 [증명]), $\tau(K_1)=1$ 이므로 정리 C2 로 $\tau(W_5)=\tau(K_1+C_5)\ge4$. 상한은 R04 $d_R(W_5)=3$ ($\tau\le d_R+1=4$) 또는 $\chi=4$. 따라서 **$\tau(W_5)=4>3=\omega(W_5)$**, 6 정점 그래프로서 $\tau>\omega$ 의 최소급이다 (5 정점 이하는 $\tau>\omega$ 가 없는지는 확인하지 않았다). 더 일반으로 홀수 사이클들의 조인 $C_{2k_1+1}+\cdots+C_{2k_r+1}$ 은 $\tau=\operatorname{zig}=\chi=3r>2r=\omega$ ($\tau\ge3r$ 은 C2, $\chi\le3r$). $C_5+C_5$ ($n=10$, $\omega=4$, $\tau=6$) 가 그 예이다. STMT 는 조인에 대해 닫히므로 $\{K_1\}$, 간선 없는 그래프, 이분 그래프, 홀수 사이클, $C_n[K_m]$ ($n\ge5,m\ge2$), $K_{p/q}$ 들의 모든 조인에서 성립한다.

### D. 위상 값을 정확히 아는 족에서 zig 와 비교

**D1. 순환 그래프 $K_{p/q}$** ($i\sim j\iff q\le|i-j|\le p-q$). zig 는 전 순열 정확 계산 (`n1_rho1`), 하한은 $\omega$, 홀수 사이클 포함 여부, 그리고 $B_0$ 의 $\mathbb Z_2$ 계수 호몰로지 연결도(`b0lib.tau_h`, [계산 확인]).
| $(p,q)$ | $\omega$ | zig (정확) | $\tau$ 하한 | 결과 |
|---|---|---|---|---|
| (5,2)=$C_5$ | 2 | 3 | 3 | $\tau=\operatorname{zig}$ |
| (7,2)=$\overline{C_7}$ | 3 | 3 | $\omega=3$ | $\tau=\operatorname{zig}=3<\chi=4$ [증명] |
| (10,3) | 3 | 3 | $\omega=3$ | $\tau=\operatorname{zig}=3$ [증명] |
| (11,3) | 3 | 3 | $\omega=3$ | $\tau=\operatorname{zig}=3$ [증명] |
| (8,3), (11,4) | 2 | 3 | 비이분 ⇒ 3 | $\tau=\operatorname{zig}=3$ [증명] |
| (9,2)=$\overline{C_9}$ | 4 | 5 | $\tau_h=5$ | $\tau=\operatorname{zig}=5$ — 하한은 Z₂ 호몰로지 연결도에서 온 것으로, 연결도→coind 를 쓰려면 단순연결 확인이 필요해 [기억-미검증] |
어긋남 없음. 특히 $\tau>\omega$ 인 $\overline{C_9}$ 가 하나 더 확보됨 (조건부).
**D2. 안정/Schrijver, Kneser, Borsuk.** $\tau=\chi$ 이고 zig 가 $\tau$ 와 $\chi$ 사이에 끼므로 자동 등호 (알려진 사실의 재진술, 새로운 것 없음).
**D3. 소형 전수 신호 (근거 아님)**: 연결·$K_4$-자유·$\le7$ 정점 아틀라스 그래프 중 $\operatorname{zig}\ge4$ (Q₂ 위반) 는 13 개. 11 개는 $W_5$ 를 부분그래프로 품고 (따라서 $\tau\ge4$ 증명됨, C2 와 단조성), 나머지 2 개(아틀라스 1005, 1104) 는 $W_5$-자유인데 $\tau_h=4$ (호몰로지 하한). 13 개 모두 휴리스틱 평면 배치 탐색(`n1_dr2.py`; 평면 분리 조건은 "정점이 이웃 3 개의 삼각형 밖" + "4-사이클 대각선 비교차" 로 환원됨 — $d=2$ 에서 Radon 쌍은 크기 $\le4$ 로 충분) 에서 배치를 못 찾았다. 정점 $8$–$11$ 의 $K_4$-자유·비이분 순환 그래프에서는 Q₂ 위반이 하나도 없었다. 모두 비존재 증명이 아니므로 결론에 쓰지 않는다.

### E. 어디서 어긋날 수 있나 (구조적 후보 목록)

1. **G1 (coind↔ind)**: 일반 $\mathbb Z_2$-공간에서는 $\operatorname{coind}<\operatorname{ind}$ 가 있다. 예: 비가향 종수 3 곡면 $N$ 의 가향 이중피복 $K$ (종수 2 곡면) 는 $\pi_1(N)$ 이 꼬임 없음 때문에 $S^2\to K$ 등변사상이 없고 ($\operatorname{coind}K=1$), $w^2\ne0$ 이라 $\operatorname{ind}K\ge2$ (스티펠–휘트니 높이) [증명 스케치, 표준 사실 `[기억-미검증]`]. 현탁 $\Sigma K$ 에서 $w^3\ne0$ 도 갱신식 Gysin 열로 계산되어 $\operatorname{ind}(\Sigma K)=3$ 임을 얻었다 (세부 오류 가능, `[기억-미검증]` 수준). 그러나 $\operatorname{coind}(\Sigma K)$ 가 2 인지 3 인지는 **결정하지 못했다**: $\pi_2(\Sigma K)=H_1(K)$ 에서 $H^3(\mathbb{RP}^3;\pi_2)$ 의 장애류를 계산해야 한다. 또 이 $\Sigma K$ 가 어떤 그래프의 $B_0$ 로 나타나는지는 Csorba "모든 자유 $\mathbb Z_2$-복합체는 어떤 상자복합체의 현탁과 Z₂-호모토피 동치" `[기억-미검증]` 에 의존한다. 두 가지가 모두 성립하면 STMT 는 거짓이다. 이것이 내가 본 **가장 구체적인 반례 후보**이다 (미완결).
2. **G2 (ind↔$d_R$)**: $\mathbb Z_2$-사상 $B_0\to S^d$ 가 분리 초평면 배치에서 오는 것인지. 사상이 단체선형이 아니면 점 배치로 바꿀 수 없을 수 있다. 정보 없음.
3. **G3 ($d_R+1$↔zig)**: 평면 배치(비볼록 위치)는 볼록 곡선(=순서)보다 풍부하다. Q₂ 위반이면서 $d_R\le2$ 인 그래프를 찾으면 반례. 위 탐색에서 소형엔 없었다.

## 약점 자가 진단

- 판정은 **미결**이다. 가장 큰 구멍은 E.1: $\operatorname{coind}(\Sigma K)$ 의 값과 Csorba 보편성이다. 둘 다 `[기억-미검증]` 이거나 계산 미완. 이것이 풀리면 STMT 가 결정된다 (거짓이 될 가능성이 현재로서는 더 커 보이나, 근거가 약해 추측으로만 둔다 `[추측]`).
- 명제 A 는 Steiner 그림 1 의 $\operatorname{ind}(B_0)+1\le\operatorname{zig}$ 와 우리 증명($d_R$ 사슬)에 의존한다. 후자는 R03·R04 에서 재도출되었지만 나는 이 라운드에서 다시 쓰지 않고 인용했다.
- C3 의 증명에서 "극대쌍의 $G$-쪽 제한도 극대쌍" 논법을 한 번 점검했을 뿐 독립 재검증은 없다. 공집합 쪽 처리($\rho$ 정의의 퇴화 경우)가 가장 위험한 줄이다.
- D1 의 (9,2) 하한은 호몰로지 연결도라서 coindex 하한으로 올리는 단계 (단순연결+Hurewicz) 를 증명하지 않았다.
- (d) 의 두 막힌 지점 (i)(ii) 는 그대로 열려 있다. $\operatorname{zig}(K_1+G)\ge\operatorname{zig}(G)+1$ 을 순서만으로 증명하려던 시도는 짝수 길이 지그재그에서 실패했다.
- 평면 배치 탐색은 임의 재시작 지역 탐색이라 "없다"는 증거가 못 된다.

## 후속연구 지점

1. **$\operatorname{coind}(\Sigma K)$ 결정 (E.1)** — 무엇: $K$ = 종수 2 곡면과 (비가향 종수 3 곡면의 이중피복) 자유 대합에서 $\operatorname{coind}(K*S^0)$ 이 2 인지 3 인지, 그리고 $K*S^0$ 가 어떤 $B_0(G)$ 와 Z₂-호모토피 동치인지. 왜: 맞으면 STMT 거짓 (명제 A 의 따름). 시작: $\pi_2=H_1(K)$ 계수 $H^3(\mathbb{RP}^3;\pi_2)$ 의 등변 장애이론 계산, $Q=\Sigma K/\mathbb Z_2$ 가 $N$ 에 $K$ 위의 원뿔을 붙인 것임을 이용. 병행해 Csorba 보편성의 문헌 확인(요청). 난점: 장애류의 선택(2-골격 단면)에 대한 의존, 그래프 실현의 구체적 구성.
2. **$d=2$ 첫 비자명 경우**: "$\mathbb Z_2$-사상 $B_0\to S^2$ 가 있으면 교대 4-사이클을 피하는 순서가 있다" — 무엇: $\operatorname{ind}(B_0)\le2\Rightarrow\operatorname{zig}\le3$ 의 증명 또는 반례. 왜: 위상→순서 방향의 가장 작은 시험, $K_4$-마이너-자유(증명됨)와 $\overline{C_7}$(개별)을 포괄해야 한다. 시작: $\operatorname{ind}(B_0)\le 2$ 인 그래프의 구조(예: $K_{2,3}$ 와 $K_{3,3}$ 부분의 사용 방식), 정점 8–9 에서 Q₂ 위반이면서 $\tau_h\le3$ 인 그래프 탐색. 난점: $\tau_h$ 는 하한뿐, 상한 증명은 사상 구성 필요.
3. **$\operatorname{zig}(K_1+G)\ge\operatorname{zig}(G)+1$ 의 순서 증명** — 무엇: 임의 순서에서 $v$ 가 런 경계에만 놓이는 경우를 다른 쌍으로 우회. 왜: 성립하면 (d) 의 zig 쪽이 무조건 닫히고, 깨지면 반례 (본문 대우). 시작: 짝수 길이 지그재그에서 어긋나는 최소 구조를 `n1_rho` 로 정점 $\le 7$ 에서 찾기. 난점: 조합적 구조가 아직 불명.
4. **G3 평면 배치 반례 탐색의 체계화** — 무엇: Q₂ 위반이면서 평면 분리 조건(정점이 이웃의 볼록 껍질 밖, 4-사이클 비교차)을 만족하는 그래프. 왜: 증명된 $d_R+1\le\operatorname{zig}$ 의 엄격성 여부. 시작: SAT/순서형(order type)으로 평면 배치를 정확히 결정, 소형 그래프 족(바퀴 변형, 모저 스핀들 계열) 시험. 난점: 평면 점 배치의 조합적 표현.
5. **조인 이외의 닫힘 연산**: Mycielskian, 블로업 $G[K_m]$, 분리합. 무엇: $\operatorname{gap}$ 이 이 연산들에서 어떻게 변하는지. 왜: 조인은 간극을 만들지 못했으므로 간극이 생긴다면 다른 연산에서다. 시작: Mycielski 의 $B_0$ 현탁 관계(`[기억-미검증]`) 와 $\rho$ 의 대응, $G[K_m]$ 은 R04 정리 3 의 틀 재사용. 난점: 위상 쪽 정확값을 알기 어렵다.

## 문주님께 요청
- (있으면 좋음, 긴급도 낮음) Csorba, *Homotopy types of box complexes* (Combinatorica 2007) 의 "모든 자유 Z₂-복합체가 상자복합체로 실현된다"는 정리의 정확한 진술(현탁이 필요한지 여부). 없을 때의 대안: 후속연구 1 을 위상 쪽(coind 계산)만으로 진행하고 실현 가능성은 `[기억-미검증]` 로 둔다.
