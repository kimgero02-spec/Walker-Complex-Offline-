import sympy as sp, itertools
t,a1,a2,a3=sp.symbols('t a1 a2 a3')
A=sp.Matrix([[0,1,1],[1,0,1],[1,1,0]])
def g(M): return sp.expand((t*A-M).det())
# ansatz: M = [[x1,y1,0],[y1,x2,y2],[0,y2,x3]]-type tridiagonal / sparse; search
syms=sp.symbols('m11 m12 m13 m22 m23 m33')
m11,m12,m13,m22,m23,m33=syms
Mg=sp.Matrix([[m11,m12,m13],[m12,m22,m23],[m13,m23,m33]])
G=sp.Poly(g(Mg),t)
print(G.all_coeffs())
# target: 2 t^3+2a1 t^2+2a2 t+2a3
# try: m11=m33=0? search over zero patterns with polynomial solution
target=[2,2*a1,2*a2,2*a3]
co=G.all_coeffs()
import itertools
for zs in itertools.product([0,None],repeat=6):
    sub={s:z for s,z in zip(syms,zs) if z is not None}
    eqs=[sp.expand(c.subs(sub)-tg) for c,tg in zip(co[1:],target[1:])]
    free=[s for s in syms if s not in sub]
    if len(free)<3: continue
    try:
        sol=sp.solve(eqs,free,dict=True)
    except Exception as e:
        continue
    for s in sol:
        if all(v.is_polynomial(a1,a2,a3) for v in s.values()) and len(s)==len(free) : 
            print(sub,s)
