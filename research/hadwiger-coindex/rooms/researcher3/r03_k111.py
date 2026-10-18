import networkx as nx
from r03_conv import Qd_search
for m in (2,3,4,5,6,7):
    G=nx.complete_multipartite_graph(1,1,1,*([1]*0)) 
    G=nx.Graph([(0,1),(0,2),(1,2)])
    for k in range(m): G.add_edges_from([(3+k,0),(3+k,1),(3+k,2)])
    print("K_{1,1,1,%d}"%m,"n=",3+m,"Q3:",Qd_search(G,3,100),flush=True)
