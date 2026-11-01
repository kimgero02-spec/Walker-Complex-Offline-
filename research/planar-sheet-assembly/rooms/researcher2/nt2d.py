# q=5: 평면 조각 W5 (바퀴) 의 프로필은 간선 비트 P[J]=C5 로 정해지지 않는다; 평면 가제트(오각별)가 구별
import networkx as nx, sys, io
_o = sys.stdout; sys.stdout = io.StringIO()
from nt2 import profile, partitions, chi, glue, piece
sys.stdout = _o
rim = [(i, (i+1) % 5) for i in range(5)]
W5 = piece(1, rim + [('h', i) for i in range(5)]); C5 = piece(1, rim)
star = piece(2, [(i, (i+2) % 5) for i in range(5)])
EJ = [((1, i), (2, i)) for i in range(5)]
J = [(1, i) for i in range(5)]
disc = frozenset(frozenset([x]) for x in J)
for nm, P in (("W5", W5), ("C5", C5)):
    pr = profile(P, J, 5)
    Gam, G = glue([P, star], EJ)
    print(nm, "planar", nx.check_planarity(P)[0], "|Pi5|", len(pr), "discrete in Pi5", disc in pr,
          "| u pentagram: chi(G)", chi(G), "pentagram planar", nx.check_planarity(star)[0])
