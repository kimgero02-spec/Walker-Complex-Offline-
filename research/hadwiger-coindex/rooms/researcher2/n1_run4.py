import networkx as nx, time
from networkx.generators.atlas import graph_atlas_g
from n1_zig import zig_le
from n1_hom import hom_map
bad=[];cnt={}
t0=time.time()
for i,G in enumerate(graph_atlas_g()):
    if G.number_of_nodes()<4 or G.number_of_edges()==0: continue
    if not nx.is_connected(G): continue
    z=2
    while not zig_le(G,z): z+=1
    if z<4: continue
    # xi: smallest k with Hom->Q_k
    k=2
    while not hom_map(G,k)[0]: k+=1
    cnt[(z,k+1)]=cnt.get((z,k+1),0)+1
    if k+1!=z: bad.append((i,z,k+1))
print(cnt,bad,round(time.time()-t0,1))
