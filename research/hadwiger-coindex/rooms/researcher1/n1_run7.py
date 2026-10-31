import networkx as nx, time
from n1_lib2 import *
from n1_run4 import poset, chains, betti
from n1_bock import *
def Cn2(n):
    G=nx.Graph(); G.add_nodes_from(range(n))
    for i in range(n):
        G.add_edge(i,(i+1)%n); G.add_edge(i,(i+2)%n)
    return G
for n in [8,10,11]:
    G=Cn2(n); pairs=maxbic(G); P=poset(pairs); ch=chains(P)
    t=time.time()
    z=zig(n,pairs)
    print(n,"pairs",len(pairs),"ell",len(ch),"zig",z,"betti",betti(ch),"bockstein0",bockstein_zero(P,ch),time.time()-t,flush=True)
