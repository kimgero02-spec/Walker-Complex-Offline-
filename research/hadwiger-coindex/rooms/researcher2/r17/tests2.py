import sys
sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r17')
from k7minor import base_edges, cross_pairs, has_K_minor
import time
full = set(cross_pairs())
def run(name, keep):
    removed = full - set(keep)
    E = base_edges() | set(keep)
    t = time.time()
    r = has_K_minor(E, 7)
    print(f"{name}: kept_cross={len(keep)} edges={len(E)} K7={r} ({round(time.time()-t,1)}s)", flush=True)
run("G2 perfect matching only", [(i + 1, 6 + i) for i in range(5)])
run("G3 hub to all c + rim to c0", [(0, v) for v in range(6, 11)] + [(i, 6) for i in range(1, 6)])
run("G4 two rim vertices to all c (r1,r3)", [(1, v) for v in range(6, 11)] + [(3, v) for v in range(6, 11)])
