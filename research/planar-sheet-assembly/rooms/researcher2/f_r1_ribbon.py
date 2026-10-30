# F-R1 researcher2 (재배정 임무): 리본 설명서의 사상 없는 복원, 홀로노미, 평면성
import networkx as nx, itertools
from f_r1 import chi

def assemble(pieces, cycles, arcs):
    """pieces[k]: nx.Graph; cycles[k]: C_k vertex list (oriented);
    arcs: list of (k, pathk, j, pathj): pathk forward along C_k, pathj list identified pointwise.
    returns simple G, eps list, b, n, m, holonomy-trivial flag."""
    rep={}
    for k,P in enumerate(pieces):
        for v in P: rep[(k,v)]=(k,v)
    def find(x):
        while rep[x]!=x: x=rep[x]
        return x
    eps=[]; arcedges=set()
    for (k,pk,j,pj) in arcs:
        for a,b in zip(pk,pj): rep[find((k,a))]=find((j,b))
        Ck,Cj=cycles[k],cycles[j]
        assert all(Ck[(Ck.index(pk[i])+1)%len(Ck)]==pk[i+1] for i in range(len(pk)-1))
        fwd=all(Cj[(Cj.index(pj[i])+1)%len(Cj)]==pj[i+1] for i in range(len(pj)-1))
        bwd=all(Cj[(Cj.index(pj[i])-1)%len(Cj)]==pj[i+1] for i in range(len(pj)-1))
        assert fwd or bwd
        eps.append(+1 if bwd else -1)  # +1: 두 경계 방향이 호를 반대로 지남
        for i in range(len(pk)-1):
            arcedges.add((k,frozenset((pk[i],pk[i+1])))); arcedges.add((j,frozenset((pj[i],pj[i+1]))))
    G=nx.Graph()
    for k,P in enumerate(pieces):
        for v in P: G.add_node(find((k,v)))
        for u,v in P.edges():
            a,b=find((k,u)),find((k,v)); assert a!=b; G.add_edge(a,b)
    M=nx.MultiGraph()
    for k,C in enumerate(cycles):
        for i in range(len(C)):
            u,v=C[i],C[(i+1)%len(C)]
            if (k,frozenset((u,v))) in arcedges: continue
            M.add_edge(find((k,u)),find((k,v)))
    assert all(d==2 for _,d in M.degree())
    b=nx.number_connected_components(M)
    n=len(pieces); m=len(arcs)
    # holonomy: 2-colour pieces by orientation flips
    H=nx.MultiGraph(); H.add_nodes_from(range(n))
    for idx,(k,pk,j,pj) in enumerate(arcs): H.add_edge(k,j,s=eps[idx])
    sign={}; triv=True
    for comp in nx.connected_components(H):
        r=min(comp); sign[r]=1; st=[r]
        while st:
            x=st.pop()
            for _,y,d in H.edges(x,data=True):
                want=sign[x]*d['s']
                if y not in sign: sign[y]=want; st.append(y)
                elif sign[y]!=want: triv=False
    return G,eps,b,n,m,triv

def cyc(names):
    C=nx.Graph(); nx.add_cycle(C,names); return C
def report(tag,res):
    G,eps,b,n,m,triv=res
    print(f"{tag}: |V|={G.number_of_nodes()} |E|={G.number_of_edges()} eps={eps} b={b} n-m+b={n-m+b} holonomy_trivial={triv} planar={nx.check_planarity(G)[0]}")
    return G

# ---- R1: 위치(간격) 데이터가 필요: 육각형 + 정사각형 2개, 간격 (1,3) vs (2,2)
for gaps,(e1,e2) in [("(1,3)",(0,2)),("(2,2)",(0,3))]:
    if e2 is None: continue
    hexC=list(range(6)); P=[cyc(hexC),cyc(['a','b','c','d']),cyc(['a','b','c','d'])]
    arcs=[(0,[e1,e1+1],1,['b','a']),(0,[e2,e2+1],2,['b','a'])]
    G=report("R1 hex gaps"+gaps, assemble(P,[hexC,['a','b','c','d'],['a','b','c','d']],arcs))
    globals()['G_'+str(e2)]=G
print("   R1 two G isomorphic?", nx.is_isomorphic(G_2,G_3))

# ---- R2: 회전 rho 가 필요: 육각형 2장, H=세타(이중 3변), 호 = 한 칸씩 건너 변
X=list(range(6)); Y=['y0','y1','y2','y3','y4','y5']
P=[cyc(X),cyc(Y)]
# P0 arcs: 01, 23, 45 (order alpha,beta,gamma). P1 arcs y0y1, y2y3, y4y5.
arcsA=[(0,[0,1],1,['y1','y0']),(0,[2,3],1,['y5','y4']),(0,[4,5],1,['y3','y2'])]   # rho_1 reversed-compatible (planar theta)
arcsB=[(0,[0,1],1,['y1','y0']),(0,[2,3],1,['y3','y2']),(0,[4,5],1,['y5','y4'])]   # other cyclic order
GA=report("R2 theta rho=A", assemble(P,[X,Y],arcsA))
GB=report("R2 theta rho=B", assemble(P,[X,Y],arcsB))
print("   R2B ~ K33?", nx.is_isomorphic(GB,nx.complete_bipartite_graph(3,3)), " R2A ~ prism?", nx.is_isomorphic(GA,nx.circular_ladder_graph(3)))

# ---- R3: 다각형 조각 위상 환원: 호/간격 길이를 늘려도 위상 불변 (세분) - 예: R2B 에서 호 길이 2, 간격 2
X2=list(range(12)); Y2=[f'y{i}' for i in range(12)]
arcsB2=[(0,[0,1,2],1,['y2','y1','y0']),(0,[4,5,6],1,['y6','y5','y4']),(0,[8,9,10],1,['y10','y9','y8'])]
GB2=report("R3 R2B lengthened", assemble([cyc(X2),cyc(Y2)],[X2,Y2],arcsB2))
def homeo_core(G):
    H=G.copy()
    changed=True
    while changed:
        changed=False
        for v in list(H):
            if H.degree(v)==2:
                a,b=list(H.neighbors(v))
                if not H.has_edge(a,b): H.remove_node(v); H.add_edge(a,b); changed=True; break
    return H
print("   R3 suppressed cores isomorphic:", nx.is_isomorphic(homeo_core(GB2),homeo_core(GB)))

# ---- R4: 2-연결 조각에서는 위치가 평면성을 바꿈: 엇갈림 토러스 (R01 §5) 팔각형 + 지름 현
def torus(chord):
    O=list(range(8)); P0=cyc(O)
    if chord: P0.add_edge(*chord)
    sq=lambda: cyc(['p','q','r','s'])
    P=[P0,sq(),sq(),sq(),sq()]; C=[O]+[['p','q','r','s']]*4
    # a=01 -> Q1, a'=45 -> Q2, Q1-Q2 via rs ; b=23 -> R1, b'=67 -> R2, R1-R2 via rs
    arcs=[(0,[0,1],1,['q','p']),(0,[4,5],2,['q','p']),(1,['r','s'],2,['s','r']),
          (0,[2,3],3,['q','p']),(0,[6,7],4,['q','p']),(3,['r','s'],4,['s','r'])]
    return assemble(P,C,arcs)
report("R4 bare octagon",torus(None))
for ch in [(0,4),(1,5),(0,2),(1,3),(1,6),(0,5),(2,7),(1,4)]:
    G,eps,b,n,m,triv=torus(ch); print(f"   chord {ch}: planar={nx.check_planarity(G)[0]}  b={b} triv={triv}")
