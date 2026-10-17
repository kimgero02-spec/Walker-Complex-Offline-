# convex position, no 3 pairwise crossing chords (omega(Cr)<=2): look for chi>=6 (limited tries)
import random, itertools
from pysat.solvers import Glucose4
random.seed(11)
def cross(e,f):
    a,b=e;c,d=f
    if len({a,b,c,d})<4: return False
    return (a<c<b)!=(a<d<b)
def colorable(n,E,k):
    v=lambda i,c:i*k+c+1; s=Glucose4()
    for i in range(n): s.add_clause([v(i,c) for c in range(k)])
    for a,b in E:
        for c in range(k): s.add_clause([-v(a,c),-v(b,c)])
    r=s.solve(); s.delete(); return r
best=0; tries=0; found=None
for n in [7,8,9,10,11,12]:
    for t in range(80):
        tries+=1
        D=[e for e in itertools.combinations(range(n),2)]; random.shuffle(D); E=[]
        for e in D:
            X=[f for f in E if cross(e,f)]
            if any(cross(f,g) for f,g in itertools.combinations(X,2)): continue
            E.append(e)
        k=5
        if not colorable(n,E,5): found=(n,E); break
    if found: break
print("tries",tries,"found chi>=6 with omega<=2:",found)
# also: max edges observed vs 4n-10
