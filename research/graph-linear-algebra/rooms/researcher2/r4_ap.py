from sympy import symbols, Poly, GF, factor_list, primerange, legendre_symbol
import sympy as sp
t=symbols('t')
def cnt(f,p):  # #{(t,y): y^2=f(t)} affine + points at infinity for quartic/cubic
    c=Poly(f,t); d=c.degree()
    N=0
    for x in range(p):
        v=int(c.eval(x))%p
        N+= 1 if v==0 else (2 if pow(v,(p-1)//2,p)==1 else 0)
    lead=int(c.LC())%p
    if d%2==1: N+=1
    else: N+= 2 if pow(lead,(p-1)//2,p)==1 else 0
    return N
def ap(f,p): return p+1-cnt(f,p)
EG=(t**2-1)*(7*t**2+2*t-1)
Y=(7*t**2+2*t-1)*(7*t**2-2*t-1)
E2=sp.expand(t*(49*t**2-18*t+1))   # v^2=u(49u^2-18u+1)
for p in [3,5,7,11,13,17,19,23,29,31,37,41,43]:
    print(p,'a_p(E_G)=',ap(EG,p),' a_p(Y)=',ap(Y,p),' a_p(E2)=',ap(E2,p))
