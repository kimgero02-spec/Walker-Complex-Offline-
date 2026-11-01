# K2: any two vertices with prescribed statuses -> FB?  (search for one decisive counterexample)
import networkx as nx, itertools, sys
from tri import fb,dual
exec(open('t6.py').read().split('print(G.number_of_nodes()')[0])
cands=[('oct',nx.octahedral_graph()),('ico',nx.icosahedral_graph()),('g13',G),('tutte*',dual(nx.tutte_graph()))]
for name,H in cands:
    bad=[]
    for u,w in itertools.combinations(H,2):
        for X,Y in itertools.product('FB',repeat=2):
            if fb(H,{u:X,w:Y}) is None: bad.append((u,w,X,Y,H.has_edge(u,w)))
    print(name,len(bad),bad[:8]); sys.stdout.flush()
