# R19: structured split of M(W5); verify by computation (hand proof in report)
import networkx as nx, itertools
exec(open('r19_myc.py').read().split('G=myc')[0])
G=myc(W5())
rim=range(1,6); nb=lambda i:[(i-2)%5+1, i%5+1]
P1=[('v0','v%d'%j) for j in rim]+[('v0','u%d'%j) for j in range(2,6)]+[('u0','v%d'%j) for j in rim]+[('z','u%d'%j) for j in range(2,6)]+[('u1','v2'),('u1','v5')]
P1=nx.Graph(P1)
P2=nx.Graph([e for e in G.edges() if not P1.has_edge(*e)])
assert all(G.has_edge(*e) for e in P1.edges())
print('P1',P1.number_of_edges(),nx.is_bipartite(P1),nx.check_planarity(P1)[0])
print('P2',P2.number_of_edges(),sorted(map(sorted,P2.edges())),chi(P2),nx.check_planarity(P2)[0])
print('chiG',chi(G))
V=list(G); owned=[]
for m in range(1<<len(V)):
    V1=[V[i] for i in range(len(V)) if m>>i&1]; V2=[v for v in V if v not in V1]
    if all(P1.has_edge(*e) for e in G.subgraph(V1).edges()) and all(P2.has_edge(*e) for e in G.subgraph(V2).edges()):
        owned.append((sorted(V1),chi(G.subgraph(V1)) if V1 else 0,chi(G.subgraph(V2))))
print(len(owned)); [print(o) for o in owned[:10]]
# complement connected?
print('complement connected',nx.is_connected(nx.complement(G)))
