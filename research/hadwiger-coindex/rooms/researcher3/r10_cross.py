# R10 researcher3: cross-edge axioms on 3+3 vertex blocks. X = B0 with empties.
import sys, io, contextlib, itertools
sys.path.insert(0, ".")
from r06_lib import make, B0_empty, reduced_betti
def tops(n, E):
    b = reduced_betti(B0_empty(make(n, E), n))
    nz = {k:v for k,v in b.items() if v}
    return (max(nz) if nz else -2), nz
T1 = [(0,1),(1,2),(0,2)]; T2 = [(3,4),(4,5),(3,5)]
cases = {
 "2K3 (no cross)": T1+T2,
 "prism K3xK2 (cross matching)": T1+T2+[(0,3),(1,4),(2,5)],
 "K3 + K3 + cross C6 (K33 minus PM)": T1+T2+[(a,b) for a in range(3) for b in range(3,6) if (a,b) not in [(0,3),(1,4),(2,5)]],
 "K6 (full cross = join)": T1+T2+[(a,b) for a in range(3) for b in range(3,6)],
}
for name,E in cases.items():
    t, nz = tops(6, E)
    print(name, "| top", t, nz, "| join bound 5")
