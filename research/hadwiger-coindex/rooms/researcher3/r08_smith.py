# R08 researcher3: Smith-type test. sigma(x)=2x mod 5 on K_5 (order 4, swaps C5 and its complement); sigma^2 = -x.
# Fixed set of sigma^2 on |B_0(K5)| = order complex of sigma^2-invariant faces (chains of invariant faces).
import sys, itertools
sys.path.insert(0, "/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3")
from r06_lib import make, B0_empty, reduced_betti

def chains_fixed(n, E, perm):
    F = B0_empty(make(n, E), n)
    faces = [f for k in F for f in F[k] if f]
    inv = [f for f in faces if tuple(sorted(perm[x] for x in f)) == f]
    S = set(inv)
    # order complex on invariant faces (proper chains)
    chains = {0: [(f,) for f in inv]}
    k = 0
    cur = [(f,) for f in inv]
    allc = {0: cur}
    while True:
        nxt = []
        for c in allc[k]:
            top = c[-1]
            for g in inv:
                if len(g) > len(top) and set(top) <= set(g):
                    nxt.append(c + (g,))
        if not nxt: break
        k += 1
        allc[k] = nxt
    # convert to simplicial complex with vertices = faces; reduced_betti expects sorted tuples of ids -> relabel
    idx = {f: i for i, f in enumerate(inv)}
    out = {d: sorted(tuple(idx[f] for f in c) for c in allc[d]) for d in allc}
    return out, len(inv)

n = 5
E = list(itertools.combinations(range(5), 2))
# vertices of B0: copy1 i -> i, copy2 i -> n+i. sigma(v)=2v mod 5 on each copy, sigma^2(v)=-v mod 5 (as v -> 4v)
perm2 = {}
for x in range(10):
    c, v = (0, x) if x < n else (1, x-n)
    w = (4*v) % 5
    perm2[x] = w + c*n
out, nf = chains_fixed(n, E, perm2)
print("invariant faces under sigma^2:", nf)
print("fixed-set dims (chains):", {d: len(v) for d, v in out.items()})
b = reduced_betti(out)
print("reduced betti of Fix(sigma^2) (F_p, p=10007):", {k: v for k, v in b.items() if v})
