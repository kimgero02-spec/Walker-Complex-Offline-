import random, itertools
random.seed(2)
def orient(p,q,r): return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
def segx(P,e,f):
    a,b=e;c,d=f
    if len({a,b,c,d})<4: return False
    return orient(P[a],P[b],P[c])*orient(P[a],P[b],P[d])<0 and orient(P[c],P[d],P[a])*orient(P[c],P[d],P[b])<0
E=list(itertools.combinations(range(6),2))
for t in range(200000):
    P=[(random.randint(0,40),random.randint(0,40)) for _ in range(6)]
    if any(orient(*[P[i] for i in s])==0 for s in itertools.combinations(range(6),3)): continue
    C=[(e,f) for e,f in itertools.combinations(E,2) if segx(P,e,f)]
    if max(sum(1 for c in C if e in c) for e in E)<=1:
        print("K6 straight 1-planar: points",P,"crossings",C); break
