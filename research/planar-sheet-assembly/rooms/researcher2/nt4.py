# N-T4 researcher2: 재현용 결정적 계산 (탐색 없음)
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher, categorical_node_match
from itertools import product

def chi(G, qmax=8):
    nodes=sorted(G.nodes(), key=lambda v:-G.degree(v))
    for q in range(1,qmax+1):
        col={}
        def bt(i):
            if i==len(nodes): return True
            v=nodes[i]
            for c in range(q):
                if all(col.get(u)!=c for u in G[v]):
                    col[v]=c
                    if bt(i+1): return True
                    del col[v]
            return False
        if bt(0): return q
    return None

def strip(n):
    S=nx.Graph(); S.add_nodes_from(range(n))
    for i in range(n):
        if i+1<n: S.add_edge(i,i+1)
        if i+2<n: S.add_edge(i,i+2)
    return S

def pair_ball(G,a,b,r):
    da=nx.single_source_shortest_path_length(G,a,cutoff=r)
    db=nx.single_source_shortest_path_length(G,b,cutoff=r)
    H=G.subgraph(set(da)|set(db)).copy()
    for v in H: H.nodes[v]['root']= 1 if v==a else (2 if v==b else 0)
    return H

def iso_rooted(H1,H2):
    return GraphMatcher(H1,H2,node_match=categorical_node_match('root',0)).is_isomorphic()

print("== (b) T3-4 재검: S_30, (12,18) vs (12,17) ==")
S=strip(30)
for p in [(12,18),(12,17)]:
    a,b=p
    print(p,"deg",S.degree(a),S.degree(b),"dist",nx.shortest_path_length(S,a,b),
          "common",len(set(S[a])&set(S[b])))
for r in range(1,5):
    H1=pair_ball(S,12,18,r); H2=pair_ball(S,12,17,r)
    cross=lambda H,a,b,r: None
    print(f"r={r}: 쌍-공 |V|,|E| =",(H1.number_of_nodes(),H1.number_of_edges()),
          (H2.number_of_nodes(),H2.number_of_edges()),"뿌리표시 동형?",iso_rooted(H1,H2))
# 개별 공 (상대의 주장) 확인
for r in [4]:
    B=lambda v: S.subgraph(nx.single_source_shortest_path_length(S,v,cutoff=r)).copy()
    print("개별 반지름4 공 동형 12~17,12~18,17~18:",nx.is_isomorphic(B(12),B(17)),nx.is_isomorphic(B(12),B(18)),nx.is_isomorphic(B(17),B(18)))
# 수선: 거리 > 2r 인 쌍이면 쌍-공이 서로소 합 -> 동형
print("== 수선판: S_80, (10,40) [차 30, mod3=0] vs (10,41) [차 31] ==")
S=strip(80)
for p in [(10,40),(10,41)]:
    print(p,"dist",nx.shortest_path_length(S,*p))
for r in range(1,7):
    H1=pair_ball(S,10,40,r); H2=pair_ball(S,10,41,r)
    print(f"r={r}: 쌍-공 동형?",iso_rooted(H1,H2))
def glue_K4e(S,a,b):
    G=S.copy(); G.add_edges_from([(a,'p'),(a,'q'),(b,'p'),(b,'q'),('p','q')])
    return G
for p in [(10,40),(10,41)]:
    G=glue_K4e(S,*p); print(p,"K4-uv 붙임 chi",chi(G),"평면",nx.check_planarity(G)[0])

print("== (a) 포트 반례: 같은 조각 둘, 같은 골격 K3, 다른 chi ==")
# 다이아몬드 t0 t1 t2 + s (s~t1,t2) : 3-색칠 유일, c(s)=c(t0)
def diamond(tag):
    D=nx.Graph(); D.add_edges_from([((tag,'t0'),(tag,'t1')),((tag,'t0'),(tag,'t2')),((tag,'t1'),(tag,'t2')),((tag,'s'),(tag,'t1')),((tag,'s'),(tag,'t2'))]); return D
portsA=[('A','t0'),('A','s'),('A','t1')]   # x1=x2 강제, x3 다름
portsB=[('B','t1'),('B','t0'),('B','s')]   # x2=x3 강제, x1 다름
def assemble(perm):
    G=nx.union(diamond('A'),diamond('B'))
    for i in range(3):
        G=nx.contracted_nodes(G,portsA[i],portsB[perm[i]],self_loops=True)
    return G
for name,perm in [("설명서1 (x_i~x_i)",(0,1,2)),("설명서2 (회전)",(1,2,0))]:
    G=assemble(perm)
    loops=list(nx.selfloop_edges(G))
    G=nx.Graph(G); 
    print(name,"고리",loops,"|V|,|E|",G.number_of_nodes(),G.number_of_edges(),"chi",chi(G),"평면",nx.check_planarity(G)[0])
# 골격: 식별류 3개, 두 조각 모두 세 류를 만남 -> 둘 다 K3

print("== (c) K6: 평면 조각 + 숲 골격 설명서 없음의 확인용 ==")
print("K6-e 평면?",nx.check_planarity(nx.complete_graph(6).copy().__class__(nx.complete_graph(6).edges()) if False else (lambda H:(H.remove_edge(0,1),H)[1])(nx.complete_graph(6)))[0])
print("K5-e 평면?",nx.check_planarity((lambda H:(H.remove_edge(0,1),H)[1])(nx.complete_graph(5)))[0])
# 자명 해독기: G를 만들어 계산하는 규칙은 평면성도 결정 -> 정보적 읽기는 STMT를 공허하게 만듦

print("== 수선판 2: 거리까지 같은 쌍, S_80, (10,40)[차30] vs (10,39)[차29] ==")
S=strip(80)
for p in [(10,40),(10,39)]:
    print(p,"dist",nx.shortest_path_length(S,*p),"deg",S.degree(p[0]),S.degree(p[1]))
for r in range(1,7):
    print(f"r={r}: 쌍-공 동형?",iso_rooted(pair_ball(S,10,40,r),pair_ball(S,10,39,r)))
for p in [(10,40),(10,39)]:
    G=glue_K4e(S,*p); print(p,"chi",chi(G),"평면",nx.check_planarity(G)[0])
