"""s*=m=3 인 예 찾기: Q_pi 가제트(삼각형 z0z1z2, 포트 i 는 블록 b 이면 z_j (j!=b) 에 연결) 세 장을
류 크기 3 으로 붙인다. 라벨 삼중쌍 집합 T 가 '모든 sigma2,sigma3 에서 어떤 삼중쌍이 무지개' 이면 s*>=3."""
import itertools, networkx as nx
exec(open('fr2.py').read().split("def sq(c)")[0])
S3 = list(itertools.permutations(range(3)))
trip = list(itertools.product(range(3), repeat=3))
def good(T):
    return all(any(len({a, s2[b], s3[c]}) == 3 for a, b, c in T) for s2 in S3 for s3 in S3)
best = None
for r in range(1, 8):
    for T in itertools.combinations(trip, r):
        if good(T): best = T; break
    if best: break
print('minimal |T| =', len(best), best, flush=True)
def gadget(labels):
    E = [('z0','z1'),('z1','z2'),('z0','z2')]
    for i, b in enumerate(labels):
        for j in range(3):
            if j != b: E.append((('x', i), 'z%d' % j))
    return E
T = best
P = {k: gadget([t[k] for t in T]) for k in range(3)}
for k in P: print('piece', k, 'planar:', nx.check_planarity(nx.Graph(P[k]))[0])
cl = [[(k, ('x', i)) for k in range(3)] for i in range(len(T))]
A = build(P, cl)
info('gadget3', A, 5)
