import networkx as nx
from r21_shadow import certified5, chi
def myc(H):
    G=nx.Graph(); n=list(H.nodes())
    for u,v in H.edges():
        G.add_edge(('v',u),('v',v)); G.add_edge(('u',u),('v',v)); G.add_edge(('v',u),('u',v))
    for u in n: G.add_edge('z',('u',u))
    return G
W5=nx.wheel_graph(6)
print('M(W5) certified', certified5(myc(W5)))
K2C5=nx.complement(nx.disjoint_union(nx.complement(nx.complete_graph(2)), nx.complement(nx.cycle_graph(5))))
print('K2+C5 chi',chi(K2C5),'certified',certified5(K2C5))
# check P1/P2 of chosen decomposition
G=nx.Graph()
A=['w','a1','a2','a3','a4']; B=['w','b1','b2','b3','b4']
for S in (A,B):
    for i in range(5):
        for j in range(i+1,5): G.add_edge(S[i],S[j])
G.remove_edge('w','a1'); G.remove_edge('w','b1'); G.add_edge('a1','b1')
P1=nx.Graph([('a1','a2'),('a1','a3'),('a1','a4'),('a1','b1'),('a2','w'),('a3','w'),('a4','w'),('b1','b2'),('b3','w'),('b4','w')])
P2=nx.Graph([e for e in G.edges() if not P1.has_edge(*e)])
print(len(P1.edges()),len(P2.edges()),nx.is_bipartite(P1),nx.check_planarity(P1)[0],nx.check_planarity(P2)[0],chi(P2),sorted(map(sorted,P2.edges())))
