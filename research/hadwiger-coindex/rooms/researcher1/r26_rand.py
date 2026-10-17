# R26: random sampling of cross patterns for K7 minor (upper bound on m*), W5 + K3
import random, networkx as nx
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
rnd = random.Random(1)
for m in range(8, 13):
    hits = 0
    tries = 0
    example = None
    for _ in range(300):
        S = rnd.sample(cross, m)
        G = base.copy()
        G.add_edges_from(S)
        tries += 1
        if k7_minor(G):
            hits += 1
            example = S
            break
    print("m=", m, "tries", tries, "hits", hits, "example", example, flush=True)
