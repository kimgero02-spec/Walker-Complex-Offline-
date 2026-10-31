# hand construction: K4 (colors 1..4) + octahedral gadget in faces 123,134,124 ; coloring x'=c(x) etc.
import networkx as nx, itertools
from tri import fb,is_fb
G=nx.complete_graph([1,2,3,4]); c={v:v for v in G}
def gadget(G,c,f,tag):
    x,y,z=f; X,Y,Z=(tag,x),(tag,y),(tag,z)
    G.add_edges_from([(X,Y),(Y,Z),(Z,X),(X,y),(X,z),(Y,x),(Y,z),(Z,x),(Z,y)])
    c[X],c[Y],c[Z]=c[x],c[y],c[z]
for t,f in enumerate([(1,2,3),(1,3,4),(1,2,4)]): gadget(G,c,f,t)
print(G.number_of_nodes(),G.number_of_edges(),3*13-6,nx.check_planarity(G)[0])
assert all(c[u]!=c[v] for u,v in G.edges())
for p in itertools.combinations(range(1,5),2):
    H=G.subgraph([v for v in G if c[v] in p]); print(p,nx.number_connected_components(H),[e[0] for e in nx.find_cycle(H)])
S=fb(G); print('FB',S, is_fb(G,S))
