# R23 researcher3: two-vertex extensions (vertices 7,8; edge 7-8 optional) of Moser, C7^2, complement C7.
import sys, io, contextlib, itertools, time, pickle
sys.path.insert(0, ".")
with contextlib.redirect_stdout(io.StringIO()):
    from r22_ext import omega, chi_ge4, moser, c72, quotient_betti
C7=[(i,(i+1)%7) for i in range(7)]
comp7=[(a,b) for a,b in itertools.combinations(range(7),2) if (a,b) not in set(C7)]
bases={"moser":moser,"C7sq":c72,"comp_C7":comp7}
t=time.time()
cands=[]
for name,base in bases.items():
    n=7; cnt=0
    for N1 in range(128):
        for N2 in range(128):
            for e78 in (0,1):
                E=list(base)+[(v,7) for v in range(7) if N1>>v&1]+[(v,8) for v in range(7) if N2>>v&1]
                if e78: E.append((7,8))
                if omega(9,E)>3: continue
                if not chi_ge4(9,E): continue
                cnt+=1
                cands.append((name,N1,N2,e78,E))
    print(name,"omega<=3, chi>=4 count:",cnt, round(time.time()-t,1), flush=True)
pickle.dump(cands, open("/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3/r23_cands.pkl","wb"))
