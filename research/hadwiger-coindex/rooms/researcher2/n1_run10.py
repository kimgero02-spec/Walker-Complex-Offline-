import networkx as nx
from n1_zig import zig_le
from n1_rho import maxbicl, runs
from n1_homZ import circ
for n in (9,10,11,12,13):
    G=circ(n,(1,2,3))
    z=2
    while True:
        r,o=zig_le(G,z,True)
        if r: break
        z+=1
    P=maxbicl(G); pos={v:i for i,v in enumerate(o)}
    mr=max(runs(o,pos,A,B) for A,B in P)
    alpha=max(len(c) for c in nx.find_cliques(nx.complement(G)))
    print('C_%d^3'%n,'zig',z,'order',o,'max runs over',len(P),'maximal bicliques =',mr,'alpha',alpha,'chi>=',-(-n//alpha),flush=True)
