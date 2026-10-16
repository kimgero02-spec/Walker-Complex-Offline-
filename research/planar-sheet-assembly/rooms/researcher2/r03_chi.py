# R03 researcher2: 색칠수 반례·확인 (작은 그래프만, 정확 계산)
import itertools, networkx as nx

def chi(G):
    nodes = sorted(G.nodes(), key=lambda v: -G.degree(v))
    for k in range(1, len(nodes) + 1):
        col = {}
        def bt(i):
            if i == len(nodes):
                return True
            v = nodes[i]
            used = {col[u] for u in G[v] if u in col}
            mx = max(col.values(), default=-1)
            for c in range(min(k, mx + 2)):  # 대칭 깨기
                if c not in used:
                    col[v] = c
                    if bt(i + 1):
                        return True
                    del col[v]
            return False
        if bt(0):
            return k
    return 0

def tw(G):
    # 정확 treewidth: 작은 그래프에서 제거 순서 DP (부분집합)
    from functools import lru_cache
    V = list(G.nodes()); n = len(V); idx = {v: i for i, v in enumerate(V)}
    adj = [0]*n
    for u, v in G.edges():
        adj[idx[u]] |= 1 << idx[v]; adj[idx[v]] |= 1 << idx[u]
    def q(S, v):  # S 를 제거한 뒤 v 의 이웃 수 (S 를 통한 도달)
        seen = 1 << v; stack = [v]; cnt = 0
        while stack:
            w = stack.pop()
            nb = adj[w] & ~seen
            while nb:
                b = nb & -nb; nb ^= b; seen |= b; j = b.bit_length()-1
                if (S >> j) & 1: stack.append(j)
                else: cnt += 1
        return cnt
    @lru_cache(None)
    def TW(S):
        if S == 0: return -1
        best = 10**9
        s = S
        while s:
            b = s & -s; s ^= b; v = b.bit_length()-1
            best = min(best, max(TW(S ^ b), q(S ^ b, v)))
        return best
    return TW((1 << n) - 1)

def union(*Ps):
    G = nx.Graph()
    for P in Ps: G.add_nodes_from(P.nodes()); G.add_edges_from(P.edges())
    return G

def rep(name, pieces, G):
    cs = [chi(P) for P in pieces]
    pl = [nx.check_planarity(P)[0] for P in pieces]
    print(f"{name}: 조각 chi={cs} 평면={pl} | G: n={G.number_of_nodes()} m={G.number_of_edges()} chi={chi(G)} tw={tw(G) if G.number_of_nodes()<=16 else '-'}")

K = nx.complete_graph
def g(edges, nodes=()):
    G = nx.Graph(); G.add_nodes_from(nodes); G.add_edges_from(edges); return G

# E1: 1-합(정점 공유)인데 H 에 사이클: K2 세 개 -> K3
P = [g([(0,1)]), g([(1,2)]), g([(2,0)])]
rep("E1 삼각형=K2x3 (H=C3, 1-합)", P, union(*P))
P = [g([e]) for e in itertools.combinations(range(5), 2)]
rep("E1' K5=K2x10 (H=선그래프, 1-합)", P, union(*P))

# E2: H 가 별(나무), 2-합인데 간선이 잎 조각에만: K_{2,n} + 삼각형(i,j,w_ij)
for n in (4, 5):
    base = nx.complete_bipartite_graph(2, n)  # 0,1 | 2..n+1
    S = list(range(2, n+2))
    leaves = [g([(i, j), (i, ('w', i, j)), (j, ('w', i, j))]) for i, j in itertools.combinations(S, 2)]
    rep(f"E2 K_(2,{n})+삼각형 잎 (비정규화)", [base]+leaves, union(base, *leaves))
    basen = base.copy(); basen.add_edges_from(itertools.combinations(S, 2))
    print("   정규화한 중심 조각 chi =", chi(basen))

# E3: 간선 공유 2-합 (간선 유지) vs 간선 삭제 2-합
A = K(4); B = nx.relabel_nodes(K(4), {0:0, 1:1, 2:'c', 3:'d'})
rep("E3a K4 (+)_uv K4, uv 유지", [A, B], union(A, B))
Gd = union(A, B); Gd.remove_edge(0, 1)
print("E3b 같은 것에서 uv 삭제(행렬식 2-합): chi =", chi(Gd))

# E4: 간선 아닌 2-합에서 +1 (u,v 는 G 에서 비인접)
# 3색: A=K4-uv (u=v 강제), B=(K4-wv)+uw (u!=v 강제)
A = g([('u','a'),('u','b'),('v','a'),('v','b'),('a','b')])
B = g([('w','p'),('w','q'),('v','p'),('v','q'),('p','q'),('u','w')])
G = union(A, B); assert not G.has_edge('u','v')
rep("E4a 3색판 (K4-uv) + 다름장치", [A, B], G)
# 4색, 평면: K5-ce 는 c=e 강제 (적층 삼각분할)
A = nx.relabel_nodes(K(5), dict(zip(range(5), 'abcde'))); A.remove_edge('c','e')
B = nx.relabel_nodes(K(5), {0:'a2',1:'b2',2:'c',3:'d2',4:'e2'}); B.remove_edge('c','e2'); B.add_edge('e2','e')
G = union(A, B); assert not G.has_edge('c','e')
rep("E4b 4색 평면판 (K5-ce) + 다름장치", [A, B], G)

# E5: 클릭 합 보존
A = K(4); B = nx.relabel_nodes(K(4), {0:0,1:1,2:2,3:'x'})
rep("E5 K4 (+)_삼각형 K4 = K5-e", [A, B], union(A, B))

# E6: 정규화된 3-합 나무에서 +2  (핵심 반례)
Q = g([('a','b'),('b','c'),('c','a'),
       ('x','b'),('x','c'),('y','a'),('y','c'),('z','a'),('z','b'),
       ('p','a'),('p','b'),('p','x'),('p','y'),
       ('q','a'),('q','c'),('q','x'),('q','z'),
       ('r','b'),('r','c'),('r','y'),('r','z')])
def K113(T, tag):
    h1, h2 = (tag, 1), (tag, 2)
    return g([(h1, h2)] + [(h, t) for h in (h1, h2) for t in T])
K1 = K113(('x','y','z'), 'h'); K2_ = K113(('p','q','r'), 'k')
G6 = union(Q, K1, K2_)
for T in (('x','y','z'), ('p','q','r')):
    assert not any(G6.has_edge(s, t) for s, t in itertools.combinations(T, 2))
rep("E6 K113(xyz) - Q - K113(pqr), 3-합 나무, 접합 삼중쌍 G 에서 독립", [K1, Q, K2_], G6)

# Q 의 함의 확인: 4-색칠에서 T1 비무지개 => T2 무지개 (Q 하나의 4-색칠 전부; 9점이라 작음)
def colorings(Gr, k):
    V = list(Gr.nodes()); col = {}
    def bt(i):
        if i == len(V):
            yield dict(col); return
        v = V[i]
        for c in range(k):
            if all(col.get(u) != c for u in Gr[v]):
                col[v] = c; yield from bt(i+1); del col[v]
    yield from bt(0)
bad = 0; tot = 0; pats = set()
for c in colorings(Q, 4):
    tot += 1
    r1 = len({c['x'], c['y'], c['z']}) == 3; r2 = len({c['p'], c['q'], c['r']}) == 3
    if not r1 and not r2: bad += 1
print(f"   Q 의 4-색칠 {tot}개 중 (T1 비무지개 & T2 비무지개) = {bad}  (증명의 단계 확인용)")

# 단일 접합 정규화판: 같은 조각들을 한 삼중쌍에 붙이면 +1 이하
G7 = union(Q, K113(('x','y','z'), 'h'), K113(('x','y','z'), 'k'))
rep("E7 Q + K113(xyz) 둘 (같은 접합 xyz 하나)", [Q, K113(('x','y','z'),'h')], G7)

# (4) K4-uv 와 H 데이터 바꾸기
A = g([('u','a'),('u','b'),('v','a'),('v','b'),('a','b')])
cases = {
  "B=K2(uv), uv 는 B 에서만 간선": g([('u','v')]),
  "uv 가 A,B 모두에서 간선 (A 정규화=K4), B=K2": None,
  "B=경로 u-w-v, uv 비간선": g([('u','w'),('w','v')]),
  "B=K4-uv 사본, uv 비간선": g([('u','c'),('u','d'),('v','c'),('v','d'),('c','d')]),
  "B=다름장치 (K4-wv)+uw, uv 비간선": g([('w','p'),('w','q'),('v','p'),('v','q'),('p','q'),('u','w')]),
  "B=K4 (u,v,c,d), uv 간선 공유 후 삭제": g(list(itertools.combinations(['u','v','c','d'],2))),
}
for name, Bc in cases.items():
    if Bc is None:
        An = A.copy(); An.add_edge('u','v'); Gc = union(An, g([('u','v')])); ps = [An, g([('u','v')])]
    else:
        Gc = union(A, Bc); ps = [A, Bc]
        if "삭제" in name: Gc.remove_edge('u','v')
    rep("(4) "+name, ps, Gc)
# u 와 v 를 한 점으로 식별 (H 레이블이 '같은 점')
Gm = nx.contracted_nodes(A, 'u', 'v', self_loops=False)
print("(4) u=v 식별(A/uv): chi =", chi(nx.Graph(Gm)))

# treewidth 와 chi
for name, Gt in [("K4", K(4)), ("K4-uv", A), ("C5", nx.cycle_graph(5)), ("Q", Q), ("E6 G", G6),
                 ("격자3x3", nx.grid_2d_graph(3,3)), ("피터슨", nx.petersen_graph())]:
    print(f"tw/chi {name}: tw={tw(Gt)} chi={chi(Gt)}  chi<=tw+1: {chi(Gt) <= tw(Gt)+1}")
