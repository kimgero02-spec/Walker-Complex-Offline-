import random, itertools, sys
from collections import Counter
from tors import curve, disc3, gco
from burn import rank_mod
A=[[0,1,1],[1,0,1],[1,1,0]]
def val(n,p):
    if n==0: return 99
    v=0
    while n%p==0: n//=p; v+=1
    return v
def mats(M):
    m11,m12,m13,m22,m23,m33=M
    return [[m11,m12,m13],[m12,m22,m23],[m13,m23,m33]]
def analyze(M,p):
    a,b,c=curve(M); D=disc3(a,b,c)
    if D==0 or D%p: return None
    # roots mod p of Y-cubic
    roots=[x for x in range(p) if (x**3+a*x*x+b*x+c)%p==0]
    # multiplicity
    def mult(r):
        m=0; cur=[1,a%p,b%p,c%p]
        while len(cur)>1:
            q=[cur[0]]
            for z in cur[1:-1]: q.append((z+q[-1]*r)%p)
            if (cur[-1]+q[-1]*r)%p==0: m+=1;cur=q
            else: break
        return m
    ms=sorted((mult(r),r) for r in roots)
    top=ms[-1]
    Mm=mats(M)
    nubar=(top[1]*pow(2,-1,p))%p     # X=2 nu
    B=[[ (Mm[i][j]-nubar*A[i][j])%p for j in range(3)] for i in range(3)]
    r=rank_mod(B,p)
    return top[0], r, val(D,p), (a,b,c)
if __name__=="__main__":
    p=int(sys.argv[1]); random.seed(5)
    cnt=Counter()
    for _ in range(int(sys.argv[2])):
        # force near-degenerate: choose M as nu0*A + p*something or random
        M=[random.randint(-3*p,3*p) for _ in range(6)]
        res=analyze(M,p)
        if res: cnt[(res[0],res[1],min(res[2],6))]+=1
    for k,v in sorted(cnt.items()): print("mult",k[0],"rank(M-nuA)",k[1],"v_p(disc)",k[2],v)
