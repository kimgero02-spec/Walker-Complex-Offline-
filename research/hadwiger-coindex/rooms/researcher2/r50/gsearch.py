# find partition of G* : T induced bipartite, S induced with each component having <=1 cycle, which is even
from common import *
from pysat.solvers import Cadical153
G=gstar(); V=list(G); idx={v:i+1 for i,v in enumerate(V)}; n=len(V)
s_=lambda v: idx[v]          # true = v in S
side=lambda v: n+idx[v]      # bipartition side for T
sol=Cadical153()
for u,w in G.edges():
    # both in T -> different sides
    sol.add_clause([s_(u),s_(w),side(u),side(w)]); sol.add_clause([s_(u),s_(w),-side(u),-side(w)])
# triangles: not all S (odd cycle)
for t in [c for c in nx.enumerate_all_cliques(G) if len(c)==3]:
    sol.add_clause([-s_(v) for v in t])
it=0
while sol.solve():
    m=set(x for x in sol.get_model() if x>0); it+=1
    S=[v for v in V if s_(v) in m]
    bad=bad_cores(G,S,'uni')
    if not bad:
        T=[v for v in V if v not in S]
        assert nx.is_bipartite(G.subgraph(T))
        H=G.subgraph(S)
        print('FOUND after',it,'|S|=',len(S),'|T|=',len(T))
        for cc in nx.connected_components(H):
            C=H.subgraph(cc); print('  S-comp size',len(cc),'edges',C.number_of_edges(),'cycle' if C.number_of_edges()==len(cc) else 'tree', sorted(cc,key=str) if C.number_of_edges()==len(cc) else '')
        import pickle; pickle.dump(S,open('gstar_S.pkl','wb'))
        break
    for X in bad: sol.add_clause([-s_(v) for v in X])
else: print('NONE after',it)
