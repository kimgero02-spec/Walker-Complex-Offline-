# researcher2 (반례꾼) 독립 인증서 탐색: tau(G) <= d+1 을 주는 R^d 배치 y: V->R^d
# 조건: 모든 극대 완전이분쌍 (A,B) (A,B 비어있지 않음) 에 대해 y_A, y_B 가 어파인 초평면으로 엄격 분리됨.
import itertools, random, sys
import numpy as np
import networkx as nx
from scipy.optimize import linprog

def lex_product_c(n, m):
    # C_n[K_m]: 정점 (i,s), i in Z_n, s in range(m)
    G = nx.Graph()
    V = [(i, s) for i in range(n) for s in range(m)]
    G.add_nodes_from(V)
    for i in range(n):
        for s in range(m):
            for t in range(m):
                if s != t:
                    G.add_edge((i, s), (i, t))
            j = (i + 1) % n
            for t in range(m):
                G.add_edge((i, s), (j, t))
    return G

def max_pairs(G):
    """극대 완전이분쌍 (A,B): A = N(N(A)) 인 A, B = N(A). A,B 비어있지 않음."""
    V = list(G.nodes())
    idx = {v: k for k, v in enumerate(V)}
    nb = [0] * len(V)
    for v in V:
        for u in G[v]:
            nb[idx[v]] |= 1 << idx[u]
    n = len(V)
    full = (1 << n) - 1
    def common(mask):
        r = full
        k = 0
        while mask:
            if mask & 1:
                r &= nb[k]
            mask >>= 1
            k += 1
        return r
    pairs = set()
    for A in range(1, 1 << n):
        B = common(A)
        if B == 0:
            continue
        A2 = common(B)
        if A2 != A:
            continue
        pairs.add((A, B))
    out = []
    for A, B in pairs:
        Al = [V[k] for k in range(n) if A >> k & 1]
        Bl = [V[k] for k in range(n) if B >> k & 1]
        out.append((Al, Bl))
    return out

def margin_for_pair(Y, Al, Bl, idx, d):
    """LP: max delta s.t. w.y_a + c >= delta (a in A), w.y_b + c <= -delta (b in B), |w_i|<=1, |c|<=1e3."""
    # variables: w (d), c, delta ; minimize -delta
    nv = d + 2
    A_ub, b_ub = [], []
    for a in Al:
        y = Y[idx[a]]
        row = np.zeros(nv); row[:d] = -y; row[d] = -1; row[d + 1] = 1  # -(w.y + c) + delta <= 0 -> delta <= w.y+c
        A_ub.append(row); b_ub.append(0.0)
    for b in Bl:
        y = Y[idx[b]]
        row = np.zeros(nv); row[:d] = y; row[d] = 1; row[d + 1] = 1  # w.y + c + delta <= 0
        A_ub.append(row); b_ub.append(0.0)
    cobj = np.zeros(nv); cobj[d + 1] = -1
    bounds = [(-1, 1)] * d + [(-1e3, 1e3), (None, 1)]
    res = linprog(cobj, A_ub=np.array(A_ub), b_ub=np.array(b_ub), bounds=bounds, method="highs")
    if res.status != 0:
        return -1.0, None
    return res.x[d + 1], res.x[:d + 1]

def global_margin(Y, pairs, idx, d):
    worst = 1e9; arg = None
    for k, (Al, Bl) in enumerate(pairs):
        dl, _ = margin_for_pair(Y, Al, Bl, idx, d)
        if dl < worst:
            worst = dl; arg = k
    return worst, arg

def search(G, d, iters=3000, restarts=5, seed=1):
    random.seed(seed); np.random.seed(seed)
    V = list(G.nodes()); idx = {v: k for k, v in enumerate(V)}
    pairs = max_pairs(G)
    best_overall = (-1, None)
    for r in range(restarts):
        Y = np.random.uniform(-1, 1, size=(len(V), d))
        cur, _ = global_margin(Y, pairs, idx, d)
        step = 0.3
        for it in range(iters):
            Z = Y.copy()
            k = random.randrange(len(V))
            Z[k] = np.clip(Z[k] + np.random.normal(0, step, size=d), -1, 1)
            val, _ = global_margin(Z, pairs, idx, d)
            if val >= cur:
                Y, cur = Z, val
            if it % 500 == 499:
                step *= 0.7
        if cur > best_overall[0]:
            best_overall = (cur, Y.copy())
        print(f"restart {r}: margin {cur:.4f}", flush=True)
    return best_overall, pairs, V, idx

if __name__ == "__main__":
    which = sys.argv[1]
    d = int(sys.argv[2])
    if which == "C5K2":
        G = lex_product_c(5, 2)
    elif which == "C5K3":
        G = lex_product_c(5, 3)
    elif which == "C7K2":
        G = lex_product_c(7, 2)
    print(which, "n=", G.number_of_nodes(), "m=", G.number_of_edges(), "omega=", max(len(c) for c in nx.find_cliques(G)))
    pairs = max_pairs(G)
    print("maximal complete pairs:", len(pairs))
    (m, Y), pairs, V, idx = search(G, d, iters=int(sys.argv[3]) if len(sys.argv) > 3 else 3000)
    print("best margin", m)
    np.save(f"{which}_d{d}.npy", Y)
