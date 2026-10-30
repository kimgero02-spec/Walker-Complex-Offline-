# R09 researcher1: scan m=2 rings with S1={1,2}, S2={3,4}, no private vertices.
# P1, P2 = arbitrary edge sets on {1,2,3,4}. Check which P_2 channels carry nonzero trace.
import itertools, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r09_m2 import channels_from_T
from r09_channel import cycle_types
EDGES = [(1,2),(3,4),(1,3),(1,4),(2,3),(2,4)]  # pairs on {1,2,3,4} (0-indexed below)
def ring_T(q, E1, E2):
    pairs = list(itertools.product(range(q), repeat=2))  # labels x=(x1,x2) on S1, y=(x3,x4) on S2
    # colouring of 4 vertices v=(a,b,c,d) for vertices 1,2,3,4
    def ok(E, col):
        return all(col[u-1] != col[v-1] for (u, v) in E)
    # N1(y,x): P1 with labels (1=x1,2=x2,3=y1,4=y2)
    N1 = {}
    for y in pairs:
        for x in pairs:
            N1[(y, x)] = int(ok(E1, (x[0], x[1], y[0], y[1])))
    N2 = {}
    for x in pairs:
        for y in pairs:
            N2[(x, y)] = int(ok(E2, (x[0], x[1], y[0], y[1])))
    idx = {p: i for i, p in enumerate(pairs)}
    T = [[sum(N2[(x, y)] * N1[(y, xp)] for y in pairs) for xp in pairs] for x in pairs]
    tr = sum(T[i][i] for i in range(len(pairs)))
    return pairs, T, tr
if __name__ == "__main__":
    q = int(sys.argv[1])
    subsets = [frozenset(S) for r in range(len(EDGES)+1) for S in itertools.combinations(EDGES, r)]
    seen = {}
    for E1 in subsets:
        for E2 in subsets:
            pairs, T, tr = ring_T(q, E1, E2)
            ch = channels_from_T(q, T, pairs)
            key = tuple(sorted((k, str(v)) for k, v in ch.items()))
            if key not in seen:
                seen[key] = (sorted(E1), sorted(E2), tr)
    for key, (E1, E2, tr) in seen.items():
        if any(v != '0' for k, v in key if k in ('q-2,2', 'q-2,1,1')):
            print("NONTRIVIAL P2 channel:", key, "E1=", E1, "E2=", E2, "Tr=", tr)
    print("q=%d distinct channel patterns=%d" % (q, len(seen)))
    for key, (E1, E2, tr) in list(seen.items())[:6]:
        print(key, E1, E2, tr)
