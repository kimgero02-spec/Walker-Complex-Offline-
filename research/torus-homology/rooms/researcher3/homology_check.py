"""researcher3: 장애물/반례 검증 스크립트 (정수 SNF, Z/2, Q 계수)."""
import itertools, random
from fractions import Fraction

# ---------- 선형대수 ----------
def snf_diag(M):
    """정수 행렬의 Smith 표준형 대각 원소(0 아닌 것)."""
    A = [row[:] for row in M]
    m = len(A); n = len(A[0]) if m else 0
    diag = []; t = 0
    while t < min(m, n):
        piv = None
        for i in range(t, m):
            for j in range(t, n):
                if A[i][j] != 0 and (piv is None or abs(A[i][j]) < abs(A[piv[0]][piv[1]])):
                    piv = (i, j)
        if piv is None: break
        i, j = piv
        A[t], A[i] = A[i], A[t]
        for r in A: r[t], r[j] = r[j], r[t]
        while True:
            p = A[t][t]; done = True
            for i in range(t+1, m):
                q = A[i][t] // p
                if q:
                    A[i] = [a - q*b for a, b in zip(A[i], A[t])]
                if A[i][t] != 0:
                    done = False
            for j in range(t+1, n):
                q = A[t][j] // p
                if q:
                    for r in A: r[j] -= q * r[t]
                if A[t][j] != 0: done = False
            if done:
                # 나눗셈 조건
                bad = None
                for i in range(t+1, m):
                    for j in range(t+1, n):
                        if A[i][j] % p: bad = i
                if bad is None: break
                A[t] = [a + b for a, b in zip(A[t], A[bad])]
                continue
            # 더 작은 피벗으로 교체
            best = (t, t)
            for i in range(t, m):
                if A[i][t] and abs(A[i][t]) < abs(A[best[0]][best[1]]): best = (i, t)
            for j in range(t, n):
                if A[t][j] and abs(A[t][j]) < abs(A[best[0]][best[1]]): best = (t, j)
            i, j = best
            A[t], A[i] = A[i], A[t]
            for r in A: r[t], r[j] = r[j], r[t]
        diag.append(abs(A[t][t])); t += 1
    return diag

def rank_mod(M, p=None):
    """p=None 이면 Q 위의 랭크, 아니면 F_p 위의 랭크."""
    if not M or not M[0]: return 0
    A = [[(Fraction(x) if p is None else x % p) for x in r] for r in M]
    m, n = len(A), len(A[0]); r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i][c] != 0), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]
        inv = (1/A[r][c]) if p is None else pow(A[r][c], -1, p)
        A[r] = [(x*inv if p is None else x*inv % p) for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [(a - f*b if p is None else (a - f*b) % p) for a, b in zip(A[i], A[r])]
        r += 1
    return r

def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def is_zero(M): return all(x == 0 for r in M for x in r)

def homology(dims, bds):
    """dims[k]=셀 수, bds[k]= ∂_k : C_k -> C_{k-1} (행: k-1 셀, 열: k 셀), k=1..top."""
    top = len(dims) - 1
    out = {}
    for name, p in [("Z", None), ("Q", None), ("Z2", 2)]:
        res = []
        for k in range(top+1):
            rk_out = rank_mod(bds[k], p) if k >= 1 and dims[k-1] else 0   # rank ∂_k
            rk_in = rank_mod(bds[k+1], p) if k+1 <= top and dims[k+1] else 0
            if name == "Z":
                free = dims[k] - (rank_mod(bds[k]) if k >= 1 and dims[k-1] else 0) - (rank_mod(bds[k+1]) if k+1 <= top and dims[k+1] else 0)
                tors = [d for d in (snf_diag(bds[k+1]) if k+1 <= top and dims[k+1] else []) if d > 1]
                res.append((free, tors))
            else:
                res.append(dims[k] - rk_out - rk_in)
        out[name] = res
    return out

def fmtZ(h):
    s = []
    for free, tors in h:
        parts = ([f"Z^{free}" if free > 1 else "Z"] if free else []) + [f"Z/{d}" for d in tors]
        s.append(" + ".join(parts) if parts else "0")
    return s

# ---------- 단어(사각형 접착) -> 셀 복합체 ----------
def word_complex(word):
    """word: 예 'a b A B' (대문자=역). 꼭짓점 동일시는 union-find로 계산."""
    toks = word.split(); n = len(toks)
    letters = sorted(set(t.lower() for t in toks))
    par = list(range(n))
    def f(x):
        while par[x] != x: par[x] = par[par[x]]; x = par[x]
        return x
    ends = {}
    for i, t in enumerate(toks):
        tail, head = (i, (i+1) % n) if t.islower() else ((i+1) % n, i)
        ends.setdefault(t.lower(), []).append((tail, head))
    for L, lst in ends.items():
        for (t0, h0) in lst[1:]:
            par[f(t0)] = f(lst[0][0]); par[f(h0)] = f(lst[0][1])
    vs = sorted(set(f(i) for i in range(n))); vid = {v: k for k, v in enumerate(vs)}
    d1 = [[0]*len(letters) for _ in vs]
    for j, L in enumerate(letters):
        t0, h0 = ends[L][0]
        d1[vid[f(h0)]][j] += 1; d1[vid[f(t0)]][j] -= 1
    d2 = [[0] for _ in letters]
    for t in toks:
        d2[letters.index(t.lower())][0] += 1 if t.islower() else -1
    return [len(vs), len(letters), 1], [None, d1, d2]

# ---------- 단체 복합체 ----------
def simplicial(tris):
    tris = [tuple(t) for t in tris]
    V = sorted(set(v for t in tris for v in t))
    E = sorted(set(tuple(sorted(e)) for t in tris for e in itertools.combinations(t, 2)))
    T = [tuple(sorted(t)) for t in tris]
    vi = {v: i for i, v in enumerate(V)}; ei = {e: i for i, e in enumerate(E)}
    d1 = [[0]*len(E) for _ in V]
    for j, (a, b) in enumerate(E): d1[vi[b]][j] += 1; d1[vi[a]][j] -= 1
    d2 = [[0]*len(T) for _ in E]
    for j, (a, b, c) in enumerate(T):
        d2[ei[(b, c)]][j] += 1; d2[ei[(a, c)]][j] -= 1; d2[ei[(a, b)]][j] += 1
    return V, E, T, [len(V), len(E), len(T)], [None, d1, d2]

def link_check(V, E, T):
    """각 꼭짓점의 링크가 하나의 원(사이클)인지, 각 변이 정확히 2개 삼각형에 속하는지."""
    ok = True; info = {}
    for e in E:
        c = sum(1 for t in T if set(e) <= set(t))
        if c != 2: ok = False; info.setdefault("bad_edges", []).append((e, c))
    for v in V:
        lk = [tuple(sorted(set(t) - {v})) for t in T if v in t]
        lv = set(x for e in lk for x in e)
        deg = {x: sum(1 for e in lk if x in e) for x in lv}
        # 연결성
        adj = {x: set() for x in lv}
        for a, b in lk: adj[a].add(b); adj[b].add(a)
        seen = set(); st = [next(iter(lv))] if lv else []
        while st:
            x = st.pop()
            if x in seen: continue
            seen.add(x); st += list(adj[x])
        # 꼭짓점이 1차원 변에만 속하는 경우도 체크
        is_circle = lv and all(d == 2 for d in deg.values()) and seen == lv
        if not is_circle: ok = False; info.setdefault("bad_vertices", []).append(v)
    return ok, info

def orientable(T):
    """삼각형들의 일관된 방향 존재 여부(BFS)."""
    T = [tuple(t) for t in T]
    ori = {0: T[0]}; q = [0]
    def edges(t): return [(t[0], t[1]), (t[1], t[2]), (t[2], t[0])]
    while q:
        i = q.pop()
        for (a, b) in edges(ori[i]):
            for j, t in enumerate(T):
                if j == i or not {a, b} <= set(t): continue
                c = (set(t) - {a, b}).pop()
                want = (b, a, c)  # 이웃은 공유변을 반대 방향으로
                if j in ori:
                    if set(edges(ori[j])) & {(a, b)}: return False
                else:
                    ori[j] = want; q.append(j)
    return True

def report(name, dims, bds):
    for k in range(2, len(dims)):
        assert is_zero(matmul(bds[k-1], bds[k])), f"{name}: ∂∂≠0"
    h = homology(dims, bds)
    chi = sum((-1)**k * d for k, d in enumerate(dims))
    print(f"{name:34s} cells={dims} χ={chi}  H(Z)={fmtZ(h['Z'])}  b(Q)={h['Q']}  b(Z2)={h['Z2']}")
    # 보편계수정리 검사: dim H_k(Z2) = b_k + t2_k + t2_{k-1}
    t2 = [sum(1 for d in tors if d % 2 == 0) for _, tors in h['Z']]
    for k in range(len(dims)):
        pred = h['Z'][k][0] + t2[k] + (t2[k-1] if k else 0)
        assert pred == h['Z2'][k], f"UCT 불일치 {name} k={k}"
        assert h['Z'][k][0] == h['Q'][k]
    return h

if __name__ == "__main__":
    print("== 1. 단어 대조 실험 (∂∂=0, UCT 자동 검사) ==")
    words = {"토러스 a b A B": "a b A B", "클라인 병 a b a B": "a b a B",
             "함정: a a B b (B b 상쇄→RP^2)": "a a B b", "클라인 병 a a b b (RP2#RP2)": "a a b b", "RP^2 a b a b": "a b a b",
             "RP^2 a a": "a a", "구 a A": "a A", "구 a b B A": "a b B A",
             "토러스(육각형) a b c A B C": "a b c A B C",
             "종수2 a b A B c d C D": "a b A B c d C D"}
    for nm, w in words.items():
        dims, bds = word_complex(w)
        print("  ∂1 =", bds[1], " ∂2 =", [r[0] for r in bds[2]])
        report(nm, dims, bds)

    print("\n== 4. 3x3 격자 삼각분할 (9 꼭짓점) ==")
    def grid(n):
        v = lambda i, j: (i % n) * n + (j % n)
        tris = []
        for i in range(n):
            for j in range(n):
                tris.append((v(i, j), v(i+1, j), v(i+1, j+1)))
                tris.append((v(i, j), v(i, j+1), v(i+1, j+1)))
        return tris
    tris = grid(3)
    V, E, T, dims, bds = simplicial(tris)
    print("서로 다른 삼각형 꼭짓점집합 수:", len(set(map(frozenset, tris))), "/", len(tris))
    print("링크 조건:", link_check(V, E, T), " 방향가능:", orientable(tris))
    h = report("3x3 격자 토러스", dims, bds)
    # 기본류: ∂2 의 핵 생성원
    # 방향 맞춘 삼각형 합이 사이클인지 확인
    # 주의: (i,j),(i+1,j),(i+1,j+1) 은 반시계, (i,j),(i,j+1),(i+1,j+1) 은 시계 방향 → 두번째 유형을 뒤집어야 일관됨
    ori = [t if k % 2 == 0 else (t[0], t[2], t[1]) for k, t in enumerate(tris)]
    naive = list(tris)
    vec = []
    for t in T:
        o = next(x for x in ori if tuple(sorted(x)) == t)
        # 순열 부호
        perm = [t.index(x) for x in o]; inv = sum(1 for i in range(3) for j in range(i+1, 3) if perm[i] > perm[j])
        vec.append((-1)**inv)
    bdry = [sum(bds[2][i][j]*vec[j] for j in range(len(T))) for i in range(len(E))]
    print("일관 방향 2-체인(유형1 - 유형2)의 경계 = 0 ? (기본류)", all(x == 0 for x in bdry))
    vec2 = []
    for t in T:
        o = next(x for x in naive if tuple(sorted(x)) == t)
        perm = [t.index(x) for x in o]; inv = sum(1 for i in range(3) for j in range(i+1, 3) if perm[i] > perm[j])
        vec2.append((-1)**inv)
    bd2 = [sum(bds[2][i][j]*vec2[j] for j in range(len(T))) for i in range(len(E))]
    print("함정: 코드에 적힌 순서 그대로 더한 2-체인의 경계 = 0 ?", all(x == 0 for x in bd2), " (0 아닌 성분 수", sum(1 for x in bd2 if x), ")")

    print("\n== 대조: 3x3 격자 클라인 병 (한 방향 접착에서 j -> -j) ==")
    def kgrid(n):
        def v(i, j):
            if i >= n: i -= n; j = -j
            return i * n + (j % n)
        tr = []
        for i in range(n):
            for j in range(n):
                tr.append((v(i, j), v(i+1, j), v(i+1, j+1)))
                tr.append((v(i, j), v(i, j+1), v(i+1, j+1)))
        return tr
    kt = kgrid(3)
    print("서로 다른 삼각형:", len(set(map(frozenset, kt))), "/", len(kt))
    Vk, Ek, Tk, dk, bk = simplicial(kt)
    print("링크 조건:", link_check(Vk, Ek, Tk), " 방향가능:", orientable(kt))
    report("3x3 격자 클라인 병", dk, bk)

    print("\n== 함정: 2x2 격자를 단체복합체로 착각 ==")
    t2 = grid(2)
    print("삼각형 꼭짓점집합 서로 다른 수:", len(set(map(frozenset, t2))), "/", len(t2))
    V, E, T, dims, bds = simplicial(t2)
    print("링크 조건:", link_check(V, E, T))
    report("2x2 격자를 단체로 축약(틀림)", dims, bds)

    print("\n== 7꼭짓점 뫼비우스(최소) 토러스 ==")
    t7 = [(i, (i+1) % 7, (i+3) % 7) for i in range(7)] + [(i, (i+2) % 7, (i+3) % 7) for i in range(7)]
    V, E, T, dims, bds = simplicial(t7)
    print("링크 조건:", link_check(V, E, T), " 방향가능:", orientable(t7))
    report("7꼭짓점 토러스", dims, bds)

    print("\n== 반례: 호몰로지는 토러스와 같지만 토러스가 아닌 S^1∨S^1∨S^2 ==")
    S2 = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    V, E, T, dims, bds = simplicial(S2)
    # 고리 두 개 (0-4-5-0), (0-6-7-0) 를 1-셀로 추가
    extraE = [(0, 4), (4, 5), (0, 5), (0, 6), (6, 7), (0, 7)]
    V2 = V + [4, 5, 6, 7]; E2 = E + extraE
    vi = {v: i for i, v in enumerate(V2)}; ei = {e: i for i, e in enumerate(E2)}
    d1 = [[0]*len(E2) for _ in V2]
    for j, (a, b) in enumerate(E2): d1[vi[b]][j] += 1; d1[vi[a]][j] -= 1
    d2 = [[0]*len(T) for _ in E2]
    for j, (a, b, c) in enumerate(T):
        d2[ei[(b, c)]][j] += 1; d2[ei[(a, c)]][j] -= 1; d2[ei[(a, b)]][j] += 1
    report("S^1∨S^1∨S^2", [len(V2), len(E2), len(T)], [None, d1, d2])
    print("  링크 조건:", link_check(V2, E2, T)[0], "(변 (0,4) 등이 삼각형 0개에 속함, 0의 링크=원+고립점4개) → 다양체 아님")

    print("\n== 함정: 부호 오류 ==")
    V, E, T, dims, bds = simplicial(grid(3))
    nosign = [[abs(x) for x in r] for r in bds[2]]
    print("부호 없는 ∂2 (모두 +1) 사용 시 ∂1∂2 = 0 ?", is_zero(matmul(bds[1], nosign)))
    print("  (Z/2 위에서는 ∂∂=0 이 되어버려 오류를 못 잡음:",
          all(x % 2 == 0 for r in matmul(bds[1], nosign) for x in r), ")")
    bad = [r[:] for r in bds[2]]; bad[0] = [-x for x in bad[0]]   # 변 하나 방향을 ∂2 에서만 뒤집음
    print("변 하나의 방향을 ∂2 에서만 뒤집으면 ∂1∂2 = 0 ?", is_zero(matmul(bds[1], bad)))
    good1 = [r[:] for r in bds[1]]
    for r in good1: r[0] = -r[0]
    print("∂1 의 같은 열도 함께 뒤집으면(일관된 재방향) ∂1∂2 = 0 ?", is_zero(matmul(good1, bad)))
    report("  일관되게 재방향한 토러스", dims, [None, good1, bad])
    random.seed(1)
    flip = [random.choice([1, -1]) for _ in T]
    d2f = [[bds[2][i][j]*flip[j] for j in range(len(T))] for i in range(len(E))]
    report("  삼각형 방향 무작위 뒤집기", dims, [None, bds[1], d2f])

    print("\n== 단체가 아닌 Δ-복합체: 2삼각형 토러스 (1꼭짓점, 3변) ==")
    # 꼭짓점 v, 변 a,b,c ; U=[v0v1v2] 경계 b - c + a  (Hatcher 2.1 표기), L 동일
    d1 = [[0, 0, 0]]
    d2 = [[1, 1], [1, 1], [-1, -1]]
    report("Δ-토러스 (Hatcher)", [1, 3, 2], [None, d1, d2])
    d2k = [[1, -1], [1, 1], [-1, -1]]  # 클라인 병 Δ (한 변 방향 반전 예시)
    print("  ∂1∂2 for Klein 시도:", matmul(d1, d2k))
    report("Δ-클라인병 시도", [1, 3, 2], [None, d1, d2k])
