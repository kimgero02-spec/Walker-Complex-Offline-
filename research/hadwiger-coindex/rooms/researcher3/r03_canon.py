import numpy as np, networkx as nx, itertools
from scipy.spatial import Delaunay
from networkx.algorithms.planar_drawing import triangulate_embedding, get_canonical_ordering
def pair_violations(G,order):
    pos={v:i for i,v in enumerate(order)}; bad=[]
    for a,b in itertools.combinations(G.nodes(),2):
        C=set(G[a])&set(G[b]); lo,hi=sorted((pos[a],pos[b]))
        if len(C)<3: continue
        z=set(0 if pos[c]<lo else (1 if pos[c]<hi else 2) for c in C)
        if len(z)==3: bad.append((a,b))
    return bad
def tri_graph(seed,n):
    rng=np.random.default_rng(seed); P=rng.random((n,2)); T=Delaunay(P)
    G=nx.Graph()
    for s in T.simplices: G.add_edges_from([(int(s[0]),int(s[1])),(int(s[1]),int(s[2])),(int(s[0]),int(s[2]))])
    return G
for n,seed in [(14,0),(20,1),(30,2),(40,3),(60,4)]:
    G=tri_graph(seed,n); ok,emb=nx.check_planarity(G)
    emb2,outer=triangulate_embedding(emb,True)
    co=get_canonical_ordering(emb2,outer)
    order=[c[0] for c in co]
    G2=nx.Graph(emb2.edges())
    # compare: canonical order vs sorted-by-degeneracy vs BFS
    deg=[]; H=G2.copy()
    while H.number_of_nodes():
        v=min(H.nodes(),key=H.degree); deg.append(v); H.remove_node(v)
    print(n,seed,"|V|",G2.number_of_nodes(),"canonical viol",len(pair_violations(G2,order)),"degeneracy-reverse viol",len(pair_violations(G2,deg[::-1])),"BFS viol",len(pair_violations(G2,list(nx.bfs_tree(G2,order[0])))),flush=True)
