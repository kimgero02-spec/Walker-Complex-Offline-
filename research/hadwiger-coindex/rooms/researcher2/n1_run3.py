import networkx as nx, time
from n1_zig import zig
from n1_hom import hom_map
def circ(n,ks):
    G=nx.Graph()
    for i in range(n):
        for k in ks: G.add_edge(i,(i+k)%n)
    return G
def blow(G,m):
    H=nx.Graph()
    for u,v in G.edges():
        for a in range(m):
            for b in range(m): H.add_edge((u,a),(v,b))
    for u in G.nodes():
        for a in range(m):
            for b in range(a+1,m): H.add_edge((u,a),(u,b))
    return H
moser=nx.Graph([(0,1),(0,2),(1,2),(1,3),(2,3),(0,4),(0,5),(4,5),(4,6),(5,6),(3,6)])
tests={'C8^2':circ(8,(1,2)),'C9^2':circ(9,(1,2)),'moser':moser,'C5[K2]':blow(nx.cycle_graph(5),2),'petersen':nx.petersen_graph()}
for name,G in tests.items():
    t=time.time(); z=zig(G); print(name,'n',G.number_of_nodes(),'zig',z,round(time.time()-t,1),flush=True)
    for k in range(2,z+1):
        t=time.time(); r,nf=hom_map(G,k); print('   Hom->Q_%d'%k,r,nf,round(time.time()-t,1),flush=True)
        if r: break
