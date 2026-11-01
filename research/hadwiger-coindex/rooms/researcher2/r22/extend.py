import pickle, sys, time
sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r08')
from zig_dfs import feasible
cands = pickle.load(open('/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r21/cands7.pkl','rb'))
def colorable(adj, k):
    n = len(adj); col = [-1]*n
    def bt(i):
        if i == n: return True
        for c in range(k):
            if all(not(adj[i][j] and col[j]==c) for j in range(i)):
                col[i]=c
                if bt(i+1): return True
                col[i]=-1
        return False
    return bt(0)
t = time.time()
found = []
stats = {'chi4_zig3':0, 'chi4':0, 'zig3_chi5plus':0}
for ci, E in enumerate(cands):
    base = [[False]*7 for _ in range(7)]
    for u, v in E: base[u][v]=base[v][u]=True
    for mask in range(1 << 7):
        adj = [[False]*8 for _ in range(8)]
        for i in range(7):
            for j in range(7):
                adj[i][j] = base[i][j]
        for i in range(7):
            if mask >> i & 1:
                adj[i][7] = adj[7][i] = True
        if colorable(adj, 3): continue          # chi >= 4 required
        if not colorable(adj, 4): continue      # want chi == 4 exactly
        stats['chi4'] += 1
        if feasible(8, adj, 3)[0]:
            stats['chi4_zig3'] += 1
            found.append((ci, mask))
print("stats", stats, "time", round(time.time()-t,1), flush=True)
print("found (cand index, neighbourhood mask of new vertex 7):", found[:20])
