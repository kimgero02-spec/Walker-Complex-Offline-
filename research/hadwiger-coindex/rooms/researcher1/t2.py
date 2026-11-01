import networkx as nx, time
from networkx.generators.atlas import graph_atlas_g
from boxlib import *
A=graph_atlas_g()
for i in (878,998,1002,1101,1170):
    G=A[i]; t=time.time()
    r=sw_height(G,join=True,maxchains=2500000)
    print(i,sorted(G.edges()),'SW',r,round(time.time()-t,1),flush=True)
for n in (2,3,4):
    print('K',n,sw_height(nx.complete_graph(n),join=True), 'C5',sw_height(nx.cycle_graph(5)) if n==2 else '')
