from g import *
exec(open('f.py').read().split("f=-(t+1)")[0].split("import sympy as sp")[1])
D4=Mx([(0,1),(0,2),(1,2),(1,3),(2,3)],4)  # diamond K4-e
print(Pg(D4), Pg(tens(D4,K(2))))
fD=sp.expand(Pg(tens(D4,K(2))))
print(sp.Poly(fD,t).degree(), sp.factorint(sp.discriminant(fD,t)))
fG=Pg(D4)
for p in [7,11,13,19,23]:
    a=p+1-counts(fG,p)[0]
    N1,N2,c1,c2=lpoly(fD,p)
    prod=sp.expand((x**2-a*x+p)**2)
    h=x**4+c1*x**3+c2*x**2+p*c1*x+p**2
    print(p,'a',a,'J(G x K2) charpoly',h,' vs (E_G)^2',prod, 'equal' if sp.expand(h-prod)==0 else 'DIFF', 'factors',len(sp.factor_list(h)[1]))
print('----')
for p in [7,11,13,19,23,29,31]:
    a=p+1-counts(fG,p)[0]
    N1,N2,c1,c2=lpoly(fD,p)
    h=x**4+c1*x**3+c2*x**2+p*c1*x+p**2
    q=x**2-a*x+p
    print(p,a,sp.factor(h), 'E_G divides' , sp.rem(sp.Poly(h,x),sp.Poly(q,x)).is_zero)
