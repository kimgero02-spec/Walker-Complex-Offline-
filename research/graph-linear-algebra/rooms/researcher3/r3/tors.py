import itertools, sys
from fractions import Fraction
from collections import Counter, defaultdict
import sympy as sp
def gco(M):
    m11,m12,m13,m22,m23,m33=M
    g2=(m11-2*m12-2*m13+m22-2*m23+m33)
    g1=(-2*m11*m23+2*m12*m13+2*m12*m23-2*m12*m33-2*m13*m22+2*m13*m23)
    g0=(-m11*m22*m33+m11*m23**2+m12**2*m33-2*m12*m13*m23+m13**2*m22)
    return g2,g1,g0
def curve(M):
    g2,g1,g0=gco(M)
    return (g2,2*g1,4*g0)   # Y^2=X^3+aX^2+bX+c
def disc3(a,b,c): return -4*a**3*c+a*a*b*b+18*a*b*c-4*b**3-27*c*c
# group law
def add(P,Q,a,b,c):
    if P is None: return Q
    if Q is None: return P
    x1,y1=P;x2,y2=Q
    if x1==x2 and y1==-y2: return None
    if P==Q:
        lam=(3*x1*x1+2*a*x1+b)/(2*y1)
    else:
        lam=(y2-y1)/(x2-x1)
    x3=lam*lam-a-x1-x2
    y3=-(y1+lam*(x3-x1))
    return (x3,y3)
def torsion(a,b,c):
    D=disc3(a,b,c)
    pts=[None]
    # candidates Y=0 or Y^2 | D (Nagell-Lutz for monic integer model; use Y^2 | D)
    fac=sp.factorint(abs(D))
    ds=[1]
    for pr,e in fac.items():
        ds=[d*pr**k for d in ds for k in range(e//2+1)]
    cand=set()
    # Y=0
    for r in sp.Poly([1,a,b,c],sp.Symbol('x')).ground_roots() if False else []: pass
    x=sp.Symbol('x')
    for Y in [0]+ds:
        if Y==0:
            poly=sp.Poly(x**3+a*x**2+b*x+c,x)
        else: poly=sp.Poly(x**3+a*x**2+b*x+c-Y*Y,x)
        for r,m in sp.roots(poly,filter='Z').items() if True else []:
            if r.is_integer:
                cand.add((int(r),Y)); cand.add((int(r),-Y))
    cand=[(Fraction(X),Fraction(Y)) for X,Y in cand]
    # find torsion by order test: multiply up to 12 (Mazur)
    tors=[None]
    for P in cand:
        Q=P; ok=False
        for n in range(1,17):
            if Q is None: ok=True;break
            Q=add(Q,P,a,b,c) if n>=1 else Q
        # recompute properly
    res=[None]
    for P in cand:
        Q=P; order=None
        for n in range(1,20):
            if Q is None: order=n-1;break
            if n>=19: break
            Q=add(Q,P,a,b,c)
        # careful: compute order by repeated addition
    return cand
def order(P,a,b,c,maxn=16):
    Q=P
    for n in range(1,maxn+1):
        if Q is None: return n-1 if n>1 else 1
        Q=add(Q,P,a,b,c) if True else None
    return None
def tors_group(a,b,c):
    cand=torsion(a,b,c)
    pts=[]
    for P in cand:
        # order via multiples
        Q=P;n=1
        while Q is not None and n<=16:
            Q=add(Q,P,a,b,c); n+=1
        if Q is None: pts.append((P,n))
    # exclude non-torsion; (P of order n: nP = O: loop ended with Q None after adding n-1 times => order n)
    orders=Counter(n for P,n in pts)
    size=1+len(pts)
    o2=sum(1 for P,n in pts if n==2)
    maxo=max([n for P,n in pts],default=1)
    return size,o2,maxo,orders
def structure(size,o2,maxo):
    if o2==3: return f"Z2xZ{size//2}"
    return f"Z{size}"
if __name__=="__main__":
    R=int(sys.argv[1])
    seen={}
    stat=Counter(); bad=0; ex={}
    for M in itertools.product(range(-R,R+1),repeat=6):
        a,b,c=curve(M)
        D=disc3(a,b,c)
        if D==0: continue
        key=(a,b,c)
        if key in seen: continue
        # rational roots of f: roots X=2nu of monic integer cubic
        x=sp.Symbol('x')
        rts=sp.roots(sp.Poly(x**3+a*x**2+b*x+c,x),filter='Q')
        nr=len([r for r in rts])
        size,o2,maxo,orders=tors_group(a,b,c)
        n2=o2
        assert (nr==0 and n2==0) or (nr==1 and n2==1) or (nr==3 and n2==3),(M,nr,n2)
        seen[key]=M
        stat[(nr,structure(size,o2,maxo))]+=1
        ex.setdefault((nr,structure(size,o2,maxo)),[]).append(M)
    print(len(seen))
    for k,v in sorted(stat.items()): print(k,v,ex[k][:2])
