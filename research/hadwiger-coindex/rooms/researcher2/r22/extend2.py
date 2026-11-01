import pickle, sys, time, itertools
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
def has_K4(adj):
    n=len(adj)
    return any(all(adj[u][v] for u,v in itertools.combinations(S,2)) for S in itertools.combinations(range(n),4))
t=time.time()
stats={'K4free_chi4':0,'zig3':0}
found=[]
for ci,E in enumerate(cands):
    base=[[False]*8 for _ in range(8)]
    for u,v in E: base[u][v]=base[v][u]=True
    for mask in range(1,1<<7):
        adj=[row[:] for row in base]
        for i in range(7):
            if mask>>i&1: adj[i][7]=adj[7][i]=True
        if has_K4(adj): continue
        if colorable(adj,3) or not colorable(adj,4): continue
        stats['K4free_chi4']+=1
        if feasible(8,adj,3)[0]:
            stats['zig3']+=1; found.append((ci,mask))
    print("cand",ci,"done",stats,round(time.time()-t,1),flush=True)
print("found", found, flush=True)
