import numpy as np, sys, itertools
from fractions import Fraction
from burn import rank_mod
def ad(g,p):
    # g in GL2(F_p), Ad on sl2 basis e,h,f
    a,b,c,d=[int(x)%p for x in g.flatten()]
    det=(a*d-b*c)%p; inv=pow(det,-1,p)
    gi=np.array([[d,-b],[-c,a]])*inv%p
    g=np.array([[a,b],[c,d]])
    basis=[np.array([[0,1],[0,0]]),np.array([[1,0],[0,-1]]),np.array([[0,0],[1,0]])]
    cols=[]
    for X in basis:
        Y=(g@X@gi)%p
        # coords: e coef=Y01, h coef=Y00, f coef=Y10
        cols.append([Y[0,1],Y[0,0],Y[1,0]])
    return np.array(cols).T%p
def elems(p):
    L=[(1,ad(np.eye(2,dtype=np.int64),p))]
    L.append((p*p-1,ad(np.array([[1,1],[0,1]]),p)))
    for a in range(2,p): L.append((p*(p+1)//2,ad(np.array([[a,0],[0,1]]),p)))
    # nonsplit torus: find irreducible x^2 - t x + n with generator of F_{p^2}^x: use companion of x^2 - n for nonresidue n? element sqrt(n) is not a generator generally.
    # build F_{p^2}=F_p[s]/(s^2-n), n nonresidue; elements a+bs as matrices [[a,n b],[b,a]]; take all nonzero elements modulo F_p^*: reps k via brute force classes
    n=next(x for x in range(2,p) if pow(x,(p-1)//2,p)==p-1)
    seen=set(); reps=[]
    els=[(a,b) for a in range(p) for b in range(p) if (a,b)!=(0,0)]
    # group elements mod scalars: normalize
    def norm(a,b):
        if a!=0: i=pow(a,-1,p); return (1,b*i%p)
        return (0,1)
    T=sorted(set(norm(a,b) for a,b in els))
    assert len(T)==p+1
    for (a,b) in T:
        if (a,b)==(1,0): continue
        g=np.array([[a,n*b],[b,a]])
        L.append((p*(p-1)//2,ad(g,p)))
    return L
def burnside(p):
    L=elems(p); tot_w=sum(w for w,_ in L); assert tot_w==p*(p*p-1),(tot_w)
    tot=0
    I9=np.eye(9,dtype=np.int64)
    for w1,A1 in L:
        for w2,A2 in L:
            K=np.kron(A1,A2)%p
            dp=9-rank_mod((K-I9)%p,p); dm=9-rank_mod((K+I9)%p,p)
            tot+=w1*w2*(p**dp+p**dm)
    return Fraction(tot,2*(p*(p*p-1))**2)
if __name__=="__main__":
    for p in map(int,sys.argv[1:]):
        print(p,burnside(p),Fraction(2*p**3+4*p*p+7*p+5,2),flush=True)
