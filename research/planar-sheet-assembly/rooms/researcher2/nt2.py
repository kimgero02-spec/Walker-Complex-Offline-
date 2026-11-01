# N-T2 (researcher2): 독립 재계산 + 반례. researcher1 코드를 쓰지 않고 새로 짠다.
import itertools, networkx as nx

def colorable(G, q, pre=None):
    """q-색칠 존재 여부 (백트래킹). pre: 미리 정한 색 dict."""
    nodes = sorted(G.nodes(), key=lambda v: -G.degree(v))
    col = dict(pre or {})
    for v in col:
        if any(col.get(w) == col[v] for w in G[v]): return False
    rest = [v for v in nodes if v not in col]
    def bt(i):
        if i == len(rest): return True
        v = rest[i]
        used = {col[w] for w in G[v] if w in col}
        for c in range(q):
            if c not in used:
                col[v] = c
                if bt(i+1): return True
                del col[v]
        return False
    if any(u == v for u, v in G.edges()): return False
    return bt(0)

def chi(G):
    if any(u == v for u, v in G.edges()): return None
    q = 1 if G.number_of_nodes() else 0
    while not colorable(G, q): q += 1
    return q

def quotient(V, EP, EJ):
    """Gamma=(V, EP u EJ) -> G=Gamma/EJ (멀티간선은 합침, 고리는 남김)."""
    J = nx.Graph(); J.add_nodes_from(V); J.add_edges_from(EJ)
    cls = {}
    for i, C in enumerate(nx.connected_components(J)):
        for v in C: cls[v] = i
    G = nx.Graph(); G.add_nodes_from(set(cls.values()))
    for a, b in EP: G.add_edge(cls[a], cls[b])
    return G, cls

def partitions(xs):
    xs = list(xs)
    if not xs: yield []; return
    first, rest = xs[0], xs[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i+1:]
        yield [[first]] + p

def derived(P, blocks):
    """P_pi: 블록마다 한 점으로 합치고 서로 다른 블록 사이를 모두 잇는다."""
    H = P.copy(); reps = []
    for B in blocks:
        r = B[0]
        for x in B[1:]:
            H = nx.contracted_nodes(H, r, x, self_loops=True)
        reps.append(r)
    H = nx.Graph(H)
    for a, b in itertools.combinations(reps, 2): H.add_edge(a, b)
    return H

def profile(P, J, q):
    out = set()
    for p in partitions(J):
        if len(p) <= q and colorable(derived(P, p), q):
            out.add(frozenset(frozenset(b) for b in p))
    return out

def show(pr):
    return sorted("|".join("".join(sorted(str(x[-1]) for x in b)) for b in sorted(p, key=lambda b: sorted(map(str,b)))) for p in pr)

def chi_formula(pieces, EJ):
    """chi(G) = min_Pi max(|Pi|, max_k chi((P_k)_{Pi|J_k}))  -- G 를 만들지 않음."""
    V = [v for P in pieces for v in P.nodes()]
    J = nx.Graph(); J.add_nodes_from(V); J.add_edges_from(EJ)
    cls = {}
    for i, C in enumerate(nx.connected_components(J)):
        for v in C: cls[v] = i
    Jv = {v for e in EJ for v in e}
    classes = sorted({cls[v] for v in Jv})
    best = None
    for Pi in partitions(classes):
        lab = {c: i for i, B in enumerate(Pi) for c in B}
        m = len(Pi); bad = False
        for P in pieces:
            Jk = [x for x in P.nodes() if x in Jv]
            blocks = {}
            for x in Jk: blocks.setdefault(lab[cls[x]], []).append(x)
            c = chi(derived(P, list(blocks.values())))
            if c is None: bad = True; break
            m = max(m, c)
        if not bad and (best is None or m < best): best = m
    return best

def piece(k, edges, nodes=()):
    P = nx.Graph(); P.add_nodes_from((k, a) for a in nodes)
    P.add_edges_from(((k, a), (k, b)) for a, b in edges); return P

def glue(pieces, EJ):
    V = [v for P in pieces for v in P.nodes()]
    EP = [e for P in pieces for e in P.edges()]
    G, cls = quotient(V, EP, EJ)
    Gam = nx.Graph(); Gam.add_nodes_from(V); Gam.add_edges_from(EP); Gam.add_edges_from(EJ)
    return Gam, G

pl = lambda H: nx.check_planarity(H)[0]
degs = lambda H: sorted(d for _, d in H.degree())
D = lambda u,a,b,v: [(u,a),(u,b),(a,b),(a,v),(b,v)]   # diamond, 끝점 u,v (uv 비간선)

print("== 재계산 예1: K4 = (K4-uv) u K2 ==")
P1 = piece(1, D('u','p','r','v')); P2 = piece(2, [('u','v')])
EJ = [((1,'u'),(2,'u')), ((1,'v'),(2,'v'))]
Gam, G = glue([P1, P2], EJ)
print(" G~K4", nx.is_isomorphic(G, nx.complete_graph(4)), "chi P1,P2,G", chi(P1), chi(P2), chi(G),
      "chi(Gamma)", chi(Gam), "formula", chi_formula([P1,P2],EJ), "Gamma planar", pl(Gam))
for q in (3,4):
    print("  Pi_%d(P1)=" % q, show(profile(P1, [(1,'u'),(1,'v')], q)), " Pi_%d(P2)=" % q, show(profile(P2, [(2,'u'),(2,'v')], q)))

print("== 재계산 예2 (T1 의 A,B) ==")
A2 = piece(2, D('u','a','b','w') + [('w','v')])
B2 = piece(2, D('u','a','b','v') + [('a','z')])
for nm, Q in (("A", A2), ("B", B2)):
    Gam, G = glue([P1, Q], EJ)
    print(" ", nm, "n,m", Q.number_of_nodes(), Q.number_of_edges(), "planar", pl(Q), "chi(P2)", chi(Q),
          "deg", degs(Q), "Pi3", show(profile(Q, [(2,'u'),(2,'v')], 3)), "chi(G)", chi(G), "G planar", pl(G),
          "chi(Gamma)", chi(Gam), "formula", chi_formula([P1,Q],EJ))

print("== 반례 C1: 같은 (비표지) 조각, 접합점만 다르게 -> chi 가 갈림 ==")
# P2 = diamond(u,a,b,w) + 매달린 점 z (w 에). 비표지 그래프로 하나.
base = D('u','a','b','w') + [('w','z')]
# C1a: 접합점 (u, z) ; C1b: 접합점 (u, w)
for nm, (s, t) in (("C1a", ('u','z')), ("C1b", ('u','w'))):
    Q = piece(2, base)
    EJx = [((1,'u'),(2,s)), ((1,'v'),(2,t))]
    Gam, G = glue([P1, Q], EJx)
    print(" ", nm, "P2 deg", degs(Q), "J-pair deg", (Q.degree((2,s)), Q.degree((2,t))), "Pi3",
          show(profile(Q, [(2,s),(2,t)], 3)), "chi(G)", chi(G), "G planar", pl(G), "chi(Gamma)", chi(Gam))

print("== 반례 C2: 차수열 + 접합점 차수까지 같고 chi 가 갈리는 쌍 (구성) ==")
# 결정적 탐색: 7점 이하 연결 평면 그래프에서, 비인접 쌍 (x,y),(x',y') 가 deg 쌍이 같고
# 하나는 3색에서 '같음 강제', 다른 하나는 '다름 강제'.
from networkx.generators.atlas import graph_atlas_g
found = None
for H in graph_atlas_g():
    if H.number_of_nodes() < 5 or not nx.is_connected(H) or not pl(H) or chi(H) != 3: continue
    same, diff = {}, {}
    for x, y in itertools.combinations(H.nodes(), 2):
        if H.has_edge(x, y): continue
        pr = profile(H, [x, y], 3)
        key = tuple(sorted((H.degree(x), H.degree(y))))
        if len(pr) == 1:
            (p,) = pr
            (same if len(p) == 1 else diff).setdefault(key, (x, y))
    common = set(same) & set(diff)
    if common:
        k = sorted(common)[0]; found = (H, same[k], diff[k]); break
H, (x, y), (x2, y2) = found
print("  H edges", sorted(H.edges()), "deg", degs(H), "same-forced", (x, y), "diff-forced", (x2, y2))
for nm, (s, t) in (("C2a(same)", (x, y)), ("C2b(diff)", (x2, y2))):
    Q = piece(2, list(H.edges()))
    EJx = [((1,'u'),(2,s)), ((1,'v'),(2,t))]
    Gam, G = glue([P1, Q], EJx)
    print("  ", nm, "J deg", (H.degree(s), H.degree(t)), "dist", nx.shortest_path_length(H, s, t),
          "chi(G)", chi(G), "formula", chi_formula([P1, Q], EJx), "G planar", pl(G))

print("== (a) 조건 (W) 없이: 접힘 ==")
# F1: P1 = C5 (x a y b c), P2 = 한 점 w, EJ = {xw, yw}: 식별류 {x,y,w} 가 P1 을 두 번 만남
P = piece(1, [('x','a'),('a','y'),('y','b'),('b','c'),('c','x')]); W = piece(2, [], nodes=['w'])
EJf = [((1,'x'),(2,'w')), ((1,'y'),(2,'w'))]
Gam, G = glue([P, W], EJf)
print("  F1 G edges", sorted(G.edges()), "chi(G)", chi(G), "formula(W 없이)", chi_formula([P, W], EJf))
# F2: P1 = 오각형 + 대각 접힘으로 고리: P1 = 경로 x-y (간선), w 로 둘 다 식별 -> 고리
P = piece(1, [('x','y')]); Gam, G = glue([P, W], EJf)
print("  F2 loop?", any(a == b for a, b in G.edges()), "chi(G)", chi(G), "formula", chi_formula([P, W], EJf))
# F3: 접힘이 평면 조각들에서 비평면 G 를 만든다: K_{3,3} 를 두 조각과 접힘으로
# P1 = K_{3,3} 에서 a1 을 a1', a1'' 두 점으로 쪼갠 평면 그래프 (a1'-b1,b2 ; a1''-b3)
E33 = [('a2','b1'),('a2','b2'),('a2','b3'),('a3','b1'),('a3','b2'),('a3','b3'),
       ('s','b1'),('s','b2'),('t','b3')]
P = piece(1, E33); W = piece(2, [], nodes=['w'])
EJs = [((1,'s'),(2,'w')), ((1,'t'),(2,'w'))]
Gam, G = glue([P, W], EJs)
print("  F3 P1 planar", pl(P), "G~K33", nx.is_isomorphic(G, nx.complete_bipartite_graph(3,3)), "Gamma planar", pl(Gam))

print("== (b) 평면 가제트 q=4: 쌓은 삼각분할 (유일 4-색칠) ==")
# U: K4{a,b,c,d}, e in abd (색 c), f in abe (색 d)  -> d,f 같은 색 강제, 비인접
U = [('a','b'),('a','c'),('a','d'),('b','c'),('b','d'),('c','d'),
     ('e','a'),('e','b'),('e','d'),('f','a'),('f','b'),('f','e')]
Ug = nx.Graph(U)
print("  U planar", pl(Ug), "df edge", Ug.has_edge('d','f'), "cf edge", Ug.has_edge('c','f'),
      "Pi4(U,{d,f})", show(profile(Ug, ['d','f'], 4)), "Pi4(U,{c,f})", show(profile(Ug, ['c','f'], 4)))
# P = U 를 (c,f) 로 접합 (다름 강제), Q = U 를 (d,f) 로 접합 (같음 강제). 둘 다 평면, uv 비간선.
Pp = piece(1, U); Qp = piece(2, U)
EJq = [((1,'c'),(2,'d')), ((1,'f'),(2,'f'))]
Gam, G = glue([Pp, Qp], EJq)
print("  P(c,f) u Q(d,f): chi pieces", chi(Pp), chi(Qp), "chi(G)", chi(G), "formula", chi_formula([Pp,Qp],EJq), "G planar", pl(G))
# 대조: P' = 두 점 고립 (평면, Pi4 = 둘 다) 와 같은 Q
Pq = piece(1, [], nodes=['c','f'])
Gam, G = glue([Pq, Qp], EJq); print("  P'(2 고립점) u Q: chi(G)", chi(G))
# T1 의 q=4 가제트 (K4 z1..z4, u,v -> z2,z3,z4) 는 비평면
Z = nx.complete_graph(['z1','z2','z3','z4']); Z.add_edges_from((x, z) for x in 'uv' for z in ['z2','z3','z4'])
print("  T1 gadget Q_{uv}, q=4 planar?", pl(Z), " Pi4", show(profile(Z, ['u','v'], 4)))
# |J|=3 블록 {uv|w}: 유일 4-색칠 평면 그래프에서 같은 색 두 점 + 다른 색 한 점
print("  Pi4(U,{d,f,c})", show(profile(Ug, ['d','f','c'], 4)))

print("== (b') q=5 에서 평면 조각의 프로필: 비인접 쌍은 항상 {같음, 다름} ==")
print("  Pi5(U,{d,f})", show(profile(Ug, ['d','f'], 5)), " Pi5(U,{c,f})", show(profile(Ug, ['c','f'], 5)))

print("== (c) 프로필 = 파생 그래프들의 색칠수 벡터 ==")
for nm, Q, Jq in (("A2", A2, [(2,'u'),(2,'v')]), ("B2", B2, [(2,'u'),(2,'v')])):
    vec = {"|".join("".join(str(x[1]) for x in b) for b in p): chi(derived(Q, p)) for p in partitions(Jq)}
    print("  ", nm, "chi(P_pi):", vec)

print("== (c') 퇴화: 조각이 모두 K2 이면 공식 = 정의 ==")
Pet = nx.petersen_graph()
pieces = [piece(i, [('x','y')]) for i in range(15)]
ends = {}
for i, (a, b) in enumerate(Pet.edges()):
    ends.setdefault(a, []).append((i,'x')); ends.setdefault(b, []).append((i,'y'))
EJp = [(L[j], L[j+1]) for L in ends.values() for j in range(len(L)-1)]
Gam, G = glue(pieces, EJp)
print("  Petersen from 15 K2: G~Petersen", nx.is_isomorphic(G, Pet), "chi(G)", chi(G), "|classes|", 10,
      "Bell(10)=115975 개의 Pi 를 훑어야 함 (공식은 G 의 색칠 탐색과 같음)")
