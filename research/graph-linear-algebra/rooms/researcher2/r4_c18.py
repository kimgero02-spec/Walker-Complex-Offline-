import warnings;warnings.filterwarnings('ignore')
from r4_gam import *
def cyc(n):
    A=[[0]*n for _ in range(n)]
    for i in range(n): A[i][(i+1)%n]=A[(i+1)%n][i]=1
    return A
P={n:PG(cyc(n)) for n in (3,6,9,18)}
def ratio(a,b): return sp.factor(sp.cancel(P[a].as_expr()/P[b].as_expr()))
for a,b in [(6,3),(9,3),(18,6),(18,9),(18,3)]:
    r=ratio(a,b); c,fl=sp.factor_list(r,t)
    print(f'C{a}/C{b}: R=',r,' square?', all(m%2==0 for f,m in fl) and sp.Integer(c)==1 or all(m%2==0 for f,m in fl))
for p in [5,7,11,13,17]:
    print(p,{n:gam_order(P[n],p)[2] for n in (3,6,9,18)})
