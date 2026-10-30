# R12: r_W = beta1(G)-beta1(G-W) equals r(D); N <= b + r on named realizations (strata r=0,1 cores and a few others)
import networkx as nx, itertools
def manual0(pieces, E11=False):
    M=nx.Graph(); F={}
    for k,P in enumerate(pieces):
        for v in P.nodes(): M.add_node(('c',v,k)); F.setdefault(v,[]).append(('c',v,k))
        for a,b in P.edges(): M.add_edge(('c',a,k),('c',b,k))
    W=[v for v in F if len(F[v])>=2]
    for v in W:
        for x in F[v]: M.add_edge(('w',v),x)
    if E11:
        for a,b in itertools.combinations(W,2):
            if sum(1 for P in pieces if P.has_edge(a,b))>=2: M.add_edge(('w',a),('w',b))
    return M,[('w',v) for v in W]
def b1(X): return X.number_of_edges()-X.number_of_nodes()+nx.number_connected_components(X)
def chi(H):
    n=H.number_of_nodes(); nodes=list(H)
    for q in range(1,n+1):
        for c in itertools.product(range(q),repeat=n):
            d=dict(zip(nodes,c))
            if all(d[a]!=d[b] for a,b in H.edges()): return q
def rD(pieces):
    I=nx.Graph(); cnt={}
    blocks=[P.subgraph(C) for P in pieces for C in nx.connected_components(P)]
    for B in blocks:
        for v in B: cnt[v]=cnt.get(v,0)+1
    for i,B in enumerate(blocks):
        I.add_node(('b',i))
        for v in B:
            if cnt[v]>=2: I.add_edge(('b',i),('h',v))
    return b1(I)
E=lambda *es: nx.Graph(list(es))
def Kme(N): K=nx.complete_graph(N); K.remove_edge(0,1); return K
K1=lambda v: (lambda g:(g.add_node(v),g)[1])(nx.Graph())
cases={
 'r0: broomed K4 (K1 at 0 twice)':[nx.complete_graph(4),K1(0),K1(0)],
 'r1A: K3 + dup edge':[nx.complete_graph(3),E((0,1))],
 'r1A: K4 + dup edge':[nx.complete_graph(4),E((0,1))],
 'r1B1: K3 = P3+K2 (C7)':[Kme(3),E((0,1))],
 'r1B1: K5 = (K5-e)+K2':[Kme(5),E((0,1))],
 'r1B2: K2=(K2,K2) (C6)':[E((0,1)),E((0,1))],
 'r1B3: K3 = three K2 (C9)':[E((0,1)),E((1,2)),E((0,2))],
 'K5 ex1.5 two 5-cycles':[nx.cycle_graph(5),E((0,2),(2,4),(4,1),(1,3),(3,0))],
 'K5 edge-decomp (K5^(3))':[E(e) for e in nx.complete_graph(5).edges()],
}
for name,p in cases.items():
    G,W=manual0(p); H=G.copy(); H.remove_nodes_from(W)
    N=len(set().union(*[set(P.nodes()) for P in p]))
    rW=b1(G)-b1(H); b=max(chi(H.subgraph(C)) for C in nx.connected_components(H))
    print(f'{name:32s} |V(G)|={G.number_of_nodes():3d} N={N} r(D)={rD(p)} r_W={rW} b={b} N<=b+r:{N<=b+rW}')
