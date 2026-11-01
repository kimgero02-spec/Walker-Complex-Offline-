import sys, io, contextlib, time, pickle
sys.path.insert(0, ".")
with contextlib.redirect_stdout(io.StringIO()):
    from r17_quot import quotient_betti
cands = pickle.load(open("r23_cands.pkl","rb"))
t=time.time()
for c in cands[:3]:
    q = quotient_betti(9, c[4]); print(c[:4], q, round(time.time()-t,2), flush=True)
