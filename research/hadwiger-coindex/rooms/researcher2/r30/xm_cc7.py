import pickle, networkx as nx
cands = pickle.load(open('/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r21/cands7.pkl','rb'))
G=nx.Graph(cands[4]); nodes=sorted(G.nodes())
matching_valid=[]
for mask in range(1<<7):
    S1=[nodes[i] for i in range(7) if mask>>i&1]; S2=[v for v in nodes if v not in S1]
    side=set(S1)
    if all(sum(1 for u in G[v] if (u in side)!=(v in side))<=1 for v in nodes):
        matching_valid.append((S1,S2))
print("matching-valid cuts (ordered):", len(matching_valid))
fails={}
for S1,S2 in matching_valid:
    p1=nx.check_planarity(G.subgraph(S1))[0]; p2=nx.check_planarity(G.subgraph(S2))[0]
    key=(len(S1), p1, p2)
    fails[key]=fails.get(key,0)+1
print("(|S1|, planar S1, planar S2) -> count:", fails)
ok,w=nx.check_planarity(G,counterexample=True)
print("Kuratowski witness of whole graph (nodes):", sorted(w.nodes()), "edges:", sorted(w.edges()))
