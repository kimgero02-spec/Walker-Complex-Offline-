# F-R3: 바퀴 조각 리본 설명서, H = K5. 명제 M-e 의 가지 집합을 직접 만들어 확인
import networkx as nx, itertools, random
n = 5; m = 8
pairs = list(itertools.combinations(range(n), 2))
slot = {k: 0 for k in range(n)}; G = nx.Graph(); rep = {}
def v(k, i): return (k, i)
for k in range(n):
    for i in range(m):
        G.add_edge(v(k, i), v(k, (i+1) % m)); G.add_edge(v(k, 'c'), v(k, i))
arcs = []
for (k, l) in pairs:
    a = slot[k]; b = slot[l]; slot[k] += 2; slot[l] += 2
    twist = (k + l) % 2  # 부호는 아무렇게나
    ka = [v(k, a), v(k, a+1)]; la = [v(l, b+1), v(l, b)] if not twist else [v(l, b), v(l, b+1)]
    arcs.append((k, l, ka, la))
uf = {}
def find(x):
    while uf.get(x, x) != x: x = uf[x]
    return x
for k, l, ka, la in arcs:
    for x, y in zip(ka, la): uf[find(y)] = find(x)
Q = nx.Graph()
for a, b in G.edges(): Q.add_edge(find(a), find(b))
print("V,E =", Q.number_of_nodes(), Q.number_of_edges(), "planar:", nx.check_planarity(Q)[0])
# sigma: 호 (k,l) 의 정점은 k 에 배정
B = {k: set() for k in range(n)}
for k in range(n):
    for i in list(range(m)) + ['c']: B[k].add(find(v(k, i)))
assigned = {}
for k, l, ka, la in arcs:
    for x in ka: assigned[find(x)] = k
for k in range(n):
    B[k] = {x for x in B[k] if assigned.get(x, k) == k}
ok = all(nx.is_connected(Q.subgraph(B[k])) for k in range(n))
disj = all(not (B[a] & B[b]) for a, b in pairs)
adj = all(any(Q.has_edge(x, y) for x in B[a] for y in B[b]) for a, b in pairs)
print("가지 집합 연결:", ok, "서로소:", disj, "모든 쌍 인접:", adj, "=> K5 마이너 모델")
