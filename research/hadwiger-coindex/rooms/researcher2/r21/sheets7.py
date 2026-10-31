import pickle, itertools
import networkx as nx
cands = pickle.load(open('/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r21/cands7.pkl','rb'))
def planar(G, S):
    H = G.subgraph(S)
    return nx.check_planarity(H)[0]
for ci, E in enumerate(cands):
    G = nx.Graph(E)
    nodes = sorted(G.nodes())
    good = []
    for mask in range(1 << 7):
        S1 = [nodes[i] for i in range(7) if mask >> i & 1]
        S2 = [v for v in nodes if v not in S1]
        if planar(G, S1) and planar(G, S2):
            good.append((S1, S2))
    print(f"cand {ci}: edges={G.number_of_edges()} 2-sheet partitions (ordered, both planar)={len(good)}")
    if good:
        S1, S2 = good[0]
        print("   example", S1, S2)
    else:
        # minimal obstruction: check K5 / K33 in sides for best cuts
        best = None
        for mask in range(1 << 7):
            S1 = [nodes[i] for i in range(7) if mask >> i & 1]
            S2 = [v for v in nodes if v not in S1]
            bad1 = not planar(G, S1); bad2 = not planar(G, S2)
            if best is None or (bad1 + bad2) < best[0]:
                best = (bad1 + bad2, S1, S2)
        print("   no planar 2-split. best cut has", best[0], "nonplanar side(s):", best[1], best[2])
