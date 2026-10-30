# R09 researcher1: channel values for the m=2 size-2 ring with union C4 (1-3-2-4-1),
# P1 = path 4-1-3-2, P2 = C4. Fit each channel value as a polynomial in q (Lagrange, exact).
import sys, os
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r09_scan import ring_T
from r09_m2 import channels_from_T
E1 = [(1,3),(1,4),(2,3)]
E2 = [(1,3),(1,4),(2,3),(2,4)]
def lagrange_coeffs(xs, ys):
    n = len(xs)
    # solve Vandermonde exactly
    A = [[Fraction(x)**j for j in range(n)] + [Fraction(y)] for x, y in zip(xs, ys)]
    for i in range(n):
        p = next(r for r in range(i, n) if A[r][i] != 0)
        A[i], A[p] = A[p], A[i]
        piv = A[i][i]
        A[i] = [v / piv for v in A[i]]
        for r in range(n):
            if r != i and A[r][i] != 0:
                f = A[r][i]
                A[r] = [a - f*b for a, b in zip(A[r], A[i])]
    return [A[i][n] for i in range(n)]
qs = list(range(4, 11))
data = {}
for q in qs:
    pairs, T, tr = ring_T(q, frozenset(E1), frozenset(E2))
    ch = channels_from_T(q, T, pairs)
    for k, v in ch.items():
        data.setdefault(k, []).append(v)
    data.setdefault('Tr', []).append(Fraction(tr))
for k in data:
    c = lagrange_coeffs(qs, data[k])
    s = " + ".join("%s*q^%d" % (c[j], j) for j in range(len(c)) if c[j] != 0)
    print(k, ":", s)
print("values q=4..10:", {k: [str(x) for x in v] for k, v in data.items()})
