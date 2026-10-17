# cd(H) 계산: Kneser 표현 H (ground = 비인접쌍, e_x = x 를 포함하는 비인접쌍) 에 대해
# cd(H) = min{|U| : U ⊆ ground, 간선 {e: e∩U=∅} 이 ground\U 위에서 2-색칠 가능}
import itertools, sys

def two_colorable(vertices, edges):
    # vertices: list, edges: list of frozensets (⊆ vertices). 색칠 = 모든 간선이 두 색을 모두 포함.
    idx = {v: i for i, v in enumerate(vertices)}
    E = [[idx[v] for v in e] for e in edges]
    if any(len(e) == 0 for e in E):
        return False
    if any(len(e) == 1 for e in E):
        return False
    n = len(vertices)
    col = [-1] * n
    by_v = [[] for _ in range(n)]
    for k, e in enumerate(E):
        for v in e:
            by_v[v].append(k)
    def ok(v):
        for k in by_v[v]:
            cs = [col[u] for u in E[k]]
            if all(c != -1 for c in cs) and len(set(cs)) == 1:
                return False
        return True
    def bt(i):
        if i == n:
            return True
        for c in (0, 1):
            if i == 0 and c == 1:
                break  # 대칭 제거
            col[i] = c
            if ok(i) and bt(i + 1):
                return True
        col[i] = -1
        return False
    return bt(0)

def cd_of(ground, hedges):
    # hedges: dict x -> frozenset (⊆ ground)
    best = None
    for k in range(0, len(ground) + 1):
        for U in itertools.combinations(ground, k):
            Us = set(U)
            rest = [v for v in ground if v not in Us]
            E = [e for e in hedges.values() if not (e & Us)]
            if not two_colorable(rest, E):
                continue
            return k, U
    return None

def kneser_rep(n, adj):
    nonedges = [frozenset((a, b)) for a in range(n) for b in range(a + 1, n) if b not in adj[a]]
    priv = [('p', x) for x in range(n)]  # 사적 원소: 인접 관계를 바꾸지 않고 빈 초변을 막는다
    ground = nonedges + priv
    hedges = {x: frozenset([p for p in nonedges if x in p] + [('p', x)]) for x in range(n)}
    return ground, hedges

def check_rep(n, adj, hedges):
    for x in range(n):
        for y in range(x + 1, n):
            disj = not (hedges[x] & hedges[y])
            assert disj == (y in adj[x]), (x, y)
    return True

def cycle(n):
    return [set([(i - 1) % n, (i + 1) % n]) for i in range(n)]

def lex(n, adjsets):
    return adjsets

def graph_from_edges(n, E):
    adj = [set() for _ in range(n)]
    for a, b in E:
        adj[a].add(b); adj[b].add(a)
    return adj

def complement(adj):
    n = len(adj)
    return [set(range(n)) - adj[v] - {v} for v in range(n)]

def lexicographic(G, k):
    # G[K_k]: 각 정점을 K_k 로 치환
    n = len(G)
    adj = [set() for _ in range(n * k)]
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            if b in G[a]:
                for i in range(k):
                    for j in range(k):
                        adj[a * k + i].add(b * k + j)
    for a in range(n):
        for i in range(k):
            for j in range(k):
                if i != j:
                    adj[a * k + i].add(a * k + j)
    return adj

if __name__ == '__main__':
    tests = []
    for n in (3, 4):
        tests.append(('K%d' % n, [set(range(n)) - {v} for v in range(n)]))
    tests.append(('C5', cycle(5)))
    tests.append(('C7', cycle(7)))
    tests.append(('comp(C7)', complement(cycle(7))))
    tests.append(('C5[K2]', lexicographic(cycle(5), 2)))
    for name, adj in tests:
        n = len(adj)
        ground, hedges = kneser_rep(n, adj)
        check_rep(n, adj, hedges)
        res = cd_of(ground, hedges)
        print(name, 'n=', n, '|ground|=', len(ground), 'cd(H_nonedge)=', res[0], 'U=', res[1], flush=True)
