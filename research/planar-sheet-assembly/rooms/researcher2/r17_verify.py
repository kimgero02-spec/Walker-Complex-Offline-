# 찾은 모형의 독립 검증: 가지 집합이 서로소·연결이고 X 의 각 변마다 G 의 변이 있는지
import networkx as nx, itertools as it
from r17_hM import has_minor, Mcirc
def verify(G,X,m):
    sets=list(m.values()); U=set()
    for S in sets:
        assert not (U&set(S)); U|=set(S); assert nx.is_connected(G.subgraph(S))
    for a,b in X.edges():
        assert any(G.has_edge(x,y) for x in m[a] for y in m[b]),(a,b)
    return True
H=nx.heawood_graph(); S=nx.Graph()
for u,v in H.edges(): S.add_edge(u,('s',u,v)); S.add_edge(('s',u,v),v)
E5=list(it.combinations(range(5),2))
for name,D in [('C5+C5*',[[(i,(i+1)%5) for i in range(5)],[(i,(i+2)%5) for i in range(5)]]),('K5-e+K2',[[e for e in E5 if e!=(3,4)],[(3,4)]])]:
    X=Mcirc(5,D); m=has_minor(S,X,maxset=7); print(name,verify(S,X,m))
# Petersen 이 헤우드의 마이너인가 (위 결과의 따름을 직접 확인)
print('Petersen minor of Heawood', bool(has_minor(H,nx.petersen_graph(),maxset=3)))
