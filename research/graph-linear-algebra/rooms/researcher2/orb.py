import itertools, sys
from math import comb, factorial

def matmul(A,B,p):
    n=len(A);k=len(B);m=len(B[0])
    return tuple(tuple(sum(A[i][t]*B[t][j] for t in range(k))%p for j in range(m)) for i in range(n))
def E(n,u,v,c,p):
    M=[[1 if i==j else 0 for j in range(n)] for i in range(n)]
    M[u][v]=c%p
    return tuple(map(tuple,M))
def orbits(n,m,p,rowgens,colgens=()):
    # matrices as tuples of n rows
    allM=list(itertools.product(range(p),repeat=n*m))
    idx={M:i for i,M in enumerate(allM)}
    par=list(range(len(allM)))
    def find(x):
        while par[x]!=x:
            par[x]=par[par[x]];x=par[x]
        return x
    def mat(M): return tuple(tuple(M[i*m:(i+1)*m]) for i in range(n))
    def flat(X): return tuple(x for r in X for x in r)
    for M in allM:
        X=mat(M)
        for g in rowgens:
            Y=flat(matmul(g,X,p)); a,b=find(idx[M]),find(idx[Y])
            if a!=b: par[a]=b
        for h in colgens:
            Y=flat(matmul(X,h,p)); a,b=find(idx[M]),find(idx[Y])
            if a!=b: par[a]=b
    return len({find(i) for i in range(len(allM))})
def gens_from_rel(n,rel,p):
    return [E(n,u,v,c,p) for (u,v) in rel for c in range(1,p)]
def closure_rel(n,arcs):
    R=set(arcs)
    ch=True
    while ch:
        ch=False
        for (a,b) in list(R):
            for (c,d) in list(R):
                if b==c and a!=d and (a,d) not in R: R.add((a,d));ch=True
    return R
def grp_order(gens,n,p):
    I=tuple(tuple(1 if i==j else 0 for j in range(n)) for i in range(n))
    S={I};fr=[I]
    while fr:
        nf=[]
        for X in fr:
            for g in gens:
                Y=matmul(g,X,p)
                if Y not in S: S.add(Y);nf.append(Y)
        fr=nf
    return len(S)
if __name__=="__main__":
    p=3
    # collapse
    und=[(0,1),(1,0),(1,2),(2,1)]
    print("undirected P3 group order F3:",grp_order(gens_from_rel(3,und,3),3,3),"(|SL3(F3)|=5616)")
    print("directed path 0->1->2 order:",grp_order(gens_from_rel(3,closure_rel(3,[(0,1),(1,2)]),3),3,3),"(27)")
    print("directed path w/o closure (no 0->2 gen) order:",grp_order(gens_from_rel(3,[(0,1),(1,2)],3),3,3))
    # 2-cycle + tail: 0<->1, 1->2
    arcs=[(0,1),(1,0),(1,2)]
    R=closure_rel(3,arcs); print("SCC {0,1} ->2 order:",grp_order(gens_from_rel(3,R,3),3,3),"expected |SL2(3)|*3^2=",24*9)
