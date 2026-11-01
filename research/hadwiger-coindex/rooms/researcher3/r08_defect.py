# R08 researcher3: sheet defect test. Union of sheet complexes inside B_0(G) for edge splits.
import sys, itertools
sys.path.insert(0, "/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3")
from r06_lib import make, B0_empty, reduced_betti

def cross_ok(E_sub, n, f):
    # f = tuple of ids; cross pairs (i in copy1, n+j in copy2) must be edges of E_sub
    A = [x for x in f if x < n]; B = [x-n for x in f if x >= n]
    S = set(map(frozenset, E_sub))
    return all(frozenset((a,b)) in S for a in A for b in B)

def sheet_union_betti(n, E_all, sheets):
    F = B0_empty(make(n, E_all), n)
    out = {}
    for k in sorted(F):
        keep = [f for f in F[k] if any(cross_ok(s, n, f) for s in sheets)]
        if keep: out[k] = keep
    # reduced betti of the subcomplex (faces closed under subsets automatically since each sheet B_0 is a complex)
    return reduced_betti(out), {k: len(v) for k, v in out.items()}

def sheet_B0_betti(n, E_sub):
    F = B0_empty(make(n, E_sub), n)
    return reduced_betti(F)

K6 = list(itertools.combinations(range(6),2))
PM3 = [(0,3),(1,4),(2,5)]
OCT = [e for e in K6 if e not in PM3]
print("B0(oct) reduced betti", {k:v for k,v in sheet_B0_betti(6, OCT).items() if v})
print("B0(PM3) reduced betti", {k:v for k,v in sheet_B0_betti(6, PM3).items() if v})
b, sizes = sheet_union_betti(6, K6, [OCT, PM3])
print("union of sheet complexes in B0(K6): reduced betti", {k:v for k,v in b.items() if v}, sizes)
print("B0(K6) reduced betti", {k:v for k,v in sheet_B0_betti(6, K6).items() if v})
