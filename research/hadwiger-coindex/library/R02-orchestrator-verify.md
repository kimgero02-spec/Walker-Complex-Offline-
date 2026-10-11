# [R02-orchestrator-verify] R02 오케스트레이터 독립 재검증

- 작성자: 오케스트레이터 / 라운드 2 / 독립 재검증

## 1. $C_5[K_3]$ 의 $\tau\le6$ 인증서 (researcher2 의 주장, researcher3 의 망상꾼 #? 값)
- **[계산 확인, 오케스트레이터 독립 재검증]** 오케스트레이터가 새로 짠 코드(아래)로 $C_5[K_3]$(15정점)의 극대 완전이분쌍을 전수 열거했다: 순서쌍 250개, 무방향 125개(researcher2 의 "250" 과 일치). researcher2 의 배치 `C5K3_d5.npy`($\mathbb R^5$)에 대해 각 쌍마다 LP 로 분리 초평면 $(w,c)$ 를 구하고, $w,c$ 를 유리수로 반올림해 **float 의 정확한 유리수 값**에서 $w\cdot y_a-c>0$ ($a\in A$), $<0$ ($b\in B$) 를 모두 확인했다. 실패한 쌍 0개 → 인증서 유효. 따라서 $\tau(C_5[K_3])\le 6$.
- $\tau\ge\omega=6$ ([증명], 부분그래프 단조) → $\tau(C_5[K_3])=6$.
- 이 검증은 researcher2 의 코드를 쓰지 않았다(배치 데이터만 사용).

## 2. $\chi$ 하한에서 블로업 공식을 쓰지 않아도 된다 [증명, 오케스트레이터]
$\chi(G)\ge\lceil n/\alpha(G)\rceil$ (색류는 독립집합이므로). 
- $C_5[K_m]$: $n=5m$, $\alpha=2$ (한 블롭에서 한 점뿐이고 서로 인접하지 않은 블롭은 최대 2개) ⇒ $\chi\ge\lceil 5m/2\rceil$.
- $C_5[K_2]$: $\chi\ge5>4=\tau$. $C_5[K_3]$: $\chi\ge8>6=\tau$. $C_7[K_2]$: $n=14$, $\alpha=3$ ⇒ $\chi\ge\lceil14/3\rceil=5>4=\tau$.
- 연구원들이 `[기억-미검증]` 으로 둔 "블로업 공식 $\chi_f(G[K_m])=m\chi_f(G)$" 는 **필요 없다.** 위 부등식으로 $\tau<\chi$ 가 모두 [증명] 된다.
- 귀결 [증명 조건부]: 만약 $\tau(C_5[K_m])=2m$ 이 모든 $m\ge2$ 에 성립하면 $\chi-\tau\ge\lceil5m/2\rceil-2m=\lceil m/2\rceil\to\infty$ 로 $\tau$ 와 $\chi$ 의 간극은 유계가 아니다 (현재 $m=2,3$ 만 확인, 간극 1, 2).

## 3. 연구원 주장 중 오케스트레이터가 직접 따져 본 것
- $\tau(C_4)=2<3=\tau(K_3)$, $C_4\succ K_3$: [증명] (τ≤χ(C_4)=2, 간선 하나 수축 시 $K_3$). τ 는 마이너 단조 아님.
- $\tau(K_4)>\tau(K_2)+1$: 산수 확인.
- S3 의 τ 판: Steiner 4–5쪽 본문 직접 대조 (`SRC-steiner-2312.17130.md`).
- Hajós 추측 상태(t≤4 참, t=5·6 열림, t≥7 거짓 Catlin): [기억-미검증]. researcher1 의 "t=5 는 Mader/Thomassen" 문장은 의심스럽다.
- 연구원의 "S1-Radon t≤6 성립"은 $d_R\le\chi-1$ 과 Hadwiger($h\le5$ ⇒ $\chi\le5$, Norin–Steiner 1쪽·Steiner 1쪽) 로 정합. 인용 의존.

## 4. 검증 코드 (실행: `python3 -I orch_verify.py <npy> 5 3`)
```python
# 오케스트레이터 독립 검증: C5[K3] 의 R^5 배치가 모든 극대 완전이분쌍을 엄격 분리하는지 (유리수 정확 검사)
import sys, itertools, numpy as np
from fractions import Fraction
from scipy.optimize import linprog
Y = np.load(sys.argv[1]); n_c, m = int(sys.argv[2]), int(sys.argv[3]); d = Y.shape[1]
V = [(i,s) for i in range(n_c) for s in range(m)]; idx = {v:k for k,v in enumerate(V)}; N = len(V)
adj = [[False]*N for _ in range(N)]
for (i,s) in V:
    for (j,t) in V:
        if (i,s)==(j,t): continue
        if i==j or (i-j)%n_c in (1, n_c-1): adj[idx[(i,s)]][idx[(j,t)]] = True
nb = [frozenset(k for k in range(N) if adj[v][k]) for v in range(N)]
def common(S):
    r = set(range(N))
    for v in S: r &= nb[v]
    return frozenset(r)
pairs = set()
for mask in range(1, 1<<N):
    A = frozenset(k for k in range(N) if mask>>k & 1)
    B = common(A)
    if not B: continue
    A2 = common(B)           # 폐포
    pairs.add((A2, common(A2)))   # (A2, B2): A2 = N(B2), B2 = N(A2)
pairs = {p for p in pairs if p[0] and p[1]}
print("n", N, "d", d, "극대 완전이분쌍(비공집합, 순서쌍)", len(pairs))
# 순서쌍 (A,B) 와 (B,A) 는 같은 분리 문제. 무방향 쌍으로 줄인다.
und = {frozenset([p[0], p[1]]) for p in pairs}
print("무방향 쌍", len(und))
Yf = [[Fraction(x) for x in row] for row in Y]       # float 의 정확한 유리수 값
bad = 0; worst = None
for pr in und:
    L = list(pr)
    A, B = sorted(L[0]), sorted(L[-1])  # 두 변
    if len(L)==1: A=B=sorted(L[0])
    # LP: w·a - c >= 1 (a in A), w·b - c <= -1 (b in B), w in [-W,W]
    nvar = d+1
    Aub = []; bub = []
    for a in A: Aub.append([-x for x in Y[a]] + [1.0]); bub.append(-1.0)
    for b in B: Aub.append(list(Y[b]) + [-1.0]); bub.append(-1.0)
    r = linprog(np.zeros(nvar), A_ub=Aub, b_ub=bub, bounds=[(None,None)]*nvar, method="highs")
    if r.status != 0: bad += 1; continue
    w = [Fraction(x).limit_denominator(10**6) for x in r.x[:d]]; c = Fraction(r.x[d]).limit_denominator(10**6)
    ok = all(sum(wi*yi for wi,yi in zip(w,Yf[a])) - c > 0 for a in A) and all(sum(wi*yi for wi,yi in zip(w,Yf[b])) - c < 0 for b in B)
    if not ok: bad += 1
print("실패 쌍 수:", bad, "→", "인증서 유효" if bad==0 else "인증서 무효")
```
