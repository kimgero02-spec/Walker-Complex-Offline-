# R19: find owned splits of M(W5) with few P1/P2 pattern; prefer small cross structure
import networkx as nx, itertools, random
exec(open('r19_myc.py').read().split('G=myc')[0])
G=myc(W5()); V=sorted(G)
def try_split(V1):
    V2=[v for v in V if v not in V1]
    A=G.subgraph(V1); B=G.subgraph(V2)
    if A.number_of_edges()==0 or not nx.is_bipartite(A): return None
    if not nx.check_planarity(B)[0] or not chi_le(B,3) or chi_le(B,2): return None
    cross=[e for e in G.edges() if (e[0] in V1)!=(e[1] in V1)]
    for t in range(300):
        P1=nx.Graph(A.edges()); P2=nx.Graph(B.edges()); random.shuffle(cross); ok=True
        for e in cross:
            P1.add_edge(*e)
            if nx.is_bipartite(P1) and nx.check_planarity(P1)[0]: continue
            P1.remove_edge(*e); P2.add_edge(*e)
            if nx.check_planarity(P2)[0] and chi_le(P2,3): continue
            ok=False;break
        if ok: return P1,P2
    return None
random.seed(0); res=[]
for r in range(2,8):
    for V1 in itertools.combinations(V,r):
        s=try_split(set(V1))
        if s: res.append((V1,s)); print(V1, s[0].number_of_edges(), s[1].number_of_edges()); 
        if len(res)>=6: break
    if len(res)>=6: break
V1,(P1,P2)=res[0]
print('P1',sorted(map(sorted,P1.edges())));print('P2',sorted(map(sorted,P2.edges())))
