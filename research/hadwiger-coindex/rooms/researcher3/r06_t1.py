# Test 1: homology of B0_empty(G) vs suspension of N(G): H~_k(B0) == H~_{k-1}(N(G))
import sys; sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3')
from r06_lib import *
def cyc(n): return [(i,(i+1)%n) for i in range(n)]
def cplx(n, E): return make(n, E)
tests = {
 "K1": (1, []),
 "K2": (2, cyc(2)[:1]),
 "K3": (3, [(0,1),(1,2),(0,2)]),
 "P3": (3, [(0,1),(1,2)]),
 "C5": (5, cyc(5)),
 "C6": (6, cyc(6)),
 "K4": (4, list(itertools.combinations(range(4),2))),
 "C5+pendant": (6, cyc(5)+[(0,5)]),
}
for name,(n,E) in tests.items():
    adj = make(n,E)
    B = reduced_betti(B0_empty(adj,n))
    N = reduced_betti(Nfaces(adj,n))
    Bs = {k:v for k,v in B.items() if v}
    Ns = {k:v for k,v in N.items() if v}
    # shift: H~_k(B) should equal H~_{k-1}(N)
    shifted = {k+1:v for k,v in Ns.items()}
    print(name, "B0_empty H~:", Bs, " N(G) H~:", Ns, " shift(N)=", shifted, " MATCH" if Bs==shifted else " MISMATCH", flush=True)
