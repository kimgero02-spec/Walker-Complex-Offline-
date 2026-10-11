import sys, io, contextlib, itertools
sys.path.insert(0, ".")
with contextlib.redirect_stdout(io.StringIO()):
    from r23_run import zig_le
    from r06_lib import zig, make
from r22_ext import moser, c72
K=lambda n: list(itertools.combinations(range(n),2))
C5=[(i,(i+1)%5) for i in range(5)]
C7=[(i,(i+1)%7) for i in range(7)]
for name,(n,E) in {"K4":(4,K(4)),"K5":(5,K(5)),"C5":(5,C5),"moser":(7,moser),"C7sq":(7,c72)}.items():
    print(name, "zig_le3:", zig_le(n,E,3), "brute zig:", zig(make(n,E),n), flush=True)
