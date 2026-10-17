# R02 researcher3: d_R checks. Radon-free in R^1 = disjoint intervals for every biclique (X,Y).
import itertools

def bicliques(n, E):
    adj = {v: set() for v in range(n)}
    for a, b in E:
        adj[a].add(b); adj[b].add(a)
    out = []
    for k in range(1, n):
        for X in itertools.combinations(range(n), k):
            X = frozenset(X)
            common = set(range(n))
            for x in X:
                common &= adj[x]
            common -= X
            for m in range(1, len(common) + 1):
                for Y in itertools.combinations(sorted(common), m):
                    out.append((X, frozenset(Y)))
    return out

def radon_free(n, E, y):
    for X, Y in bicliques(n, E):
        xl, xh = min(y[v] for v in X), max(y[v] for v in X)
        yl, yh = min(y[v] for v in Y), max(y[v] for v in Y)
        if not (xh < yl or yh < xl):
            return False, (sorted(X), sorted(Y))
    return True, None

C4 = (4, [(0, 2), (2, 1), (1, 3), (3, 0)])        # parts {0,1} | {2,3}
K33 = (6, [(i, j) for i in range(3) for j in range(3, 6)])
K3 = (3, list(itertools.combinations(range(3), 2)))
K4 = (4, list(itertools.combinations(range(4), 2)))

# [증명] bipartite: put part 1 left of part 2 -> radon-free on R^1
print("C4, parts left/right in R^1:", radon_free(*C4, [0.0, 1.0, 2.0, 3.0]))
print("K33, parts left/right in R^1:", radon_free(*K33, [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]))

# K3 (= C4/edge): all 3! placements on R^1 fail
ok_any = any(radon_free(*K3, list(p))[0] for p in itertools.permutations(range(3)))
print("K3 radon-free placement in R^1 exists:", ok_any)

# K4 placements in R^2: 4 points, any placement has a Radon pair, so fails (sanity)
# simplex placement in R^3 works (d_R(K4)<=3):
import numpy as np
S = np.array([[1,0,0],[0,1,0],[0,0,1],[0,0,0]], float)
def radon_free_nd(n, E, Y):
    for X, Yb in bicliques(n, E):
        # convex hulls disjoint <=> no lambda,mu with sum-equal; use LP
        from scipy.optimize import linprog
        A = []; b = []
        nx, ny = len(X), len(Yb)
        Aeq = np.zeros((Y.shape[1] + 1, nx + ny)); beq = np.zeros(Y.shape[1] + 1)
        P = np.hstack([Y[list(X)].T, -Y[list(Yb)].T])
        Aeq[:-1] = P; Aeq[-1, :nx] = 1; Aeq[-1, nx:] = -1
        beq[-1] = 0.0
        # hulls intersect iff exists lam>=0,sum lam=1,mu>=0,sum mu=1 with sum lam*x - sum mu*y = 0
        Aeq2 = np.zeros((Y.shape[1] + 2, nx + ny)); beq2 = np.zeros(Y.shape[1] + 2)
        Aeq2[:-2] = P; Aeq2[-2, :nx] = 1; Aeq2[-1, nx:] = 1; beq2[-2] = 1; beq2[-1] = 1
        res = linprog(np.zeros(nx + ny), A_eq=Aeq2, b_eq=beq2, bounds=[(0, None)] * (nx + ny), method="highs")
        if res.status == 0:
            return False, (sorted(X), sorted(Yb))
    return True, None
print("K4 simplex vertices in R^3 (generic Radon check):", radon_free_nd(4, K4[1], S))
