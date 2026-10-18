import networkx as nx, itertools, random
def chi(G):
    n=G.number_of_nodes()
    if G.number_of_edges()==0: return 1
    nodes=sorted(G.nodes(),key=lambda v:-G.degree(v))
    for k in range(1,n+1):
        col={}
        def bt(i):
            if i==len(nodes): return True
            v=nodes[i]; used={col[u] for u in G[v] if u in col}
            for c in range(min(k, max(col.values(),default=-1)+2)):
                if c not in used:
                    col[v]=c
                    if bt(i+1): return True
                    del col[v]
            return False
        if bt(0): return k
def omega(G):
    return max((len(c) for c in nx.find_cliques(G)),default=1) if G.number_of_nodes() else 0
def planar(G): return nx.check_planarity(G)[0]
def report(N,pieces,name=""):
    K=set(frozenset(e) for e in itertools.combinations(range(N),2))
    cov=set()
    for P in pieces: cov|=set(frozenset(e) for e in P.edges())
    s=sum(chi(P) for P in pieces); w=sum(omega(P) for P in pieces)
    print(name,"N=",N,"covers K_N:",cov>=K,"all planar:",all(planar(P) for P in pieces),
          "chis:",[chi(P) for P in pieces],"omegas:",[omega(P) for P in pieces],"sigma=",s,"sum omega=",w)
    return s,w
