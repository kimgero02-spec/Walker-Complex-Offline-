import sympy as sp
t=sp.symbols('t')
def IJ(f):
    p=sp.Poly(sp.expand(f),t); c=p.all_coeffs()
    c=[0]*(5-len(c))+c; a,b,cc,d,e=c
    I=12*a*e-3*b*d+cc**2; J=72*a*cc*e+9*b*cc*d-27*a*d**2-27*b**2*e-2*cc**3
    return I,J
def jinv(f):
    I,J=IJ(f); return sp.Rational(1728)*4*I**3/(4*I**3-J**2)
for nm,f in [('Q3',(t**2-1)*(9*t**2-1)),('Q3 compl',(4*t**2-1)*(4*t-1)),('P4',(t**2-t-1)*(t**2+t-1))]:
    print(nm,IJ(f),jinv(f), sp.factorint(4*IJ(f)[0]**3-IJ(f)[1]**2))
