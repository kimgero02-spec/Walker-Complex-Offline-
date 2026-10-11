# R15 researcher3: zig under subdivision and contraction (small graphs). zig via r06_lib.zig (brute force, n<=7).
import sys, itertools, io, contextlib
sys.path.insert(0, ".")
from r06_lib import make, zig, popc
def zg(n, E):
    return zig(make(n, E), n)
def K(n): return list(itertools.combinations(range(n), 2))
def subdiv(n, E, e):
    u, v = e; E2 = [x for x in E if x != e]; w = n
    return n+1, E2 + [(u, w), (w, v)]
def contract(n, E, e):
    u, v = e  # merge v into u, relabel
    mp = {}; k = 0
    for x in range(n):
        if x == v: continue
        mp[x] = k; k += 1
    mp[v] = mp[u]
    E2 = set()
    for a, b in E:
        if (a, b) == e: continue
        x, y = mp[a], mp[b]
        if x != y: E2.add((min(x, y), max(x, y)))
    return k, sorted(E2)
C5 = [(i, (i+1) % 5) for i in range(5)]
C4 = [(i, (i+1) % 4) for i in range(4)]
K33 = [(a, b) for a in range(3) for b in range(3, 6)]
PRISM = [(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5)]
W4 = [(0,1),(1,2),(2,3),(3,0),(4,0),(4,1),(4,2),(4,3)]
graphs = {"K3": (3, K(3)), "K4": (4, K(4)), "C5": (5, C5), "K33": (6, K33), "prism": (6, PRISM), "W4": (5, W4), "K4minus": (4, K(4)[1:])}
for name, (n, E) in graphs.items():
    z = zg(n, E)
    line = [f"{name}: zig={z}"]
    for e in E[:1]:
        n2, E2 = subdiv(n, E, e); line.append(f"subdiv1 zig={zg(n2, E2)}")
    for e in E[:1]:
        n3, E3 = contract(n, E, e); line.append(f"contract zig={zg(n3, E3)}")
    print(" | ".join(line))
