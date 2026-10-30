"""Triangle clique-sums in the uncovered regime, and the K4-necklace C_m^3 (holonomy test)."""
import itertools, sys, networkx as nx
from topo import h_index, simplices_B, chi
from r03c import glue, hajos

def L(G, dmax=5):
    G = nx.convert_node_labels_to_integers(G)
    return h_index(simplices_B(G, dmax), dmax) + 2

K4 = nx.complete_graph(4)
print("K4 +_K3 K4 = K5-e :", "L", L(glue(K4, K4, [(0, 0), (1, 1), (2, 2)])), "chi", chi(glue(K4, K4, [(0, 0), (1, 1), (2, 2)])))
M = nx.convert_node_labels_to_integers(hajos(K4, 0, 1, K4, 0, 1))
tris = [t for t in itertools.combinations(M.nodes(), 3) if all(M.has_edge(a, b) for a, b in itertools.combinations(t, 2))]
print("Moser triangles", tris)
dev = 0
for s in tris:
    for t in tris:
        for p in itertools.permutations(t):
            G = glue(M, M, list(zip(s, p)))
            l = L(G, 4)
            if l != 3:
                dev += 1; print("Moser +_K3 Moser", s, p, "L", l, "chi", chi(G))
print("Moser+_K3 deviations", dev)
print("== K4 necklace C_m^3 : pieces K4 on 4 consecutive, H=C_m, interfaces triangles ==")
for m in range(8, 12):
    G = nx.Graph()
    for i in range(m):
        for d in (1, 2, 3): G.add_edge(i, (i + d) % m)
    print(f"C_{m}^3 holonomy {'trivial' if m % 4 == 0 else 'nontrivial'}: chi", chi(G), "L", L(G, 5)); sys.stdout.flush()
