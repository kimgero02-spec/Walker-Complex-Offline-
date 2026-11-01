import sys
sys.path.insert(0,'.')
from r06_lib import make, max_bicliques
def zig_le(n, E, k):
    adj = make(n, E)
    MB = max_bicliques(adj, n)
    # each biclique: (X,Y) bitmasks; state: last label per biclique (-1 none), runs count
    m = len(MB)
    seen = set()
    def rec(placed, last, runs):
        if placed == (1<<n)-1: return True
        key = (placed, tuple(last), tuple(runs))
        if key in seen: return False
        seen.add(key)
        for v in range(n):
            if placed>>v &1: continue
            ok = True
            nl = list(last); nr = list(runs)
            for i,(X,Y) in enumerate(MB):
                if X>>v&1: lab=0
                elif Y>>v&1: lab=1
                else: continue
                if nl[i]==-1: nr[i]=1
                elif nl[i]!=lab: nr[i]+=1
                nl[i]=lab
                if nr[i]>k: ok=False; break
            if ok and rec(placed|(1<<v), nl, nr): return True
        return False
    return rec(0, [-1]*m, [0]*m)
