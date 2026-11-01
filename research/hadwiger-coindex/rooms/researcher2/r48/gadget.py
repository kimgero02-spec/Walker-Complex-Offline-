# Gadget search: H planar, x,y adjacent precolored (alpha,beta); find M on other vertices
# so that precoloring does not extend to L-coloring, L(v)={5,6} ∪ M(v).
import itertools, networkx as nx
from pysat.solvers import Cadical153
PAIRS=list(itertools.combinations([1,2,3,4],2))
def extend(G,L,pre):
    s=Cadical153(); var={}; n=0
    for v in G:
        cs=[pre[v]] if v in pre else L[v]
        for c in cs: n+=1; var[v,c]=n
        s.add_clause([var[v,c] for c in cs])
    for u,w in G.edges():
        for c in range(1,7):
            if (u,c) in var and (w,c) in var: s.add_clause([-var[u,c],-var[w,c]])
    if not s.solve(): return None
    m=set(x for x in s.get_model() if x>0)
    return {v:c for (v,c),x in var.items() if x in m}
def gadget(G,pre):
    inner=[v for v in G if v not in pre]
    s=Cadical153(); mv={}; n=0
    for v in inner:
        for p in PAIRS: n+=1; mv[v,p]=n
        s.add_clause([mv[v,p] for p in PAIRS])
        for p,q in itertools.combinations(PAIRS,2): s.add_clause([-mv[v,p],-mv[v,q]])
    it=0
    while s.solve():
        m=set(x for x in s.get_model() if x>0)
        M={v:[p for p in PAIRS if mv[v,p] in m][0] for v in inner}
        L={v:[5,6]+list(M[v]) for v in inner}
        c=extend(G,L,pre); it+=1
        if c is None: return M,it
        s.add_clause([mv[v,p] for v in inner if c[v]<=4 for p in PAIRS if c[v] not in p])
    return None,it
if __name__=="__main__":
    G=nx.icosahedral_graph(); x,y=0,1; assert G.has_edge(x,y)
    for pre in [(5,6),(5,1),(1,2)]:
        print(pre, gadget(G,{x:pre[0],y:pre[1]}),flush=True)
