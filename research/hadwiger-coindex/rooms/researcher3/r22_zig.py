import sys, io, contextlib, itertools, time
sys.path.insert(0, ".")
with contextlib.redirect_stdout(io.StringIO()):
    import r22_ext as R
from r06_lib import make, zig
import networkx as nx
