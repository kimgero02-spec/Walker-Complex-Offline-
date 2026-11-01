import networkx as nx, random
from radon import *
random.seed(5)
def rand_planar_tri(n):
    G=nx.complete_graph(3); faces=[(0,1,2),(0,1,2)]
    for v in range(3,n):
        f=faces.pop(random.randrange(len(faces))); a,b,c=f
        G.add_edges_from([(v,a),(v,b),(v,c)]); faces+= [(a,b,v),(b,c,v),(a,c,v)]
    return G
for n in (7,8,9):
  for k in range(4):
    G=rand_planar_tri(n)
    assert nx.check_planarity(G)[0]
    Y,s,_=search(G,3,iters=200,seed=k)
    print("planar tri n",n,"d=3","found" if Y is not None else "none",flush=True)
# outerplanar: triangulated polygon
for n in (6,8):
    G=nx.cycle_graph(n); 
    for i in range(2,n-1): G.add_edge(0,i)
    Y,s,_=search(G,2,iters=200)
    print("outerplanar fan n",n,"d=2","found" if Y is not None else "none",flush=True)
