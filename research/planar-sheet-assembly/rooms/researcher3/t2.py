"""skeleton-level tests: G = disjoint cycles + arcs. arcs: ((i,p),(j,q))"""
import itertools, networkx as nx, numpy as np
import r03
def run(name, lens, arcs):
    Ws=[[(i,p) for p in range(L)] for i,L in enumerate(lens)]
    where={(i,p):(i,p) for i,L in enumerate(lens) for p in range(L)}
    ends={e:a for e,a in enumerate(arcs)}
    assert len({x for a in arcs for x in a})==2*len(arcs)
    G=nx.Graph()
    for W in Ws: nx.add_cycle(G,W)
    for e,(x,y) in ends.items(): G.add_edge(x,('m',e)); G.add_edge(('m',e),y)
    # (A)
    b=len(Ws); C=nx.MultiGraph(); C.add_nodes_from(range(b))
    for e,(x,y) in ends.items(): C.add_edge(x[0],y[0],key=e)
    okA=True
    for k in range(b):
        L=len(Ws[k]); br=[]
        for e,(x,y) in ends.items():
            if x[0]==k==y[0]: br.append({x[1],y[1]})
        Ck=C.copy(); Ck.remove_node(k)
        for comp in nx.connected_components(Ck):
            att=set()
            for e,(x,y) in ends.items():
                if x[0]==k and y[0] in comp: att.add(x[1])
                if y[0]==k and x[0] in comp: att.add(y[1])
            br.append(att)
        O=nx.Graph(); O.add_nodes_from(range(len(br)))
        for p,q in itertools.combinations(range(len(br)),2):
            if r03.skew(L,br[p],br[q]): O.add_edge(p,q)
        okA&=nx.is_bipartite(O)
    okB=True; infos=[]
    for bl in r03.blocks_of(C):
        rot=r03.rotations(bl,Ws,where,ends)
        lin,info=r03.condition_B_block(rot,bl[1])
        okB&=lin; infos.append((bl[0],lin,info))
    real=nx.check_planarity(G)[0]
    print("%-34s (A)=%s (B)=%s pred=%s real=%s %s"%(name,okA,okB,okA and okB,real,infos))
# E1: C = K3 with double edges, grouped vs alternating at vertex 0
grouped=[((0,0),(1,1)),((0,1),(1,0)),((1,2),(2,1)),((1,3),(2,0)),((2,2),(0,3)),((2,3),(0,2))]
run("E1a K3 double, grouped, coherent",[4,4,4],grouped)
alt=[((0,0),(1,1)),((0,2),(1,0)),((1,2),(2,1)),((1,3),(2,0)),((2,2),(0,3)),((2,3),(0,1))]
run("E1b K3 double, alternating at W0",[4,4,4],alt)
# E2: grouped everywhere, but one pair's order flipped -> parity obstruction
par=[((0,0),(1,0)),((0,1),(1,1)),((1,2),(2,1)),((1,3),(2,0)),((2,2),(0,3)),((2,3),(0,2))]
run("E2 K3 double, grouped, odd parity",[4,4,4],par)
par2=[((0,0),(1,0)),((0,1),(1,1)),((1,2),(2,0)),((1,3),(2,1)),((2,2),(0,3)),((2,3),(0,2))]
run("E2' two pairs flipped (even)",[4,4,4],par2)
# E3: star C, three leaves pairwise interleaved on centre W0
star=[((0,0),(1,0)),((0,3),(1,1)),((0,1),(2,0)),((0,4),(2,1)),((0,2),(3,0)),((0,5),(3,1))]
run("E3 star, 3 leaves pairwise skew",[6,2,2,2],star)
star2=[((0,0),(1,0)),((0,3),(1,1)),((0,1),(2,0)),((0,4),(2,1)),((0,2),(3,1)),((0,5),(3,0))]
run("E3' star, only 2 leaves skew",[6,2,2,2],[((0,0),(1,0)),((0,1),(1,1)),((0,2),(2,0)),((0,4),(2,1)),((0,3),(3,0)),((0,5),(3,1))])
