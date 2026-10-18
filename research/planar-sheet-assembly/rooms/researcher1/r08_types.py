# R08 researcher1: which diagonal kernel types (partition of base junction) lie in the composite
# for K4 as 3-ring, base junction S={1,2} (size 2). Checks "meets diagonal" vs "contains whole diagonal".
import itertools, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r08_ring import colorings
K4 = {
 "P1": ((1, 2, 3), [(1, 2), (2, 3), (1, 3)], (3,), (1, 2)),
 "P2": ((1, 4, 2), [(1, 4), (4, 2)], (1, 2), (4,)),
 "P3": ((4, 3), [(4, 3)], (4,), (3,)),
}
order = ["P2", "P3", "P1"]  # base junction (1,2) on the left of P2
def relation(piece, q):
    V, E, L, R = piece
    rel = set()
    for c in colorings(V, E, q):
        rel.add((tuple(c[v] for v in L), tuple(c[v] for v in R)))
    return rel
def compose(A, B):
    out = set()
    for (x, y) in A:
        for (y2, z) in B:
            if y == y2:
                out.add((x, z))
    return out
for q in (3, 4):
    comp = None
    for name in order:
        R = relation(K4[name], q)
        comp = R if comp is None else compose(comp, R)
    diag = {(x, x) for x in itertools.product(range(q), repeat=2)}
    hit = comp & diag
    def kind(x):
        return "a=b" if x[0] == x[1] else "a!=b"
    kinds = sorted({kind(x[0]) for x in hit})
    print("q=%d: |composite|=%d, diagonal points in composite=%d, kernel types hit=%s, full diagonal contained=%s"
          % (q, len(comp), len(hit), kinds, diag <= comp))
