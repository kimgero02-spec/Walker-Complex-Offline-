"""Predictions tested (stated before running, see report sec. 4):
P1 (c=3): every closed triangle chain with odd holonomy has ind B >= 2 (zlift False), L_h = 4.
P2 (c=3, local): even holonomy => ind B <= 1 (zlift True)."""
import sys
from r04 import chain, holonomy, sign, L_h
from r04gen import find, cycle_type
from zlift import ind_le_1
from topo import chi
cases = [(7, (2, 1)), (8, (2, 1)), (9, (2, 1)), (10, (2, 1)), (9, (3,)), (10, (3,)), (11, (3,)), (12, (1, 1, 1))]
for m, ct in cases:
    ell = find(3, m, ct, 2, 4, seed=m)
    if ell is None: print(m, ct, "not found"); continue
    G, T, c = chain(m, ell); g = holonomy(m, ell, T, c)
    print(f"m={m} ell={ell} hol-type={ct} sgn={'+' if sign(g)>0 else '-'} chi={chi(G)} L_h={L_h(G,4)} ind<=1:{ind_le_1(G)}")
    sys.stdout.flush()
