import itertools, random
def graph(n, edges, loops=()):
    A=[[0]*n for _ in range(n)]
    for u,v in edges: A[u][v]=A[v][u]=1
    for u in loops: A[u][u]=1
    return A
def cyc(n): return graph(n,[(i,(i+1)%n) for i in range(n)])
def path(n): return graph(n,[(i,i+1) for i in range(n-1)])
def comp(n): return graph(n,[(i,j) for i in range(n) for j in range(i+1,n)])
def kmn(a,b): return graph(a+b,[(i,a+j) for i in range(a) for j in range(b)])
def homs(AH,AG):
    m=len(AH); n=len(AG); res=[]
    f=[0]*m
    def rec(i):
        if i==m: res.append(tuple(f)); return
        for g in range(n):
            ok=True
            for j in range(i):
                if AH[i][j] and not AG[g][f[j]]: ok=False;break
            if ok and AH[i][i] and not AG[g][g]: ok=False
            if ok: f[i]=g; rec(i+1)
    rec(0); return res
def rank(rows,p):
    rows=[[x%p for x in r] for r in rows]; r=0
    if not rows: return 0
    nc=len(rows[0])
    for c in range(nc):
        piv=None
        for i in range(r,len(rows)):
            if rows[i][c]: piv=i;break
        if piv is None: continue
        rows[r],rows[piv]=rows[piv],rows[r]
        inv=pow(rows[r][c],p-2,p)
        rows[r]=[x*inv%p for x in rows[r]]
        for i in range(len(rows)):
            if i!=r and rows[i][c]:
                t=rows[i][c]; rows[i]=[(x-t*y)%p for x,y in zip(rows[i],rows[r])]
        r+=1
    return r
def vec(f,n):
    v=[0]*(len(f)*n)
    for h,g in enumerate(f): v[h*n+g]=1
    return v
def dimS(AH,AG,p=1000003):
    H=homs(AH,AG); n=len(AG)
    return len(H), rank([vec(f,n) for f in H],p)
def stats(AG):
    n=len(AG); seen=[-1]*n; comps=[]
    for s in range(n):
        if seen[s]>=0: continue
        col={s:0}; st=[s]; bip=True; verts=[s]; seen[s]=1
        while st:
            u=st.pop()
            for v in range(n):
                if AG[u][v]:
                    if v not in col: col[v]=1-col[u]; st.append(v); verts.append(v); seen[v]=1
                    elif col[v]==col[u]: bip=False
        comps.append((verts,bip))
    iso=[c for c in comps if len(c[0])==1 and not AG[c[0][0]][c[0][0]]]
    non=[c for c in comps if c not in iso]
    n1=sum(len(c[0]) for c in non); c1=len(non); b1=sum(1 for c in non if c[1])
    return n1,c1,b1
def bound(m,AG):
    n1,c1,b1=stats(AG); k=c1+b1
    return m*n1-(m-1)*k
