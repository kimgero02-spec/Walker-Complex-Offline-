"""R04 (researcher3): colour-holonomy sign conjecture.
Closed chains of K_c (circular-arc model): vertex j arrives at step j (mod m), lives ell[j] steps.
Pieces T_i = vertices alive at step i (must have size c); seams T_i & T_{i+1} ((c-1)-cliques).
G = union of the cliques T_i.  Holonomy g in S_c by colour propagation; sign = sgn(g).
Computes chi, L_h = h(B(G))+2, and a *vector certificate* for ind B(G) <= D-1 (odd map to S^{D-1}):
w: V -> R^D with 0 notin conv(w(A) u -w(B)) for every maximal simplex A|B of B(G)."""
import itertools, sys
import numpy as np, networkx as nx
from topo import h_index, simplices_B, chi

def chain(m, ell):
    ell = list(ell); assert len(ell) == m
    dep = [(j + ell[j]) % m for j in range(m)]
    assert sorted(dep) == list(range(m)), "departures not a permutation"
    assert all(1 <= l < m for l in ell)
    alive = lambda j, i: (i - j) % m < ell[j]
    T = [frozenset(j for j in range(m) if alive(j, i)) for i in range(m)]
    c = len(T[0]); assert all(len(t) == c for t in T)
    G = nx.Graph(); G.add_nodes_from(range(m))
    for t in T:
        G.add_edges_from(itertools.combinations(sorted(t), 2))
    return G, T, c

def holonomy(m, ell, T, c):
    """unrolled colour propagation from T_0; returns g (tuple) with g[init colour]=new colour,
    and psi[(v, lap)] colours on the universal cover for lap in {-1,0,1}"""
    col = {v: i for i, v in enumerate(sorted(T[0]))}
    init = dict(col)
    dep = {(j + ell[j]) % m: j for j in range(m)}       # step -> departing vertex
    cur = dict(col)                                   # current colour of alive vertices
    unrolled = {}                                     # vertex -> colour at its first arrival in (0,m]
    for i in range(1, m + 1):
        s = i % m
        d = dep[s]; a = s                             # vertex a arrives at step s
        cur[a] = cur.pop(d) if d != a else cur[d]
        unrolled[a] = cur[a]
    g = [None] * c
    for v, i0 in init.items(): g[i0] = unrolled[v]
    return tuple(g)

def sign(p):
    p = list(p); s = 1; seen = [False] * len(p)
    for i in range(len(p)):
        if not seen[i]:
            j = i; L = 0
            while not seen[j]: seen[j] = True; j = p[j]; L += 1
            s *= (-1) ** (L - 1)
    return s

def L_h(G, dmax):
    G = nx.convert_node_labels_to_integers(G)
    return h_index(simplices_B(G, dmax), dmax) + 2

# ---------- vector certificate ----------
def maximal_simplices_B(G):
    V = list(G.nodes()); adj = {v: set(G[v]) for v in V}
    def CN(S): return set(V) if not S else set.intersection(*[adj[a] for a in S])
    out = set()
    for x in V:
        nb = sorted(adj[x])
        for k in range(1, len(nb) + 1):
            for A in itertools.combinations(nb, k):
                B = frozenset(CN(A)); A2 = frozenset(CN(B))
                if B and A2 and not (A2 & B):
                    out.add((A2, B)); out.add((B, A2))
    return out

def rot_plane(D, u, v, theta):
    """rotation by theta in plane span(u,v) (u,v orthonormal) in R^D"""
    I = np.eye(D); U = np.outer(u, u) + np.outer(v, v); W = np.outer(v, u) - np.outer(u, v)
    return I + (np.cos(theta) - 1) * U + np.sin(theta) * W

def path_to(perm_inv_matrix_target, steps_list):
    pass

def three_cycles(p):
    """write even permutation p (list) as product of 3-cycles (a b c) meaning a->b->c->a, applied right-to-left"""
    p = list(p); n = len(p); out = []
    # reduce p to identity by left-multiplying with 3-cycles / transposition pairs
    trans = []
    q = p[:]
    for i in range(n):
        while q[i] != i:
            j = q[i]
            trans.append((i, j)); q[i], q[j] = q[j], q[i]
    return trans  # list of transpositions whose product gives p (up to order); even length iff sign +

def basis_vectors(c, extra):
    D = c + (1 if extra else 0)
    E = np.zeros((c, D))
    for i in range(c):
        E[i, i] = 1.0
    E[:, :c] -= 1.0 / c
    return E, D

def transposition_path(c, D, a, b, use_extra):
    """path s in [0,1] -> rotation taking (e_a - e_b) to -(e_a - e_b); if use_extra rotate through extra axis
    (gives transposition (+) (-1) on extra), else returns None"""
    u = np.zeros(D); u[a] = 1 / np.sqrt(2); u[b] = -1 / np.sqrt(2)
    v = np.zeros(D); v[D - 1] = 1.0
    return lambda s: rot_plane(D, u, v, np.pi * s)

def pair_path(c, D, t1, t2):
    """two transpositions (a b)(c d) or (a b)(b c): rotate through each other's plane inside sum-zero space"""
    (a, b), (x, y) = t1, t2
    u = np.zeros(D); u[a] += 1; u[b] -= 1; u /= np.linalg.norm(u)
    w = np.zeros(D); w[x] += 1; w[y] -= 1
    w = w - (w @ u) * u
    if np.linalg.norm(w) < 1e-9:
        return lambda s: np.eye(D)   # same transposition twice = identity
    w /= np.linalg.norm(w)
    # reflection_u * reflection_w' ; product of reflections in u and in w2 = rotation; we build
    # the exact target matrix and a geodesic-free path: rotate in plane(u, w) by 2*angle
    return None

def perm_matrix(p, D):
    M = np.eye(D)
    P = np.zeros((D, D)); P[len(p):, len(p):] = np.eye(D - len(p))
    for i, j in enumerate(p): P[j, i] = 1.0   # e_i -> e_{p(i)}
    return P

def refl(u):
    u = u / np.linalg.norm(u); return np.eye(len(u)) - 2 * np.outer(u, u)

def so_path(M, c, wind=None):
    """geodesic-type path I -> M for M = permutation matrix on first c coords (+ -1 on extra coords), det +1.
    Fourier planes of each cycle rotate by their principal angle; all -1 eigenvectors are paired and rotated by pi."""
    D = M.shape[0]
    p = [int(np.argmax(M[:, i])) for i in range(c)]   # M e_i = e_{p(i)}
    planes = []; neg = []
    seen = [False] * c
    for i in range(c):
        if seen[i]: continue
        cyc = []; j = i
        while not seen[j]: seen[j] = True; cyc.append(j); j = p[j]
        L = len(cyc)
        for k in range(1, (L + 1) // 2):
            if 2 * k == L: continue
            u = np.zeros(D); v = np.zeros(D)
            for t, a in enumerate(cyc):
                u[a] = np.cos(2 * np.pi * k * t / L); v[a] = np.sin(2 * np.pi * k * t / L)
            u /= np.linalg.norm(u); v /= np.linalg.norm(v)
            planes.append([u, v, 2 * np.pi * k / L])
        if L % 2 == 0:
            u = np.zeros(D)
            for t, a in enumerate(cyc): u[a] = (-1) ** t
            neg.append(u / np.linalg.norm(u))
    for k in range(c, D):
        if M[k, k] < 0:
            u = np.zeros(D); u[k] = 1; neg.append(u)
    assert len(neg) % 2 == 0
    for t in range(0, len(neg), 2): planes.append([neg[t], neg[t + 1], np.pi])
    def Rot(s, pl):
        out = np.eye(D)
        for u, v, th in pl:
            out = out + (np.cos(s * th) - 1) * (np.outer(u, u) + np.outer(v, v)) + np.sin(s * th) * (np.outer(v, u) - np.outer(u, v))
        return out
    # fix orientation of each plane so that Rot(1) = M
    for idx in range(len(planes)):
        u, v, th = planes[idx]
        test = Rot(1, [planes[idx]])
        # compare action on u
        if not np.allclose(test @ u, M @ u):
            planes[idx][2] = -th
    assert np.allclose(Rot(1, planes), M), "path end"
    if wind == "count": return len(planes)
    if wind is not None:
        for idx, k in enumerate(wind): planes[idx][2] += 2 * np.pi * k
        assert np.allclose(Rot(1, planes), M), "path end 2"
    return lambda s: Rot(s, planes)

def certificate1(m, ell, T, c, g, extra=None, verbose=False, wind=None):
    """build w_v = R(t_v) E[psi(v)] and check 0 notin conv(w_A u -w_B) for all maximal simplices.
    sign + : D = c-1 (sum-zero space inside R^c), M = P_g^{-1};  sign - : extra axis, M = P_g^{-1} (+) (-1)."""
    sg = sign(g)
    if extra is None: extra = (sg < 0)
    D = c + (1 if extra else 0)
    E = np.zeros((c, D)); E[:, :c] = np.eye(c) - 1.0 / c
    ginv = [None] * c
    for i, j in enumerate(g): ginv[j] = i
    Pinv = np.zeros((D, D))
    for i in range(c): Pinv[ginv[i], i] = 1.0
    for k in range(c, D): Pinv[k, k] = -1.0
    # Pinv acts on the all-ones direction trivially; restrict check of det on sum-zero + extra
    R1 = so_path(Pinv, c, wind) if (np.linalg.det(Pinv) > 0) else None
    if R1 is None:
        # det(Pinv) on R^c(+extra) = sgn * (-1)^extra ; the ones-direction is fixed, fine
        return None
    def R(s):
        k = int(np.floor(s)); fr = s - k
        return R1(fr) @ np.linalg.matrix_power(Pinv, k) if k >= 0 else R1(fr) @ np.linalg.matrix_power(np.linalg.inv(Pinv), -k)
    # colours on the lift: vertex j (arrival step j in [0,m)), first lift = arrival at j; colour by propagation from T_0
    col = {v: i for i, v in enumerate(sorted(T[0]))}
    dep = {(j + ell[j]) % m: j for j in range(m)}
    cur = dict(col); liftcol = {}
    # vertices of T_0: their arrival lift is j - m if j > 0 (wrapping), with colour col[v]
    for v in T[0]:
        liftcol[v] = (v if v == 0 else v - m, col[v])
    for i in range(1, m):
        d = dep[i]; a = i
        cur[a] = cur.pop(d); liftcol[a] = (a, cur[a])
    w = {}
    for v, (start, cc) in liftcol.items():
        mid = start + (ell[v] - 1) / 2.0
        w[v] = R(mid / m) @ E[cc]
    G = nx.Graph(); G.add_nodes_from(range(m))
    for t in T: G.add_edges_from(itertools.combinations(sorted(t), 2))
    worst = np.inf
    for A, B in maximal_simplices_B(G):
        P = np.array([w[a] for a in A] + [-w[b] for b in B])
        ok, marg = separate(P)
        if not ok:
            if verbose: print("fail", sorted(A), sorted(B))
            return False, 0.0, D
        worst = min(worst, marg)
    return True, worst, D

def certificate(m, ell, T, c, g, extra=None, verbose=False):
    sg = sign(g)
    if extra is None: extra = (sg < 0)
    D = c + (1 if extra else 0)
    ginv = [None] * c
    for i, j in enumerate(g): ginv[j] = i
    Pinv = np.zeros((D, D))
    for i in range(c): Pinv[ginv[i], i] = 1.0
    for k in range(c, D): Pinv[k, k] = -1.0
    n = so_path(Pinv, c, "count")
    best = (False, 0.0, D)
    for wind in itertools.product((0, -1, 1), repeat=n):
        r = certificate1(m, ell, T, c, g, extra, verbose, wind)
        if r and r[0] and r[1] > best[1]: best = r
        if best[0] and best[1] > 0.05: break
    return best

def separate(P, iters=20000):
    """find y with P y > 0 (exact check on floats); perceptron + normalisation; returns (ok, margin)."""
    P = P / np.linalg.norm(P, axis=1, keepdims=True)
    y = P.mean(axis=0)
    for _ in range(iters):
        s = P @ y
        k = int(np.argmin(s))
        if s[k] > 1e-9:
            return True, float(s[k] / np.linalg.norm(y))
        y = y + P[k]
    return False, 0.0

def run(name, m, ell, dmax=None, cert=True):
    G, T, c = chain(m, ell)
    g = holonomy(m, ell, T, c); sg = sign(g)
    if dmax is None: dmax = c + 1
    x = chi(G); Lh = L_h(G, dmax)
    cs = ""
    if cert:
        r = certificate(m, ell, T, c, g)
        if r is None: cs = "cert:n/a"
        else:
            ok, marg, D = r
            cs = f"cert ind<= {D-2} -> Lind<={D}: {'OK' if ok else 'FAIL'} (margin {marg:.3f})"
    print(f"{name:28s} c={c} m={m} hol={g} sgn={'+' if sg>0 else '-'} chi={x} L_h={Lh}  {cs}")
    sys.stdout.flush()
    return c, g, sg, x, Lh

if __name__ == "__main__":
    for c in (3, 4):
        for m in range(c + 1, 3 * c + 3):
            run(f"C_{m}^{c-1}", m, [c] * m)
