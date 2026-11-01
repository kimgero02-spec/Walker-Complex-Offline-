import networkx as nx, time, itertools, sys
from n1_lib2 import *
from n1_run4 import poset, chains
from n1_bock import *
def test(name,G,doz=True):
    G=nx.convert_node_labels_to_integers(G); n=G.number_of_nodes()
    pairs=maxbic(G); P=poset(pairs); ch=chains(P)
    b=bockstein_zero(P,ch)
    z=zig(n,pairs) if doz else None
    print(name,n,"ell",len(ch),"zig",z,"tau<=3(bockstein0)",b,flush=True)
test("Groetzsch",nx.mycielski_graph(4))
test("Mycielski(C5)=Groetzsch check",nx.mycielskian(nx.cycle_graph(5)))
test("Petersen",nx.petersen_graph())
for n in range(7,14):
    for S in itertools.combinations(range(1,n//2+1),2):
        G=nx.circulant_graph(n,list(S))
        if nx.is_connected(G):
            pairs=maxbic(G)
            ch=chains(poset(pairs))
            z=zig(n,pairs)
            if z>=4: test(f"circ{n}{S}",G)
