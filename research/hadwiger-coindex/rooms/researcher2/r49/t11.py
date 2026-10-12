import networkx as nx, itertools
from tri import dual,fb,faces_of
H=dual(nx.tutte_graph())
W=H.subgraph([0,1,8,4,9,10,11,12,13,23]).copy()
print(W.number_of_nodes(),W.number_of_edges(),'tri?',W.number_of_edges()==3*10-6)
print(sorted(W.edges()))
print('deg',dict(W.degree()))
for P in itertools.product('FB',repeat=3):
    if len(set(P))>1: print('outer (0,1,8)=',P, 'extendable' if fb(W,dict(zip((0,1,8),P))) else 'NOT')
