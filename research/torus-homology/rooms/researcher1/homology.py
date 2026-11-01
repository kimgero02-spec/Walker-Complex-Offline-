#!/usr/bin/env python3
"""researcher1 (R01): 여러 모델로 H_n(X;Z) 직접 계산.
- 정수 스미스 표준형(SNF)을 직접 구현 (정확한 정수 연산)
- 모델: CW, Delta-복합체, 단체 복합체 (S^1, T^2, T^3, Klein bottle)
"""
import itertools
from collections import defaultdict

# ---------------------------------------------------------------- SNF
def smith_diagonal(M):
    """정수 행렬 M (list of lists)의 스미스 표준형 대각 성분(0 아닌 것)."""
    A = [row[:] for row in M]
    m = len(A)
    n = len(A[0]) if m else 0
    diag = []
    r = 0
    while r < m and r < n:
        # 피벗: 남은 부분행렬에서 절댓값 최소 nonzero
        piv = None
        for i in range(r, m):
            for j in range(r, n):
                if A[i][j] != 0 and (piv is None or abs(A[i][j]) < abs(A[piv[0]][piv[1]])):
                    piv = (i, j)
        if piv is None:
            break
        i, j = piv
        A[r], A[i] = A[i], A[r]
        for row in A:
            row[r], row[j] = row[j], row[r]
        while True:
            changed = False
            p = A[r][r]
            # 열 r 소거
            for i in range(r + 1, m):
                if A[i][r] != 0:
                    q = A[i][r] // p
                    for k in range(r, n):
                        A[i][k] -= q * A[r][k]
                    if A[i][r] != 0:
                        changed = True
            # 행 r 소거
            for j in range(r + 1, n):
                if A[r][j] != 0:
                    q = A[r][j] // p
                    for k in range(r, m):
                        A[k][j] -= q * A[k][r]
                    if A[r][j] != 0:
                        changed = True
            if changed:
                # 더 작은 nonzero를 피벗으로
                best = (r, r)
                for i in range(r, m):
                    if A[i][r] != 0 and abs(A[i][r]) < abs(A[best[0]][best[1]]):
                        best = (i, r)
                for j in range(r, n):
                    if A[r][j] != 0 and abs(A[r][j]) < abs(A[best[0]][best[1]]):
                        best = (r, j)
                i, j = best
                A[r], A[i] = A[i], A[r]
                for row in A:
                    row[r], row[j] = row[j], row[r]
                continue
            # 나눗셈 조건: p 가 나머지 모든 성분을 나누는지
            bad = None
            for i in range(r + 1, m):
                for j in range(r + 1, n):
                    if A[i][j] % p != 0:
                        bad = i
                        break
                if bad is not None:
                    break
            if bad is not None:
                for k in range(r, n):
                    A[r][k] += A[bad][k]
                continue
            break
        diag.append(abs(A[r][r]))
        r += 1
    return diag


def homology(dims, bds):
    """dims[k]=rank C_k, bds[k]=행렬 d_k : C_k -> C_{k-1} (행 dims[k-1] x 열 dims[k]), k>=1.
    반환: [(betti, [torsion])...] for k=0..top."""
    top = len(dims) - 1
    snf = {}
    for k in range(1, top + 1):
        M = bds[k]
        snf[k] = smith_diagonal(M) if dims[k] and dims[k - 1] else []
    res = []
    for k in range(top + 1):
        rk_k = len(snf.get(k, []))          # rank d_k
        rk_k1 = len(snf.get(k + 1, []))     # rank d_{k+1}
        betti = dims[k] - rk_k - rk_k1
        tors = [d for d in snf.get(k + 1, []) if d > 1]
        res.append((betti, tors))
    return res


def matmul(A, B):
    if not A or not B or not B[0]:
        return []
    return [[sum(A[i][t] * B[t][j] for t in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))]


def check_dd(dims, bds):
    ok = True
    for k in range(2, len(dims)):
        if dims[k] and dims[k - 2]:
            P = matmul(bds[k - 1], bds[k])
            if any(x != 0 for row in P for x in row):
                ok = False
    return ok


def fmt(b, t):
    parts = []
    if b == 1:
        parts.append(r"\mathbb{Z}")
    elif b > 1:
        parts.append(r"\mathbb{Z}^{%d}" % b)
    for d in t:
        parts.append(r"\mathbb{Z}/%d" % d)
    return " \\oplus ".join(parts) if parts else "0"


# ------------------------------------------------- 단체 복합체(정렬 꼭짓점)
def simplicial_chain_complex(facets):
    """facets: 최고차원 단체들(꼭짓점 집합). 모든 면을 생성하고, 꼭짓점 정렬순 방향."""
    top = max(len(f) for f in facets) - 1
    simp = [set() for _ in range(top + 1)]
    for f in facets:
        f = tuple(sorted(f))
        for k in range(1, len(f) + 1):
            for s in itertools.combinations(f, k):
                simp[k - 1].add(s)
    simp = [sorted(s) for s in simp]
    idx = [{s: i for i, s in enumerate(L)} for L in simp]
    dims = [len(L) for L in simp]
    bds = [None]
    for k in range(1, top + 1):
        M = [[0] * dims[k] for _ in range(dims[k - 1])]
        for j, s in enumerate(simp[k]):
            for i in range(k + 1):
                face = s[:i] + s[i + 1:]
                M[idx[k - 1][face]][j] += (-1) ** i
        bds.append(M)
    return dims, bds, simp


def pseudomanifold_check(simp):
    """닫힌 다양체 조건 간이 확인: 각 (top-1)-단체가 정확히 2개 top-단체에 포함."""
    top = len(simp) - 1
    cnt = defaultdict(int)
    for s in simp[top]:
        for i in range(top + 1):
            cnt[s[:i] + s[i + 1:]] += 1
    return all(cnt[f] == 2 for f in simp[top - 1])


def link_is_sphere_surface(simp):
    """2차원: 각 꼭짓점의 링크가 단일 순환(원)인지."""
    tris = simp[2]
    for v in simp[0]:
        v = v[0]
        edges = [tuple(x for x in t if x != v) for t in tris if v in t]
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b); adj[b].append(a)
        if any(len(l) != 2 for l in adj.values()):
            return False
        # 연결성
        start = next(iter(adj)); seen = {start}; st = [start]
        while st:
            x = st.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y); st.append(y)
        if len(seen) != len(adj):
            return False
    return True


# ------------------------- Kuhn(Freudenthal) 삼각분할의 R^d / N Z^d 몫 (Delta 또는 단체)
def kuhn_torus(d, N):
    """R^d 의 Kuhn 삼각분할을 N Z^d 로 나눈 몫. N=1 이면 꼭짓점 1개 Delta-복합체.
    단체를 '평행이동 류'로 식별 (Delta-복합체 구조). 반환: dims, bds, info"""
    def canon(verts):
        base = verts[0]
        shift = tuple((b % N) - b for b in base)
        return tuple(tuple(v[c] + shift[c] for c in range(d)) for v in verts)

    tops = set()
    for cube in itertools.product(range(N), repeat=d):
        for perm in itertools.permutations(range(d)):
            v = list(cube); verts = [tuple(v)]
            for c in perm:
                v[c] += 1; verts.append(tuple(v))
            tops.add(canon(verts))
    simp = [set() for _ in range(d + 1)]
    simp[d] = tops
    for k in range(d, 0, -1):
        for s in simp[k]:
            for i in range(k + 1):
                simp[k - 1].add(canon(s[:i] + s[i + 1:]))
    simp = [sorted(s) for s in simp]
    idx = [{s: i for i, s in enumerate(L)} for L in simp]
    dims = [len(L) for L in simp]
    bds = [None]
    for k in range(1, d + 1):
        M = [[0] * dims[k] for _ in range(dims[k - 1])]
        for j, s in enumerate(simp[k]):
            for i in range(k + 1):
                M[idx[k - 1][canon(s[:i] + s[i + 1:])]][j] += (-1) ** i
        bds.append(M)
    # 단체 복합체인지: 꼭짓점 집합(mod N) 이 서로 다르고 반복 없음
    is_simplicial = True
    for k in range(d + 1):
        keys = set()
        for s in simp[k]:
            vs = frozenset(tuple(x % N for x in v) for v in s)
            if len(vs) != k + 1 or vs in keys:
                is_simplicial = False
            keys.add(vs)
    return dims, bds, is_simplicial


# -------------------------------- 격자 몫 (union-find): 토러스 / 클라인 병 단체 복합체
def grid_surface(m, n, kind):
    """(i,j), 0<=i<=m, 0<=j<=n 격자. 각 정사각형을 대각선 (i,j)-(i+1,j+1)로 분할.
    torus: (i,0)~(i,n), (0,j)~(m,j);  klein: (i,0)~(i,n), (0,j)~(m,n-j)."""
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def union(a, b):
        parent[find(a)] = find(b)
    for i in range(m + 1):
        union((i, 0), (i, n))
    for j in range(n + 1):
        union((0, j), (m, j) if kind == "torus" else (m, n - j))
    for i in range(m + 1):
        for j in range(n + 1):
            find((i, j))
    reps = sorted({find(p) for p in parent})
    lab = {r: k for k, r in enumerate(reps)}
    V = lambda p: lab[find(p)]
    tris = []
    for i in range(m):
        for j in range(n):
            a, b, c, e = (i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)
            tris.append((V(a), V(b), V(c)))
            tris.append((V(a), V(e), V(c)))
    ok = all(len(set(t)) == 3 for t in tris) and len({frozenset(t) for t in tris}) == len(tris)
    # 그리드 변 수와 꼭짓점쌍 변 수가 같아야 진짜 단체 복합체
    grid_edges = 3 * m * n  # 닫힌 곡면: E = 3F/2 = 3mn
    edges = {frozenset(p) for t in tris for p in itertools.combinations(t, 2)}
    ok = ok and len(edges) == grid_edges
    return tris, ok


def run(name, model, dims, bds, extra=""):
    H = homology(dims, bds)
    chi = sum((-1) ** k * c for k, c in enumerate(dims))
    chiH = sum((-1) ** k * b for k, (b, _) in enumerate(H))
    dd = check_dd(dims, bds)
    row = dict(space=name, model=model, cells=dims, H=[fmt(b, t) for b, t in H],
               chi=chi, chiH=chiH, dd=dd, extra=extra)
    print(f"{name:6s} | {model:38s} | cells={dims} | H=" +
          ", ".join(f"H{k}={fmt(b,t)}" for k, (b, t) in enumerate(H)) +
          f" | chi={chi} (betti chi={chiH}) | dd=0:{dd} {extra}")
    return row


def show_matrix(M):
    return "\n".join("    [" + " ".join(f"{x:2d}" for x in r) + " ]" for r in M)


if __name__ == "__main__":
    rows = []
    # ---- S^1
    rows.append(run("S1", "CW (e0, e1), d1=0", [1, 1], [None, [[0]]]))
    d, b, s = kuhn_torus(1, 1)
    rows.append(run("S1", "Delta (Kuhn N=1)", d, b, f"simplicial={s}"))
    d, b, s = kuhn_torus(1, 3)
    rows.append(run("S1", "simplicial (삼각형 경계, N=3)", d, b, f"simplicial={s}"))

    # ---- T^2 CW: d1(a)=d1(b)=v-v=0, d2(U)=a+b-a-b=0
    rows.append(run("T2", "CW (1,2,1) word aba^-1b^-1", [1, 2, 1],
                    [None, [[0, 0]], [[1 - 1], [1 - 1]]]))
    # ---- T^2 Delta (Hatcher): edges a,b,c; dU = b - c + a, dL = a - c + b  (모두 a+b-c)
    d2 = [[1, 1], [1, 1], [-1, -1]]
    print("T2 Delta d2 (rows a,b,c; cols U,L):\n" + show_matrix(d2))
    rows.append(run("T2", "Delta (Hatcher, 1/3/2)", [1, 3, 2], [None, [[0, 0, 0]], d2]))
    d, b, s = kuhn_torus(2, 1)
    print("T2 Kuhn N=1 d2:\n" + show_matrix(b[2]))
    rows.append(run("T2", "Delta (Kuhn N=1, 자동생성)", d, b, f"simplicial={s}"))
    for N in (2, 3, 4):
        d, b, s = kuhn_torus(2, N)
        rows.append(run("T2", f"Kuhn N={N} ({N}x{N} 격자)", d, b, f"simplicial={s}"))
    tris, ok = grid_surface(3, 3, "torus")
    d, b, simp = simplicial_chain_complex(tris)
    rows.append(run("T2", "simplicial 3x3 격자(union-find)", d, b,
                    f"valid={ok}, pm={pseudomanifold_check(simp)}, link={link_is_sphere_surface(simp)}"))
    # 7-꼭짓점 Möbius 토러스: {i,i+1,i+3}, {i,i+2,i+3} mod 7
    tris7 = [(i, (i + 1) % 7, (i + 3) % 7) for i in range(7)] + \
            [(i, (i + 2) % 7, (i + 3) % 7) for i in range(7)]
    d, b, simp = simplicial_chain_complex(tris7)
    rows.append(run("T2", "simplicial 7꼭짓점 (Möbius/Császár)", d, b,
                    f"pm={pseudomanifold_check(simp)}, link={link_is_sphere_surface(simp)}, "
                    f"E=K7:{len(simp[1])==21}"))

    # ---- T^3
    z = lambda r, c: [[0] * c for _ in range(r)]
    rows.append(run("T3", "CW 큐브 (1,3,3,1), 모든 d=0", [1, 3, 3, 1],
                    [None, z(1, 3), z(3, 3), z(3, 1)]))
    d, b, s = kuhn_torus(3, 1)
    rows.append(run("T3", "Delta (Kuhn N=1, 큐브 6사면체)", d, b, f"simplicial={s}"))
    d, b, s = kuhn_torus(3, 3)
    rows.append(run("T3", "simplicial (Kuhn N=3, 27꼭짓점)", d, b, f"simplicial={s}"))

    # ---- Klein bottle
    # CW: word a b a b^-1 : d2 = a + b + a - b = 2a
    rows.append(run("K", "CW (1,2,1) word aba b^-1", [1, 2, 1],
                    [None, [[0, 0]], [[2], [0]]]))
    # Delta (Hatcher Fig.): dU = a + b - c, dL = a - b + c  (rows a,b,c)
    d2K = [[1, 1], [1, -1], [-1, 1]]
    print("K Delta d2 (rows a,b,c; cols U,L):\n" + show_matrix(d2K))
    rows.append(run("K", "Delta (Hatcher, 1/3/2)", [1, 3, 2], [None, [[0, 0, 0]], d2K]))
    for (m, n) in ((3, 3), (4, 4)):
        tris, ok = grid_surface(m, n, "klein")
        d, b, simp = simplicial_chain_complex(tris)
        rows.append(run("K", f"simplicial {m}x{n} 격자(union-find)", d, b,
                        f"valid={ok}, pm={pseudomanifold_check(simp)}, link={link_is_sphere_surface(simp)}"))

    import json
    with open(__file__.replace("homology.py", "results.json"), "w") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
