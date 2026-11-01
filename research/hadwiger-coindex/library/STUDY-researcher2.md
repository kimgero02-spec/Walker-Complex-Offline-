# STUDY — Norin–Steiner, *A Proof of the Linear Hadwiger Conjecture* (arXiv:2610.05291v1) 정독 (연구원2)

## 요약

- 13–41쪽 전체를 정독했고, 10–12쪽(Theorem 9 진술과 Lemma 7 의 쌍대 단계)도 다시 확인했다. Lemma 7, Lemma 8, Lemma 12, Theorem 5 (부트스트랩), Theorem 9 (부록 A) 의 증명 흐름을 독립적으로 재구성했다. Lean 형식화는 접속하지 못했다.
- 확인 결과: Lemma 7 의 쌍대 단계 (정점당 $\sum_v z_{uv}\le 1/\mu$, 임계값으로 $D$ 정의, 독립집합의 $\sum y$ 상계), Lemma 8 의 마이너 논법, Lemma 12 의 greedy 와 degeneracy 논법, Theorem 5 의 $k=(\log t)^{\alpha/3}$ 축약 논법은 모두 [증명] 또는 [계산 확인] 으로 맞다. 부트스트랩 산술 $\tfrac13(\tfrac43)^{10}=1048576/177147\approx 5.9192\ge 5$ 도 맞다.
- **기존 요약 정정 (중요):** 오케스트레이터 요약 SRC 의 "이 논문은 S1 에 새 정보를 주지 않는다 (χ 상한은 τ 상한을 주지 않는다)" 는 **부등식 방향 오류**다. $\tau\le\chi$ 이므로 $\chi\le C\,h$ 에서 $\tau\le C\,h$ 가 따라 나온다. 즉 **선형 S1 (τ 판) 이 논문 정리 2 에서 조건부로 나온다.** 이는 STATUS 의 78행("선형 S1 $\tau\le Ch$ [증명, Norin–Steiner 정리 2 의존]")과 일치하며, SRC 요약 줄 17 과는 모순이므로 SRC 를 고쳐야 한다. 조건: 논문 증명이 맞아야 하고, 논문 스스로 AI 생성이라고 고지했으므로 독립 검증 전이다.
- 기법 이식: 분수 색칠 + 보조 간선 + 가중 매칭은 **χ 전용** 도구로 보인다. 결정적 장애는 $\tau(C_5)=3>\chi_f(C_5)=5/2$ 이므로, $\chi_f$ 에 대한 상계로는 $\tau$ 를 직접 잡을 수 없다.

## 읽은 쪽

- 13–41쪽 전체 (본문 13–27쪽, 부록 A 31–36쪽, 부록 B 37–41쪽, 참고문헌 28–30쪽은 훑음).
- 10–12쪽: Theorem 9 진술, (P-CODEGREE)/(D-CODEGREE), Lemma 7 증명 시작부 — 재확인.
- 1–9쪽: 오케스트레이터 요약 SRC 에 의존. **미재독.** 특히 쪽 2–4 의 Theorem 2 가 LH(5) 에서 나오는 Delcourt–Postle 축소, 쪽 8–9 의 Theorem 4 조립 산술 (α(G') 축약 포함)은 본 연구원이 직접 검증하지 않았다.

---

## 확인된 것

### 1. Lemma 7 (쪽 10–14): $\chi(G)\le\chi_f(G\cup D)+\gamma n$, $\Delta(D)\le(600(m+2)/\gamma)^{20m+41}$

**(a) 쌍대로 $D$ 를 정하는 단계 — 독립적으로 맞다.** [증명]
- 최적 쌍대 $(y,z)$ 에 대해 $\sum_{u:uv\in\bar E} z_{uv}\le 1/\mu$ (쪽 11). 귀류법: 위반 정점 $v$ 의 $y_v$ 와 $v$ 에 붙은 $z$ 를 모두 0 으로 바꾼다. (D-CODEGREE) 의 제약 $\sum_{w\in I}y_w-\sum_{\{a,b\}\subseteq I} z_{ab}\le 1$ 은, $v\in I$ 인 경우 좌변이 $I\setminus\{v\}$ 의 기존 좌변과 같아지므로 (이 집합도 독립) 유지된다. 목적함수 변화는 $-y_v+\mu\sum z$ 인데 최적성상 $\le 0$, 따라서 $\sum z\le y_v/\mu\le 1/\mu$ ($y_v\le 1$ 은 $I=\{v\}$ 제약).
- 임계값 $\tau_0=\frac1\mu\big(\frac{\gamma}{600(m+2)}\big)^{20m+41}=\frac{\gamma}{600(m+2)2^{20m+40}}$ (μ 대입으로 확인). $D:=\{uv\in\bar E: z_{uv}\ge\tau_0\}$. 정점당 차수 $\le(1/\mu)/\tau_0=(600(m+2)/\gamma)^{20m+41}$. [계산 확인]
- $G\cup D$ 의 독립집합 $I$: 내부 쌍은 모두 $z<\tau_0$, 쌍 수 $\le m^2$ 이므로 $\sum_{v\in I}y_v\le 1+m^2\tau_0<1+\gamma/2$. 따라서 $y/(1+\gamma/2)$ 는 $G\cup D$ 의 (D) 가능해. [계산 확인]
- 결합: $\chi_f(G\cup D)\ge\frac{1}{1+\gamma/2}\sum y\ge(1-\tfrac\gamma2)\sum y\ge(1-\tfrac\gamma2)(\mathrm{OPT}+\mu\sum z)\ge \mathrm{OPT}-\tfrac\gamma2 n$. 즉 $\mathrm{OPT}\le\chi_f(G\cup D)+\tfrac\gamma2 n$. [증명] (쌍대 강성 $\sum y-\mu\sum z=\mathrm{OPT}$ 사용.)

**(b) "$\sum_{I\ni v}x_I=1$ 로 맞출 수 있다" (쪽 12–13).** [증명] $1+\varepsilon$ 이면 $v$ 를 포함하는 독립집합 $J_i$ 들의 $x$ 를 $\varepsilon_i$ 만큼 줄이고 $J_i\setminus\{v\}$ 의 $x$ 를 늘린다. 쌍 $\{a,b\}\subseteq J_i\setminus v$ 의 codegree 는 순변화 0, 쌍 $\{v,a\}$ 는 증가 없음, $u\ne v$ 의 cover 는 불변. 

**(c) 하이퍼그래프 $\mathcal H$ (쪽 13).** [계산 확인]
- $r=m+2$, 더미 $S$, $|S|=s=\lceil r\mathrm{OPT}-n\rceil$. 간선 $I\cup T$ ($T\subseteq S$, $|T|=r-|I|$), 가중 $x'_e=x_I/\binom{s}{r-|I|}$. 전체 가중 $=\mathrm{OPT}$.
- 원래 정점 차수 $=\sum_{I\ni v}x_I=1$. 더미 차수 $=\sum_I x_I\,(r-|I|)/s=(r\,\mathrm{OPT}-n)/s\in(1-1/s,\,1]$ (쓴 식은 $\sum_v\sum_{I\ni v}x_I=\sum_I|I|x_I=n$).
- $m\,\mathrm{OPT}\ge\sum|I|x_I=n$ (α≤m) 이므로 $s\ge 2\,\mathrm{OPT}\ge 2n/m\ge m+2$ (필요한 $n\ge m(m+2)/2$ 는 큰 $n$ 가정에서 나옴).
- codegree: 원-원 $\le\mu$ 는 (P-CODEGREE) 제약 그대로. 원-더미 $\le r/s\le m(m+2)/n\le\mu$: 가정 $n\ge(600(m+2)/\gamma)^{20m+40}$ 에서 $\mu=(\gamma/300(m+2))^{20m+40}$ 이 나오고, 비율 $2^{20m+40}\ge m(m+2)$ 로 충분. 더미-더미 $\le 2(m+2)^2m^2/n\le\mu$. 차수 하한 $1-\mu$: $1/s\le m/(2n)\le\mu$. 모두 충족.
- $\xi=\gamma/(3r)$, $\mu=(\xi/100)^{20r}$ 로 Theorem 9 적용 → 덮지 않는 정점 $\le\xi(n+s)$. 매칭 간선의 원래 부분 $I_j$ 는 서로소 독립집합. [증명]
- 색칠: $\chi(G)\le|M|+\xi(n+s)\le\frac{n+s}{r}+\xi(n+s)<\mathrm{OPT}+\frac1r+\frac\gamma3(\mathrm{OPT}+1)\le\mathrm{OPT}+\frac\gamma2 n$ ($n\gg1/\gamma$). (a) 와 결합하여 $\chi(G)\le\chi_f(G\cup D)+\gamma n$. [증명]

**(d) 본문 오타.** 쪽 13 의 "$\mu=(\gamma/3000(m+2))^{20m+40}$" 은 쪽 11·14 와 $\xi/100$ 정의에 맞지 않는다. $(\xi/100)^{20r}=(\gamma/300(m+2))^{20m+40}$ 이므로 올바른 값은 $300$. 증명 흐름은 300 을 썼다. [계산 확인]

**(e) 작은 $n$ 경우.** 논문은 $n\ge(600(m+2)/\gamma)^{20m+40}$ 을 가정하고 증명한다 (쪽 11 첫 줄). 명시되지 않은 나머지 경우는 본 연구원이 다음으로 처리할 수 있다 (논문에는 없음, [증명] 본 연구원 추가): $D=K_n$. $\Delta(K_n)=n-1<(600(m+2)/\gamma)^{20m+41}$, $\chi_f(G\cup K_n)=n\ge\chi(G)$. 이 경우 $\chi(G)\le n$ 이므로 Theorem 4 용도로는 $n\le t^{o(1)}$ 이면 충분하다.

### 2. Lemma 8 (쪽 15–19): $h(G)<t$, $\alpha(G)\le m$, $\Delta(D)\le d$ ⇒ $\chi_f(G\cup D)\le 4t+(d+1)^{4m}$

- 핵심 입력: Reed–Seymour $\chi_f(F)\le 2h(F)$ (논문 Theorem 10, 인용 [29] Thm 1.3). [기억-미검증 — 인용으로만 사용]. 증명을 적용하는 대상은 $G$ 자신이 아니라 **유도 부분그래프의 매칭 축약 $G'=G[V(M)]/M$** 이다 ($h(G')\le h(G)<t$). 이 점이 $e^{\sqrt{\log t}}$ 류 곱 경계를 피하는 이유라는 논문 설명은 맞다. [증명]
- Lemma 12 를 $r=2m-1$ 로 적용 ($r+1=2m$): $\sum_R w+\sum|w_u-w_v|\le m(1+\sum_{j=0}^{2m-1}(d+1)^j)<m(1+(d+1)^{2m})$. [계산 확인]
- $w'(\mathrm{ctr}(uv))=\min(w_u,w_v)$. $\chi_f(G')<2t$ 이므로 독립 $J$ 에 대해 $\sum_J w'\ge\frac1{2t}\sum_{uv\in M}\min$ (평균 논법). $\sum_M\min=\tfrac12(\sum_{V\setminus R}w-\sum|\Delta w|)$ 이고 $\sum_{V\setminus R}w=\chi_f(G\cup D)-\sum_R w$. 따라서 $\sum_J w'\ge\frac1{4t}(\chi_f(G\cup D)-m(1+(d+1)^{2m}))$. [계산 확인]
- $N=\{uv\in M:\mathrm{ctr}(uv)\in J\}$, $U=V(N)$. $G[U]=N$ (J 가 G' 에서 독립이므로 N 외의 G-간선이 없음), $|N|\le\alpha(G)\le m$, $|U|\le 2m$. $H=(G\cup D)[U]$ 의 사이클은 길이 $\le 2m=r+1$ 이고 $M\cup D$ 의 사이클이므로 N 간선을 쓰지 않는다 (Lemma 12). [증명]
- Observation 11 (쪽 16): $H$ 에서 $E\setminus N$ 을 축약한 $H'$ 이 숲이 되므로 방향(출차수 ≤1)을 주면 각 N 간선의 시작점 집합 $I$ 가 독립이다. 표준 논법으로 맞다. [증명, 스케치 수준으로 확인]
- 결합: $1\ge\sum_{v\in I}y_v\ge\sum_N\min=\sum_J w'\ge\frac{1}{4t}(\chi_f-m(1+(d+1)^{2m}))$ ⇒ $\chi_f\le4t+m(1+(d+1)^{2m})\le4t+(d+1)^{4m}$. 마지막 부등식은 $d,m\ge1$ 에서 성립. [계산 확인]

### 3. Lemma 12 (쪽 17–22): 짧은 사이클을 피하는 greedy 매칭 — [증명]

- 알고리즘 1: 미처리 정점 중 가중 최대 $v$ 를 골라, $(N_G(v)\cap U)\setminus B^H_r(v)$ 에서 최대 가중 $u$ 와 매칭. 후보가 없으면 $v\in R$. 각 단계 후 $M\cup D$ 에서 새 간선 $uv$ 는 짧은 사이클을 만들지 않고 $M\cap E(D)=\emptyset$ 도 유지됨.
- 기대값 재해석: 균등 $t\in[0,1]$, $X_t=\{v\in R:w_v\ge t\}\cup\{\text{매칭 쌍의 무거운 끝점 } v: w_u<t<w_v\}$ 에 대해 $\mathbb E|X_t|=\sum_R w+\sum|w_u-w_v|$. [계산 확인]
- 핵심 보조 주장 (쪽 21): $x_i\in X_t$ 의 나중 이웃 $x_j\in X_t$ 는 $B^{M\cup D}_r(x_i)$ 안에 있다. 귀류: $x_i$ 는 argmax 로 처리되었고 (partner 가 더 무거우면 $x_i\notin X_t$), $x_j$ 가 밖이면 $x_i$ 는 매칭되며 partner $u$ 에 대해 $w_u\ge w_{x_j}\ge t>w_u$. 모순. $M'\subseteq M$ 과 $B^{M'\cup D}\subseteq B^{M\cup D}$ 를 쓰는 단계도 맞다. [증명]
- 따라서 $G[X_t]$ 는 $\sum_{j=0}^r(d+1)^j$-퇴화, $\chi\le1+\sum(d+1)^j$, $|X_t|\le\alpha\chi\le m(1+\sum)$, 기댓값 취하면 Lemma 12. [증명]

### 4. Theorem 5 (쪽 26–27): $\mathrm{LH}(\alpha)\Rightarrow\mathrm{LH}(\tfrac43\alpha)$ — [증명]

- 설정: $k=(\log t)^{\alpha/3}$. $h(G)<t$, $v(G)\le t(\log t)^{4\alpha/3}$.
- (i) 서로소 큰 연결 유도 이분 부분그래프 $H_1..H_m$ ($v>k$) 를 극대로 뽑아 $U_1$. $G_1$ 의 축약 $G_1'$ 은 $v(G_1')=m\le v(G)/k\le t(\log t)^\alpha$, $h(G_1')<t$, 따라서 $\mathrm{LH}(\alpha)$ 로 $\chi(G_1')\le C_\alpha t$. 각 $H_i$ 가 이분이므로 Lemma 13 ($s=2$): $\chi(G_1)\le 2C_\alpha t$. [증명]
- (ii) $G_2=G[V\setminus U_1]$: 연결 이분 유도부분그래프는 모두 $\le k$ 정점 ($b(G_2)\le k$). Lemma 16 (Gyárfás 경로 + 색수 감소, 쌍 $(U,v)$ 극대 선택) 과 Cor 17 ($\chi_f\le 2h$ 와 $\alpha(J)\le k(k-1)$ 로 $v(J)\le 2ak^2$).
  - Cor 17 의 가설 "$h(J)<a$, $v(J)\le 2ak^2\Rightarrow\chi(J)\le s$" 을 $\mathrm{LH}(\alpha)$ 로 확인: $2ak^2=2a(\log t)^{2\alpha/3}\le a(\log a)^\alpha$ ($t$ 충분히 큼, $a\ge t/\sqrt{\log t}$). 그러면 $\chi(J)\le C_\alpha a$. 따라서 $s\ge C_\alpha a$ 이면 Cor 17 이 $h(H)\ge a$ 를 주어 모순. 즉 $s<C_\alpha a$, $f(G_2,t)\le C_\alpha$. [증명, 조건 확인]
  - Theorem 15 (DP 형 분리 정리, 부록 B): $\chi(G_2)\le C_{\rm sep}(1+C_\alpha)t$. [부록 B 는 골격과 B.12 의 구조만 확인, 상수 체인은 skim]
- 결합: $\chi(G)\le\chi(G_1)+\chi(G_2)\le(2C_\alpha+C_{\rm sep}(1+C_\alpha))\,t=C't$. [증명]
- **부트스트랩 산술.** $\tfrac13(\tfrac43)^{10}=\dfrac{4^{10}}{3^{11}}=\dfrac{1048576}{177147}\approx5.9192\ge5$. [계산 확인, python 으로 확인] 출발점은 정리 4 가 주는 $\mathrm{LH}(\tfrac12-\varepsilon)$ 이고, $\tfrac12-\varepsilon\ge\tfrac13$ 이므로 $\mathrm{LH}(\tfrac13)$ 에서 시작해 10 번 반복하면 $\mathrm{LH}(5.919)$. $\mathrm{LH}(\beta)\Rightarrow\mathrm{LH}(\alpha)$ ($\alpha\le\beta$) 는 가설 $v\le t\log^\alpha t$ 가 더 강하므로 맞다. 따라서 $\mathrm{LH}(5)$. [증명]

### 5. 정리 2 로의 연결 (요약 기준, 미재독)

- 요약대로: Delcourt–Postle 축소 (정리 3, $v\le t\log^5t$) 에 $\mathrm{LH}(5)$ 를 넣어 전체 선형 Hadwiger. 쪽 2–4 는 본 연구원이 재독하지 않았다.

### 6. Theorem 9 (부록 A, 쪽 31–36): 가중 Pippenger — 증명 흐름

- 도구: Rödl nibble 의 한 단계를 Lemma A.3 로 떼어 쓰고, Lemma A.4 에서 $\lceil D\rceil$ 에 대한 귀납으로 반복. Efron–Stein (Prop A.1) → Bernoulli 분산 상계 (Cor A.2) 를 쓴다.
- Lemma A.3 의 확률 구성: 간선 $e\in M_0$ 확률 $1-\exp(-ax_e/D)$ (무거운 간선 선호), 정점 $Z_0$ 확률 $1-\exp(-a(1-d(v)/D))$ (낮은 차수 정점 선호). $M$ = $M_0$ 중 다른 $M_0$ 간선과 서로소인 것. $U=V\setminus(V(M_0)\cup Z_0)$ 위에서 가중을 줄여 $\Delta(H')\le D'=De^{-a(r-1)}$.
  - 생존 확률 $\Pr(S\subseteq U)\ge\exp(-a|S|+a|S|^2\Delta_2/(2D))$ (식 10, 12). [계산 확인]
  - Claim A.3.1 $\mathbb E|M|\ge \frac{ae^{-ar}}{D}\mathsf e(\mathcal H)$ — 간선별 확률 계산 확인. [증명]
  - Claim A.3.2 $\mathbb EW\le\frac{D'a^2}{2}n$: 분산은 Cor A.2 + Cauchy–Schwarz, $\Delta_2\le a^3D/(64r^2)$ 대입으로 $\mathbb EW\le e^{-a}na^2D(\tfrac18+\tfrac{a^2}{64})\le\tfrac12a^2D'n$ ($e^{-a}D=e^{a(r-2)}D'\le2D'$). [계산 확인]
  - (17) $1-ae^{-ar}-e^{-a}\le ra^2$: $e^{-a}\ge1-a$, $e^{-ar}\ge1-ar$ 로 증명. [증명]
- Lemma A.4: 귀납 ($D-D'\ge aD/2\ge1$ 로 $\lceil D\rceil$ 감소). 핵심 부등식 $e^{-a/2}+e^{a(r-1)/(2r)}\le 2-\frac{a}{2r}+\frac{3a^2}{8}\le2$ ($a<\frac1{8r}$). [계산 확인]
- Theorem 9: $D=1$, $\mathrm{def}(1,\mathcal H)\le\mu v(\mathcal H)$, $\Delta_2\le\mu$. A.4 로 덮지 않는 정점 $\le(\mu+\xi/2)v\le\xi v$. 이때 $(2^{15}r^5\mu)^{1/2r}\le\xi/2$ 는 $\mu=(\xi/100)^{20r}$ 로 충족 ($100^{20r}\ge2^{2r+15}r^5$ for $r\ge2$). [계산 확인]

---

## 기존 요약 (SRC-norin-steiner-2610.05291.md) 의 오류·보완

1. **[오류] 줄 17 (S1 관련).** "τ 는 χ 의 하한이므로 χ 상한은 τ 상한을 주지 않는다" 는 틀렸다. $\tau\le\chi$ 이므로 $\chi\le Ch$ 에서 $\tau\le Ch$. 즉 선형 S1 이 조건부로 나온다. 정정 필요. (problem.md 21행, STATUS 12·78행과 일치하는 쪽이 맞다.)
2. **[보완] 쪽 27, Cor 18.** $\chi\le C\,h_o$ (홀수 마이너). Steiner [34] 의 "$\chi\le f(h)\Rightarrow\chi\le2f(h_o)$" 를 쓴다 (인용, [기억-미검증]). 따라서 $\tau\le 2C\,h_o$, 즉 **선형 홀수 판 (S2 의 선형 약화)** 도 τ 에 나온다. 요약에 빠져 있었다.
3. **[정정] 쪽 13 의 μ 오타** ($3000\to300$), 위 1(d) 참조.
4. **[보완] 요약 줄 33 의 $\exp(8(\log t)^{1-\varepsilon/2})$.** 본 연구원 산술: 지수는 $\approx80\,m^2\log(m/\gamma)$, $m\approx(\log t)^{1/2-\varepsilon/2}$ 이므로 $\exp(O((\log t)^{1-\varepsilon}\log\log t))$ 이고 이는 $\exp(8(\log t)^{1-\varepsilon/2})$ 보다 작다. 상한으로는 타당. [계산 확인; γ 선택은 쪽 8 미재독]
5. **[보완] Lemma 7 의 $n$ 가정.** 요약은 "$n$ 가정 없음" 으로 적었으나 논문 증명은 $n\ge(600(m+2)/\gamma)^{20m+40}$ 을 가정한다. 나머지 경우는 $D=K_n$ 으로 처리 가능 (위 1(e)).

---

## 우리 τ 과제와의 관계

**(A) 직접 함의 (논문이 맞다는 조건).**
- $\tau(G)\le\chi(G)\le C\,h(G)$: 선형 S1 (τ 판). 상수 $C$ 는 논문에서 $10^{10}$–$10^{100}$ 정도로 추정 (쪽 28, 최적화하지 않음). [증명, 조건부: 논문 증명 및 $\tau\le\chi$ 의 문헌 확인에 의존]
- $\tau(G)\le 2C\,h_o(G)$: 선형 홀수 판. [증명, 조건부 + Steiner 인용]
- 주의: 이는 S1 의 **정확한 형** ($\tau\ge t\Rightarrow K_t$ 마이너, 상수 1) 이 아니다. S2, S3, S4, S5 의 정확한 형에 대해서는 아무 정보도 주지 않는다. 요약의 나머지 결론 ("S1 정확형에 대한 새 정보 없음") 은 맞다.

**(B) 분수화 + 보조 간선 + 가중 매칭 기법의 τ 이식 가능성 — 부정적 판단이 우세하다.**
- **결정적 장애:** $\tau(C_5)=3$ (problem.md 가 $\tau(C_{2k+1})=3$ 로 기재; 본 보고서에서는 독립 재확인하지 않음) 이고 $\chi_f(C_5)=5/2$. 따라서 $\tau\le\chi_f(\cdot)+\text{작은 오차}$ 형태의 부등식은 $C_5$ 에서 이미 실패한다. Lemma 8 이 χ_f 상계를 주는 구조를 τ 에 그대로 쓸 수 없다. [증명, 조건부]
- Lemma 7 의 $\gamma n$ 오차는 χ 의 선형 목표에서는 문제없지만, τ 가 정수 위상 불변량이라 분수적 완화는 정수성을 잃는다.
- Observation 11 (독립 선택) 과 Lemma 12 (짧은 사이클 회피 greedy) 는 조합적·사이클 구조에 의존한다. τ 는 위상 불변량이므로 이 구조를 옮길 대응 객체가 현재 없다. [추측]
- **Lemma 13 (축약 상계 $\chi(G)\le s\chi(G')$) 의 τ 판은 성립하지 않는다.** STATUS 77행의 "덧셈형 축약 보조정리 $\tau(G)\le\tau(G/F)+1$ 거짓 ($K_4\to K_2$)" 이 이를 막는다. 따라서 정리 5 의 부트스트랩 구조를 τ 에 그대로 옮길 수 없다. [증명, STATUS 인용]
- **Delcourt–Postle 색수 분리 (쪽 24, Def. 의 $s$-chromatic-separable)** 는 τ 판을 정의할 수 있으나, "$\tau(H_i)\ge\tau(G)-s$ 인 서로소 두 부분" 을 보장하는 분할 정리가 τ 에 대해서는 증명되어 있지 않다. [추측]
- 가능성이 남는 부분: τ 는 부분그래프에 단조이고 (STATUS 85), 독립 집합 대신 "연결 이분 축약" 의 위상적 대응을 찾으면 정리 5 의 두 가지 축 (축약 + 서브그래프 분리) 가 τ 에도 필요할 수 있다. 이것은 열린 질문이다.

---

## 문주님께 요청

1. **(권장, 우선도 높음) Reed–Seymour, "Fractional colouring and Hadwiger's conjecture", *J. Combin. Theory Ser. B* 74 (1998) 147–152 원문.** 이유: Lemma 8 의 입력 $\chi_f\le2h$ (논문 Theorem 10) 이 논문 증명 전체의 최하위 기둥이다. 현재 우리는 인용만 가지고 있다. 없을 때 대안: 논문 쪽 15 의 진술을 인용으로 두고 [기억-미검증] 표기 유지.
2. **(선택) Delcourt–Postle, arXiv:2108.01633v5 원문.** 이유: 정리 14 (쪽 24) 의 원 증명과 Thm 1.6/7.1 대조. 없을 때 대안: 부록 B 의 적응본을 쓰되 상수 체인은 미검증으로 둔다.
3. **(선택) Lean 저장소 `github.com/snorin239/LinearHadwiger` 접근 허용 여부.** 이유: Lemma 7/8·정리 2 의 형식화 범위를 확인해 AI 생성 증명의 신뢰도를 올린다. 없을 때 대안: "AI 생성, 독립 검증 전" 표기 유지.

결정 사항 (문주님 판단 요청 아님): 선형 S1 (τ 판) 을 STATUS 에 "조건부 참" 으로 올릴지는 오케스트레이터가 결정한다.

---

## 후속연구 지점

1. **[우선순위 1] τ 용 분수 대체 객체 탐색 (χ_f 를 대체하는 Z_2-위상 분수 판).**
   - 이유: 이 논문의 상계 전체가 χ_f 에 의존하고, 그 χ_f 는 τ 와 정수성에서 어긋난다 ($C_5$: 5/2 vs 3). τ 에 대한 Lemma 8 류 부등식을 찾는 것이 이식의 가장 직접적인 경로다.
   - 시작 방법: $C_5$, $K_n$, $C_5[K_2]$ 에서 "τ ≤ f(…)" 형 후보 식을 세우고, 위상 쪽 대응 (coind 기반 가중 독립 개념) 을 정의한 뒤 연역적으로 증명 시도. 수치 점검은 근거로 쓰지 않는다.
   - 난점: 위상 쪽의 "분수 색칠" 대응이 정의되어 있지 않다. [추측]
2. **[우선순위 2] 선형 S1-τ 조건부 사슬을 STATUS 에 명시.** 사슬: $\tau\le\chi$ (정의상, problem.md) $\wedge$ $\chi\le Ch$ (논문 정리 2, AI 생성 증명, 독립 검증 전). 상수 $C$ 의 추정 범위와 홀수 판 $\tau\le2Ch_o$ 를 함께 기록.
   - 이유: 요약 줄 17 의 오류를 바로잡고, S1 의 상수 1 판과 선형 판의 차이를 분명히 한다.
   - 시작 방법: SRC 요약 정정 + STATUS 표에 행 추가. (본 연구원은 파일을 수정하지 않았다.)
   - 난점: 독립 검증 불가 (Lean 미접속).
3. **[우선순위 3] Lemma 12 의 "짧은 사이클 회피 greedy" 가 τ 의 사이클 구조와 관계 있는지 점검.**
   - 이유: τ(C_{2k+1})=3, τ(C_5[K_2])=4 등 사이클 구조에 민감한 값이 있으므로, τ 가 짧은 사이클 제약에 어떻게 반응하는지 알면 greedy 구조의 이식 가능성을 판단할 수 있다.
   - 시작 방법: 짧은 사이클이 없는 그래프족 (예: 둘레(girth)가 큰 그래프족) 에서 τ 값의 변화를 연역적으로 추적. 수치 전수는 하지 않는다.
   - 난점: τ 는 마이너 단조가 아니다 (STATUS 86). 짧은 사이클 제약을 τ 의 단조 구조와 맞추기 어렵다.
4. **[우선순위 3] Delcourt–Postle 색수 분리의 위상 판 정의 여부.** 이유: 정리 15 의 "$s$-chromatic-inseparable" 은 τ 로 옮기면 "$s$-τ-inseparable" 이 되고, 이것이 Gyárfás 경로 논법을 살리는지 확인할 가치가 있다. 시작 방법: 정의만 적고, $\tau(G)=\tau(H_1)$ 류 단조성 보조정리를 먼저 증명. 난점: 분할 보조정리를 위상적으로 보장하는 방법이 불명확하다. [추측]

---

## 보고 한 줄

- 논문 쪽 13–41 + 10–12 를 정독했고, Lemma 7·8, Lemma 12, Theorem 5 (부트스트랩 산술 5.919 ≥ 5 포함), Theorem 9 의 흐름은 맞다. Reed–Seymour 와 DP 등 인용 정리는 [기억-미검증].
- 기존 요약의 "S1 에 새 정보 없음" 은 방향 오류. $\tau\le\chi\le Ch$ 이므로 선형 S1 (τ 판, 조건부) 과 선형 홀수 판이 나온다.
- 분수화 기법의 τ 이식은 $\tau(C_5)=3>\chi_f(C_5)=5/2$ 때문에 막힌다. τ 용 위상 분수 대체 객체가 우선 과제다.
