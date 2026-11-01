"""researcher2 표(d) 독립 재현: 2정점·2변 S^1 의 체인 텐서곱 T^n, 그리고 코쥘 부호 (-1)^p 를 빼먹는 함정."""
import itertools, numpy as np
from homology_check import snf_diag, rank_mod, matmul, is_zero
# S^1: C0 = <v,w>, C1 = <e,f>, ∂e = w - v, ∂f = v - w
S1 = {0: 2, 1: 2}; d = np.array([[-1, 1], [1, -1]])  # 행 v,w / 열 e,f
def tensor(n, sign=True):
    cells = {}
    for degs in itertools.product([0, 1], repeat=n):
        for idx in itertools.product([0, 1], repeat=n):
            cells.setdefault(sum(degs), []).append((degs, idx))
    pos = {k: {c: i for i, c in enumerate(v)} for k, v in cells.items()}
    bd = {}
    for k in range(1, n+1):
        M = [[0]*len(cells[k]) for _ in cells[k-1]]
        for j, (degs, idx) in enumerate(cells[k]):
            p = 0
            for t in range(n):
                if degs[t] == 1:
                    s = (-1)**p if sign else 1
                    for r in range(2):
                        c = d[r][idx[t]]
                        if c:
                            nd = degs[:t] + (0,) + degs[t+1:]; ni = idx[:t] + (r,) + idx[t+1:]
                            M[pos[k-1][(nd, ni)]][j] += s*c
                p += degs[t]
        bd[k] = M
    return [len(cells[k]) for k in range(n+1)], bd
for n in range(1, 5):
    for sign in (True, False):
        dims, bd = tensor(n, sign)
        dd = all(is_zero(matmul(bd[k-1], bd[k])) for k in range(2, n+1))
        if not dd:
            print(f"n={n} 부호 없음: ∂∂≠0 (함정 확인)"); continue
        res = []
        for k in range(n+1):
            r_out = rank_mod(bd[k]) if k >= 1 else 0
            r_in = rank_mod(bd[k+1]) if k < n else 0
            tors = [x for x in (snf_diag(bd[k+1]) if k < n else []) if x > 1]
            res.append((dims[k]-r_out-r_in, tors))
        print(f"n={n} sign={sign} cells={dims} H=", res)
