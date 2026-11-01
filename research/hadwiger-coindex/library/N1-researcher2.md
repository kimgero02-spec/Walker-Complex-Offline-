# [N1-researcher2] $\tau=\operatorname{zig}$ 증명 시도: 부분 증명, 호-라벨 보조정리, 새 예 $\tau(C_{11}^3)=5$

- 작성자·라운드·유파: researcher2 (논객 을) / 라운드 5 제1초식(블라인드 입론) / 증명 중심(조합·순서). 코드: rooms/researcher2/n1_*.py.
- **블라인드 준수**: 이 입론을 쓰는 동안 library/ 의 N1-*, N2-*, N3-* 파일은 읽지 않았다(디렉터리 목록에 다른 논객 파일이 보였을 뿐 내용은 열지 않았다). 읽은 것은 problem.md, STATUS.md, R03-researcher2, R04-researcher1, SRC 노트 일부.
- 인용 규칙: Steiner·Norin–Steiner 의 정리는 검증된 결과로 인용만 한다(Steiner 그림 1 의 사슬 $\operatorname{zig}\ge\operatorname{Xind}(\operatorname{Hom}(K_2,G))+2\ge\dots\ge\tau$).

## 결론

**미결 (조건부 부분 결과 있음).** 일반 $G$ 에 대한 $\tau\ge\operatorname{zig}$ 증명은 얻지 못했고, 반례도 얻지 못했다. 증명한 것: (1) $\tau,\operatorname{zig}$ 는 준동형에 단조이므로 코어 불변량이다. (2) 등식이 성립하는 그래프의 족은 조인(join)과 서로소 합집합에 대해 닫힌다. (3) $\operatorname{zig}\le3$ 이면 $\tau=\operatorname{zig}$ (따라서 첫 반례는 $\tau=3<\operatorname{zig}$ 꼴이어야 한다). (4) $\tau(C_8^2)=3$ (R04 의 열린 문제 해결), 그리고 $\omega<\tau<\chi$ 인 첫 그래프 $C_{11}^3$ ($\tau=5$). (5) 진술을 둘로 쪼갠다: (I) 순수 조합 보조정리 "부호 호-라벨 $k$ 색 $\Rightarrow$ 런 수 $\le k+1$ 인 순서" 와 (II) "$\mathbb Z_2$-사상 $\Rightarrow$ 호-라벨". (I) 은 $k=1$ 에서 증명, $k=2,3$ 에서 정점 $\le7$ 이면 성립(SAT, 소규모). (II) 가 진짜 장애물이며 아래에 정확히 적는다.

## 증명 또는 구성

### 0. 표기
$B_0(G)$, $\tau=\operatorname{coind}B_0(G)+1$, $\operatorname{zig}=\rho$ (R04 명제 O: 선형 순서에서 극대 완전이분쌍의 라벨 런 수의 최댓값을 순서에 대해 최소화). 알려진 사슬 $\tau\le d_R+1\le\operatorname{zig}\le\chi$ [증명, 우리 것]. "$k$-연결 자유 $\mathbb Z_2$-공간은 $\operatorname{coind}\ge k+1$" [증명, 표준 사실(Matoušek 5.3), R02·R03 에서 사용].

### 1. 정리 1 (준동형 단조, 코어 불변) [증명]
$f:G\to H$ 준동형이면 $\tau(G)\le\tau(H)$ 이고 $\operatorname{zig}(G)\le\operatorname{zig}(H)$. 따라서 $G$ 와 준동형 동치인 그래프(특히 코어)는 같은 $\tau,\operatorname{zig}$ 를 가진다.
*증명.* $\tau$: $f$ 는 면 $(A,B)$ 를 면 $(f(A),f(B))$ 로 보내는 $\mathbb Z_2$-단체사상 $B_0(G)\to B_0(H)$ 를 주고($A\times B\subseteq E(G)\Rightarrow f(A)\times f(B)\subseteq E(H)$), $\mathbb Z_2$-사상의 합성이므로 coind 가 단조. $\operatorname{zig}$: $H$ 의 진색칠 $c$ 와 그 최대 지그재그 길이를 $L$ 이라 하자. $c\circ f$ 는 $G$ 의 진색칠이다. $G$ 의 $c\circ f$-지그재그 $z_1,\dots,z_k$ (색 증가, 홀·짝 번째 집합이 서로 완전) 의 상 $f(z_i)$ 는 $c$-색이 증가하므로 서로 다른 점이고, 홀·짝 상이 $H$ 에서 서로 완전이므로 길이 $k$ 지그재그다. 따라서 $k\le L$. ∎
함의: 독립집합 블로업($G[\overline{K_m}]$)은 아무것도 바꾸지 않는다. 반례 후보는 코어여야 한다.

### 2. 정리 2 (조인) [증명]
(a) $B_0(G+H)\cong B_0(G)*B_0(H)$ ($\mathbb Z_2$ 대각 작용). (b) $\tau(G+H)\ge\tau(G)+\tau(H)$. (c) $\operatorname{zig}(G+H)\le\operatorname{zig}(G)+\operatorname{zig}(H)$. 따라서 $\tau=\operatorname{zig}$ 인 두 그래프의 조인도 $\tau=\operatorname{zig}$ 이고 값은 합이다.
*증명.* (a) $G+H$ 의 면 $(A,B)$ 는 $A=A_G\cup A_H$, $B=B_G\cup B_H$ 이고, $A\times B\subseteq E(G+H)$ 는 교차쌍이 자동으로 변이므로 $A_G\times B_G\subseteq E(G)$, $A_H\times B_H\subseteq E(H)$ 와 동치. 이는 두 복합체의 면의 합집합(공집합 허용)이다. (b) $S^a\to B_0(G)$, $S^b\to B_0(H)$ 가 등변이면 $S^a*S^b=S^{a+b+1}\to B_0(G)*B_0(H)$ 도 등변. 그래서 $\operatorname{coind}\ge(\tau(G)-1)+(\tau(H)-1)+1$. (c) $G$ 를 색 $1..m$, $H$ 를 색 $m+1..$ 로 최적 색칠한다. 색이 증가하는 지그재그에서 $V(G)$ 쪽 원소들이 앞 접두부, $V(H)$ 쪽이 뒤 접미부이며 각각 해당 그래프의 지그재그. 길이 합 $\le$ 합. 마지막 주장은 $\tau(G+H)\ge\tau(G)+\tau(H)=\operatorname{zig}(G)+\operatorname{zig}(H)\ge\operatorname{zig}(G+H)\ge\tau(G+H)$. ∎
**따름 2a.** 서로소 합집합: $\tau(G\sqcup H)=\max$ , $\operatorname{zig}(G\sqcup H)=\max$ (길이 $\ge2$ 지그재그는 연결) 이므로 등식 족은 서로소 합집합에도 닫힌다.
**따름 2b (새 예).** $J_r=\overline{C_7}+\dots+\overline{C_7}$ ($r$ 개): $\tau(\overline{C_7})=\operatorname{zig}(\overline{C_7})=3$ (R02·R03; 내 SAT 도 zig=3) 이므로 $\tau(J_r)=\operatorname{zig}(J_r)=3r$, 반면 $\chi(J_r)=4r$. 간극 $\chi-\tau=r$. 또 꼭짓점 하나를 더하는 연산(apex)은 둘 다 정확히 1 을 올린다. [증명]

### 3. 정리 3 ($\operatorname{zig}\le3$ 이면 등식) [증명, 조건: 홀수 순환의 $\tau=3$]
$\operatorname{zig}(G)\le3$ 이면 $\tau(G)=\operatorname{zig}(G)$.
*증명.* $\operatorname{zig}=1$: 변 없음, $\tau=1$. $\operatorname{zig}=2$: 런 3 금지(길이 3 교대 $a<b<a'$, $ab,ba'\in E$ 금지)이므로 순서에서 모든 정점이 소스 또는 싱크, 곧 이분이고 변이 있다. 변이 있으므로 $\tau\ge\tau(K_2)=2$, $\tau\le\operatorname{zig}$. $\operatorname{zig}=3$: 이분이 아니므로 홀수 순환 $C_{2j+1}\subseteq G$ 가 있고, $\tau(C_{2j+1})=3$ (R01–R03: $C_5$ 는 $B_0$ 가 단일연결로 계산 확인, 일반 홀수 순환은 표준 사실[이웃복합체 $\simeq S^1$]) 와 부분그래프 단조로 $\tau\ge3$. $\tau\le\operatorname{zig}$ 로 마무리. ∎
**함의.** 반례가 있다면 $\tau=3$ 이고 $\operatorname{zig}\ge4$ 인 코어에서 시작한다(어떤 반례도 $\tau\ge3$ 이고 $\operatorname{zig}\ge4$ 이므로 $\tau=3$ 이 최소 반례의 형태). 순서 언어로 $\operatorname{zig}\le3$ 는: $a<b<c<d$ 이면서 $ab,bc,cd,ad\in E$ 인 "볼록 4-순환" 이 없는 순서의 존재. 즉 **$\tau\le3\Rightarrow$ 볼록 4-순환 없는 순서가 존재하는가**가 진술의 가장 작은 비자명 사례다.

### 4. 구체 그래프 결과 [계산 확인; 3번은 정수 호몰로지를 쓰는 증명]
1. **$\tau(C_8^2)=3$** (R04 의 "$\{3,4\}$ 열림" 해결). 순서 $(0,1,2,3,6,4,7,5)$ 에는 $p<q<r<s$ 이면서 $pq,qr,rs,ps\in E(C_8^2)$ 인 네 점이 없다(70 개 4-부분집합 전수 확인, 독립 코드로 극대 완전이분쌍 18 개의 런 수 $\le3$ 도 확인). 그래서 $\operatorname{zig}\le3$, $\omega=3\le\tau\le\operatorname{zig}$. $\chi(C_8^2)=4$. R04 의 자연 순서 런 4 는 순서 선택의 문제였다.
2. Moser 방추: $\operatorname{zig}=3$ (SAT 순서), $\omega=3$ 이므로 $\tau=3<\chi=4$. Petersen: $\operatorname{zig}=3$. $C_{9}^2$: 3.
3. **$\tau(C_{11}^3)=5$, 따라서 $\omega=4<\tau=5<\chi$ ($\chi\ge\lceil11/2\rceil=6$).** 이것은 R03 에서 열려 있던 "$\omega<\tau<\chi$ 인 그래프" 의 첫 예다. 증명: (상한) 순서 $10,9,\dots,0$ 에서 극대 완전이분쌍 55 개의 런 수가 $\le5$ 이므로 $\operatorname{zig}\le5$, $\tau\le5$. (하한) $B_0(C_{11}^3)$ 은 면 5766 개, 정수 계수 기약 호몰로지 $\tilde H_j=0$ ($j\le3$; 경계행렬 $\partial_1..\partial_5$ 의 스미스 표준형에 비자명 소인수 없음, $\tilde H_4=\mathbb Z$), 기본군은 간선경로 삼각형 폐포 알고리즘으로 자명(176/176 간선). Hurewicz–Whitehead 로 3-연결, 따라서 $\operatorname{coind}\ge4$, $\tau\ge5$. 그래서 $\tau=\operatorname{zig}=5$. 같은 계산으로 $C_9^3=\overline{C_9}$ 는 $\tau=\operatorname{zig}=\chi=5$, $C_{10}^3$ 은 $\operatorname{zig}=4=\omega<\chi\ge5$ ($\tau=4$). 모두 $\tau=\operatorname{zig}$ 와 정합한다.

### 5. 정리 5 (호-라벨 보조정리) [증명] — 진술을 조합 문제로 바꾼다
$Q_k$ = $\{+,-,0\}^k\setminus\{0\}$ 에 부호 집합 포함 순서를 준 포셋(구면 $S^{k-1}$ 의 십자다면체 면 포셋), $P(G)=\{(A,B):A,B\ne\emptyset,A\times B\subseteq E\}$ ($\operatorname{Hom}(K_2,G)$ 의 세포 포셋). 다음은 동치다.
(i) 등변 포셋 사상 $f:P(G)\to Q_k$ ($f(B,A)=-f(A,B)$) 가 있다.
(ii) 호(방향 있는 변)의 라벨 $g:\{a\to b\}\to\{\pm1,\dots,\pm k\}$ 가 있어 $g(b\to a)=-g(a\to b)$ 이고, **4-워크 조건**: $ab,ab',a'b,a'b'\in E$ ($a=a'$ 또는 $b=b'$ 허용) 이면 $g(a\to b)\ne-g(a'\to b')$.
*증명.* (i)⇒(ii): 변 $\{a,b\}$ 마다 $f(\{a\},\{b\})$ 의 한 원소 $g(a\to b)$ 를 고르고 반대 방향에는 부호를 뒤집어 준다($f(\{b\},\{a\})=-f(\{a\},\{b\})$ 이므로 유효). 4-워크가 주어지면 $(\{a,a'\},\{b,b'\})\in P(G)$ 이고 $f$ 의 단조성으로 두 호의 라벨이 모두 $f(\{a,a'\},\{b,b'\})$ 의 원소인데, 부호 벡터는 반대 부호쌍을 갖지 않는다. (ii)⇒(i): $f(A,B)=\{g(a\to b):a\in A,b\in B\}$ 로 정의. 임의의 두 호 $a\to b$, $a'\to b'$ ($a,a'\in A$, $b,b'\in B$) 는 4-워크이므로 반대 부호쌍이 없어 $Q_k$ 의 원소이고, 단조·등변이 자명. ∎
[계산 확인] 이 동치를 $K_3,K_4,C_5,W_5,\overline{C_7},C_5[K_2]$ 에서 두 개의 독립 SAT(포셋 사상 / 호 라벨) 로 $k=1,2,3$ 일치 확인.
**의미.** $\xi(G):=\min\{k:$ 위 (i),(ii)$\}$ 라 하자. Steiner 그림 1 의 사슬에서 $\tau\le\xi+1\le\operatorname{zig}$ ($\xi+1=\operatorname{Xind}(\operatorname{Hom}(K_2,G))+2$, 정의 대응은 [기억-미검증], 위 SAT 에서 $K_3$(2), $K_4$(3), $C_5$(2), $W_5$(3), $\overline{C_7}$(2) 로 맞음). 따라서 **$\xi+1<\operatorname{zig}$ 인 그래프 하나가 곧 반례** ($\tau\le\xi+1<\operatorname{zig}$)이고, 이것은 SAT 로 결정 가능한 유한 점검이다. 점검한 이름 있는 그래프에서는 모두 $\xi+1=\operatorname{zig}$: $K_3,K_4,C_5,W_5,\overline{C_7},C_8^2,C_9^2$(3), Moser(3), Petersen(3), $C_5[K_2]$(4), $C_9^3$(5; $k=3$ 불가능, $k=4$ 가능). (근거로 쓰지 않는다; 반례가 안 나왔다는 기록이다.)
**구조.** $k=2$ 이면 라벨은 변을 두 색 $E_1\cup E_2$ 로 나누고 각 $E_i$ 가 $U_i\to D_i$ 이분 방향을 갖는 것이며, 조건은 "같은 색 두 변 $a\to b$, $b'\to a'$ 와 그 교차변 $ab',a'b$ (둘 다 반대 색) 가 4-순환을 이루지 않는다" 이다.

### 6. 분해와 증명 시도의 현황
진술 $\tau=\operatorname{zig}$ 는 $\tau\le\xi+1\le\operatorname{zig}$ 사슬에서 다음 둘의 합이다.
- **(I) [조합, 순서] $\xi+1\ge\operatorname{zig}$**, 즉 **보조정리 $L_k$: 호-라벨 $k$ 색이 있으면 모든 극대 완전이분쌍의 런 수가 $\le k+1$ 인 순서가 있다.**
 - $L_1$ [증명]: 각 정점의 호가 모두 같은 부호(별 조건)이므로 정점은 소스/싱크, 이분. 소스를 먼저 놓으면 런 $\le2$.
 - $L_2$, $L_3$: 정점 수 $\le7$ 이면 성립 [계산 확인]. 방법은 CEGAR(라벨 가능한 그래프 + "모든 순서에서 교대 패턴이 존재" 를 SAT 로 반복해서 반례를 찾는 것): $n=7,k=2$: UNSAT(64 회); $n=7,k=3$: UNSAT; 양성 대조군(삼각형, $K_4$) 은 SAT 로 나와 도구는 작동한다. $n=8,k=2$ 는 5분을 넘겨 중단(결론 없음). 소규모 정점 수의 유한 정리일 뿐 일반 증명이 아니다.
 - 일반 증명 시도: 한 색 $i$ 를 빼고 귀납(남은 호는 $k-1$ 색 라벨) 하여 순서 $\sigma'$ 를 얻은 뒤 $U_i$ 를 앞, $D_i$ 를 뒤로 안정 분할하는 방법. 막힌 곳: 완전이분쌍 $(A,B)$ 의 색 $i$ 호가 $A\cap U_i\to B\cap D_i$ 로만 가는 것은 맞지만, $B$ 가 $U_i$ 의 원소나 $A$ 가 $D_i$ 의 원소를 (다른 색 호로 연결되어) 포함할 수 있어 분할 뒤 런이 2 이상 늘어난다. 이 증가를 막으려면 4-워크 조건의 "교차변이 반대 색" 구조를 써야 하는데, 어느 정점이 $U_i,D_i$ 중립인지에 대한 일관된 순서를 못 만들었다.
- **(II) [위상] $\tau\ge\xi+1$**, 즉 등변사상 $B_0(G)\to S^{k-1}$ 이 있으면 호-라벨(등변 포셋 사상)이 있다. 이것이 진짜 장애물이다.
 - 포셋 사상은 부분분할 없는 단체 근사에 해당하므로 일반 $\mathbb Z_2$-사상보다 엄격히 약하다. 실제로 **$B_0$ 의 면 포셋에서 $Q_3$ 으로 가는 등변 포셋 사상은 $\overline{C_7}$ 에 없다**(SAT UNSAT; $Q_4$ 는 가능) 인데 $\tau(\overline{C_7})=3$ 이다. 즉 $B_0$ 위의 포셋 지수는 $\tau$ 보다 엄격히 크고, 의미 있는 포셋은 $\operatorname{Hom}$ 쪽($P(G)$)이며, 현탁 $B_0\simeq\Sigma B$ (Csorba [기억-미검증]) 는 포셋 수준에서 성립하지 않는다.
 - 알려진 모든 $\tau$ 값에서 $\tau=\xi+1$ 이었다. 단, 이는 선택 편향이 있다(아래 자가 진단).

### 7. 막힌 곳의 정확한 장애물 (반례 후보 구조)
1. **(I) 의 $k=2$ 사례** (라벨 2 색 $\Rightarrow$ 볼록 4-순환 없는 순서) 가 증명되지 않았다. 반례가 있다면 $E=E_1\cup E_2$ 구조, 정점 수 $\ge8$ 이어야 한다(CEGAR 로 $n\le7$ 배제).
2. **(II) 의 최소 사례**: $\tau=3$ 이지만 $\xi+1\ge4$ 인 그래프는 존재할 수 있는가? $\tau\le3$ 은 $\mathbb Z_2$-사상 $B_0(G)\to S^2$ 이고, 이 사상이 구조상 선형·셀 수준으로 내려오지 않으면 $\xi\ge3$. 이런 그래프를 만들려면 $B_0$ 의 차원이 3 을 크게 넘으면서 장애물 이론 상 $S^2$ 로 가는 사상이 존재하는 그래프(높은 차원, 낮은 호모토피 구조)가 필요하다.
3. 증명된 상한은 모두 순서(=zig) 상한이고, 하한은 $\omega$ 나 연결성이다. **$\tau$ 의 상한을 순서 외의 방법으로 준 적이 없으므로, 알려진 모든 예에서 $\tau=\operatorname{zig}$ 인 것은 상·하한의 샌드위치 구조에서 거의 자동으로 나온 결과**다. 이것이 등식의 증거로 약한 이유이며, 진짜 시험은 순서 상한과 위상 하한이 어긋나는 그래프(예: $\xi+1=\operatorname{zig}$ 이지만 연결성 하한이 $\operatorname{zig}-1$ 이하인 그래프)에서만 가능하다.

## 약점 자가 진단
1. **가장 약한 단계**: (II). 비선형 등변사상을 호-라벨(포셋 사상)로 끌어내리는 논증이 없다. 이것이 없으면 증명은 $\tau=\xi+1$ 을 가정한 조건부다.
2. (I) 의 일반 $k$ 증명이 없다($k=1$ 만 증명, $k=2,3$ 은 $n\le7$ 소규모 SAT).
3. 정리 3 은 홀수 순환의 $\tau=3$ 에 의존한다($C_5$ 는 계산 확인, 일반 순환은 표준 사실 인용).
4. $\xi+1=\operatorname{Xind}+2$ 의 정의 대응은 기억 의존이다. 정리 5(호-라벨 동치) 자체는 정의에서 직접 증명했고, 결론 "첫 반례는 $\xi+1<\operatorname{zig}$ 로 검출 가능" 은 이 대응과 Steiner 그림 1 에 의존한다.
5. 정리 4.3 의 단순연결성은 간선경로 삼각형 폐포 알고리즘(모든 간선이 자명으로 폐포되면 $\pi_1=1$) 이며 구현은 $C_9^3$ 에서도 일관되었다. 정수 호몰로지는 스미스 표준형(희소 단위 피벗 소거 + 잔여 sympy)이다. 독립 구현으로 재확인되지 않았다.
6. 전수·통계는 쓰지 않았다. 이름 있는 그래프 점검은 반례 탐색 기록일 뿐 증거가 아니다.

## 문주님께 요청
없음.

## 후속연구 지점
1. **보조정리 $L_2$ (호-라벨 2 색 $\Rightarrow$ 볼록 4-순환 없는 순서)의 증명 또는 반례.** 이유: (I) 의 최소 사례이고 구조(두 이분 그래프의 합 + 반대 색 교차변 금지)가 구체적이다. 시작: $E_1,E_2$ 구조에서 정점 유형 $C(v)\subseteq\{\pm1,\pm2\}$ 8 종을 원주에 놓고 순서를 각도로 정의, CEGAR 를 대칭 제거(정점 유형 고정)로 $n=8,9$ 까지 확장. 난점: 중립 정점 처리와 귀납(한 색 제거)의 런 증가.
2. **(II) 의 최소 사례: $\tau=3$ 이면서 $\xi\ge3$ 인 그래프 탐색 또는 불가능 증명.** 이유: 진술의 진짜 위상 핵심. 시작: $\operatorname{Hom}(K_2,G)$ 의 차원과 장애물류(등변 사상 $B\to S^1$ 의 존재 $\Leftrightarrow$ 장애 코호몰로지류 소거) 를 소형 코어에서 계산하고 포셋 사상 SAT 와 비교; $B_0$ 가 아닌 $\operatorname{Hom}$ 포셋을 쓸 것($B_0$ 포셋은 $\overline{C_7}$ 에서 이미 부적절). 난점: 등변 사상 존재 판정에 일반 계산기가 없다.
3. **$\omega<\tau<\chi$ 족의 확장: $\tau(C_n^k)$ 를 순환 구조로 일반 증명.** 이유: $C_{11}^3$ 가 첫 예이고 순서 상한이 자연 순환 순서에서 나오므로, 연결성(이웃복합체가 Vietoris–Rips형 홀수 구면) 하한과 순서 상한을 한꺼번에 증명하는 최초의 비자명 족이 될 수 있다. 시작: $N(C_n^k)$ 의 호모토피형을 순환 Rips 복합체 결과(Adamaszek–Adams, [기억-미검증])와 대조. 난점: 순환 수 $\operatorname{zig}$ 의 정확한 값 공식.
4. **순서 상한과 위상 하한이 어긋나는 그래프 찾기** (진짜 시험대): $\operatorname{zig}$ 는 큰데 연결성·$\operatorname{cd}$·호몰로지 하한이 작은 코어. 시작: $\xi+1=\operatorname{zig}$ 가 확인된 그래프 중 $B_0$ 의 연결성이 $\operatorname{zig}-3$ 이하인 것(예: $C_{10}^3$ 은 $\operatorname{zig}=\omega$ 라 해당 없음) 을 구성적으로 찾는다. 난점: 이런 그래프에서 $\tau$ 의 정확한 값에 도달할 도구가 없다 — 이 자체가 장애물.
5. **조인·서로소합 외의 닫힘 연산** (Mycielski, 클리크합, 블로업의 부분 정리). 이유: 등식 족 $\mathcal T$ 를 키우면 최소 반례의 모양이 더 제한된다. 시작: Mycielski $M(G)$ 에 대해 $\operatorname{zig}(M(G))\le\operatorname{zig}(G)+1$ 과 $\tau(M(G))\ge\tau(G)+1$ (Csorba [기억-미검증]) 을 증명해 닫힘을 얻기. 난점: 두 번째 부등식은 $B_0(M(G))\simeq\Sigma B_0(G)$ 의 $\mathbb Z_2$ 판 필요.
