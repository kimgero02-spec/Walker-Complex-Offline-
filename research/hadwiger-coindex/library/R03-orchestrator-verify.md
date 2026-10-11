# [R03-orchestrator-verify] R03 오케스트레이터 독립 재검증 (중간)

- 작성자: 오케스트레이터 / 라운드 3 / 독립 재검증. 대상: `R03-researcher1-interim.md` (τ(C_n[K_m])=2m 의 모멘트 곡선 구성).

## 결과
- **증명 구조 재도출 [증명, 오케스트레이터]**: 점 $(i,s)\mapsto\gamma(t)=(t,\dots,t^d)$, $t=im+s+1$, $d=2m-1$. 초평면 $w\cdot x=c$ 는 $\gamma$ 위에서 차수 $\le d$ 다항식 $p(t)=w\cdot\gamma(t)-c$ 가 되고, **$p$ 는 차수 $\le d$ 인 임의의 다항식이 될 수 있다**(상수항이 $-c$). 두 점집합 $A,B$ 를 $t$ 순서로 늘어놓았을 때 라벨 변화 수가 $\le d$ 이면 변화 지점 사이에 근을 하나씩 두어 $A$ 에서 $p>0$, $B$ 에서 $p<0$ 인 $p$ 를 만들 수 있다(Gale/Descartes 형 부호 논법). 극대쌍은 (P) 한 블롭 안 부분집합 대 나머지+양옆 블롭, (Q) 인접 두 블롭 안의 분할 두 종류. (Q) 는 점 $2m$ 개라 변화 $\le2m-1=d$. (P) 는 점 $\le3m$ 개이나 라벨이 "양옆 B 블록, 가운데 블롭 혼합"이라 변화 $\le m+1\le2m-1$ ($m\ge2$). 극대쌍 분류는 $n\ge5$ 에서 블롭 $i,i+2$ 의 공통 이웃이 블롭 $i+1$ 뿐이라는 사실에 의존.
- **분류와 구성의 계산 점검 [계산 확인, 오케스트레이터 새 코드]** (`orch_moment.py`, 아래): $(n,m)=(5,2),(5,3),(7,3),(5,4)$ 에서 **폐포(A↦N(N(A))) 전수 열거**로 극대 완전이분쌍을 구하면 무방향 25, 125, 175, 565 개로 연구원 공식 $n(2^m-1)+n(2^m-2)^2/2$ 와 **일치**. 각 쌍마다 근을 변화 지점의 중점에 두는 다항식 $\prod(x-r_j)$ 의 부호를 유리수로 정확히 평가해 모든 점이 올바른 쪽에 있음을 확인: 실패 0, 최대 변화 수는 정확히 $2m-1=d$ (여유 없음, 경계에서 성립).
- 따라서 $\tau(C_n[K_m])\le2m$ ($m\ge2,n\ge5$). 하한 $\tau\ge\omega=2m$ 은 [증명]. **$\tau(C_n[K_m])=2m$.** $C_5[K_m]$ 에서 $\chi\ge\lceil5m/2\rceil$ ($R02$-orchestrator-verify §2, $\alpha=2$) ⇒ $\chi-\tau\ge\lceil m/2\rceil$, **간극은 비유계.**
- 위 계산은 $m=2,3,4$ 와 $C_7[K_3]$ 에 대한 증명 점검이며, 일반 $m$ 은 증명이 담당한다.

## 주의
- $d_R$(Radon-free 배치의 최소 차원)이 아니라 $\tau$ 의 상한을 주는 인증서다. $\tau\le d+1$ 은 R01·R02 에서 [증명] 된 방향.
- 이것은 $\tau$ 가 $\chi$ 와 임의로 멀어질 수 있음을 뜻한다. Hadwiger 추측 자체와는 무관하나, τ 로 증명할 수 있는 $\chi$ 하한의 한계를 보여 준다(τ 하한만으로 $K_{\chi}$ 마이너를 얻는 S1 은 $\tau$ 가 작은 이런 족에서는 더 약한 명제가 된다).

## 검증 코드
```python
# 오케스트레이터 독립 검증: C_n[K_m] 의 극대 완전이분쌍 전수 열거(폐포) + 모멘트 곡선 위 분리 다항식 구성(유리수 정확)
import sys
from fractions import Fraction
n, m = int(sys.argv[1]), int(sys.argv[2]); d = 2*m-1
V = [(i,s) for i in range(n) for s in range(m)]; N = len(V); idx = {v:k for k,v in enumerate(V)}
full = (1<<N)-1
nb = [0]*N
for (i,s) in V:
    for (j,t) in V:
        if (i,s)!=(j,t) and (i==j or (i-j)%n in (1,n-1)): nb[idx[(i,s)]] |= 1<<idx[(j,t)]
com = [full]*(1<<N)
for mask in range(1,1<<N):
    low = mask & -mask
    com[mask] = com[mask ^ low] & nb[low.bit_length()-1]
pairs = set()
for mask in range(1,1<<N):
    B = com[mask]
    if not B: continue
    A2 = com[B]; B2 = com[A2]
    pairs.add(frozenset([A2,B2]) if A2!=B2 else frozenset([A2]))
print(f"n={n} m={m}: 극대 완전이분쌍(무방향) {len(pairs)}  (연구원 공식 {n*(2**m-1)+n*(2**m-2)**2//2})")
t = {idx[(i,s)]: i*m+s+1 for (i,s) in V}          # 곡선 γ(t)=(t,...,t^d) 위의 매개변수
maxchg = 0; bad = 0
for pr in pairs:
    L = list(pr); Aset = L[0]; Bset = L[1] if len(L)>1 else L[0]
    pts = sorted([(t[k], +1) for k in range(N) if Aset>>k&1] + [(t[k], -1) for k in range(N) if Bset>>k&1])
    chg = [(Fraction(pts[k][0]+pts[k+1][0],2)) for k in range(len(pts)-1) if pts[k][1]!=pts[k+1][1]]
    maxchg = max(maxchg, len(chg))
    if len(chg) > d: bad += 1; continue
    # 다항식 p(x)=Π(x-r), 부호를 첫 점 라벨에 맞춤. 차수 = len(chg) ≤ d 이므로 초평면 w·γ(x)-c 로 표현 가능
    def sgn(x):
        v = 1
        for r in chg: v *= (x - r)
        return 1 if v>0 else -1
    s0 = pts[0][1]*sgn(pts[0][0])
    if not all(pts[k][1] == s0*sgn(pts[k][0]) for k in range(len(pts))): bad += 1
print("최대 부호변화", maxchg, " 허용 d =", d, " 실패 쌍", bad, "→", "상한 τ ≤ %d 성립"%(d+1) if bad==0 else "실패")
```
