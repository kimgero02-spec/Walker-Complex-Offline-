# look for a SMALL triangulation where some single-vertex status is forced (K1v fails) -- one decisive example
import networkx as nx, random
from tri import fb
from t4 import tri_from_flips
rng=random.Random(7); found=None
for n in range(7,17):
    for trial in range(150):
        G=tri_from_flips(n,80,rng)
        for u in G:
            for X in 'FB':
                if fb(G,{u:X}) is None: found=(n,u,X,G); break
            if found: break
        if found: break
    if found: break
if found:
    n,u,X,G=found; print(n,u,'cannot be',X,dict(G.degree()),sorted(G.edges()))
    nx.write_edgelist(G,'k1v_small.edgelist',data=False)
else: print('none')
