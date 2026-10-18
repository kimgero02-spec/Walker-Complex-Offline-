# 예측 Πσ 의 시험: K6-e (모든 K5 모형에 한 점 가지 집합이 있음) 의 sub¹ 에서 표적 M°(D) 찾기
import networkx as nx, itertools as it, sys
from r17_hM import has_minor, Mcirc, decomps
G0=nx.complete_graph(6); G0.remove_edge(4,5); S=nx.Graph()
for u,v in G0.edges(): S.add_edge(u,('s',u,v)); S.add_edge(('s',u,v),v)
Ds=decomps(S.number_of_nodes()); E5=list(it.combinations(range(5),2))
Xs=[]
for D in Ds:
    X=Mcirc(5,[[E5[i] for i in P] for P in D])
    if X.number_of_edges()>S.number_of_edges(): continue
    if any(nx.is_isomorphic(X,Y) for Y in Xs if Y.number_of_nodes()==X.number_of_nodes() and Y.number_of_edges()==X.number_of_edges()): continue
    Xs.append(X)
print('candidates',len(Xs),flush=True)
for X in sorted(Xs,key=lambda X:X.number_of_nodes()):
    m=has_minor(S,X,maxset=6)
    if m: print('FOUND',X.number_of_nodes(),{str(k):sorted(map(str,v)) for k,v in m.items()}); break
else: print('none found (maxset 6)')
