# G**: G* plus, in every W copy t, an extra W glued in face (x,y,p) forbidding (x,y) again. Test FB+ (uni) and FB2 (ert); test P by transparency argument (no computation needed)
import sys
from common import *
from pysat.solvers import Cadical153
def gss():
    G=nx.complete_graph('abcd'); ms={}
    for t,o in {1:('a','b','c'),2:('b','d','a'),3:('c','d','a'),4:('b','c','d')}.items(): ms[t]=glue(G,o,t)
    ms[5]=glue(G,('a','c',ms[1]['q1']),5); ms[6]=glue(G,('d','a',ms[3]['q5']),6)
    for t in range(1,7): glue(G,(ms[t]['x'],ms[t]['y'],ms[t]['p']),10+t)
    return G
G=gss(); print('n',G.number_of_nodes(),'e',G.number_of_edges(),'planar',nx.check_planarity(G)[0])
V=list(G); idx={v:i+1 for i,v in enumerate(V)}; n=len(V)
for mode in ['uni','ert']:
    sol=Cadical153(); s_=lambda v: idx[v]; side=lambda v:n+idx[v]
    for u,w in G.edges():
        sol.add_clause([s_(u),s_(w),side(u),side(w)]); sol.add_clause([s_(u),s_(w),-side(u),-side(w)])
    for t in [c for c in nx.enumerate_all_cliques(G) if len(c)==3]: sol.add_clause([-s_(v) for v in t])
    it=0; res='NONE'
    while sol.solve():
        m=set(x for x in sol.get_model() if x>0); it+=1
        S=[v for v in V if s_(v) in m]; bad=bad_cores(G,S,mode)
        if not bad: res='FOUND'; break
        for X in bad: sol.add_clause([-s_(v) for v in X])
    print(mode,res,'iters',it)
