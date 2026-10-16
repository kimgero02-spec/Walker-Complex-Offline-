"""R02 researcher3: ribbon manual -> assembly surface X, Z2 intersection form Q (bouquet),
boundary-chord interlace matrix M on W = dX (b=1), check M = N^T Q^{-1} N, rank = Euler genus,
W-bridge overlap graph (Tutte).  Own code, no import from other rooms."""
import networkx as nx
import numpy as np
from itertools import combinations

# ---------- GF(2) linear algebra ----------
def rank2(A):
    A = (np.array(A, dtype=np.uint8) % 2).copy()
    if A.size == 0:
        return 0
    r = 0
    rows, cols = A.shape
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i, c]:
                piv = i; break
        if piv is None:
            continue
        A[[r, piv]] = A[[piv, r]]
        for i in range(rows):
            if i != r and A[i, c]:
                A[i] ^= A[r]
        r += 1
        if r == rows:
            break
    return r

def inv2(A):
    A = np.array(A, dtype=np.uint8) % 2
    n = A.shape[0]
    M = np.concatenate([A, np.eye(n, dtype=np.uint8)], axis=1)
    r = 0
    for c in range(n):
        piv = None
        for i in range(r, n):
            if M[i, c]:
                piv = i; break
        if piv is None:
            return None
        M[[r, piv]] = M[[piv, r]]
        for i in range(n):
            if i != r and M[i, c]:
                M[i] ^= M[r]
        r += 1
    return M[:, n:]

# ---------- manual ----------
class Manual:
    """pieces: {k: rim list (cyclic)}; arcs: list of (i, j, path) path = vertex list,
    a subpath of both rims; interior: {k: list of extra edges inside piece k}."""
    def __init__(self, pieces, arcs, interior=None):
        self.P = pieces
        self.arcs = arcs
        self.inner = interior or {}
        self.build()

    def rim_edges(self, k):
        c = self.P[k]
        return [(c[t], c[(t + 1) % len(c)]) for t in range(len(c))]

    def orient(self, k, path):
        """+1 if rim k traverses path in given direction, -1 if reversed; also position."""
        c = self.P[k]; L = len(c)
        for t in range(L):
            if all(c[(t + s) % L] == path[s] for s in range(len(path))):
                return +1, t
            if all(c[(t + s) % L] == path[::-1][s] for s in range(len(path))):
                return -1, t
        raise ValueError("arc %s not on rim %s" % (path, k))

    def build(self):
        G = nx.MultiGraph()
        for k, c in self.P.items():
            for u, v in self.rim_edges(k):
                G.add_edge(u, v)
            for u, v in self.inner.get(k, []):
                G.add_edge(u, v)
        # glue: identical labels already identify; collapse multi-edges from arcs
        self.G = nx.Graph(G)
        self.H = nx.MultiGraph()
        self.H.add_nodes_from(self.P)
        self.eps = {}
        self.rho = {k: [] for k in self.P}
        for e, (i, j, path) in enumerate(self.arcs):
            ti, pi = self.orient(i, path)
            tj, pj = self.orient(j, path)
            self.eps[e] = -ti * tj
            self.H.add_edge(i, j, key=e)
            self.rho[i].append((pi, e))
            self.rho[j].append((pj, e))
        for k in self.rho:
            self.rho[k] = [e for _, e in sorted(self.rho[k])]
        # rails & boundary
        arc_edges = {k: set() for k in self.P}
        for e, (i, j, path) in enumerate(self.arcs):
            for s in range(len(path) - 1):
                f = frozenset((path[s], path[s + 1]))
                arc_edges[i].add(f); arc_edges[j].add(f)
        R = nx.MultiGraph()
        self.rail_piece = {}
        for k in self.P:
            for u, v in self.rim_edges(k):
                if frozenset((u, v)) not in arc_edges[k]:
                    R.add_edge(u, v, piece=k)
        self.R = R
        comps = list(nx.connected_components(R))
        self.b = len(comps)
        assert all(d == 2 for _, d in R.degree()), "boundary not a union of circles (pinch?)"
        self.chi = self.H.number_of_nodes() - self.H.number_of_edges()
        self.arc_edges = arc_edges

    # ---- holonomy of a cycle of H given as list of edge keys forming closed walk ----
    def holonomy_edges(self, keys):
        p = 1
        for e in keys:
            p *= self.eps[e]
        return p

    def orientable(self):
        # 2-colour pieces by orientation
        s = {}
        for comp in nx.connected_components(self.H):
            r = next(iter(comp)); s[r] = 1; stack = [r]
            while stack:
                u = stack.pop()
                for _, v, e in self.H.edges(u, keys=True):
                    want = s[u] * self.eps[e]
                    if v not in s:
                        s[v] = want; stack.append(v)
                    elif s[v] != want:
                        return False
        return True

    def euler_genus(self):
        return 2 - self.chi - self.b

    # ---- bouquet by spanning-tree contraction (signed rotation system) ----
    def bouquet(self):
        rot = {k: [(e, k) for e in self.rho[k]] for k in self.P}  # half-edges (edge, end-vertex tag)
        # half-edge tags: for loop-free H each edge e has ends i,j ; tag by vertex name
        sign = dict(self.eps)
        T = nx.minimum_spanning_tree(nx.Graph(self.H))
        tree_keys = set()
        for u, v in T.edges():
            # pick one H-edge key between u,v
            ks = sorted(self.H[u][v].keys())
            tree_keys.add(ks[0])
        parent = {k: k for k in self.P}
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        members = {k: {k} for k in self.P}
        for e in sorted(tree_keys):
            i, j, _ = self.arcs[e]
            u, v = find(i), find(j)
            ru, rv = rot[u], rot[v]
            hu = [t for t, h in enumerate(ru) if h[0] == e and h[1] == i]
            hv = [t for t, h in enumerate(rv) if h[0] == e and h[1] == j]
            hu, hv = hu[0], hv[0]
            if sign[e] == -1:
                # flip block v: reverse rotation, toggle signs of edges with exactly one end in block
                rv = rv[::-1]
                hv = len(rv) - 1 - hv
                inblock = members[v]
                for f, (a, c, _) in enumerate(self.arcs):
                    if (a in inblock) != (c in inblock):
                        sign[f] = -sign[f]
            a_seq = ru[hu + 1:] + ru[:hu]
            b_seq = rv[hv + 1:] + rv[:hv]
            rot[u] = a_seq + b_seq
            del rot[v]
            parent[v] = u
            members[u] |= members[v]
        assert len(rot) == 1
        seq = list(rot.values())[0]
        loops = sorted(set(h[0] for h in seq))
        pos = {e: [t for t, h in enumerate(seq) if h[0] == e] for e in loops}
        n = len(loops)
        Q = np.zeros((n, n), dtype=np.uint8)
        for a, e in enumerate(loops):
            Q[a, a] = 1 if sign[e] == -1 else 0
            for c, f in enumerate(loops):
                if c <= a:
                    continue
                x0, x1 = pos[e]; y0, y1 = pos[f]
                inter = (x0 < y0 < x1) != (x0 < y1 < x1)
                Q[a, c] = Q[c, a] = 1 if inter else 0
        # fundamental cycles as edge-incidence rows
        Tg = nx.MultiGraph()
        for e in tree_keys:
            i, j, _ = self.arcs[e]; Tg.add_edge(i, j, key=e)
        Tg.add_nodes_from(self.P)
        Nrows = []
        for e in loops:
            i, j, _ = self.arcs[e]
            path = nx.shortest_path(nx.Graph(Tg), i, j)
            row = np.zeros(len(self.arcs), dtype=np.uint8); row[e] = 1
            for s in range(len(path) - 1):
                ks = [k for k in Tg[path[s]][path[s + 1]]]
                row[ks[0]] ^= 1
            Nrows.append(row)
        N = np.array(Nrows, dtype=np.uint8).reshape(n, len(self.arcs))
        return loops, Q, N, tree_keys

    # ---- boundary cycle W (b=1) and dual interlace matrix M ----
    def W_cycle(self):
        assert self.b == 1
        start = next(iter(self.R.nodes()))
        cyc = [start]; prev = None; cur = start
        used = set()
        while True:
            nxt = None
            for _, v, key in self.R.edges(cur, keys=True):
                if (frozenset((cur, v)), key) not in used:
                    nxt = (v, key); break
            if nxt is None:
                break
            used.add((frozenset((cur, nxt[0])), nxt[1]))
            cur = nxt[0]
            if cur == start:
                break
            cyc.append(cur)
        return cyc

    def w1_cycle(self, cyc_vertices, edge_piece):
        """cyc_vertices closed list; edge_piece[t] = piece assigned to edge t (v_t,v_{t+1})."""
        p = 1; L = len(cyc_vertices)
        for t in range(L):
            a, b = edge_piece[t - 1], edge_piece[t]
            if a != b:
                x = cyc_vertices[t]
                f = self.arc_at(a, x)
                assert f is not None and self.arc_at(b, x) == f, (a, b, x)
                p *= self.eps[f]
        return p

    def arc_at(self, k, x):
        for e, (i, j, path) in enumerate(self.arcs):
            if k in (i, j) and x in path:
                return e
        return None

    def rail_owner(self, u, v):
        ps = [d['piece'] for d in self.R.get_edge_data(u, v).values()]
        return ps[0]

    def dual_M(self):
        W = self.W_cycle(); L = len(W)
        pos = {v: t for t, v in enumerate(W)}
        m = len(self.arcs)
        M = np.zeros((m, m), dtype=np.uint8)
        ends = {e: (path[0], path[-1]) for e, (_, _, path) in enumerate(self.arcs)}
        for e, f in combinations(range(m), 2):
            a, b = sorted((pos[ends[e][0]], pos[ends[e][1]]))
            c, d = pos[ends[f][0]], pos[ends[f][1]]
            if len({a, b, c, d}) < 4:
                continue
            if (a < c < b) != (a < d < b):
                M[e, f] = M[f, e] = 1
        for e, (i, j, path) in enumerate(self.arcs):
            u, v = path[0], path[-1]
            # closed curve: arc u->v (piece i), then W from v back to u
            tv = pos[v]
            wpath = []
            t = tv
            while W[t] != u:
                wpath.append(W[t]); t = (t + 1) % L
            wpath.append(u)
            cyc = list(path) + wpath[1:-1]
            pieces = [i] * (len(path) - 1)
            for s in range(len(wpath) - 1):
                pieces.append(self.rail_owner(wpath[s], wpath[s + 1]))
            M[e, e] = 1 if self.w1_cycle(cyc, pieces) == -1 else 0
        return W, M

# ---------- W-bridges (Tutte) ----------
def bridges(G, W):
    Wset = set(W); L = len(W)
    Wedges = {frozenset((W[t], W[(t + 1) % L])) for t in range(L)}
    out = []
    for u, v in G.edges():
        if u in Wset and v in Wset and frozenset((u, v)) not in Wedges:
            out.append(({u, v}, nx.Graph([(u, v)])))
    Gm = G.subgraph([x for x in G if x not in Wset])
    for comp in nx.connected_components(Gm):
        att = set()
        B = nx.Graph()
        for x in comp:
            for y in G[x]:
                B.add_edge(x, y)
                if y in Wset:
                    att.add(y)
        out.append((att, B))
    return out

def overlap(W, A1, A2):
    pos = {v: t for t, v in enumerate(W)}
    if len(A1 & A2) >= 3:
        return True
    for u, u2 in combinations(A1, 2):
        a, b = sorted((pos[u], pos[u2]))
        for v, v2 in combinations(A2, 2):
            if len({u, u2, v, v2}) < 4:
                continue
            c, d = pos[v], pos[v2]
            if (a < c < b) != (a < d < b):
                return True
    return False

def tutte_report(G, W):
    Bs = bridges(G, W)
    O = nx.Graph(); O.add_nodes_from(range(len(Bs)))
    for x, y in combinations(range(len(Bs)), 2):
        if overlap(W, Bs[x][0], Bs[y][0]):
            O.add_edge(x, y)
    L = len(W)
    Wg = nx.Graph([(W[t], W[(t + 1) % L]) for t in range(L)])
    each = all(nx.check_planarity(nx.compose(Wg, B))[0] for _, B in Bs)
    return Bs, O, nx.is_bipartite(O), each

def planar(G):
    return nx.check_planarity(G)[0]

def report(name, Mn, verbose=True):
    loops, Q, N, T = Mn.bouquet()
    out = {"name": name, "V": Mn.G.number_of_nodes(), "E": Mn.G.number_of_edges(),
           "pieces": len(Mn.P), "arcs": len(Mn.arcs), "b": Mn.b, "chi": Mn.chi,
           "orientable": Mn.orientable(), "eg": Mn.euler_genus(), "rankQ": rank2(Q),
           "detQ": 1 if inv2(Q) is not None else 0, "planarG": planar(Mn.G)}
    # holonomy of fundamental cycles vs diag Q
    hol_ok = True
    for a, e in enumerate(loops):
        keys = [f for f in range(len(Mn.arcs)) if N[a, f]]
        if (Mn.holonomy_edges(keys) == -1) != bool(Q[a, a]):
            hol_ok = False
    out["diagQ=holonomy"] = hol_ok
    if Mn.b == 1:
        W, M = Mn.dual_M()
        Qi = inv2(Q)
        pred = (N.T.astype(int) @ Qi.astype(int) @ N.astype(int)) % 2
        out["M=NtQinvN"] = bool((pred == M).all())
        out["rankM"] = rank2(M)
        I = nx.Graph(); I.add_nodes_from(range(len(Mn.arcs)))
        for e, f in combinations(range(len(Mn.arcs)), 2):
            if M[e, f]:
                I.add_edge(e, f)
        out["I_bipartite"] = nx.is_bipartite(I)
        Bs, O, bip, each = tutte_report(Mn.G, W)
        out["bridges"] = len(Bs); out["overlap_bip"] = bip; out["each_planar"] = each
        out["_M"] = M; out["_W"] = W
    out["_Q"] = Q; out["_N"] = N; out["_loops"] = loops
    if verbose:
        print(name, {k: v for k, v in out.items() if not k.startswith("_")})
    return out
