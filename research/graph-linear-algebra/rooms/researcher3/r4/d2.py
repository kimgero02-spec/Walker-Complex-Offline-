import itertools
from collections import Counter
from fractions import Fraction
def spec_cay(a,S):
    return [sum(1-2*(bin(x&s).count('1')&1) for s in S) for x in range(1<<a)]
def pmul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): r[i+j]+=x*y
    return r
def sqf(sp_,n):
    c=Counter(sp_); r=sum(m for l,m in c.items() if l!=0)
    odd=[l for l,m in c.items() if l!=0 and m%2==1]
    p=[(-1)**(n-r)]
    for l in odd: p=pmul(p,[-1,l])   # coeffs ascending: (l t -1)
    return p,odd
def IJ(p):
    p=p+[0]*(5-len(p)); e,d,cc,b,a=p[:5]
    return 12*a*e-3*b*d+cc**2, 72*a*cc*e+9*b*cc*d-27*a*d**2-27*b**2*e-2*cc**3
def j(p):
    I,J=IJ(p); den=4*I**3-J**2
    return None if den==0 else Fraction(1728*4*I**3,den)
import sys
a=int(sys.argv[1]); n=1<<a; elems=list(range(1,n))
seen={}
for k in range(2,n-2):
    for S in itertools.combinations(elems,k):
        if S[0]!=1 and False: pass
        Sc=[x for x in elems if x not in S]
        s1=spec_cay(a,S); s2=spec_cay(a,Sc)
        p1,o1=sqf(s1,n); p2,o2=sqf(s2,n)
        if len(p1)-1 in (3,4) and len(p2)-1 in (3,4):
            j1,j2=j(p1),j(p2)
            if j1 is None or j2 is None: continue
            key=(tuple(sorted(Counter(s1).items())),j1,j2)
            if key not in seen: seen[key]=S
for k,S in seen.items(): print(S,k[0],k[1],k[2],'SAME' if k[1]==k[2] else 'DIFF')
