# R23: 7-vertex gap graphs from networkx atlas (all graphs <=7 nodes), filter chi=4, omega<=3, zig<=3
import itertools, networkx as nx
from networkx.generators.atlas import graph_atlas_g
from r22_ext import zig_le3, omega
from r22_check import colourable, two_sheet_planar
gaps=[]
for G in graph_atlas_g():
    if G.number_of_nodes()!=7: continue
    if not nx.is_connected(G): continue
    if omega(G)>3: continue
    if colourable(G,3): continue
    ok,_=zig_le3(G)
    if ok: gaps.append(G)
print("connected 7-vertex graphs with chi=4, omega<=3, zig<=3:", len(gaps))
for i,G in enumerate(gaps):
    print(i, "edges",G.number_of_edges(), "degrees",sorted(d for _,d in G.degree()), "2-sheet partition", two_sheet_planar(G) is not None)
import pickle; pickle.dump(gaps, open('r23_gaps7.pkl','wb'))
