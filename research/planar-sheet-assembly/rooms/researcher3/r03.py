"""R03 researcher3 (CS view): polygon ribbon manual with b>=2 boundary circles.
Skeleton G = disjoint cycles W_1..W_b + arcs (a matching after suppressing degree-2 vertices).
Criterion F:  G planar <=> (A) every W_k-bridge overlap graph O_k is bipartite
                         and (B) every block of the connection graph C (= H^*) is flip-planar,
(B) decided by the Z2 linear system  sum_t lam_t N_et N_ft = A0(e,f).
Own code only (surf.py is mine from R02)."""
import itertools
import networkx as nx
import numpy as np
from surf import Manual, rank2

# ---------------- boundary circles and arcs ----------------
def circles(Mn):
    out = []
    for comp in nx.connected_components(Mn.R):
        sub = Mn.R.subgraph(comp)
        start = min(comp, key=str); cyc = [start]; prev = None; cur = start
        used = set()
        while True:
            nxt = None
            for _, v, key in sub.edges(cur, keys=True):
                if (frozenset((cur, v)), key) not in used:
                    nxt = (v, key); break
            if nxt is None:
                break
            used.add((frozenset((cur, nxt[0])), nxt[1])); cur = nxt[0]
            if cur == start:
                break
            cyc.append(cur)
        out.append(cyc)
    return out

def skeleton_data(Mn):
    Ws = circles(Mn)
    where = {}
    for i, W in enumerate(Ws):
        for t, v in enumerate(W):
            where[v] = (i, t)
    ends = {e: (p[0], p[-1]) for e, (_, _, p) in enumerate(Mn.arcs)}
    return Ws, where, ends

def skew(L, A, B):
    """A, B: sets of positions on a circle of length L (distinct points). skew-overlap?"""
    for a1, a2 in itertools.combinations(sorted(A), 2):
        for b1, b2 in itertools.combinations(B, 2):
            if len({a1, a2, b1, b2}) < 4:
                continue
            if (a1 < b1 < a2) != (a1 < b2 < a2):
                return True
    return len(set(A) & set(B)) >= 3

# ---------------- (A) ----------------
def condition_A(Mn, verbose=False):
    Ws, where, ends = skeleton_data(Mn)
    b = len(Ws)
    C = nx.MultiGraph(); C.add_nodes_from(range(b))
    for e, (x, y) in ends.items():
        C.add_edge(where[x][0], where[y][0], key=e)
    ok = True
    for k in range(b):
        L = len(Ws[k]); bridges = []
        for e, (x, y) in ends.items():
            if where[x][0] == k and where[y][0] == k:
                bridges.append(("chord", e, {where[x][1], where[y][1]}))
        Ck = C.copy(); Ck.remove_node(k)
        for comp in nx.connected_components(Ck):
            att = set()
            for e, (x, y) in ends.items():
                ix, iy = where[x][0], where[y][0]
                if ix == k and iy in comp: att.add(where[x][1])
                if iy == k and ix in comp: att.add(where[y][1])
            bridges.append(("comp", tuple(sorted(comp)), att))
        O = nx.Graph(); O.add_nodes_from(range(len(bridges)))
        for p, q in itertools.combinations(range(len(bridges)), 2):
            if skew(L, bridges[p][2], bridges[q][2]):
                O.add_edge(p, q)
        bip = nx.is_bipartite(O)
        if verbose:
            print("  W%d: %d bridges, O_k edges %d, bipartite %s" % (k, len(bridges), O.number_of_edges(), bip))
        ok &= bip
    return ok, C, Ws, where, ends

# ---------------- (B) ----------------
def blocks_of(C):
    S = nx.Graph()
    for u, v in C.edges():
        if u != v: S.add_edge(u, v)
    S.add_nodes_from(C.nodes())
    out = []
    for bl in nx.biconnected_components(S):
        if len(bl) < 2: continue
        es = [k for u, v, k in C.edges(keys=True) if u != v and u in bl and v in bl]
        out.append((sorted(bl), es))
    return out

def rotations(block, Ws, where, ends):
    """rotation at each node: list of half-edges (e, node) in cyclic order along W."""
    nodes, es = block
    rot = {}
    for v in nodes:
        hs = []
        for e in es:
            for x in ends[e]:
                if where[x][0] == v:
                    hs.append((where[x][1], e))
        rot[v] = [(e, v) for _, e in sorted(hs)]
    return rot

def faces_genus0(rot, es, flips):
    """orientable rotation system, vertex v reversed if flips[v]; return planar?"""
    R = {v: (r[::-1] if flips[v] else r) for v, r in rot.items()}
    nxt = {}
    for v, r in R.items():
        for i, h in enumerate(r):
            nxt[h] = r[(i + 1) % len(r)]
    other = {}
    for e in es:
        hs = [h for r in R.values() for h in r if h[0] == e]
        other[hs[0]] = hs[1]; other[hs[1]] = hs[0]
    seen = set(); F = 0
    for h in nxt:
        if h in seen: continue
        F += 1; x = h
        while x not in seen:
            seen.add(x); x = nxt[other[x]]
    V = len(R); E = len(es)
    return V - E + F == 2

def bouquet_word(rot, es, tree, root, lam):
    """merge rotations along rooted spanning tree; lam[t]=1 -> reverse subtree word."""
    T = nx.Graph()
    for t in tree:
        u, v = [h[1] for r in rot.values() for h in r if h[0] == t]
        T.add_edge(u, v, key=t)
    T.add_nodes_from(rot)
    def word(v, parent_edge):
        r = rot[v]
        if parent_edge is not None:
            i = [j for j, h in enumerate(r) if h[0] == parent_edge][0]
            r = r[i + 1:] + r[:i]
        out = []
        for h in r:
            if h[0] in tree and h[0] != parent_edge:
                # child
                child = [x[1] for rr in rot.values() for x in rr if x[0] == h[0] and x[1] != v][0]
                w = word(child, h[0])
                if lam[h[0]]: w = w[::-1]
                out.extend(w)
            else:
                out.append(h)
        return out
    return word(root, None)

def interlace(word, cot):
    pos = {e: [i for i, h in enumerate(word) if h[0] == e] for e in cot}
    A = np.zeros((len(cot), len(cot)), dtype=np.uint8)
    for a, c in itertools.combinations(range(len(cot)), 2):
        x0, x1 = pos[cot[a]]; y0, y1 = pos[cot[c]]
        A[a, c] = A[c, a] = 1 if ((x0 < y0 < x1) != (x0 < y1 < x1)) else 0
    return A

def tree_and_N(rot, es, root):
    S = nx.MultiGraph()
    for e in es:
        u, v = [h[1] for r in rot.values() for h in r if h[0] == e]
        S.add_edge(u, v, key=e)
    bfs = {root: None}; order = [root]; tree = []
    for u in order:
        for _, v, k in S.edges(u, keys=True):
            if v not in bfs:
                bfs[v] = (u, k); order.append(v); tree.append(k)
    cot = [e for e in es if e not in tree]
    # N[e,t] = 1 iff t on tree path between ends of cotree edge e
    def path_edges(v):
        p = []
        while bfs[v] is not None:
            p.append(bfs[v][1]); v = bfs[v][0]
        return p
    N = np.zeros((len(cot), len(tree)), dtype=np.uint8)
    for a, e in enumerate(cot):
        u, v = [h[1] for r in rot.values() for h in r if h[0] == e]
        for t in set(path_edges(u)) ^ set(path_edges(v)):
            N[a, tree.index(t)] = 1
    return tree, cot, N

def solve2(A, rhs):
    """solvable? A x = rhs over GF(2)"""
    return rank2(A) == rank2(np.concatenate([A, rhs.reshape(-1, 1)], axis=1))

def condition_B_block(rot, es, check=True):
    root = min(rot)
    tree, cot, N = tree_and_N(rot, es, root)
    lam0 = {t: 0 for t in tree}
    A0 = interlace(bouquet_word(rot, es, tree, root, lam0), cot)
    rows, rhs = [], []
    for a, c in itertools.combinations(range(len(cot)), 2):
        rows.append([N[a, j] & N[c, j] for j in range(len(tree))]); rhs.append(A0[a, c])
    if rows:
        lin = solve2(np.array(rows, dtype=np.uint8), np.array(rhs, dtype=np.uint8))
    else:
        lin = True
    info = {"vars": len(tree), "eqs": len(rows)}
    if check:
        # step check 1: toggle formula for every lam (small blocks only)
        formula_ok = True
        for bits in itertools.product([0, 1], repeat=len(tree)):
            lam = dict(zip(tree, bits))
            A = interlace(bouquet_word(rot, es, tree, root, lam), cot)
            pred = A0.copy()
            for a, c in itertools.combinations(range(len(cot)), 2):
                pred[a, c] ^= sum(bits[j] & N[a, j] & N[c, j] for j in range(len(tree))) % 2
                pred[c, a] = pred[a, c]
            formula_ok &= bool((A == pred).all())
        # step check 2: brute-force flips with face counting
        nodes = sorted(rot)
        brute = any(faces_genus0(rot, es, dict(zip(nodes, s)))
                    for s in itertools.product([0, 1], repeat=len(nodes)))
        info.update(formula_ok=formula_ok, brute=brute)
    return lin, info

def criterion(Mn, name, verbose=True):
    okA, C, Ws, where, ends = condition_A(Mn, verbose=verbose)
    okB = True; infos = []
    for bl in blocks_of(C):
        rot = rotations(bl, Ws, where, ends)
        lin, info = condition_B_block(rot, bl[1])
        okB &= lin; infos.append((bl[0], lin, info))
    real = nx.check_planarity(Mn.G)[0]
    print("%-28s b=%d  (A)=%s (B)=%s -> pred %s | real planar %s | blocks %s" %
          (name, len(Ws), okA, okB, okA and okB, real, infos))
    return okA and okB, real
