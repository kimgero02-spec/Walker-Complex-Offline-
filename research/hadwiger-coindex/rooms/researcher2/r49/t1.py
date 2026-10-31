import networkx as nx
from tri import *
# decisive candidate 1: dual of Tutte graph (3-conn cubic planar, non-Hamiltonian => no tree+tree)
G=dual(nx.tutte_graph())
print(G.number_of_nodes(),G.number_of_edges(),sorted(d for _,d in G.degree()))
S=fb(G); print('FB',S is not None, S and is_fb(G,S))
# parity criterion check on this witness
T=[v for v in G if v not in S]
print('T connected',nx.is_connected(G.subgraph(T)))
for C in nx.connected_components(G.subgraph(S)):
    print(len(C),sum(G.degree(v) for v in C)%2,end='; ')
print()
