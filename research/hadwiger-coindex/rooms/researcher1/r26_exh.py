# R26: exhaustive check of cross patterns with m = 8..11 edges for K7 minor (W5 + K3)
import itertools, networkx as nx, sys
from r26_fast import k7_minor

def W5():
    G = nx.Graph()
    for i in range(5):
        G.add_edge(i, (i + 1) % 5)
        G.add_edge(i, 5)
    return G

B1 = W5()
B2 = nx.Graph()
B2.add_edges_from([(6, 7), (7, 8), (6, 8)])
base = nx.union(B1, B2)
cross = [(a, b) for a in range(6) for b in (6, 7, 8)]
for m in range(8, 12):
    total = 0
    hits = []
    for S in itertools.combinations(cross, m):
        G = base.copy()
        G.add_edges_from(S)
        total += 1
        if k7_minor(G):
            hits.append(S)
            break
    print("m=", m, "patterns", total, "K7-minor found:", len(hits) > 0, hits[:1], flush=True)
print("DONE", flush=True)
