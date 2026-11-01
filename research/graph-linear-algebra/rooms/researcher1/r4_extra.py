import sympy as sp, itertools
from r4_gamma import *
# Kneser(6,2)
V=list(itertools.combinations(range(6),2))
E=[(i,j) for i in range(15) for j in range(i+1,15) if not set(V[i])&set(V[j])]
Kn=adj(15,E)
P=Pg(Kn); print("Kneser(6,2)",sp.factor(P))
for q in [5,7,11,13]:
    pr=predict(P,q); J,gt=jac_order(P,q)
    p=Poly(P,t,modulus=q); N1,N2,d=counts([int(x) for x in p.all_coeffs()],q)
    e1=1+q-N1; p2=1+q*q-N2; e2=(e1*e1-p2)//2
    ind=(1-e1+e2)*q**pr['urank']
    print(q,"pred",J*pr['Nloc'],"indep",ind,"t,u,g~",pr['trank'],pr['urank'],gt, "J=",J)
# K_n general formula
for n in range(3,9):
    P=Pg(complete(n))
    for q in [5,7,11,13,17]:
        if n==q: continue
        pr=predict(P,q)
        if n%2==1: f=q**((n-3)//2)*(q-legendre(-n,q))
        else: f=q**((n-2)//2)
        assert pr['Nloc']==f,(n,q,pr,f)
print("K_n formula OK n=3..8")
# P4 Weierstrass cross-check: Y^2=X^3-27 I X -27 J, I=21,J=-162
for q in [7,11,13,17,19,23,29,31]:
    cnt=1+sum(1+legendre(x**3-27*21*x-27*(-162),q) for x in range(q))
    P=Pg(path(4)); p=Poly(P,t,modulus=q); N1,N2,d=counts([int(x) for x in p.all_coeffs()],q)
    print(q,cnt,N1)
