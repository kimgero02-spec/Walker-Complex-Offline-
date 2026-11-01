import sympy as sp
exec(open('f.py').read().split("f=-(t+1)")[0].split("import sympy as sp")[1])
f=(t**2-t-1)*(t**2+t-1)
print('P4 a_p',[(p,p+1-counts(f,p)[0]) for p in [7,11,19,23,31]])
print('P4 & -f a_p',[(p,p+1-counts(-f,p)[0]) for p in [7,11,19,23,31]])
from g import *
print('K1+P4',Pg(dsum(K(1),P(4))))
# product examples
print('K2boxP4', sp.factor(Pg(cart(K(2),P(4)))))
print('K13boxP4', sp.factor(Pg(cart(star(3),P(4)))))
