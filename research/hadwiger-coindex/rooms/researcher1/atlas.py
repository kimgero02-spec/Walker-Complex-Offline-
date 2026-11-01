import networkx as nx, itertools, json, sys
from networkx.generators.atlas import graph_atlas_g
from multiprocessing import Pool
from boxlib import *
def chrom(G):
    n=G.number_of_nodes()
    if G.number_of_edges()==0: return 1
    for k in range(1,n+1):
        nodes=list(G.nodes())
        # backtracking
        col={}
        order=sorted(nodes,key=lambda v:-G.degree(v))
        def bt(i,m):
            if i==len(order): return True
            v=order[i]
            for c in range(min(m+1,k)):
                if all(col.get(u)!=c for u in G[v]):
                    col[v]=c
                    if bt(i+1,max(m,c+1)): return True
                    del col[v]
            return False
        if bt(0,0): return k
def work(i_G):
    i,G=i_G
    chi=chrom(G); h,ex=hadwiger_number(G)
    n,S=B0_simplices(G)
    k,hk,sc,_=certified_conn(S)
    # coind>=k+1 -> tau>=k+2 ; (if k<0 : complex disconnected/empty -> coind>=0 -> tau>=1)
    L=max(k+2,1) if k>=0 else 1
    # G with edge: coind>=1
    if G.number_of_edges()>0: L=max(L,2)
    return dict(i=i,n=G.number_of_nodes(),m=G.number_of_edges(),chi=chi,h=h,exact=ex,L=L,hk=hk,sc=sc)
if __name__=='__main__':
    gs=[(i,G) for i,G in enumerate(graph_atlas_g()) if G.number_of_nodes()>=1]
    with Pool(4) as p: res=p.map(work,gs,chunksize=8)
    json.dump(res,open('atlas.json','w'))
    print(len(res))
    print('not exact h:',sum(not r['exact'] for r in res))
    print('L>chi:',[r['i'] for r in res if r['L']>r['chi']])
    print('chi>h:',[r['i'] for r in res if r['chi']>r['h']])
    gap=[r for r in res if r['L']<r['chi']]
    print('L<chi:',len(gap))
    for r in gap: print(r)
    print('L>h:',[r['i'] for r in res if r['L']>r['h']])
