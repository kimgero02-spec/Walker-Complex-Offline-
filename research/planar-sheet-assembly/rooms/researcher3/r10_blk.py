# R10: block-level invariants b(D), r(D)=beta1(I(D)), chi(G) on a few named examples
import networkx as nx, itertools
def chi(H):
    n=H.number_of_nodes()
    if n==0: return 0
    nodes=list(H)
    for q in range(1,n+1):
        for c in itertools.product(range(q),repeat=n):
            d=dict(zip(nodes,c))
            if all(d[a]!=d[b] for a,b in H.edges()): return q
def blocks(pieces):
    B=[]
    for k,P in enumerate(pieces):
        for C in nx.connected_components(P): B.append(P.subgraph(C).copy())
    return B
def r_of(pieces):
    B=blocks(pieces); I=nx.Graph()
    cnt={}
    for i,b in enumerate(B):
        I.add_node(('b',i))
        for v in b: cnt[v]=cnt.get(v,0)+1
    for i,b in enumerate(B):
        for v in b:
            if cnt[v]>=2: I.add_edge(('b',i),('h',v))
    return I.number_of_edges()-I.number_of_nodes()+nx.number_connected_components(I), max(chi(b) for b in B)
def G_of(p):
    G=nx.Graph()
    for P in p: G.add_nodes_from(P); G.add_edges_from(P.edges())
    return G
E=lambda *es: nx.Graph(list(es))
K4=nx.complete_graph(4)
ex={
 'K4 D=(P1,P2) ex1.3':[E((0,1),(1,3),(3,2),(2,0)),E((0,3),(3,1),(1,2),(2,0))],
 "K4 D'''=(P1,03,12)":[E((0,1),(1,3),(3,2),(2,0)),E((0,3)),E((1,2))],
 "K4 D'=6 edges":[E(e) for e in K4.edges()],
 'K5=(K5-e,K2)':[nx.complete_graph(5).copy(),None],
 'K4=(K4-uv,K2)':[None,None],
}
K5e=nx.complete_graph(5); K5e.remove_edge(0,1); ex['K5=(K5-e,K2)']=[K5e,E((0,1))]
K4e=nx.complete_graph(4); K4e.remove_edge(0,1); ex['K4=(K4-uv,K2)']=[K4e,E((0,1))]
ex['ex2.6 ab|cd one piece']=[E(('a','b'),('c','d'))]
for k,p in ex.items():
    r,b=r_of(p); G=G_of(p); c=chi(G)
    print(f'{k:24s} b={b} r={r} chi={c} gap={c-b} b+r={b+r} planar={nx.check_planarity(G)[0]}')
