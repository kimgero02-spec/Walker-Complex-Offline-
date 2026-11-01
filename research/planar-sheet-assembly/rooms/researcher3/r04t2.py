"""Counterexample hunt at small m (c=3): sign + but ind B >= 2 (exact via zlift), or sign - with L_h >= 5.
Also records the largest biclique span (locality)."""
import itertools, sys, networkx as nx
from r04 import chain, holonomy, sign, L_h
from zlift import ind_le_1
from topo import chi
c = 3
for m in range(4, 9):
    seen = []; found = 0; total = 0
    for perm in itertools.permutations(range(m)):
        ell = [(perm[j] - j) % m for j in range(m)]
        if 0 in ell or sum(ell) != c * m: continue
        try: G, T, cc = chain(m, ell)
        except AssertionError: continue
        if any(nx.is_isomorphic(G, H) for H in seen): continue
        seen.append(G); total += 1
        g = holonomy(m, ell, T, cc); s = sign(g)
        ok1 = ind_le_1(G); x = chi(G)
        clique = max(len(q) for q in nx.find_cliques(G))
        bad = (s > 0 and not ok1)
        lh = L_h(G, 5) if (s < 0 or bad) else 3
        if bad or (s < 0 and lh > 4) or True:
            print(f"m={m} ell={ell} hol={g} sgn={'+' if s>0 else '-'} chi={x} omega={clique} ind<=1:{ok1} L_h={lh} {'<-- VIOLATION' if (bad or (s<0 and lh>4)) else ''}")
    print(f"m={m}: {total} non-isomorphic chains"); sys.stdout.flush()
