# R16: look for planar x giving chi=b+2 in Theta* (x+triangle) / 8* (x+2 disjoint edges); example finding only
import networkx as nx, itertools
from networkx.algorithms import isomorphism
def chi(G):
    n=G.number_of_nodes(); nodes=list(G); 
    for k in range(1,n+1):
        col={}
        def bt(i):
            if i==n: return True
            v=nodes[i]
            for c in range(k):
                if all(col.get(u)!=c for u in G[v]):
                    col[v]=c
                    if bt(i+1): return True
                    del col[v]
            return False
        if bt(0): return k
def hasK(G,k):
    return any(all(G.has_edge(a,b) for a,b in itertools.combinations(S,2)) for S in itertools.combinations(G,k))
if __name__!="__main__": raise SystemExit
res={'T':[], '8':[]}
for x in nx.graph_atlas_g()[1:]:
    if x.number_of_nodes()<3 or not nx.is_connected(x) or not nx.check_planarity(x)[0]: continue
    cx=chi(x)
    for H in itertools.combinations(x.nodes(),3):
        b=max(cx,3); y=x.copy(); y.add_edges_from(itertools.combinations(H,2))
        if chi(y)>=b+2: res['T'].append((cx,x.number_of_nodes(),x.number_of_edges(),hasK(y,b+2)))
    for a in itertools.permutations(x.nodes(),4):
        if a[0]>a[1] or a[2]>a[3] or a[0]>a[2]: continue
        b=max(cx,2); y=x.copy(); y.add_edges_from([(a[0],a[1]),(a[2],a[3])])
        if chi(y)>=b+2: res['8'].append((cx,x.number_of_nodes(),x.number_of_edges(),hasK(y,b+2)))
for k,v in res.items():
    print(k,len(v),sorted(set(v)))
