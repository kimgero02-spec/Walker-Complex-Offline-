import pickle, sys, itertools
sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r08')
from zig_dfs import feasible
cands = pickle.load(open('/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r21/cands7.pkl','rb'))
def build(ci, mask):
    adj=[[False]*8 for _ in range(8)]
    for u,v in cands[ci]: adj[u][v]=adj[v][u]=True
    for i in range(7):
        if mask>>i&1: adj[i][7]=adj[7][i]=True
    return adj
def colorable(adj,k):
    n=len(adj); col=[-1]*n
    def bt(i):
        if i==n: return True
        for c in range(k):
            if all(not(adj[i][j] and col[j]==c) for j in range(i)):
                col[i]=c
                if bt(i+1): return True
                col[i]=-1
        return False
    return bt(0)
for ci,mask in [(0,1),(4,1),(4,108)]:
    adj=build(ci,mask)
    ok,order=feasible(8,adj,3)
    # unfiltered verification of max runs under the returned order
    pos={v:i for i,v in enumerate(order)}
    worst=0
    n=8
    for la in range(1,1<<n):
        A=[i for i in range(n) if la>>i&1]
        common=[j for j in range(n) if not la>>j&1 and all(adj[a][j] for a in A)]
        for lb in range(1,1<<len(common)):
            B=[common[k] for k in range(len(common)) if lb>>k&1]
            seq=sorted([(pos[v],0) for v in A]+[(pos[v],1) for v in B])
            r=1+sum(seq[k][1]!=seq[k-1][1] for k in range(1,len(seq)))
            worst=max(worst,r)
    chi3=colorable(adj,3); chi4=colorable(adj,4)
    print(f"cand {ci} mask {mask}: order {order} unfiltered max runs {worst}; 3-col {chi3}; 4-col {chi4}; edges {sum(map(sum,adj))//2}")
