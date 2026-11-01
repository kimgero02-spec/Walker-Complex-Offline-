# F-R1 researcher2: 병합 후보 공격용 결정적 예 계산
import networkx as nx, itertools

def colorable(G, k):
    nodes = sorted(G.nodes(), key=lambda v: -G.degree(v))
    col = {}
    adj = {v: set(G.neighbors(v)) - {v} for v in G}
    if any(G.has_edge(v, v) for v in G): return False
    def pick():
        best=None; bs=(-1,-1)
        for v in nodes:
            if v in col: continue
            s=len({col[u] for u in adj[v] if u in col})
            if (s,len(adj[v]))>bs: bs=(s,len(adj[v])); best=v
        return best
    def bt():
        v=pick()
        if v is None: return True
        used={col[u] for u in adj[v] if u in col}
        mx=max(col.values(), default=-1)
        for c in range(min(k, mx+2)):
            if c in used: continue
            col[v]=c
            if bt(): return True
            del col[v]
        return False
    return bt()

def chi(G):
    k=1
    while not colorable(G,k): k+=1
    return k

def junction(pieces, classes):
    """pieces: list of nx.Graph (vertex names local); classes: list of lists of (k,v) ports (size>=2)."""
    A=nx.Graph()
    for k,P in enumerate(pieces):
        for v in P: A.add_node(('b',k,v))
        for u,v in P.edges(): A.add_edge(('b',k,u),('b',k,v))
    for i,cl in enumerate(classes):
        for (k,v) in cl: A.add_edge(('w',i),('b',k,v))
    return A

def contract(pieces, classes):
    """G = A / white stars, as MultiGraph (keeps parallel edges)."""
    rep={}
    for k,P in enumerate(pieces):
        for v in P: rep[(k,v)]=(k,v)
    for cl in classes:
        r=cl[0]
        for p in cl: rep[p]=r
    G=nx.MultiGraph()
    for k,P in enumerate(pieces):
        for v in P: G.add_node(rep[(k,v)])
        for u,v in P.edges(): G.add_edge(rep[(k,u)],rep[(k,v)],piece=k)
    return G, rep

def subst(A, t):
    B=nx.Graph(); B.add_nodes_from(n for n in A if n[0]=='b')
    B.add_edges_from((u,v) for u,v in A.edges() if u[0]=='b' and v[0]=='b')
    for w in [n for n in A if n[0]=='w']:
        K=[('k',w,i) for i in range(t)]
        B.add_nodes_from(K); B.add_edges_from(itertools.combinations(K,2))
        for x in A.neighbors(w):
            for y in K: B.add_edge(x,y)
    return B

def seq(A, T):
    return [chi(subst(A,t)) for t in range(T)]

def boundary_b(pieces, cycles, arcs, rep):
    """cycles[k]: list of vertices of C_k in order; arcs: set of (k,u,v) boundary edges that are shared (arc edges).
    b = # cycles of non-arc boundary edges after identification."""
    M=nx.MultiGraph()
    for k,C in enumerate(cycles):
        for i in range(len(C)):
            u,v=C[i],C[(i+1)%len(C)]
            if (k,u,v) in arcs or (k,v,u) in arcs: continue
            M.add_edge(rep[(k,u)],rep[(k,v)])
    M.remove_nodes_from([n for n in list(M) if M.degree(n)==0])
    assert all(d==2 for _,d in M.degree()), dict(M.degree())
    return nx.number_connected_components(M)

def simple(G):
    S=nx.Graph(); S.add_nodes_from(G); S.add_edges_from((u,v) for u,v in G.edges() if u!=v); return S

def cyc(names):
    C=nx.Graph(); nx.add_cycle(C,names); return C
def wheel(rim, c='c'):
    W=cyc(rim); W.add_edges_from((c,r) for r in rim); return W

out=[]
def rep_line(s): print(s); out.append(s)

# ---- E1: 팔면체 = W4 ∪ W4 (테두리 전체 공유): 해석(parse) 모호성
P=[wheel([0,1,2,3]), wheel([0,1,2,3])]
cls=[[(0,i),(1,i)] for i in range(4)]
A=junction(P,cls); G,rep=contract(P,cls); S=simple(G)
rep_line(f"E1 octa: G planar={nx.check_planarity(S)[0]}, G~octahedron={nx.is_isomorphic(S,nx.octahedral_graph())}, A planar={nx.check_planarity(A)[0]}")
for name,arcs in [("parseA {01,23}",{(0,0,1),(1,0,1),(0,2,3),(1,2,3)}),("parseB {12,30}",{(0,1,2),(1,1,2),(0,3,0),(1,3,0)})]:
    b=boundary_b(P,[[0,1,2,3],[0,1,2,3]],arcs,rep); n,m=2,2
    rep_line(f"   {name}: n={n} m={m} b={b} n-m+b={n-m+b}")

# ---- E2: 두 W6 를 테두리 경로 0-1-2-3 으로 접합: 한 호 vs 두 호
P=[wheel([0,1,2,3,4,5]), wheel([0,1,2,3,4,5])]
cls=[[(0,i),(1,i)] for i in range(4)]
A=junction(P,cls); G,rep=contract(P,cls); S=simple(G)
rep_line(f"E2 W6|W6: G planar={nx.check_planarity(S)[0]}, A planar={nx.check_planarity(A)[0]}, parallel edges in G={G.number_of_edges()-S.number_of_edges()}")
C6=[0,1,2,3,4,5]
for name,arcs,m in [("one arc 0123",{(k,i,i+1) for k in (0,1) for i in range(3)},1),("two arcs 01,23",{(k,0,1) for k in (0,1)}|{(k,2,3) for k in (0,1)},2)]:
    b=boundary_b(P,[C6,C6],arcs,rep)
    rep_line(f"   {name}: n=2 m={m} b={b} n-m+b={2-m+b}")

# ---- E3: 정사각형 2장 뫼비우스 -> K4 (다각형 조각, 정리 U 영역)
P=[cyc(['a','b','c','d']), cyc(['a','b','c','d'])]
cls=[[(0,'a'),(1,'a')],[(0,'b'),(1,'b')],[(0,'c'),(1,'d')],[(0,'d'),(1,'c')]]
A=junction(P,cls); G,rep=contract(P,cls); S=simple(G)
rep_line(f"E3 Mobius n=2: G~K4={nx.is_isomorphic(S,nx.complete_graph(4))}, G planar={nx.check_planarity(S)[0]}, A planar={nx.check_planarity(A)[0]}, |A|={A.number_of_nodes()},{A.number_of_edges()}")
b=boundary_b(P,[['a','b','c','d']]*2,{(0,'a','b'),(1,'a','b'),(0,'c','d'),(1,'c','d')},rep)
rep_line(f"   b={b} (n-m+b={2-2+b}, [eps]!=0)")
rep_line(f"   chi seq t=0..4: {seq(A,5)}  chi(G)={chi(S)}")

# ---- E4: 정사각형 3장 뫼비우스 -> K33
sq=lambda: cyc(['a','b','c','d'])
P=[sq(),sq(),sq()]
# piece k: arc ab (shared with k-1) and arc cd (shared with k+1); piece k's (c,d) -> piece k+1's (b,a) straight; last twisted
cls=[]
for k in range(3):
    j=(k+1)%3
    if k<2: cls+= [[(k,'c'),(j,'b')],[(k,'d'),(j,'a')]]
    else:   cls+= [[(k,'c'),(j,'a')],[(k,'d'),(j,'b')]]
A=junction(P,cls); G,rep=contract(P,cls); S=simple(G)
rep_line(f"E4 Mobius n=3: G~K33={nx.is_isomorphic(S,nx.complete_bipartite_graph(3,3))}, A planar={nx.check_planarity(A)[0]}")

# ---- E5: K5 = W4 ∪ C4 (R01, n=2 띠, 리본형): 정리 A 수열
P1=cyc(['a','b','d','c']); P1.add_edges_from(('e',x) for x in 'abcd')
P2=cyc(['a','b','c','d'])
P=[P1,P2]; cls=[[(0,x),(1,x)] for x in 'abcd']
A=junction(P,cls); G,rep=contract(P,cls); S=simple(G)
rep_line(f"E5 W4uC4: G~K5={nx.is_isomorphic(S,nx.complete_graph(5))}, chi(P)={chi(P1)},{chi(P2)}, A planar={nx.check_planarity(A)[0]}")
rep_line(f"   chi(A^(t)) t=0..5: {seq(A,6)}")

# ---- E6: 삼각형 셋을 세 꼭짓점에서 동시 식별 (비리본, 흰 점 차수 3)
P=[cyc([0,1,2]) for _ in range(3)]
cls=[[(k,i) for k in range(3)] for i in range(3)]
A=junction(P,cls); G,rep=contract(P,cls); S=simple(G)
rep_line(f"E6 triple K3: G~K3={nx.is_isomorphic(S,nx.complete_graph(3))}, A planar={nx.check_planarity(A)[0]}")

# ---- E7: 간선 접합점까지 넣은 세분형(후보 4)에서 정리 A 공식의 출력: E5 의 세분
P1s=nx.Graph(); P2s=nx.Graph()
def subdiv(P,tag):
    Q=nx.Graph()
    for u,v in P.edges(): m=('m',tag,frozenset((u,v))); Q.add_edge(u,m); Q.add_edge(m,v)
    return Q
Q1=subdiv(P1,0); Q2=subdiv(P2,1)
cls2=[[(0,x),(1,x)] for x in 'abcd']
for (u,v) in [('a','b'),('c','d')]:
    cls2.append([(0,('m',0,frozenset((u,v)))),(1,('m',1,frozenset((u,v))))])
A2=junction([Q1,Q2],cls2)
s2=seq(A2,4)
rep_line(f"E7 subdivided E5: chi(A^(t)) t=0..3: {s2}  -> formula min{{t+1: chi<=t+1}} = {min(t+1 for t,c in enumerate(s2) if c<=t+1)} (true chi(K5)=5)")
