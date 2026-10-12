# 관 매장의 명시적 구성: 시트 평면 매장 고정, 관 = (B1 면, B2 면) 쌍, 관마다 사다리 (환형 비교차 간선열).
# 사다리를 정확 덮개로 고르고 회전계를 조립해 면 추적으로 종수 = t-1 을 확인한다 (상계의 확인).
from r49_tube import faces, genus, tube_info
import networkx as nx, itertools

def ccw_rot(B):
    ok, emb = nx.check_planarity(B); assert ok
    return {v: list(emb.neighbors_cw_order(v))[::-1] for v in B}

def face_list(rot):
    out = []
    for w in faces(rot):
        out.append([a for a, b in w])   # 면 경계 순서 (보행 방향)
    return out

def ladders(P, Q):
    """P,Q: 면 경계 순서 (각 길이 3 등). 비교차 환형 사다리 = 단계 (di,dj) 로 도는 순환열."""
    res = {}
    nP, nQ = len(P), len(Q)
    def rec(seq, ti, tj):
        i, j = seq[-1]
        for di in range(nP):
            for dj in range(nQ):
                if di == 0 and dj == 0: continue
                Ti, Tj = ti + di, tj + dj
                if Ti > nP or Tj > nQ: continue
                ni, nj = (i + di) % nP, (j + dj) % nQ
                if (ni, nj) == seq[0] and Ti in (0, nP) and Tj in (0, nQ):
                    key = frozenset((P[a], Q[b]) for a, b in seq)
                    if len(key) == len(seq): res.setdefault(key, [(P[a], Q[b]) for a, b in seq])
                    continue
                if (ni, nj) in seq: continue
                rec(seq + [(ni, nj)], Ti, Tj)
    for i in range(nP):
        for j in range(nQ):
            res.setdefault(frozenset([(P[i], Q[j])]), [(P[i], Q[j])])
            rec([(i, j)], 0, 0)
    return res

def assemble(B1rot, B2rot, tubes, rev1, rev2):
    """tubes: list of (face1 walk, face2 walk, ladder seq). 회전계 조립."""
    rot = {v: list(l) for v, l in {**B1rot, **B2rot}.items()}
    ins = {}  # (v, prev) -> list of new nbrs
    for f1, f2, seq in tubes:
        for side, f, rev in ((0, f1, rev1), (1, f2, rev2)):
            n = len(f)
            for k, v in enumerate(f):
                prev = f[k - 1]  # 보행에서 v 직전 정점 → 모서리는 rot[v] 에서 prev 바로 다음
                nb = [e[1 - side] for e in seq if e[side] == v]
                if rev: nb = nb[::-1]
                ins.setdefault((v, prev), []).extend(nb)
    for (v, prev), nb in ins.items():
        L = rot[v]; i = L.index(prev)
        rot[v] = L[:i + 1] + nb + L[i + 1:]
    return rot

def search(G, V1, t, max_hits=1, mirror2=(False, True)):
    V1 = list(V1); V2 = [v for v in G if v not in V1]
    r1 = ccw_rot(G.subgraph(V1)); H = {frozenset(e) for e in G.edges() if (e[0] in V1) != (e[1] in V1)}
    for mir in mirror2:
        r2 = ccw_rot(G.subgraph(V2))
        if mir: r2 = {v: l[::-1] for v, l in r2.items()}
        F1, F2 = face_list(r1), face_list(r2)
        for combo in itertools.product(range(len(F1)), range(len(F2)), repeat=t):
            pairs = [(combo[2 * k], combo[2 * k + 1]) for k in range(t)]
            if len(set(pairs)) < t or len({p[0] for p in pairs}) < t or len({p[1] for p in pairs}) < t: continue
            if pairs != sorted(pairs): continue
            for d2 in (False, True):
                Ls = []
                for a, b in pairs:
                    Q = F2[b][::-1] if d2 else F2[b]
                    Ls.append([(k, s) for k, s in ladders(F1[a], Q).items() if all(frozenset(e) in H for e in k)])
                # 정확 덮개
                def cover(i, used, chosen):
                    if i == t:
                        if used == H: yield list(chosen)
                        return
                    for k, s in Ls[i]:
                        ks = {frozenset(e) for e in k}
                        if ks & used: continue
                        yield from cover(i + 1, used | ks, chosen + [s])
                for chosen in cover(0, set(), []):
                    for rev1, rev2 in itertools.product((False, True), repeat=2):
                        tubes = [(F1[a], F2[b], s) for (a, b), s in zip(pairs, chosen)]
                        rot = assemble(r1, r2, tubes, rev1, rev2)
                        ti = tube_info(rot, V1)
                        if ti['genus'] == t - 1 and ti['bad'] == 0 and ti['g1'] == 0 and ti['g2'] == 0:
                            return dict(pairs=pairs, ladders=chosen, info=ti, mirror=mir)
    return None
