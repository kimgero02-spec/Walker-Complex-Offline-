import sys, io, contextlib
sys.path.insert(0, ".")
with contextlib.redirect_stdout(io.StringIO()):
    from r17_quot import quotient_betti
    from r06_lib import make, B0_empty, reduced_betti
# Mycielski of C5 = Grotzsch: v0..v4 (0..4), u0..u4 (5..9), w (10)
E = [(i,(i+1)%5) for i in range(5)]
for i in range(5):
    E.append((5+i,(i-1)%5)); E.append((5+i,(i+1)%5)); E.append((5+i,10))
n = 11
print("quotient F2 betti (unreduced, dims):", quotient_betti(n, E))
print("B0 reduced betti:", {k:v for k,v in reduced_betti(B0_empty(make(n,E),n)).items() if v})
