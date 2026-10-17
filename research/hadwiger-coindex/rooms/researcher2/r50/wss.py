# W: all partitions with x,y in S, T bipartite, S 2-choosable (ERT). Does the S-component of x always contain a cycle?
from common import *
w=W(); V=list(w)
for bits in itertools.product([0,1],repeat=10):
    S=[v for v,b in zip(V,bits) if b]
    if 'x' not in S or 'y' not in S: continue
    if not nx.is_bipartite(w.subgraph([v for v in V if v not in S])): continue
    if bad_cores(w,S,'ert'): continue
    H=w.subgraph(S); C=H.subgraph(nx.node_connected_component(H,'x'))
    print(sorted(S),'cycles:',nx.cycle_basis(C))
