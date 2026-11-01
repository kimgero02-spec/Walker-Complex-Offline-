import warnings;warnings.filterwarnings('ignore')
from r4_gam import *
def K(n): return [[0 if i==j else 1 for j in range(n)] for i in range(n)]
def bip(A):
    n=len(A); B=[[0]*(2*n) for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if A[i][j]: B[i][n+j]=1;B[n+i][j]=1
    return B
for n in (5,):
    PGp=PG(K(n)); PH=PG(bip(K(n)))
    print(sp.factor(PGp.as_expr())); print(sp.factor(PH.as_expr()))
    print('check P_H=±P(t)P(-t):',sp.expand(PH.as_expr()-sp.expand(PGp.as_expr()*PGp.as_expr().subs(t,-t))))
    for p in [3,7,11,13,17,19,23,29]:
        g=gam_order(PGp,p); h=gam_order(PH,p)
        print(p,'|Γ_K5|=',g[2],'|Γ_K5xK2|=',h[2],'divides?',h[2]%g[2]==0, 'ratio',h[2]/g[2])
