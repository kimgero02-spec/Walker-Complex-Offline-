# R48: CEGAR for lists L(v)={5,6} ∪ M(v), M(v) 2-subset of {1..4}.
# Find M making planar G not L-colorable, or prove none exists (UNSAT).
import itertools, sys, networkx as nx
from pysat.solvers import Cadical153
PAIRS=list(itertools.combinations([1,2,3,4],2))
def color(G,L):
    s=Cadical153(); var={}
    n=0
    for v in G:
        for c in L[v]:
            n+=1; var[v,c]=n
        s.add_clause([var[v,c] for c in L[v]])
    for u,w in G.edges():
        for c in set(L[u])&set(L[w]): s.add_clause([-var[u,c],-var[w,c]])
    if not s.solve(): return None
    m=set(x for x in s.get_model() if x>0)
    return {v:c for (v,c),x in var.items() if x in m and True} and {v:[c for c in L[v] if var[v,c] in m][0] for v in G}
def cegar(G,fix=None,verbose=False):
    s=Cadical153(); mv={}; n=0
    for v in G:
        for p in PAIRS: n+=1; mv[v,p]=n
        s.add_clause([mv[v,p] for p in PAIRS])
        for p,q in itertools.combinations(PAIRS,2): s.add_clause([-mv[v,p],-mv[v,q]])
    if fix:
        for v,p in fix.items(): s.add_clause([mv[v,p]])
    it=0
    while s.solve():
        m=set(x for x in s.get_model() if x>0)
        M={v:[p for p in PAIRS if mv[v,p] in m][0] for v in G}
        L={v:[5,6]+list(M[v]) for v in G}
        c=color(G,L); it+=1
        if c is None: return M,it
        cl=[mv[v,p] for v in G if c[v]<=4 for p in PAIRS if c[v] not in p]
        s.add_clause(cl)
        if verbose and it%200==0: print(it,flush=True)
    return None,it
if __name__=="__main__":
    G=nx.icosahedral_graph()
    print(cegar(G,fix={0:(1,2)},verbose=True))
