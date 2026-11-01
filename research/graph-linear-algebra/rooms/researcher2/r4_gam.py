import sympy as sp
from sympy import symbols, Poly, GF
from r4lib import *
import itertools
def sqfdec_mod(P,p):
    """P poly in Z[t] -> over F_p: (c, [(irreducible pi, mult)])"""
    c,fl=sp.factor_list(P.as_expr(),t,modulus=p)
    return c,fl
def is_square_in(val_poly,pi,p):
    # element val (poly mod pi) square in F_p[t]/pi ? via Euler: val^((p^f-1)/2)==1
    f=Poly(pi,t,modulus=p).degree()
    q=p**f
    r=Poly(1,t,modulus=p)
    base=Poly(val_poly,t,modulus=p).rem(Poly(pi,t,modulus=p))
    if base.is_zero: return 0
    e=(q-1)//2
    res=Poly(1,t,modulus=p); b=base
    pim=Poly(pi,t,modulus=p)
    while e:
        if e&1: res=(res*b).rem(pim)
        b=(b*b).rem(pim); e>>=1
    return 1 if res==Poly(1,t,modulus=p) else -1
def J_order(S,c,p):
    """|Jac(w^2=c*S)(F_p)| for squarefree S (deg d) genus g=(d-1)//2 <=2; brute force"""
    d=S.degree()
    if d<=2: return 1
    g=(d-1)//2
    f=Poly(c*S.as_expr(),t,modulus=p)
    def count_ext(k):
        # points over F_{p^k}: implement F_{p^k} via galois-free approach: only k=1,2 ; k=2 via sympy GF? use manual field
        pass
    # k=1
    def N1():
        N=0
        for x in range(p):
            v=int(f.eval(x))%p
            N+=1 if v==0 else (2 if pow(v,(p-1)//2,p)==1 else 0)
        lead=int(f.LC())%p
        N+= 1 if d%2==1 else (2 if pow(lead,(p-1)//2,p)==1 else 0)
        return N
    n1=N1()
    if g==1: return n1
    # genus 2: need N2 over F_{p^2}: represent F_{p^2}=F_p[i]/(i^2-r) r nonresidue
    r=next(a for a in range(2,p) if pow(a,(p-1)//2,p)==p-1)
    coeffs=[int(x)%p for x in f.all_coeffs()]
    def mul(a,b): return ((a[0]*b[0]+r*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
    def pw(a,e):
        res=(1,0)
        while e:
            if e&1:res=mul(res,a)
            a=mul(a,a);e>>=1
        return res
    N2=0
    q2=p*p
    for x0 in range(p):
        for x1 in range(p):
            x=(x0,x1); v=(0,0)
            for cf in coeffs:
                v=mul(v,x); v=((v[0]+cf)%p,v[1])
            if v==(0,0):N2+=1
            else: N2+= 2 if pw(v,(q2-1)//2)==(1,0) else 0
    lead=(coeffs[0],0)
    N2+= 1 if d%2==1 else (2 if pw(lead,(q2-1)//2)==(1,0) else 0)
    return (n1*n1+N2)//2-p
def gam_order(P,p):
    """|Gamma(F_p)| for P=det(tA-I), assuming S0 nonconstant, p odd good prime."""
    c,fl=sp.factor_list(P.as_expr(),t,modulus=p)
    S0=sp.Integer(1); Lord=1
    items=[]
    for f,m in fl:
        if m%2: S0*=f
    S0P=Poly(S0,t,modulus=p)
    cc=int(c)%p
    if S0P.degree()==0: return None
    J=J_order(Poly(S0,t,modulus=p).set_domain(sp.ZZ),cc,p)
    for f,m in fl:
        mm=m//2
        if mm==0: continue
        fd=Poly(f,t,modulus=p).degree(); q=p**fd
        # residue of S0*c at root of f
        if Poly(f,t,modulus=p).rem(Poly(f,t,modulus=p)).is_zero and Poly(S0,t,modulus=p).rem(Poly(f,t,modulus=p)).is_zero:
            Lord*= q**mm
        else:
            val=sp.expand(cc*S0)
            s=is_square_in(val,f,p)
            Lord*= q**(mm-1)*(q-1 if s==1 else q+1)
    return J,Lord,J*Lord
if __name__=='__main__':
    # graphs
    def cyc(n):
        A=[[0]*n for _ in range(n)]
        for i in range(n): A[i][(i+1)%n]=A[(i+1)%n][i]=1
        return A
    def K(n): return [[0 if i==j else 1 for j in range(n)] for i in range(n)]
    def cube():
        A=[[0]*8 for _ in range(8)]
        for a in range(8):
            for b in range(3): A[a][a^(1<<b)]=1
        return A
    Ps={'K3':PG(K(3)),'C6':PG(cyc(6)),'C9':PG(cyc(9)),'K4':PG(K(4)),'Q3':PG(cube())}
    for nm,P in Ps.items(): print(nm,sp.factor(P.as_expr()),'p_a=',(P.degree()-1)//2)
    for p in [5,7,11,13,17]:
        print('p=',p,{nm:gam_order(P,p) for nm,P in Ps.items()})
