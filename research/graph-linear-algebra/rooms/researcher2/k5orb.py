import numpy as np, random, itertools
p=3;n=5
A=np.ones((n,n),dtype=np.int64)-np.eye(n,dtype=np.int64)
pairs=[(i,j) for i in range(n) for j in range(i,n)]
d=np.load('/tmp/claude-0/k5fib.npy',allow_pickle=True).item()
tmap={(1,2,2):(0,1,0,0,0),(1,1,3):(0,1,0,0,1),(1,4):(0,1,0,1,1),(1,1,1,2):(0,1,1,1,2),(5,):(1,0,0,0,2),(2,3):(1,0,0,1,2)}
def refl(v):
    Av=(A@v)%p; Q=int(v@Av)%p
    if Q==0: return None
    c=(2*pow(Q,-1,p))%p
    return (np.eye(n,dtype=np.int64)-c*np.outer(Av,v))%p
rng=random.Random(2); gens=[]
while len(gens)<8:
    P=refl(np.array([rng.randrange(p) for _ in range(n)],dtype=np.int64))
    if P is not None: gens.append(P)
# also SO gens: products of two reflections
so=[(gens[0]@g)%p for g in gens[1:]]
def enc(M): return sum(M[:,k]*p**k for k in range(15))
def act(P,M):
    S=np.zeros((M.shape[0],n,n),dtype=np.int64)
    for k,(i,j) in enumerate(pairs): S[:,i,j]=M[:,k]; S[:,j,i]=M[:,k]
    R=np.einsum('ab,mbc,dc->mad',P,S,P)%p
    return np.stack([R[:,i,j] for (i,j) in pairs],axis=1)
for t,c in tmap.items():
    key=sum(c[k]*p**k for k in range(5)); M=d[key]
    E=enc(M); o=np.argsort(E); Es=E[o]; Ms=M[o]
    for name,G in (('O',gens),('SO',so)):
        lab=np.arange(len(Ms)); perms=[]
        for P in G:
            pos=np.searchsorted(Es,enc(act(P,Ms))); assert (Es[pos]==enc(act(P,Ms))).all(); perms.append(pos)
        while True:
            old=lab.copy()
            for pr in perms: lab=np.minimum(lab,lab[pr])
            lab=lab[lab]
            if np.array_equal(old,lab): break
        u,cn=np.unique(lab,return_counts=True)
        print(t,c,name,"fiber",len(Ms),"orbits",len(u),"sizes",sorted(set(cn.tolist())),flush=True)
