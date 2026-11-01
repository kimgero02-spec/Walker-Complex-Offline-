import networkx as nx
from tri import dual,faces_of
H=dual(nx.tutte_graph())
F=set(frozenset(f) for f in faces_of(H))
sep=[t for t in nx.enumerate_all_cliques(H) if len(t)==3 and frozenset(t) not in F]
print('separating triangles',sep)
for t in sep:
    R=H.copy(); R.remove_nodes_from(t)
    print(t,[sorted(c) for c in nx.connected_components(R)])
for v in [0,1,2,8]: print(v,sorted(H[v]))
