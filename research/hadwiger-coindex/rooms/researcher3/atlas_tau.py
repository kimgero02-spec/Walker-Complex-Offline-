import networkx as nx, pickle, time
from networkx.generators.atlas import graph_atlas_g
from b0lib import tau_h
t0=time.time()
res=[]
for i,G in enumerate(graph_atlas_g()):
    if G.number_of_nodes()==0: continue
    res.append((i,tau_h(G)))
pickle.dump(res,open('atlas_tau.pkl','wb'))
print(len(res),time.time()-t0)
