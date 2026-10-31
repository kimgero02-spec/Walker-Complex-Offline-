from fractions import Fraction as F
import itertools
P=[(F(a),F(b)) for a,b in [("0.0552","0.656"),("0.5108","0.5699"),("0.4131","0.7531"),("0.7979","0.8352"),("-0.0287","0.6686"),("1.1874","0.9514"),("0.9025","-0.2772"),("0.4105","0.6883")]]
L1=[(0,4),(0,6),(0,7),(1,2),(1,3),(1,6),(2,3),(2,4),(2,6),(2,7),(3,4),(3,5),(3,6),(4,5),(4,6),(4,7),(5,6),(6,7)]
L2=[(0,1),(0,2),(0,3),(0,5),(1,4),(1,5),(1,7),(2,5),(3,7),(5,7)]
def o(a,b,c):
    v=(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]); assert v!=0; return v>0
for t in itertools.combinations(range(8),3): o(*[P[i] for i in t])
def x(e,f):
    if set(e)&set(f): return False
    a,b=P[e[0]],P[e[1]]; c,d=P[f[0]],P[f[1]]
    return o(a,b,c)!=o(a,b,d) and o(c,d,a)!=o(c,d,b)
assert sorted(L1+L2)==list(itertools.combinations(range(8),2))
print("internal crossings",[sum(x(e,f) for e,f in itertools.combinations(L,2)) for L in (L1,L2)])
print("X",sum(x(e,f) for e in L1 for f in L2),"(c1,c2)",(max(sum(x(e,f) for f in L2) for e in L1),max(sum(x(e,f) for e in L1) for f in L2)))
