"""망상꾼 R01: 순환 조각(cycle pieces)의 방향 홀로노미, 주변 사이클 판정, 몫 조립, 방향 이중피복."""
import itertools, networkx as nx

def cyc_edges(c):
    return [(c[i], c[(i+1) % len(c)]) for i in range(len(c))]

def is_peripheral(G, c):
    """Tutte 주변 사이클: 유도(현 없음) + 제거 후 연결."""
    S = set(c)
    induced = G.subgraph(S).number_of_edges() == len(c)
    R = G.copy(); R.remove_nodes_from(S)
    return induced and (R.number_of_nodes() == 0 or nx.is_connected(R))

def overlap_graph(pieces):
    """H: 조각=점, 공유 변마다 변(멀티그래프). 레이블: 두 방향 사이클이 공유 변을
    반대 방향으로 지나면 +1(정합), 같은 방향이면 -1."""
    H = nx.MultiGraph(); H.add_nodes_from(range(len(pieces)))
    dir_ = [dict() for _ in pieces]
    for i, c in enumerate(pieces):
        for (a, b) in cyc_edges(c):
            dir_[i][frozenset((a, b))] = (a, b)
    mult = {}
    for i, j in itertools.combinations(range(len(pieces)), 2):
        for e in set(dir_[i]) & set(dir_[j]):
            lab = +1 if dir_[i][e] != dir_[j][e] else -1
            H.add_edge(i, j, e=tuple(sorted(e)), lab=lab)
    for i in range(len(pieces)):
        for e in dir_[i]:
            mult[e] = mult.get(e, 0) + 1
    return H, mult

def holonomy_trivial(H):
    """Z2 코사이클이 쌍대경계(coboundary)인지: 점에 부호 s 를 주어 lab = s_i s_j 가 되나."""
    s = {}
    for comp in nx.connected_components(H):
        r = next(iter(comp)); s[r] = 1; stack = [r]
        while stack:
            u = stack.pop()
            for _, v, d in H.edges(u, data=True):
                want = s[u] * d['lab']
                if v not in s:
                    s[v] = want; stack.append(v)
                elif s[v] != want:
                    return False
    return True

def assemble(pieces, H):
    """몫(colimit): 각 조각의 정점 복제 (i,v); H 의 공유 변 e=(a,b) 를 따라 (i,a)~(j,a),(i,b)~(j,b)."""
    uf = {}
    def f(x):
        uf.setdefault(x, x)
        while uf[x] != x:
            uf[x] = uf[uf[x]]; x = uf[x]
        return x
    for i, c in enumerate(pieces):
        for v in c: f((i, v))
    for i, j, d in H.edges(data=True):
        for v in d['e']:
            uf[f((i, v))] = f((j, v))
    A = nx.Graph()
    for i, c in enumerate(pieces):
        for (a, b) in cyc_edges(c):
            A.add_edge(f((i, a)), f((i, b)))
    return A

def orientation_double_cover(pieces, H):
    """조각을 두 장(시트 +,-)으로 복제, 레이블 +1 이면 같은 시트끼리, -1 이면 엇갈려 접착."""
    P2, src = [], []
    for i, c in enumerate(pieces):
        P2.append([(v, 0) for v in c]); src.append((i, 0))
        P2.append([(v, 1) for v in reversed(c)]); src.append((i, 1))
    # 접착 그래프: 원래 H 의 변을 시트 규칙대로 들어올림
    H2 = nx.MultiGraph(); H2.add_nodes_from(range(len(P2)))
    idx = {s: k for k, s in enumerate(src)}
    for i, j, d in H.edges(data=True):
        a, b = d['e']
        for t in (0, 1):
            t2 = t if d['lab'] == +1 else 1 - t
            # 덮개 정점: 원래 정점 v 의 시트 t 복제는 (v,t). 접착은 같은 원래 정점끼리
            H2.add_edge(idx[(i, t)], idx[(j, t2)], pair=((a, t), (a, t2), (b, t), (b, t2)))
    uf = {}
    def f(x):
        uf.setdefault(x, x)
        while uf[x] != x:
            uf[x] = uf[uf[x]]; x = uf[x]
        return x
    for k, c in enumerate(P2):
        for v in c: f((k, v))
    for k, l, d in H2.edges(data=True):
        a0, a1, b0, b1 = d['pair']
        uf[f((k, a0))] = f((l, a1)); uf[f((k, b0))] = f((l, b1))
    A = nx.Graph()
    for k, c in enumerate(P2):
        for (x, y) in cyc_edges(c):
            A.add_edge(f((k, x)), f((k, y)))
    proj = {f((k, v)): v[0] for k, c in enumerate(P2) for v in c}
    return A, proj

def is_covering(A, G, proj):
    for u in A:
        img = [proj[w] for w in A[u]]
        if len(set(img)) != len(img) or set(img) != set(G[proj[u]]):
            return False
    return True

def report(name, G, pieces):
    H, mult = overlap_graph(pieces)
    A = assemble(pieces, H)
    per = [is_peripheral(G, c) for c in pieces]
    eu = nx.Graph(H)
    print(f"== {name}: |V|={G.number_of_nodes()} |E|={G.number_of_edges()} 조각 {len(pieces)}")
    print("  조립=G?", nx.is_isomorphic(A, G), "| H 단순화:", eu.number_of_nodes(), "점", eu.number_of_edges(), "변",
          "| 변의 최대 중복", max(mult.values()), "| 모든 변 덮음", set(mult) == {frozenset(e) for e in G.edges()})
    print("  주변사이클?", all(per), per if not all(per) else "", "| 3-연결?", nx.node_connectivity(G) >= 3)
    print("  홀로노미 자명?", holonomy_trivial(H), "| G 평면?", nx.check_planarity(G)[0])
    chi = G.number_of_nodes() - G.number_of_edges() + len(pieces)
    print("  χ(X)=V-E+F =", chi)
    D, proj = orientation_double_cover(pieces, H)
    print("  방향 이중피복: |V|", D.number_of_nodes(), "평면?", nx.check_planarity(D)[0],
          "연결?", nx.is_connected(D), "G 의 피복?", is_covering(D, G, proj))
    return H, D

def ladder(k, twist):
    G = nx.Graph(); P = []
    for i in range(k):
        a, b, a2, b2 = ('a', i), ('b', i), ('a', (i+1) % k), ('b', (i+1) % k)
        if twist and i == k-1:
            a2, b2 = ('b', 0), ('a', 0)
        P.append([a, a2, b2, b])
        G.add_edges_from(cyc_edges(P[-1]))
    return G, P

if __name__ == "__main__":
    for k in (2, 3, 4, 5):
        for tw in (False, True):
            G, P = ladder(k, tw)
            if k == 2 and not tw: continue  # 다중변
            report(f"{'Mobius' if tw else 'prism'} k={k}", G, P)
    # K5 = 삼각형 5개 뫼비우스 띠
    K5 = nx.complete_graph(5)
    T = [[i, (i+1) % 5, (i+2) % 5] for i in range(5)]
    report("K5, 삼각형 {i,i+1,i+2}", K5, T)
    # 피터슨 = 반-12면체: 6개 오각형, 모든 변이 정확히 2개에
    Pet = nx.petersen_graph()
    cyc5 = [c for c in nx.simple_cycles(Pet.to_directed()) if len(c) == 5]
    uniq = {}
    for c in cyc5:
        uniq.setdefault(frozenset(c), c)
    C = list(uniq.values())
    print("피터슨 5-사이클 수", len(C))
    found = None
    for S in itertools.combinations(range(len(C)), 6):
        cnt = {}
        for s in S:
            for e in cyc_edges(C[s]): cnt[frozenset(e)] = cnt.get(frozenset(e), 0) + 1
        if len(cnt) == 15 and all(v == 2 for v in cnt.values()):
            found = [C[s] for s in S]; break
    report("Petersen, 오각형 6개(반-12면체)", Pet, found)
    # 토러스 격자 K3 x K3: 사각형 9개, 홀로노미 자명인데 비평면
    G = nx.Graph(); Q = []
    for i in range(3):
        for j in range(3):
            q = [(i, j), ((i+1) % 3, j), ((i+1) % 3, (j+1) % 3), (i, (j+1) % 3)]
            Q.append(q); G.add_edges_from(cyc_edges(q))
    report("K3□K3 (토러스), 사각형 9개", G, Q)
    # K4 = M4 의 대안: 삼각형 띠? 정사각형 조각은 주변사이클이 아님
