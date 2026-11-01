import sys, itertools
sys.path.insert(0, ".")
from r15_minor import zg, K, subdiv, contract
n, E = 4, K(4)
e1, e2 = (0,1), (2,3)   # opposite edges
n2, E2 = subdiv(n, E, e1); n3, E3 = subdiv(n2, E2, e2)
print("K4 two opposite subdivided: zig", zg(n3, E3))
e1, e2 = (0,1), (0,2)   # adjacent
n2, E2 = subdiv(n, E, e1); n3, E3 = subdiv(n2, E2, e2)
print("K4 two adjacent subdivided: zig", zg(n3, E3))
