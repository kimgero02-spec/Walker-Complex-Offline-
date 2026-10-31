import networkx as nx, itertools, sys
def maxbicl(G):
    V=list(G.nodes()); n=len(V)
    adj={v:set(G[v]) for v in V}
    res=set()
    for r in range(1,n+1):
        for B in itertools.combinations(V,r):
            cn=set(V)
            for b in B: cn&=adj[b]
            if not cn: continue
            # A=cn ; B must equal common nbrs of A
            cb=set(V)
            for a in cn: cb&=adj[a]
            if cb==set(B): res.add((frozenset(cn),frozenset(B)))
    out=set()
    for A,B in res: out.add(frozenset([A,B]))
    return [tuple(x) for x in out]
def runs(order,pos,A,B):
    pts=sorted(list(A)+list(B),key=lambda v:pos[v])
    r=1
    for x,y in zip(pts,pts[1:]):
        if (x in A)!=(y in A): r+=1
    return r
def rho(G,limit=None):
    P=maxbicl(G); V=list(G.nodes()); best=99;bo=None
    for perm in itertools.permutations(V[1:]):
        order=(V[0],)+perm
        pos={v:i for i,v in enumerate(order)}
        m=max(runs(order,pos,A,B) for A,B in P)
        if m<best: best=m;bo=order
        if best<=3 and limit==3: break
    return best,bo,len(P)
if __name__=="__main__":
    n=int(sys.argv[1]);G=nx.Graph()
    for i in range(n):
        for k in (1,2): G.add_edge(i,(i+k)%n)
    print(n,rho(G))
