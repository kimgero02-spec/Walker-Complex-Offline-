import pickle
import networkx as nx
cands = pickle.load(open('/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r21/cands7.pkl','rb'))
for ci, E in enumerate(cands):
    G = nx.Graph(E)
    ok, witness = nx.check_planarity(G, counterexample=True)
    print("cand", ci, "planar:", ok, "edges", G.number_of_edges(), "degseq", sorted(d for _, d in G.degree()))
    if not ok:
        print("  Kuratowski witness edges:", sorted(witness.edges()), "nodes", witness.number_of_nodes(), "edges", witness.number_of_edges())
G = nx.Graph(cands[4])
print("complement-of-C7 check: is complement a 7-cycle?", nx.is_isomorphic(nx.complement(G), nx.cycle_graph(7)))
# balanced planar 2-sheet split for complement C7
nodes = sorted(G.nodes())
for S1 in [[nodes[0]], nodes[:3], nodes[:4]]:
    S2 = [v for v in nodes if v not in S1]
    print("split", S1, S2, "planar sides:", nx.check_planarity(G.subgraph(S1))[0], nx.check_planarity(G.subgraph(S2))[0])
