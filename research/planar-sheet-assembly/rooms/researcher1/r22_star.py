import itertools, sys
def colorable(adj, verts, k):
    verts=sorted(verts, key=lambda v:-len(adj[v]&verts))
    col={}
    def bt(i):
        if i==len(verts): return True
        v=verts[i]
        used={col[u] for u in adj[v] if u in col}
        for c in range(k):
            if c not in used:
                col[v]=c
                if bt(i+1): return True
                del col[v]
            if c>=len(col): break  # symmetry: new colour only once
        return False
    return bt(0)
def star_violation(adj):
    """return (z,s) giving shadow H with chi>=4, or None. exact over all s (maximal options)."""
    V=set(adj)
    for z in V:
        rest=sorted(V-{z},key=str)
        opts=[]
        for v in rest:
            sets={frozenset(adj[v]&(adj[t]-{z})) for t in adj[z]}
            mx=[S for S in sets if not any(S<T for T in sets)]
            opts.append(mx)
        for choice in itertools.product(*opts):
            al=dict(zip(rest,choice))
            A={v:{u for u in al[v] if v in al[u]} for v in rest}
            core=set(rest)
            ch=True
            while ch:
                ch=False
                for v in list(core):
                    if len(A[v]&core)<3: core.discard(v); ch=True
            if core and not colorable({v:A[v]&core for v in core}, core, 3):
                return z,al
    return None
def chi(adj):
    k=1
    while not colorable(adj,set(adj),k): k+=1
    return k
def edges_to_adj(E):
    adj={}
    for u,v in E:
        adj.setdefault(u,set()).add(v); adj.setdefault(v,set()).add(u)
    return adj
def K5(names): return list(itertools.combinations(names,2))
def hajos(E1,E2,x,y1,y2):
    """E1,E2 share vertex x only; remove x y1 from E1, x y2 from E2, add y1y2"""
    f=lambda e: frozenset(e)
    A=[e for e in E1 if f(e)!=f((x,y1))]; B=[e for e in E2 if f(e)!=f((x,y2))]
    assert len(A)==len(E1)-1 and len(B)==len(E2)-1
    return A+B+[(y1,y2)]
