# R04 r1: G[K_m] 의 극대 완전이분쌍 = 블롭 수준 타입 (X,Y,Z) + Z 블롭 분할.
import sys, itertools
from fractions import Fraction
import networkx as nx

def omega(G): return max(len(c) for c in nx.find_cliques(G))

def nbmasks(G):
    V=list(G.nodes()); idx={v:i for i,v in enumerate(V)}; n=len(V)
    nb=[0]*n
    for u,v in G.edges(): nb[idx[u]]|=1<<idx[v]; nb[idx[v]]|=1<<idx[u]
    return V,idx,nb

def types(G):
    """극대 타입 전수 (3^n 이상 배정). 반환: 집합 {(X,Y,Z)} (X<=Y 정규화, 비트마스크)."""
    V,idx,nb=nbmasks(G); n=len(V); out=set()
    for assign in itertools.product((0,1,2,3),repeat=n):
        X=Y=Z=0
        for i,a in enumerate(assign):
            if a==1: X|=1<<i
            elif a==2: Y|=1<<i
            elif a==3: Z|=1<<i
        if not (Y|Z) or not (X|Z): continue
        ok=True
        for i in range(n):
            if X>>i&1 and (Y|Z)&~nb[i]: ok=False;break
            if Y>>i&1 and (X|Z)&~nb[i]: ok=False;break
            if Z>>i&1 and (X|Y|(Z&~(1<<i)))&~nb[i]: ok=False;break
        if not ok: continue
        used=X|Y|Z
        if any((not used>>w&1) and (((Y|Z)&~nb[w])==0 or ((X|Z)&~nb[w])==0) for w in range(n)): continue
        out.add((X,Y,Z) if X<=Y else (Y,X,Z))
    return V,idx,nb,out

def bits(x,n): return [i for i in range(n) if x>>i&1]

def expand(n,m,T):
    """타입 -> 블로업의 극대쌍(정점=(블롭,s)). Z 는 m>=2 에서 비어있지 않은 진부분집합 분할."""
    pairs=set()
    for (X,Y,Z) in T:
        zs=bits(Z,n)
        if zs and m<2: continue
        A0=frozenset((i,s) for i in bits(X,n) for s in range(m))
        B0=frozenset((i,s) for i in bits(Y,n) for s in range(m))
        parts=[]
        for z in zs:
            subs=[S for r in range(1,m) for S in itertools.combinations(range(m),r)]
            parts.append([(z,S) for S in subs])
        for ch in itertools.product(*parts):
            A=set(A0);B=set(B0)
            for (z,S) in ch:
                for s in range(m):
                    (A if s in S else B).add((z,s))
            pairs.add(frozenset([frozenset(A),frozenset(B)]))
    return pairs

def brute(G,m):
    V,idx,nb=nbmasks(G); n=len(V)
    VV=[(i,s) for i in range(n) for s in range(m)]; N=len(VV); k={v:j for j,v in enumerate(VV)}
    adj=[0]*N
    for a in VV:
        for b in VV:
            if a!=b and (a[0]==b[0] or nb[a[0]]>>b[0]&1): adj[k[a]]|=1<<k[b]
    full=(1<<N)-1
    com=[full]*(1<<N)
    for mask in range(1,1<<N):
        low=mask&-mask; com[mask]=com[mask^low]&adj[low.bit_length()-1]
    pairs=set()
    for mask in range(1,1<<N):
        B=com[mask]
        if not B: continue
        A2=com[B]; B2=com[A2]
        fa=frozenset(VV[j] for j in range(N) if A2>>j&1); fb=frozenset(VV[j] for j in range(N) if B2>>j&1)
        pairs.add(frozenset([fa,fb]))
    return pairs

def check_moment(n,m,pairs,order,d):
    """블롭 순서 order(블롭 인덱스 리스트), t=pos*m+s+1. 유리수 정확: 변화 지점 중점 근 다항식 부호 확인."""
    pos={b:p for p,b in enumerate(order)}
    t=lambda v: pos[v[0]]*m+v[1]+1
    maxchg=0;bad=0
    for pr in pairs:
        L=list(pr); A=L[0]; B=L[1] if len(L)>1 else L[0]
        pts=sorted([(t(v),1) for v in A]+[(t(v),-1) for v in B])
        roots=[Fraction(pts[i][0]+pts[i+1][0],2) for i in range(len(pts)-1) if pts[i][1]!=pts[i+1][1]]
        maxchg=max(maxchg,len(roots))
        if len(roots)>d: bad+=1; continue
        def sg(x):
            v=1
            for r in roots: v*=(x-r)
            return 1 if v>0 else -1
        s0=pts[0][1]*sg(pts[0][0])
        if not all(pts[i][1]==s0*sg(pts[i][0]) for i in range(len(pts))): bad+=1
    return maxchg,bad

def Dsigma(n,T,order,m):
    """타입 상계 max((m-1)z + c_sigma): c = 제한된 블롭열에서 XX,YY 가 아닌 인접쌍 수."""
    pos={b:p for p,b in enumerate(order)}
    best=0;arg=None
    for (X,Y,Z) in T:
        letters=sorted([(pos[i],'X') for i in bits(X,n)]+[(pos[i],'Y') for i in bits(Y,n)]+[(pos[i],'Z') for i in bits(Z,n)])
        w=[l for _,l in letters]
        c=sum(1 for a,b in zip(w,w[1:]) if not (a==b and a in 'XY'))
        z=len(bits(Z,n))
        # Z 블롭은 m>=2 에서만
        if z and m<2: continue
        val=(m-1)*z+c
        if val>best: best=val;arg=(X,Y,Z)
    return best,arg

if __name__=="__main__":
    pass

def types2(G):
    """빠른 극대 타입 열거: 클리크 Z, N=공통이웃, Y⊆N, X=N∩cn(Y). 폐포·불교차 조건."""
    V,idx,nb=nbmasks(G); n=len(V); full=(1<<n)-1
    def cn(S):
        r=full
        for i in bits(S,n): r&=nb[i]
        return r
    cliques=[0]
    for c in nx.enumerate_all_cliques(G):
        cliques.append(sum(1<<idx[v] for v in c))
    out=set()
    for Z in cliques:
        N=cn(Z) if Z else full
        Nb=bits(N,n)
        if len(Nb)>16: raise RuntimeError("공통이웃이 너무 큼")
        for r in range(len(Nb)+1):
            for Ys in itertools.combinations(Nb,r):
                Y=sum(1<<i for i in Ys)
                X=N&cn(Y) if Y else N
                if X&Y: continue
                if X and (N&cn(X))!=Y: continue
                if not X and Y!=N: continue
                if not (X|Z) or not (Y|Z): continue
                out.add((X,Y,Z) if X<=Y else (Y,X,Z))
    return V,idx,nb,out
