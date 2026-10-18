import networkx as nx, time
from b0lib import *
G=nx.lexicographic_product(nx.cycle_graph(5),nx.complete_graph(2))
G=nx.convert_node_labels_to_integers(G)
t=time.time();S,n=b0_simplices(G);print(n,len(S),time.time()-t)
b=reduced_betti(S);print(b,"tau_h=",tau_h(G),time.time()-t)
