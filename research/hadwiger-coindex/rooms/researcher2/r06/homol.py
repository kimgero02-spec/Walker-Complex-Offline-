# R06 반례꾼: GF(2) 호몰로지. 복합체는 면 리스트 (정렬된 정점 튜플의 집합).
from itertools import combinations
def rank_gf2(rows):
    # rows: list of ints (bitsets)
    piv = {}
    r = 0
    for x in rows:
        while x:
            h = x.bit_length()-1
            if h in piv: x ^= piv[h]
            else:
                piv[h] = x; r += 1; break
    return r

def betti_gf2(faces):
    """faces: set of frozensets (nonempty). returns reduced Betti numbers over GF(2) (dict dim->b), dim -1 = empty face."""
    by = {}
    for f in faces:
        by.setdefault(len(f)-1, []).append(tuple(sorted(f)))
    maxd = max(by) if by else -1
    idx = {d: {f: i for i, f in enumerate(sorted(by[d]))} for d in by}
    ranks = {}
    for d in range(0, maxd+1):
        # boundary d -> d-1 ; rows indexed by d-simplices as bitsets over (d-1)-simplices
        if d == 0:
            # augmentation: each vertex -> empty face (index 0 in dim -1)
            rows = [1 for _ in by[0]]
            ranks[d] = rank_gf2(rows)
            continue
        rows = []
        for f in by.get(d, []):
            x = 0
            for i in range(len(f)):
                g = f[:i]+f[i+1:]
                x |= 1 << idx[d-1][g]
            rows.append(x)
        ranks[d] = rank_gf2(rows)
    betti = {}
    for d in range(-1, maxd+1):
        n_d = len(by.get(d, [])) if d >= 0 else 1
        rk_out = ranks.get(d, 0) if d >= 0 else 0
        rk_in = ranks.get(d+1, 0)
        betti[d] = n_d - rk_out - rk_in
    return {d: b for d, b in betti.items() if b}

def neighborhood_complex(n, adj):
    faces = set()
    for v in range(n):
        nb = [u for u in range(n) if adj[v] >> u & 1]
        for k in range(1, len(nb)+1):
            for S in combinations(nb, k): faces.add(frozenset(S))
    return faces

def box_complex_empty(n, adj):
    """X(G): 면 = (A,B) 의 원소 (A,copy1)∪(B,copy2) 로 인코딩, 정점 v -> (v,1)=v, (v,2)=n+v; A×B ⊆ E."""
    faces = set()
    full = (1<<n)-1
    def common(mask):
        r = full; k = 0
        while mask:
            if mask & 1: r &= adj[k]
            mask >>= 1; k += 1
        return r
    for A in range(0, 1<<n):
        C = common(A) if A else full
        # B 는 C 의 부분집합 (B 는 A 와 상호 완전)
        sub = C
        while True:
            B = sub
            vs = [v for v in range(n) if A>>v&1] + [n+v for v in range(n) if B>>v&1]
            if vs: faces.add(frozenset(vs))
            if sub == 0: break
            sub = (sub-1) & C
    return faces
