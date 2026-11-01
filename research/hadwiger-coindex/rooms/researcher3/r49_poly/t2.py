from lib import *
from fractions import Fraction
import networkx as nx, time
def Mmat(W1,W2,H,x):
    P1=list(set_partitions(W1)); P2=list(set_partitions(W2))
    return P1,P2,[[M_entry(pi,rho,H,x) for rho in P2] for pi in P1]
def report(name,W1,W2,H):
    out=[]
    for x in (6,10**6+3):
        P1,P2,M=Mmat(W1,W2,H,x); out.append(rank_mod(M))
    P1,P2,M=Mmat(W1,W2,H,1000)
    ratios={Fraction(M[i][j],ff(1000,len(pi))*ff(1000,len(rho))) for i,pi in enumerate(P1) for j,rho in enumerate(P2)}
    print(f'{name:28s} |W|=({len(W1)},{len(W2)}) Bell=({len(P1)},{len(P2)}) rank@x=6:{out[0]} rank@generic:{out[1]}  M∝uu^T:{len(ratios)==1}')
A=lambda m:['a%d'%i for i in range(m)]; B=lambda m:['b%d'%i for i in range(m)]
report('empty',A(3),B(3),[])
report('single edge',A(3),B(3),[('a0','b0')])
report('star a0->b0,b1,b2',A(1),B(3),[('a0','b0'),('a0','b1'),('a0','b2')])
report('path a0-b0-a1 (2 edges)',A(2),B(1),[('a0','b0'),('a1','b0')])
for m in (2,3,4,5):
    report('matching m=%d'%m,A(m),B(m),[('a%d'%i,'b%d'%i) for i in range(m)])
for m,n in ((2,2),(3,2),(3,3),(4,3),(4,4)):
    report('join K_{%d,%d}'%(m,n),A(m),B(n),[(a,b) for a in A(m) for b in B(n)])
for m in (4,5,6):
    H=[('a%d'%i,'b%d'%((i+s)%m)) for i in range(m) for s in (0,1,2)]
    t=time.time(); report('3-reg circulant m=%d'%m,A(m),B(m),H)
