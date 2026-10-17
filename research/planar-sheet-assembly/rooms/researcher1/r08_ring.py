# R08 researcher1: ring frame check. Pure python (no numpy/sympy needed).
import itertools

def colorings(vertices, edges, q):
    """all proper q-colorings of piece (vertices list, edges list of pairs), as dicts"""
    out = []
    for vals in itertools.product(range(q), repeat=len(vertices)):
        c = dict(zip(vertices, vals))
        if all(c[a] != c[b] for a, b in edges):
            out.append(c)
    return out

def ring_trace(pieces, q):
    """pieces: list of (vertices, edges, Lj, Rj) with Lj, Rj tuples of junction vertices;
    Rj of piece i must equal Lj of piece i+1 (cyclic). Returns (trace, number of colorings count).
    Trace = sum over junction labelings of product of piece counts = #proper colorings of G
    (when pieces share only junction vertices). Also returns boolean trace."""
    m = len(pieces)
    idx = lambda labs: tuple(labs)
    # N_i as dict: (x,y) -> count, x in [q]^L_i, y in [q]^R_i
    Ns = []
    for (V, E, L, R) in pieces:
        N = {}
        for c in colorings(V, E, q):
            key = (tuple(c[v] for v in L), tuple(c[v] for v in R))
            N[key] = N.get(key, 0) + 1
        Ns.append(N)
    # all junction-label tuples of the first junction
    L0 = pieces[0][2]
    labs0 = list(itertools.product(range(q), repeat=len(L0)))
    tr = 0
    btr = 0
    for x0 in labs0:
        # vector over current junction labels
        vec = {x0: 1}
        for N in Ns:
            new = {}
            for x, w in vec.items():
                for (a, b), cnt in N.items():
                    if a == x:
                        new[b] = new.get(b, 0) + w * cnt
            vec = new
        tr += vec.get(x0, 0)
    return tr

def chi_ring(pieces, qmax=8):
    for q in range(1, qmax + 1):
        if ring_trace(pieces, q) > 0:
            return q
    return None

def cycle_pieces(m):
    """C_m as ring of m edge pieces, junction vertex v_i (vertices 0..m-1)"""
    pcs = []
    for i in range(m):
        u, w = i, (i + 1) % m
        pcs.append(((u, w), [(u, w)], (u,), (w,)))
    return pcs

def chrom_cycle(m, q):
    return (q - 1) ** m + (-1) ** m * (q - 1)

if __name__ == "__main__":
    # C5 via 5 K2 pieces: expect P=(q-1)^5-(q-1), chi=3
    for m in (4, 5):
        pcs = cycle_pieces(m)
        print("C%d" % m, [ring_trace(pcs, q) for q in range(1, 6)],
              [chrom_cycle(m, q) for q in range(1, 6)], "chi =", chi_ring(pcs))

    # K4 as 3-ring: P1 triangle {1,2,3}, P2 path 1-4-2, P3 edge {3,4}
    # junctions: S31={3} (between P3 and P1), S12={1,2} (P1-P2), S24={4} (P2-P3)
    K4 = [
        ((1, 2, 3), [(1, 2), (2, 3), (1, 3)], (3,), (1, 2)),
        ((1, 4, 2), [(1, 4), (4, 2)], (1, 2), (4,)),
        ((4, 3), [(4, 3)], (4,), (3,)),
    ]
    print("K4 traces q=1..5:", [ring_trace(K4, q) for q in range(1, 6)], "(chi(K4)*? expect q(q-1)(q-2)(q-3) =", [q*(q-1)*(q-2)*(q-3) for q in range(1, 6)], ")")
    print("K4 chi =", chi_ring(K4))

    # Triangle ring: pieces triangle{v_i,v_{i+1},p_i}, m=3; expect q(q-1)(q-2)^4, chi=3
    TR = []
    for i in range(3):
        v, w, p = i, (i + 1) % 3, 3 + i
        TR.append(((v, w, p), [(v, w), (w, p), (v, p)], (v,), (w,)))
    print("triangle-ring traces q=1..5:", [ring_trace(TR, q) for q in range(1, 6)],
          "formula q(q-1)(q-2)^4:", [q * (q - 1) * (q - 2) ** 4 for q in range(1, 6)], "chi =", chi_ring(TR))

    # Ring of 3 paths of length 2 (= C6): expect (q-1)^6+(q-1)
    P2 = []
    for i in range(3):
        v, w, x = i, (i + 1) % 3, 3 + i
        P2.append(((v, x, w), [(v, x), (x, w)], (v,), (w,)))
    print("path-ring (C6) traces:", [ring_trace(P2, q) for q in range(1, 6)],
          "expect:", [(q - 1) ** 6 + (q - 1) for q in range(1, 6)])
