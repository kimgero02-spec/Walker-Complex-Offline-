# R24 researcher2: 접합 그래프 H 의 RAAG/RACG 불변량과 가법성.
# 반례 탐색·예 구성용이다. 근거로 쓰지 않는다 (보고서의 증명이 근거).
import itertools, random
import networkx as nx

def chi(edges, verts=None, cap=8):
    G = nx.Graph(); G.add_edges_from(edges)
    if verts: G.add_nodes_from(verts)
    V = sorted(G.nodes(), key=lambda v: -G.degree(v))
    if not V: return 0
    if G.number_of_edges() == 0: return 1
    for k in range(1, cap + 1):
        col = {}
        def bt(i):
            if i == len(V): return True
            v = V[i]; used = {col[u] for u in G[v] if u in col}
            mx = max(col.values(), default=-1)
            for c in range(min(k, mx + 2)):
                if c not in used:
                    col[v] = c
                    if bt(i + 1): return True
                    del col[v]
            return False
        if bt(0): return k

def planar(edges):
    G = nx.Graph(); G.add_edges_from(edges)
    return nx.check_planarity(G)[0]

def norm(e): return tuple(sorted(e))

def gamma():
    A = ['x', 'a1', 'a2', 'a3', 'a4']; B = ['x', 'b1', 'b2', 'b3', 'b4']
    E = {norm(e) for e in itertools.combinations(A, 2)} | {norm(e) for e in itertools.combinations(B, 2)}
    E -= {norm(('x', 'a1')), norm(('x', 'b1'))}
    E |= {norm(('a1', 'b1'))}
    return sorted(E)

def owner_ok(E, P1, P2, V1, V2):
    for (u, v) in E:
        if u in V1 and v in V1 and (u, v) not in P1: return False
        if u in V2 and v in V2 and (u, v) not in P2: return False
    return True

def additive(E, P1, P2):
    return chi(P1) + chi(P2) == chi(E)

def find_gamma_decomp():
    E = gamma(); V = sorted({v for e in E for v in e})
    for r in range(1, len(V)):
        for V1 in itertools.combinations(V, r):
            V1 = set(V1); V2 = set(V) - V1
            I1 = [e for e in E if e[0] in V1 and e[1] in V1]
            I2 = [e for e in E if e[0] in V2 and e[1] in V2]
            if chi(I1, V1) != 2 or chi(I2, V2) != 3: continue
            C = [e for e in E if (e[0] in V1) != (e[1] in V1)]
            for mask in range(2 ** len(C)):
                P1 = I1 + [C[i] for i in range(len(C)) if mask >> i & 1]
                P2 = I2 + [C[i] for i in range(len(C)) if not mask >> i & 1]
                if chi(P1) == 2 and chi(P2) == 3 and planar(P1) and planar(P2):
                    return E, sorted(P1), sorted(P2), V1, V2
    return None

def bitstats(E, P1, P2):
    s1, s2 = set(P1), set(P2)
    a = sum(1 for e in E if e in s1 and e not in s2)
    b = sum(1 for e in E if e in s2 and e not in s1)
    c = sum(1 for e in E if e in s1 and e in s2)
    return a, b, c

def Hbit(E, P1, P2):
    """보고서 정의 4.1 의 부호화: 원래 점마다 잎 5개, 변마다 중간점 m_e 와 잎 t(e)개."""
    s1, s2 = set(P1), set(P2); H = nx.Graph()
    V = sorted({v for e in E for v in e})
    for v in V:
        for i in range(5): H.add_edge(('v', v), ('lv', v, i))
    for e in E:
        t = 3 if (e in s1 and e in s2) else (1 if e in s1 else 2)
        m = ('m', e); H.add_edge(m, ('v', e[0])); H.add_edge(m, ('v', e[1]))
        for i in range(t): H.add_edge(m, ('lm', e, i))
    return H

def cross_graph(E, V1, V2):
    H = nx.Graph(); H.add_nodes_from(V1 | V2)
    H.add_edges_from(e for e in E if (e[0] in V1) != (e[1] in V1)); return H

def shared_graph(P1, P2):
    H = nx.Graph(); s = set(P1) & set(P2)
    H.add_nodes_from({v for e in P1 for v in e} & {v for e in P2 for v in e})
    H.add_edges_from(s); return H

if __name__ == '__main__':
    E, P1, P2, V1, V2 = find_gamma_decomp()
    print('Gamma |E|', len(E), 'chi', chi(E))
    print('V1', sorted(V1), 'V2', sorted(V2))
    print('P1', P1); print('P2', P2)
    print('chi P1,P2', chi(P1), chi(P2), 'planar', planar(P1), planar(P2), 'owner', owner_ok(E, P1, P2, V1, V2))
    C = [e for e in E if (e[0] in V1) != (e[1] in V1)]
    print('cross', C, 'in P1:', [e for e in C if e in P1])
    # D_J: 내부 변 제거 (교차 그래프 보존)
    P1j = [e for e in P1 if e in C]; P2j = [e for e in P2 if e in C]
    print('D_J: chi(G)=', chi(C), 'chi P', chi(P1j), chi(P2j), 'additive', additive(C, P1j, P2j),
          'H_J iso', nx.is_isomorphic(cross_graph(E, V1, V2), cross_graph(C, V1, V2)))
    # D_S: 공유 그래프만 남김
    S = sorted(set(P1) & set(P2)); print('shared edges', S)
    # D_e: 사설 내부 변 하나 제거
    for e in E:
        if (e in P2 and e not in P1 and e[0] in V2 and e[1] in V2) or (e in P1 and e not in P2 and e[0] in V1 and e[1] in V1):
            E2 = [f for f in E if f != e]; Q1 = [f for f in P1 if f != e]; Q2 = [f for f in P2 if f != e]
            print('D-e', e, 'chi(G-e)', chi(E2), 'chi', chi(Q1), chi(Q2), 'additive', additive(E2, Q1, Q2),
                  'owner', owner_ok(E2, Q1, Q2, V1, V2),
                  'H_J iso', nx.is_isomorphic(cross_graph(E, V1, V2), cross_graph(E2, V1, V2)),
                  'H_S iso', nx.is_isomorphic(shared_graph(P1, P2), shared_graph(Q1, Q2)))
    st = bitstats(E, P1, P2); print('bit stats (a,b,c)', st, 'Sigma t', st[0] + 2 * st[1] + 3 * st[2])
    # 같은 (a,b,c) 의 비가법 분해 탐색 (Gamma 위, 소유 분할 있음, 평면 두 조각)
    random.seed(1); Vall = sorted({v for e in E for v in e}); found = None
    for it in range(200000):
        lab = {e: random.choice([1, 2, 3]) for e in E}
        Q1 = sorted(e for e in E if lab[e] in (1, 3)); Q2 = sorted(e for e in E if lab[e] in (2, 3))
        if bitstats(E, Q1, Q2) != st: continue
        if not (planar(Q1) and planar(Q2)): continue
        ok = None
        for r in range(0, len(Vall) + 1):
            for W in itertools.combinations(Vall, r):
                W = set(W)
                if owner_ok(E, Q1, Q2, W, set(Vall) - W): ok = W; break
            if ok is not None: break
        if ok is None: continue
        if not additive(E, Q1, Q2):
            found = (Q1, Q2, ok); break
    if found:
        Q1, Q2, W = found
        print('nonadditive same stats: Q1', Q1); print('Q2', Q2); print('W1', sorted(W))
        print('chi', chi(Q1), chi(Q2), 'Sigma t equal; Hbit sizes',
              Hbit(E, P1, P2).number_of_nodes(), Hbit(E, P1, P2).number_of_edges(),
              Hbit(E, Q1, Q2).number_of_nodes(), Hbit(E, Q1, Q2).number_of_edges())
    # K4 쌍
    K4 = [norm(e) for e in itertools.combinations([1, 2, 3, 4], 2)]
    D1 = ([(1, 2), (2, 3), (3, 4), (1, 4)], [(1, 3), (2, 3), (2, 4), (1, 4)])
    D4 = (K4, [(1, 2), (2, 3), (3, 4)])
    for D in (D1, D4):
        print('K4', D, 'chi', chi(D[0]), chi(D[1]), 'additive', additive(K4, *D), 'stats', bitstats(K4, *D))

def same_stats_nonadditive_gamma():
    """(a,b,c)=(4,15,0) 인 Gamma 의 비가법 분해를 결정적으로 찾는다 (예 구성용)."""
    E = gamma(); Vall = sorted({v for e in E for v in e})
    for T in itertools.combinations(E, 4):
        T = list(T); R = [e for e in E if e not in T]
        if not (planar(T) and planar(R)): continue
        if chi(T) + chi(R) <= 5: continue
        for r in range(0, len(Vall) + 1):
            for W in itertools.combinations(Vall, r):
                W = set(W)
                if owner_ok(E, T, R, W, set(Vall) - W):
                    return T, R, W, chi(T), chi(R)
    return None

if __name__ == '__main__':
    print('same-stats nonadditive:', same_stats_nonadditive_gamma())
