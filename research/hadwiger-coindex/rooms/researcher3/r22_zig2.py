import sys, io, contextlib, itertools, time
sys.path.insert(0, ".")
with contextlib.redirect_stdout(io.StringIO()):
    from r22_ext import omega, chi_ge4, moser, c72, quotient_betti
from r06_lib import make, zig
ext_moser = [(0,1),(0,2),(1,2),(1,3),(2,3),(0,4),(0,5),(4,5),(4,6),(5,6),(3,6)]
t=time.time()
res={}
for name,base in [("moser",moser),("C7sq",c72)]:
    n=7
    for r in range(0,n+1):
        for N in itertools.combinations(range(n),r):
            E2=base+[(v,n) for v in N]
            if omega(n+1,E2)>3 or not chi_ge4(n+1,E2): continue
            if quotient_betti(n+1,E2).get(3,0)!=0: continue
            z=zig(make(n+1,E2),n+1)
            res.setdefault(z,[]).append((name,N))
            print(name,N,"zig",z, round(time.time()-t,1), flush=True)
print({k:len(v) for k,v in res.items()})
