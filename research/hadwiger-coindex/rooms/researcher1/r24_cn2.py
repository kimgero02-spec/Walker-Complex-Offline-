# R24: 2-sheet planar test for circulants C_n^2 (small, guessing aid)
import networkx as nx, sys
from r22_check import two_sheet_planar, colourable
def cn2(n):
    G=nx.Graph(); G.add_nodes_from(range(n))
    for i in range(n):
        G.add_edge(i,(i+1)%n); G.add_edge(i,(i+2)%n)
    return G
for n in [8,9,10,11,12]:
    G=cn2(n)
    p=nx.check_planarity(G)[0]
    c3=colourable(G,3)
    part=two_sheet_planar(G)
    print("n=",n,"planar",p,"3-colourable",c3,"2-sheet partition",part)
    sys.stdout.flush()
