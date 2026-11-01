"""Moser spindle: planar? odd K3-chain? E-criterion (ind Hom(K2,G)<=1)?  Also explicit cyclic orientation t."""
import networkx as nx
from r05 import e_crit, tri_orient, four_cycles
from oddchain import odd_chain
from zlift import ind_le_1
M = nx.Graph([(0,1),(0,2),(1,2),(1,3),(2,3),(0,4),(0,5),(4,5),(4,6),(5,6),(3,6)])
print("chi>=4 check (no 3-col):", not any(all(c[u]!=c[v] for u,v in M.edges()) for c in
      [dict(zip(range(7),t)) for t in __import__('itertools').product(range(3),repeat=7)]))
print("planar:", nx.check_planarity(M)[0], "oddchain:", odd_chain(M,3), "E:", e_crit(M), "zlift:", ind_le_1(M))
print("4-cycles:", four_cycles(M))
