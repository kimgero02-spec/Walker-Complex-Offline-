import sys, io, contextlib
sys.path.insert(0, ".")
with contextlib.redirect_stdout(io.StringIO()):
    from r17_quot import quotient_betti
    from r06_lib import make, B0_empty, reduced_betti
E = [(i,(i+1)%5) for i in range(5)] + [(i,5) for i in range(5)]
n = 6
print("W5 quotient F2 betti:", quotient_betti(n, E))
print("W5 B0 reduced betti:", {k:v for k,v in reduced_betti(B0_empty(make(n,E),n)).items() if v})
