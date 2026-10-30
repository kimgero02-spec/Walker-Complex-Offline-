# R24 researcher1: (star) under Hajos identification. Search/check only, not evidence.
import itertools
def colorable(adj, verts, k):
    verts=sorted(verts, key=lambda v:-len(adj[v]&verts)); col={}
    def bt(i,mx):
        if i==len(verts): return True
        v=verts[i]; used={col[u] for u in adj[v] if u in col}
        for c in range(min(k,mx+2)):
            if c not in used:
                col[v]=c
                if bt(i+1,max(mx,c)): return True
                del col[v]
        return False
    return bt(0,-1)
def chi(adj):
    k=1
    while not colorable(adj,set(adj),k): k+=1
    return k
def witness(adj,k=4):
    V=set(adj)
    for z in sorted(V,key=str):
        rest=sorted(V-{z},key=str); opts=[]
        for v in rest:
            d={}
            for t in adj[z]:
                S=frozenset(adj[v]&(adj[t]-{z}))
                d.setdefault(S,t)
            mx=[(S,d[S]) for S in d if len(S)>=k-1 and not any(S<T for T in d)]
            opts.append(mx if mx else [(frozenset(),None)])
        for choice in itertools.product(*opts):
            al={v:c[0] for v,c in zip(rest,choice)}
            A={v:{u for u in al[v] if v in al[u]} for v in rest}
            core=set(rest); ch=True
            while ch:
                ch=False
                for v in list(core):
                    if len(A[v]&core)<k-1: core.discard(v); ch=True
            if core and not colorable({v:A[v]&core for v in core}, core, k-1):
                return z,{v:c[1] for v,c in zip(rest,choice) if v in core},core
    return None
def adj_of(E):
    adj={}
    for u,v in E:
        adj.setdefault(u,set()).add(v); adj.setdefault(v,set()).add(u)
    return adj
def identify(adj,u,v,m='m'):
    assert v not in adj[u]
    new={}
    for x in adj:
        if x in (u,v): continue
        new[x]={ (m if y in (u,v) else y) for y in adj[x]}
    new[m]=(adj[u]|adj[v])
    return new
def gamma():
    a=['w','a1','a2','a3','a4']; b=['w','b1','b2','b3','b4']
    E=[e for e in itertools.combinations(a,2) if set(e)!={'w','a1'}]+[e for e in itertools.combinations(b,2) if set(e)!={'w','b1'}]+[('a1','b1')]
    return adj_of(E)
if __name__=='__main__':
    G=gamma(); print('chi',chi(G),'witness',witness(G))
    V=sorted(G)
    for u,v in itertools.combinations(V,2):
        if v in G[u]: continue
        Gp=identify(G,u,v)
        print(u,v,'chi',chi(Gp),'wit',witness(Gp))
