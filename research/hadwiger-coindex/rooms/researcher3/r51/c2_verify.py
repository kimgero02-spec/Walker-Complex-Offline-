from fractions import Fraction as F
import itertools
P=[(0.0552, 0.656), (0.5108, 0.5699), (0.4131, 0.7531), (0.7979, 0.8352), (-0.0287, 0.6686), (1.1874, 0.9514), (0.9025, -0.2772), (0.4105, 0.6883)]
P=[(F(str(x)),F(str(y))) for x,y in P]
L1=[(0, 4), (0, 6), (0, 7), (1, 2), (1, 3), (1, 6), (2, 3), (2, 4), (2, 6), (2, 7), (3, 4), (3, 5), (3, 6), (4, 5), (4, 6), (4, 7), (5, 6), (6, 7)]
L2=[(0, 1), (0, 2), (0, 3), (0, 5), (1, 4), (1, 5), (1, 7), (2, 5), (3, 7), (5, 7)]
def o(p,q,r): return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
assert all(o(P[a],P[b],P[c])!=0 for a,b,c in itertools.combinations(range(8),3))
def x(e,f):
    a,b=e;c,d=f
    if len({a,b,c,d})<4: return False
    return o(P[a],P[b],P[c])*o(P[a],P[b],P[d])<0 and o(P[c],P[d],P[a])*o(P[c],P[d],P[b])<0
assert sorted(L1+L2)==list(itertools.combinations(range(8),2))
for L in (L1,L2): assert not any(x(e,f) for e,f in itertools.combinations(L,2))
X=sum(x(e,f) for e in L1 for f in L2)
deg1=[max(sum(x(e,f) for f in L2) for e in L1), max(sum(x(e,f) for e in L1) for f in L2)]
print("exact OK: K8 = two plane straight layers, X =",X,"crossing degrees (c1,c2) =",deg1)
