import pickle, itertools, networkx as nx
cands = pickle.load(open('/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r21/cands7.pkl','rb'))
def in_XM(G):
    nodes=list(G.nodes()); n=len(nodes)
    for mask in range(1<<n):
        S1=[nodes[i] for i in range(n) if mask>>i&1]; S2=[v for v in nodes if v not in S1]
        side=set(S1)
        # cross matching: each vertex has at most one neighbour across the cut
        ok=True
        for v in nodes:
            c=sum(1 for u in G[v] if (u in side)!=(v in side))
            if c>1: ok=False; break
        if not ok: continue
        if nx.check_planarity(G.subgraph(S1))[0] and nx.check_planarity(G.subgraph(S2))[0]:
            return (S1,S2)
    return None
for i,E in enumerate(cands):
    G=nx.Graph(E)
    r=in_XM(G)
    print("7-vertex gap cand",i,"edges",G.number_of_edges(),"X_M witness:",r)
