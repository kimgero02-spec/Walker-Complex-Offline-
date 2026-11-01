import itertools, sympy as sp
from collections import Counter
from fractions import Fraction
t=sp.symbols('t')
def spec_cay(a,S):
    n=1<<a
    return [sum(1-2*(bin(x&s).count('1')&1) for s in S) for x in range(n)]
def sqfree(spec,n):
    c=Counter(spec); r=sum(m for l,m in c.items() if l!=0)
    odd=[l for l,m in c.items() if l!=0 and m%2==1]
    eps=(-1)**(n-r)
    f=eps
    for l in odd: f*= (l*t-1)
    return sp.expand(f),odd
def IJ(f):
    c=sp.Poly(f,t).all_coeffs(); c=[0]*(5-len(c))+c; a,b,cc,d,e=c
    return 12*a*e-3*b*d+cc**2, 72*a*cc*e+9*b*cc*d-27*a*d**2-27*b**2*e-2*cc**3
def j(f):
    I,J=IJ(f); den=4*I**3-J**2
    return None if den==0 else Fraction(int(1728*4*I**3),int(den))
a=3; n=1<<a; elems=list(range(1,n))
res=[]
for k in range(1,n-1):
    for S in itertools.combinations(elems,k):
        Sc=[x for x in elems if x not in S]
        sp1=spec_cay(a,S); sp2=spec_cay(a,Sc)
        f1,o1=sqfree(sp1,n); f2,o2=sqfree(sp2,n)
        d1=sp.Poly(f1,t).degree(); d2=sp.Poly(f2,t).degree()
        if d1 in (3,4) and d2 in (3,4):
            j1=j(f1); j2=j(f2)
            res.append((S,sorted(Counter(sp1).items()),j1,j2))
seen=set()
for S,s,j1,j2 in res:
    key=(tuple(s),j1,j2)
    if key in seen: continue
    seen.add(key); print(S,s,j1,j2, 'SAME' if j1==j2 else 'DIFF')
