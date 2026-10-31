import itertools, math
def rank_mod(M,p):
    M=[[x%p for x in r] for r in M]; r=0
    if not M: return 0
    for c in range(len(M[0])):
        piv=None
        for i in range(r,len(M)):
            if M[i][c]: piv=i;break
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]; inv=pow(M[r][c],-1,p)
        M[r]=[x*inv%p for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]:
                f=M[i][c]; M[i]=[(a-f*b)%p for a,b in zip(M[i],M[r])]
        r+=1
        if r==len(M): break
    return r
def Bmat(n,arcs,lam,p):
    B=[]
    for (u,v) in arcs:
        row=[0]*n; row[u]=(row[u]-lam)%p; row[v]=(row[v]+1)%p; B.append(row)
    return B
def dimker(n,arcs,lam,p): return n-rank_mod(Bmat(n,arcs,lam,p),p)
def BtB(B,p,n):
    return [[sum(B[a][i]*B[a][j] for a in range(len(B)))%p for j in range(n)] for i in range(n)]
def order(l,p):
    k=1;x=l%p
    while x!=1: x=x*l%p;k+=1
    return k
def winding_gcd_components(n,arcs):
    # BFS potential, gcd of residual
    adj={i:[] for i in range(n)}
    for (u,v) in arcs: adj[u].append((v,1)); adj[v].append((u,-1))
    seen={};res=[]
    for r in range(n):
        if r in seen: continue
        seen[r]=0;st=[r];g=0;comp=[r]
        while st:
            x=st.pop()
            for y,d in adj[x]:
                if y not in seen: seen[y]=seen[x]+d;st.append(y);comp.append(y)
                else: g=math.gcd(g,seen[x]+d-seen[y])
        res.append(g)
    return res
def predicted(n,arcs,k):
    return sum(1 for g in winding_gcd_components(n,arcs) if g%k==0)
if __name__=="__main__":
    # directed cycle tables
    for p,lams in [(5,[1,4,2]),(7,[1,6,2,3]),(13,[2,5,12])]:
        for lam in lams:
            k=order(lam,p)
            row=[]
            for n in range(1,15):
                arcs=[(i,(i+1)%n) for i in range(n)]
                d=dimker(n,arcs,lam,p); assert d==predicted(n,arcs,k)
                row.append(d)
            print("p",p,"lam",lam,"ord",k,"dim C->_n, n=1..14:",row)
    # mixed cycles: all orientations of C_n, check formula k | n-2b
    for p,lam in [(5,2),(7,2),(7,3),(13,2)]:
        k=order(lam,p)
        for n in [3,4,5,6]:
            cnt=0
            for o in itertools.product([0,1],repeat=n):
                arcs=[(i,(i+1)%n) if o[i]==0 else ((i+1)%n,i) for i in range(n)]
                d=dimker(n,arcs,lam,p); b=sum(o)
                assert d==(1 if (n-2*b)%k==0 else 0); cnt+=d
            print("p",p,"lam",lam,"k",k,"C_%d balanced orientations"%n,cnt,"of",2**n)
    # B^T B kernel vs B kernel
    p=5;lam=2
    for n in range(2,8):
        arcs=[(i,(i+1)%n) for i in range(n)]
        B=Bmat(n,arcs,lam,p);G=BtB(B,p,n)
        print("Z5 lam2 dirC",n,"dimker B",n-rank_mod(B,p),"dimker BtB",n-rank_mod(G,p))
    p=7
    for lam in [2,3,6,1]:
      for n in [3,6,7,4,8]:
        arcs=[(i,(i+1)%n) for i in range(n)]
        B=Bmat(n,arcs,lam,p);G=BtB(B,p,n)
        print("Z7 lam",lam,"dirC",n,"kerB",n-rank_mod(B,p),"kerBtB",n-rank_mod(G,p))
