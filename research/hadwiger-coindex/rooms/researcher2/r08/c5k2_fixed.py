import sys
sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r08')
from zig_dfs import feasible
# C5[K2]: lexicographic product, blobs {2i, 2i+1} are EDGES (K2), blobs adjacent in C5 are fully joined.
n = 10
E = set()
for i in range(5):
    E.add(frozenset((2*i, 2*i+1)))           # inner edge of the K2 blob
    j = (i+1) % 5
    for s in range(2):
        for t in range(2):
            E.add(frozenset((2*i+s, 2*j+t)))
print("edges:", len(E))           # expect 5 + 20 = 25
adj = [[frozenset((a, b)) in E for b in range(n)] for a in range(n)]
# identity-order run count over ALL bicliques
best = 0
for la in range(1, 1 << n):
    A = [i for i in range(n) if la >> i & 1]
    common = [j for j in range(n) if not (la >> j) & 1 and all(adj[a][j] for a in A)]
    for lb in range(1, 1 << len(common)):
        B = [common[k] for k in range(len(common)) if lb >> k & 1]
        seq = sorted([(v, 0) for v in A] + [(v, 1) for v in B])
        runs = 1 + sum(seq[k][1] != seq[k-1][1] for k in range(1, len(seq)))
        best = max(best, runs)
print("identity order: max runs over all bicliques =", best)
for r in (3, 4):
    ok, order = feasible(n, adj, r)
    print("zig <=", r, ":", ok, order)
