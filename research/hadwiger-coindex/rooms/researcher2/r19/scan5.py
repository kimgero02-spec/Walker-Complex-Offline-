import sys, itertools, time
sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r19')
sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r08')
from k4k4 import cross, chi, adjmat
from zig_dfs import feasible
def omega(adj):
    n = len(adj); best = 1
    for k in range(2, n+1):
        if any(all(adj[u][v] for u, v in itertools.combinations(S, 2)) for S in itertools.combinations(range(n), k)):
            best = k
        else:
            break
    return best
t = time.time()
out = []
m = len(cross)
stats = {}
for mask in range(1 << m):
    F = [cross[i] for i in range(m) if mask >> i & 1]
    adj = adjmat(F)
    c = chi(F)
    if c < 5: continue
    w = omega(adj)
    stats[(c, w)] = stats.get((c, w), 0) + 1
    if w < c:
        z = None
        # tau <= zig; check zig <= c-1
        ok = feasible(8, adj, c-1)[0]
        out.append((c, w, ok, F))
print("stats (chi, omega): count", stats, "time", round(time.time()-t,1), flush=True)
print("omega<chi cases:", len(out))
print("with zig<chi (tau<chi certified):", sum(1 for o in out if o[2]))
for o in out:
    if o[2]:
        print("CERT", o[0], o[1], sorted(o[3]), flush=True)
