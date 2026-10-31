import itertools, networkx as nx
from pysat.solvers import Cadical153
def zig_le(G,t,return_order=False):
    """exists vertex order with no alternating complete-bipartite pattern of length t+1 (i.e. all bicliques <= t runs)"""
    V=list(G.nodes()); n=len(V); idx={v:i for i,v in enumerate(V)}
    adj=[[False]*n for _ in range(n)]
    for u,v in G.edges(): adj[idx[u]][idx[v]]=adj[idx[v]][idx[u]]=True
    var={}
    c=0
    for i in range(n):
        for j in range(i+1,n):
            c+=1; var[(i,j)]=c
    def x(i,j): return var[(i,j)] if i<j else -var[(j,i)]
    s=Cadical153()
    for i in range(n):
        for j in range(n):
            if i==j: continue
            for k in range(n):
                if k==i or k==j: continue
                s.add_clause([-x(i,j),-x(j,k),x(i,k)])
    L=t+1
    # DFS over tuples p1..pL distinct, odd positions complete to even positions
    def rec(seq):
        if len(seq)==L:
            s.add_clause([-x(seq[i],seq[i+1]) for i in range(L-1)]); return
        for v in range(n):
            if v in seq: continue
            pos=len(seq)  # 0-based; parity classes
            ok=True
            for q,u in enumerate(seq):
                if (q%2)!=(pos%2) and not adj[u][v]: ok=False;break
            if ok: rec(seq+[v])
    rec([])
    r=s.solve()
    if not return_order: return r
    if not r: return r,None
    m=set(l for l in s.get_model() if l>0)
    key=lambda i:sum(1 for j in range(n) if j!=i and (x(j,i) in m if x(j,i)>0 else -x(j,i) not in m))
    order=sorted(range(n),key=key)
    return r,[V[i] for i in order]
def zig(G):
    t=2
    while not zig_le(G,t): t+=1
    return t
