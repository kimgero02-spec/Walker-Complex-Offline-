import networkx as nx, itertools, time
from networkx.generators.atlas import graph_atlas_g
def c4s(G):
    # list of 4-tuples-as-cycles: all (x1,x2,x3,x4) vertex sets with a cyclic 4-cycle labelling; for order check enumerate 4-sets and 3 pairings
    A={v:set(G[v]) for v in G}
    out=[]
    for S in itertools.combinations(sorted(G),4):
        a,b,c,d=S
        for (p,q),(r,s) in (((a,c),(b,d)),((a,b),(c,d)),((a,d),(b,c))):
            if all(y in A[x] for x in (p,q) for y in (r,s)): out.append(((p,q),(r,s)))
    return out
def q2(G):
    C=c4s(G); n=G.number_of_nodes()
    nodes=sorted(G)
    for perm in itertools.permutations(nodes):
        pos={v:i for i,v in enumerate(perm)}
        ok=True
        for (p,q),(r,s) in C:
            # alternate in order?
            L=sorted([(pos[p],0),(pos[q],0),(pos[r],1),(pos[s],1)])
            if [x[1] for x in L] in ([0,1,0,1],[1,0,1,0]): ok=False;break
        if ok: return perm
    return None
t=time.time(); bad=[]
for i,G in enumerate(graph_atlas_g()):
    n=G.number_of_nodes()
    if n<4 or not nx.is_connected(G): continue
    if max(len(c) for c in nx.find_cliques(G))>=4: continue
    if q2(G) is None: bad.append((i,n,G.number_of_edges()))
print(len(bad),bad[:20],time.time()-t)
