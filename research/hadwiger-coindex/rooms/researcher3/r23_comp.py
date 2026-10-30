import sys, io, contextlib, itertools
sys.path.insert(0, ".")
with contextlib.redirect_stdout(io.StringIO()):
    from r22_ext import omega, chi_ge4
    from r17_quot import quotient_betti
from r23_ziglib import zig_le
C7=set(frozenset((i,(i+1)%7)) for i in range(7))
comp7=[(a,b) for a,b in itertools.combinations(range(7),2) if frozenset((a,b)) not in C7]
print("comp C7 edges:", len(comp7), "omega", omega(7,comp7), "chi>=4", chi_ge4(7,comp7))
tot=0; h0=0; z=0; hits=[]
for N1 in range(128):
    for N2 in range(128):
        for e78 in (0,1):
            E=list(comp7)+[(v,7) for v in range(7) if N1>>v&1]+[(v,8) for v in range(7) if N2>>v&1]
            if e78: E.append((7,8))
            if omega(9,E)>3 or not chi_ge4(9,E): continue
            tot+=1
            if quotient_betti(9,E).get(3,0)!=0: continue
            h0+=1
            if not zig_le(9,E,3): hits.append((N1,N2,e78))
print("comp_C7 2-ext: omega<=3 chi>=4:",tot," H3=0:",h0," zig>3 among H3=0:",len(hits), hits[:5])
