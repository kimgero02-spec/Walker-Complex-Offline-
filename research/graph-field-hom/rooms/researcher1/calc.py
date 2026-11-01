# researcher1 R1: dims of F^G for 4 undirected rules; ker(B^T B) vs ker B; minpolys mod p
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
        if rule=='0':
            a=[0]*n;a[u]=1;R.append(a);b=[0]*n;b[v]=1;R.append(b);continue
        r=[0]*n
        if rule=='eq': r[u]+=1;r[v]-=1
        if rule=='neg': r[u]+=1;r[v]+=1
        R.append(r)
    return R
def rank_mod(A,p):
    A=[[e%p for e in r] for r in A]
    if not A: return 0
    r=0
    for c in range(len(A[0])):
        piv=next((i for i in range(r,len(A)) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c],-1,p);A[r]=[(a*inv)%p for a in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]:
                f=A[i][c];A[i]=[(a-f*b)%p for a,b in zip(A[i],A[r])]
        r+=1
    return r
def kdim(rule,n,E,p): return n-rank_mod(rows(rule,n,E),p)
def matmul(A,B,p):
    n=len(A);return [[sum(A[i][k]*B[k][j] for k in range(n))%p for j in range(n)] for i in range(n)]
def minpoly(M,p):
    n=len(M);I=[[int(i==j) for j in range(n)] for i in range(n)]
    pw=[I];
    for k in range(1,n+2):
        pw.append(matmul(pw[-1],M,p))
        vecs=[[e for r in P for e in r] for P in pw]  # rows = powers; find dependency
        # solve sum c_i vecs[i]=0 with c_k=1: Gaussian on transpose
        cols=len(pw)
        T=[[vecs[i][j] for i in range(cols)] for j in range(n*n)]
        # row reduce T
        A=[[e%p for e in r] for r in T];piv=[];r=0
        for c in range(cols):
            pi=next((i for i in range(r,len(A)) if A[i][c]),None)
            if pi is None: continue
            A[r],A[pi]=A[pi],A[r];inv=pow(A[r][c],-1,p);A[r]=[(a*inv)%p for a in A[r]]
            for i in range(len(A)):
                if i!=r and A[i][c]:
                    f=A[i][c];A[i]=[(a-f*b)%p for a,b in zip(A[i],A[r])]
            piv.append(c);r+=1
        if cols-1 not in piv:  # last column free => monic dependency
            v=[0]*cols;v[cols-1]=1
            for i,c in enumerate(piv): v[c]=(-A[i][cols-1])%p
            return v
def roots_mult(v,p):
    # factor out (x-a) for a in F_p, return list of (a,mult), remainder degree
    v=v[:];res=[]
    for a in range(p):
        m=0
        while len(v)>1:
            # synthetic division by (x-a), coefficients low->high
            q=[0]*(len(v)-1);carry=0
            for i in range(len(v)-1,0,-1):
                carry=(v[i]+carry*a)%p;q[i-1]=carry
            rem=(v[0]+carry*a)%p
            if rem==0: v=q;m+=1
            else: break
        if m: res.append((a,m))
    return res,len(v)-1
def ops(n,E):
    D=[[0]*n for _ in range(n)];A=[[0]*n for _ in range(n)]
    for u,v in E:
        D[u][u]+=1;D[v][v]+=1;A[u][v]+=1;A[v][u]+=1
    L=[[D[i][j]-A[i][j] for j in range(n)] for i in range(n)]
    Q=[[D[i][j]+A[i][j] for j in range(n)] for i in range(n)]
    return D,L,Q
if __name__=='__main__':
    G=graphs()
    print('dims (R0, a=b, a+b=0, F^2) for p=2,3,5,7')
    for name,(n,E) in G.items():
        print(name,[(kdim('0',n,E,p),kdim('eq',n,E,p),kdim('neg',n,E,p),n) for p in (2,3,5,7)])
    print('\nname p : op: (linear factors a^mult, nonlinear rem deg), dimker B, dimker B^TB')
    for name in ['K2','C3','C4','C5','C6','C7','K4','K5','K23']:
        n,E=G[name];D,L,Q=ops(n,E)
        for p in (2,3,5,7):
            out=[]
            for nm,M,rule in (('D',D,'0'),('L',L,'eq'),('Q',Q,'neg')):
                Mm=[[e%p for e in r] for r in M]
                mp=minpoly(Mm,p);rt=roots_mult(mp,p)
                out.append((nm,rt,kdim(rule,n,E,p),n-rank_mod(Mm,p)))
            print(name,p,out)
