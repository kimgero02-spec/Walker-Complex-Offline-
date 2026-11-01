# Schnyder-tree preorders (from the canonical ordering) on K_{2,m}-rich triangulations
from r04_lib import *
from networkx.algorithms.planar_drawing import triangulate_embedding, get_canonical_ordering
def trees(G):
    ok,emb=nx.check_planarity(G); emb2,outer=triangulate_embedding(emb,True)
    co=get_canonical_ordering(emb2,outer)
    order=[c[0] for c in co]; rank={v:i for i,v in enumerate(order)}
    G2=nx.Graph(emb2.edges())
    par1={};par2={};par3={}
    for v,cont in co[2:]:
        par1[v]=cont[0]; par2[v]=cont[-1]
        for w in cont[1:-1]: par3[w]=v
    return G2,order,par1,par2,par3
def preorder(par,order,rootcands):
    ch={}
    for v,p in par.items(): ch.setdefault(p,[]).append(v)
    seen=[];st=[]
    roots=[v for v in order if v not in par]
    def dfs(v):
        seen.append(v)
        for c in sorted(ch.get(v,[]),key=lambda x:order.index(x)): dfs(c)
    import sys; sys.setrecursionlimit(10000)
    for r in roots: dfs(r)
    return seen
for name,G in tests():
    G2,order,p1,p2,p3=trees(G)
    res={"canon":nviol(G2,order),"T1pre":nviol(G2,preorder(p1,order,0)),"T2pre":nviol(G2,preorder(p2,order,0)),"T3pre":nviol(G2,preorder(p3,order,0)),
         "T1post-rev":nviol(G2,preorder(p1,order,0)[::-1])}
    print(name,"pairs",len(pairs_of(G2)),res,flush=True)
