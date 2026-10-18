import json, itertools, networkx as nx, collections
from networkx.generators.atlas import graph_atlas_g
from boxlib import *
from multiprocessing import Pool
def Lof(G):
    if G.number_of_edges()==0: return 1
    n,S=B0_simplices(G)
    k,hk,sc,_=certified_conn(S)
    L=max(k+2,2)
    if not nx.is_bipartite(G): L=max(L,3)
    return L
def work(a):
    i,G=a
    nodes=list(G.nodes()); best=Lof(G); 
    for r in range(len(nodes)-1,1,-1):
        for sub in itertools.combinations(nodes,r):
            H=G.subgraph(sub)
            if H.number_of_edges()==0: continue
            if H.number_of_edges()<best*(best-1)//2 and best>=3: pass
            best=max(best,Lof(H))
    return i,best
if __name__=='__main__':
    res=json.load(open('atlas.json'))
    gs=list(enumerate(graph_atlas_g()))
    gs=[(r['i'],gs[r['i']][1]) for r in res if r['L']<r['chi']]
    with Pool(4) as p: out=dict(p.map(work,gs))
    still=[]
    for r in res:
        if r['i'] in out: r['L']=max(r['L'],out[r['i']])
        if r['L']<r['chi']: still.append(r)
    json.dump(res,open('atlas2.json','w'))
    print(len(still),collections.Counter((x['chi'],x['L'],x['h']) for x in still))
    print([ (x['i'],x['n'],x['m']) for x in still])
