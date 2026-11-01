# 정리 P9 의 계산 확인: C9 + 모든 독립 삼중쌍에 K_{1,1,3} 잎
from r04_lib import *
def chi_ordered(G, order):
    for k in range(1, 7):
        if col_ok(G, [], k, order) is not None: return k
def leaf_order(n, T):
    o=[]
    for v in range(n):
        o.append(v)
        for i,t in enumerate(T):
            if max(t)==v: o += [('h',i,1),('h',i,2)]
    return o
P = nx.cycle_graph(9)
T = [t for t in itertools.combinations(P.nodes(),3) if indep(P,t)]
G = assemble(P, T)
pieces = [P] + [G.subgraph(list(t)+[('h',i,1),('h',i,2)]).copy() for i,t in enumerate(T)]
print('잎 수', len(T), 'G 점/변', G.number_of_nodes(), G.number_of_edges())
print('조각 평면?', all(nx.check_planarity(Q)[0] for Q in pieces), '조각 chi', sorted({chi(Q) for Q in pieces}))
print('정규화(접합이 G 에서 독립)?', all(indep(G,t) for t in T))
print('변 덮음?', set(map(frozenset,G.edges()))==set().union(*[set(map(frozenset,Q.edges())) for Q in pieces]))
# 잎은 서로 C9 를 통해서만 만나므로, G 의 4-색칠 = C9 의 4-색칠 + 각 잎의 독립 확장. 전수(4^9) 로 직접 확인
def leaf_ext(c, t, k=4):
    return any(a!=b and a not in {c[v] for v in t} and b not in {c[v] for v in t} for a in range(k) for b in range(k))
cnt=0
for c in itertools.product(range(4), repeat=9):
    if any(c[i]==c[(i+1)%9] for i in range(9)): continue
    cnt+=1
    assert not all(leaf_ext(c,t) for t in T)
print('C9 의 4-색칠', cnt, '개 모두 어떤 잎에서 막힘 -> chi(G)>=5; 5-색칠 존재:', col_ok(G,[],5,leaf_order(9,T)) is not None)
S8 = [(0, 4, 7), (1, 5, 8), (2, 4, 7), (2, 4, 8), (2, 5, 7), (2, 5, 8), (3, 5, 8), (4, 6, 8)]
G8 = assemble(P, S8); print('8잎판 4-색 불가?', col_ok(P,S8) is None, G8.number_of_nodes(), G8.number_of_edges())
Q = nx.Graph([('a','b'),('b','c'),('a','c'),('x','b'),('x','c'),('y','a'),('y','c'),('z','a'),('z','b')]+
  [('p',w) for w in 'abxy']+[('q',w) for w in 'acxz']+[('r',w) for w in 'bcyz'])
print('E6 Q: 점연결도', nx.node_connectivity(Q), Q.number_of_nodes(), Q.number_of_edges())
