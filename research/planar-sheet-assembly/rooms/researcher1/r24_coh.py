import networkx as nx, itertools
P1=[('s','a'),('a','c'),('a','e'),('b','c'),('b','d'),('b','e')]
P2=[('s','b'),('c','d'),('c','e'),('d','e'),('a','d')]
G=nx.Graph(P1+P2); A=nx.Graph(P1); B=nx.Graph(P2)
print(len(G.edges()), nx.check_planarity(A)[0], nx.check_planarity(B)[0])
V=list(G); models=[]
for lab in itertools.product(range(6),repeat=len(V)):  # 0..4 branch, 5 none
    bs=[[V[i] for i in range(len(V)) if lab[i]==j] for j in range(5)]
    if any(not b for b in bs): continue
    if lab!=tuple(sorted(lab)) and False: pass
    if not all(nx.is_connected(G.subgraph(b)) for b in bs): continue
    if all(any(G.has_edge(x,y) for x in bs[i] for y in bs[j]) for i,j in itertools.combinations(range(5),2)):
        models.append(frozenset(frozenset(b) for b in bs))
models=set(models); print('models',len(models))
def coh(m,P):
    for b in m:
        bb=[x for x in b if x in P]
        if bb and not nx.is_connected(P.subgraph(bb)): return False
    return True
for m in models: print(sorted(map(sorted,m)), coh(m,A), coh(m,B))
