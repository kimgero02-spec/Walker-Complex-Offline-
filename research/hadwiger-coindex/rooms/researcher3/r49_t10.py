# 부착 집합의 면 덮개수 phi (Bienstock–Monma 의 face cover) : 정이십면체 전체, 가젯 단위 U 의 두 쪽
import networkx as nx, itertools
from r49_ladder import ccw_rot, face_list
def phi(B, A):
    F=[set(f) for f in face_list(ccw_rot(B))]
    for k in range(1,len(F)+1):
        for c in itertools.combinations(F,k):
            if set(A) <= set().union(*c): return k
I=nx.icosahedral_graph(); print('phi(icosahedron, all 12) =',phi(I,range(12)))
p,q,r,s,P,Q_,R=range(7)
A=nx.Graph(); A.add_edges_from(itertools.combinations([p,q,r,s],2))
A.add_edges_from([(P,q),(P,r),(P,s),(Q_,p),(Q_,r),(Q_,s),(R,p),(R,q),(R,s)])
print('phi(Apollonian A, {p,q,r,P,Q,R}) =',phi(A,[p,q,r,P,Q_,R]))
K4=nx.complete_graph(4); print('phi(K4, all)=',phi(K4,range(4)),' phi(K3,all)=',phi(nx.complete_graph(3),range(3)))
