import warnings;warnings.filterwarnings('ignore')
from r4lib import *
import itertools, random
random.seed(3)
n=4
edges=[(i,j) for i in range(n) for j in range(i+1,n)]
perms=list(itertools.permutations(range(3)))
def permmat(p):
    M=sp.zeros(3,3)
    for i in range(3): M[i,p[i]]=1
    return M
A=[[0 if i==j else 1 for j in range(n)] for i in range(n)]
tree={(0,1),(0,2),(0,3)}
found=0
for trial in range(200):
    volt={e:(tuple(range(3)) if e in tree else random.choice(perms)) for e in edges}
    H=sp.zeros(3*n,3*n)
    for (i,j),p in volt.items():
        M=permmat(p)
        H[3*i:3*i+3,3*j:3*j+3]=M; H[3*j:3*j+3,3*i:3*i+3]=M.T
    PH=PG(H.tolist()); PGp=PG(A)
    R=sp.cancel(PH.as_expr()/PGp.as_expr())
    c,fl=sp.factor_list(R,t)
    nonsq=[(f,m) for f,m in fl if m%2]
    if nonsq:
        print('volt',volt); print('R factor',sp.factor(R)); found+=1
        # connectivity: group generated
        break
print('found',found)
