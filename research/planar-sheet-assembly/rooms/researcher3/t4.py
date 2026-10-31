import sys, io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import ex6
from t3 import seppairs
import networkx as nx
G=ex6.Mn.G; print(G.number_of_nodes(),G.number_of_edges(),nx.check_planarity(G)[0])
for p,c in seppairs(G): print(p,[x for x in c if len(x)<6])
