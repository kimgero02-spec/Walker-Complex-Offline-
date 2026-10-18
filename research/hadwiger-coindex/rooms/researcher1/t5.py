from networkx.generators.atlas import graph_atlas_g
from sw2 import *
A=graph_atlas_g()
for i in (878,998,1002,1101,1170):
    nv,S,g=direct_B0_model(A[i]); print(i,'direct B0',sw_height_tuples(nv,S,g,kmax=3,verbose=False),flush=True)
