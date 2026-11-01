import networkx as nx, sys
from radon import *
nm=sys.argv[1]; d0=int(sys.argv[2])
C,m={"C5K3":(5,3),"C7K2":(7,2),"C5K2":(5,2),"C9K2":(9,2)}[nm]
G=nx.convert_node_labels_to_integers(nx.lexicographic_product(nx.cycle_graph(C),nx.complete_graph(m)))
print(nm,G.number_of_nodes(),len(max_pairs(G)),flush=True)
for d in range(d0,d0+3):
    ok=False
    for seed in range(4):
        Y,s,_=search(G,d,iters=300,seed=seed)
        print(nm,"d",d,"seed",seed,"found" if Y is not None else ("none",s),flush=True)
        if Y is not None: ok=True;break
    if ok:break
