import networkx as nx, itertools, random
from networkx.generators.atlas import graph_atlas_g
from b0lib import tau_h
from radon import search
random.seed(3)
gs=[G for G in graph_atlas_g() if G.number_of_nodes()==7 and nx.is_connected(G) and G.number_of_edges()>=9]
random.shuffle(gs)
gap=0;ex=0
for G in gs[:40]:
    n=7
    L=0
    for r in range(1,n+1):
        for S in itertools.combinations(G.nodes(),r):
            L=max(L,tau_h(G.subgraph(S).copy().__class__(nx.convert_node_labels_to_integers(G.subgraph(S)))))
    U=None
    for d in range(max(1,L-1),7):
        Y,s,_=search(G,d,iters=120)
        if Y is not None: U=d+1;break
    chi=max(nx.coloring.greedy_color(G,'DSATUR').values())+1
    print(sorted(G.edges()) if L!=U else "", "L=",L,"U=",U,"chi<=",chi,"omega",max(len(c) for c in nx.find_cliques(G)),flush=True)
    if L==U: ex+=1
    else: gap+=1
print("exact",ex,"gap",gap)
