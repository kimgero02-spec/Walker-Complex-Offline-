import numpy as np, sys, itertools, random, collections
from ff import Field
A=[[0,1,1],[1,0,1],[1,1,0]]
def setup(q):
    F=Field(q); N=q**6
    idx=np.arange(N)
    m=[((idx//q**k)%q).astype(np.int16) for k in range(6)]
    Mx=[[m[0],m[1],m[2]],[m[1],m[3],m[4]],[m[2],m[4],m[5]]]
    return F,N,Mx
def pmul(F,a,b):
    r=[None]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            t=F.MUL[x,y]
            r[i+j]=t if r[i+j] is None else F.ADD[r[i+j],t]
    return r
def padd(F,a,b):
    n=max(len(a),len(b)); r=[]
    for i in range(n):
        if i<len(a) and i<len(b): r.append(F.ADD[a[i],b[i]])
        else: r.append(a[i] if i<len(a) else b[i])
    return r
def gpoly(F,Mx):
    # det(tA-M) as list of 4 coefficient arrays [t^0..t^3]
    shape=Mx[0][0].shape
    ent=[[ [F.NEG[Mx[i][j]], np.full(shape,A[i][j],np.int16)] for j in range(3)] for i in range(3)]
    tot=None
    for perm in itertools.permutations(range(3)):
        sgn=1
        for i in range(3):
            for j in range(i+1,3):
                if perm[i]>perm[j]: sgn=-sgn
        p=pmul(F,pmul(F,ent[0][perm[0]],ent[1][perm[1]]),ent[2][perm[2]])
        if sgn<0: p=[F.NEG[c] for c in p]
        tot=p if tot is None else padd(F,tot,p)
    return tot
def refl(F,v):
    # P = I - 2 (A v) v^T / Q , Q=v^T A v
    Av=[0]*3
    for i in range(3):
        acc=0
        for k in range(3): acc=F.ADD[acc,F.MUL[A[i][k],v[k]]]
        Av[i]=int(acc)
    Q=0
    for i in range(3): Q=F.ADD[Q,F.MUL[v[i],Av[i]]]
    if Q==0: return None
    c=F.MUL[F.smul(2,1),F.INV[Q]]
    P=[[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            t=F.MUL[c,F.MUL[Av[i],v[j]]]
            P[i][j]=int(F.ADD[1 if i==j else 0, F.NEG[t]])
    return P
def pm(F,X,Y):
    return [[int(sum_(F,[F.MUL[X[i][k],Y[k][j]] for k in range(3)])) for j in range(3)] for i in range(3)]
def sum_(F,l):
    a=0
    for x in l: a=F.ADD[a,x]
    return a
def T(X): return [[X[j][i] for j in range(3)] for i in range(3)]
def det3(F,P):
    t=0
    for perm in itertools.permutations(range(3)):
        s=1
        for i in range(3):
            for j in range(i+1,3):
                if perm[i]>perm[j]: s=-s
        pr=F.MUL[F.MUL[P[0][perm[0]],P[1][perm[1]]],P[2][perm[2]]]
        t=F.ADD[t,pr if s>0 else F.NEG[pr]]
    return int(t)
def isO(F,P): return pm(F,pm(F,P,A),T(P))==A
def action_perm(F,q,Mx,P):
    # M -> P M P^T ; return index permutation
    def mm(X,Y):
        return [[sum_(F,[F.MUL[X[i][k],Y[k][j]] for k in range(3)]) for j in range(3)] for i in range(3)]
    PM=mm(P,Mx)       # P scalars times arrays
    R=mm(PM,T(P))
    new=np.zeros_like(R[0][0],dtype=np.int64)
    for k,(i,j) in enumerate([(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]):
        new+=R[i][j].astype(np.int64)*q**k
    return new
def components(perms,N):
    lab=np.arange(N)
    while True:
        old=lab.copy()
        for pm_ in perms:
            lab=np.minimum(lab,lab[pm_])
        lab=lab[lab]
        if np.array_equal(lab,old): break
    return lab
def gens(F,q,ngen,rng,SO=False):
    out=[]
    while len(out)<ngen:
        v=[rng.randrange(q) for _ in range(3)]
        r1=refl(F,v)
        if r1 is None: continue
        if SO:
            w=[rng.randrange(q) for _ in range(3)]
            r2=refl(F,w)
            if r2 is None: continue
            r1=pm(F,r1,r2)
        assert isO(F,r1)
        out.append(r1)
    return out
def fdisc(F,f2,f1,f0):
    # disc of x^3+f2 x^2+f1 x+f0 : a^2b^2-4b^3-4a^3c-27c^2+18abc
    M=F.MUL
    a,b,c=f2,f1,f0
    def sm(n,x): return F.smul(n,x)
    t1=M[M[a,a],M[b,b]]
    t2=sm(-4,M[b,M[b,b]])
    t3=sm(-4,M[M[a,M[a,a]],c])
    t4=sm(-27,M[c,c])
    t5=sm(18,M[M[a,b],c])
    return int(sum_(F,[t1,t2,t3,t4,t5]))
def nroots(F,f2,f1,f0):
    q=F.q; n=0
    for x in range(q):
        v=F.ADD[F.ADD[F.MUL[F.MUL[x,x],F.ADD[x,f2]],F.MUL[f1,x]],f0]
        if v==0: n+=1
    return n
def run(q,ngen,seed,SO=False,quiet=False):
    F,N,Mx=setup(q); rng=random.Random(seed)
    g=gpoly(F,Mx)
    i2=F.INV[F.smul(2,1)]
    f2=F.MUL[g[2],i2]; f1=F.MUL[g[1],i2]; f0=F.MUL[g[0],i2]
    assert (g[3]==F.smul(2,1)).all()
    key=(f2.astype(np.int64)*q+f1)*q+f0
    gs=gens(F,q,ngen,rng,SO)
    perms=[action_perm(F,q,Mx,P) for P in gs]
    lab=components(perms,N)
    # per key: fiber size, orbit sizes
    res={}
    order=np.lexsort((lab,key))
    ks=key[order]; ls=lab[order]
    # orbit table
    pair=ks*N+ls
    up,cnt=np.unique(pair,return_counts=True)
    ukey=up//N
    d=collections.defaultdict(list)
    for k,c in zip(ukey,cnt): d[int(k)].append(int(c))
    return F,d
if __name__=="__main__":
    q=int(sys.argv[1]); ngen=int(sys.argv[2]); seed=int(sys.argv[3]); SO=len(sys.argv)>4 and sys.argv[4]=="SO"
    F,d=run(q,ngen,seed,SO)
    G=2*q*(q*q-1)
    stat=collections.defaultdict(lambda: collections.Counter())
    bad=[]
    for k,sizes in d.items():
        f0=k%q; f1=(k//q)%q; f2=k//(q*q)
        disc=fdisc(F,f2,f1,f0); r=nroots(F,f2,f1,f0)
        sf = disc!=0
        sig=(("sqfree" if sf else "nonsqfree"),r,tuple(sorted(sizes)))
        stat[sig][0]+=1
        if sf and len(sizes)!=1+r: bad.append((f2,f1,f0,sizes))
    print("q",q,"ngen",ngen,"seed",seed,"SO" if SO else "O","|O(A)|",G)
    for sig in sorted(stat): 
        s=sig[2]
        print(sig[0],"roots",sig[1],"fiber",sum(s),"orbits",len(s),"sizes",s,"stab",[G//x if G%x==0 else ('nodiv',G/x) for x in s],"#f",stat[sig][0])
    print("BAD(sqfree, orbits != 1+roots):",len(bad),bad[:5])
