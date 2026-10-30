import sys, time; sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3')
from r06_lib import *
from r06_hodge import hodge
def cyc(n): return [(i,(i+1)%n) for i in range(n)]
t0=time.time()
o=hodge(make(6,list(itertools.combinations(range(6),2))),6,"K6")
print("K6 real Hodge (inv,anti) per k:", {k:v for k,v in o.items() if v!=(0,0)}, f"{time.time()-t0:.1f}s", flush=True)
# Petersen: outer 0-4 cycle, inner 5-9 pentagram, spokes
P=[(i,(i+1)%5) for i in range(5)]+[(5+i,5+(i+2)%5) for i in range(5)]+[(i,5+i) for i in range(5)]
t0=time.time()
adj=make(10,P)
F=B0_empty(adj,10)
print("Petersen faces", sum(len(v) for v in F.values()), flush=True)
B=reduced_betti(F)
print("Petersen B0_empty reduced betti:", {k:v for k,v in B.items() if v}, f"{time.time()-t0:.1f}s", flush=True)
