# Pi3 heuristic: try to write Mycielski M5 (23 v, chi 5, triangle-free) as B u T, B planar bipartite, T planar.
import networkx as nx, random, sys
from r19_lib import planar
G=nx.mycielski_graph(5)
print(G.number_of_nodes(),G.number_of_edges())
E=list(G.edges())
def attempt(seed):
    rnd=random.Random(seed)
    side={v:rnd.randint(0,1) for v in G}
    # local search: make G[X], G[Y] planar first
    def bad():
        return [s for s in (0,1) if not planar(G.subgraph([v for v in G if side[v]==s]))]
    for it in range(400):
        if not bad(): break
        v=rnd.choice(list(G)); side[v]^=1
        if len(bad())>0 and rnd.random()<0.7:
            pass
    if bad(): return None
    T=nx.Graph(); T.add_nodes_from(G)
    T.add_edges_from([e for e in E if side[e[0]]==side[e[1]]])
    B=nx.Graph(); B.add_nodes_from(G)
    cross=[e for e in E if side[e[0]]!=side[e[1]]]
    rnd.shuffle(cross); left=[]
    for e in cross:
        B.add_edge(*e)
        if not planar(B):
            B.remove_edge(*e); T.add_edge(*e)
            if not planar(T): T.remove_edge(*e); left.append(e)
    return len(left),B,T,side
best=None
for s in range(int(sys.argv[1]) if len(sys.argv)>1 else 300):
    r=attempt(s)
    if r is None: continue
    if best is None or r[0]<best[0]:
        best=r; print("seed",s,"uncovered",r[0]); sys.stdout.flush()
    if r[0]==0: break
if best and best[0]==0:
    B,T=best[1],best[2]
    print("FOUND. B bipartite:",nx.is_bipartite(B),"B planar",planar(B),"T planar",planar(T))
    print("B edges",sorted(B.edges())); print("T edges",sorted(T.edges()))
