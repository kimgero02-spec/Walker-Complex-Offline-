# R08 researcher1: K4 as a 2-ring (digon) of single-vertex junctions a,b.
# P1 = K4 - ab (terminals a,b nonadjacent, private c,d), P2 = edge ab (terminals b,a).
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r08_ring import ring_trace
K4mab = ((0, 2, 3, 1), [(0, 2), (0, 3), (1, 2), (1, 3), (2, 3)], (0,), (1,))  # a=0,b=1,c=2,d=3
K2 = ((0, 1), [(0, 1)], (1,), (0,))
ring = [K4mab, K2]
print("digon K4 traces q=1..5:", [ring_trace(ring, q) for q in range(1, 6)])
print("q(q-1)(q-2)(q-3):      ", [q*(q-1)*(q-2)*(q-3) for q in range(1, 6)])
# contraction check: P(K4-ab / ab) = P(K3) = q(q-1)(q-2)
