from r48_at import *
import networkx as nx
oct_=nx.octahedral_graph(); Eo=list(oct_.edges())
print('octahedron t=(2^6):',coef(6,Eo,[2]*6))
ico=nx.icosahedral_graph(); Ei=list(ico.edges())
print('ico deg',dict(ico.degree()))
# 교차 차수 3 정점 집합 T (t=2), 나머지 교차 차수 2 (t=3). sum = 2*6+3*6 = 30 = |E|
import itertools
# 패턴 1: 한 정점 0 과 그 이웃 5개 -> d_H=3 ; 패턴 2: 독립집합 쪽
pats={'star(0)':[0]+list(ico[0]),
      'antipodal pairs 3':None}
# 대척점 찾기
dist=dict(nx.all_pairs_shortest_path_length(ico))
anti={v:[u for u in ico if dist[v][u]==3][0] for v in ico}
pats['antipodal pairs 3']=[0,anti[0]]+[list(ico[0])[0],anti[list(ico[0])[0]]]+[list(ico[0])[2],anti[list(ico[0])[2]]]
# 독립 6? 이십면체 alpha=3, 그래서 6 정점은 간선 포함
for name,T in pats.items():
    t=[2 if v in T else 3 for v in range(12)]
    print(name,T,'sum',sum(t),'coef',coef(12,Ei,t))
# 교차 차수 3 이 7개 이상이면 sum<30 -> 계수 정의 불가(혼합정리 적용 불가)
