# researcher1 추측 10 공격: H 단순, 조각 '강체'(내부면마다 호 ≤1), 리본 곡면 = 구멍 하나 토러스(가향, 종수1), 그런데 G 평면?
import itertools as it, networkx as nx
from band2 import check
oct_ = [f'v{i}' for i in range(8)]
P0_faces = [('v0', f'v{i}', f'v{i+1}') for i in range(1, 7)]  # 부채 삼각분할 (v0 중심)
def band(name, e_start, e_end, cross):
    # 도미노 2개 = 사각형 4개, 가로대 e_start -> 중간 -> e_end. cross: 레일 연결 방식
    (a0, b0) = e_start; (a4, b4) = e_end
    if cross: a4, b4 = b4, a4
    A = [a0] + [f'{name}a{j}' for j in range(1, 4)] + [a4]
    B = [b0] + [f'{name}b{j}' for j in range(1, 4)] + [b4]
    return [(A[j], A[j+1], B[j+1], B[j]) for j in range(4)]
res = {}
for c1, c2 in it.product([False, True], repeat=2):
    faces = P0_faces + band('p', ('v0','v1'), ('v4','v5'), c1) + band('q', ('v2','v3'), ('v6','v7'), c2)
    ok, G, cyc = check(faces)
    V, E, F = G.number_of_nodes(), G.number_of_edges(), len(faces)
    print("cross", c1, c2, "가향", ok, "χ", V - E + F, "G 평면", nx.check_planarity(G)[0])
