# R17: K7 = (K2 + P5) + (K5 - P5) 이 평면분해이고 |V(M°)|=17 인지 확인 (예 확인용)
import networkx as nx, itertools
from r17_hadwiger import manual
s=[0,1]; w=[2,3,4,5,6]; path=[(2,3),(3,4),(4,5),(5,6)]
P=nx.Graph(); P.add_edge(0,1); P.add_edges_from((a,b) for a in s for b in w); P.add_edges_from(path)
Q=nx.complete_graph(w); Q.remove_edges_from(path)
print('P planar',nx.check_planarity(P)[0],'Q planar',nx.check_planarity(Q)[0])
U=set(map(frozenset,P.edges()))|set(map(frozenset,Q.edges())); print('covers K7',len(U)==21)
Mc,M,mu=manual([(list(P.nodes()),list(P.edges())),(list(Q.nodes()),list(Q.edges()))])
print('|V(Mc)|',Mc.number_of_nodes(),'excess',sum(mu.values())-21)
