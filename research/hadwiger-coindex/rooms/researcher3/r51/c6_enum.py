# count partitions of diagonals of convex K_n (n even) into n/2 non-crossing layers (=triangulations), up to layer relabel; compare with zigzag orbit
import itertools
from pysat.solvers import Glucose4
def cross(e,f):
    a,b=e;c,d=f
    if len({a,b,c,d})<4: return False
    return (a<c<b)!=(a<d<b)
for n in [6,8,10]:
    k=n//2
    D=[e for e in itertools.combinations(range(n),2) if (e[1]-e[0]) not in (1,n-1)]
    v=lambda i,c:i*k+c+1
    s=Glucose4()
    for i in range(len(D)):
        s.add_clause([v(i,c) for c in range(k)])
        for c,d in itertools.combinations(range(k),2): s.add_clause([-v(i,c),-v(i,d)])
    for i,j in itertools.combinations(range(len(D)),2):
        if cross(D[i],D[j]):
            for c in range(k): s.add_clause([-v(i,c),-v(j,c)])
    parts=set(); cnt=0
    while s.solve():
        m=set(x for x in s.get_model() if x>0)
        col=[next(c for c in range(k) if v(i,c) in m) for i in range(len(D))]
        P=frozenset(frozenset(D[i] for i in range(len(D)) if col[i]==c) for c in range(k))
        parts.add(P); cnt+=1
        s.add_clause([-v(i,col[i]) for i in range(len(D))])
        if cnt>200000: break
    # orbit of dihedral group on partitions
    def act(P,g):
        return frozenset(frozenset(tuple(sorted((g(a),g(b)))) for a,b in L) for L in P)
    orbits=[];seen=set()
    G=[(lambda r:lambda x:(x+r)%n)(r) for r in range(n)]+[(lambda r:lambda x:(r-x)%n)(r) for r in range(n)]
    for P in parts:
        if P in seen: continue
        orb={act(P,g) for g in G}; seen|=orb; orbits.append(len(orb))
    print("n",n,"partitions",len(parts),"dihedral orbits",len(orbits),"orbit sizes",orbits)
    for P in parts:
        L=list(P)
        Xs=sorted(sum(cross(e,f) for e in A for f in B) for A,B in itertools.combinations(L,2))
        ham=[ (lambda A: max(sum(1 for e in A if x in e) for x in range(n)))(A) for A in L]
        print("   pairwise X",Xs," max diag-degree per layer",ham)
