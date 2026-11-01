# R2 researcher2: A_G = Z^V / <a u + b v : u->v>, 스미스 꼴 직접 구현 (순수 Python)
import random, itertools
from math import gcd
def snf_diag(M):
    A=[r[:] for r in M]; m=len(A); n=len(A[0]) if m else 0; d=[]; t=0
    while t<min(m,n):
        best=None
        for i in range(t,m):
            for j in range(t,n):
                if A[i][j] and (best is None or abs(A[i][j])<abs(A[best[0]][best[1]])): best=(i,j)
        if best is None: break
        i,j=best; A[t],A[i]=A[i],A[t]
        for r in A: r[t],r[j]=r[j],r[t]
        while True:
            ch=False
            for i in range(t+1,m):
                q=A[i][t]//A[t][t]
                if q: A[i]=[x-q*y for x,y in zip(A[i],A[t])]
                if A[i][t]: A[t],A[i]=A[i],A[t]; ch=True
            for j in range(t+1,n):
                q=A[t][j]//A[t][t]
                if q:
                    for r in A: r[j]-=q*r[t]
                if A[t][j]:
                    for r in A: r[t],r[j]=r[j],r[t]
                    ch=True
            if ch: continue
            bad=False
            for i in range(t+1,m):
                for j in range(t+1,n):
                    if A[i][j]%A[t][t]:
                        A[t]=[x+y for x,y in zip(A[t],A[i])]; bad=True;break
                if bad:break
            if not bad:break
        d.append(abs(A[t][t])); t+=1
    return d
def AG(n,arcs,a,b):
    M=[]
    for (u,v) in arcs:
        r=[0]*n; r[u]+=a; r[v]+=b; M.append(r)
    d=snf_diag(M)
    return [x for x in d if x!=1], n-len(d)   # (비자명 비틀림 인자, 자유 계수)
def dcyc(n): return [(i,(i+1)%n) for i in range(n)]
if __name__=="__main__":
    # 1. 방향 사이클 공식
    ok=True
    for a in range(-6,7):
        for b in range(-6,7):
            if a==0 or b==0: continue
            g=gcd(abs(a),abs(b)); a1,b1=a//g,b//g
            for n in range(1,7):
                T,f=AG(n,dcyc(n),a,b)
                N1=a1**n-(-b1)**n
                exp=sorted(([g]*(n-1) if g>1 else [])+([abs(g*N1)] if abs(g*N1)!=1 else []))
                if N1==0:
                    exp=sorted([g]*(n-1) if g>1 else []); fr=1
                else: fr=0
                if g==1 and N1!=0: exp=[abs(N1)] if abs(N1)!=1 else []
                if sorted(T)!=exp or f!=fr: ok=False; print("불일치",a,b,n,T,f,exp,fr)
    print("방향 사이클 공식 일치:",ok)
    # 2. 혼합 사이클: det, p-랭크
    def mixed(n,orient):
        arcs=[(i,(i+1)%n) if orient[i] else ((i+1)%n,i) for i in range(n)]
        return arcs
    def rank_mod(n,arcs,a,b,p):
        A=[[0]*n for _ in arcs]
        for k,(u,v) in enumerate(arcs): A[k][u]=(A[k][u]+a)%p; A[k][v]=(A[k][v]+b)%p
        r=0
        for c in range(n):
            piv=next((i for i in range(r,len(A)) if A[i][c]%p),None)
            if piv is None: continue
            A[r],A[piv]=A[piv],A[r]; iv=pow(A[r][c],-1,p); A[r]=[x*iv%p for x in A[r]]
            for i in range(len(A)):
                if i!=r and A[i][c]%p: f=A[i][c]; A[i]=[(x-f*y)%p for x,y in zip(A[i],A[r])]
            r+=1
        return r
    ok=True
    for (a,b) in [(-2,1),(-3,1),(2,3),(-6,5),(-4,9),(1,1),(-2,-3)]:
        for n in range(2,8):
            for orient in itertools.product([0,1],repeat=n):
                arcs=mixed(n,orient); T,f=AG(n,arcs,a,b)
                fw=sum(orient); rv=n-fw
                det=a**fw*b**rv-(-1)**n*a**rv*b**fw
                srcs=sum(1 for i in range(n) if orient[i]==1 and orient[i-1]==0)  # i가 두 호의 꼬리
                # 정점 i: 호 i-1 (i-1->i 이면 orient[i-1]=1 가 i로 들어옴), 호 i
                indeg=[0]*n; outdeg=[0]*n
                for (u,v) in arcs: outdeg[u]+=1; indeg[v]+=1
                S=sum(1 for i in range(n) if indeg[i]==0); K=sum(1 for i in range(n) if outdeg[i]==0)
                prod=1
                for t in T: prod*=t
                if det!=0 and prod!=abs(det): ok=False; print("det불일치",a,b,orient,T,det)
                for p in [2,3,5]:
                    if a%p==0 and b%p!=0:
                        if n-rank_mod(n,arcs,a,b,p)!=S: ok=False; print("p|a 랭크",a,b,orient,p)
                    if b%p==0 and a%p!=0:
                        if n-rank_mod(n,arcs,a,b,p)!=K: ok=False; print("p|b 랭크",a,b,orient,p)
    print("혼합 사이클 det, p-랭크(=원천/싱크 수) 일치:",ok)
