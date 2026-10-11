import networkx as nx
from networkx.generators.atlas import graph_atlas_g
from networkx.algorithms import isomorphism as iso
W=nx.wheel_graph(6)
atlas=graph_atlas_g()
for i in [187,775,777,951,968,974,1005,1079,1095,1097,1104,1167,1212]:
    G=atlas[i]
    print(i, iso.GraphMatcher(G,W).subgraph_is_monomorphic())
