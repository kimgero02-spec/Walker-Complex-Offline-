import random, sys
import networkx as nx
from r20_frozen import planar, random_triangulation, movable
def run(N, seed, iters):
    rng = random.Random(seed)
    T1 = random_triangulation(N, rng); T2 = random_triangulation(N, rng)
    perm = list(range(N)); rng.shuffle(perm)
    T2 = nx.relabel_nodes(T2, dict(enumerate(perm)))
    G = nx.Graph(); G.add_edges_from(T1.edges()); G.add_edges_from(T2.edges())
    E = [tuple(sorted(e)) for e in G.edges()]
    col = {}; cls=[[],[],[]]
    for e in rng.sample(E,len(E)):
        for j in rng.sample([0,1,2],3):
            if planar(cls[j]+[e]): cls[j].append(e); col[e]=j; break
    cur = movable(E,col); best=cur
    for it in range(iters):
        e = rng.choice(E); j = rng.choice([x for x in range(3) if x!=col[e]])
        if not planar([x for x in E if col[x]==j]+[e]): continue
        old=col[e]; col[e]=j
        if all(col[x]!=old for x in E): col[e]=old; continue
        m=movable(E,col)
        if m<=cur or rng.random()<0.05: cur=m; best=min(best,m)
        else: col[e]=old
    return len(E), best
N=int(sys.argv[1])
for s in range(3): print(N, s, run(N,s,int(sys.argv[2])))
