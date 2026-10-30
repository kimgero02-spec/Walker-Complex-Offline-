import networkx as nx
from r21_shadow import *
# explicit labels
G=nx.Graph()
A=['w','a1','a2','a3','a4']; B=['w','b1','b2','b3','b4']
for S in (A,B):
    for i in range(5):
        for j in range(i+1,5): G.add_edge(S[i],S[j])
G.remove_edge('w','a1'); G.remove_edge('w','b1'); G.add_edge('a1','b1')
print(G.number_of_nodes(),G.number_of_edges(),chi(G),certified5(G))
ds=owned_decomps(G,limit=400)
print(len(ds))
seen=set()
for V1,P1,P2 in ds:
    k=(tuple(sorted(V1)),len(P1))
    if k in seen: continue
    seen.add(k); print(sorted(V1),len(P1),sorted(map(sorted,P1)))
