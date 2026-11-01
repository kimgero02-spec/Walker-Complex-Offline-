from r48_at import *
import networkx as nx, itertools, collections
ico=nx.icosahedral_graph(); Ei=list(ico.edges())
st=collections.defaultdict(lambda:[0,0])
for T in itertools.combinations(range(12),6):
    t=[2 if v in T else 3 for v in range(12)]
    c=coef(12,Ei,t)
    eT=ico.subgraph(T).number_of_edges()
    st[eT][0 if c==0 else 1]+=1
print('edges inside T(t=2): [zero, nonzero]',dict(st))
