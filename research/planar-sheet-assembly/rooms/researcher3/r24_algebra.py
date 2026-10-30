# R24 researcher3: 검산용 (근거 아님). 보고서 R24-researcher3.md 의 구성들이 문자 그대로 작동하는지 본다.
# 1) q=2 Bayer-Lovasz 증명서의 조각 분할 (C5 = 경로 + 경로)
# 2) 토릭 들어올림 (정리 3.1 의 구성) 이 ker psi_{M°} 에 들어가는지
# 3) 연결 분할 격자 = 조각 연결 분할들의 join 닫힘 (정리 4.2)
# 4) 같은 "공유 자료" (7점, 해밀턴 7-사이클 둘, 공유 변 0) 에서 chi 가 다름
# 5) chi(M°) <= 5
import itertools
from fractions import Fraction
import networkx as nx

# ---------- 1. polynomial arithmetic (dict: exponent tuple -> Fraction)
def padd(a, b, s=1):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, 0) + s * v
        if r[k] == 0:
            del r[k]
    return r

def pmul(a, b):
    r = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            k = tuple(x + y for x, y in zip(k1, k2))
            r[k] = r.get(k, 0) + v1 * v2
            if r[k] == 0:
                del r[k]
    return r

N = 5
def var(i, c=1):
    e = [0] * N; e[i] = 1
    return {tuple(e): Fraction(c)}
one = {tuple([0] * N): Fraction(1)}

def h2(u, v):  # q=2: h_uv = x_u + x_v
    return padd(var(u), var(v))

cyc = [0, 1, 2, 3, 4]
piece = {(0, 1): 1, (1, 2): 1, (2, 3): 1, (3, 4): 2, (4, 0): 2}  # 간선 비트
f = {1: {}, 2: {}}
half_x0 = var(0, Fraction(1, 2))
for i in range(5):
    u, v = cyc[i], cyc[(i + 1) % 5]
    term = pmul(half_x0, h2(u, v))
    f[piece[(u, v)]] = padd(f[piece[(u, v)]], term, (-1) ** i)
x0sq_minus1 = padd(pmul(var(0), var(0)), one, -1)
f[2] = padd(f[2], x0sq_minus1, -1)
total = padd(f[1], f[2])
print("1) certificate f1+f2 == 1 :", total == one)

# ---------- 2. toric lift
def manual_compressed(V, pieces):
    V0 = [(v, k) for k, (PV, PE) in enumerate(pieces) for v in PV]
    F = {v: [(v, k) for k, (PV, PE) in enumerate(pieces) if v in PV] for v in V}
    E00 = [frozenset({(u, k), (v, k)}) for k, (PV, PE) in enumerate(pieces) for (u, v) in PE]
    E01 = [frozenset({x, ('w', v)}) for v in V if len(F[v]) >= 2 for x in F[v]]
    return V0, F, E00, E01

def psi(monomial):  # monomial: dict edge->exp ; edge = frozenset of 2 vertices -> vertex exponent dict
    r = {}
    for e, a in monomial.items():
        for x in e:
            r[x] = r.get(x, 0) + a
    return r

def lift(u_mon, v_mon, owner, F):
    # u_mon, v_mon: dict G-edge(frozenset) -> exp with psi_G equal
    def to_M(m):
        r = {}
        for e, a in m.items():
            k = owner[e]
            ee = frozenset({(x, k) for x in e})
            r[ee] = r.get(ee, 0) + a
        return r
    U, W = to_M(u_mon), to_M(v_mon)
    pu, pw = psi(U), psi(W)
    for v, cop in F.items():
        if len(cop) < 2:
            continue
        for x in cop:
            port = frozenset({x, ('w', v)})
            a, b = pu.get(x, 0), pw.get(x, 0)
            if b:
                U[port] = U.get(port, 0) + b
            if a:
                W[port] = W.get(port, 0) + a
    return U, W

def check_toric(V, pieces, name):
    V0, F, E00, E01 = manual_compressed(V, pieces)
    owner = {}
    for k, (PV, PE) in enumerate(pieces):
        for (a, b) in PE:
            owner.setdefault(frozenset({a, b}), k)
    E = list(owner)
    ok = cnt = 0
    for a, b, c, d in itertools.permutations(V, 4):
        e1, e2, e3, e4 = frozenset({a, b}), frozenset({c, d}), frozenset({a, c}), frozenset({b, d})
        if all(e in owner for e in (e1, e2, e3, e4)):
            um = {e1: 1, e2: 1}; vm = {e3: 1, e4: 1}
            if len(set([e1, e2])) < 2 or len(set([e3, e4])) < 2:
                continue
            U, W = lift(um, vm, owner, F)
            cnt += 1
            # psi_{M°} equal ?  and image under phi (ports->1, copies->G edges) is u-v ?
            same = psi(U) == psi(W)
            back = lambda m: {frozenset({x[0] for x in e}): a for e, a in m.items() if all(isinstance(x, tuple) and x[0] != 'w' for x in e)}
            ok += same and back(U) == um and back(W) == vm
    print(f"2) toric lift {name}: {ok}/{cnt} quadratic binomials lift into ker psi_M° and map back")

V5 = list(range(5))
P1 = (V5, [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)])
P2 = (V5, [(0, 2), (2, 4), (4, 1), (1, 3), (0, 3)])
check_toric(V5, [P1, P2], "K5=C5+C5'")
V4 = list(range(4))
Q1 = (V4, [(0, 1), (1, 3), (3, 2), (2, 0)])
Q2 = (V4, [(0, 3), (3, 1), (1, 2), (2, 0)])
check_toric(V4, [Q1, Q2], "K4=C4+C4")

# ---------- 3. connected partitions = join closure of piece connected partitions
def set_partitions(s):
    s = list(s)
    if not s:
        yield []
        return
    first, rest = s[0], s[1:]
    for p in set_partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [p[i] | {first}] + p[i + 1:]
        yield p + [{first}]

def canon(p):
    return frozenset(frozenset(b) for b in p)

def connected_parts(V, E):
    g = nx.Graph(); g.add_nodes_from(V); g.add_edges_from(E)
    out = set()
    for p in set_partitions(V):
        if all(nx.is_connected(g.subgraph(b)) for b in p):
            out.add(canon(p))
    return out

def join(p, q):
    # finest common coarsening
    g = nx.Graph()
    for b in list(p) + list(q):
        b = list(b); g.add_nodes_from(b)
        g.add_edges_from(zip(b, b[1:]))
    return canon([set(c) for c in nx.connected_components(g)])

def check_join(V, pieces, name):
    E = [e for _, PE in pieces for e in PE]
    LG = connected_parts(V, E)
    Ls = [connected_parts(V, PE) for _, PE in pieces]
    J = set(Ls[0])
    for L in Ls[1:]:
        J = {join(a, b) for a in J for b in L}
    print(f"3) {name}: |L(G)|={len(LG)}, |join closure|={len(J)}, equal={J == LG}, |L(P_k)|={[len(L) for L in Ls]}")

check_join(V5, [P1, P2], "K5")
check_join(V4, [Q1, Q2], "K4")

# ---------- 4. two edge-disjoint Hamiltonian 7-cycles, different chi
def chi(g):
    nodes = list(g.nodes())
    for q in range(1, len(nodes) + 1):
        col = {}
        def bt(i):
            if i == len(nodes):
                return True
            v = nodes[i]
            for c in range(q):
                if all(col.get(u) != c for u in g[v]):
                    col[v] = c
                    if bt(i + 1):
                        return True
                    del col[v]
            return False
        if bt(0):
            return q
def ham_cycles(g):
    nodes = sorted(g.nodes()); s = nodes[0]; out = set()
    def dfs(path):
        if len(path) == len(nodes):
            if s in g[path[-1]]:
                cyc = frozenset(frozenset(e) for e in zip(path, path[1:] + [s]))
                out.add(cyc)
            return
        for u in g[path[-1]]:
            if u not in path:
                dfs(path + [u])
    dfs([s]); return out

def two_ham_decomp(g):
    E = frozenset(frozenset(e) for e in g.edges())
    for c in ham_cycles(g):
        rest = E - c
        h = nx.Graph(); h.add_nodes_from(g.nodes()); h.add_edges_from(tuple(e) for e in rest)
        if all(d == 2 for _, d in h.degree()) and nx.is_connected(h):
            return c, rest
    return None

A = nx.complement(nx.cycle_graph(7))
B = nx.complement(nx.disjoint_union(nx.cycle_graph(3), nx.cycle_graph(4)))
for name, g in (("co-C7", A), ("co-(C3+C4)", B)):
    d = two_ham_decomp(g)
    print(f"4) {name}: 4-regular={all(x==4 for _,x in g.degree())}, two Ham-cycle decomposition={d is not None}, chi={chi(g)}, planar={nx.check_planarity(g)[0]}")

# ---------- 5. chi(M°)
def Mcirc(V, pieces):
    V0, F, E00, E01 = manual_compressed(V, pieces)
    g = nx.Graph(); g.add_nodes_from(V0)
    g.add_edges_from(tuple(e) for e in E00 + E01)
    return g
for name, (V, ps) in (("K5", (V5, [P1, P2])), ("K4", (V4, [Q1, Q2]))):
    print(f"5) chi(M° of {name} decomposition) = {chi(Mcirc(V, ps))}")

# ---------- 6. Hadwiger number (brute force over connected partitions of a subset) for the two 7-vertex graphs
def hadwiger(g):
    best = 1
    V = list(g.nodes())
    for p in set_partitions(V):  # g connected: may absorb leftovers, so partitions of all V suffice
        if all(nx.is_connected(g.subgraph(b)) for b in p):
            t = len(p)
            if t > best and all(any(g.has_edge(a, b) for a in p[i] for b in p[j]) for i in range(t) for j in range(i + 1, t)):
                best = t
    return best
for name, g in (("co-C7", A), ("co-(C3+C4)", B)):
    print(f"6) {name}: connected={nx.is_connected(g)}, Hadwiger number={hadwiger(g)}, chi={chi(g)}")
