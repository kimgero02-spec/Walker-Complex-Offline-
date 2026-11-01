import sys
sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r08')
from zig_dfs import feasible, zig_value
# Grotzsch = Mycielski(C5): v0..v4 (0..4), u0..u4 (5..9), w (10)
E = [(i, (i+1) % 5) for i in range(5)]
for i in range(5):
    for j in ((i-1) % 5, (i+1) % 5):
        E.append((5+i, j))
for i in range(5):
    E.append((5+i, 10))
n = 11
adj = [[False]*n for _ in range(n)]
for a, b in E:
    adj[a][b] = adj[b][a] = True
print("edges", len(E), "triangle-free check:", all(not(adj[a][b] and adj[b][c] and adj[a][c]) for a in range(n) for b in range(n) for c in range(n)))
print("zig<=4:", feasible(n, adj, 4)[0])
import time
t = time.time()
ok, order = feasible(n, adj, 3)
print("zig<=3:", ok, order, "time", round(time.time()-t, 1))
