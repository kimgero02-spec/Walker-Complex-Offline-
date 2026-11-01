import sys,random,collections,itertools,numpy as np
nsamp=int(sys.argv[1])
sys.argv=[sys.argv[0],'7']
exec(open('sim.py').read().split("if p==5:")[0].replace("p=int(sys.argv[1]); nsamp=int(sys.argv[2]) if len(sys.argv)>2 else 0","p=7"))
nr=np.random.default_rng(3)
types=collections.defaultdict(list)
for c in itertools.product(range(p),repeat=4):
    t=ftype(c)
    if t is not None and len(types[t])<1: types[t].append(c)
tinfo={}
for t,l in types.items():
    for c in l: tinfo[((c[3]*p+c[2])*p+c[1])*p+c[0]]=(t,c)
hits=collections.defaultdict(list)
for it in range(nsamp):
    n=2_000_000
    ent={pr:nr.integers(0,p,n) for pr in pairs}
    f=quartic_f(ent)
    key=((f[3]*p+f[2])*p+f[1])*p+f[0]
    for tk in tinfo:
        sel=np.where(key==tk)[0]
        if len(sel): hits[tk].append(np.stack([ent[pr][sel] for pr in pairs],axis=1))
def orbit(M0,gens):
    allv=enc(M0[None,:]); fr=M0[None,:]
    while len(fr):
        news=[act(P,fr)*pow(m,-1,p)%p for P,m in gens]
        Rr=np.vstack(news); e=enc(Rr)
        e,ui=np.unique(e,return_index=True); Rr=Rr[ui]
        msk=~np.isin(e,allv); fr=Rr[msk]; allv=np.union1d(allv,e[msk])
    return allv
for tk,(t,c) in tinfo.items():
    H=np.vstack(hits[tk]); row=[]
    for name,g in sets.items():
        seen=np.array([],dtype=np.int64); sizes=[]
        for i in range(len(H)):
            e=enc(H[i][None,:])[0]
            if e in seen: continue
            o=orbit(H[i],g); sizes.append(len(o)); seen=np.union1d(seen,o)
            if len(seen)>=112896: break
        row.append((name,len(sizes),sorted(sizes)[:2],sum(sizes)))
    print(t,c,"hits",len(H),row,flush=True)
