import sys,random,collections,itertools,numpy as np
sys.argv=[sys.argv[0],'7']+sys.argv[1:]
import k4
from k4 import *
ngen=int(sys.argv[2]); seed=int(sys.argv[3]); nsamp=int(sys.argv[4])
rng=random.Random(seed); nr=np.random.default_rng(seed)
types=collections.defaultdict(list)
for c in itertools.product(range(p),repeat=4):
    t=ftype(c)
    if t is not None and len(types[t])<2: types[t].append(c)
tinfo={}
for t,l in types.items():
    for c in l: tinfo[((c[3]*p+c[2])*p+c[1])*p+c[0]]=(t,c)
gens=[]
while len(gens)<ngen:
    v=np.array([rng.randrange(p) for _ in range(4)],dtype=np.int64)
    P=refl4(v)
    if P is None: continue
    gens.append(P)
hits=collections.defaultdict(list)
for it in range(nsamp):
    n=2_000_000
    ent={pr:nr.integers(0,p,n) for pr in pairs}
    f=quartic_f(ent)
    key=((f[3]*p+f[2])*p+f[1])*p+f[0]
    for tk in tinfo:
        sel=np.where(key==tk)[0]
        if len(sel): hits[tk].append(np.stack([ent[pr][sel] for pr in pairs],axis=1))
G=2*p**2*(p**2-1)**2
def orbit(M0):
    vis=enc(M0[None,:]); allv=vis.copy(); fr=M0[None,:]
    while len(fr):
        news=[]
        for P in gens:
            R=act(P,fr); news.append(R)
        R=np.vstack(news); e=enc(R)
        e,ui=np.unique(e,return_index=True); R=R[ui]
        m=~np.isin(e,allv)
        fr=R[m]; allv=np.union1d(allv,e[m])
    return allv
for tk,(t,c) in tinfo.items():
    H=np.vstack(hits[tk]); 
    seen=np.array([],dtype=np.int64); orbs=[]
    for i in range(len(H)):
        e=enc(H[i][None,:])[0]
        if e in seen: continue
        o=orbit(H[i]); orbs.append(len(o)); seen=np.union1d(seen,o)
        if len(seen)>=G//2: break
    # check all hits covered
    cov=np.isin(enc(H),seen).all()
    print(t,c,"hits",len(H),"orbits found",len(orbs),sorted(orbs),"sum",sum(orbs),"|O|/2=",G//2,"all hits covered",cov,flush=True)
