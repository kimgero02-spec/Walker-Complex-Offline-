"""F-R3: 마이너 언어. (a) E3 의 A 에서 쿠라토프스키 부분그래프가 별을 쪼개는지,
(b) K4 마이너가 A 에는 있고 G 에는 없는 예 (직렬-병렬 축약으로 판정)."""
import itertools, networkx as nx
exec(open('fr2.py').read().split("def sq(c)")[0])
def sq(c): return [(c[i], c[(i + 1) % len(c)]) for i in range(len(c))]

def has_K4_minor(g):
    """K4 마이너 없음 <=> 직렬-병렬 축약(차수<=2 제거·억제, 다중변 병합)으로 사라짐."""
    M = nx.MultiGraph(g); changed = True
    while changed:
        changed = False
        for u, v in list(M.edges()):
            pass
        S = nx.Graph()
        for u, v in M.edges():
            if u != v: S.add_edge(u, v)
        S.add_nodes_from(M.nodes)
        M = nx.MultiGraph(S)
        for v in list(M.nodes):
            d = M.degree(v)
            if d <= 1:
                M.remove_node(v); changed = True; break
            if d == 2:
                nb = [x for x in M.neighbors(v)]
                if len(set(nb)) == 2:
                    a, b = nb; M.remove_node(v); M.add_edge(a, b); changed = True; break
                else:
                    M.remove_node(v); changed = True; break
    return M.number_of_nodes() > 0

# (a) E3
P3 = {1: sq([1,2,3,4]) + [('h',1),('h',3)], 2: [('h',2),('h',4)]}
A = build(P3, [[(1,'h'),(2,'h')],[(1,2),(2,2)],[(1,4),(2,4)]])
ok, K = nx.check_planarity(A, counterexample=True)
deg = sorted(d for _, d in K.degree() if d >= 3)
print('E3: A planar', ok, '; Kuratowski subgraph branch-vertex degrees', deg, '; nodes', sorted(map(str, K.nodes)))
# (b) 직렬-병렬 G 에서 포트를 엇갈리게 쪼갠 설명서: G = K_{2,3}(a,b | x,y,z) 에 변 xy 추가? 우선 후보 몇 개.
cands = {}
# G1 = C4 (1234) + 대각선 13 (직렬-병렬). 정점 1 의 변 12,13,14 중 13 만 다른 조각으로.
cands['C4+13, split 1: {12,14}|{13}'] = build({1: [(1,2),(2,3),(3,4),(4,1)], 2: [(1,3)]},
                                            [[(1,1),(2,1)],[(1,3),(2,3)]])
# G2 = K_{2,3}, a 의 변 ax,az | ay, b 의 변 bx,bz | by 로 쪼갬
cands['K23 split a,b'] = build({1: [('a','x'),('a','z'),('b','x'),('b','z')], 2: [('a','y'),('b','y')]},
                               [[(1,'a'),(2,'a')],[(1,'b'),(2,'b')]])
# G3 = 사다리 C6+현 (프리즘 아닌 직렬병렬: 경로 1-2-3, 4-5-6, 가로대 14,25,36 은 K4 마이너 있음) -> 대신 바퀴 없는 C5+두 현 13,14 (부채꼴, 직렬병렬)
cands['fan 1:{12,15,14}|{13}'] = build({1: [(1,2),(2,3),(3,4),(4,5),(5,1),(1,4)], 2: [(1,3)]},
                                     [[(1,1),(2,1)],[(1,3),(2,3)]])
cands['fan 1:{12,14}|{13,15}'] = build({1: [(1,2),(2,3),(3,4),(4,5),(1,4)], 2: [(1,3),(1,5)]},
                                     [[(1,1),(2,1)],[(1,3),(2,3)],[(1,5),(2,5)]])
for name, A in cands.items():
    G = nx.Graph(recover(A)[0])
    print('%-28s G:K4minor=%s planar=%s | A:K4minor=%s planar=%s' % (name, has_K4_minor(G), nx.check_planarity(G)[0],
          has_K4_minor(A), nx.check_planarity(A)[0]))
print('sanity K4', has_K4_minor(nx.complete_graph(4)), 'C5', has_K4_minor(nx.cycle_graph(5)), 'K23', has_K4_minor(nx.complete_bipartite_graph(2,3)))
