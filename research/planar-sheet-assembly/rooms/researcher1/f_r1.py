"""F-R1: 테 접합 그래프 R (검정=조각 점, 흰=접합점, 회색=테 표지) 에서
G 복원, 정리 A 수열, 리본 데이터(H, [eps], b, I) 를 읽는다. 결정적 예만."""
import itertools, networkx as nx

def chrom(g):
    nodes = sorted(g.nodes, key=lambda v: -g.degree(v))
    if not nodes: return 0
    for q in range(1, len(nodes)+1):
        col = {}
        def bt(i):
            if i == len(nodes): return True
            v = nodes[i]; used = {col[u] for u in g[v] if u in col}
            for c in range(q):
                if c not in used:
                    col[v] = c
                    if bt(i+1): return True
                    del col[v]
            return False
        if bt(0): return q
    return None

def build(pieces, rims, classes):
    """pieces: {k: list of edges on labels}; rims: {k: cyclic list}; classes: list of list of (k,label)."""
    R = nx.Graph()
    for k, E in pieces.items():
        for (a, b) in E:
            R.add_edge((k, a), (k, b))
        for v in {x for e in E for x in e}:
            R.nodes[(k, v)]['c'] = 'B'
    for k, cyc in rims.items():
        for i in range(len(cyc)):
            a, b = cyc[i], cyc[(i+1) % len(cyc)]
            assert R.has_edge((k, a), (k, b)), (k, a, b)
            g = ('g', k, a, b); R.add_node(g, c='R'); R.add_edge(g, (k, a)); R.add_edge(g, (k, b))
    for j, cl in enumerate(classes):
        w = ('w', j); R.add_node(w, c='W')
        for p in cl: R.add_edge(w, p)
    return R

def black(R): return [v for v in R if R.nodes[v]['c'] == 'B']
def whites(R): return [v for v in R if R.nodes[v]['c'] == 'W']

def junction(R):  # 𝔄 = R 에서 회색 삭제
    return R.subgraph([v for v in R if R.nodes[v]['c'] != 'R']).copy()

def recover(R):
    rep = {v: v for v in black(R)}
    for w in whites(R):
        ports = list(R[w]); r = min(ports)
        for p in ports: rep[p] = r
    G = nx.Graph(); G.add_nodes_from(set(rep.values()))
    for a, b in R.subgraph(black(R)).edges:
        assert rep[a] != rep[b], 'loop'
        G.add_edge(rep[a], rep[b])
    return G, rep

def subst(A, t):
    S = A.subgraph(black(A)).copy()
    for w in whites(A):
        cl = [(w, i) for i in range(t)]
        S.add_nodes_from(cl)
        S.add_edges_from(itertools.combinations(cl, 2))
        for c in cl:
            for p in A[w]: S.add_edge(c, p)
    return S

def seqA(R, T):
    A = junction(R)
    return [chrom(subst(A, t)) for t in range(T+1)]

def rims_of(R):
    """회색 표지에서 테 C_k 를 읽는다 (조각별 순환 순서)."""
    rim_edges = {}
    for g in R:
        if R.nodes[g]['c'] == 'R':
            a, b = list(R[g]); rim_edges.setdefault(a[0], []).append((a, b))
    rims = {}
    for k, E in rim_edges.items():
        C = nx.Graph(E); assert all(d == 2 for _, d in C.degree) and nx.is_connected(C)
        cyc = [e[0] for e in nx.find_cycle(C)]
        rims[k] = cyc
    return rims, {k: {frozenset(e) for e in E} for k, E in rim_edges.items()}

def ribbon(R):
    rims, rimE = rims_of(R)
    W = whites(R)
    port = {w: {p[0]: p for p in R[w]} for w in W}
    assert all(len(R[w]) == 2 and len(port[w]) == 2 for w in W), '흰 점 차수 2, 서로 다른 조각'
    # 호: 두 흰 점의 포트가 양쪽 테에서 모두 이웃
    Agr = nx.Graph(); Agr.add_nodes_from(W)
    for w, x in itertools.combinations(W, 2):
        if set(port[w]) == set(port[x]):
            if all(frozenset((port[w][k], port[x][k])) in rimE[k] for k in port[w]):
                Agr.add_edge(w, x)
    arcs = [sorted(c) for c in nx.connected_components(Agr)]
    eps = []
    for arc in arcs:
        i, j = sorted(port[arc[0]])
        assert len(arc) >= 2, '호는 변이 1개 이상'
        w0, w1 = next(iter(Agr.subgraph(arc).edges))
        def d(k):
            cyc = rims[k]; a, b = cyc.index(port[w0][k]), cyc.index(port[w1][k])
            return +1 if (b - a) % len(cyc) == 1 else -1
        eps.append((i, j, -d(i)*d(j)))
    # 가향성 [eps]=0 ?
    H = nx.MultiGraph(); H.add_nodes_from(rims)
    for (i, j, e) in eps: H.add_edge(i, j, eps=e)
    s = {}; orient = True
    for comp in nx.connected_components(H):
        r = next(iter(comp)); s[r] = 1; st = [r]
        while st:
            u = st.pop()
            for _, v, dd in H.edges(u, data=True):
                need = s[u]*dd['eps']
                if v not in s: s[v] = need; st.append(v)
                elif s[v] != need: orient = False
    # 경계 ∂X: 호 아닌 테 변 (G 에서)
    G, rep = recover(R)
    arcE = set()
    for arc in arcs:
        for w, x in Agr.subgraph(arc).edges:
            for k in port[w]: arcE.add(frozenset((port[w][k], port[x][k])))
    bd = nx.Graph()
    for k, E in rimE.items():
        for e in E:
            if e not in arcE:
                a, b = tuple(e); bd.add_edge(rep[a], rep[b])
    b = nx.number_connected_components(bd)
    n, m = H.number_of_nodes(), H.number_of_edges()
    out = dict(n=n, m=m, eps=eps, orientable=orient, b=b, chiX=n-m,
               sphere=(orient and n-m+b == 2))
    if b == 1:
        Wc = [e[0] for e in nx.find_cycle(bd)]
        ends = []
        for arc in arcs:
            sub = Agr.subgraph(arc); e = [w for w in arc if sub.degree(w) <= 1]
            ends.append({rep[min(R[w])] for w in e})
        I = nx.Graph(); I.add_nodes_from(range(len(arcs)))
        for a, c in itertools.combinations(range(len(arcs)), 2):
            if len(ends[a] | ends[c]) < 4: continue
            lab = [0 if v in ends[a] else 1 for v in Wc if v in ends[a] | ends[c]]
            if all(lab[t] != lab[t+1] for t in range(3)): I.add_edge(a, c)
        out['I_edges'] = list(I.edges); out['I_bip'] = nx.is_bipartite(I)
    return out

def report(name, R, T=5, rib=True):
    G, _ = recover(R)
    A = junction(R)
    print('==', name)
    print('  G: n=%d m=%d  chi=%d  planar=%s' % (G.number_of_nodes(), G.number_of_edges(), chrom(G), nx.check_planarity(G)[0]))
    print('  seq chi(A^(t)), t=0..%d:' % T, seqA(R, T), '  A planar:', nx.check_planarity(A)[0])
    if rib:
        print('  ribbon:', ribbon(R))
    return G

def sq(k, cyc):  # 다각형 조각
    return [(cyc[i], cyc[(i+1) % len(cyc)]) for i in range(len(cyc))]

if __name__ == '__main__':
    # 예1a: K4 = (K4-uv) ∪ K2  (색칠 층만; K2 는 원판 조각 아님)
    R = build({1: [('u','a'),('u','b'),('v','a'),('v','b'),('a','b')], 2: [('u','v')]},
              {1: ['u','a','v','b']}, [[(1,'u'),(2,'u')], [(1,'v'),(2,'v')]])
    G = report('K4=(K4-uv)+K2', R, rib=False)
    print('  iso K4:', nx.is_isomorphic(G, nx.complete_graph(4)))
    # 예1b: K4 = 정사각형 2장 뫼비우스 (리본 설명서)
    R = build({1: sq(1, [0,1,3,2]), 2: sq(2, [0,3,1,2])}, {1: [0,1,3,2], 2: [0,3,1,2]},
              [[(1,v),(2,v)] for v in range(4)])
    G = report('K4 = 2 squares Moebius', R)
    print('  iso K4:', nx.is_isomorphic(G, nx.complete_graph(4)))
    # 예2: 정사각형 k 장 띠, 곧게 / 한 번 꼬아
    for k in (3, 4):
        for twist in (0, 1):
            pieces, rims, cls = {}, {}, []
            for i in range(k):
                cyc = [('t', i), ('t', i+1), ('s', i+1), ('s', i)]
                if twist and i == k-1:
                    cyc = [('t', i), ('s', 0), ('t', 0), ('s', i)]   # 마지막 가로대를 뒤집어 붙임
                pieces[i] = sq(i, cyc); rims[i] = cyc
            for i in range(k):
                j = (i+1) % k
                if i == k-1:
                    a, b = (('t',0),('s',0)) if twist else (('t',k),('s',k))
                    a0, b0 = ('t',0), ('s',0)
                    if twist: cls += [[(i, ('s',0)), (j, ('t',0))], [(i, ('t',0)), (j, ('s',0))]]
                    else: cls += [[(i, ('t',k)), (j, ('t',0))], [(i, ('s',k)), (j, ('s',0))]]
                else:
                    cls += [[(i, ('t',i+1)), (j, ('t',i+1))], [(i, ('s',i+1)), (j, ('s',i+1))]]
            R = build(pieces, rims, cls)
            G = report('band k=%d twist=%d' % (k, twist), R, T=4)
            tgt = nx.circular_ladder_graph(k) if not twist else nx.circulant_graph(2*k, [1, k])
            print('  iso target:', nx.is_isomorphic(G, tgt))
    # 예3: K5 = W4 ∪ C4 (R01): W4 테 a b d c, 중심 e; C4 a b c d; 호 ab, cd
    W4 = [('a','b'),('b','d'),('d','c'),('c','a'),('e','a'),('e','b'),('e','c'),('e','d')]
    R = build({1: W4, 2: sq(2, ['a','b','c','d'])}, {1: ['a','b','d','c'], 2: ['a','b','c','d']},
              [[(1,v),(2,v)] for v in 'abcd'])
    G = report('K5 = W4 + C4', R)
    print('  iso K5:', nx.is_isomorphic(G, nx.complete_graph(5)))
