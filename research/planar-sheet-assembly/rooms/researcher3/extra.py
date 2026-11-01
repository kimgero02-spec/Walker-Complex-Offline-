import networkx as nx
from holo import *
# 1) 이중피복의 정체
K5 = nx.complete_graph(5); T=[[i,(i+1)%5,(i+2)%5] for i in range(5)]
H,_=overlap_graph(T); D,_=orientation_double_cover(T,H)
print("K5 피복 ≅ C10(1,2)(=5-반각기둥)?", nx.is_isomorphic(D, nx.circulant_graph(10,[1,2])))
Pet=nx.petersen_graph()
import itertools
C=[];seen=set()
for c in nx.simple_cycles(Pet.to_directed()):
    if len(c)==5 and frozenset(c) not in seen: seen.add(frozenset(c)); C.append(c)
for S in itertools.combinations(C,6):
    cnt={}
    for c in S:
        for e in cyc_edges(c): cnt[frozenset(e)]=cnt.get(frozenset(e),0)+1
    if len(cnt)==15 and all(v==2 for v in cnt.values()): break
H,_=overlap_graph(list(S)); D,_=orientation_double_cover(list(S),H)
print("Petersen 피복 ≅ 12면체?", nx.is_isomorphic(D, nx.dodecahedral_graph()))
for k in (3,4,5):
    G,P=ladder(k,True); H,_=overlap_graph(P); D,_=orientation_double_cover(P,H)
    print(f"M_{2*k} 피복 ≅ 프리즘 C_{2*k}xK2?", nx.is_isomorphic(D, nx.circular_ladder_graph(2*k)))
# 2) 나무 H, 공유 3점: K_{2,3} ∪_{1,2,3} K_{1,3} = K_{3,3}
P1=nx.complete_bipartite_graph(2,3)  # 0,1 | 2,3,4
P2=nx.Graph([(9,2),(9,3),(9,4)])
G=nx.compose(P1,P2)
print("나무 접착(공유 3점) 조각 평면?", nx.check_planarity(P1)[0], nx.check_planarity(P2)[0], "결과 K33?", nx.is_isomorphic(G,nx.complete_bipartite_graph(3,3)))
# P1 에서 {2,3,4} 가 한 면 위에 있는가: 평면 매장의 면 열거
def faces(Gp):
    ok,emb=nx.check_planarity(Gp); F=[];used=set()
    for u,v in emb.edges():
        if (u,v) in used: continue
        F.append(emb.traverse_face(u,v,mark_half_edges=used))
    return F
print(" K23 의 면에 {2,3,4} 모두 있는 면?", any({2,3,4}<=set(f) for f in faces(P1)))
# 3) 공유 4점, 바퀴 W4 두 개, 테두리 순서 1234 vs 1324
A=nx.Graph([(1,2),(2,3),(3,4),(4,1)]+[('a',i) for i in range(1,5)])
B=nx.Graph([(1,3),(3,2),(2,4),(4,1)]+[('b',i) for i in range(1,5)])
G=nx.compose(A,B); print("W4 ∪ W4' (순서 1234/1324) 평면?", nx.check_planarity(G)[0])
B2=nx.Graph([(1,2),(2,3),(3,4),(4,1)]+[('b',i) for i in range(1,5)])
print("같은 순서(공유 4-사이클)일 때 평면?", nx.check_planarity(nx.compose(A,B2))[0])
# 4) 발전가능성(코사이클) 실패: 조각 3개, 삼각형 H, 레이블 합성이 비자명 -> 조각이 몫에 단사로 안 들어감
# P_i = 경로 x_i - c_i - y_i (3개). 공유: P1.y~P2.x, P2.y~P3.x, P3.y~P1.? (끝점 대응을 레이블로)
def colim(pieces, glue):
    uf={}
    def f(x):
        uf.setdefault(x,x)
        while uf[x]!=x: x=uf[x]
        return x
    for p in pieces:
        for v in p.nodes(): f(v)
    for a,b in glue: uf[f(a)]=f(b)
    A=nx.MultiGraph()
    for p in pieces:
        for u,v in p.edges(): A.add_edge(f(u),f(v))
    inj=all(len({f(v) for v in p.nodes()})==p.number_of_nodes() for p in pieces)
    return A,inj
# 조각: 삼각형 3개가 한 점을 공유하는 '부채'. 공유 부분 = 정점 하나. 레이블 = 그 정점을 상대 조각의 어느 정점에 대응시키나
t=lambda i:nx.Graph([((i,0),(i,1)),((i,1),(i,2)),((i,2),(i,0))])
P=[t(0),t(1),t(2)]
good=[((0,0),(1,0)),((1,0),(2,0)),((2,0),(0,0))]
bad =[((0,0),(1,0)),((1,0),(2,0)),((2,0),(0,1))]  # 한 바퀴 돌면 0.0 -> 0.1
for nm,g in (("정합",good),("비정합",bad)):
    A,inj=colim(P,g); print(f"  {nm}: 몫 |V|={A.number_of_nodes()} 다중변/고리 있음={any(u==v for u,v in A.edges()) or not nx.is_isomorphic(nx.Graph(A),A) if False else (A.number_of_edges()!=nx.Graph(A).number_of_edges() or nx.number_of_selfloops(A)>0)} 조각 단사={inj}")
