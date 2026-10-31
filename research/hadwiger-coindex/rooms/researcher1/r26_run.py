# R26: minimal number m of cross edges giving a K7 minor, for block pair (W5, K3) on 9 vertices
import itertools, sys, networkx as nx
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
print("cross candidates", len(cross), flush=True)
for m in range(8, 19):
    found = None
    cnt = 0
    for S in itertools.combinations(cross, m):
        G = base.copy()
        G.add_edges_from(S)
        cnt += 1
        if k7_minor(G):
            found = S
            break
    print("m=", m, "patterns tried", cnt, "found", found, flush=True)
    if found:
        break
