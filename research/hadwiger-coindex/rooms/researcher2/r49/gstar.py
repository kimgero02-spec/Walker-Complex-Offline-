# Counterexample construction to Conjecture K.
# W = 10-vertex triangulation (dual of Tutte fragment), outer face (x,y,z); FB of W never has x,y both in F.
import networkx as nx, itertools
from tri import fb, is_fb, faces_of
WE=[('x','y'),('x','p'),('x','z'),('x','q1'),('x','q2'),('x','q3'),('y','p'),('y','z'),('y','q4'),('y','q5'),
    ('p','q3'),('p','q4'),('z','q1'),('z','q5'),('q1','q2'),('q1','q5'),('q1','c'),('q2','q3'),('q2','c'),
    ('q3','q4'),('q3','c'),('q4','q5'),('q4','c'),('q5','c')]
# relabel of Tutte-dual piece: 0->x,1->y,8->z,4->p,9->q1,10->q2,11->q3,12->q4,13->q5,23->c
def W():
    G=nx.Graph(WE); return G
def glue(G,outer,tag):
    """glue a copy of W into face outer=(X,Y,Z) of G; forbidden pair = (X,Y). returns dict of W-labels->G-vertices"""
    X,Y,Z=outer; m={'x':X,'y':Y,'z':Z}
    for v in W():
        if v not in m: m[v]=(tag,v)
    G.add_edges_from((m[u],m[v]) for u,v in WE)
    return m
if __name__=="__main__":
    w=W(); assert w.number_of_edges()==3*10-6 and nx.check_planarity(w)[0]
    print('W: patterns on (x,y,z):',{P:bool(fb(w,dict(zip('xyz',P)))) for P in itertools.product('FB',repeat=3) if len(set(P))>1})
    # G* : K4 on a,b,c,d ; faces abc,abd,acd,bcd
    G=nx.complete_graph('abcd')
    glue(G,('a','b','c'),1)   # forbid ab
    glue(G,('b','d','a'),2)   # forbid bd
    glue(G,('c','d','a'),3)   # forbid cd
    m4=glue(G,('b','c','d'),4)   # forbid bc
    # nested: inside W1 (outer a,b,c), the face (x,z,q1) = (a,c,(1,q1)) ; glue W forbidding (a,c)
    glue(G,('a','c',(1,'q1')),5)
    # inside W3 (outer c,d,a): x=c,y=d,z=a ; face (y,z,q5)=(d,a,(3,q5)) ; forbid (d,a)
    glue(G,('d','a',(3,'q5')),6)
    n=G.number_of_nodes(); print('G*: n',n,'e',G.number_of_edges(),'3n-6',3*n-6,'planar',nx.check_planarity(G)[0])
    fs=set(frozenset(f) for f in faces_of(G))
    for f in [('x','z','q1'),('y','z','q5')]: assert frozenset(f) in set(frozenset(g) for g in faces_of(w))
    print('FB of G*:',fb(G))
    H=nx.convert_node_labels_to_integers(G,label_attribute='lab')
    nx.write_edgelist(H,'gstar46.edgelist',data=False)
    print('K4 vertices ->',{v:H.nodes[v]['lab'] for v in H if isinstance(H.nodes[v]['lab'],str)})
