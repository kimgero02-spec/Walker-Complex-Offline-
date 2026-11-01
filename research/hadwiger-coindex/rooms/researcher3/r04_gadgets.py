# K3-sum forcing test on 8 explicit gadgets, ALL triangles, all 6 (middle, side) T-block profiles, plus T-last / T-first
from r04_lib import *
from r04_mid import allt
from r04_prof import profiles
from r04_tend import tend
def nested(k):
    G=nx.Graph(); 
    for l in range(k):
        for i in range(3): G.add_edge((l,i),(l,(i+1)%3))
    for l in range(k-1):
        for i in range(3):
            G.add_edge((l,i),(l+1,i)); G.add_edge((l,i),(l+1,(i+1)%3))
    return G
def bip(m):
    G=nx.cycle_graph(m); G.add_edges_from(("N",i) for i in range(m)); G.add_edges_from(("S",i) for i in range(m)); return G
n7=nx.Graph([(0,1),(0,2),(0,3),(0,5),(0,6),(1,2),(1,3),(1,4),(1,5),(1,6),(2,3),(2,4),(2,5),(3,4),(3,6)])
K1112=nx.complete_multipartite_graph(1,1,1,2)
gad=[("K1112",K1112),("octahedron",nx.octahedral_graph()),("icosahedron",nx.icosahedral_graph()),("bipyr7",bip(7)),("n7",n7),
     ("nested3",nested(3)),("nested4+poles",None),("apollonian12",stacked(5,12))]
G4=nested(4); G4.add_edges_from(("P",(0,i)) for i in range(3)); G4.add_edges_from(("Q",(3,i)) for i in range(3)); gad[6]=("nested4+poles",G4)
for name,G in gad:
    G=nx.convert_node_labels_to_integers(G)
    ok,_=nx.check_planarity(G); ts=allt(G)
    noblock=0; onlyone=0; tl=0
    for T in ts:
        P=profiles(G,T)
        noblock+=sum(1 for m in T if not (P[(m,'before')] or P[(m,'after')]))
        for m in T:
            if P[(m,"before")]!=P[(m,"after")]: onlyone+=1
        tl+= (not tend(G,T))
    print(name,"n",G.number_of_nodes(),"planar",ok,"triangles",len(ts),"| (T,m) lacking any T-block order:",noblock,"| (T,m) with one side only:",onlyone,"| triangles with NO T-last order:",tl,flush=True)
