# Check chi(X) <= chi(X/T) + chi(X[T]) - 1 on random small graphs (T any vertex subset, quotient identifies T).
import itertools, random
def chi(V, E):
    V = list(V)
    for q in range(1, len(V)+1):
        for col in itertools.product(range(q), repeat=len(V)):
            c = dict(zip(V, col))
            if all(c[a] != c[b] for a,b in map(tuple,E)):
                return q
    return 0
def quotient(V, E, T):
    z = ('z',)
    V2 = [v for v in V if v not in T] + [z]
    E2 = set()
    for a,b in map(tuple,E):
        fa = z if a in T else a; fb = z if b in T else b
        if fa != fb: E2.add(frozenset({fa,fb}))
    return V2, E2
rng = random.Random(1); bad = 0; tight = 0; n = 0
for _ in range(150):
    nv = rng.randint(2,6)
    V = list(range(nv))
    E = set(frozenset(p) for p in itertools.combinations(V,2) if rng.random()<0.5)
    if not E: continue
    T = set(v for v in V if rng.random()<0.5)
    if len(T) < 1: continue
    V2,E2 = quotient(V,E,T)
    ET = set(e for e in E if e <= T)
    lhs = chi(V,E); rhs = chi(V2,E2) + chi(T,ET) - 1
    n += 1
    if lhs > rhs: bad += 1; print("VIOLATION", V,E,T)
    if lhs == rhs: tight += 1
print("cases", n, "violations", bad, "equality cases", tight)
# K_n with T = n-q+1 vertices: equality
for N in range(3,7):
    V = list(range(N)); E = set(frozenset(p) for p in itertools.combinations(V,2))
    T = set(range(N-1))   # contract a clique of size N-1
    V2,E2 = quotient(V,E,T)
    print("K%d, T of size %d: chi=%d chi(X/T)=%d chi(X[T])=%d" % (N, N-1, chi(V,E), chi(V2,E2), chi(T, set(e for e in E if e<=T))))
