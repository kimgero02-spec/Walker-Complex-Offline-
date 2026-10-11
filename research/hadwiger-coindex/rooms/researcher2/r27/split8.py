import pickle, networkx as nx
cands = pickle.load(open('/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r21/cands7.pkl','rb'))
C7bar = nx.Graph(cands[4])   # complement of C7, nonplanar
print("C7bar planar:", nx.check_planarity(C7bar)[0])
reps = {"N={0}":[0], "N={0,1}":[0,1], "N={0,3,5}":[0,3,5]}
for name, N in reps.items():
    H = C7bar.copy(); H.add_node(7)
    for u in N: H.add_edge(u, 7)
    nodes = list(range(8))
    best=None; sols=[]
    for mask in range(1, 255):
        S1=[v for v in nodes if mask>>v&1]; S2=[v for v in nodes if not mask>>v&1]
        if not S2: continue
        p1=nx.check_planarity(H.subgraph(S1))[0]; p2=nx.check_planarity(H.subgraph(S2))[0]
        if p1 and p2: sols.append((S1,S2))
    sols=[s for s in sols if s[0] and s[1]]
    sols.sort(key=lambda s: abs(len(s[0])-len(s[1])))
    print(name, "2-sheet planar splits (nonempty sides, unordered-by-mask):", len(sols), "most balanced:", sols[0] if sols else None)
    if not sols:
        ok,w=nx.check_planarity(H,counterexample=True); print("  Kuratowski witness nodes:", sorted(w.nodes()))
