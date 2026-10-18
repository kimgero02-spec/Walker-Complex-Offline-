import sys, time; sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3')
from r06_lib import *
def cyc(n): return [(i,(i+1)%n) for i in range(n)]
adj=make(6,cyc(6)); z,o=zig(adj,6,return_order=True)
print("zig(C6)=",z,"order",o)
for X,Y in max_bicliques(adj,6):
    print(" biclique X=",[i for i in range(6) if X>>i&1]," Y=",[i for i in range(6) if Y>>i&1]," runs=",runs(o,X,Y))
# C5[K2] (lex product) homology of B0_empty, n=10
n=10; E=[]
C5=cyc(5)
for (a,b) in C5:
    for i in range(2):
        for j in range(2):
            E.append((2*a+i,2*b+j))
for i in range(2):
    E.append((2*0+i,2*0+1-i)) if False else None
for a in range(5):
    E.append((2*a,2*a+1))
t0=time.time()
adj=make(10,E)
F=B0_empty(adj,10)
print("C5[K2] faces", sum(len(v) for v in F.values()), flush=True)
print("C5[K2]-version W/ internal edges? note: K2 blow-up has edge inside blob ->"," (lex product C5[K2] has blobs = K2 (adjacent)")
