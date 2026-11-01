"""search for a decisive planar counterexample to: (planar, no odd K3-chain) => ind Hom(K2,G) <= 1."""
import networkx as nx, random, sys
from r05 import e_crit
from oddchain import odd_chain
random.seed(5)
def rand_planar(n):
    pts = {i:(random.random(), random.random()) for i in range(n)}
    import itertools
    # Delaunay-ish: greedy planar edge insertion by length
    G = nx.Graph(); G.add_nodes_from(range(n))
    pairs = sorted(itertools.combinations(range(n),2), key=lambda p:(pts[p[0]][0]-pts[p[1]][0])**2+(pts[p[0]][1]-pts[p[1]][1])**2)
    for u,v in pairs:
        G.add_edge(u,v)
        if not nx.check_planarity(G)[0]: G.remove_edge(u,v)
    return G
found = 0
for trial in range(3000):
    n = random.randint(7, 12)
    G = rand_planar(n)
    E = list(G.edges()); random.shuffle(E)
    for e in E[:random.randint(0, len(E)//2)]: G.remove_edge(*e)
    if odd_chain(G,3): continue
    if not e_crit(G):
        print("COUNTEREXAMPLE", sorted(G.edges())); found += 1
        if found >= 3: break
print("done", trial)
