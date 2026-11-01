# find a SMALL triangulation with a 4-coloring in which all six Kempe subgraphs contain a cycle (=> all disconnected)
import networkx as nx, itertools, random
from t3 import colorings
def flip_random(G,emb_faces,rng):
    pass
def tri_from_flips(n,steps,rng):
    # start: double wheel (bipyramid) over C_{n-2}, random flips keep triangulation
    G=nx.Graph(); m=n-2
    for i in range(m): G.add_edge(i,(i+1)%m); G.add_edge(i,'N'); G.add_edge(i,'S')
    G=nx.convert_node_labels_to_integers(G)
    for _ in range(steps):
        u,v=rng.choice(list(G.edges()))
        com=[w for w in G[u] if w in G[v]]
        # in triangulation, edge uv lies in exactly two faces; with separating triangles common nbrs >2: skip
        if len(com)!=2: continue
        a,b=com
        if G.has_edge(a,b) or G.degree(u)<=3 or G.degree(v)<=3: continue
        G.remove_edge(u,v); G.add_edge(a,b)
    assert nx.check_planarity(G)[0] and G.number_of_edges()==3*n-6
    return G
def cyc_all(G,c):
    return all(not nx.is_forest(G.subgraph([v for v in G if c[v] in p])) for p in itertools.combinations(range(4),2))
if __name__=="__main__":
  rng=random.Random(1)
  best=None
  for n in range(15,23):
      for trial in range(60):
          G=tri_from_flips(n,60,rng)
          for c in colorings(G):
              if cyc_all(G,c): best=(n,G,c); break
          if best: break
      if best: break
  n,G,c=best
  print(n,sorted(G.edges()),c)
  nx.write_edgelist(G,'small_allcyc.edgelist',data=False)
  