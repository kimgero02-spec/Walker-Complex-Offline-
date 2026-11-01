import sys, io, contextlib
sys.path.insert(0, ".")
with contextlib.redirect_stdout(io.StringIO()):
    from r17_quot import quotient_betti
    from r08_checks import graph
for name in ["C5", "K33"]:
    n, E = graph(name)
    print(name, quotient_betti(n, E))
