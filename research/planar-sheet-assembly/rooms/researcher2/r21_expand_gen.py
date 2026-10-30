# R21: 일반화된 조작 T (장마다 표시 쌍 0~2 개, 칸 수 = 2 + 쌍 수). 초과 e = N - sigma 를 보존하는지 검산.
# 시험: K_8 = P ∪ B1 ∪ B2 (sigma=7) 에 표시 쌍 P:(0,2), B1:(1,3) (B1 의 같은 쪽 쌍).
import itertools, networkx as nx
from r19_lib import chi, omega
def step(N, sheets, pairs):
    x, y, z = N, N+1, N+2
    used = [v for ps in pairs for p in ps for v in p]
    free = [v for v in range(N) if v not in used]; fi = 0
    new = [P.copy() for P in sheets]; A, B = [], []
    for j, (P, ps) in enumerate(zip(new, pairs)):
        roles = (z, x) if j % 2 == 0 else (x, z)
        for t, r in enumerate(roles):
            if t < len(ps):
                a, b = ps[t]; P.add_edge(r, a); P.add_edge(r, b); nb = [a, b]
            else:
                l = free[fi]; fi += 1; P.add_edge(r, l); nb = [l]
            (A if r == z else B).extend(nb)
    assert fi == len(free) and sorted(A+B) == list(range(N)) and A and B
    new[0].add_edge(x, y); new[1].add_edge(y, z)
    S = nx.Graph([(x, a) for a in A] + [(y, a) for a in A] + [(y, b) for b in B] + [(z, b) for b in B] + [(x, z)])
    return N+3, new+[S], pairs+[[(x, y)]]
def check(N, sh):
    cnt = {}
    for G in sh:
        for e in G.edges(): cnt[frozenset(e)] = cnt.get(frozenset(e), 0)+1
    ex = set(cnt) == set(frozenset(e) for e in itertools.combinations(range(N), 2)) and all(c == 1 for c in cnt.values())
    ch = [chi(G) for G in sh]; om = [omega(G) for G in sh]
    return dict(N=N, exact=ex, planar=all(nx.check_planarity(G)[0] for G in sh), sigma=sum(ch), e=N-sum(ch),
                Delta=sum(c > o for c, o in zip(ch, om)), chis=ch)
P=nx.Graph([(0,1),(2,3),(4,5),(6,7),(2,4),(2,6),(5,7)])
B1=nx.Graph([(0,4),(0,5),(0,6),(0,7),(1,4),(1,5),(2,7),(3,6),(3,7)])
B2=nx.Graph([(0,2),(0,3),(1,2),(1,3),(1,6),(1,7),(2,5),(3,4),(3,5),(4,6),(4,7),(5,6)])
N, sh, pr = 8, [P, B1, B2], [[(0, 2)], [(1, 3)], []]
print(check(N, sh))
for _ in range(3):
    N, sh, pr = step(N, sh, pr); print(check(N, sh))
