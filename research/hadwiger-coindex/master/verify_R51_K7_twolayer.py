from fractions import Fraction as F
import itertools
P=[(F(s[0]),F(s[1])) for s in [("0.296","0.251"),("0.805","0.736"),("0.483","0.921"),("0.154","0.096"),("0.552","0.576"),("0.889","0.774"),("0.43","0.572")]]
L2={(0,1),(1,3),(0,2),(0,6),(1,6),(5,6)}
E=list(itertools.combinations(range(7),2)); L1=[e for e in E if e not in L2]
def o(a,b,c): v=(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]); assert v!=0; return v>0
def cross(e,f):
    if set(e)&set(f): return False
    a,b=P[e[0]],P[e[1]]; c,d=P[f[0]],P[f[1]]
    return o(a,b,c)!=o(a,b,d) and o(c,d,a)!=o(c,d,b)
print("L1 internal crossings",sum(cross(e,f) for e,f in itertools.combinations(L1,2)))
print("L2 internal crossings",sum(cross(e,f) for e,f in itertools.combinations(L2,2)))
c1=max(sum(cross(e,f) for f in L2) for e in L1); c2=max(sum(cross(f,e) for e in L1) for f in L2)
print("|L1|,|L2|",len(L1),len(L2),"(c1,c2)",(c1,c2),"total cross",sum(cross(e,f) for e in L1 for f in L2))
