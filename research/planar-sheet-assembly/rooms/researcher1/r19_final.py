# R19 final example: M(W5) = P1 u P2, verify all claims (support only; hand proofs in report)
import networkx as nx
exec(open('r19_myc.py').read().split('G=myc')[0])
G=myc(W5())
P1=nx.Graph([('v1','v2'),('v1','v0'),('v1','v5'),('v1','u2'),('v1','u5'),('v2','v3'),('v2','u0'),('v2','u1'),('v2','u3'),('z','u0'),('z','u1'),('z','u3'),('z','u4')])
assert all(G.has_edge(*e) for e in P1.edges())
P2=nx.Graph([e for e in G.edges() if not P1.has_edge(*e)])
print('P1',P1.number_of_edges(),nx.is_bipartite(P1),nx.check_planarity(P1)[0])
print('P2',P2.number_of_edges(),chi(P2),nx.check_planarity(P2)[0])
print('chi G',chi(G),'omega',max(map(len,nx.find_cliques(G))),'co-connected',nx.is_connected(nx.complement(G)))
ok,emb=nx.check_planarity(P2)
seen=set();faces=[]
for u,v in emb.edges():
    if (u,v) in seen: continue
    f=emb.traverse_face(u,v,mark_half_edges=seen); faces.append(f)
for f in faces: print(f)
print(len(faces))
