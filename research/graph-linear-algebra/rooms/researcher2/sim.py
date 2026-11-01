import sys,random,collections,itertools,numpy as np
p=int(sys.argv[1]); nsamp=int(sys.argv[2]) if len(sys.argv)>2 else 0
sys.argv=[sys.argv[0],str(p)]
import k4
from k4 import *
sq=set((x*x)%p for x in range(1,p))
def find_sims(mu,count=3,rng=random.Random(1)):
    # rows r_i with r_i A r_j^T = mu A_ij
    vecs=[np.array(v,dtype=np.int64) for v in itertools.product(range(p),repeat=4)]
    out=[]
    def bt(rows):
        i=len(rows)
        if i==4: return rows
        cand=vecs[:]; rng.shuffle(cand)
        for v in cand:
            if all(int(rows[j]@A4@v)%p==(mu*int(A4[j][i]))%p for j in range(i)) and int(v@A4@v)%p==(mu*int(A4[i][i]))%p:
                r=bt(rows+[v])
                if r: return r
        return None
    for _ in range(count):
        r=bt([]); P=np.array(r)%p
        assert ((P@A4@P.T)%p==(mu*A4)%p).all()
        out.append(P)
    return out
def detmod(P):
    import sympy
    return int(sympy.Matrix(P.tolist()).det())%p
def actsim(P,M,mu):
    R=act(P,M); return (R*pow(mu,-1,p))%p
ns=[m for m in range(1,p) if m not in sq]
mu=ns[0]
sims=find_sims(mu,4)
for S in sims: print("sim det",detmod(S),"mu^2",(mu*mu)%p,"-mu^2",(-mu*mu)%p)
rng=random.Random(5)
def refls(n):
    out=[]
    while len(out)<n:
        v=np.array([rng.randrange(p) for _ in range(4)],dtype=np.int64)
        P=refl4(v)
        if P is not None: out.append(P)
    return out
R=refls(10)
# group gens as (matrix, mu, det sign)
def gen_sets():
    O=[(P,1) for P in R]
    SO=[((R[0]@R[i])%p,1) for i in range(1,len(R))]+[((R[1]@R[i])%p,1) for i in range(2,len(R))]
    # similitudes: proper ones (det=+mu^2)
    props=[];imps=[]
    for S in sims:
        d=detmod(S)
        (props if d==(mu*mu)%p else imps).append((S,mu))
    # also multiply by reflections to get both kinds
    allsim=[(S,mu) for S in sims]
    GSO=SO[:]; GO=O[:]
    for S,m in allsim:
        d=detmod(S)
        if d==(m*m)%p: GSO.append((S,m))
        else: GSO.append(((S@R[0])%p,m))
        GO.append((S,m))
    return {'O':O,'SO':SO,'GSO':GSO,'GO':GO}
sets=gen_sets()
def orbits_in(M,gens):
    n=M.shape[0]
    E=enc(M); order=np.argsort(E); Es=E[order]; Ms=M[order]
    lab=np.arange(n); perms=[]
    for P,m in gens:
        Ni=enc((act(P,Ms)*pow(m,-1,p))%p); pos=np.searchsorted(Es,Ni); assert (Es[pos]==Ni).all(); perms.append(pos)
    while True:
        old=lab.copy()
        for pr in perms: lab=np.minimum(lab,lab[pr])
        lab=lab[lab]
        if np.array_equal(old,lab): break
    u,c=np.unique(lab,return_counts=True); return len(u),sorted(c.tolist())
if p==5:
    types=collections.defaultdict(list)
    for c in itertools.product(range(p),repeat=4):
        t=ftype(c)
        if t is not None and len(types[t])<2: types[t].append(c)
    targets=[];tinfo={}
    for t,l in types.items():
        for c in l:
            kk=((c[3]*p+c[2])*p+c[1])*p+c[0]; targets.append(kk); tinfo[kk]=(t,c)
    res=k4.chunk(((),targets))
    for tk,M in res:
        out=[]
        for name,g in sets.items():
            out.append((name,)+orbits_in(M,g))
        print(tinfo[tk],"fiber",M.shape[0],[(a,b,c[:3]) for a,b,c in out],flush=True)
