# G*: partition T induced bipartite meeting every face + S induced, components with <=1 cycle (even) [mode uni] or ERT-2-choosable
import sys
from common import *
from pysat.solvers import Cadical153
sys.path.insert(0,'/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r49')
from tri import faces_of
G=gstar(); V=list(G); idx={v:i+1 for i,v in enumerate(V)}; n=len(V)
mode=sys.argv[1] if len(sys.argv)>1 else 'uni'
s_=lambda v: idx[v]; side=lambda v: n+idx[v]
sol=Cadical153()
for u,w in G.edges():
    sol.add_clause([s_(u),s_(w),side(u),side(w)]); sol.add_clause([s_(u),s_(w),-side(u),-side(w)])
F=[tuple(f) for f in faces_of(G)]; print('faces',len(F))
for f in F: sol.add_clause([-s_(v) for v in f])   # every face meets T
it=0
while sol.solve():
    m=set(x for x in sol.get_model() if x>0); it+=1
    S=[v for v in V if s_(v) in m]
    bad=bad_cores(G,S,mode)
    if not bad:
        H=G.subgraph(S); print('FOUND',it,[ (len(c),H.subgraph(c).number_of_edges()) for c in nx.connected_components(H)]); break
    for X in bad: sol.add_clause([-s_(v) for v in X])
else: print('NONE',it)
