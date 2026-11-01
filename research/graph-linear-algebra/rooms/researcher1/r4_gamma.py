import sympy as sp, itertools, sys
from sympy import symbols, Matrix, Poly, GF
t=symbols('t')

def adj(n,edges,loops=()):
    A=sp.zeros(n,n)
    for a,b in edges: A[a,b]=A[b,a]=1
    for a in loops: A[a,a]=1
    return A
def complete(n): return adj(n,[(i,j) for i in range(n) for j in range(i+1,n)])
def cycle(n): return adj(n,[(i,(i+1)%n) for i in range(n)])
def path(n): return adj(n,[(i,i+1) for i in range(n-1)])
def multipartite(parts):
    idx=[];c=0
    for p in parts: idx.append(list(range(c,c+p))); c+=p
    E=[]
    for i in range(len(parts)):
        for j in range(i+1,len(parts)):
            E+= [(a,b) for a in idx[i] for b in idx[j]]
    return adj(c,E)
def petersen():
    E=[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(5+i,5+(i+2)%5) for i in range(5)]
    return adj(10,E)
def cube():
    E=[(a,a^(1<<k)) for a in range(8) for k in range(3) if a<a^(1<<k)]
    return adj(8,E)
def dsum(A,B):
    return sp.diag(A,B)
G={'K3':complete(3),'K4':complete(4),'K5':complete(5),'C5':cycle(5),'P4':path(4),
   'K222':multipartite([2,2,2]),'Petersen':petersen(),'Q3':cube(),'P5':path(5),
   '2K2':dsum(complete(2),complete(2)),'2K3':dsum(complete(3),complete(3)),'K33':multipartite([3,3]),'K2222':multipartite([2,2,2,2])}

def Pg(A):
    n=A.shape[0]
    return sp.expand((t*A-sp.eye(n)).det())

def legendre(a,q):
    a%=q
    if a==0: return 0
    return 1 if pow(a,(q-1)//2,q)==1 else -1

# arithmetic F_{q^2}
def make_q2(q):
    nu=next(x for x in range(2,q) if legendre(x,q)==-1)
    return nu
def mul2(a,b,q,nu): return ((a[0]*b[0]+nu*a[1]*b[1])%q,(a[0]*b[1]+a[1]*b[0])%q)
def pow2(a,e,q,nu):
    r=(1,0)
    while e:
        if e&1: r=mul2(r,a,q,nu)
        a=mul2(a,a,q,nu); e>>=1
    return r
def chi2(a,q,nu):
    if a==(0,0): return 0
    return 1 if pow2(a,(q*q-1)//2,q,nu)==(1,0) else -1

def counts(coeffs,q,reducible_two_comp=False):
    """coeffs: integer list high->low of P. returns N1,N2 of proper completion"""
    c=[x%q for x in coeffs]
    while c and c[0]==0: c=c[1:]
    d=len(c)-1
    nu=make_q2(q)
    N1=0
    for x in range(q):
        v=0
        for a in c: v=(v*x+a)%q
        N1+=1+legendre(v,q)
    N2=0
    for x0 in range(q):
        for x1 in range(q):
            x=(x0,x1); v=(0,0)
            for a in c:
                v=mul2(v,x,q,nu); v=((v[0]+a)%q,v[1])
            N2+=1+chi2(v,q,nu)
    lead=c[0]
    if d%2==0:
        N1+=1+legendre(lead,q)
        N2+=1+1   # lead in F_q is square in F_{q^2}
    else:
        N1+=1; N2+=1
    return N1,N2,d

def structure(Pexpr,q):
    """factor mod q; return list of (pi, f, m)"""
    p=Poly(Pexpr,t,modulus=q)
    lc,facs=p.factor_list()
    return p,[(Poly(f,t,modulus=q),m) for f,m in facs]

def predict(Pexpr,q):
    """formula-based |Gamma(F_q)| via structure theorem; also returns data"""
    p,facs=structure(Pexpr,q)
    d=p.degree(); c=int(p.LC())%q
    odd=[(f,m) for f,m in facs if m%2==1]
    s=sum(f.degree() for f,m in odd)
    # S0 = c * prod pi (odd)
    # N_loc
    Nloc=1; trank=0; urank=0
    for f,m in facs:
        fd=f.degree()
        if m==1: continue
        R=Poly(p.as_expr(),t,modulus=q).quo(f**m)  # P/pi^m
        k=m//2
        if m%2==0:
            res=sp.resultant(f.as_expr(),R.as_expr(),t,modulus=q) if R.degree()>0 else int(R.LC())**f.degree()
            res=int(res)%q
            chi=legendre(res,q)
            Nloc*= (q**fd-chi)*q**(fd*(k-1)); trank+=fd; urank+=fd*(k-1)
        else:
            Nloc*= q**(fd*k); urank+=fd*k
    sp_=s  # number of odd-multiplicity roots (affine) counted with degree
    return dict(d=d,s=s,Nloc=Nloc,trank=trank,urank=urank,facs=[(str(f.as_expr()),m) for f,m in facs],c=c)

def jac_order(Pexpr,q):
    """order of J(C~) for C~: w^2=S0(t) (g~<=1 only)"""
    p,facs=structure(Pexpr,q)
    c=int(p.LC())%q
    S0=Poly(c,t,modulus=q)
    for f,m in facs:
        if m%2==1: S0=S0*f
    coeffs=[int(x) for x in S0.all_coeffs()]
    s=S0.degree()
    gt=(s+1)//2-1
    if gt<=0: return 1,gt
    if gt==1:
        N1,N2,d=counts(coeffs,q)
        return N1,gt
    N1,N2,d=counts(coeffs,q)
    return (N1*N1+N2)//2-q,gt

if __name__=="__main__":
    qs=[5,7,11,13,17,19,23]
    for name,A in G.items():
        P=Pg(A); 
        print("==",name,"P =",sp.factor(P))
        for q in qs:
            if q==2: continue
            pr=predict(P,q)
            J,gt=jac_order(P,q)
            reducible=(pr['s']==0)
            if reducible:
                # c square required
                assert legendre(pr['c'],q)==1
                pred=pr['Nloc']//(q-1)
            else:
                pred=J*pr['Nloc']
            # independent Lefschetz-type check
            p=Poly(P,t,modulus=q)
            coeffs=[int(x) for x in p.all_coeffs()]
            N1,N2,d=counts(coeffs,q)
            hdim=2*gt+pr['trank'] if not reducible else pr['trank']-1
            # a1,a2
            comps=2 if reducible else 1
            S1=comps*q+1-N1 if False else None
            e1=(1+comps*q) - N1   # sum alpha
            p2=(1+comps*q*q) - N2 # sum alpha^2
            note=""
            if hdim<=2 and reducible:
                trk=pr['trank']-1
                # H^1 of dimension trk (all weight 0)
                if trk==1: lef=q-e1; note="e1=%d"%e1
                else: lef=None
            elif hdim==0:
                lef=1; note="N1=%d (expect %d)"%(N1,(1+q if d%2==0 and False else N1))
            elif hdim==1:
                lef=q-e1
            elif hdim==2:
                e2=(e1*e1-p2)//2
                # char poly x^2 - e1 x + e2 ; evaluate prod(q-alpha)=q^2-e1 q+e2 if weight0, prod(1-alpha)=1-e1+e2 if weight1
                if pr['trank']==2: lef=q*q-e1*q+e2
                elif gt==1: lef=1-e1+e2
            else: lef=None
            u=pr['urank']
            lefpred=None if lef is None else lef*q**u
            print("  q=%2d |Γ|=%d  (J=%d, Nloc=%d, t=%d, u=%d, g~=%d)  independent=%s %s"%(q,pred,J,pr['Nloc'],pr['trank'],u,gt,lefpred,"OK" if lefpred in (None,pred) else "MISMATCH"))
