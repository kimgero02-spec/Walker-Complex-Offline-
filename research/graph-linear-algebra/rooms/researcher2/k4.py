import numpy as np, sys, itertools, random, collections, sympy
from multiprocessing import Pool
p=int(sys.argv[1]) if len(sys.argv)>1 else 5
A4=np.ones((4,4),dtype=np.int64)-np.eye(4,dtype=np.int64)
pairs=[(i,j) for i in range(4) for j in range(i,4)]
def det4(a):  # a: 4x4 list of arrays (int32/64) mod p
    # Laplace via 2x2 minors of rows (0,1) and (2,3)
    def mn(r1,r2,c1,c2): return (a[r1][c1]*a[r2][c2]-a[r1][c2]*a[r2][c1])%p
    tot=0
    cols=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    for (c1,c2) in cols:
        rest=[c for c in range(4) if c not in (c1,c2)]
        sign=(-1)**(c1+c2+1)  # sign for rows 0,1 -> (-1)^{(0+1)+(c1+c2)} with 0-index shift: use +2
        sign=(-1)**((0+1)+(c1+c2))
        tot=tot+sign*mn(0,1,c1,c2)*mn(2,3,rest[0],rest[1])
    return tot%p
# interpolation matrix: g(t)=sum c_k t^k at t=0..4
V=sympy.Matrix(5,5,lambda i,j: i**j)
Vinv=np.array(V.inv_mod(p).tolist(),dtype=np.int64)
def quartic_f(ent):
    # ent: dict (i,j)->array
    vals=[]
    for t in range(5):
        a=[[ (t*int(A4[i][j])-ent[(min(i,j),max(i,j))])%p for j in range(4)] for i in range(4)]
        vals.append(det4(a))
    vals=np.stack(vals)  # 5 x n
    c=(Vinv@vals)%p      # coefficients c0..c4
    lead=(-3)%p
    assert (c[4]==lead).all()
    il=pow(lead,-1,p)
    f=(c[:4]*il)%p   # monic quartic: x^4 + f3 x^3+..: f[k] coefficient of t^k, k<4
    return f
def chunk(args):
    prefix,targets=args
    n=p**(10-len(prefix))
    idx=np.arange(n,dtype=np.int64)
    ent={}
    k=0
    for pi,(i,j) in enumerate(pairs):
        if pi<len(prefix): ent[(i,j)]=np.full(n,prefix[pi],dtype=np.int64)
        else:
            ent[(i,j)]=(idx//p**(pi-len(prefix)))%p
    f=quartic_f(ent)
    key=((f[3]*p+f[2])*p+f[1])*p+f[0]
    out=[]
    for tk in targets:
        sel=np.where(key==tk)[0]
        if len(sel):
            M=np.stack([ent[pr][sel] for pr in pairs],axis=1)
            out.append((tk,M))
    return out
