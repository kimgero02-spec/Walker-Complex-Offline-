from r04_lib import *
P = nx.Graph()
P.add_edges_from([('a','b'),('b','c'),('a','c')])
ears = {'x':('b','c'),'y':('a','c'),'z':('a','b')}
for name in ['x1','x2','y1','y3','z2','z3']:
    for w in ears[name[0]]: P.add_edge(name, w)
for v, nb in [('p',['a','b','x1','y1']),('q',['a','c','x2','z2']),('r',['b','c','y3','z3'])]:
    for w in nb: P.add_edge(v, w)
T = [(x,y,z) for x in ['x1','x2'] for y in ['y1','y3'] for z in ['z2','z3']] + [('p','q','r')]
print('planar', nx.check_planarity(P)[0], 'chi', chi(P), all(indep(P,t) for t in T))
print('4col with constraints:', col_ok(P, T))
G = assemble(P, T); print('chi G', chi(G))
