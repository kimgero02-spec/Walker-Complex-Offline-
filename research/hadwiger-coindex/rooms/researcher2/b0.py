import itertools, networkx as nx
from networkx.algorithms import approximation
def simplices(G, nonempty_only=True):
    V=list(G.nodes()); n=len(V); idx={v:i for i,v in enumerate(V)}
    adj=[0]*n
    for u,v in G.edges(): adj[idx[u]]|=1<<idx[v]; adj[idx[v]]|=1<<idx[u]
    out=[]
    # (A,B) bitmasks, A subset of CN(B)
    for B in range(1<<n):
        cn=(1<<n)-1
        for i in range(n):
            if B>>i&1: cn&=adj[i]
        # A any subset of cn
        A=cn
        while True:
            if A or B: out.append((A,B))
            if A==0: break
            A=(A-1)&cn
    return out,n
def betti_min(G, Zeff=True):
    S,n=simplices(G)
    # vertex set: (i,side) -> A bits 0..n-1, B bits n..2n-1
    def mask(s): return s[0] | (s[1]<<n)
    byd={}
    for s in S:
        m=mask(s); d=bin(m).count('1')-1
        byd.setdefault(d,[]).append(m)
    maxd=max(byd)
    ids={d:{m:i for i,m in enumerate(byd[d])} for d in byd}
    def rank(d): # rank of boundary d->d-1 over GF(2)
        if d==0 or d not in byd: return 0
        rows=[]
        for m in byd[d]:
            r=0; x=m
            while x:
                b=x&-x; x^=b
                r|=1<<ids[d-1][m^b]
            rows.append(r)
        basis={}; rk=0
        for r in rows:
            while r:
                h=r.bit_length()-1
                if h in basis: r^=basis[h]
                else: basis[h]=r; rk+=1; break
        return rk
    rk={d:rank(d) for d in range(0,maxd+2)}
    rk[0]=0
    # reduced: H~_d = dim C_d - rk_d - rk_{d+1} (with augmentation: d=0 reduced subtract 1)
    res={}
    for d in range(0,maxd+1):
        b=len(byd[d])-rk[d]-rk.get(d+1,0)
        if d==0: b-=1
        res[d]=b
    return res
def tau_h(G):
    r=betti_min(G)
    for d in sorted(r):
        if r[d]>0: return d+1, r   # hc=d, tau_h=hc+1
    return None, r
if __name__=="__main__":
    for name,G in [("K1",nx.complete_graph(1)),("K2",nx.complete_graph(2)),("K3",nx.complete_graph(3)),("K4",nx.complete_graph(4)),("K5",nx.complete_graph(5)),("C5",nx.cycle_graph(5)),("C7",nx.cycle_graph(7)),("C4",nx.cycle_graph(4)),("K33",nx.complete_bipartite_graph(3,3)),("E3",nx.empty_graph(3)),("P3",nx.path_graph(3))]:
        print(name,tau_h(G))
