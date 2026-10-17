import sys, io, contextlib, itertools
sys.path.insert(0, ".")
with contextlib.redirect_stdout(io.StringIO()):
    from r17_quot import quotient_betti
    from r06_lib import make, B0_empty, reduced_betti
def omega(n,E):
    S=set(map(frozenset,E)); best=1
    for k in range(2,n+1):
        for c in itertools.combinations(range(n),k):
            if all(frozenset((a,b)) in S for a,b in itertools.combinations(c,2)): best=k
    return best
def rep(name,n,E):
    b={k:v for k,v in reduced_betti(B0_empty(make(n,E),n)).items() if v}
    q=quotient_betti(n,E)
    print(name, "omega",omega(n,E), "B0 red F2-ish", b, "quotient", q, flush=True)
C7=[(i,(i+1)%7) for i in range(7)]
comp7=[(a,b) for a,b in itertools.combinations(range(7),2) if (a,b) not in set(map(tuple,C7)) and (b,a) not in set(map(tuple,C7))]
rep("compC7", 7, comp7)
rep("W7 (K1+C7)", 8, C7+[(i,7) for i in range(7)])
rep("C7^2", 7, [(i,(i+1)%7) for i in range(7)]+[(i,(i+2)%7) for i in range(7)])
rep("prism C4xK2 (omega2)", 8, [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)])
rep("C6+K1 wheel", 7, [(i,(i+1)%6) for i in range(6)]+[(i,6) for i in range(6)])
