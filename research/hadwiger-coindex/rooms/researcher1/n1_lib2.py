from n1_lib import *
def chainlen(pairs):
    P=set()
    for a,b in pairs: P.add((a,b)); P.add((b,a))
    P=sorted(P,key=lambda p:bin(p[0]).count('1'))
    best={}
    for p in P:
        best[p]=1+max([best[q] for q in best if q[0]!=p[0] and q[0]&p[0]==q[0]]+[0])
    return max(best.values())
def zigle(n,pairs,k):
    """exists order with every pair runs<=k ?  DFS, appending vertices; monotone."""
    P=[(a,b) for a,b in pairs]
    m=len(P)
    # state: last label (0 none,1 A,2 B), runs
    sys_lim=10**9
    def dfs(placed,last,runs):
        if placed==(1<<n)-1: return True
        seen=set()
        for v in range(n):
            if placed>>v&1: continue
            nl=list(last); nr=list(runs); ok=True
            for i,(a,b) in enumerate(P):
                lab=1 if a>>v&1 else (2 if b>>v&1 else 0)
                if lab and lab!=nl[i]:
                    nr[i]+=1; nl[i]=lab
                    if nr[i]>k: ok=False;break
            if not ok: continue
            key=(placed|1<<v,tuple(nl),tuple(nr))
            if key in memo: continue
            memo.add(key)
            if dfs(placed|1<<v,nl,nr): return True
        return False
    memo=set()
    return dfs(0,[0]*m,[0]*m)
def zig(n,pairs):
    k=1
    while not zigle(n,pairs,k): k+=1
    return k
