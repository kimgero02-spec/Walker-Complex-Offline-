import sys, itertools, time
sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r19')
blocks = [list(range(0,4)), list(range(4,8)), list(range(8,12))]
n = 12
pairs = [(u, v) for i in range(3) for j in range(i+1,3) for u in blocks[i] for v in blocks[j]]
def build(F):
    adj = [[False]*n for _ in range(n)]
    for B in blocks:
        for u in B:
            for v in B:
                if u != v: adj[u][v] = True
    for u, v in F: adj[u][v] = adj[v][u] = True
    return adj
def colorable(adj, k):
    col = [-1]*n
    order = sorted(range(n), key=lambda v: -sum(adj[v]))
    def bt(i):
        if i == n: return True
        v = order[i]
        for c in range(k):
            if all(not(adj[v][u] and col[u]==c) for u in range(n)):
                col[v]=c
                if bt(i+1): return True
                col[v]=-1
        return False
    return bt(0)
def chi_ge5(F):
    return not colorable(build(F), 4)
t=time.time()
for size in range(0, 5):
    cnt=0; ex=None
    for F in itertools.combinations(pairs, size):
        if chi_ge5(F):
            cnt+=1
            if ex is None: ex=F
    print("size", size, "patterns with chi>=5:", cnt, "example", ex, "time", round(time.time()-t,1), flush=True)
    if cnt: break
# glued: each pair of blocks has >=1 cross edge, size 3
glued=0; tot=0
for F in itertools.product(*[[None]+[p for p in []]] ,) : pass
