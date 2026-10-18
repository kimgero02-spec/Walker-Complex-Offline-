# vertex arboricity <=2 test (two induced forests) via SAT + cycle CEGAR
import networkx as nx, sys
from pysat.solvers import Cadical153
from tri import dual
from gstar import W
def ff(G):
    idx={v:i+1 for i,v in enumerate(G)}; s=Cadical153()
    for t in [c for c in nx.enumerate_all_cliques(G) if len(c)==3]:
        s.add_clause([idx[v] for v in t]); s.add_clause([-idx[v] for v in t])
    while s.solve():
        m=set(x for x in s.get_model() if x>0)
        A=[v for v in G if idx[v] in m]; B=[v for v in G if idx[v] not in m]; done=True
        for X,sg in ((A,-1),(B,1)):
            try: c=nx.find_cycle(G.subgraph(X)); s.add_clause([sg*idx[u] for u,_ in c]); done=False
            except nx.NetworkXNoCycle: pass
        if done: return A
    return None
for name,G in [('T25',dual(nx.tutte_graph())),('W',W()),('G46',nx.read_edgelist('gstar46.edgelist',nodetype=int))]:
    print(name,'two-forest partition:',ff(G) is not None)
