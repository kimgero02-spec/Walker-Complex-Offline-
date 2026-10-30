import networkx as nx
from fb import fb
from fam2 import bipyr, capped_antiprism
for name,G in [("ico",nx.icosahedral_graph()),("capAP6",capped_antiprism(6)),("dodeca-dual-ico",nx.icosahedral_graph())]:
    print(name,fb(G))
