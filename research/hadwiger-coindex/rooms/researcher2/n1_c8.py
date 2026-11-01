import networkx as nx, itertools, time
from b0 import betti_min, simplices
def circ(n,ks):
    G=nx.Graph(); G.add_nodes_from(range(n))
    for i in range(n):
        for k in ks: G.add_edge(i,(i+k)%n)
    return G
t=time.time()
for n in (7,8):
    G=circ(n,(1,2))
    S,_=simplices(G)
    print(n,len(S),betti_min(G),time.time()-t)
