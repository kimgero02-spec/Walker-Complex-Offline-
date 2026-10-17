import networkx as nx, itertools
from r07_chi import chi, gluing_sat, profile_sat, min_q, colorings

def comp(*Ps): return nx.compose_all(Ps)

pieces = {}
# K4 = K4-uv + K2(uv), S={u,v}
K4m = nx.Graph([('u','x'),('u','y'),('v','x'),('v','y'),('x','y')])
K2 = nx.Graph([('u','v')])
G = comp(K4m, K2); print('K4 chi', chi(G), 'planar pieces', nx.check_planarity(K4m)[0], nx.check_planarity(K2)[0])
print('  profile min q:', min_q(lambda q: profile_sat(['u','v'], [K4m,K2], q), 6))
# K4 = two 4-cycles of textbook example 1.3, S = all vertices
C4a = nx.Graph([(0,1),(1,3),(3,2),(2,0)]); C4b = nx.Graph([(0,3),(3,1),(1,2),(2,0)])
G = comp(C4a,C4b); print('K4 (2 squares) chi', chi(G), 'glue min q', min_q(lambda q: gluing_sat(G.nodes(), [C4a,C4b], q), 5))

# K5 = K_{1,1,3} + K3 on {a,b,c}, S={a,b,c}
K113 = nx.Graph([('d','e')]+[(h,s) for h in 'de' for s in 'abc'])
K3 = nx.complete_graph('abc')
G = comp(K113,K3); print('K5 chi', chi(G), 'profile min q', min_q(lambda q: profile_sat(list('abc'), [K113,K3], q), 6))
# K5 = two pentagons (textbook 1.5 style), S = all vertices
C5a = nx.cycle_graph(range(5)); C5b = nx.Graph([(i,(i+2)%5) for i in range(5)])
G = comp(C5a,C5b); print('K5 (2 pentagons) chi', chi(G), 'profile(S=V) min q', min_q(lambda q: profile_sat(range(5), [C5a,C5b], q), 6))

# C3 = path 1-2-3 + edge 13, S={1,3}
Pp = nx.Graph([(1,2),(2,3)]); E13 = nx.Graph([(1,3)])
G = comp(Pp,E13); print('C3 chi', chi(G), 'profile min q', min_q(lambda q: profile_sat([1,3],[Pp,E13],q), 5))
# C4 = path 1-2-3 + path 3-4-1, S={1,3}
Pa = nx.Graph([(1,2),(2,3)]); Pb = nx.Graph([(3,4),(4,1)])
G = comp(Pa,Pb); print('C4 chi', chi(G), 'profile min q', min_q(lambda q: profile_sat([1,3],[Pa,Pb],q), 5))

# K3,3 = C6 + 3 matching edges (multi-piece, all share the 6 vertices)
C6 = nx.cycle_graph([('a',1),('b',1),('a',2),('b',2),('a',3),('b',3)])
M = nx.Graph([(('a',1),('b',2)),(('a',2),('b',3)),(('a',3),('b',1))])
pcs=[C6]+[nx.Graph([e]) for e in M.edges()]
G = comp(*pcs); print('K3,3 chi', chi(G), 'K33 edges', G.number_of_edges(), 'nonplanar', not nx.check_planarity(G)[0],
      'pieces planar', all(nx.check_planarity(P)[0] for P in pcs))
print('  gluing min q (fiber labels):', min_q(lambda q: gluing_sat(G.nodes(), pcs, q), 3))

# contraction lemma: chi(C4/{1,4}) vs identification in C4-14 with c1=c4
C4 = nx.cycle_graph([1,2,3,4])
C4_14 = C4.copy(); C4_14.remove_edge(1,4)
def ident_sat(q):
    for c in colorings(C4_14,q):
        if c[1]==c[4]: return True
    return False
print('C4/14 identification min q', min_q(ident_sat,5), '; chi(C3)=', chi(nx.complete_graph(3)), 'chi(C4)=', chi(C4))
