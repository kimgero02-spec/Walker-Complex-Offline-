import sys, itertools
sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r19')
sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r08')
from k4k4 import cross, chi, adjmat
from zig_dfs import feasible
def has_clique(adj, k):
    n = len(adj)
    for S in itertools.combinations(range(n), k):
        if all(adj[u][v] for u, v in itertools.combinations(S, 2)):
            return True
    return False
pats = []
for F in itertools.combinations(cross, 8):
    if chi(F) >= 6:
        pats.append(F)
print("count", len(pats))
for F in pats:
    adj = adjmat(F)
    k6 = has_clique(adj, 6)
    # zig <= 5 test (tau <= zig)
    z5 = feasible(8, adj, 5)[0]
    z4 = feasible(8, adj, 4)[0] if not k6 else None
    print(sorted(F), "chi>=6", "K6" if k6 else "noK6", "zig<=5:", z5, "zig<=4:", z4, flush=True)
