import sys
sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r08')
from zig_dfs import feasible, zig_value
n = 7
C7 = {frozenset((i, (i+1) % 7)) for i in range(7)}
adj = [[(i != j and frozenset((i, j)) not in C7) for j in range(n)] for i in range(n)]
print("edges of complement C7:", sum(adj[i][j] for i in range(n) for j in range(i+1, n)))
print("zig(comp C7) <= 3:", feasible(n, adj, 3))
print("zig(comp C7) <= 4:", feasible(n, adj, 4)[0])
