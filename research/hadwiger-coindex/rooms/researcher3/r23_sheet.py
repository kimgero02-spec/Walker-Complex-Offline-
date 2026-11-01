import sys, pickle, itertools
sys.path.insert(0,'.')
h0 = pickle.load(open("r23_h0.pkl","rb"))
def has_k5(S, Eset):
    return all(frozenset(p) in Eset for p in itertools.combinations(S,2))
ok=0; tot=0; ex=None
for c in h0:
    E=c[4]; Eset=set(frozenset(e) for e in E)
    tot+=1
    found=False
    for B in itertools.combinations(range(9),5):
        if not has_k5(B,Eset):
            found=True; break
    if found:
        ok+=1
        if ex is None: ex=(c[:4],B)
print("candidates:",tot,"with planar 4+5 vertex split (5-part K5-free):",ok, "example:",ex)
