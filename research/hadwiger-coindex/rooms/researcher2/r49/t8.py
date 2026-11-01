import networkx as nx, itertools
from tri import fb,dual,faces_of
H=dual(nx.tutte_graph())
print('deg',dict(H.degree()))
for u in H:
    r=[X for X in 'FB' if fb(H,{u:X}) is None]
    if r: print('vertex',u,'deg',H.degree(u),'cannot be',r)
bad=[]
for f in faces_of(H):
    for P in itertools.product('FB',repeat=3):
        if len(set(P))>1 and fb(H,dict(zip(f,P))) is None: bad.append((f,P))
print('face-pattern failures',len(bad),bad[:10])
