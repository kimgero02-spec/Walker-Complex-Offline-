import networkx as nx, itertools
from b0lib import *
from radon import *
def groetzsch(): return nx.convert_node_labels_to_integers(nx.mycielski_graph(4))
def kneser(n,k):
    V=list(itertools.combinations(range(n),k)); G=nx.Graph(); G.add_nodes_from(range(len(V)))
    for i,a in enumerate(V):
        for j,b in enumerate(V):
            if i<j and not set(a)&set(b): G.add_edge(i,j)
    return G
for nm,G in [("Groetzsch",groetzsch()),("KG(6,2)",kneser(6,2)),("KG(7,2)",kneser(7,2))]:
    print(nm,G.number_of_nodes(),"tau_h",tau_h(G),flush=True)
    for d in range(2,7):
        Y,s,npairs=search(G,d,iters=200)
        print(nm,"d",d,"found" if Y is not None else "none",npairs,flush=True)
        if Y is not None: break
