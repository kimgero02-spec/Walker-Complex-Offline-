def graphs():
    g={}
    g['K2']=(2,[(0,1)])
    g['P3']=(3,[(0,1),(1,2)])
    g['C3']=(3,[(0,1),(1,2),(2,0)])
    g['C4']=(4,[(i,(i+1)%4) for i in range(4)])
    g['C5']=(5,[(i,(i+1)%5) for i in range(5)])
    g['C6']=(6,[(i,(i+1)%6) for i in range(6)])
    g['C7']=(7,[(i,(i+1)%7) for i in range(7)])
    g['K4']=(4,[(i,j) for i in range(4) for j in range(i+1,4)])
    g['K5']=(5,[(i,j) for i in range(5) for j in range(i+1,5)])
    g['K23']=(5,[(i,j) for i in range(2) for j in range(2,5)])
    g['loop+K2']=(3,[(0,0),(1,2)])
    g['2xedge']=(2,[(0,1),(0,1)])
    g['K3+K2+pt']=(6,[(0,1),(1,2),(2,0),(3,4)])
    g['Q3']=(8,[(a,a^(1<<k)) for a in range(8) for k in range(3) if a<a^(1<<k)])
    g['K33']=(6,[(i,j) for i in range(3) for j in range(3,6)])
    return g
def rows(rule,n,E):
    R=[]
    for (u,v) in E:
        r=[0]*n
        if rule=='0':
            a=[0]*n;a[u]=1;R.append(a);b=[0]*n;b[v]=1;R.append(b);continue
        if rule=='eq': r[u]+=1;r[v]-=1
        if rule=='neg': r[u]+=1;r[v]+=1
        R.append(r)
    return R
def kdim(rule,n,E,p):
    R=rows(rule,n,E)
    if not R: return n
    M=Matrix(R)
    return n-M.rank(iszerofunc=lambda e: e%p==0) if False else n-rank_mod(M,p)
def rank_mod(M,p):
    A=[[int(e)%p for e in M.row(i)] for i in range(M.rows)]
    r=0
    for c in range(M.cols):
        piv=None
        for i in range(r,len(A)):
            if A[i][c]%p: piv=i;break
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(a*inv)%p for a in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]%p:
                f=A[i][c];A[i]=[(a-f*b)%p for a,b in zip(A[i],A[r])]
        r+=1
    return r
G=graphs()
print('dims (R0,R(a=b),R(a+b=0),R4=n) for p=2,3,5,7')
for name,(n,E) in G.items():
    out=[]
    for p in (2,3,5,7):
        out.append((kdim('0',n,E,p),kdim('eq',n,E,p),kdim('neg',n,E,p),n))
    print(name,out)
def minpoly(M,p):
    n=M.rows
    # smallest k with I..M^k dependent mod p
    pw=[sp.eye(n)]
    for k in range(1,n+2):
        pw.append((pw[-1]*M).applyfunc(lambda e:e%p))
        V=Matrix([[int(e) for e in P.reshape(1,n*n)] for P in pw]).T
        # solve for dependency: nullspace mod p
        ns=nullspace_mod(V,p)
        if ns:
            c=ns[0]
            return Poly(sum(int(c[i])*x**i for i in range(len(c))),x,modulus=p)
def nullspace_mod(V,p):
    rws,cols=V.shape
    A=[[int(V[i,j])%p for j in range(cols)] for i in range(rws)]
    piv=[];r=0
    for c in range(cols):
        pi=None
        for i in range(r,rws):
            if A[i][c]: pi=i;break
        if pi is None: continue
        A[r],A[pi]=A[pi],A[r]
        inv=pow(A[r][c],-1,p);A[r]=[(a*inv)%p for a in A[r]]
        for i in range(rws):
            if i!=r and A[i][c]:
                f=A[i][c];A[i]=[(a-f*b)%p for a,b in zip(A[i],A[r])]
        piv.append(c);r+=1
    free=[c for c in range(cols) if c not in piv]
    res=[]
    for f in free:
        v=[0]*cols;v[f]=1
        for i,c in enumerate(piv): v[c]=(-A[i][f])%p
        res.append(v)
    # want the lowest-degree dependency: use the last free col (highest) -> check monic deg
    return res[:1]
def ops(n,E):
    D=sp.zeros(n,n);A=sp.zeros(n,n)
    for u,v in E:
        D[u,u]+=1;D[v,v]+=1;A[u,v]+=1;A[v,u]+=1
    return D,D-A,D+A
print('\nminpoly of D, L, Q  and dim ker (B^TB) vs dim ker B')
for name in ['K2','C3','C4','C5','C6','C7','K4','K5','K23']:
    n,E=G[name]
    D,L,Q=ops(n,E)
    for p in (3,5,7,2):
        res=[]
        for nm,M,rule in (('D',D,'0'),('L',L,'eq'),('Q',Q,'neg')):
            mp=minpoly(M,p)
            kb=kdim(rule,n,E,p); kt=n-rank_mod(M,p)
            res.append((nm,sp.factor_list(mp.as_expr(),modulus=p)[1] if False else str(sp.factor(mp.as_expr(),modulus=p)),kb,kt))
        print(name,p,res)
