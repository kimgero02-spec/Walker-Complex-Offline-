# K_7 = P u complement(P): find ONE non-rigid equality example (construction only)
import networkx as nx
from networkx.generators.atlas import graph_atlas_g
from r19_lib import *
found={}
for G in graph_atlas_g():
    if G.number_of_nodes()!=7: continue
    H=nx.complement(G)
    if not(planar(G) and planar(H)): continue
    a,b=chi(G),chi(H)
    if a+b!=7: continue
    wa,wb=omega(G),omega(H)
    key=((a,wa),(b,wb))
    if wa+wb<7 and key not in found:
        found[key]=sorted(G.edges())
for k,v in found.items(): print(k,v)
