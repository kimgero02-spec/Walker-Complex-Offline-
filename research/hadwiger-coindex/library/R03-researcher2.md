# [R03-researcher2] 추측 C 반증 · 정리 A 증명 완결 · $\tau\le\operatorname{zig}$ 직접 증명

- 작성자·라운드·역할: researcher2 / 라운드 3 / 반례꾼 (표적: 추측 C, 정리 A, 보조 $\tau\le\operatorname{zig}$). 중간본: R03-researcher2-interim.md. 코드: rooms/researcher2/{r3_checks.py, pi1_c5.py, zig_check.py}.
- 도서관 공격: R03-researcher1(.md, interim)을 읽고 공격했다(§F). R03-researcher3* 는 작성 시작·종료 직전 두 번 확인했으나 **도서관에 없었다**(반영 불가).
- 읽은 논문: Steiner 2312.17130 p.3 (정의 1, 그림 1), p.4 (정의 2–3, 정리 1), p.5 (정리 2–3), **p.8–9 (정리 3 의 증명 전체)**. p.6–7 (정리 2 증명)은 훑었으나 이번 임무에 쓰지 않았다. p.10–12 미독.

## 요약
1. **(b) 추측 C 는 거짓이다 [증명].** $G=C_5$ ($\tau=3$)와 $G=\overline{C_7}$ ($\tau=3$)의 **모든** Kneser 표현 $\mathcal H$ 에서 $\operatorname{cd}(\mathcal H)\le2<\tau$. 점 두 개 $U=\{a,b\}$ 를 잘 골라 나머지 집합을 2-색칠 가능하게 만드는 명시적 논증(§C). 막는 불변량: 독립집합이 $\le2$ 개인 그래프에서는 독립쌍(서로 교차하는 두 집합)이 한 점으로 한꺼번에 제거되고, 이는 위상 지표 $\tau$ 가 보지 않는 Helly형 정보다. 경로 "추측 C ⇒ 정리 3 ⇒ S1(τ)" 은 닫힌다.
2. **(a) 정리 A ($\operatorname{cd}\le\tau$) 는 증명이 완결된다 [증명].** R02 스케치에 틀린 단계는 없다. (F1)–(F3) 과 (O1) 을 쓰지 않는 **명시적 등변 사상** $S^{c-1}\to B_0(G)$ (모멘트 곡선)으로 짧게 증명한다(§B). (O1) 은 공허하다.
3. **(c) $\tau\le\operatorname{zig}$ 를 문헌 없이 직접 증명했다 [증명]**(§D). Borsuk–Ulam 만 쓴다. 그림 1 의 사슬이나 Daneshpajou–Meunier 에 의존하지 않는다. 따라서 S3(τ판)은 Steiner 정리 2(zig 판)에만 의존한다.
4. 부산물 [증명]: Steiner 정리 3 의 증명(p.8–9)이 주는 부분그래프 $K_{n_1}+K^*_{n_2,n_2}$ 로도 $C_5$ 는 막힌다($\psi(C_5)=2<\tau$). 즉 "τ≥t ⇒ 정리 3 형 부분그래프" 도 거짓.

## 본문

### 0. 정의·오프셋 점검 (K_1, K_2, K_3) 과 SRC 정정
- $B_0(G)$: 정점 $V(G)\times\{1,2\}$, 면 $=A\times\{1\}\cup B\times\{2\}$ with $A\times B\subseteq E(G)$ (변이 비어도 됨). [문헌 확인: Steiner p.3 정의 1 — $B_0$ 는 공통이웃 조건이 **없고**, $B$ 에 공통이웃 조건이 있다.] **정정**: `library/SRC-steiner-2312.17130.md` 의 "정의" 절은 이를 반대로 적었다($B_0$ 에 이웃 조건이 붙는다고). 원문 p.3 이 맞고 우리 정의와 같다. 오케스트레이터가 SRC 를 고치면 좋다(결론에는 영향 없음).
- $K_1$: $B_0=\{(v,1),(v,2)\}$ 두 점(면: $\{(v,1)\}$,$\{(v,2)\}$, 둘 함께는 불가 — $A\times B\ni(v,v)\notin E$). $S^0$, coind 0, $\tau=1$. $K_2$: 4정점 사각형(면: $\{(1,1),(2,2)\}$ 등) $=S^1$, $\tau=2$. $K_3$: 교차다면체 경계 $S^2$, $\tau=3$. $K_n$ 일반: $S^{n-1}$, $\tau=n$ [증명]. 오프셋 $+1$ 유지.
- $\tau(C_5)=3$ 의 하한은 R01 의 "$B_0(C_5)\simeq S^2$" 를 이번에 **독립 계산**으로 보강했다: $B_0(C_5)$ (면 수 10,30,30,10,2) 의 기본군을 간선경로군 표현으로 계산하면 21개 생성원이 모두 소거되어 **단일연결** [계산 확인, pi1_c5.py]. 자유 $\mathbb Z_2$-복합체가 1-연결이면 $\operatorname{coind}\ge2$ (표준 사실: $k$-연결 ⇒ coind $\ge k+1$) [증명, 표준 사실 인용]. 상한 $\tau\le\chi=3$. 따라서 $\tau(C_5)=3$.
- $\tau(\overline{C_7})=3$: $\omega=3$ (하한), $\mathbb R^2$ 배치 인증서(R02, 극대쌍 28개)를 이번에 내 verify.py 로 재실행해 유리수 정확 검증 통과 [계산 확인]. 상한 3.

### A. 공격 대장
| 대상 | 방법 | 결과 | 방어한 이유(불변량) / 공격 성공의 내용 | 표기 |
|---|---|---|---|---|
| **추측 C** ($\max_{\mathcal H}\operatorname{cd}=\tau$), $G=C_5$ | 임의 표현의 구조 분석(§C.1) | **반례** | 모든 $\mathcal H$ 에서 $\operatorname{cd}\le2<3=\tau$ | [증명] |
| 추측 C, $G=\overline{C_7}$ | 같은 논증(§C.2) | **반례** | 모든 $\mathcal H$ 에서 $\operatorname{cd}\le2<3=\tau$ | [증명] |
| "τ≥t ⇒ $K_{n_1}+K^*_{n_2,n_2}$ 부분그래프, $n_1+n_2=t$" | $C_5$ 에서 부분그래프 열거 | **반례** | $C_5$ 는 삼각형·차수 3·$C_6$ 이 없어 $t=3$ 형을 못 담음($\psi(C_5)=2$), $\tau=3$ | [증명] |
| 정리 A 단계 1–2 ($\Sigma,\Psi$ 면 조건·단조·등변) | 정의 대조 | 방어 | $e\subseteq S^+$, $f\subseteq S^-$, $S^+\cap S^-=\varnothing$, 간선 비공집합 ⇒ $e\cap f=\varnothing$ ⇒ $e\sim f$ | [증명] |
| 단계 3 ($\Lambda$ 제거) | $K_3+v_0$ 외 일반 점검 | 방어 | $\Psi(S)=\varnothing\iff S\in\Lambda$, $\Lambda$ 는 하향 닫힘(부분복합체). 제거 없이는 $\Psi$ 가 정의역을 비운다 | [증명] |
| 단계 4 (골격 차수 $|S|\le N-c$) | 정의 대조 | 방어 | $S\in\Lambda$ ⇒ $S^+\cup S^-$ 가 $V\setminus U$ 의 2-색칠(간선이 어느 한쪽에 통째로 안 들어감) ⇒ $|U|\ge c$ | [증명] |
| 단계 5 (F1)–(F3) 연결성·등변 사상 | 명시적 대체(§B) | 방어(대체됨) | 골격 여집합에서 구면으로 가는 사상을 모멘트 곡선으로 직접 쓴다: 임의 $c$ 행이 독립인 $N\times c$ 행렬 | [증명] |
| (O1) 여분 원소 불변성 | 논증의 $N$ 의존성 점검 | **공허** | 증명은 $c\le N$ 만 쓰고 $N$ 크기에 의존하지 않음. (또 $\operatorname{cd}$ 자체도 여분 원소에 불변: $U$ 에 여분 원소는 불필요) | [증명] |
| R02-r1 의 $\operatorname{cd}(\mathcal H)\ge1$ 가정 | 경계 사례 | 방어 | 모든 간선 비공집합이면 $U=V$ 가 항상 허용 ⇒ $\operatorname{cd}\le N$. $c=0$ 이면 자명 | [증명] |
| R03-r1 정리 A (극대쌍 분류, $n=5$ 경계) | 재도출 | 방어 | $n\ge5$ 에서 $N[c-1]\cap N[c+1]=\{c\}$ ($c-2\equiv c+2$ 는 $n|4$ 일 때만) | [증명] |
| R03-r1 정리 B (모멘트 곡선) | $i=0,n-1$ 의 곡선 위 순서 재점검 | 방어 | $i=0$: $K^0,K^1,K^{n-1}$ 순서 ⇒ 변화 $\le m$; $i=n-1$: $K^0,K^{n-2},K^{n-1}$ ⇒ $\le m$; (Q) 는 $2m$ 점 ⇒ 변화 $\le2m-1=d$ | [증명] |
| R03-r1 $m=1$ 실패 위치 | $\tau(C_n)=3$ 과 대조 | 방어(정합) | (P) 변화 $2>d=1$ 이 정확히 $m=1$ 에서만 | [증명] |
| 보조 $\tau\le\operatorname{zig}$ (문헌 의존 제거) | §D | 직접 증명 성공 | 모멘트 비소멸 + 부호변화 | [증명] |

### B. (a) 정리 A 의 완결 증명

**정리 A.** $\mathcal H=(V,E)$, 모든 $e\in E$ 비공집합, $N=|V|$, $G=KG(\mathcal H)$, $c=\operatorname{cd}(\mathcal H)$. 그러면 $\mathbb Z_2$-사상 $S^{c-1}\to B_0(G)$ 가 있고, 따라서 $\operatorname{coind}(B_0(G))\ge c-1$, 즉 $\operatorname{cd}(\mathcal H)\le\tau(G)$. [증명]

*증명.* $c=0$ 이면 자명. $c\ge1$ 이고 $c\le N$ ($U=V$ 는 허용되므로). 서로 다른 실수 $t_1<\dots<t_N$ 으로 $N\times c$ 행렬 $M_{ik}=t_i^{\,k}$ ($0\le k<c$) 를 만든다. 임의의 $c$ 행은 $c\times c$ Vandermonde 이므로 독립이다. 따라서 $y\in S^{c-1}$ 에 대해 $z:=My\in\mathbb R^N$ 은 **0 인 좌표가 $\le c-1$ 개** (0 인 좌표 $c$ 개면 $c$ 개 행에 직교하는 $y\ne0$ 이 되어 모순).
$P=\{i:z_i>0\}$, $Q=\{i:z_i<0\}$, $U=V\setminus(P\cup Q)$ 라 하면 $|U|\le c-1$.
각 $e\in E$ 에 대해 $a(e):=\min_{i\in e}\max(z_i,0)$, $b(e):=\min_{i\in e}\max(-z_i,0)$. $a(e)>0\iff e\subseteq P$, $b(e)>0\iff e\subseteq Q$.

*주장 1: $s:=\sum_e(a(e)+b(e))>0$.* 아니면 어떤 간선도 $P$ 에, $Q$ 에 통째로 들어가지 않는다. 그러면 $U$ 를 피하는 간선들은 모두 $P\cup Q$ 안에 있고, $P$/$Q$ 로 색칠하면 단색 간선이 없다. 즉 $|U|\le c-1$ 인 허용 집합이 존재해 $\operatorname{cd}<c$, 모순.

*주장 2: 지지집합이 $B_0$ 의 면.* $A=\{e:e\subseteq P\}$, $B=\{f:f\subseteq Q\}$. $P\cap Q=\varnothing$ 이고 간선이 비공집합이므로 $e\in A,f\in B$ 는 서로소 ⇒ $G$ 에서 인접 ⇒ $A\times B\subseteq E(G)$ (그리고 $A\cap B=\varnothing$).
$\Phi(y):=\frac1s\big(\sum_{e}a(e)\,(e,1)+\sum_e b(e)\,(e,2)\big)\in|B_0(G)|$ 로 정의. $y$ 에 대해 연속(min, max, $s>0$). $y\to-y$ 이면 $z\to-z$, $a\leftrightarrow b$ 이므로 $\Phi(-y)=\operatorname{swap}\Phi(y)$ — 등변. ∎ (S^{c-1}→B_0 등변이면 coind ≥ c−1; 정의.)

*R02 스케치와의 대응:* $\Sigma$ = $z/|z|_1$ 이 사는 교차다면체 경계, $\Psi$ = 지지집합 $\mapsto(A,B)$, $\Lambda$ = $s=0$, 골격 조건 "$\ge N-c+1$ 개 비영 좌표" = 모멘트 곡선의 성질. (F1)(F2)(F3) 는 이 명시적 사상으로 대체되었다.
*점검* [계산 확인, 증명의 구현 점검일 뿐]: r3_checks.py 에서 무작위 소형 $\mathcal H$ 244개(brute force $c$)·각 40개 $y$ 에 대해 $s>0$ 이고 지지가 면 — 위반 0.
*결론 (a):* **완성 쪽.** 결함 단계 없음, (O1) 공허.

### C. (b) 추측 C 의 반증

**용어.** $\kappa(G):=\max\{\operatorname{cd}(\mathcal H):KG(\mathcal H)\cong G\}$. 추측 C: $\kappa=\tau$. 표현에서 집합 $S_v$ ($v\in V(G)$) 는 $v\sim w\iff S_v\cap S_w=\varnothing$ 이다. 한 점이 속하는 집합들은 서로 교차하므로 비인접(독립)이다.

**C.1 $G=C_5$.** 꼭짓점 $0,\dots,4$, $i\sim i\pm1$. 비인접쌍은 $\{i,i+2\}$ 이므로 $S_i\cap S_{i+2}\ne\varnothing$, $S_i\cap S_{i+1}=\varnothing$.
*(i) 모든 집합은 원소가 $\ge2$ 개*: $S_4$ 는 $S_1$, $S_2$ 와 교차하고 $S_1\cap S_2=\varnothing$ 이므로 $S_4$ 에는 서로 다른 두 점이 있다(다른 $i$ 도 대칭).
*(ii)* $a\in S_0\cap S_2$, $b\in S_1\cap S_3$ 를 하나씩 고르고 $U=\{a,b\}$. $S_0,S_2\ni a$, $S_1,S_3\ni b$ 이므로 $U$ 를 피하는 집합은 $S_4$ 뿐 후보. 실제 $a\notin S_4$ ($a\in S_0$, $S_4\cap S_0=\varnothing$), $b\notin S_4$ ($b\in S_3$, $S_4\cap S_3=\varnothing$). 즉 $S_4$ 는 $U$ 를 피한다. $S_4$ 의 서로 다른 두 점(둘 다 $V\setminus U$ 안)을 다른 색으로 칠하면 $(V\setminus U,\{S_4\})$ 는 2-색칠 가능.
*(iii)* 따라서 $\operatorname{cd}(\mathcal H)\le2$. 모든 표현에 대해 성립하므로 $\kappa(C_5)\le2<3=\tau(C_5)$. ∎ [증명]

**C.2 $G=\overline{C_7}$.** 정점 $\mathbb Z_7$, $i\sim j\iff j-i\in\{\pm2,\pm3\}$. 따라서 $S_i\cap S_{i+1}\ne\varnothing$, 그 밖의 쌍은 서로소.
*(i)* 연속 집합들의 교점: $e\in S_3\cap S_4$, $c\in S_4\cap S_5$, $d\in S_5\cap S_6$, $f\in S_6\cap S_0$ 를 하나씩 고른다. 서로 다른 점이다: $e=c$ 면 $S_3\cap S_5\ne\varnothing$, $e=d$ 면 $S_3\cap S_5$, $e=f$ 면 $S_3\cap S_6$, $c=d$ 면 $S_4\cap S_6$, $c=f$ 면 $S_4\cap S_6$, $d=f$ 면 $S_5\cap S_0$ — 모두 서로소 쌍이라 불가.
*(ii)* $a\in S_0\cap S_1$, $b\in S_2\cap S_3$, $U=\{a,b\}$. $S_0,S_1\ni a$, $S_2,S_3\ni b$. 그리고 $S_4,S_5,S_6$ 은 $U$ 를 피한다: $a\in S_0,S_1$ 이고 $S_4\cap S_0=S_5\cap S_0=\varnothing=S_6\cap S_1$; $b\in S_2$ 이고 $S_4\cap S_2=S_5\cap S_2=S_6\cap S_2=\varnothing$. 
*(iii)* $e,c,d,f\notin U$ ($e,c\in S_4$, $d\in S_5$, $f\in S_6$ 이고 이 집합들은 $U$ 를 피함). $e,d$ 는 빨강, $c,f$ 는 파랑, 나머지는 임의. $S_4\supseteq\{e,c\}$, $S_5\supseteq\{c,d\}$, $S_6\supseteq\{d,f\}$ 모두 두 색을 포함. 2-색칠 가능.
*(iv)* $\operatorname{cd}(\mathcal H)\le2$, $\kappa(\overline{C_7})\le2<3=\tau$. ∎ [증명]
(참고: 점 두 개로 집합 4개를 제거하는 것이 핵심 — $\overline{C_7}$ 의 독립쌍 $\{0,1\},\{2,3\}$.)

**C.3 일반화 [증명].** **보조정리 E.** $\alpha(G)\le2$ 이고 모든 정점 $v$ 가 서로 인접한 두 비이웃을 가지면(★), 모든 Kneser 표현에서 $\operatorname{cd}(\mathcal H)\le\chi(G)-1$.
*증명.* (★) 로 모든 $S_v$ 는 원소 $\ge2$ 개(C.1(i) 와 같은 논증). 최적 진색칠의 색류는 크기 $\le2$ 이고 서로 교차하는 집합들이다. 크기 2 인 류 $\{S,S'\}$ 는 공통점 하나를, 크기 1 인 류는 임의의 한 점을 뽑는다. 마지막 류 하나만 빼고 $\chi-1$ 개 점으로 $U$ 를 만들면 $U$ 를 피하는 집합은 마지막 류 안에만 있고, 그것은 (원소 $\ge2$ 개인) 집합 하나, 또는 공통점 $x$ 를 가진 두 집합 $S\ni x,y$, $S'\ni x,z$ 이다. $x$ 를 빨강, $y,z$ 를 파랑으로 칠하면 된다. ∎
따름: $\tau(G)=\chi(G)$ 인 그래프 중 (★) 를 만족하면 $\kappa(G)<\tau(G)$. 예: $C_5$.
**상계 $\kappa\le\psi$** [증명, Steiner p.8–9 의 증명에서]: 정리 3 의 증명은 $\operatorname{cd}(\mathcal H)=|U|=t$ 인 최소 $U$ 로부터 부분그래프 $K_{n_1}+K^*_{n_2,n_2}\subseteq G$ ($n_1+n_2=t$) 를 만든다($K^*_{n,n}$ = $K_{n,n}$ 에서 완전매칭 제거). 따라서 $\kappa(G)\le\psi(G):=\max\{n_1+n_2: K_{n_1}+K^*_{n_2,n_2}\subseteq G\}$. $\psi(C_5)=2$: $t=3$ 형 네 가지 $(3,0),(2,1),(1,2),(0,3)$ 은 각각 삼각형, 삼각형(=$K_2+2K_1$), 차수 4 정점, $C_6$(정점 6개)을 요구해 $C_5$ 에 없다. 이것이 C.1 의 독립적인 두 번째 증명이다. $\psi(\overline{C_7})=3$ 이므로 $\overline{C_7}$ 에는 C.2 의 직접 논증이 필요했다(싱글톤 집합 3개 $\Rightarrow K_3$ 의 경우를 (i) 의 "원소 $\ge2$ 개"가 막는다).

**결론 (b): 반례 쪽 (추측 C 거짓).** $\tau(C_5)=\tau(\overline{C_7})=3$ 인데 $\kappa\le2$. 가장 작은 비자명 후보 $\overline{C_7}$ 에서 비존재 증명 완료, 더 쉬운 $C_5$ 에서도.

**어떤 불변량이 막는가.** $\operatorname{cd}$ 는 표현의 점-집합 접촉 구조만 본다. 한 점은 서로 교차하는 집합 하나의 족을 한꺼번에 "삭제"한다. $\alpha(G)\le2$ 이면 독립집합은 쌍이어서 Helly 성질이 자명하게 성립하고(두 집합이 교차하면 공통점이 있다), 그래서 $\chi-1$ 개의 점이면 충분하다. $\tau$ 는 $\mathbb Z_2$-위상(여기서는 $B_0(C_5)\simeq S^2$ 의 단일연결성)이라 이 "점 하나로 독립쌍 제거"를 보지 못한다. 즉 $\tau-\kappa\ge1$ 의 원인은 위상 지표와 Helly/횡단수형 조합 지표의 불일치다.
**S1 에의 영향.** 추측 C 가 필요했던 경로가 막혔다. 정리 3 은 $\operatorname{cd}$ 에서 $K_t$ 마이너를 주지만, $\tau\ge t$ 인 $C_5$ 같은 그래프는 어떤 표현으로도 $\operatorname{cd}\ge t$ 에 못 닿는다. S1(τ판) 의 증명은 정리 3 과 독립적인 다른 방법이 필요하다(이 반례 자체는 S1 을 반증하지 않는다. $C_5$ 는 $K_3$ 마이너를 가진다).

### D. (c) $\tau\le\operatorname{zig}$ 의 직접 증명 [증명]

**정리 D.** 모든 그래프 $G$ 에서 $\operatorname{coind}(B_0(G))+1\le\operatorname{zig}(G)$.
(정의: Steiner p.4 정의 2. 진색칠 $c:V\to\mathbb N$ 에서 지그재그 $z_1,\dots,z_k$: $c(z_1)<\dots<c(z_k)$, 홀수/짝수 번째 집합이 서로 완전. $\operatorname{zig}=\min_c\max$(지그재그 길이).)

*증명.* 진색칠 $c$ 와 그 최대 지그재그 길이 $L$ 을 고정. $m=\max c$. $|B_0(G)|$ 의 점 $w$ (가중치, 지지집합 면 $(A,B)$) 에 대해 $x(w)\in\mathbb R^m$ 을 $x_j=\sum_{v\in A,c(v)=j}w(v,1)-\sum_{v\in B,c(v)=j}w(v,2)$ 로 정의. $A\times B\subseteq E$ 이므로 $a\in A,b\in B$ 는 인접해 색이 다르다 ⇒ 각 색은 $A$ 쪽 또는 $B$ 쪽에만 나타나 상쇄가 없다. 따라서 $x\ne0$, $x_j>0$ 은 색 $j$ 가 $A$ 에, $x_j<0$ 은 $B$ 에 있음. $x$ 는 $w$ 에 선형이고 복사본 교환 시 $x\mapsto-x$.
*(1) 부호변화와 지그재그.* $x$ 의 비영 성분을 $j$ 순서로 읽을 때 부호가 바뀌는 횟수 $S^-(x)$, 부호 블록 수 $r=S^-(x)+1$. 각 블록에서 그 색의 정점 하나씩 $z_1,\dots,z_r$ 을 고르면 색이 증가하고, 블록이 교대하므로 홀수/짝수 번째가 각각 $A$ 쪽, $B$ 쪽(또는 반대)이며 $A\times B\subseteq E$ 로 서로 완전. 즉 길이 $r$ 지그재그. 그러므로 $S^-(x)+1\le L$.
*(2) 모멘트 보조정리.* $\mu_k(x):=\sum_{j=1}^m x_j j^k$ ($k=0,\dots,L-1$) 라 하면 $x\ne0$, $S^-(x)\le L-1$ 일 때 $\mu(x)\ne0$. (귀류: $\mu_k(x)=0$ $\forall k<L$ 이면 $s=S^-(x)\le L-1$ 이므로 부호변화 사이 비정수 점에 근을 둔 차수 $s$ 다항식 $p$ 를 잡는다. 부호를 맞추면 모든 $j$ 에서 $x_jp(j)\ge0$, 비영 $x_j$ 에서 $>0$. $\sum_jx_jp(j)>0$ 이나 이는 $\mu_0,\dots,\mu_s$ 의 선형결합 $=0$. 모순.)
*(3)* $F(w):=\mu(x(w))\in\mathbb R^L\setminus0$ 는 연속, 등변(홀수). 따라서 $\mathbb Z_2$-사상 $B_0(G)\to S^{L-1}$. 만약 $S^k\to B_0(G)$ 등변사상이 있으면 합성 $S^k\to S^{L-1}$ 이 등변이므로 Borsuk–Ulam 으로 $k\le L-1$. 즉 $\operatorname{coind}(B_0(G))\le L-1$, $\tau\le L=L(c)$. $c$ 는 임의의 진색칠이므로 $\tau\le\operatorname{zig}(G)$. ∎

*점검* [계산 확인, 구현 점검]: zig_check.py — $C_5$ (두 색칠), $K_4$, $\overline{C_7}$ (4색 색칠; 최대 지그재그 3) 에서 모든 면(82, 82, 80, 478개)·무작위 가중치에서 $\mu\ne0$, 위반 0. 부수적으로 $\overline{C_7}$ 의 그 색칠에서 최대 지그재그 길이 3 이므로 $\operatorname{zig}(\overline{C_7})\le3=\tau$ (앞서 $\tau\le\operatorname{zig}$ 와 합쳐 $\operatorname{zig}(\overline{C_7})=3<\chi=4$) [계산 확인 + 정리 D].
**결론 (c):** $\tau\le\operatorname{zig}$ 는 [증명]. S3(τ판)는 이제 Steiner **정리 2**(p.5; 증명 p.6–8, 본 보고서에서 재검증하지 않음)에만 의존한다. 그림 1 사슬 의존 제거. 원리는 Simonyi–Tardos 의 지그재그 정리와 같은 모멘트 논법이다 [기억-미검증: 출처 연결].

### E. 증명 시도 요약 (연구 원칙)
- 연역 증명 3건: 정리 A(§B), 추측 C 비존재(§C), 정리 D(§D). 막힌 곳 없음.
- 전수·통계 점검은 하지 않았다. 계산은 증명의 구현 점검에만 썼다(수 초).

### F. 도서관 공격 메모
- R03-researcher1: 정리 A(극대쌍 분류)와 정리 B(모멘트 곡선 구성)의 경계 경우 $n=5$, $i=0,n-1$ 재점검 통과(§A). 오케스트레이터 재검증(R03-orchestrator-verify)과도 일관. 결함 없음. 참고: R03-r1 의 "$\tau\in(\omega,\chi)$ 인 그래프" 열린 점과, 나의 $\overline{C_7}$ 결과($\tau=\omega=\operatorname{zig}=3<\chi$)는 모순 없음.
- R03-researcher3: 도서관에 없었음(작성 시작·종료 직전).
- R02-researcher1 의 "추측 C 부정적 증거는 표현 선택 문제인지 거짓인지 구분 못 함": **거짓이다**(§C). 또 "후속연구 지점 1: $\overline{C_7}$ 에서 $\operatorname{cd}=3$ 인 표현 탐색" 은 불필요(비존재 증명).

## 문주님께 요청
없음. (참고로 SRC-steiner 정의 절의 $B$/$B_0$ 설명 반전은 오케스트레이터가 고칠 수 있는 일이다.)

## 후속연구 지점
1. **S1(τ판) 의 새 증명 경로: 정리 3 의 일반화 대신 "τ 가 크면 마이너"를 주는 구조 찾기.** 이유: 추측 C 가 거짓이고 정리 3 형 부분그래프($\psi$)도 $C_5$ 에서 막혀, 정리 3 의 모든 직접 이전이 차단됨. 시작: $\tau(G)\ge t$ 에서 얻을 수 있는 구조의 최소 예 $C_5$($K_3$ 마이너가 수축으로만 나옴)를 분석해, 수축이 필요한 구조를 $\mathbb Z_2$-사상 $S^{t-2}\to B_0(G)$ 의 상(像)에서 읽는 방법(예: 정리 D 의 모멘트 사상의 역상)을 찾는다. 난점: 마이너 단조가 아닌 $\tau$ 와 맞물린 귀납 구조.
2. **$\kappa(G)$ 의 정확한 값/상계 (Helly·횡단수형).** 이유: $\kappa\le\psi$ 와 보조정리 E 로 $\kappa<\tau$ 가 확인됐으나 $\kappa$ 와 $\tau$ 의 간극 크기는 모름. 시작: $\kappa(G)\le\min(\psi(G),\ldots)$ 의 개선, $\alpha(G)=2$ 족(보수가 삼각형 없는 그래프)에서 \kappa\le\chi-1 (보조정리 E) 의 등호 여부 추측 후 증명, $\overline{C_7}$ 에서 $\kappa=2$ 인지(표현 구성). 난점: 표현 공간이 크므로 구성적 하한(좋은 표현 설계)이 필요.
3. **$\operatorname{zig}$ 와 $\tau$ 사이의 간극.** 이유: 정리 D 로 $\tau\le\operatorname{zig}\le\chi$ 가 증명되었고 $\overline{C_7}$ 에서 $\operatorname{zig}=\tau<\chi$ 임을 봄. $\tau<\operatorname{zig}$ 인 그래프가 있는가? 시작: $C_5[K_m]$ 에서 $\operatorname{zig}$ 계산(진색칠 최적화). 난점: $\operatorname{zig}$ 의 최소화가 색칠 전역탐색.
4. **Steiner 정리 2 (zig 판 홀수 마이너)의 증명 검증(p.6–8)과 p.10–12 읽기.** 이유: S3(τ판)의 마지막 문헌 의존. 시작: 보조정리 5 와 Claim (∗) 을 소형 그래프에서 직접 확인. 난점: 보조정리 5 의 출처가 [25] 라 증명 일부가 원문 밖.
5. **[기억-미검증] 재확인**: 정리 D 의 모멘트 논법과 Simonyi–Tardos 지그재그 정리의 연결, "k-연결 ⇒ coind ≥ k+1" 표준 사실의 출처(Matoušek 책), Csorba 현탁 동형. 시작: 문주님이 Matoušek *Using the Borsuk–Ulam Theorem* §5.3 / Simonyi–Tardos 2006 을 주시면 대조(있으면 좋음).
