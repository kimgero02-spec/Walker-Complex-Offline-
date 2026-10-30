import networkx as nx
exec(open('r19_myc.py').read().split('G=myc')[0])
G=myc(W5())
def test(P1e):
    P1=nx.Graph(P1e); assert all(G.has_edge(*e) for e in P1.edges())
    P2=nx.Graph([e for e in G.edges() if not P1.has_edge(*e)])
    V1={'v1','v2','z'}; V2=set(G)-V1
    own=all(P1.has_edge(*e) for e in G.subgraph(V1).edges()) and all(P2.has_edge(*e) for e in G.subgraph(V2).edges())
    print(P1.number_of_edges(),nx.is_bipartite(P1),nx.check_planarity(P1)[0],'|',P2.number_of_edges(),nx.check_planarity(P2)[0],chi(P2),'owned',own)
    return P1,P2
base=[('v1','v2')]+[('z','u%d'%i) for i in range(6)]
P1,P2=test(base+[('v1',x) for x in ['u0','u2','u5','v0','v5']]+[('v2','v3')])
# variants: v0 on A side -> v2v0 in P1, v1v0 not
P1,P2=test(base+[('v1',x) for x in ['u0','u2','u5','v5']]+[('v2','v3'),('v2','v0')])
P1,P2=test(base+[('v1',x) for x in ['u0','u2','u5','v0']]+[('v2','v3')])
P1,P2=test(base+[('v1',x) for x in ['u0','u2','u5']]+[('v2','v3'),('v2','v0')])
