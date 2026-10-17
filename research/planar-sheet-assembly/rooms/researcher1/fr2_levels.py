"""단계 1(A 평면) / 2(다중 접합점 A' 평면) / 3(G 평면) 을 가르는 예 E7, 그리고 E3 의 단계 2 실패 확인용 소규모 탐색."""
import itertools, networkx as nx
exec(open('fr2.py').read().split("def sq(c)")[0])
def sq(c): return [(c[i], c[(i + 1) % len(c)]) for i in range(len(c))]
# E7: W4 중심 류에 포트 셋 h(P1: h1,h3), h'(P2: h2), h''(P3: h4)
P = {1: sq([1,2,3,4]) + [('h',1),('h',3)], 2: [('h',2)], 3: [('h',4)]}
cl = [[(1,'h'),(2,'h'),(3,'h')], [(1,2),(2,2)], [(1,4),(3,4)]]
A = build(P, cl)
info('E7', A, 4)
print('  G iso W4:', nx.is_isomorphic(nx.Graph(recover(A)[0]), nx.wheel_graph(5)))
# 다중 접합점 A': 중심 류의 흰 점을 둘로: w1~{h,h'}, w2~{h,h''}
A2 = A.copy(); A2.remove_node(('w', 0))
A2.add_node('w1', c='W'); A2.add_node('w2', c='W')
A2.add_edges_from([('w1',(1,'h')),('w1',(2,'h')),('w2',(1,'h')),('w2',(3,'h'))])
print('  A\' (두 흰 점) planar:', nx.check_planarity(A2)[0])
MG = A2.copy()
# 같은 류(흰-검정 성분) 오므리기 → W4 확인
B = nx.Graph(); rep = {}
H = nx.Graph(); H.add_edges_from((u, v) for u, v in A2.edges if 'W' in (A2.nodes[u]['c'], A2.nodes[v]['c']))
for comp in nx.connected_components(H):
    r = min(x for x in comp if A2.nodes[x]['c'] == 'B')
    for x in comp: rep[x] = r
G2 = nx.Graph((rep.get(u, u), rep.get(v, v)) for u, v in A2.subgraph(black(A2)).edges)
print('  A\' contracts to W4:', nx.is_isomorphic(G2, nx.wheel_graph(5)))
# E3: 류 {h,h'} 에 흰 점 k 개 (k=1..3), 각 흰 점이 h,h' 에 연결 → 모두 비평면인지 (정리 NX 의 특수 경우 확인)
P3 = {1: sq([1,2,3,4]) + [('h',1),('h',3)], 2: [('h',2),('h',4)]}
for k in (1, 2, 3):
    A3 = build(P3, [[(1,2),(2,2)],[(1,4),(2,4)]])
    for i in range(k):
        A3.add_node(('s', i), c='W'); A3.add_edges_from([(('s', i),(1,'h')),(('s', i),(2,'h'))])
    print('  E3 with %d parallel whites: planar=%s' % (k, nx.check_planarity(A3)[0]))
