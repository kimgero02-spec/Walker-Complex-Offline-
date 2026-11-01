import numpy as np, sys, itertools
from collections import Counter, defaultdict
import sympy as sp
p=int(sys.argv[1]); lab=np.load(f"lab{p}.npy")
n=p**9
reps={}
u,first=np.unique(lab,return_index=True)
Ainv=sp.Matrix([[-1,sp.Rational(1,2),sp.Rational(1,2)],[sp.Rational(1,2),-1,sp.Rational(1,2)],[sp.Rational(1,2),sp.Rational(1,2),-1]])
def modp(r): 
    r=sp.Rational(r); return (r.p*pow(r.q,-1,p))%p
def rankp(M):
    from burn import rank_mod
    return rank_mod([[int(x)%p for x in M.row(i)] for i in range(3)],p)
def mult_pattern(c):
    roots=[x for x in range(p) if (x**3+c[0]*x*x+c[1]*x+c[2])%p==0]
    # multiplicities
    cc=[1,c[0],c[1],c[2]]; mult={}
    for r in roots:
        m=0; cur=cc[:]
        while len(cur)>1:
            q=[cur[0]]
            for k in cur[1:-1]: q.append((k+q[-1]*r)%p)
            if (cur[-1]+q[-1]*r)%p==0: m+=1;cur=q
            else: break
        mult[r]=m
    return tuple(sorted(mult.values(),reverse=True)), roots
cnt=Counter()
for i in first:
    digs=[(int(i)//p**(8-k))%p for k in range(9)]
    M=sp.Matrix(3,3,digs)
    phi=Ainv*M
    X=phi.T*Ainv.T*0  # placeholder
    # adjoint wrt A: phi* = A^{-1} phi^T A
    A=sp.Matrix([[0,1,1],[1,0,1],[1,1,0]])
    ps=Ainv*phi.T*A
    H=ps*phi
    t=sp.symbols('t')
    cp=sp.Poly((t*sp.eye(3)-H).det(),t)
    co=[modp(x) for x in cp.all_coeffs()]
    pat,roots=mult_pattern(co[1:])
    r=rankp(M)
    d=modp(M.det())
    dcls = 0 if d==0 else (1 if pow(d,(p-1)//2,p)==1 else -1)
    # type of h: with irreducible info
    nroots=len(roots)
    cnt[(r,pat,nroots,dcls)]+=1
tot=0
for k,v in sorted(cnt.items()): print(k,v); tot+=v
print(tot)
