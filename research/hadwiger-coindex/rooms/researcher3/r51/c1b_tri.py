# min crossings between two diagonal-disjoint triangulations of convex n-gon
import itertools
def cross(e,f):
    a,b=e; c,d=f
    if len({a,b,c,d})<4: return False
    return (a<c<b) != (a<d<b)
def tris(lo,hi):
    # triangulations of polygon lo..hi (consecutive), as sets of diagonals (pairs) excluding edge lo-hi
    if hi-lo<2: return [frozenset()]
    res=[]
    for m in range(lo+1,hi):
        for A in tris(lo,m):
            for B in tris(m,hi):
                s=set(A)|set(B)
                if m-lo>1: s.add((lo,m))
                if hi-m>1: s.add((m,hi))
                res.append(frozenset(s))
    return res
for n in [5,6,7,8,9]:
    T=[t for t in set(tris(0,n-1))]
    best=None; arg=None; allvals=set()
    for A,B in itertools.combinations(T,2):
        if A&B: continue
        x=sum(cross(e,f) for e in A for f in B)
        allvals.add(x)
        if best is None or x<best: best=x; arg=(sorted(A),sorted(B))
    print(n,"#tri",len(T),"min X over disjoint pairs",best,"(2n-7=%d, n-3=%d)"%(2*n-7,n-3),"example",arg, "max", max(allvals) if allvals else None)
