# researcher3 명제 E 공격: 각 공유부분은 '어떤' 매장에서 면 위에 있지만, 모든 공유부분을 동시에 면 위에 두는 매장은 없음
import networkx as nx
P = nx.complete_bipartite_graph(['u','v'], ['x','y','z','w'])
P = nx.Graph([(a,b) for a in 'uv' for b in 'xyzw'])
G = P.copy()
for q, S in [('q1','uxy'), ('q2','uxz'), ('q3','uyz')]:
    G.add_edges_from((q, s) for s in S)
    Gi = P.copy(); Gi.add_edges_from((q, s) for s in S)
    print(q, S, "단독 접착 평면", nx.check_planarity(Gi)[0])
print("두 개 q1,q2 평면", nx.check_planarity(nx.compose(P, nx.Graph([('q1',s) for s in 'uxy']+[('q2',s) for s in 'uxz'])))[0])
print("세 개 모두: G 평면", nx.check_planarity(G)[0], "V,E", G.number_of_nodes(), G.number_of_edges())
