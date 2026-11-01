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

def ftype(coefs):  # coefs f0..f3 ; return factor degree tuple
    x=sympy.symbols('x')
    poly=sympy.Poly(x**4+coefs[3]*x**3+coefs[2]*x**2+coefs[1]*x+coefs[0],x,modulus=p)
    fl=poly.factor_list()[1]
    if any(m>1 for _,m in fl): return None
    return tuple(sorted(f.degree() for f,_ in fl))
def refl4(v):
    Av=(A4@v)%p; Q=int(v@Av)%p
    if Q==0: return None
    c=(2*pow(Q,-1,p))%p
    return (np.eye(4,dtype=np.int64)-c*np.outer(Av,v))%p   # P = I - 2 Av v^T/Q  (so P A P^T = A)
def act(P,M):  # M: n x 10 array; returns encoded index
    n=M.shape[0]
    S=np.zeros((n,4,4),dtype=np.int64)
    for k,(i,j) in enumerate(pairs):
        S[:,i,j]=M[:,k]; S[:,j,i]=M[:,k]
    R=np.einsum('ab,nbc,dc->nad',P,S,P)%p
    return np.stack([R[:,i,j] for (i,j) in pairs],axis=1)
def enc(M):
    e=np.zeros(M.shape[0],dtype=np.int64)
    for k in range(10): e+=M[:,k]*p**k
    return e
if __name__=="__main__":
    ngen=int(sys.argv[2]); seed=int(sys.argv[3])
    rng=random.Random(seed)
    # choose target quartics: first two of each type
    types=collections.defaultdict(list)
    for c in itertools.product(range(p),repeat=4):
        t=ftype(c)
        if t is not None and len(types[t])<2:
            types[t].append(c)
    targets=[]
    tinfo={}
    for t,l in types.items():
        for c in l:
            k=((c[3]*p+c[2])*p+c[1])*p+c[0]; targets.append(k); tinfo[k]=(t,c)
    print("targets",tinfo,flush=True)
    # sanity: group
    gens=[]
    while len(gens)<ngen:
        v=np.array([rng.randrange(p) for _ in range(4)],dtype=np.int64)
        P=refl4(v)
        if P is None: continue
        assert ((P@A4@P.T)%p==A4).all()
        gens.append(P)
    plen=3 if p==7 else 0
    prefixes=[()] if plen==0 else list(itertools.product(range(p),repeat=plen))
    # for p=5 whole 9.7M at once
    with Pool(4) as pool:
        res=pool.map(chunk,[(pf,targets) for pf in prefixes])
    fib=collections.defaultdict(list)
    for r in res:
        for tk,M in r:
            # prefix entries need to be prepended
            fib[tk].append(M)
    # reconstruct full M with prefix
    full=collections.defaultdict(list)
    for pf,r in zip(prefixes,res):
        for tk,M in r:
            pre=np.tile(np.array(pf,dtype=np.int64),(M.shape[0],1)) if plen else np.zeros((M.shape[0],0),dtype=np.int64)
            full[tk].append(np.hstack([pre,M[:,plen:]]) if plen else M)
    # |O| 
    disc=(-3)%p  # det A4 ; type
    sq=set((x*x)%p for x in range(1,p))
    plus = (disc in sq)  # disc of 4-dim form = det (since (-1)^{2}=1)
    G=2*p**2*(p**2-1)**2 if plus else 2*p**2*(p**4-1)
    print("p",p,"O_4^"+("+" if plus else "-"),"|O|",G)
    for tk in targets:
        M=np.vstack(full[tk]); n=M.shape[0]
        E=enc(M); order=np.argsort(E); Es=E[order]; Ms=M[order]
        lab=np.arange(n)
        perms=[]
        for P in gens:
            Ni=enc(act(P,Ms))
            pos=np.searchsorted(Es,Ni); assert (Es[pos]==Ni).all()
            perms.append(pos)
        while True:
            old=lab.copy()
            for pr in perms: lab=np.minimum(lab,lab[pr])
            lab=lab[lab]
            if np.array_equal(old,lab): break
        u,c=np.unique(lab,return_counts=True)
        print(tinfo[tk],"fiber",n,"orbits",len(u),"sizes",sorted(c.tolist()),"stab",sorted(G//x for x in c.tolist()),flush=True)
