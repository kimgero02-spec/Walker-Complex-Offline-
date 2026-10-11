# [R04-orchestrator-verify] R04 오케스트레이터 독립 재검증 (중간)

- 작성자: 오케스트레이터 / 라운드 4 / 독립 재검증. 대상: `R04-researcher1.md` (블로업 붕괴·Petersen·$C_n^2$).

## 결과
- **$\tau(P[K_2])\le4=\omega$ [계산 확인, 오케스트레이터 새 코드]**: Petersen $P=KG(5,2)$ 의 블로업 $P[K_2]$(20정점)에서 폐포로 극대 완전이분쌍을 전수 열거 → **60개**(연구원의 60개와 일치). 블롭 순서를 **임의로** 3번 섞고(seed 1,2,3) 모멘트 곡선 $t=\mathrm{pos}\cdot m+s+1$ 에 놓았을 때 라벨 변화 수의 최댓값이 매번 **3 = $2m-1=d$**. 따라서 $\tau(P[K_2])\le4$, $\tau\ge\omega=4$ → $\tau(P[K_2])=4=\omega$. 연구원의 "임의 순서에서 작동"과 일치. 일반 $m$ 은 연구원의 정리 3·T 의 증명이 담당하며 오케스트레이터는 구조(타입 분류 → $\psi\le m(\omega-z)$)를 따라가 확인했다.
- **$C_n^2$ 자연 순서 [계산 확인]**: $n=7$ 런 5, $n=8$ 런 4, $n=9..12$ **런 3**(최대 변화 2). 연구원의 정리 C2 ($n\ge9$ 에서 $\tau(C_n^2)=3$), $C_7^2$ 자연 순서 인증서 5, $\tau(C_8^2)\in\{3,4\}$ 열림과 모두 일치.
- 정리 K ($K_{s,s}$-자유 ⇒ $\tau\le2s-1$): 완전이분쌍 $(A,B)$, $|A|\le|B|$ 의 라벨 런 수 $\le2|A|+1$ 이므로 [증명, 오케스트레이터 재도출]. $K_{s,s}$-자유이면 $|A|\le s-1$ 이라 런 $\le2s-1$ ⇒ $Q_{2s-2}$ ⇒ $\tau\le2s-1$. 귀결: **둘레(girth)가 큰 그래프는 색수가 얼마든 $\tau\le3$.** 즉 $\tau$ 하한은 높은 둘레 그래프의 큰 $\chi$ 를 전혀 포착하지 못한다.
- **시험대 결론**: Petersen 블로업은 $\tau>\omega$ 시험대가 아니다. $m\ge\min(n-\omega+1,\operatorname{zig}+\omega-1)$ 이면 어떤 $G$ 든 $\tau(G[K_m])=m\omega$ 라 S1·S2·S4·S5 모두 자명. 남은 시험대 창은 $\lceil\operatorname{zig}/\omega\rceil\le m<m^*$ 뿐(열림).

## 미검증
- 정리 3·T 의 일반 증명 전체를 오케스트레이터가 줄 단위로 검증하지는 않았다(구조·부등식 $\psi\le m(\omega-z)$ 의 틀과 $P[K_2]$, $C_n^2$ 수치만 확인).

## 검증 코드 (`python3 -I orch_blowup.py P 2`)
```python
# 오케스트레이터 독립 검증: 블로업 G[K_m] 의 극대 완전이분쌍을 폐포로 전수 열거하고,
# 임의의 블롭 순서 + 모멘트 곡선(t=pos*m+s+1) 에서 라벨 변화 수의 최댓값을 구한다. (변화 ≤ d 이면 τ ≤ d+1)
import sys, itertools, random
def build(kind):
    if kind=="P":      # Petersen = KG(5,2)
        V=[frozenset(c) for c in itertools.combinations(range(5),2)]
        adj=lambda a,b: not (a&b)
    elif kind.startswith("C2_"):   # C_n^2
        n=int(kind[3:]); V=list(range(n))
        adj=lambda a,b: a!=b and min((a-b)%n,(b-a)%n)<=2
    return V, adj
def run(kind, m, seed):
    V, adj = build(kind); n=len(V)
    N=n*m; ids=[(i,s) for i in range(n) for s in range(m)]; idx={v:k for k,v in enumerate(ids)}
    full=(1<<N)-1; nb=[0]*N
    for (i,s) in ids:
        for (j,t) in ids:
            if (i,s)!=(j,t) and (i==j or adj(V[i],V[j])): nb[idx[(i,s)]] |= 1<<idx[(j,t)]
    com=[full]*(1<<N)
    for mask in range(1,1<<N):
        low=mask & -mask; com[mask]=com[mask^low] & nb[low.bit_length()-1]
    pairs=set()
    for mask in range(1,1<<N):
        B=com[mask]
        if not B: continue
        A2=com[B]; B2=com[A2]
        pairs.add(frozenset([A2,B2]) if A2!=B2 else frozenset([A2]))
    random.seed(seed); order=list(range(n)); random.shuffle(order); pos={u:p for p,u in enumerate(order)}
    tpar={idx[(i,s)]: pos[i]*m+s+1 for (i,s) in ids}
    mx=0
    for pr in pairs:
        L=list(pr); A=L[0]; B=L[1] if len(L)>1 else L[0]
        pts=sorted([(tpar[k],1) for k in range(N) if A>>k&1]+[(tpar[k],-1) for k in range(N) if B>>k&1])
        ch=sum(1 for k in range(len(pts)-1) if pts[k][1]!=pts[k+1][1]); mx=max(mx,ch)
    return len(pairs), mx
kind, m = sys.argv[1], int(sys.argv[2])
for seed in (1,2,3):
    npairs, mx = run(kind, m, seed)
    print(f"{kind}[K_{m}] seed={seed}: 극대쌍 {npairs}, 최대 변화 {mx}  (d=2m-1={2*m-1}) -> {'τ≤'+str(mx+1)}")
```

---

## 추가 (R04-researcher3 최종 보고에 대한 오케스트레이터 점검)
- **7정점 반례 ("$T$ 를 맨 끝에" 접합 불가) [계산 확인, 오케스트레이터 새 코드]**: 간선 15개 평면 삼각분할(정점 0..6)의 극대 완전이분쌍은 13개. $Q_3$(런 $\le4$)을 만족하는 정점 순서는 5040개 중 **852개**, 그중 $T=\{0,2,3\}$ 이 마지막 세 자리인 것은 **0개**, 연속 세 자리인 것은 12개. researcher3 의 값(852 / 0 / 12)과 정확히 일치. 이로써 "자식 삼각분할을 $T$ 마지막에 놓는" 접합은 불가.
- **$d_R(W_{2k+1})=3$ [증명, 오케스트레이터 논리 확인]**: (1) $h\notin\operatorname{conv}\{c_i\}$ 로 허브에서 본 방향이 한 반평면 안에 정렬되고, (2)(3) 두 조건으로 어떤 $c_i$ 도 이웃 둘 사이에 놓일 수 없음(반직선이 선분 $c_{i-1}c_{i+1}$ 에 닿는 점 $p$ 에서 $|hc_i|\ge|hp|$ 이면 (2) 위반, 아니면 (3) 위반). 따라서 모든 $c_i$ 가 국소 극값이고 이웃과 극값 종류가 달라야 하므로 홀수 사이클에서 모순. 상계는 $\chi=4$. 결함 없음.
- 평면 ⇒ $Q_3$ 은 4색정리($\chi\le4$ ⇒ $Q_3$)로 이미 참이다. 따라서 **새 정보는 색칠 없는 증명이 가능한가**이며 연구원도 그렇게 서술했다. 쌍 환원(A.1)·5색칠 환원(B.1)·접합 보조정리(C.2)는 증명되었으나 평면 ⇒ $Q_3$ 의 색칠 없는 증명은 나오지 않았다.
