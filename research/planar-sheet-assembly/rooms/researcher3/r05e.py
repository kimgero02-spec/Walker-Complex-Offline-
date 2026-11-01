"""Lemma L check on a few arc-model chains with c=3, max lifetime l, m > 4(l-1): every 4-cycle has a chord."""
import random, networkx as nx
from r04 import chain
from r05 import four_cycles, e_crit, tri_orient
random.seed(1); seen = 0
while seen < 8:
    m = random.choice((13,14,15,16)); ell = [random.choice((2,3,4)) for _ in range(m)]
    try: G, T, c = chain(m, ell)
    except AssertionError: continue
    if c != 3 or max(ell) != 4: continue
    seen += 1
    ind = [q for q in four_cycles(G) if not (G.has_edge(q[0],q[2]) or G.has_edge(q[1],q[3]))]
    print(m, ell, "induced C4:", ind, "t exists:", tri_orient(G) is not None, "E:", e_crit(G))
