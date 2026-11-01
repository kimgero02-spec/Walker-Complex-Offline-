from orb import *
from math import comb, factorial
def rook(n,m,q): return sum(comb(n,k)*comb(m,k)*factorial(k)*(q-1)**k for k in range(min(n,m)+1))
posets3={
 "antichain":[], "chain 0>1>2":[(0,1),(1,2)], "V (0>1,0>2)":[(0,1),(0,2)],
 "Lambda (0>2,1>2)":[(0,2),(1,2)], "one arc 0>1 +iso":[(0,1)], "arcs 0>1 ,2 iso" :[(0,1)],
}
for q in (2,3):
  print("q=",q)
  for name,arcs in posets3.items():
    R=closure_rel(3,arcs); g=gens_from_rel(3,R,q)
    r=[orbits(3,m,q,g) for m in (1,2)]
    print("  left only",name,"m=1,2:",r)
  # two-sided 3x3 q=2, m=3
for q in (2,):
  ch=closure_rel(3,[(0,1),(1,2)])
  V=closure_rel(3,[(0,1),(0,2)])
  for nm,(P,Q) in {"chain,chain":(ch,ch),"chain,V":(ch,V),"V,V":(V,V),"chain,antichain":(ch,set()),"V,antichain":(V,set()),"anti,anti":(set(),set())}.items():
    print(q,nm,orbits(3,3,q,gens_from_rel(3,P,q),gens_from_rel(3,Q,q)),"rook=",rook(3,3,q))
for (n,m) in [(2,2),(2,3),(3,2)]:
  for q in (2,3):
    cn=closure_rel(n,[(i,i+1) for i in range(n-1)]);cm=closure_rel(m,[(i,i+1) for i in range(m-1)])
    print(n,m,q,orbits(n,m,q,gens_from_rel(n,cn,q),gens_from_rel(m,cm,q)),rook(n,m,q))
# opposite orientation both sides
n=m=3;q=3
ch=closure_rel(3,[(0,1),(1,2)]);rv=closure_rel(3,[(1,0),(2,1)])
print("chain,reverse chain q=3:",orbits(3,3,3,gens_from_rel(3,ch,3),gens_from_rel(3,rv,3)),rook(3,3,3))
# edgeless with torus: orbits of T x T on 2x2, 2x3 : sum (q-1)^{beta1}
def torus_gens(n,p):
    out=[]
    for i in range(n):
        for c in range(2,p):
            M=[[1 if a==b else 0 for b in range(n)] for a in range(n)];M[i][i]=c;out.append(tuple(map(tuple,M)))
    return out
for (n,m,q) in [(2,2,3),(2,2,5),(2,3,3)]:
    print("torus orbits",n,m,q,orbits(n,m,q,torus_gens(n,q),torus_gens(m,q)))
