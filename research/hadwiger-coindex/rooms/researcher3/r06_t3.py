# Test 3: (a) zig vs top reduced-homology degree of B0_empty(G); (b) real Hodge: harmonic cochains split by swap sign.
import sys, time; sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3')
from r06_lib import *
import numpy as np
def cyc(n): return [(i,(i+1)%n) for i in range(n)]
def Kmn(m,k): return [(i,m+j) for i in range(m) for j in range(k)]
def mobius(n8=8):  # V8 = Mobius ladder on 8 vertices: cycle 0..7 plus diagonals i,i+4
    return cyc(8)+[(i,i+4) for i in range(4)]
G = {
 "K3":(3,list(itertools.combinations(range(3),2))),
 "K4":(4,list(itertools.combinations(range(4),2))),
 "C5":(5,cyc(5)),
 "C6":(6,cyc(6)),
 "C7":(7,cyc(7)),
 "K33":(6,Kmn(3,3)),
 "W5(wheel)":(6, cyc(5)+[(5,i) for i in range(5)]),
 "V8":(8,mobius()),
}
def top_deg(F):
    B = reduced_betti(F); nz=[k for k,v in B.items() if v]
    return (max(nz) if nz else None), {k:v for k,v in B.items() if v}
for name,(n,E) in G.items():
    t0=time.time()
    adj=make(n,E)
    F=B0_empty(adj,n)
    top,B = top_deg(F)
    z,_ = zig(adj,n,return_order=True)
    print(f"{name}: n={n} zig={z} top H~ degree of B0_empty={top} betti={B} faces={sum(len(v) for v in F.values())} t={time.time()-t0:.1f}s", flush=True)
