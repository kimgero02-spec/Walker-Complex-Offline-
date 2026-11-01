# R09 researcher3: top-degree of X(G) vs join formula for vertex partitions. X = B0 with empties.
import itertools, sys, io, contextlib
sys.path.insert(0, ".")
from r06_lib import make, B0_empty, reduced_betti
with contextlib.redirect_stdout(io.StringIO()):
    from r08_checks import graph
def sub(n, E, S):
    idx = {v:i for i,v in enumerate(S)}
    E2 = [(idx[a],idx[b]) for a,b in E if a in idx and b in idx]
    return len(S), E2
def topdeg(n, E):
    b = reduced_betti(B0_empty(make(n, E), n))
    nz = [k for k,v in b.items() if v]
    return (max(nz) if nz else -2), {k:v for k,v in b.items() if v}
def test(name, parts):
    n, E = graph(name)
    tops = []
    for S in parts:
        m, E2 = sub(n, E, S)
        tops.append(topdeg(m, E2)[0])
    T, bT = topdeg(n, E)
    bound = sum(t+1 for t in tops) - 1
    rel = "equal" if T==bound else ("below" if T<bound else "ABOVE")
    print(name, parts, "block tops", tops, "X top", T, bT, "join bound", bound, rel)
test("K5", [[0,1,2,3],[4]])
test("K6", [[0,1,2],[3,4,5]])
test("K6", [[0,1],[2,3,4,5]])
test("K33", [[0,1,2],[3,4,5]])
test("C5K2", [[0,1],[2,3,4,5,6,7,8,9]])
test("C5K2", [[0,1,2,3],[4,5,6,7,8,9]])
test("C5K2", [[0,1,2,3,4],[5,6,7,8,9]])
