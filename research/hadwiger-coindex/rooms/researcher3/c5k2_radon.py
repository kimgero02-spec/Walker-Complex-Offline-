import networkx as nx, sys
from radon import *
G=nx.convert_node_labels_to_integers(nx.lexicographic_product(nx.cycle_graph(5),nx.complete_graph(2)))
print(len(max_pairs(G)),flush=True)
for d in (3,4):
    for seed in range(6):
        Y,s,_=search(G,d,iters=400,seed=seed)
        print("d",d,"seed",seed,"found" if Y is not None else ("none",s),flush=True)
        if Y is not None:
            np.save(f"c5k2_d{d}.npy",Y);break
