import numpy as np, networkx as nx, itertools, time
from r04_sat import *
def flips(G,k,seed):
    rng=np.random.default_rng(seed); G=G.copy()
    for _ in range(k):
        e=list(G.edges()); u,v=e[rng.integers(len(e))]
        C=list(set(G[u])&set(G[v]))
        if len(C)!=2: continue
        a,b=C
        if G.has_edge(a,b) or G.degree(u)<=3 or G.degree(v)<=3: continue
        G.remove_edge(u,v); G.add_edge(a,b)
    return G
def hubflips(G,k,seed):
    # prefer flips that increase max degree (build K_{2,m}-rich triangulations)
    rng=np.random.default_rng(seed); G=G.copy()
    for _ in range(k):
        e=list(G.edges()); u,v=e[rng.integers(len(e))]
        C=list(set(G[u])&set(G[v]))
        if len(C)!=2: continue
        a,b=C
        if G.has_edge(a,b) or G.degree(u)<=3 or G.degree(v)<=3: continue
        if G.degree(a)+G.degree(b) >= G.degree(u)+G.degree(v) or rng.random()<0.03:
            G.remove_edge(u,v); G.add_edge(a,b)
    return G
def nviol(G,order):
    pos={v:i for i,v in enumerate(order)}; c=0
    for a,b,C in pairs_of(G):
        lo,hi=sorted((pos[a],pos[b]))
        if len(set(0 if pos[x]<lo else (1 if pos[x]<hi else 2) for x in C))==3: c+=1
    return c
def solve_levels(G,root):
    lev=nx.single_source_shortest_path_length(G,root)
    def extra(S,X,idx):
        for u in G:
            for v in G:
                if lev[u]<lev[v]: S.add_clause([X(idx[u],idx[v])])
    return solve(G,extra)
def tests():
    T=[]
    for n,s in ((30,0),(30,1),(50,2)): T.append(("hub%d/%d"%(n,s),hubflips(tri_graph(s,n),60*n,s)))
    for n,s in ((30,0),(50,1)): T.append(("flip%d/%d"%(n,s),flips(tri_graph(s,n),30*n,s)))
    for n,s in ((30,0),(50,1)): T.append(("stk%d/%d"%(n,s),stacked(s,n)))
    for n,s in ((50,0),): T.append(("del%d/%d"%(n,s),tri_graph(s,n)))
    return T
