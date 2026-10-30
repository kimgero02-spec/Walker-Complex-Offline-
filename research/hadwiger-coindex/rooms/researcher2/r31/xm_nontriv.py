import pickle, itertools, networkx as nx
def xm_nontrivial(G):
    nodes=list(G.nodes()); n=len(nodes); idx={v:i for i,v in enumerate(nodes)}
    for mask in range(1,(1<<n)-1):
        side=[nodes[i] for i in range(n) if mask>>i&1]; s=set(side)
        if any(sum(1 for u in G[v] if (u in s)!=(v in s))>1 for v in nodes): continue
        other=[v for v in nodes if v not in s]
        if nx.check_planarity(G.subgraph(side))[0] and nx.check_planarity(G.subgraph(other))[0]:
            return (side, other)
    return None
# C5[K2]: blobs {2i,2i+1} are K2, consecutive blobs fully joined
C = nx.Graph()
for i in range(5):
    C.add_edge(2*i,2*i+1); j=(i+1)%5
    for s in range(2):
        for t in range(2): C.add_edge(2*i+s,2*j+t)
print("C5[K2]: n",C.number_of_nodes(),"m",C.number_of_edges(),"nontrivial X_M witness:", xm_nontrivial(C))
cands = pickle.load(open('/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r21/cands7.pkl','rb'))
G8 = nx.Graph(cands[4]); G8.add_node(7); G8.add_edge(0,7)
print("cand4 + pendant (8 vertices): nontrivial X_M witness:", xm_nontrivial(G8))
