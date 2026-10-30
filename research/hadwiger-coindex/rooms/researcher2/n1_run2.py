import networkx as nx, time
from n1_hom import hom_map
tests={'K3':nx.complete_graph(3),'K4':nx.complete_graph(4),'C5':nx.cycle_graph(5),'W5':nx.wheel_graph(6),'co-C7':nx.complement(nx.cycle_graph(7))}
for name,G in tests.items():
    for k in (2,3,4):
        t=time.time(); r,nf=hom_map(G,k); print(name,'Hom->Q_%d'%k,r,nf,round(time.time()-t,1),flush=True)
