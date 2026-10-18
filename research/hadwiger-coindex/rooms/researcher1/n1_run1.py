import networkx as nx, time
from networkx.generators.atlas import graph_atlas_g
from n1_lib import *
t=time.time()
res=[]
for G in graph_atlas_g():
    n=G.number_of_nodes()
    if n<6 or n>7 or not nx.is_connected(G): continue
    cl=max(len(c) for c in nx.find_cliques(G))
    if cl>=4: continue
    # chi>=4 test
    from itertools import product
    def col3(G):
        nodes=list(G.nodes()); 
        for c in product(range(3),repeat=len(nodes)):
            if all(c[u]!=c[v] for u,v in G.edges()): return True
        return False
    if col3(G): continue
    pairs=maxbic(G)
    z,_=rho(G,pairs)
    print(n,G.number_of_edges(),"zig",z,len(pairs),flush=True)
    if z>=4:
        Y=search(n,[(bl(a),bl(b)) for a,b in pairs],iters=1500,restarts=20)
        print("  planar radon-free found:",Y is not None, sorted(G.edges()),flush=True)
print(time.time()-t)
