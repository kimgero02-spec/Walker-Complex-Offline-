"""Exact test of  ind B(G) <= 1  (Z2-map B(G) -> S^1):  S^1 = K(Z,1), so it holds iff the double-cover class
w1 in H^1(B/Z2;Z2) is the mod-2 reduction of an integral class, i.e. iff the cochain w (=1 on edges joining the
two sheets) lies in  Z^1(B/Z2;Z) + 2 C^1  (mod 2).  Integer kernel by unimodular column reduction."""
import itertools, sys, networkx as nx
from topo import simplices_B

def quotient_cells(G):
    G = nx.convert_node_labels_to_integers(G)
    S = simplices_B(G, 2)                       # all simplices of dim <= 2 (|A|+|B| <= 3)
    cells = {0: [], 1: [], 2: []}
    for A, B in S:
        d = len(A) + len(B) - 1
        if d <= 2:
            verts = tuple(sorted([(a, 1) for a in A] + [(b, 2) for b in B]))
            cells[d].append(verts)
    return cells

def tau(v): return (v[0], 3 - v[1])
def perm_sign(seq):
    s = 1; seq = list(seq)
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]: s = -s
    return s

def build(G):
    cells = quotient_cells(G)
    rep = {}; idx = {}
    for d in (0, 1, 2):
        reps = []
        for s in cells[d]:
            t = tuple(sorted(tau(v) for v in s))
            r = min(s, t)
            if r == s and r not in rep:
                pass
        orb = {}
        for s in cells[d]:
            t = tuple(sorted(tau(v) for v in s)); r = min(s, t)
            orb[r] = 1
        reps = sorted(orb)
        idx[d] = {r: i for i, r in enumerate(reps)}
    def cls(s):
        """orbit index and sign: [s] = sign * [rep]"""
        t_img = [tau(v) for v in s]; t = tuple(sorted(t_img))
        if s <= t: return idx[len(s) - 1][s], 1
        # s = tau(t'), with rep = t ; orientation of s vs tau(rep): tau(rep) as image list then sorted
        r = t; img = [tau(v) for v in r]           # tau applied to rep (ordered as rep)
        # s sorted vs img: sign of permutation sorting img
        return idx[len(s) - 1][r], perm_sign(img)
    def bd(d):
        rows = len(idx[d - 1]); M = [[0] * len(idx[d]) for _ in range(rows)]
        for r, j in idx[d].items():
            for i in range(len(r)):
                f = r[:i] + r[i + 1:]
                k, sg = cls(f)
                M[k][j] += (-1) ** i * sg
        return M
    return idx, bd(1), bd(2)

def int_kernel(A, ncols):
    """Z-basis of {x in Z^n : A x = 0} via unimodular column operations."""
    A = [row[:] for row in A]; n = ncols
    U = [[int(i == j) for j in range(n)] for i in range(n)]   # columns of U track ops
    col = 0; r = 0
    rows = len(A)
    piv = 0
    for r in range(rows):
        # gcd-reduce entries A[r][piv:] into column piv
        while True:
            nz = [j for j in range(piv, n) if A[r][j] != 0]
            if len(nz) <= 1: break
            jmin = min(nz, key=lambda j: abs(A[r][j]))
            for j in nz:
                if j != jmin:
                    q = A[r][j] // A[r][jmin]
                    for rr in range(rows): A[rr][j] -= q * A[rr][jmin]
                    for rr in range(n): U[rr][j] -= q * U[rr][jmin]
        nz = [j for j in range(piv, n) if A[r][j] != 0]
        if nz:
            j = nz[0]
            if j != piv:
                for rr in range(rows): A[rr][j], A[rr][piv] = A[rr][piv], A[rr][j]
                for rr in range(n): U[rr][j], U[rr][piv] = U[rr][piv], U[rr][j]
            piv += 1
    return [[U[i][j] for i in range(n)] for j in range(piv, n)]

def in_span_f2(vecs, t):
    basis = {}
    for v in vecs:
        x = 0
        for i, a in enumerate(v):
            if a % 2: x |= 1 << i
        while x:
            p = x.bit_length() - 1
            if p in basis: x ^= basis[p]
            else: basis[p] = x; break
    while t:
        p = t.bit_length() - 1
        if p in basis: t ^= basis[p]
        else: return False
    return True

def ind_le_1(G):
    idx, d1, d2 = build(G)
    E = idx[1]
    # cocycles: f with f o d2 = 0  <=>  d2^T f = 0
    d2T = [[d2[i][j] for i in range(len(E))] for j in range(len(idx[2]))]
    K = int_kernel(d2T, len(E))
    w = 0
    for e, i in E.items():
        if e[0][1] != e[1][1]: w |= 1 << i
    return in_span_f2(K, w)

if __name__ == "__main__":
    from r04 import chain
    tests = [("K3", nx.complete_graph(3)), ("K4", nx.complete_graph(4)), ("C5", nx.cycle_graph(5)),
             ("W5", nx.wheel_graph(6)), ("W4", nx.wheel_graph(5))]
    for m in (6, 7, 8, 9, 10, 11, 12, 13, 14, 16):
        tests.append((f"C_{m}^2", chain(m, [3] * m)[0]))
    for name, G in tests:
        print(name, "ind B <= 1 :", ind_le_1(G)); sys.stdout.flush()
