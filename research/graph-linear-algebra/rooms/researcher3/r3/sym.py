import itertools, numpy as np, sys
from collections import defaultdict
from oagrp import OA
def run(p):
    G=OA(p)
    # all symmetric M as arrays
    idx=list(itertools.product(range(p),repeat=6))
    Ms=np.array(idx)  # m11 m12 m13 m22 m23 m33
    n=len(Ms)
    full=np.zeros((n,3,3),dtype=np.int64)
    full[:,0,0]=Ms[:,0];full[:,0,1]=full[:,1,0]=Ms[:,1];full[:,0,2]=full[:,2,0]=Ms[:,2]
    full[:,1,1]=Ms[:,3];full[:,1,2]=full[:,2,1]=Ms[:,4];full[:,2,2]=Ms[:,5]
    w=np.array([p**5,p**4,p**3,p**2,p,1])
    def index(F):
        v=np.stack([F[:,0,0],F[:,0,1],F[:,0,2],F[:,1,1],F[:,1,2],F[:,2,2]],1)%p
        return v@w
    lab=np.arange(n)
    for P in G:
        F=(P@full@P.T)%p
        lab=np.minimum(lab,index(F))
    # charpoly of N=A^{-1}M : det(tA-M)=2f ; compute f coefficients via g
    m11,m12,m13,m22,m23,m33=[Ms[:,i] for i in range(6)]
    g2=(m11-2*m12-2*m13+m22-2*m23+m33)
    g1=(-2*m11*m23+2*m12*m13+2*m12*m23-2*m12*m33-2*m13*m22+2*m13*m23)
    g0=(-m11*m22*m33+m11*m23**2+m12**2*m33-2*m12*m13*m23+m13**2*m22)
    inv2=pow(2,-1,p)
    a1=(g2*inv2)%p;a2=(g1*inv2)%p;a3=(g0*inv2)%p
    orb=defaultdict(set)
    for i in range(n): orb[(a1[i],a2[i],a3[i])].add(lab[i])
    return orb
def typ(f,p):
    a1,a2,a3=f
    roots=[x for x in range(p) if (x**3+a1*x*x+a2*x+a3)%p==0]
    # multiplicity via derivative
    def ev(c,x): 
        r=0
        for k in c: r=(r*x+k)%p
        return r
    mult={}
    for r in roots:
        m=0; c=[1,a1,a2,a3]
        # synthetic division
        while True:
            q=[c[0]]
            for k in c[1:-1]: q.append((k+q[-1]*r)%p)
            rem=(c[-1]+q[-1]*r)%p
            if rem!=0 or len(c)<=1: break
            m+=1; c=q
            if len(c)==1: break
        mult[r]=m
    ms=sorted(mult.values(),reverse=True)
    return tuple(ms), len(roots)
for p in map(int,sys.argv[1:]):
    orb=run(p)
    tot=sum(len(v) for v in orb.values())
    print("q=",p,"N=",tot,"formula",2*p**3+p*p+p, "nf",len(orb))
    by=defaultdict(set)
    for f,v in orb.items():
        t=typ(f,p)[0]
        by[t].add(len(v))
    print(dict(by))
