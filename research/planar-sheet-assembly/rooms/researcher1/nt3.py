"""N-T3 researcher1: 상대(researcher2) 턴 2 의 F1-F3, C1, C2, R2(U), W5/C5, K2 삼각형, 피터슨 재계산
+ 새 결정적 예: (i) 국소 이웃이 같은 접합쌍(띠), (ii) q=5 평면 2조각 세계의 비구별 쌍과 다조각 문맥에서의 구별.
researcher2 코드는 쓰지 않고 새로 짬."""
import itertools, networkx as nx

def chrom_ok(G, q, pre=None):
    """G 가 q-색칠 가능한가 (pre: 미리 정한 색 dict). 고리가 있으면 False."""
    if any(u == v for u, v in G.edges()):
        return False
    nodes = sorted(G.nodes(), key=lambda v: -G.degree(v))
    col = dict(pre or {})
    for u, v in G.edges():
        if u in col and v in col and col[u] == col[v]:
            return False
    rest = [v for v in nodes if v not in col]
    def bt(i):
        if i == len(rest):
            return True
        v = rest[i]
        used = {col[w] for w in G[v] if w in col}
        for c in range(q):
            if c not in used:
                col[v] = c
                if bt(i + 1):
                    return True
                del col[v]
        return False
    return bt(0)

def chi(G):
    if any(u == v for u, v in G.edges()):
        return float('inf')
    q = 0
    while not chrom_ok(G, q):
        q += 1
    return q

def partitions(xs):
    xs = list(xs)
    if not xs:
        yield []
        return
    a, rest = xs[0], xs[1:]
    for p in partitions(rest):
        yield [[a]] + p
        for i in range(len(p)):
            yield p[:i] + [[a] + p[i]] + p[i + 1:]

def canon(p):
    return tuple(sorted(tuple(sorted(map(str, b))) for b in p))

def profile(P, J, q):
    out = set()
    for p in partitions(J):
        if len(p) > q:
            continue
        pre = {}
        for i, b in enumerate(p):
            for x in b:
                pre[x] = i
        if chrom_ok(P, q, pre):
            out.add(canon(p))
    return out

def quotient(pieces, EJ):
    """pieces: list of (name, graph); 점 이름은 (name, v). EJ: 점쌍 목록. 고리 유지(MultiGraph->Graph with selfloops)."""
    U = nx.Graph()
    for nm, P in pieces:
        U.add_nodes_from((nm, v) for v in P.nodes())
    I = nx.Graph(); I.add_nodes_from(U.nodes()); I.add_edges_from(EJ)
    cls = {}
    for i, C in enumerate(nx.connected_components(I)):
        for x in C:
            cls[x] = i
    G = nx.Graph(); G.add_nodes_from(set(cls.values()))
    for nm, P in pieces:
        for u, v in P.edges():
            G.add_edge(cls[(nm, u)], cls[(nm, v)])
    return G, cls

def glue2(P, Jp, Q, Jq):
    """P 의 Jp[i] 와 Q 의 Jq[i] 를 식별."""
    return quotient([('P', P), ('Q', Q)], [(('P', a), ('Q', b)) for a, b in zip(Jp, Jq)])[0]

def pl(G):
    H = nx.Graph([(u, v) for u, v in G.edges() if u != v]); H.add_nodes_from(G.nodes())
    return nx.check_planarity(H)[0]

print("=== F1: C5 접기 ===")
C5 = nx.Graph([('x','a'),('a','y'),('y','b'),('b','c'),('c','x')])
W = nx.Graph(); W.add_node('w')
G, cls = quotient([('1', C5), ('2', W)], [(('1','x'),('2','w')), (('1','y'),('2','w'))])
print("G edges", G.number_of_nodes(), G.number_of_edges(), "chi", chi(G), "deg", sorted(d for _, d in G.degree()))
# 무(W) 정리 2 공식: f on class {x,y,w}; P1 profile 에서 x,y 같은 블록인 분할 필요
for q in range(1, 5):
    ok = any(len(b) == 2 and set(b) == {'x', 'y'} for p in profile(C5, ['x', 'y'], q) for b in p)
    print(" q", q, "formula ok", ok, "direct", chrom_ok(G, q))

print("=== F2: K2 접기 ===")
K2 = nx.Graph([('x','y')])
G, _ = quotient([('1', K2), ('2', W)], [(('1','x'),('2','w')), (('1','y'),('2','w'))])
print("loops", list(nx.selfloop_edges(G)), "chi", chi(G))

print("=== F3: K33 점 a1 을 s,t 로 쪼갠 조각 ===")
P = nx.Graph()
for a in ['a2', 'a3']:
    for b in ['b1', 'b2', 'b3']:
        P.add_edge(a, b)
P.add_edge('s', 'b1'); P.add_edge('t', 'b2'); P.add_edge('t', 'b3')
print("piece planar", pl(P))
G, _ = quotient([('1', P), ('2', W)], [(('1','s'),('2','w')), (('1','t'),('2','w'))])
print("G≅K33", nx.is_isomorphic(G, nx.complete_bipartite_graph(3, 3)), "planar", pl(G))
# (W) 형태로 바꾸면: 접힌 조각 P/(s~t) 자체가 K33 -> 평면 조각이 아님
print("folded piece itself planar", pl(nx.contracted_nodes(P, 's', 't', self_loops=False)))

K4uv = nx.complete_graph(['u','v','p','r']); K4uv.remove_edge('u','v')
print("=== C1 ===")
D = nx.Graph([('u','a'),('u','b'),('a','b'),('a','w'),('b','w'),('w','z')])
for J in [('u','z'), ('u','w')]:
    G = glue2(K4uv, ['u','v'], D, list(J))
    print(J, "Pi3", profile(D, list(J), 3), "chi", chi(G), "planar", pl(G), "deg", (D.degree(J[0]), D.degree(J[1])))

print("=== C2: 부채꼴 ===")
H = nx.Graph([(1,2),(1,3),(1,4),(1,0),(2,3),(3,4),(4,0),(0,5)])
for J in [(2,4), (0,2)]:
    G = glue2(K4uv, ['u','v'], H, list(J))
    cn = len(set(H[J[0]]) & set(H[J[1]]))
    nb = [sorted(H.degree(w) for w in H[x]) for x in J]
    print(J, "Pi3", profile(H, list(J), 3), "chi", chi(G), "planar", pl(G),
          "deg", (H.degree(J[0]), H.degree(J[1])), "dist", nx.shortest_path_length(H, *J),
          "common nbrs", cn, "nbr-degs", nb)

print("=== 새 예 S: 삼각형 띠 (v_i v_{i+1}, v_i v_{i+2}) ===")
n = 30
S = nx.Graph([(i, i+1) for i in range(n-1)] + [(i, i+2) for i in range(n-2)])
print("strip planar", pl(S), "chi", chi(S))
for J in [(12, 18), (12, 17)]:
    G = glue2(K4uv, ['u','v'], S, list(J))
    r = 4
    iso = nx.is_isomorphic(nx.ego_graph(S, J[0], r), nx.ego_graph(S, J[1], r))
    print(J, "Pi3", profile(S, list(J), 3), "chi(G)", chi(G), "planar G", pl(G),
          "deg", (S.degree(J[0]), S.degree(J[1])), "dist", nx.shortest_path_length(S, *J),
          "common", len(set(S[J[0]]) & set(S[J[1]])), "ball4 iso", iso)
# 두 쌍의 4-공 동형
b1 = [nx.ego_graph(S, x, 4) for x in (12, 18)]
b2 = [nx.ego_graph(S, x, 4) for x in (12, 17)]
print("ball(12)≅ball(17)≅ball(18):", nx.is_isomorphic(b1[0], b2[1]) and nx.is_isomorphic(b1[1], b2[1]))

print("=== R2: U (쌓은 삼각분할) ===")
U = nx.complete_graph(['a','b','c','d'])
U.add_edges_from([('e','a'),('e','b'),('e','d'),('f','a'),('f','b'),('f','e')])
print("U planar", pl(U), "edges", U.number_of_edges(), "maximal planar(3n-6)", U.number_of_edges() == 3*6-6)
print("Pi4 {d,f}", profile(U, ['d','f'], 4), "Pi4 {c,f}", profile(U, ['c','f'], 4), "Pi4 {d,f,c}", profile(U, ['d','f','c'], 4))
G = glue2(U, ['c','f'], U, ['d','f'])
print("U(c,f)+U(d,f): chi", chi(G), "chi(U)", chi(U))

print("=== W5 / C5 / 오각별 ===")
rim = list(range(5))
C5r = nx.cycle_graph(5); W5 = C5r.copy(); W5.add_edges_from(('h', i) for i in rim)
star = nx.Graph([(i, (i+2) % 5) for i in rim])
print("chi W5∪star", chi(glue2(W5, rim, star, rim)), "chi C5∪star", chi(glue2(C5r, rim, star, rim)), "star planar", pl(star))

print("=== K2 세 조각 삼각형 ===")
pcs = [(str(i), nx.Graph([('s','t')])) for i in range(3)]
EJ = [(('0','t'),('1','s')), (('1','t'),('2','s')), (('2','t'),('0','s'))]
G, _ = quotient(pcs, EJ)
Gam = nx.Graph(); Gam.add_edges_from(EJ); [Gam.add_edge((nm,'s'),(nm,'t')) for nm,_ in pcs]
print("Gamma≅C6", nx.is_isomorphic(Gam, nx.cycle_graph(6)), "G≅K3", nx.is_isomorphic(G, nx.complete_graph(3)))

print("=== 피터슨 = K2 조각 15 개 ===")
Pe = nx.petersen_graph()
pcs = [(f"e{i}", nx.Graph([(u, v)])) for i, (u, v) in enumerate(Pe.edges())]
EJ = []
for v in Pe.nodes():
    occ = [(nm, v) for nm, Pk in pcs if v in Pk]
    EJ += [(occ[0], o) for o in occ[1:]]
G, _ = quotient(pcs, EJ)
print("G≅Petersen", nx.is_isomorphic(G, Pe), "chi", chi(G))

print("=== 새 예 Z: q=5, 평면 2조각 세계에서 프로필 차이가 안 보임 ===")
# P' : 같은 면 위의 비인접 두 점 x,y 를 가진 평면 그래프, P = P'+xy (평면)
Pp = nx.Graph([('x','m'),('m','y'),('y','n'),('n','x'),('x','k'),('k','m'),('k','y')])  # x,y 가 면 x-n-y-m? 공면
P = Pp.copy(); P.add_edge('x','y')
print("P' planar", pl(Pp), "P planar", pl(P))
for q in (4, 5):
    print(" q", q, "Pi(P')", profile(Pp, ['x','y'], q), "Pi(P)", profile(P, ['x','y'], q))
# 다조각 문맥: T1 의 Q_{xy} (q=5) 를 K2 조각들로 분해 -> 평면 조각만으로 된 문맥이 P, P' 를 q=5 에서 구별
q = 5
Q = nx.complete_graph([f"z{j}" for j in range(q)])
for j in range(1, q):
    Q.add_edge('x', f"z{j}"); Q.add_edge('y', f"z{j}")  # x,y 를 블록 B_0 에 둠
print("Q_xy planar", pl(Q), "Pi5(Q)", profile(Q, ['x','y'], 5))
for name, PP in [("P'", Pp), ("P", P)]:
    pcs = [('P', PP)] + [(f"q{i}", nx.Graph([(u, v)])) for i, (u, v) in enumerate(Q.edges())]
    EJ = []
    for v in Q.nodes():
        occ = [(nm, v) for nm, Pk in pcs[1:] if v in Pk]
        if v in ('x', 'y'):
            occ = [('P', v)] + occ
        EJ += [(occ[0], o) for o in occ[1:]]
    G, cls = quotient(pcs, EJ)
    # (W) 확인: 각 식별류가 각 조각과 많아야 한 번
    Wok = all(len([x for x in cls if cls[x] == c and x[0] == nm]) <= 1 for c in set(cls.values()) for nm, _ in pcs)
    print(f" {name} ∪ (K2 조각 {len(pcs)-1}개): (W) {Wok}, all pieces planar True, 5-colorable {chrom_ok(G, 5)}, chi {chi(G)}")
