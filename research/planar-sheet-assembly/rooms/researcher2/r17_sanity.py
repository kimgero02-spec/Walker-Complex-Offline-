import networkx as nx
from r17_hM import has_minor, Mcirc
H=nx.heawood_graph(); print('K5 in Heawood', bool(has_minor(H,nx.complete_graph(5))))
P=nx.petersen_graph(); S=nx.Graph()
for u,v in P.edges(): S.add_edge(u,('s',u,v)); S.add_edge(('s',u,v),v)
Y=Mcirc(5,[[(i,(i+1)%5) for i in range(5)],[(i,(i+2)%5) for i in range(5)]])
print('M°(C5,C5*) in sub1 Petersen', bool(has_minor(S,Y,maxset=6)))
print('K6 in Heawood', bool(has_minor(H,nx.complete_graph(6))))
print('|Aut(Heawood)|', sum(1 for _ in nx.algorithms.isomorphism.GraphMatcher(H,H).isomorphisms_iter()))
