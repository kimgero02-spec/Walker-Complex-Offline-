# X11: researcher1 추측 10 반례 (독립 재구성)
import networkx as nx
from band2 import check
P0 = [('v0','v1','v2'), ('v2','v3','v4'), ('v0','v2','v4','v5'), ('v5','v6','v7','v0')]  # 팔각형 + 현 v0v2, v0v5, v2v4
def dom(name, a0, b0, a4, b4):
    A=[a0]+[f'{name}a{j}' for j in (1,2,3)]+[a4]; B=[b0]+[f'{name}b{j}' for j in (1,2,3)]+[b4]
    sq=[(A[j],A[j+1],B[j+1],B[j]) for j in range(4)]
    return sq[:2], sq[2:]   # 도미노 Q1 (사각형 2), Q2 (사각형 2)
Q1,Q2 = dom('p','v0','v1','v5','v4')   # 호 a=v0v1 -> a'=v4v5
R1,R2 = dom('q','v2','v3','v7','v6')   # 호 b=v2v3 -> b'=v6v7
faces = P0+Q1+Q2+R1+R2
ok,G,_ = check(faces)
V,E = G.number_of_nodes(), G.number_of_edges()
print("가향", ok, "V,E,면", V, E, len(faces), "χ(2-복합체)", V-E+len(faces))
print("리본: 조각 5, 호 6 → χ(X)=5-6=-1, 가향이면 g=1,b=1 (구멍 하나 토러스)")
print("G 평면", nx.check_planarity(G)[0])
# 조각 내부면이 호를 1개 이하 포함하는지
arcs={frozenset(e) for e in [('v0','v1'),('v2','v3'),('v4','v5'),('v6','v7'),('pa2','pb2'),('qa2','qb2')]}
for name,pc in [('P0',P0),('Q1',Q1),('Q2',Q2),('R1',R1),('R2',R2)]:
    print(name, [sum(frozenset((f[t],f[(t+1)%len(f)])) in arcs for t in range(len(f))) for f in pc])
# P0 를 평면 그래프로 3-연결로 바꾸면(바퀴 W8) ?
from collections import Counter
cnt=Counter(frozenset((f[t],f[(t+1)%len(f)])) for f in faces for t in range(len(f)))
Bd=nx.Graph([tuple(e) for e,c in cnt.items() if c==1])
print("경계 성분 수 b =", nx.number_connected_components(Bd), "각 성분이 사이클:", all(d==2 for _,d in Bd.degree()))
