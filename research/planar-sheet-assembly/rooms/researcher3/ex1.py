"""P1/P2/P3/P4 checks on a few curated ribbon manuals."""
from surf import *

def band(n, twist):
    # squares k: rim a_k b_k b_{k+1} a_{k+1}; arc alpha_k = (a_k,b_k) between k-1 and k
    P = {}
    for k in range(n):
        a, b = ('a', k), ('b', k)
        if k < n - 1:
            a2, b2 = ('a', k + 1), ('b', k + 1)
        else:
            a2, b2 = (('b', 0), ('a', 0)) if twist else (('a', 0), ('b', 0))
        P[k] = [a, b, b2, a2]
    arcs = []
    for k in range(n):
        prev = (k - 1) % n
        arcs.append((prev, k, [('a', k), ('b', k)]))
    return Manual(P, arcs)

for n in (2, 3, 4):
    report("prism n=%d" % n, band(n, False))
    report("mobius n=%d" % n, band(n, True))

# --- theta manual: two hexagons A,B sharing three single-edge arcs, all rim choices for B
import itertools
A = [0, 1, 2, 3, 4, 5]
arcsAB = [[0, 1], [2, 3], [4, 5]]
seen = set()
res = []
# B rim: cyclic arrangement of the three arcs (each possibly reversed), rails between
for perm in itertools.permutations(range(3)):
    if perm[0] != 0:
        continue
    for flips in itertools.product([0, 1], repeat=3):
        rim = []
        for idx, fl in zip(perm, flips):
            p = arcsAB[idx]
            rim += (p[::-1] if fl else p)
        Mn = Manual({'A': A, 'B': rim}, [('A', 'B', p) for p in arcsAB])
        key = (Mn.b, Mn.orientable())
        r = report("theta B=%s" % rim, Mn, verbose=False)
        res.append(r)
        print("theta B=%s b=%d orient=%s eg=%d rankQ=%d det=%d" % (rim, r['b'], r['orientable'], r['eg'], r['rankQ'], r['detQ']),
              {k: r[k] for k in ('M=NtQinvN', 'rankM', 'I_bipartite', 'planarG') if k in r})
