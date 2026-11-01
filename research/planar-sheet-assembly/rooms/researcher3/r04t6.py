"""P6 (c=5, odd c): a closed K_5-chain with odd holonomy, K_6-free  =>  L_h >= 6 (Theorem N_h, c odd). Predicted 6."""
import sys, random, networkx as nx
from r04 import chain, holonomy, sign, L_h
from r04gen import gen
from oddchain import odd_chain
from topo import chi
rng = random.Random(5); done = 0
for m in (11, 12, 13):
    for t in range(80):
        ell = gen(m, 5, 4, 6, rng)
        if ell is None: continue
        G, T, c = chain(m, ell); g = holonomy(m, ell, T, c)
        if sign(g) > 0: continue
        if max(len(q) for q in nx.find_cliques(G)) > 5: continue
        print(f"c=5 m={m} ell={ell} hol={g} sgn=- oddchain={odd_chain(G,5)} chi={chi(G)}", end=" "); sys.stdout.flush()
        print("L_h=", L_h(G, 6)); sys.stdout.flush(); done += 1; break
    if done >= 2: break
