"""Search for odd maps B(G)->S^1 given by vertex angles (linear on simplices):
every maximal simplex A|B needs {alpha_a} u {alpha_b + pi} inside an open half circle.  Grid search with backtracking."""
import sys, itertools, networkx as nx
from r04 import chain, maximal_simplices_B

def semicircle_ok(angs, N):
    # angles in Z_N (grid); open half circle: exists rotation where all lie in an arc of length < N/2
    a = sorted(set(x % N for x in angs))
    if len(a) <= 1: return True
    gaps = [(a[(i + 1) % len(a)] - a[i]) % N for i in range(len(a))]
    return max(gaps) > N / 2   # complement arc > half  <=> points in an arc < half

def search(G, N=24):
    V = sorted(G.nodes()); S = list(maximal_simplices_B(G))
    order = V
    alpha = {}
    def ok_partial():
        for A, B in S:
            pts = [alpha[a] for a in A if a in alpha] + [alpha[b] + N // 2 for b in B if b in alpha]
            if not semicircle_ok(pts, N): return False
        return True
    def bt(i):
        if i == len(order): return True
        v = order[i]
        for x in (range(1) if i == 0 else range(N)):
            alpha[v] = x
            if ok_partial() and bt(i + 1): return True
            del alpha[v]
        return False
    return dict(alpha) if bt(0) else None

if __name__ == "__main__":
    for m in (7, 8, 10, 11):
        G, T, c = chain(m, [3] * m)
        for N in (12, 24, 48):
            r = search(G, N)
            print(f"C_{m}^2 grid {N}: {'found ' + str(r) if r else 'none'}"); sys.stdout.flush()
            if r: break
