import sys
sys.argv=[sys.argv[0],'5']
src=open('sim.py').read().split("if p==5:")[0]
exec(src)
import sympy
x=sympy.symbols('x')
pols={'x^2(x-1)(x-2)':x**2*(x-1)*(x-2),'x^2(x^2+2)':x**2*(x**2+2),'x^2(x-1)^2':x**2*(x-1)**2,'(x^2+2)^2':(x**2+2)**2,'x^3(x-1)':x**3*(x-1),'x^4':x**4}
targets=[];info={}
for nm,P in pols.items():
    c=sympy.Poly(P,x,modulus=5).all_coeffs()[::-1]; c=[int(v)%5 for v in c]
    kk=((c[3]*p+c[2])*p+c[1])*p+c[0]; targets.append(kk); info[kk]=nm
res=k4.chunk(((),targets))
for tk,M in res:
    print(info[tk],"fiber",M.shape[0],[(nm,)+orbits_in(M,g) for nm,g in sets.items()],flush=True)
