"""반례 찾기: A 평면인데 B(=A+허용 흰-흰 간선 전부) 비평면인 두 조각 설명서. 작은 무작위 탐색 (반례 구성용)."""
import itertools, random, networkx as nx
exec(open('fr5.py').read().split("# 엇갈림")[0])
random.seed(1)
found = None
for trial in range(40000):
    n1, n2 = random.randint(3, 6), random.randint(3, 6)
    def rp(n):
        while True:
            g = nx.gnp_random_graph(n, random.uniform(0.4, 0.9), seed=random.randint(0, 10**9))
            if nx.is_connected(g) and nx.check_planarity(g)[0]: return list(g.edges)
    E1, E2 = rp(n1), rp(n2)
    k = random.randint(2, min(n1, n2))
    S1 = random.sample(range(n1), k); S2 = random.sample(range(n2), k)
    cl = [[(1, a), (2, b)] for a, b in zip(S1, S2)]
    A = build({1: E1, 2: E2}, cl)
    try: recover(A)
    except AssertionError: continue
    B = add_ww(A)
    if B.number_of_edges() > A.number_of_edges() and nx.check_planarity(A)[0] and not nx.check_planarity(B)[0]:
        found = (E1, E2, cl); break
print('found:', found)
if found:
    E1, E2, cl = found; A = build({1: E1, 2: E2}, cl); report('counterexample', A)
    G = nx.Graph(recover(A)[0]); print('G nodes', G.number_of_nodes(), 'edges', sorted(G.edges), 'conn', nx.node_connectivity(G))
