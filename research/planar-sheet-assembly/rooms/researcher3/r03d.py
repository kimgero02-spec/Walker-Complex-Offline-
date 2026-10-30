"""Hunt for a decisive counterexample to prediction (a) in the only regime the proof sketch
does not cover: pieces with L=3 (ind B = 1) but chi >= 4 (Moser spindle, Hajos sums)."""
import itertools, sys, networkx as nx
from topo import h_index, simplices_B, simplices_B0, chi
from r03c import glue, hajos

def L(G, dmax=4):
    G = nx.convert_node_labels_to_integers(G)
    return h_index(simplices_B(G, dmax), dmax) + 2

K4 = nx.complete_graph(4)
M = nx.convert_node_labels_to_integers(hajos(K4, 0, 1, K4, 0, 1))
print("Moser L", L(M), "chi", chi(M))
E = list(M.edges())
found = []
for e in E:
    for f in E:
        for flip in (False, True):
            f2 = (f[1], f[0]) if flip else f
            G = glue(M, M, [(e[0], f2[0]), (e[1], f2[1])])
            l = L(G)
            if l != 3:
                found.append((e, f2, l, chi(G)))
                print("edge-2-sum", e, f2, "L=", l, "chi=", chi(G)); sys.stdout.flush()
print("done; deviations:", len(found))
