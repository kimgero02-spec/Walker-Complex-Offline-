"""Refined prediction P3 (c=3): for the circular-arc triangle chains with m<=8,
   ind B(G) >= 2  <=>  G contains SOME closed triangle chain with odd holonomy."""
import itertools, sys, networkx as nx
from r04 import chain, holonomy, sign
from zlift import ind_le_1
from oddchain import odd_chain
c = 3
for m in range(4, 10):
    seen = []; agree = 0; dis = []
    for perm in itertools.permutations(range(m)):
        ell = [(perm[j] - j) % m for j in range(m)]
        if 0 in ell or sum(ell) != c * m: continue
        try: G, T, cc = chain(m, ell)
        except AssertionError: continue
        if any(nx.is_isomorphic(G, H) for H in seen): continue
        seen.append(G)
        oc = odd_chain(G, 3); big = not ind_le_1(G)
        if oc == big: agree += 1
        else: dis.append((ell, oc, big))
    print(f"m={m}: classes={len(seen)} agree={agree} disagree={dis}"); sys.stdout.flush()
