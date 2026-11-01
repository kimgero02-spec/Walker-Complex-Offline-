# R49 망상꾼: 관 종수 (tube genus) 확인 도구.
# 회전계(rotation system)로 G 의 매장을 주고, 면 추적으로 종수를 계산한다.
# 관 구조 판정: 모든 면이 교차 간선 출현을 0 또는 2 개만 가지면 곡선계가 결정된다.
#   R_i ~ B_i ∪ (V_i 만으로 된 면) 이므로 chi(R_i) = n_i - e_i + f_i = 2 - 2 g_i - b.
#   g_1 = g_2 = 0 이면 관 매장이고 종수 = b - 1.
# 상계용 국소 탐색 (정해 둔 작은 그래프 몇 개에만 사용).
import networkx as nx, random, itertools

def faces(rot):
    # rot: v -> list (cyclic). 다트 (u,v) 다음 = (v, rot[v] 에서 u 다음)
    pos = {v: {w: i for i, w in enumerate(rot[v])} for v in rot}
    seen = set(); F = []
    for u in rot:
        for v in rot[u]:
            if (u, v) in seen: continue
            walk = []; a, b = u, v
            while (a, b) not in seen:
                seen.add((a, b)); walk.append((a, b))
                L = rot[b]; nxt = L[(pos[b][a] + 1) % len(L)]
                a, b = b, nxt
            F.append(walk)
    return F

def genus(rot):
    V = len(rot); E = sum(len(l) for l in rot.values()) // 2
    F = len(faces(rot))
    return (2 - V + E - F) // 2

def tube_info(rot, V1):
    V1 = set(V1); F = faces(rot)
    side = lambda x: 1 if x in V1 else 2
    n = {1: 0, 2: 0}; e = {1: 0, 2: 0}; f = {1: 0, 2: 0}
    for v in rot: n[side(v)] += 1
    for u in rot:
        for v in rot[u]:
            if u < v and side(u) == side(v): e[side(u)] += 1
    bad = 0; cutfaces = []
    for i, w in enumerate(F):
        c = sum(1 for (a, b) in w if side(a) != side(b))
        if c == 0: f[side(w[0][0])] += 1
        elif c == 2: cutfaces.append(i)
        else: bad += 1
    # 곡선 = 교차 간선을 공유하는 cut 면들의 연결 성분
    D = nx.Graph(); D.add_nodes_from(cutfaces)
    owner = {}
    for i in cutfaces:
        for (a, b) in F[i]:
            if side(a) != side(b): owner.setdefault(frozenset((a, b)), []).append(i)
    for k, l in owner.items():
        if len(l) == 2: D.add_edge(*l)
    b = nx.number_connected_components(D) if cutfaces else 0
    g = {s: (2 - (n[s] - e[s] + f[s]) - b) / 2 for s in (1, 2)}
    return dict(genus=genus(rot), bad=bad, curves=b, g1=g[1], g2=g[2])

def planar_rot(G):
    ok, emb = nx.check_planarity(G)
    assert ok
    return {v: list(emb.neighbors_cw_order(v)) for v in G}

def tube_search(G, V1, iters=200000, seed=0, mirror2=False, target=None):
    """B_i 회전은 평면 매장으로 고정, 교차 간선 위치만 움직이는 국소 탐색.
    비용 = 종수 + 10*(bad 면) + 10*(g1+g2). 관 매장을 찾으면 (b-1) 반환."""
    rnd = random.Random(seed)
    V1 = set(V1); V2 = set(G) - V1
    r1 = planar_rot(G.subgraph(V1)); r2 = planar_rot(G.subgraph(V2))
    if mirror2: r2 = {v: l[::-1] for v, l in r2.items()}
    base = {**r1, **r2}
    rot = {v: list(base[v]) for v in G}
    for u, v in G.edges():
        if (u in V1) != (v in V1):
            for a, b in ((u, v), (v, u)):
                L = rot[a]; L.insert(rnd.randrange(len(L) + 1), b)
    def cost(r):
        t = tube_info(r, V1)
        pen = 10 * (abs(t['g1']) + abs(t['g2'])) if t['bad'] == 0 else 20
        return t['genus'] + 10 * t['bad'] + pen, t
    c, t = cost(rot); best = (c, t, {v: list(l) for v, l in rot.items()})
    cross = [(a, b) for a in G for b in G[a] if (a in V1) != (b in V1)]
    T = 2.0
    for it in range(iters):
        a, b = rnd.choice(cross)
        L = rot[a]; i = L.index(b); L.pop(i); j = rnd.randrange(len(L) + 1); L.insert(j, b)
        c2, t2 = cost(rot)
        if c2 <= c or rnd.random() < pow(2.718, (c - c2) / T):
            c, t = c2, t2
            if c < best[0]: best = (c, t, {v: list(l) for v, l in rot.items()})
            if target is not None and c <= target: break
        else:
            L.pop(j); L.insert(i, b)
        T = max(0.05, T * 0.99997)
    return best

def free_genus_search(G, iters=200000, seed=0, target=None):
    rnd = random.Random(seed)
    rot = {v: list(G[v]) for v in G}
    for v in rot: rnd.shuffle(rot[v])
    c = genus(rot); best = (c, {v: list(l) for v, l in rot.items()})
    E = [(a, b) for a in G for b in G[a]]
    T = 1.0
    for it in range(iters):
        a, b = rnd.choice(E); L = rot[a]
        if len(L) < 3: continue
        i = L.index(b); L.pop(i); j = rnd.randrange(len(L) + 1); L.insert(j, b)
        c2 = genus(rot)
        if c2 <= c or rnd.random() < pow(2.718, (c - c2) / T):
            c = c2
            if c < best[0]: best = (c, {v: list(l) for v, l in rot.items()})
            if target is not None and c <= target: break
        else:
            L.pop(j); L.insert(i, b)
        T = max(0.05, T * 0.99997)
    return best
