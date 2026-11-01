from g import *
s=sp.symbols('s')
A=P(4)
d1=(t*(A+s*sp.eye(4))-sp.eye(4)).det()
d2=(t*(A-s*sp.eye(4))-sp.eye(4)).det()
R=sp.expand(sp.rem(sp.expand(d1*d2),s**2-3,s))
print(sp.factor(R), sp.Poly(R,t).degree())
print(sp.factor(Pg(A)**2*R))
