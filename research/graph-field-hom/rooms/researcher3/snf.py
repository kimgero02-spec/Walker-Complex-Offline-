from math import gcd
class Matrix:
    def __init__(s,rows): s.a=[list(r) for r in rows]; s.rows=len(rows); s.cols=len(rows[0]) if rows else 0
    def row(s,i): return s.a[i]
def SNFdiag(A):
    A=[r[:] for r in A]; m=len(A); n=len(A[0]); d=[]
    t=0
    while t<min(m,n):
        # find nonzero min abs
        best=None
        for i in range(t,m):
            for j in range(t,n):
                if A[i][j] and (best is None or abs(A[i][j])<abs(A[best[0]][best[1]])): best=(i,j)
        if best is None: break
        i,j=best; A[t],A[i]=A[i],A[t]
        for r in A: r[t],r[j]=r[j],r[t]
        done=False
        while not done:
            done=True
            for i in range(t+1,m):
                q=A[i][t]//A[t][t]
                A[i]=[x-q*y for x,y in zip(A[i],A[t])]
                if A[i][t]: A[t],A[i]=A[i],A[t]; done=False
            for j in range(t+1,n):
                q=A[t][j]//A[t][t]
                for r in A: r[j]-=q*r[t]
                if A[t][j]:
                    for r in A: r[t],r[j]=r[j],r[t]
                    done=False
            if done:
                for i in range(t+1,m):
                    for j in range(t+1,n):
                        if A[i][j]%A[t][t]:
                            A[t]=[x+y for x,y in zip(A[t],A[i])]; done=False;break
                    if not done:break
        d.append(abs(A[t][t])); t+=1
    return d
def B(arcs,n,a,b):
    M=[[0]*n for _ in arcs]
    for i,(u,v) in enumerate(arcs):
        M[i][u]+=a; M[i][v]+=b
    return Matrix(M)
def snf(M):
    d=SNFdiag(M.a); free=min(M.rows,M.cols)-len(d)
    return sorted(x for x in d if x!=1), "zeros(rank-deficit)=",M.cols-len(d)
def nullity(M,p):
    M2=M
    # rank mod p via gaussian elimination
    A=[[int(x)%p for x in M2.a[i]] for i in range(M2.rows)]
    r=0;n=M2.cols
    for c in range(n):
        piv=None
        for i in range(r,len(A)):
            if A[i][c]%p: piv=i;break
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[x*inv%p for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]%p:
                f=A[i][c]; A[i]=[(x-f*y)%p for x,y in zip(A[i],A[r])]
        r+=1
    return n-r
def cyc(n): return [(i,(i+1)%n) for i in range(n)]
print("directed cycles, (a,b)=(-2,1),(3,2),(1,1)")
for (a,b) in [(-2,1),(3,2),(1,1),(-3,1)]:
    for n in [1,2,3,4]:
        M=B(cyc(n),n,a,b)
        print((a,b),n,snf(M),"expected",abs(a**n-(-b)**n))
print("v<-u, v<-w with (-2,1): arcs 0->2,1->2")
M=B([(0,2),(1,2)],3,-2,1); print(snf(M),[nullity(M,p) for p in (2,3,5)], "rank Q",snf(M)[2])
print("mixed triangle 0->1,1->2,0->2")
for ab in [(-2,1),(1,1),(1,-1),(-3,2)]:
    M=B([(0,1),(1,2),(0,2)],3,*ab); print(ab,snf(M),snf(M)[2],[nullity(M,p) for p in (2,3,5,7)])
print("K4^(3) triples")
import itertools
def hyp(edges,n,coef):
    M=[[0]*n for _ in edges]
    for i,e in enumerate(edges):
        for c,v in zip(coef,e): M[i][v]+=c
    return Matrix(M)
M=hyp(list(itertools.combinations(range(4),3)),4,(1,1,1)); print(snf(M),[nullity(M,p) for p in (2,3,5)])
fano=[(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)]
M=hyp(fano,7,(1,1,1)); print("Fano",snf(M),[nullity(M,p) for p in (2,3,5)])
print("original rule odd cycle C5, C4 undirected as arcs i->i+1")
for n in [4,5]:
    M=B(cyc(n),n,1,1); print(n,snf(M),[nullity(M,p) for p in (2,3)])
