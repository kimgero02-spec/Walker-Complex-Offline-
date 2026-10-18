# R04 researcher1: 나무형 설명서의 최소-최대 전파 공식 (정확 계산, 작은 예만)
import itertools, networkx as nx
INF = float('inf')

def chi(G):
    nodes = sorted(G.nodes(), key=lambda v: -G.degree(v))
    if not nodes: return 0
    for k in range(1, len(nodes) + 1):
        col = {}
        def bt(i):
            if i == len(nodes): return True
            v = nodes[i]; used = {col[w] for w in G[v] if w in col}
            for c in range(min(k, max(col.values(), default=-1) + 2)):
                if c not in used:
                    col[v] = c
                    if bt(i + 1): return True
                    del col[v]
            return False
        if bt(0): return k

def partitions(S):
    if not S: yield []; return
    f, rest = S[0], S[1:]
    for p in partitions(rest):
        for i in range(len(p)): yield p[:i] + [[f] + p[i]] + p[i + 1:]
        yield [[f]] + p

def canon(pi):
    return frozenset(frozenset(B) for B in pi)

def restrict(pi, S):
    S = set(S)
    return canon([set(B) & S for B in pi if set(B) & S])

def chi_pi(P, pi):
    for B in pi:
        for a, b in itertools.combinations(B, 2):
            if P.has_edge(a, b): return INF
    Q = nx.Graph(P); reps = []
    for B in pi:
        B = list(B); r = B[0]
        for x in B[1:]: Q = nx.Graph(nx.contracted_nodes(Q, r, x, self_loops=False))
        reps.append(r)
    Q.add_edges_from(itertools.combinations(reps, 2))
    return chi(Q)

def tree_formula(pieces, Hedges, root=0, cap=None, marginal=False):
    """최소-최대 전파. pieces: dict k->Graph, Hedges: 나무 변 목록.
    marginal=True 이면 조각 프로필을 접합별 주변값으로 쪼갠 (틀린) 근사."""
    H = nx.Graph(Hedges); H.add_nodes_from(pieces)
    assert nx.is_tree(H)
    # 나무 분해 조건 확인
    for x in set().union(*[set(P) for P in pieces.values()]):
        assert nx.is_connected(H.subgraph([k for k in pieces if x in pieces[k]]))
    S = {frozenset(e): sorted(set(pieces[e[0]]) & set(pieces[e[1]]), key=str) for e in Hedges}
    U = {k: sorted(set().union(*[S[frozenset((k, l))] for l in H[k]]) if H[k] else set(), key=str) for k in pieces}
    prof = {k: {canon(pi): chi_pi(pieces[k], pi) for pi in partitions(U[k])} for k in pieces}
    if cap is not None:
        prof = {k: {p: min(v, cap) for p, v in d.items()} for k, d in prof.items()}
    def msg(l, p):  # mu_{l->p}(sigma), sigma in Pi(S_lp)
        Slp = S[frozenset((l, p))]
        kids = [c for c in H[l] if c != p]
        km = {c: msg(c, l) for c in kids}
        out = {}
        for pi, v in prof[l].items():
            val = max([v] + [km[c][restrict(pi, S[frozenset((l, c))])] for c in kids])
            s = restrict(pi, Slp); out[s] = min(out.get(s, INF), val)
        return out
    if not marginal:
        km = {c: msg(c, root) for c in H[root]}
        return min(max([v] + [km[c][restrict(pi, S[frozenset((root, c))])] for c in H[root]])
                   for pi, v in prof[root].items())
    # 주변 근사: 각 q 에서 조각의 접합별 주변 허용 집합만으로 판정 (조각 안의 결합 정보 버림)
    m = max(chi(P) for P in pieces.values())
    for q in range(m, 100):
        ok = True
        allowed = {}  # (k, l) -> Pi(S_kl) 의 허용 집합 (조각 k 의 주변)
        for (k, l) in [(a, b) for e in Hedges for (a, b) in (e, e[::-1])]:
            allowed[(k, l)] = {restrict(pi, S[frozenset((k, l))]) for pi, v in prof[k].items() if v <= q}
        for e in Hedges:
            a, b = e
            if not (allowed[(a, b)] & allowed[(b, a)]): ok = False
        if ok: return q

def g(edges, nodes=()):
    G = nx.Graph(); G.add_nodes_from(nodes); G.add_edges_from(edges); return G

def run(name, pieces, Hedges, root=0, extra=True):
    G = nx.compose_all(list(pieces.values()))
    m = max(chi(P) for P in pieces.values())
    f = tree_formula(pieces, Hedges, root)
    line = f"{name}: chi(P_k)={[chi(P) for P in pieces.values()]} m={m} | chi(G)={chi(G)} | 공식={f}"
    if extra:
        line += f" | 주변근사={tree_formula(pieces, Hedges, root, marginal=True)}"
    print(line)
    return f

if __name__ == '__main__':
    # E6 (researcher2): K113(xyz) - Q - K113(pqr)
    Q = g([('a','b'),('b','c'),('c','a'),('x','b'),('x','c'),('y','a'),('y','c'),('z','a'),('z','b'),
           ('p','a'),('p','b'),('p','x'),('p','y'),('q','a'),('q','c'),('q','x'),('q','z'),
           ('r','b'),('r','c'),('r','y'),('r','z')])
    def K113(T, tag):
        h1, h2 = (tag, 1), (tag, 2)
        return g([(h1, h2)] + [(h, t) for h in (h1, h2) for t in T])
    E6 = {0: Q, 1: K113('xyz', 'h'), 2: K113('pqr', 'k')}
    run("E6 (뿌리 Q)", E6, [(0, 1), (0, 2)], root=0)
    run("E6 (뿌리 잎1)", E6, [(0, 1), (0, 2)], root=1, extra=False)
    # Q 의 4색 수준 허용 집합의 결합 구조: (T1 무지개?, T2 무지개?) 쌍
    U = ['p','q','r','x','y','z']
    pairs = set()
    for pi in partitions(U):
        if chi_pi(Q, pi) <= 4:
            rb = lambda T: len({i for t in T for i, B in enumerate(pi) if t in B}) == 3
            pairs.add((rb('xyz'), rb('pqr')))
    print("   Q 의 4색 허용 분할에서 (T1 무지개, T2 무지개) 쌍 =", sorted(pairs))
    # 정규화 절단 확인: cap = m+s-1 = 5
    print("   E6 절단 공식(cap=5) =", tree_formula(E6, [(0, 1), (0, 2)], cap=5))

    # E2 (researcher2, 정규화 없음): 중심 K_{2,n} + 쌍마다 삼각형 잎
    for n in (3, 4, 5):
        base = nx.complete_bipartite_graph(2, n); Sx = list(range(2, n + 2))
        pcs = {0: base}; Hd = []
        for t, (i, j) in enumerate(itertools.combinations(Sx, 2), start=1):
            pcs[t] = g([(i, j), (i, ('w', i, j)), (j, ('w', i, j))]); Hd.append((0, t))
        run(f"E2 n={n} (뿌리 중심)", pcs, Hd, extra=False)
        print(f"   E2 n={n} 절단 cap=m+s-1=4 공식 =", tree_formula(pcs, Hd, cap=4), "(정규화 없으면 절단 무효)")

    # O1 겹치는 접합: 중심 {u,v,w}, 변 vw; 잎1 = K4-uv (u=v 강제), 잎2 = K4-uw (u=w 강제)
    C = g([('v','w')], ['u'])
    L1 = g([('u','a1'),('u','b1'),('v','a1'),('v','b1'),('a1','b1')])
    L2 = g([('u','a2'),('u','b2'),('w','a2'),('w','b2'),('a2','b2')])
    run("O1 겹침 접합 {u,v},{u,w}", {0: C, 1: L1, 2: L2}, [(0, 1), (0, 2)])

    # 최소 예 K4-uv + K2 (정규화 없음, 한 접합)
    run("최소예 K4-uv + K2", {0: g([('u','a'),('u','b'),('v','a'),('v','b'),('a','b')]), 1: g([('u','v')])}, [(0, 1)])
