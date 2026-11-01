"""researcher3 R2: K3-matrix / 2-descent tools. Exact integer/Fraction arithmetic."""
from fractions import Fraction
from math import gcd, isqrt
import itertools, sympy as sp
A=[[0,1,1],[1,0,1],[1,1,0]]

def qA(v): return 2*(v[0]*v[1]+v[1]*v[2]+v[0]*v[2])
def matvec(M,v): return [sum(M[i][j]*v[j] for j in range(3)) for i in range(3)]
def quartic(M):
    m11,m12,m13,m22,m23,m33=M[0][0],M[0][1],M[0][2],M[1][1],M[1][2],M[2][2]
    return [m11, 2*m11-2*m12+2*m13, m11+m22+m33-2*m12+4*m13-2*m23, 2*m13-2*m23+2*m33, m33]
def evalq(c,a,b): return sum(c[i]*a**(4-i)*b**i for i in range(5))
def gpoly(M):
    """coefficients [2, g2, g1, g0] of det(tA-M)"""
    m11,m12,m13,m22,m23,m33=M[0][0],M[0][1],M[0][2],M[1][1],M[1][2],M[2][2]
    return [2, m11-2*m12-2*m13+m22-2*m23+m33,
            -2*m11*m23+2*m12*m13+2*m12*m23-2*m12*m33-2*m13*m22+2*m13*m23,
            -m11*m22*m33+m11*m23**2+m12**2*m33-2*m12*m13*m23+m13**2*m22]
def M0(a1,a2,a3): return [[0,1,0],[1,2*(a1+a2+a3+1),a2+2*a3],[0,a2+2*a3,2*a3]]

# ---------- p-adic square classes ----------
def val(n,p):
    if n==0: return 10**9
    v=0
    while n%p==0: n//=p; v+=1
    return v
def ratval(x,p): x=Fraction(x); return val(x.numerator,p)-val(x.denominator,p)
def unit_part(x,p):
    x=Fraction(x); v=ratval(x,p)
    n,d=x.numerator,x.denominator
    n//=p**max(val(n,p),0); d//=p**val(d,p)
    return n,d
def legendre(a,p): 
    a%=p
    return 0 if a==0 else (1 if pow(a,(p-1)//2,p)==1 else -1)
def sqclass(x,p):
    """class of x in Q_p^x / squares as tuple of bits. p=0 means real."""
    x=Fraction(x)
    if x==0: raise ValueError
    if p==0: return (1 if x<0 else 0,)
    v=ratval(x,p); n,d=unit_part(x,p)
    if p==2:
        u=(n*d)%8   # n/d ~ n*d mod squares (d odd unit)
        a,b={1:(0,0),5:(0,1),7:(1,0),3:(1,1)}[u]
        return (v%2,a,b)
    u=(n*d)%p
    return (v%2,0 if legendre(u,p)==1 else 1)
def addv(x,y): return tuple((i+j)%2 for i,j in zip(x,y))
def is_sq_p(x,p): return sum(sqclass(x,p))==0
def squarefree(n):
    n=int(n); s=-1 if n<0 else 1; n=abs(n)
    f=sp.factorint(n); r=1
    for q,e in f.items():
        if e%2: r*=q
    return s*r
def sqf_frac(x):
    x=Fraction(x); return squarefree(x.numerator*x.denominator)

# ---------- Hilbert symbol ----------
def hilbert(a,b,p):
    a=Fraction(a); b=Fraction(b)
    if p==0: return -1 if (a<0 and b<0) else 1
    va,vb=ratval(a,p),ratval(b,p)
    ua=Fraction(*unit_part(a,p)); ub=Fraction(*unit_part(b,p))
    ua=(ua.numerator*ua.denominator); ub=(ub.numerator*ub.denominator)
    if p==2:
        eps=lambda u:((u-1)//2)%2; om=lambda u:((u*u-1)//8)%2
        e=(eps(ua)*eps(ub)+va*om(ub)+vb*om(ua))%2
        return -1 if e else 1
    s=1
    if (va*vb)%2 and (p%4==3): s=-s
    if vb%2: s*=legendre(ua,p)
    if va%2: s*=legendre(ub,p)
    # formula: (a,b)=(-1)^{va vb eps(p)} (ua/p)^vb (ub/p)^va
    s=1
    if (va*vb)%2 and (p%4==3): s=-1
    if vb%2: s*=legendre(ua,p)
    if va%2: s*=legendre(ub,p)
    return s
def isotropic_diag(l,p):
    """ternary form <l0,l1,l2> isotropic over Q_p (p=0 real)?"""
    a,b,c=[Fraction(x) for x in l]
    return hilbert(-a*c,-b*c,p)==1

# ---------- local solvability of u^2 = F(a,b) ----------
def solv_quartic(c,p,maxdepth=14):
    """True/False/None. p=0: real."""
    if p==0:
        if c[0]>0 or c[4]>0: return True
        # negative-or-zero leading: check real roots / sign
        x=sp.symbols('x'); P=sp.Poly(sum(c[i]*x**(4-i) for i in range(5)),x)
        if P.is_zero: return True
        if len(sp.real_roots(P))>0: return True
        return P.eval(0)>=0 if c[0]==0 else False
    unk=[False]
    def status(a,b,k):
        V=evalq(c,a,b)
        if V==0: return True
        v=val(V,p)
        need=3 if p==2 else 1
        if k-v<need: return None
        w=V//p**v
        if v%2: return False
        if p==2: return w%8==1
        return legendre(w,p)==1
    def dfs(a,b,k):
        s=status(a,b,k)
        if s is True: return True
        if s is False: return False
        if k>=maxdepth: unk[0]=True; return False
        pk=p**k
        for x in range(p):
            for y in range(p):
                if dfs(a+pk*x,b+pk*y,k+1): return True
        return False
    k0=1
    pts=[(1,y) for y in range(p)]+[(x,1) for x in range(0,1)]  # (1:y) y mod p, and (0:1)... use (x:1) with x≡0
    pts=[(1,y) for y in range(p)]+[(0,1)]
    for (a,b) in pts:
        if dfs(a,b,1): return True
    return None if unk[0] else False
