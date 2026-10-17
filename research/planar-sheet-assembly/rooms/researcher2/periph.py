# researcher3 주장 C 공격: 비자명 홀로노미 + 평면 G 에서 조각이 주변 사이클인지, G 의 연결도
import networkx as nx
from band2 import band_faces, check
def peripheral(G, F):
    S = set(F)
    induced = G.subgraph(S).number_of_edges() == len(F)
    R = G.copy(); R.remove_nodes_from(S)
    return induced and (R.number_of_nodes() == 0 or nx.is_connected(R))
for name, ts, ss in [("iii-twist k4", [0,1,0,1], [1,1,1,1]), ("2fan m5", [0]*5+[1]*5+[2], [1]*5+[0]*5+[2]),
                     ("pinch k3", [1,1,0],[1,1,1])]:
    F = band_faces(ts, ss, True); ok, G, cyc = check(F)
    print(name, "가향", ok, "평면", nx.check_planarity(G)[0], "연결도", nx.node_connectivity(G),
          "주변", [peripheral(G, f) for f in F], "면", F)
