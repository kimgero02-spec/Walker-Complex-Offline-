# F-R3 researcher2: 접합 그래프 𝔄 의 마이너 샌드위치 Σ ≤ G ≤ 𝔄 와 리본 판 확인
import networkx as nx, itertools, io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    from f_r1 import junction, contract, simple
    from f_r1_ribbon import cyc
    exec(open('f_r2_bridge.py').read())

def manual_from_arcs(P, arcs):
    """ribbon arcs -> classes (pairs) for junction graph"""
    cls=[]
    for (k,pk,j,pj) in arcs:
        for a,b in zip(pk,pj): cls.append([(k,a),(j,b)])
    return cls

def Sigma(P, cls):
    """Σ = G / cells, cells = components of P_k - ports"""
    ports={p for cl in cls for p in cl}
    G,rep=contract(P,cls); S=simple(G)
    cellmap={}
    for k,Pk in enumerate(P):
        inner=Pk.subgraph([v for v in Pk if (k,v) not in ports])
        for i,comp in enumerate(nx.connected_components(inner)):
            for v in comp: cellmap[rep[(k,v)]]=('cell',k,i)
    M=nx.Graph()
    for v in S: M.add_node(cellmap.get(v,v))
    for u,v in S.edges():
        a,b=cellmap.get(u,u),cellmap.get(v,v)
        if a!=b: M.add_edge(a,b)
    return M,S

def show(name,P,cls):
    A=junction(P,cls); Sg,G=Sigma(P,cls)
    pl=lambda X: nx.check_planarity(X)[0]
    print(f"{name}: planar  Σ={pl(Sg)}  G={pl(G)}  𝔄={pl(A)}   (|Σ|={Sg.number_of_nodes()}, |G|={G.number_of_nodes()}, |𝔄|={A.number_of_nodes()})")

sq=lambda: cyc(['a','b','c','d'])
# Mobius n=2 squares (K4)
P=[sq(),sq()]; show("Mobius2 squares (G=K4)",P,[[(0,'a'),(1,'a')],[(0,'b'),(1,'b')],[(0,'c'),(1,'d')],[(0,'d'),(1,'c')]])
# annulus n=2 squares
show("annulus2 squares",P,[[(0,'a'),(1,'b')],[(0,'b'),(1,'a')],[(0,'c'),(1,'d')],[(0,'d'),(1,'c')]])
# crossing torus bare octagon (R4) and with chords
for ch in [None,(1,4),(1,6)]:
    import f_r1_ribbon as R
    Pp,C,arcs=None,None,None
    O=list(range(8)); P0=cyc(O)
    if ch: P0.add_edge(*ch)
    Sq=['p','q','r','s']; Pp=[P0]+[cyc(Sq) for _ in range(4)]
    arcs=[(0,[0,1],1,['q','p']),(0,[4,5],2,['q','p']),(1,['r','s'],2,['s','r']),
          (0,[2,3],3,['q','p']),(0,[6,7],4,['q','p']),(3,['r','s'],4,['s','r'])]
    show(f"crossing torus chord={ch}",Pp,manual_from_arcs(Pp,arcs))
# theta 9-gons: planar rotation A / torus rotation B
X=list(range(9)); Y=[f'y{i}' for i in range(9)]; P=[cyc(X),cyc(Y)]
A_=[(0,[0,1],1,['y1','y0']),(0,[3,4],1,['y7','y6']),(0,[6,7],1,['y4','y3'])]
B_=[(0,[0,1],1,['y1','y0']),(0,[3,4],1,['y4','y3']),(0,[6,7],1,['y7','y6'])]
show("theta A (X planar)",P,manual_from_arcs(P,A_)); show("theta B (X torus)",P,manual_from_arcs(P,B_))
# wheels W6 twisted / straight (3-connected, Theorem E)
def wheel(rim): W=cyc(rim); W.add_edges_from(('c',r) for r in rim); return W
R6=[0,1,2,3,4,5]; P=[wheel(R6),wheel(R6)]
show("W6uW6 straight",P,manual_from_arcs(P,[(0,[0,1],1,[1,0]),(0,[3,4],1,[4,3])]))
show("W6uW6 twisted",P,manual_from_arcs(P,[(0,[0,1],1,[1,0]),(0,[3,4],1,[3,4])]))
# K5 = W4 u C4 (n=2 band), triple triangles (non-ribbon)
P1=cyc(['a','b','d','c']); P1.add_edges_from(('e',x) for x in 'abcd')
show("K5 = W4uC4",[P1,cyc(['a','b','c','d'])],[[(0,x),(1,x)] for x in 'abcd'])
show("3 triangles glued at 3 classes",[cyc([0,1,2]) for _ in range(3)],[[(k,i) for k in range(3)] for i in range(3)])

print("---- 정리 M: 마이너 모델 = 나무 조각 설명서 (피터슨 ⊇ K5)")
def model_manual(Gbig, branch, medges):
    """branch: list of vertex sets; medges: dict (i,j)->(u,v) u in B_i, v in B_j"""
    P=[]
    for i,B in enumerate(branch):
        T=nx.minimum_spanning_tree(Gbig.subgraph(B)).copy()
        P.append(T)
    cls=[]
    for (i,j),(u,v) in medges.items():
        P[i].add_edge(u,('p',i,j)); P[j].add_edge(v,('p',j,i))
        cls.append([(i,('p',i,j)),(j,('p',j,i))])
    return P,cls
Pet=nx.petersen_graph()   # outer 0-4 cycle, spokes i-(i+5), inner 5-9 pentagram
branch=[{i,i+5} for i in range(5)]
med={}
for u,v in Pet.edges():
    bu=next(i for i,B in enumerate(branch) if u in B); bv=next(i for i,B in enumerate(branch) if v in B)
    if bu!=bv: med[(min(bu,bv),max(bu,bv))]=(u,v) if bu<bv else (v,u)
P,cls=model_manual(Pet,branch,med)
A=junction(P,cls); G,rep=contract(P,cls); G=simple(G)
Pi=A.copy()
for k,Pk in enumerate(P):  # contract each piece
    nodes=[('b',k,v) for v in Pk]
    Pi=nx.contracted_nodes(Pi,nodes[0],nodes[1],self_loops=False) if len(nodes)>1 else Pi
    for x in nodes[2:]: Pi=nx.contracted_nodes(Pi,nodes[0],x,self_loops=False)
sub=lambda F: nx.Graph([(u,('s',u,v)) for u,v in F.edges()]+[(('s',u,v),v) for u,v in F.edges()])
print("pieces are trees:", all(nx.is_tree(p) for p in P), "| whites deg 2:", all(len(c)==2 for c in cls))
print("Π(𝔄) ≅ subdivided K5:", nx.is_isomorphic(nx.Graph(Pi),sub(nx.complete_graph(5))))
def suppress(H):
    H=nx.Graph(H)
    while True:
        d2=[v for v in H if H.degree(v)==2 and not H.has_edge(*H.neighbors(v))]
        if not d2: return H
        v=d2[0]; a,b=H.neighbors(v); H.remove_node(v); H.add_edge(a,b)
print("assembly G homeomorphic to Petersen:", nx.is_isomorphic(suppress(G),Pet), "| 𝔄 homeomorphic to Petersen:", nx.is_isomorphic(suppress(A),Pet))
