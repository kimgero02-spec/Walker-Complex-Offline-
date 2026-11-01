import sympy as sp
exec(open('f.py').read().split("f=-(t+1)")[0])
f1=sp.expand((9*t**2-1)*(25*t**2-1))
f2=sp.expand((10*t-1)*(4*t-1)*(-4*t-1)*(2*t-1))
print(f1,f2)
from c import IJ,jinv
print(IJ(f1),jinv(f1),IJ(f2),jinv(f2))
print(sp.factorint(sp.discriminant(f1,t)),sp.factorint(sp.discriminant(f2,t)))
for p in [7,11,13,17,19,23,29,31,37]:
    a1=p+1-counts(f1,p)[0]; a2=p+1-counts(f2,p)[0]
    print(p,a1,a2)
