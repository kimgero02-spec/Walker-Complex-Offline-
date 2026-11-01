import sys, time; sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3')
from r06_lib import *
def cyc(n): return [(i,(i+1)%n) for i in range(n)]
n=10; E=[]
for (a,b) in cyc(5):
    for i in range(2):
        for j in range(2): E.append((2*a+i,2*b+j))
for a in range(5): E.append((2*a,2*a+1))
adj=make(n,E)
F=B0_empty(adj,n); B=reduced_betti(F)
print("C5[K2] B0_empty reduced betti:", {k:v for k,v in B.items() if v}, flush=True)
N=reduced_betti(Nfaces(adj,n)); print("C5[K2] N(G) reduced betti:", {k:v for k,v in N.items() if v}, flush=True)
