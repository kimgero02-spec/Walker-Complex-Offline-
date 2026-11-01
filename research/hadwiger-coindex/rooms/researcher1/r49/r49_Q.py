# Problem Q (one decisive attempt): planar B, f:V->{0,1,2,3}. Is there a proper colouring
# c:V->{0..4} with c(v)!=f(v)?  Equivalent to chi(B + K4 attached by f) <= 5.
import networkx as nx, itertools, sys
from pysat.solvers import Minisat22
def colour(G,f):
    V=list(G); idx={v:i for i,v in enumerate(V)}; var=lambda v,c: idx[v]*5+c+1
    s=Minisat22()
    for v in V:
        s.add_clause([var(v,c) for c in range(5) if c!=f[v]])
    for u,v in G.edges():
        for c in range(5): s.add_clause([-var(u,c),-var(v,c)])
    if not s.solve(): return None
    m=set(x for x in s.get_model() if x>0)
    return {v:next(c for c in range(5) if var(v,c) in m) for v in V}
def cegar(G,maxit=5000):
    V=list(G); idx={v:i for i,v in enumerate(V)}; fv=lambda v,a: idx[v]*4+a+1
    S=Minisat22()
    for v in V:
        S.add_clause([fv(v,a) for a in range(4)])
        for a,b in itertools.combinations(range(4),2): S.add_clause([-fv(v,a),-fv(v,b)])
    # symmetry: fix f on one vertex
    S.add_clause([fv(V[0],0)])
    for it in range(maxit):
        if not S.solve(): return ("no bad f",it)
        m=set(x for x in S.get_model() if x>0)
        f={v:next(a for a in range(4) if fv(v,a) in m) for v in V}
        c=colour(G,f)
        if c is None: return ("BAD f found",f)
        # kill colouring c (and its images under perms of {0..3} fixing 4)
        for p in itertools.permutations(range(4)):
            cc={v:(p[c[v]] if c[v]<4 else 4) for v in V}
            S.add_clause([fv(v,cc[v]) for v in V if cc[v]<4])
    return ("undecided",maxit)
ico=nx.icosahedral_graph()
print("icosahedron",cegar(ico)[0])
oct_=nx.octahedral_graph(); print("octahedron",cegar(oct_)[0])
