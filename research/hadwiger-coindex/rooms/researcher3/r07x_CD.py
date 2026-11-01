import sys, itertools; sys.path.insert(0,'/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3')
from r06_lib import zig
import numpy as np
def cross(e,f,pos):
    a,b=sorted((pos[e[0]],pos[e[1]])); c,d=sorted((pos[f[0]],pos[f[1]]))
    return (a<c<b<d) or (c<a<d<b)
def min_colors_crossing(E,pos,maxk=6):
    m=len(E); conf=[[cross(E[i],E[j],pos) for j in range(m)] for i in range(m)]
    for k in range(1,maxk+1):
        col=[-1]*m
        def bt(i):
            if i==m: return True
            for c in range(k):
                if all(not(conf[i][j] and col[j]==c) for j in range(i)):
                    col[i]=c
                    if bt(i+1): return True
            col[i]=-1; return False
        if bt(0): return k
    return None
def book_thickness(n,E):
    best=None
    for perm in itertools.permutations(range(n)):
        if perm[0]!=0: continue  # reversal symmetry
        pos={v:perm[v] for v in range(n)}
        k=min_colors_crossing(E,pos,maxk=(best-1 if best else 6))
        if k is not None and (best is None or k<best): best=k
        if best==1: break
    return best
K=lambda n: list(itertools.combinations(range(n),2))
K33=[(i,3+j) for i in range(3) for j in range(3)]
C5=[(i,(i+1)%5) for i in range(5)]
tests={"K5":(5,K(5)),"K33":(6,K33),"C5":(5,C5),"K6":(6,K(6))}
for nm,(n,E) in tests.items():
    bt=book_thickness(n,E)
    print(nm,"book thickness(min over spine orders, n<=6 brute)=",bt, flush=True)
# D: Z_3 unbranched cover K33 -> theta (2 vertices, 3 parallel edges): b1 check
def betti1(n,E):
    m=len(E); return m-n+1
print("b1(K33)=",betti1(6,K33),"  b1(theta)=",betti1(2,[(0,1)]*3),
      "  trivial-char part=b1(theta)=2, nontrivial chars contribute",betti1(6,K33)-2)
# Euler check formula chi(G)=k*chi(H)-sum_v(k-|f^-1 v|) for K33->theta (k=3, fibers 3,3)
chiG=6-9; chiH=2-3
print("RH check K33->theta:", chiG, "=?", 3*chiH-((3-3)+(3-3)))
