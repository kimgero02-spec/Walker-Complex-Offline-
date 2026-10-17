import networkx as nx, time, sys
from n1_hom import hom_map
from n1_arclab import arc_label
def circ(n,ks):
    G=nx.Graph(); G.add_nodes_from(range(n))
    for i in range(n):
        for k in ks: G.add_edge(i,(i+k)%n)
    return G
n=int(sys.argv[1])
G=circ(n,(1,2,3))
for k in (3,4):
    t=time.time(); print('C_%d^3'%n,'arc-label k=%d'%k,arc_label(G,k),round(time.time()-t,1),flush=True)
