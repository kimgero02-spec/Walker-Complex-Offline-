import networkx as nx, time
from b0 import betti_min
def circ(n,ks):
    G=nx.Graph(); G.add_nodes_from(range(n))
    for i in range(n):
        for k in ks: G.add_edge(i,(i+k)%n)
    return G
for n,ks in [(9,(1,2,3)),(10,(1,2,3)),(11,(1,2,3))]:
    t=time.time(); print(n,ks,betti_min(circ(n,ks)),round(time.time()-t,1),flush=True)
