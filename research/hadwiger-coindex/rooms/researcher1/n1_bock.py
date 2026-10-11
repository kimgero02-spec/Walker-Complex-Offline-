import itertools, numpy as np
from fractions import Fraction
def quotient_complex(P, ch):
    """P: list of closed pairs (A,B); ch: chains (tuples of increasing). sigma(A,B)=(B,A).
    returns cells dims 0..2 of Y=X/sigma with orientation signs."""
    sig=lambda c: tuple((p[1],p[0]) for p in reversed(c))  # reversed order -> still increasing chain
    cells=[]; 
    out=[]
    for k,L in enumerate(ch):
        reps={}; lst=[]
        for c in L:
            s=sig(c)
            if c<=s: reps[c]=(len(lst),1); lst.append(c)   # rep is c
        sign=(-1)**((k+1)*k//2)   # chain with k+1 vertices -> reversal sign (-1)^{(k+1)k/2}
        idx={}
        for c in L:
            s=sig(c)
            if c<=s: idx[c]=(reps[c][0],1)
            else: idx[c]=(reps[s][0],sign)
        out.append((lst,idx))
    return out
def bdry(out,k):
    lst,idx=out[k]; lst0,idx0=out[k-1]
    M=np.zeros((len(lst0),len(lst)),dtype=object)
    for j,c in enumerate(lst):
        for t in range(len(c)):
            f=c[:t]+c[t+1:]
            i,s=idx0[f]
            M[i,j]+=s*(-1)**t
    return M
def in_lattice(M,b):
    """is b in integer column lattice of M? (M: m x n int object matrix)"""
    M=[list(map(int,M[:,j])) for j in range(M.shape[1])]  # columns
    b=list(map(int,b)); m=len(b)
    cols=[c[:] for c in M if any(c)]
    # echelon by rows
    r=0
    basis=[]
    rows_done=0
    for row in range(m):
        # gcd-reduce cols on this row among cols not yet pivoted
        while True:
            nz=[c for c in cols if c[row]!=0]
            if len(nz)<=1: break
            nz.sort(key=lambda c:abs(c[row]))
            p=nz[0]
            for c in nz[1:]:
                q=c[row]//p[row]
                for i in range(m): c[i]-=q*p[i]
        nz=[c for c in cols if c[row]!=0]
        if nz:
            p=nz[0]; cols=[c for c in cols if c is not p]
            basis.append((row,p))
        # remaining cols have zero in this row
    bb=b[:]
    for row,p in basis:
        if bb[row]%p[row]!=0: 
            return False
        q=bb[row]//p[row]
        for i in range(m): bb[i]-=q*p[i]
    return all(x==0 for x in bb)
def bockstein_zero(P,ch):
    out=quotient_complex(P,ch)
    if len(out)<2: return True
    # vertex sheet: rep vertex sheet 0; if idx sign... vertex orbit: c rep -> sheet 0, sig(c) -> sheet 1
    lst0,idx0=out[0]
    sheet={}
    for c,(i,s) in idx0.items():
        sheet[c]=0 if lst0[i]==c else 1
    lst1,idx1=out[1]
    flip=[ (sheet[(e[0],)]+sheet[(e[1],)])%2 for e in lst1 ]
    d1=bdry(out,1)  # vertices x edges
    # check cocycle mod 2: flip is cocycle: d2^T flip even on every 2-cell
    if len(out)>=3:
        d2=bdry(out,2)  # edges x triangles
        coc=np.array(flip,dtype=object).dot(d2)  # integer values per triangle
        assert all(int(x)%2==0 for x in coc), "flip not cocycle"
        beta=[int(x)//2 for x in coc]
        # beta in the image of d2^T? want gamma (1-cochain... ) with delta gamma = beta ; delta gamma on a 2-cell = gamma . d2 col
        # gamma is 1-cochain: gamma^T d2 = beta  => d2^T gamma = beta
        return in_lattice(d2.T, beta)
    return True
