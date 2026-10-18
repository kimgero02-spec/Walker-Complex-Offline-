"""P4 (c=4) and P5 (c=5): L_h = c + [some closed K_c-chain has odd holonomy]  (h-version), predicted before running.
Also the designated H-cycle sign is printed, to see where the R03 conjecture 5.3 differs."""
import sys, random, networkx as nx
from r04 import chain, holonomy, sign, L_h
from r04gen import gen
from oddchain import odd_chain
from topo import chi
rng = random.Random(4)
rows = []
for m in (8, 9, 10, 11, 12):
    got = 0; tries = 0
    while got < 3 and tries < 60:
        tries += 1
        ell = gen(m, 4, 2, 6, rng)
        if ell is None: continue
        G, T, c = chain(m, ell)
        g = holonomy(m, ell, T, c); s = sign(g)
        oc = odd_chain(G, 4); om = max(len(q) for q in nx.find_cliques(G))
        if om > 4: continue          # skip graphs containing K5 (trivial)
        lh = L_h(G, 5); x = chi(G)
        print(f"c=4 m={m} ell={ell} hol={g} sgn(H)={'+' if s>0 else '-'} oddchain={oc} chi={x} L_h={lh} pred={4+int(oc)} {'OK' if lh==4+int(oc) else 'MISS'}")
        sys.stdout.flush(); got += 1
for m in (11, 12, 13):
    G, T, c = chain(m, [5] * m); g = holonomy(m, [5] * m, T, c)
    oc = odd_chain(G, 5)
    print(f"c=5 C_{m}^4 hol={g} sgn={'+' if sign(g)>0 else '-'} oddchain={oc} chi={chi(G)}", end=" "); sys.stdout.flush()
    lh = L_h(G, 6)
    print(f"L_h={lh} pred={5+int(oc)}"); sys.stdout.flush()
