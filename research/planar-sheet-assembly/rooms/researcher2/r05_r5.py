# R05: 추측 R5 (평면 L, 독립 삼중쌍 T -> 5-색 무지개) 의 증명을 알고리즘으로 옮겨
# 구조적 후보에서 실행하고, 출력 색칠을 독립적으로 검사한다.
import itertools, sys
import networkx as nx
sys.setrecursionlimit(10000)

def color(G, k, pre=None, neq=()):
    """백트래킹 k-색칠. pre: 미리 정한 색, neq: 서로 달라야 할 점 쌍."""
    pre = dict(pre or {})
    H = nx.Graph(G); H.add_edges_from(neq)
    order = sorted(H.nodes(), key=lambda u: -H.degree(u))
    c = dict(pre)
    def rec():
        free = [u for u in H if u not in c]
        if not free: return True
        u = max(free, key=lambda w: (len({c[x] for x in H[w] if x in c}), H.degree(w)))
        used = {c[x] for x in H[u] if x in c}
        for col in range(k):
            if col not in used:
                c[u] = col
                if rec(): return True
                del c[u]
        return False
    return dict(c) if rec() else None

def proper(G, c): return all(c[u] != c[v] for u, v in G.edges())
def rainbow(c, T): return len({c[t] for t in T}) == 3
def planar(G): return nx.check_planarity(G)[0]

LOG = []
def solve(L, T):
    """증명의 각 단계를 그대로 실행. 반환: T 무지개인 적정 5-색칠."""
    L = nx.Graph(L); n = L.number_of_nodes()
    if n <= 5:
        return {u: i for i, u in enumerate(L.nodes())}
    # 보조정리 B: T 의 두 점을 이어도 평면이면 4색 정리 + 보조정리 A
    for x, y in itertools.combinations(T, 2):
        L2 = nx.Graph(L); L2.add_edge(x, y)
        if planar(L2):
            c = color(L2, 4); LOG.append('B')
            return lemmaA(c, T)
    # 보조정리 C: 극대화 (T 간선은 이미 못 넣음)
    for u, v in itertools.combinations(list(L.nodes()), 2):
        if not L.has_edge(u, v) and not ({u, v} <= set(T)):
            L.add_edge(u, v)
            if not planar(L): L.remove_edge(u, v)
    assert L.number_of_edges() == 3 * n - 6
    _, emb = nx.check_planarity(L)
    # 보조정리 D: T 밖 차수 <=4
    for v in L:
        if v not in T and L.degree(v) <= 4:
            c = solve(L.subgraph([u for u in L if u != v]), T); LOG.append('D')
            c[v] = min(set(range(5)) - {c[u] for u in L[v]}); return c
    # 보조정리 E: T 밖 차수 5
    for v in L:
        if v in T or L.degree(v) != 5: continue
        cyc = list(emb.neighbors_cw_order(v))
        U = [u for u in cyc if u not in T]
        for a, b in itertools.combinations(U, 2):
            if not L.has_edge(a, b):
                w = ('w', v)
                L2 = nx.Graph(L.subgraph([u for u in L if u not in (v, a, b)]))
                L2.add_node(w)
                for u in set(L[v]) | set(L[a]) | set(L[b]):
                    if u not in (v, a, b): L2.add_edge(w, u)
                c2 = solve(L2, T); LOG.append('E-contract')
                c = {u: c2[u] for u in L2 if u != w}
                c[a] = c[b] = c2[w]
                c[v] = min(set(range(5)) - {c[u] for u in L[v]}); return c
        # U 가 클리크 -> 현 v_i v_{i+2} (둘 다 T 밖) -> 분리 삼각형
        for i in range(5):
            a, b = cyc[i], cyc[(i + 2) % 5]
            if a not in T and b not in T and L.has_edge(a, b):
                LOG.append('E-chord->S')
                return lemmaS(L, T, (v, a, b))
        raise AssertionError('E 실패')
    raise AssertionError('오일러 모순이어야 함: T 밖 차수<=5 점 없음')

def lemmaA(c, T):
    vals = [c[t] for t in T]
    if len(set(vals)) == 3: return c
    assert len(set(vals)) == 2, '단색: 보조정리 A 적용 불가'
    for t in T:
        if sum(c[s] == c[t] for s in T) == 2:
            c = dict(c); c[t] = 4; return c

def lemmaS(L, T, D):
    R = L.subgraph([u for u in L if u not in D])
    comps = [set(C) for C in nx.connected_components(R)]
    assert len(comps) >= 2, '분리 삼각형 아님'
    where = {t: next(i for i, C in enumerate(comps) if t in C) for t in T}
    if len(set(where.values())) == 1:
        i = where[T[0]]; A = comps[i]; B = set().union(*[C for j, C in enumerate(comps) if j != i])
        cA = solve(L.subgraph(A | set(D)), T); cB = color(L.subgraph(B | set(D)), 5)
        LOG.append('S-oneside'); return glue(cA, cB, D)
    complete = {t: all(L.has_edge(t, d) for d in D) for t in T}
    assert not all(complete.values()), 'K33 이어야 함'
    # 외톨이 u (부분 P), 짝 {w1,w2} (부분 Q), 짝 중 하나는 Δ 에 완전하지 않음
    for u in T:
        P = comps[where[u]]
        if any(where[t] == where[u] for t in T if t != u): continue
        w1, w2 = [t for t in T if t != u]
        if complete[w1] and complete[w2]: continue
        y, z = (w1, w2) if not complete[w1] else (w2, w1)
        a = next(d for d in D if not L.has_edge(y, d))
        Q = set().union(*[C for j, C in enumerate(comps) if j != where[u]])
        GB = L.subgraph(Q | set(D)); GA = L.subgraph(P | set(D))
        cB = color(GB.subgraph([q for q in GB if q not in (y, a)]), 4); cB[y] = cB[a] = 4
        cA = color(GA.subgraph([q for q in GA if q != u]), 4); cA[u] = 4
        # 순열: Δ 맞추고 cA 의 비Δ 색을 cB 의 비Δ 색으로, u 의 색이 z 와 다르게
        nonA = [k for k in range(5) if k not in {cA[d] for d in D}]
        nonB = [k for k in range(5) if k not in {cB[d] for d in D}]
        for order in (nonB, nonB[::-1]):
            pi = {cA[d]: cB[d] for d in D}; pi.update(dict(zip(nonA, order)))
            if pi[cA[u]] != cB[z]:
                c = dict(cB); c.update({q: pi[cA[q]] for q in GA}); LOG.append('S-split'); return c
    # 짝이 둘 다 완전 -> 서로 다른 성분: 재분할 (위 루프가 이를 포함하지 못하면 실패)
    raise AssertionError('S 재분할 실패')

def glue(cA, cB, D):
    nonA = [k for k in range(5) if k not in {cA[d] for d in D}]
    nonB = [k for k in range(5) if k not in {cB[d] for d in D}]
    pi = {cB[d]: cA[d] for d in D}; pi.update(dict(zip(nonB, nonA)))
    c = dict(cA); c.update({q: pi[cB[q]] for q in cB}); return c

def check(name, L, T):
    LOG.clear()
    if not planar(L):
        print(f'{name}: 비평면 -> 후보 아님'); return None
    assert all(not L.has_edge(a, b) for a, b in itertools.combinations(T, 2))
    c = solve(L, T)
    ok = proper(L, c) and rainbow(c, T) and set(c.values()) <= set(range(5))
    four_rain = color(L, 4, neq=[(T[0], T[1]), (T[1], T[2]), (T[0], T[2])]) is not None
    four_nonmono = any(color(L, 4, neq=[p]) is not None for p in itertools.combinations(T, 2))
    print(f'{name}: n={L.number_of_nodes()} 증명-알고리즘 출력 검사={ok} '
          f'4색무지개={four_rain} 4색비단색={four_nonmono} 단계={LOG}')
    return ok

if __name__ == '__main__':
    # 후보 1: K5-e 사슬 (모든 4-색칠에서 x=y=z 강제), 삼각분할로 보충됨(solve 안에서)
    G = nx.Graph()
    def k5e(p, q, tri):
        a, b, c = tri; G.add_edges_from([(a, b), (b, c), (a, c)])
        for s in (p, q):
            for t in tri: G.add_edge(s, t)
    k5e('x', 'y', ('a1', 'b1', 'c1')); k5e('y', 'z', ('a2', 'b2', 'c2'))
    check('K5-e 사슬', G, ('x', 'y', 'z'))
    # 후보 1': 사슬을 원형으로 닫기 (x-z 도 강제)
    G3 = nx.Graph(G);
    for t in ('a3', 'b3', 'c3'): G3.add_edge('x', t); G3.add_edge('z', t)
    G3.add_edges_from([('a3', 'b3'), ('b3', 'c3'), ('a3', 'c3')])
    check('K5-e 고리(3개)', G3, ('x', 'y', 'z'))
    # 후보 2: 적층 삼각분할 (유일 4-색), T 는 한 색 클래스의 서로 면 공유 안 하는 독립 삼중쌍
    S = nx.Graph([(0, 1), (1, 2), (0, 2)]); faces = [(0, 1, 2), (0, 1, 2)]; nxt = 3
    import random; random.seed(5)
    for _ in range(14):
        f = faces.pop(random.randrange(len(faces)))
        for t in f: S.add_edge(nxt, t)
        faces += [(f[0], f[1], nxt), (f[1], f[2], nxt), (f[0], f[2], nxt)]; nxt += 1
    c4 = color(S, 4)
    cls = [u for u in S if c4[u] == c4[3]]
    facepairs = {frozenset(p) for f in faces for p in itertools.combinations(f, 2)}
    Ts = [t for t in itertools.combinations(cls, 3)
          if not any(frozenset(p) in facepairs for p in itertools.combinations(t, 2))]
    print('적층: 같은 색 클래스', cls, '면 공유 없는 삼중쌍 수', len(Ts))
    if Ts: check('적층 삼각분할', S, Ts[0])
    # 후보 3: C9 이중 바퀴 (4-연결), T = {0,3,6}
    W = nx.cycle_graph(9)
    for i in range(9): W.add_edge('N', i); W.add_edge('S', i)
    check('C9 이중바퀴', W, (0, 3, 6))
    # 후보 4: 정이십면체 (4-연결? 5-연결), T = 거리 2 독립 삼중쌍
    I = nx.icosahedral_graph()
    T = next(t for t in itertools.combinations(I, 3)
             if all(not I.has_edge(a, b) for a, b in itertools.combinations(t, 2)))
    check('정이십면체', I, T)
    # 후보 5: C9 을 각 점에 K_{1,1,3} 잎 대신 삼각형 귀로 둘러싼 4-연결 평면 그래프
    A = nx.cycle_graph(9)
    for i in range(9): A.add_edge(('o', i), i); A.add_edge(('o', i), (i + 1) % 9); A.add_edge(('o', i), ('o', (i + 1) % 9)); A.add_edge('N', i); A.add_edge('S', ('o', i))
    check('C9 반짝이(antiprism+극)', A, (0, 3, 6))
    # 4점 판의 반례: K_{1,1,4} (R5 를 |T|=4 로 늘리면 거짓)
    K = nx.complete_multipartite_graph(1, 1, 4)
    print('K_{1,1,4} 평면?', planar(K), ' 4점 무지개 5-색칠?',
          color(K, 5, neq=list(itertools.combinations([2, 3, 4, 5], 2))) is not None)

def glue_on_face(G1, f1, G2, f2, tag):
    """G2 의 면 f2 를 G1 의 면 f1 에 붙임 (분리 삼각형 생성)."""
    m = {f2[i]: f1[i] for i in range(3)}
    H = nx.Graph(G1)
    for u, v in G2.edges():
        H.add_edge(m.get(u, (tag, u)), m.get(v, (tag, v)))
    return H

def test_S():
    I = nx.icosahedral_graph()
    f = next(t for t in itertools.combinations(I, 3) if all(I.has_edge(a, b) for a, b in itertools.combinations(t, 2)))
    H = glue_on_face(I, f, I, f, 'o')
    D = f
    inside = [u for u in I if u not in f]
    outside = [('o', u) for u in inside]
    x = inside[0]
    yz = next(p for p in itertools.combinations(outside, 2) if not H.has_edge(*p))
    T = (x,) + yz
    assert planar(H)
    LOG.clear(); c = lemmaS(H, T, D)
    print('S 시험1 (이십면체 둘, 1|2 분할):', proper(H, c) and rainbow(c, T), LOG)
    # 시험2: 외톨이 x 가 Δ 에 완전 (K4 안쪽), 짝 y,z 는 바깥 이십면체
    H2 = nx.Graph(I); H2.add_edges_from([('x', d) for d in f])
    yz = next(p for p in itertools.combinations(inside, 2) if not I.has_edge(*p))
    T2 = ('x',) + yz
    assert planar(H2)
    LOG.clear(); c = lemmaS(H2, T2, f)
    print('S 시험2 (x 가 Δ 에 완전):', proper(H2, c) and rainbow(c, T2), LOG)
    # 시험3: 세 점이 모두 다른 성분 (Δ 안쪽 x, 바깥 이십면체 안 y, 그리고 또 하나의 붙임 성분 안 z)
    f2 = next(t for t in itertools.combinations(I, 3) if all(I.has_edge(a, b) for a, b in itertools.combinations(t, 2)) and t != f)
    H3 = glue_on_face(H, f2, I, f, 'p')  # 바깥 쪽 다른 면에 붙임: 다른 분리 삼각형
    print("S 시험3 평면?", planar(H3))
test_S()

def test_S4():
    H = nx.Graph([('a','b'),('b','c'),('a','c')])
    for s in 'yz':
        for d in 'abc': H.add_edge(s, d)
    H.add_edges_from([('w','z'),('w','a'),('w','b'),('x','w'),('x','a'),('x','b')])
    assert planar(H)
    T = ('x','y','z'); LOG.clear(); c = lemmaS(H, T, ('a','b','c'))
    print('S 시험4 (y,z 둘 다 Δ 에 완전, x 는 z 쪽 성분):', proper(H, c) and rainbow(c, T), LOG, c)
test_S4()
