import numpy as np, sys
from oagrp import OA
from fractions import Fraction
def rank_mod(Mx,p):
    M=[list(map(int,r)) for r in Mx]; r=0
    rows=len(M); cols=len(M[0])
    for c in range(cols):
        piv=None
        for i in range(r,rows):
            if M[i][c]%p: piv=i;break
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        inv=pow(M[r][c],-1,p); M[r]=[x*inv%p for x in M[r]]
        for i in range(rows):
            if i!=r and M[i][c]%p:
                f=M[i][c]; M[i]=[(x-f*y)%p for x,y in zip(M[i],M[r])]
        r+=1
    return r
E=[(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
def symmat(i):
    m=np.zeros((3,3),dtype=np.int64); a,b=E[i]; m[a,b]=1; m[b,a]=1; return m
def act_matrix(P,p):
    cols=[]
    for i in range(6):
        X=(P@symmat(i)@P.T)%p
        cols.append([X[a,b] for a,b in E])
    return np.array(cols).T  # 6x6, column i = image of basis i
def run(p):
    G=OA(p)
    tot6=0; tot5=0
    # quotient: basis e_i for i=1..5 plus A=(0,1,1,0,1,0)? A entries: m12=m13=m23=1 -> coords [0,1,1,0,1,0]
    for P in G:
        R=act_matrix(P,p)
        d6=6-rank_mod((R-np.eye(6,dtype=np.int64))%p,p)
        tot6+=p**d6
        # quotient by a=[0,1,1,0,1,0]: choose complement basis: coords indices 0,1,3,4,5 (drop index 2, since a has coordinate at 2 nonzero)
        a=np.array([0,1,1,0,1,0])
        # projection: v -> v - (v[2]/a[2]) a, then take coords [0,1,3,4,5]
        def proj(v): 
            v=(v-v[2]*a)%p; return v[[0,1,3,4,5]]
        Q=np.zeros((5,5),dtype=np.int64)
        keep=[0,1,3,4,5]
        for j,k in enumerate(keep):
            Q[:,j]=proj(R[:,k])
        d5=5-rank_mod((Q-np.eye(5,dtype=np.int64))%p,p)
        tot5+=p**d5
    n=len(G)
    return Fraction(tot6,n),Fraction(tot5,n)
if __name__=="__main__":
  for p in map(int,sys.argv[1:]):
      n6,n5=run(p)
      print(p,"Sym orbits",n6,"formula",2*p**3+p*p+p,"| mod A orbits",n5,"2q^2+q+1=",2*p*p+p+1,"2q^2+2q=",2*p*p+2*p)
