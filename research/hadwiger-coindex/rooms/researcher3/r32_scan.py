import sys, io, contextlib, pickle, time
sys.path.insert(0,'.')
from collections import Counter
with contextlib.redirect_stdout(io.StringIO()):
    from r17_quot import quotient_betti
from r23_ziglib import zig_le
cands = pickle.load(open("r23_cands.pkl","rb"))
t=time.time(); cnt=Counter(); hits=[]
for c in cands:
    z3 = zig_le(9, c[4], 3)
    if z3: cnt["zig<=3"]+=1; continue
    q = quotient_betti(9, c[4])
    key = ("zig>=4", "H3=0" if q.get(3,0)==0 else "H3!=0")
    cnt[key]+=1
    if q.get(3,0)==0: hits.append(c)
    else: hits.append(c) if len(hits)<0 else None
print(cnt, round(time.time()-t,1), flush=True)
pickle.dump(hits, open("r32_hits.pkl","wb"))
print("zig>=4 & H3=0 count:", len(hits), flush=True)
