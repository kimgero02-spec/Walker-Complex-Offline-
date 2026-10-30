# 결정적 예 검증 (유리수 좌표, 정확 산술): 각 층 내부 교차 없음, 교차 차수 (c1,c2) 계산
from fractions import Fraction as Fr
import itertools
from twolayer import analyze
def o(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def cr(p,q,r,s): return o(p,q,r)*o(p,q,s)<0 and o(r,s,p)*o(r,s,q)<0
EX={6:[(0.314,0.288),(0.139,0.566),(0.14,0.141),(0.146,0.237),(0.894,0.198),(0.031,0.95)],
    7:[(0.296,0.251),(0.805,0.736),(0.483,0.921),(0.154,0.096),(0.552,0.576),(0.889,0.774),(0.43,0.572)],
    8:[(0.3854,0.0574),(0.6772,-0.0313),(0.4064,0.2397),(-0.2655,1.0042),(0.2576,0.3046),(-0.535,-0.9214),(0.5643,1.0236),(0.1985,0.0071)]}
for n,P in EX.items():
    P=[(Fr(str(x)),Fr(str(y))) for x,y in P]; E=list(itertools.combinations(range(n),2))
    # 일반 위치
    assert all(o(P[a],P[b],P[c])!=0 for a,b,c in itertools.combinations(range(n),3))
    key,lay,ncr=analyze(P,E)
    L=[[E[i] for i in lay if lay[i]==t] for t in (0,1)]; U=[E[i] for i in range(len(E)) if i not in lay]
    L[0]+=U  # 교차 없는 간선은 층 1 에
    for t in (0,1):
        assert not any(len({*e,*f})==4 and cr(P[e[0]],P[e[1]],P[f[0]],P[f[1]]) for e,f in itertools.combinations(L[t],2))
    deg=lambda e,other: sum(1 for f in other if len({*e,*f})==4 and cr(P[e[0]],P[e[1]],P[f[0]],P[f[1]]))
    c1=max(deg(e,L[1]) for e in L[0]); c2=max(deg(e,L[0]) for e in L[1])
    print(f"K_{n}: 교차 {ncr}, |L1|={len(L[0])}, |L2|={len(L[1])}, (c1,c2)=({c1},{c2})")
    print("  L2 =",L[1])
