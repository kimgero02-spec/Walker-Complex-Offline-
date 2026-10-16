# 정리 P9 의 계산 확인: C9 + 모든 독립 삼중쌍에 K_{1,1,3} 잎
from r04_lib import *
P = nx.cycle_graph(9)
T = [t for t in itertools.combinations(P.nodes(),3) if indep(P,t)]
G = assemble(P, T)
pieces = [P] + [G.subgraph(list(t)+[('h',i,1),('h',i,2)]).copy() for i,t in enumerate(T)]
print('잎 수', len(T), 'G 점/변', G.number_of_nodes(), G.number_of_edges())
print('조각 평면?', all(nx.check_planarity(Q)[0] for Q in pieces), '조각 chi', sorted({chi(Q) for Q in pieces}))
print('정규화(접합이 G 에서 독립)?', all(indep(G,t) for t in T))
print('변 덮음?', set(map(frozenset,G.edges()))==set().union(*[set(map(frozenset,Q.edges())) for Q in pieces]))
print('G 4-색 가능?', col_ok(G, [], 4) is not None, ' 5-색 가능?', col_ok(G, [], 5) is not None)
S8 = [(0, 4, 7), (1, 5, 8), (2, 4, 7), (2, 4, 8), (2, 5, 7), (2, 5, 8), (3, 5, 8), (4, 6, 8)]
G8 = assemble(P, S8); print('8잎판 chi', chi(G8), G8.number_of_nodes(), G8.number_of_edges())
# E6 의 Q 의 연결도
Q = nx.Graph([('a','b'),('b','c'),('a','c'),('x','b'),('x','c'),('y','a'),('y','c'),('z','a'),('z','b')]+
  [('p',w) for w in 'abxy']+[('q',w) for w in 'acxz']+[('r',w) for w in 'bcyz'])
print('E6 Q: 점연결도', nx.node_connectivity(Q), Q.number_of_nodes(), Q.number_of_edges())
