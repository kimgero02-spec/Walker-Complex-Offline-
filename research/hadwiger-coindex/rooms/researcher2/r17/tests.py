import sys
sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r17')
from k7minor import base_edges, cross_pairs, has_K_minor
import time
full = set(cross_pairs())
def run(name, removed):
    E = base_edges() | (full - set(removed))
    t = time.time()
    r = has_K_minor(E, 7)
    print(f"{name}: removed={len(removed)} K7={r} ({round(time.time()-t,1)}s)", flush=True)
run("A one edge", [(1, 6)])
run("B all cross at c0", [(u, 6) for u in range(6)])
run("C all cross at hub", [(0, v) for v in range(6, 11)])
run("D perfect matching", [(i + 1, 6 + i) for i in range(5)])
run("E rim r1 to all c", [(1, v) for v in range(6, 11)])
run("F hub+rim pattern: each c misses one rim", [(1 + i, 6 + i) for i in range(5)] + [(1 + i, 6 + (i+1) % 5) for i in range(5)])
