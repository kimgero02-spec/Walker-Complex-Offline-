# r1 정리 U / 정리 R 공격: 내부 핀치 정점이 있는 경우 (반-이십면체 RP^2 에서 삼각형 하나 제거)
import networkx as nx, itertools as it
from collections import defaultdict
T=[(1,2,3),(1,3,4),(1,4,5),(1,5,6),(1,6,2),(2,3,5),(3,4,6),(4,5,2),(5,6,3),(6,2,4)]
cnt=defaultdict(int)
for t in T:
    for e in it.combinations(t,2): cnt[frozenset(e)]+=1
print("닫힌 RP2: 모든 변이 삼각형 2개:", set(cnt.values())=={2}, "변 수", len(cnt))
X=[t for t in T if t!=(2,3,5)]
occ=defaultdict(list)
for i,t in enumerate(X):
    for e in it.combinations(t,2): occ[frozenset(e)].append(i)
arcs=[e for e,l in occ.items() if len(l)==2]; bd=[e for e,l in occ.items() if len(l)==1]
V=set(v for t in X for v in t)
print("조각 n=",len(X),"호 m=",len(arcs),"경계변",sorted(tuple(sorted(e)) for e in bd))
print("χ(X)=",len(V)-len(occ)+len(X), " m-n+1 =",len(arcs)-len(X)+1)
# 링크 조건: 각 정점의 링크(삼각형들의 맞은편 변)가 경로 또는 원
for v in V:
    L=nx.Graph([tuple(set(t)-{v}) for t in X if v in t])
    print(" 정점",v,"링크:", "원" if all(d==2 for _,d in L.degree()) else ("경로" if nx.is_connected(L) and max(d for _,d in L.degree())<=2 else "기타"))
W={2,3,5}
both=[e for e in arcs if e<=W]
print("양 끝이 W 위인 호:", both, "→ 엇갈림 그래프 I 의 변 0개 → 이분")
G=nx.Graph([tuple(e) for e in occ])
print("G =K6?", nx.is_isomorphic(G,nx.complete_graph(6)), " G 평면:", nx.check_planarity(G)[0])
# 홀로노미: 비가향 확인
