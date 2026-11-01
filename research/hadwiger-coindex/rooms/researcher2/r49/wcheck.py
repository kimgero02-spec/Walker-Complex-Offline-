# independent brute-force check of the W lemma (all 2^10 partitions, no SAT)
import networkx as nx, itertools
from gstar import W
w=W(); V=list(w); ok=[]
for bits in itertools.product([0,1],repeat=len(V)):
    F=[v for v,b in zip(V,bits) if b]; B=[v for v,b in zip(V,bits) if not b]
    H=w.subgraph(F)
    forest=(not F) or H.number_of_edges()==len(F)-nx.number_connected_components(H)
    if forest and nx.is_bipartite(w.subgraph(B)): ok.append(set(F))
print('FB partitions of W:',len(ok),' with x,y in F:',sum(1 for F in ok if 'x' in F and 'y' in F))
