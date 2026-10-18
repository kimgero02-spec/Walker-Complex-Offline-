from r04_lib import *
P = nx.cycle_graph(9)
T = [t for t in itertools.combinations(P.nodes(),3) if indep(P,t)]
# 탐욕 축소: 빼도 여전히 4-색칠 불가이면 뺀다
for order in [T, T[::-1]]:
    S = list(order)
    for t in list(S):
        S2 = [u for u in S if u != t]
        if col_ok(P, S2) is None: S = S2
    print(len(S), S)
# 구조적 후보
for name, S in [('i,i+3,i+6', [(0,3,6),(1,4,7),(2,5,8)]),
                ('i,i+2,i+5 all', [tuple(sorted(((i)%9,(i+2)%9,(i+5)%9))) for i in range(9)]),
                ('i,i+2,i+4 all', [tuple(sorted(((i)%9,(i+2)%9,(i+4)%9))) for i in range(9)]),
                ('i,i+3,i+5 all', [tuple(sorted(((i)%9,(i+3)%9,(i+5)%9))) for i in range(9)])]:
    print(name, col_ok(P, S))
