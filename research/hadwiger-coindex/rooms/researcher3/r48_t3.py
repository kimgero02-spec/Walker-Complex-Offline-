# AT(icosahedron) <= 4 ? : t in {2,3}, 여섯 개가 2. (AT 판정 한 건)
from r48_at import *
import networkx as nx, itertools, time
ico=nx.icosahedral_graph(); Ei=list(ico.edges())
nz=[];t0=time.time()
for T in itertools.combinations(range(12),6):
    t=[2 if v in T else 3 for v in range(12)]
    c=coef(12,Ei,t)
    if c: nz.append((T,c))
print('nonzero patterns',len(nz),nz[:5],time.time()-t0)
