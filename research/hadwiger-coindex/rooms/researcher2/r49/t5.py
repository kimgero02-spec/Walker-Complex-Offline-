import networkx as nx, itertools
from tri import dual
G=dual(nx.tutte_graph())
c={0: 0, 1: 1, 2: 2, 8: 3, 11: 1, 9: 1, 7: 1, 6: 2, 16: 2, 14: 2, 13: 0, 12: 2, 21: 0, 19: 0, 18: 0, 17: 1, 22: 3, 23: 3, 24: 3, 4: 3, 10: 2, 3: 3, 5: 3, 15: 0, 20: 1}
assert all(c[u]!=c[v] for u,v in G.edges()) and G.number_of_edges()==3*25-6
print('deg',{v:G.degree(v) for v in G})
for p in itertools.combinations(range(4),2):
    H=G.subgraph([v for v in G if c[v] in p])
    print(p,'comps',nx.number_connected_components(H),'cycle',[e[0] for e in nx.find_cycle(H)])
# separating triangles
tris=[t for t in nx.enumerate_all_cliques(G) if len(t)==3]
print('triangles',len(tris),'faces',2*25-4)
