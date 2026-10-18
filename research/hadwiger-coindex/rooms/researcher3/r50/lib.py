import networkx as nx, itertools
from pysat.solvers import Glucose3
def colorable(G, q, pre=None, allowed=None):
    """q-colorability with optional precolor dict pre{v:c} and allowed{v:set}"""
    V=list(G); idx={v:i for i,v in enumerate(V)}
    var=lambda v,c: idx[v]*q+c+1
    s=Glucose3()
    for v in V:
        cols=range(q) if not allowed or v not in allowed else allowed[v]
        s.add_clause([var(v,c) for c in cols])
        for c in range(q):
            if c not in cols: s.add_clause([-var(v,c)])
    for u,w in G.edges():
        for c in range(q): s.add_clause([-var(u,c),-var(w,c)])
    if pre:
        for v,c in pre.items(): s.add_clause([var(v,c)])
    r=s.solve(); m=s.get_model() if r else None; s.delete()
    if not r: return None
    return {v:c for v in V for c in range(q) if m[var(v,c)-1]>0}
def partitions(L):
    if not L: yield []; return
    f=L[0]
    for p in partitions(L[1:]):
        for i in range(len(p)): yield p[:i]+[[f]+p[i]]+p[i+1:]
        yield [[f]]+p
def indep_partition(G,p):
    return all(not G.has_edge(a,b) for b_ in p for a,b in itertools.combinations(b_,2))
def realized(G,W,q):
    """S_q(G,W): independent partitions of W realized by a q-coloring"""
    out=[];allI=[]
    for p in partitions(list(W)):
        if not indep_partition(G,p) or len(p)>q: continue
        allI.append(p)
        pre={v:i for i,b in enumerate(p) for v in b}
        # also blocks must be distinct colors: enforced by precolor distinct ints
        if colorable(G,q,pre) is not None: out.append(p)
    return out, allI
def chrom_poly(G):
    """chromatic polynomial via independent-set partitions: sum a_k x^(k falling)"""
    import sympy as sp
    x=sp.Symbol('x'); V=list(G); cnt={}
    adj={v:set(G[v]) for v in V}
    def rec(rem,k):
        if not rem: cnt[k]=cnt.get(k,0)+1; return
        f=rem[0]; rest=rem[1:]
        cand=[v for v in rest if v not in adj[f]]
        # choose independent set containing f from cand
        def grow(i,S,forb):
            if i==len(cand):
                rec([v for v in rest if v not in S],k+1); return
            v=cand[i]
            grow(i+1,S,forb)
            if v not in forb: grow(i+1,S|{v},forb|adj[v])
        grow(0,frozenset(),adj[f])
    rec(V,0)
    P=sum(c*sp.ff(x,k) for k,c in cnt.items())
    return sp.expand(P),x
