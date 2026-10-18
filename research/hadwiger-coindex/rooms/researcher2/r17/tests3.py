import sys
sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r17')
from k7minor import base_edges, cross_pairs, has_K_minor
import time
full = set(cross_pairs())
def run(name, removed):
    E = base_edges() | (full - set(removed))
    t = time.time(); r = has_K_minor(E, 7)
    print(f"{name}: removed={len(removed)} K7={r} ({round(time.time()-t,1)}s)", flush=True)
run("H1 remove rim r1,r2 to all c (10)", [(v, u) for v in (1,2) for u in range(6,11)])
run("H2 remove hub + r1 to all c (10)", [(0,u) for u in range(6,11)] + [(1,u) for u in range(6,11)])
run("H3 remove c0,c1 all cross (12)", [(u, v) for u in range(6) for v in (6,7)])
run("H4 remove c0 all + hub (10)", [(u,6) for u in range(6)] + [(0,v) for v in range(7,11)])
run("H5 remove 3 rim to all c (15)", [(v,u) for v in (1,2,3) for u in range(6,11)])
