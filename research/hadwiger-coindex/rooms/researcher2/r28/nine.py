import pickle, itertools, networkx as nx
cands = pickle.load(open('/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r21/cands7.pkl','rb'))
def base8(ci, mask):
    G = nx.Graph(cands[ci]); G.add_node(7)
    for i in range(7):
        if mask>>i&1: G.add_edge(i,7)
    return G
tests=[("C7bar+pendant0",4,1),("C7bar+N{0,3,5}",4,None),("cand0+pendant",0,1)]
for name,ci,mask in tests:
    if mask is None: G=base8(ci,0); [G.add_edge(x,7) for x in (0,3,5)]
    else: G=base8(ci,mask)
    for v in [8]:
        for N in [[0],[0,1,2],[0,3,5,6],[1,2,3,4,5,6,7]]:
            H=G.copy(); H.add_node(8); [H.add_edge(x,8) for x in N]
            nodes=list(range(9))
            planar5=[S for S in itertools.combinations(nodes,5) if nx.check_planarity(H.subgraph(S))[0]]
            print(f"{name} + v8 N={N}: planar 5-sets={len(planar5)}/126, 5+4 split exists={len(planar5)>0}")
# K9 check
K9=nx.complete_graph(9)
print("K9 planar 5-sets:", sum(1 for S in itertools.combinations(range(9),5) if nx.check_planarity(K9.subgraph(S))[0]))
