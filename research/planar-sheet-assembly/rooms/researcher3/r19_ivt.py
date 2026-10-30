# R19: small checks only (not evidence). K5 bit decomposition into [3]x[2], planarity, chi; Zykov sum chi.
import itertools, networkx as nx
def chi(G):
    n=G.number_of_nodes(); nodes=list(G)
    if G.number_of_edges()==0: return 1 if n else 0
    for q in range(1,n+1):
        for c in itertools.product(range(q),repeat=n):
            d=dict(zip(nodes,c))
            if all(d[u]!=d[v] for u,v in G.edges()): return q
def join(Gs):
    J=nx.Graph(); 
    for k,P in enumerate(Gs):
        J.add_nodes_from((v,k) for v in P); J.add_edges_from(((u,k),(v,k)) for u,v in P.edges())
    for (k,P),(l,Q) in itertools.combinations(enumerate(Gs),2):
        J.add_edges_from(((u,k),(v,l)) for u in P for v in Q)
    return J
lab={'a':(0,0),'b':(0,1),'c':(1,0),'d':(1,1),'x':(2,0)}
K5=nx.complete_graph('abcdx')
P1=nx.Graph([(u,v) for u,v in K5.edges() if lab[u][0]!=lab[v][0]]); P2=nx.Graph([(u,v) for u,v in K5.edges() if lab[u][1]!=lab[v][1]])
for name,P in [('P1',P1),('P2',P2)]:
    print(name,sorted(P.edges()),'planar',nx.check_planarity(P)[0],'chi',chi(P))
print('cover',set(map(frozenset,P1.edges()))|set(map(frozenset,P2.edges()))==set(map(frozenset,K5.edges())))
Q1=K5.copy(); Q1.remove_edge('c','d')
print('K5-cd planar',nx.check_planarity(Q1)[0],'chi',chi(Q1))
print('chi J(P1,P2)=',chi(join([P1,P2])),' chi K5=',chi(K5))
