import networkx as nx, itertools
from tri import *
def kplus(G,name):
    bad=[]
    for f in faces_of(G):
        for P in itertools.product('FB',repeat=3):
            if len(set(P))==1: continue
            if fb(G,dict(zip(f,P))) is None: bad.append((f,P))
    print(name,'faces',len(faces_of(G)),'bad patterns',bad[:6],len(bad))
kplus(nx.octahedral_graph(),'oct')
kplus(nx.icosahedral_graph(),'ico')
