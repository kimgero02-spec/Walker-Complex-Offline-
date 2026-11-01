import networkx as nx, time
from n1_zig import zig_le
def circ(n,ks):
    G=nx.Graph(); G.add_nodes_from(range(n))
    for i in range(n):
        for k in ks: G.add_edge(i,(i+k)%n)
    return G
for n in range(9,15):
    G=circ(n,(1,2,3)); t=time.time()
    z=2
    while not zig_le(G,z): z+=1
    # chi lower: ceil(n/alpha)
    print('C_%d^3'%n,'omega',4,'zig',z,round(time.time()-t,1),flush=True)
