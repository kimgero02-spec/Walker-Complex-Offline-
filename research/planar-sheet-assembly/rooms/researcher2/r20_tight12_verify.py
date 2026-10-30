# R20 과제2 인증서 독립 검산: K_12 = P u B1 u B2, P 는 (4,3) 평면, B_j 평면 이분, 12 = 3*2*2 (체가 꽉 참).
import ast, itertools, networkx as nx
from r19_lib import chi, omega
L=open('r20_tight12_out.txt').read().splitlines()
lab=lambda v: 3*(2*v[0][0]+v[0][1])+v[1]
P=nx.Graph([(lab(u),lab(v)) for u,v in ast.literal_eval(L[1])])
Bs=[nx.Graph([(lab(u),lab(v)) for u,v in b]) for b in ast.literal_eval(L[2])]
print("P =",sorted(tuple(sorted(e)) for e in P.edges()))
for j,b in enumerate(Bs): print(f"B{j+1} =",sorted(tuple(sorted(e)) for e in b.edges()))
cnt={}
for G in [P]+Bs:
    for e in G.edges(): cnt[frozenset(e)]=cnt.get(frozenset(e),0)+1
print("정확 분해:", set(cnt)==set(frozenset(e) for e in itertools.combinations(range(12),2)) and all(c==1 for c in cnt.values()))
print("평면:",[nx.check_planarity(G)[0] for G in [P]+Bs], "B 이분:",[nx.is_bipartite(b) for b in Bs])
print("chi(P)=",chi(P),"omega(P)=",omega(P))
fib=lambda v:v//3
for j,b in enumerate(Bs):  # B_j 의 두 쪽이 좌표 j 로 정해지는지
    coord=lambda v:((fib(v)>>1)&1) if j==0 else (fib(v)&1)
    print(f"B{j+1} 변이 좌표 {j+1} 을 가로지름:", all(coord(u)!=coord(v) for u,v in b.edges()))
Qt=nx.Graph(); Qt.add_nodes_from(range(4))
for u,v in P.edges():
    if fib(u)!=fib(v): Qt.add_edge(fib(u),fib(v))
print("P 의 올 몫그래프 변:",sorted(Qt.edges()), "숲인가:",nx.is_forest(Qt))
# 4-임계 부분그래프 (변을 탐욕적으로 지움)
H=P.copy()
for e in list(H.edges()):
    H.remove_edge(*e)
    if chi(H)<4: H.add_edge(*e)
H.remove_nodes_from([v for v in list(H) if H.degree(v)==0])
print("4-임계 부분그래프: 점",sorted(H.nodes()),"변",sorted(tuple(sorted(e)) for e in H.edges()))
print("차수:",dict(H.degree()))
