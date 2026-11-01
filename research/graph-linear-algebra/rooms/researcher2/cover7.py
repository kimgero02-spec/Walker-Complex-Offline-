import sys,random,collections,itertools,numpy as np
nsamp=int(sys.argv[1])
sys.argv=[sys.argv[0],'7']
exec(open('sim7.py').read().split("def orbit(M0,gens):")[0].replace("nsamp=int(sys.argv[1])","nsamp=%d"%nsamp).replace("exec(open('sim.py').read().split(\"if p==5:\")[0].replace(\"p=int(sys.argv[1]); nsamp=int(sys.argv[2]) if len(sys.argv)>2 else 0\",\"p=7\"))","exec(open('sim.py').read().split(\"if p==5:\")[0].replace(\"p=int(sys.argv[1]); nsamp=int(sys.argv[2]) if len(sys.argv)>2 else 0\",\"p=7\"))"))
import sympy
xs=sympy.symbols('x')
def orbit(M0,gens):
    allv=enc(M0[None,:]); fr=M0[None,:]
    while len(fr):
        news=[act(P,fr)*pow(m,-1,p)%p for P,m in gens]
        Rr=np.vstack(news); e=enc(Rr)
        e,ui=np.unique(e,return_index=True); Rr=Rr[ui]
        msk=~np.isin(e,allv); fr=Rr[msk]; allv=np.union1d(allv,e[msk])
    return allv
def dec(e):
    return np.array([(e//p**k)%p for k in range(10)],dtype=np.int64)
# hyperbolic basis for A4 over F_p
vecs=[np.array(v,dtype=np.int64) for v in itertools.product(range(p),repeat=4)]
Q=lambda v:int(v@A4@v)%p
B=lambda v,w:int(v@A4@w)%p
iso=[v for v in vecs if Q(v)==0 and v.any()]
a=iso[0]
d=[v for v in iso if B(a,v)!=0][0]
d=(d*pow(B(a,d),-1,p))%p   # B(a,d)=1 -> then Q(alpha a+delta d)=2 alpha delta
# complement
comp=[v for v in vecs if B(a,v)==0 and B(d,v)==0]
iso2=[v for v in comp if Q(v)==0 and v.any()]
b=iso2[0]; c=[v for v in iso2 if B(b,v)!=0][0]; c=(c*pow(B(b,c),-1,p))%p
# Q = 2 alpha delta + 2 beta gamma ; want alpha*delta - beta*gamma form: replace c by -c
c=(-c)%p
for u in (a,b,c,d): pass
assert Q(a)==Q(b)==Q(c)==Q(d)==0
def quart(M,rul):
    S=np.zeros((4,4),dtype=np.int64)
    for k,(i,j) in enumerate(pairs): S[i,j]=M[k]; S[j,i]=M[k]
    # X,Y linear in s: coefficient vectors (const in s0, s1)
    if rul==1: X=(a,c); Y=(b,d)   # X=s0*a+s1*c ; Y=s0*b+s1*d
    else: X=(a,b); Y=(c,d)
    def bil(U,V):  # U,V pairs (v0,v1) -> quadratic poly in (s0,s1): coefficients [s0^2,s0s1,s1^2]
        return np.array([U[0]@S@V[0], U[0]@S@V[1]+U[1]@S@V[0], U[1]@S@V[1]])%p
    XX=bil(X,X);XY=bil(X,Y);YY=bil(Y,Y)
    F=(np.convolve(XY,XY)-np.convolve(XX,YY))%p   # coefficients s0^4, s0^3 s1, ..., s1^4
    return F
def ftype_form(F):
    # binary quartic coefficients in s0^4..s1^4 ; factor type including root at infinity (s0=0 <-> deg drop)
    cs=[int(x) for x in F]
    # polynomial in t=s1/s0 : sum cs[k] t^k
    P=sympy.Poly(sum(cs[k]*xs**k for k in range(5)),xs,modulus=p)
    if P.is_zero: return 'zero'
    fl=P.factor_list()[1]
    degs=[]
    for f,m in fl: degs+=[f.degree()]*m
    inf=4-P.degree()
    degs+=[1]*inf
    return tuple(sorted(degs))
rng2=random.Random(9)
for tk,(t,cc) in tinfo.items():
    H=np.vstack(hits[tk])
    for name in ('SO',):
        g=sets[name]; seen=np.array([],dtype=np.int64); k=0
        for i in range(len(H)):
            e=enc(H[i][None,:])[0]
            if e in seen: continue
            o=orbit(H[i],g); seen=np.union1d(seen,o); k+=1
            smp=rng2.sample(list(o),min(40,len(o)))
            c1=collections.Counter(ftype_form(quart(dec(int(x)),1)) for x in smp)
            c2=collections.Counter(ftype_form(quart(dec(int(x)),2)) for x in smp)
            print(t,"SOorbit",k,"size",len(o),"F1:",dict(c1),"F2:",dict(c2),flush=True)
            if len(seen)>=112896: break
