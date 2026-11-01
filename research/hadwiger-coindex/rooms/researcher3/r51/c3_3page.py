# C3: look for a 3-page (convex 3-layer, shared hull) graph with chi>=7 (limited random tries)
import random, itertools, sys
from pysat.solvers import Glucose4
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 0)
def randtri(vs):
    if len(vs)<3: return set()
    a,b=vs[0],vs[-1]; m=random.randrange(1,len(vs)-1)
    s=randtri(vs[:m+1])|randtri(vs[m:])
    if m>1: s.add((vs[0],vs[m]))
    if len(vs)-1-m>1: s.add((vs[m],vs[-1]))
    return s
def colorable(n,E,k):
    v=lambda i,c:i*k+c+1
    s=Glucose4()
    for i in range(n): s.add_clause([v(i,c) for c in range(k)])
    for a,b in E:
        for c in range(k): s.add_clause([-v(a,c),-v(b,c)])
    s.add_clause([v(0,0)])
    r=s.solve(); s.delete(); return r
found=None; tries=0
for n in [9,10,11,12,13,14]:
    for t in range(60):
        tries+=1
        pages=[randtri(list(range(n))) for _ in range(3)]
        E=set((i,(i+1)%n) if i<(i+1)%n else ((i+1)%n,i) for i in range(n))
        for p in pages: E|=p
        if not colorable(n,E,6):
            found=(n,pages,E);break
    if found: break
print("tries",tries, "found chi>=7:", bool(found))
if found:
    n,pages,E=found; print(n,len(E),[sorted(p) for p in pages])
