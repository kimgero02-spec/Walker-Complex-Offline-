import networkx as nx, itertools
from r19_lib import *
lab={0:(0,0),1:(0,0),2:(0,1),3:(0,1),4:(1,0),5:(1,0),6:(1,1)}
C=nx.cycle_graph(7)
both=[(u,v) for u,v in itertools.combinations(range(7),2) if not C.has_edge(u,v) and lab[u][0]!=lab[v][0] and lab[u][1]!=lab[v][1]]
for m in range(2**len(both)):
    B1=nx.Graph(); B2=nx.Graph()
    for u,v in itertools.combinations(range(7),2):
        if C.has_edge(u,v): continue
        if (u,v) in both: (B1 if m>>both.index((u,v))&1 else B2).add_edge(u,v)
        elif lab[u][0]!=lab[v][0]: B1.add_edge(u,v)
        else: B2.add_edge(u,v)
    if planar(B1) and planar(B2):
        report(7,[C,B1,B2],"K7 C7uB1uB2"); print(sorted(B1.edges()),sorted(B2.edges())); break
