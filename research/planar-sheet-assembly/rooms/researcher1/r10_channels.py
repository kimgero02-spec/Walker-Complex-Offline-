# R10 researcher1: explicit s=2 channel matrices rho_lambda(N) in terms of orbit coordinates n_pi,
# check (i) multiplicativity, (ii) trace identity, (iii) examples (R09 C4, K4 m=2 splits).
# Coordinates: x=(x1,x2) row junction, y=(y1,y2) column junction; points labelled 0=x1,1=x2,2=y1,3=y2.
import itertools, random
import numpy as np
from fractions import Fraction

def kernel(t):
    seen = {}
    lab = []
    for v in t:
        if v not in seen: seen[v] = len(seen)
        lab.append(seen[v])
    return tuple(lab)          # restricted growth string = set partition of 4 points

ALL = sorted({kernel(t) for t in itertools.product(range(4), repeat=4)})   # 15 partitions

def matrix_from_n(q, n):
    idx = list(itertools.product(range(q), repeat=2))
    M = np.zeros((q*q, q*q), dtype=object)
    for i, x in enumerate(idx):
        for j, y in enumerate(idx):
            M[i, j] = n[kernel(x + y)]
    return M, idx

def n_from_matrix(q, M, idx):
    n = {}
    for i, x in enumerate(idx):
        for j, y in enumerate(idx):
            n.setdefault(kernel(x + y), M[i, j])
    return n

# name helper: partition given as string like '0 1|2 3' -> rgs
def P(s):
    blocks = [list(map(int, b.split())) for b in s.split('|')]
    lab = [None]*4
    for k, b in enumerate(blocks):
        for v in b: lab[v] = k
    return kernel(tuple(lab))

def rho(q, n):
    g = lambda s: n[P(s)]
    # f_j values (alpha,beta,gamma,delta,eps) for the three embeddings iota_1,2,3
    a1 = g('0 1 2 3'); b1 = g('0 1|2 3')
    c1 = g('0 2 3|1'); d1 = g('0|1 2 3'); e1 = g('0|1|2 3')
    a2 = (q-1)*g('0 1 2|3'); b2 = g('0 1 3|2') + (q-2)*g('0 1|2|3')
    c2 = g('0 2|1 3') + (q-2)*g('0 2|1|3'); d2 = g('0 3|1 2') + (q-2)*g('0|1 2|3')
    e2 = g('0 3|1|2') + g('0|1 3|2') + (q-3)*g('0|1|2|3')
    a3 = (q-1)*g('0 1 3|2'); b3 = g('0 1 2|3') + (q-2)*g('0 1|2|3')
    c3 = g('0 3|1 2') + (q-2)*g('0 3|1|2'); d3 = g('0 2|1 3') + (q-2)*g('0|1 3|2')
    e3 = g('0 2|1|3') + g('0|1 2|3') + (q-3)*g('0|1|2|3')
    triv = [[a1+(q-1)*b1, a2+(q-1)*b2],
            [c1+d1+(q-2)*e1, c2+d2+(q-2)*e2]]
    std = [[a1-b1, a2-b2, a3-b3],
           [c1-e1, c2-e2, c3-e3],
           [d1-e1, d2-e2, d3-e3]]
    per = (g('0 2|1 3') + g('0 3|1 2') - g('0 2|1|3') - g('0 3|1|2')
           - g('0|1 2|3') - g('0|1 3|2') + 2*g('0|1|2|3'))
    det = (g('0 2|1 3') - g('0 3|1 2') + g('0 3|1|2') - g('0 2|1|3')
           + g('0|1 2|3') - g('0|1 3|2'))
    return np.array(triv, dtype=object), np.array(std, dtype=object), per, det

def dims(q):
    return 1, q-1, Fraction(q*(q-3), 2), Fraction((q-1)*(q-2), 2)

def trace_formula(q, rs):
    T = np.identity(2, dtype=object); S = np.identity(3, dtype=object); p = 1; d = 1
    for (t, s, pe, de) in rs:
        T = T.dot(t); S = S.dot(s); p *= pe; d *= de
    dt, ds, dp, dd = dims(q)
    parts = (np.trace(T), ds*np.trace(S), dp*p, dd*d)
    return parts

def test_random():
    for q in (4, 5, 6):
        for trial in range(3):
            n1 = {p: random.randint(-3, 3) for p in ALL}
            n2 = {p: random.randint(-3, 3) for p in ALL}
            M1, idx = matrix_from_n(q, n1); M2, _ = matrix_from_n(q, n2)
            M12 = M1.dot(M2)
            n12 = n_from_matrix(q, M12, idx)
            # invariance check of product (must be S_q invariant -> consistent n)
            r1, r2, r12 = rho(q, n1), rho(q, n2), rho(q, n12)
            ok_mult = (all((r1[0].dot(r2[0]) == r12[0]).flat) and all((r1[1].dot(r2[1]) == r12[1]).flat)
                       and r1[2]*r2[2] == r12[2] and r1[3]*r2[3] == r12[3])
            ok_tr = sum(trace_formula(q, [r12])) == np.trace(M12)
            ok_tr1 = sum(trace_formula(q, [r1])) == np.trace(M1)
            print('q=%d trial %d: multiplicative %s, trace(N1N2) %s, trace(N1) %s' % (q, trial, ok_mult, ok_tr, ok_tr1))

# --- pieces: graph on junction points + private vertices; n_pi = # colourings of private part
def piece_n(q, edges, private, jx, jy):
    # jx=(v_x1,v_x2), jy=(v_y1,v_y2) vertex names; edges among any vertices
    n = {}
    for pi in ALL:
        lab = {}
        # assign colours to junction points according to pi (block k -> colour k)
        jv = list(jx) + list(jy)
        col = {}
        bad = False
        for pt, v in enumerate(jv):
            c = pi[pt]
            if v in col and col[v] != c: bad = True
            col[v] = c
        # same vertex appearing twice must get same block; else contributes 0 automatically (N(x,y)=0)
        if bad: n[pi] = 0; continue
        if max(pi) + 1 > q: n[pi] = 0; continue
        cnt = 0
        for pc in itertools.product(range(q), repeat=len(private)):
            c2 = dict(col); c2.update(zip(private, pc))
            if all(c2[u] != c2[v] for u, v in edges): cnt += 1
        n[pi] = cnt
    return n

def ring_m2(q, E1, priv1, E2, priv2, S1, S2):
    # N1: rows S2(=S0), cols S1 ; N2: rows S1, cols S2
    n1 = piece_n(q, E1, priv1, S2, S1)
    n2 = piece_n(q, E2, priv2, S1, S2)
    return [rho(q, n1), rho(q, n2)], (n1, n2)

def brute_P(q, V, E):
    V = list(V)
    return sum(1 for c in itertools.product(range(q), repeat=len(V))
               if all(c[V.index(u)] != c[V.index(v)] for u, v in E))

def show(name, V, E1, priv1, E2, priv2, S1, S2, qs=(4, 5, 6, 7)):
    print('==', name)
    E = sorted(set(map(tuple, map(sorted, E1 + E2))))
    for q in qs:
        rs, _ = ring_m2(q, E1, priv1, E2, priv2, S1, S2)
        parts = trace_formula(q, rs)
        print(' q=%d  triv=%s std=%s (q-2,2)=%s (q-2,1,1)=%s  sum=%s  P_G=%s | per=%s,%s det=%s,%s' % (
            q, parts[0], parts[1], parts[2], parts[3], sum(parts), brute_P(q, V, E),
            rs[0][2], rs[1][2], rs[0][3], rs[1][3]))

if __name__ == '__main__':
    random.seed(1)
    test_random()
    # R09 C4 example: S1={1,2}, S2={3,4}; P1 = 14,13,23 ; P2 = 13,14,23,24
    show('R09 C4', [1, 2, 3, 4], [(1, 4), (1, 3), (2, 3)], [], [(1, 3), (1, 4), (2, 3), (2, 4)], [], (1, 2), (3, 4))
    # K4 split: P1 = {12,13,24} (path 3-1-2-4), P2 = {34,14,23} (path 1-4-3-2)
    show('K4 split A (paths)', [1, 2, 3, 4], [(1, 2), (1, 3), (2, 4)], [], [(3, 4), (1, 4), (2, 3)], [], (1, 2), (3, 4))
    # K4 split B: P1 = {12,34,13,14,23}, P2 = {14,23,24}
    show('K4 split B', [1, 2, 3, 4], [(1, 2), (3, 4), (1, 3), (1, 4), (2, 3)], [], [(1, 4), (2, 3), (2, 4)], [], (1, 2), (3, 4))
    # K4 split C: det of P2 zero -> channel dies
    show('K4 split C', [1, 2, 3, 4], [(1, 2), (3, 4), (1, 3), (1, 4), (2, 3)], [], [(2, 4)], [], (1, 2), (3, 4))
    # example with private vertices: G = octahedron-like? piece with private vertex 5 adjacent to 1,3 ; and 6 adjacent to 2,4
    show('priv: P1=13+5(1,4), P2=24+6(2,3)+34+12', [1, 2, 3, 4, 5, 6],
         [(1, 3), (5, 1), (5, 4)], [5], [(2, 4), (6, 2), (6, 3), (3, 4), (1, 2)], [6], (1, 2), (3, 4))
