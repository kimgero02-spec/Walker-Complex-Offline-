# R23 researcher3: H^3(Q)=0 filter over all 2-vertex extensions, then zig<=3 via backtracking with run pruning.
import sys, io, contextlib, pickle, time, itertools
sys.path.insert(0, ".")
with contextlib.redirect_stdout(io.StringIO()):
    from r17_quot import quotient_betti
    from r06_lib import make, max_bicliques
cands = pickle.load(open("r23_cands.pkl","rb"))
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
t=time.time()
h0=[]
for c in cands:
    q = quotient_betti(9, c[4])
    if q.get(3,0)==0: h0.append(c)
print("H3(Q)=0 candidates:", len(h0), round(time.time()-t,1), flush=True)
pickle.dump(h0, open("r23_h0.pkl","wb"))
from collections import Counter
res=Counter(); bad=[]
for c in h0:
    z3 = zig_le(9, c[4], 3)
    res[z3]+=1
    if not z3: bad.append(c)
print("zig<=3 counts:", res, round(time.time()-t,1), flush=True)
print("zig>3 candidates (potential tau=4):", len(bad))
for c in bad[:20]: print(c[:4], flush=True)
pickle.dump(bad, open("r23_bad.pkl","wb"))
