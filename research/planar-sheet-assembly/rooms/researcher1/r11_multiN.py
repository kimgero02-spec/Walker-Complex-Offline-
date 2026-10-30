# search for ONE graph whose realizations give two different N (example-finding only)
import networkx as nx
from networkx.generators.atlas import graph_atlas_g
from r11_inverse import realize
for G in graph_atlas_g()[1:]:
    if not nx.is_connected(G): continue
    for mode in ('circ','full'):
        Ns = {N for (W,N,n,a,g) in realize(G,mode)}
        if len(Ns) >= 2:
            print(mode, G.number_of_nodes(), sorted(G.edges()), Ns); raise SystemExit
print('none up to 7 vertices')
