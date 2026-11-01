import sys, time; sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3')
from r06_lib import *
from r06_hodge import hodge
def cyc(n): return [(i,(i+1)%n) for i in range(n)]
n=7; C=set(tuple(sorted(e)) for e in cyc(7))
Cb=[e for e in itertools.combinations(range(7),2) if e not in C]
adj=make(7,Cb)
F=B0_empty(adj,7); B=reduced_betti(F)
N=reduced_betti(Nfaces(adj,7))
print("comp(C7): B0 betti", {k:v for k,v in B.items() if v}, " N betti", {k:v for k,v in N.items() if v}, flush=True)
z,o=zig(adj,7,return_order=True); print("zig(comp C7)=",z, o, flush=True)
o2=hodge(adj,7,"cC7")
print("comp(C7) real Hodge (inv,anti):", {k:v for k,v in o2.items() if v!=(0,0)}, flush=True)
# domination check
dom=[(a,c) for a in range(7) for c in range(7) if c!=a and adj[a] and (adj[a] & ~adj[c])==0]
print("dominated pairs in comp(C7):", dom)
