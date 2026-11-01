import sys; sys.path.insert(0,'/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3')
from r06_lib import *
def cyc(n): return [(i,(i+1)%n) for i in range(n)]
K=lambda n: list(itertools.combinations(range(n),2))
def zz(n,E): return zig(make(n,E),n)
K5=K(5); K5e=[e for e in K5 if e!=(0,1)]
K33=[(i,3+j) for i in range(3) for j in range(3)]; K33e=[e for e in K33 if e!=(0,3)]
oct_=[e for e in K(6) if e not in [(0,3),(1,4),(2,5)]]
V8=cyc(8)+[(i,i+4) for i in range(4)]
rows = {
 "K5-e (planar?)":(5,K5e), "K5":(5,K5), "K33-e":(6,K33e), "K33":(6,K33),
 "octahedron K6-PM (planar)":(6,oct_), "V8":(8,V8), "K6":(6,K(6)),
}
for k,(n,E) in rows.items(): print(k, "zig=",zz(n,E), flush=True)
print("K2 zig=",zz(2,[(0,1)]))
