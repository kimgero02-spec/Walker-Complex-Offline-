import networkx as nx
from r17_hM import has_minor
C=nx.circulant_graph(7,[1,3]); print('planar',nx.check_planarity(C)[0])
for N in (5,6): print(N, bool(has_minor(C,nx.complete_graph(N),maxset=3)))
