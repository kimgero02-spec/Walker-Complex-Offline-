import sys, itertools, time
sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r08')
from zig_dfs import feasible
# vertices 0..3 = A (K4), 4..7 = B (K4); cross pairs (a,b)
cross = [(a, b) for a in range(4) for b in range(4, 8)]
def adjmat(F):
    n = 8
    adj = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and ((i < 4) == (j < 4)):
                adj[i][j] = True
    for a, b in F:
        adj[a][b] = adj[b][a] = True
    return adj
def colorable(adj, k):
    n = len(adj)
    col = [-1]*n
    order = list(range(n))
    def ok(v, c):
        return all(not(adj[v][u] and col[u] == c) for u in range(n))
    def bt(i):
        if i == n: return True
        v = order[i]
        used = max(col) if i else -1
        for c in range(min(k, used + 2)):
            if ok(v, c):
                col[v] = c
                if bt(i+1): return True
                col[v] = -1
        return False
    return bt(0)
def chi(F):
    adj = adjmat(F)
    k = 1
    while not colorable(adj, k): k += 1
    return k
if __name__ == "__main__":
    t = time.time()
    res = {}
    for size in range(4, 9):
        found = []
        for F in itertools.combinations(cross, size):
            c = chi(F)
            if c >= 6:
                found.append((F, c))
        print("size", size, "patterns with chi>=6:", len(found), "time", round(time.time()-t,1), flush=True)
        if found:
            print("sample", found[:3], flush=True)
            break
