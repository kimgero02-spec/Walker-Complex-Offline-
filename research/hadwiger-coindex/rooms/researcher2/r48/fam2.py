import networkx as nx, sys, time
from cegar import cegar
def bipyr(m):
    G=nx.cycle_graph(m)
    for v in range(m): G.add_edge(m,v); G.add_edge(m+1,v)
    return G
def capped_antiprism(m):
    G=nx.Graph()
    for i in range(m):
        G.add_edge(i,(i+1)%m); G.add_edge(m+i,m+(i+1)%m)
        G.add_edge(i,m+i); G.add_edge(i,m+(i+1)%m)
        G.add_edge(2*m,i); G.add_edge(2*m+1,m+i)
    return G
if __name__=="__main__":
 for name,G in [("bipyr5",bipyr(5)),("bipyr7",bipyr(7)),("capAP4",capped_antiprism(4)),("capAP5",capped_antiprism(5)),("capAP6",capped_antiprism(6))]:
  assert nx.check_planarity(G)[0]
  t=time.time(); r=cegar(G,fix={0:(1,2)}); print(name,G.number_of_nodes(),r,round(time.time()-t,1),flush=True)
