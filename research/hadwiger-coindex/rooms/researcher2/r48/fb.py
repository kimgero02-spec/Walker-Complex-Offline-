# forest + bipartite vertex partition via SAT + cycle CEGAR
import networkx as nx
from pysat.solvers import Cadical153
def fb(G):
    idx={v:i for i,v in enumerate(G)}; n=len(idx)
    t=lambda v: idx[v]+1; b=lambda v: n+idx[v]+1
    s=Cadical153()
    for u,v in G.edges():
        s.add_clause([-t(u),-t(v),b(u),b(v)]); s.add_clause([-t(u),-t(v),-b(u),-b(v)])
    for tri in [c for c in nx.enumerate_all_cliques(G) if len(c)==3]:
        s.add_clause([t(v) for v in tri])
    it=0
    while s.solve():
        m=set(x for x in s.get_model() if x>0); it+=1
        S=[v for v in G if t(v) not in m]
        H=G.subgraph(S)
        try: cyc=nx.find_cycle(H)
        except nx.NetworkXNoCycle: return S,it
        s.add_clause([t(u) for u,_ in cyc])
    return None,it
