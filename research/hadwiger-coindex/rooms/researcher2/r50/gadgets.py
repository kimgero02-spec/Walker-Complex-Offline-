# blockable outer precoloring classes for triangle gadgets (outer face x,y,z)
from common import *
import wlist
from pysat.solvers import Cadical153
reps=wlist.reps
def analyze(g,name):
    wlist.w=g; wlist.I=[v for v in g if v not in 'xyz']
    res={}
    for k,(a,b,c) in reps.items():
        M,it=wlist.block({'x':a,'y':b,'z':c}); res[k]=M
    print(name,'n=',g.number_of_nodes(),{k:('BLOCK' if M else '-') for k,M in res.items()})
    for k,M in res.items():
        if M: print('   ',k,reps[k],M)
oct_=nx.Graph([('x','y'),('y','z'),('z','x'),('u','y'),('u','z'),('v','x'),('v','z'),('w','x'),('w','y'),('u','v'),('v','w'),('w','u')])
analyze(oct_,'octahedron')
ico=nx.icosahedral_graph(); t=[0,1,5]; assert all(ico.has_edge(a,b) for a,b in itertools.combinations(t,2))
ico=nx.relabel_nodes(ico,lambda v:{0:"x",1:"y",5:"z"}.get(v,"i%d"%v)); analyze(ico,'icosahedron')
