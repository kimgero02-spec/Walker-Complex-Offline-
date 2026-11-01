import numpy as np, itertools, collections, random, sympy, time
p=3; n=5
A=np.ones((n,n),dtype=np.int64)-np.eye(n,dtype=np.int64)
pairs=[(i,j) for i in range(n) for j in range(i,n)]  # 15
# interpolation of integer polynomial degree 5 from t=0..5
V=sympy.Matrix(6,6,lambda i,j:i**j); Vi=np.array(V.inv().tolist(),dtype=object)
from fractions import Fraction
Vif=np.array([[float(x) for x in r] for r in V.inv().tolist()])
t0=time.time()
N=p**15
keys=np.zeros(0,dtype=np.int64)
B=1<<20
fib=collections.defaultdict(list)
# target polys: monic quintic f over F3 squarefree, types
x=sympy.symbols('x')
def ftype(c):  # c=f0..f4
    P=sympy.Poly(x**5+sum(c[k]*x**k for k in range(5)),x,modulus=p)
    fl=P.factor_list()[1]
    if any(m>1 for _,m in fl): return None
    return tuple(sorted(f.degree() for f,_ in fl))
types=collections.defaultdict(list)
for c in itertools.product(range(p),repeat=5):
    t=ftype(c)
    if t is not None and len(types[t])<1: types[t].append(c)
print({t:l for t,l in types.items()},flush=True)
tkeys={}
for t,l in types.items():
    c=l[0]; tkeys[sum(c[k]*p**k for k in range(5))]=t
tk_arr=np.array(list(tkeys.keys()))
Af=A.astype(np.float64)
for start in range(0,N,B):
    idx=np.arange(start,min(N,start+B),dtype=np.int64)
    m=len(idx)
    ent=np.stack([(idx//p**k)%p for k in range(15)],axis=1)
    S=np.zeros((m,n,n))
    for k,(i,j) in enumerate(pairs):
        S[:,i,j]=ent[:,k]; S[:,j,i]=ent[:,k]
    vals=np.stack([np.linalg.det(t*Af[None]-S) for t in range(6)],axis=1)  # m x 6
    c=np.rint(vals@Vif.T).astype(np.int64)  # coefficients c0..c5 (integers)
    assert (c[:,5]==4).all()
    # f = g/4 mod 3 ; 4=1 mod 3
    f=c[:,:5]%p
    key=sum(f[:,k]*p**k for k in range(5))
    msk=np.isin(key,tk_arr)
    if msk.any():
        for kk in np.unique(key[msk]):
            sel=np.where(key==kk)[0]
            fib[int(kk)].append(ent[sel])
print("enum done",time.time()-t0,flush=True)
np.save('/tmp/claude-0/k5fib.npy',{k:np.vstack(v) for k,v in fib.items()},allow_pickle=True)
