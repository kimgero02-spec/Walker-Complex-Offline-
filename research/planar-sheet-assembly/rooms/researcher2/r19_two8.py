# K_8 = P u complement(P), both planar: look for ONE non-rigid equality (sigma=8, sum omega<8)
import networkx as nx, itertools
from networkx.generators.atlas import graph_atlas_g
from r19_lib import *
base=[G for G in graph_atlas_g() if G.number_of_nodes()==7 and planar(G) and planar(nx.complement(G))]
print("7-vertex bases:",len(base))
found={}; sig=set()
for G in base:
    for m in range(128):
        H=G.copy(); H.add_node(7)
        for i in range(7):
            if m>>i&1: H.add_edge(i,7)
        C=nx.complement(H)
        if not(planar(H) and planar(C)): continue
        a,b=chi(H),chi(C); wa,wb=omega(H),omega(C)
        sig.add(a+b)
        if a+b==8 and wa+wb<8:
            key=((a,wa),(b,wb))
            if key not in found: found[key]=sorted(H.edges())
print("sigma values seen:",sorted(sig))
for k,v in found.items(): print(k,v)
