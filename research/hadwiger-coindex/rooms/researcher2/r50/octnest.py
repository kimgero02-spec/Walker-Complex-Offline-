# nested octahedron gadget: octahedron (outer xyz) with an octahedron glued into each of its 7 inner faces
from common import *
import wlist
OE=[('x','y'),('y','z'),('z','x'),('u','y'),('u','z'),('v','x'),('v','z'),('w','x'),('w','y'),('u','v'),('v','w'),('w','u')]
INNER=[('x','y','w'),('y','z','u'),('z','x','v'),('x','w','v'),('y','u','w'),('z','v','u'),('u','v','w')]
def octg(depth,G=None,outer=('x','y','z'),tag=''):
    if G is None: G=nx.Graph()
    m={'x':outer[0],'y':outer[1],'z':outer[2]}
    for k in 'uvw': m[k]=tag+k
    G.add_edges_from((m[a],m[b]) for a,b in OE)
    if depth>1:
        for i,f in enumerate(INNER): octg(depth-1,G,tuple(m[k] for k in f),tag+str(i))
    return G
g=octg(2); print('n',g.number_of_nodes(),'e',g.number_of_edges())
wlist.w=g; wlist.I=[v for v in g if v not in ('x','y','z')]
for k,(a,b,c) in wlist.reps.items():
    M,it=wlist.block({'x':a,'y':b,'z':c}); print(k,(a,b,c),'BLOCK' if M else '-',it, M if M else '')
