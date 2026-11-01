import random, sys
from r3lib import *

_fac_cache = {}
def fac_mod(alg, p):
    key = (tuple(alg.a), p)
    if key not in _fac_cache:
        import sympy
        t = sympy.symbols('t')
        a1, a2, a3 = alg.a
        P = sympy.Poly(t**3 + int(a1)*t**2 + int(a2)*t + int(a3), t, modulus=p)
        fl = P.factor_list()[1]
        _fac_cache[key] = [[int(c) % p for c in reversed(g.all_coeffs())] for g, e in fl]
    return _fac_cache[key]

def sample_H(alg, p, n, R=6, rng=None):
    rng = rng or random.Random(1)
    out = []
    tries = 0
    while len(out) < n and tries < 400000:
        tries += 1
        d = [Fr(rng.randint(-R, R)) for _ in range(3)]
        r = rng.random()
        if p > 1 and r < 0.6:
            facs = fac_mod(alg, p)
            g = rng.choice(facs)           # coefficients low->high, monic
            g3 = [Fr(c) for c in g] + [Fr(0)] * (3 - len(g))
            gg = alg.mul(g3, [Fr(rng.randint(-R, R)) for _ in range(3)]) if len(g) < 4 else g3
            d = [gg[i] + p * rng.randint(-R, R) for i in range(3)]
            if rng.random() < 0.5:
                g2 = rng.choice(facs); g23 = [Fr(c) for c in g2] + [Fr(0)] * (3 - len(g2))
                d = alg.mul(d, [g23[i] + p * rng.randint(-2, 2) for i in range(3)])
        elif r < 0.8:
            for _ in range(rng.randint(1, 2)):
                a = rng.randint(-40, 40)
                d = alg.mul(d, [Fr(-a), Fr(1), Fr(0)])
        N = alg.norm(d)
        if N == 0: continue
        if not is_square_p(N, p): continue
        out.append(d)
    return out

def analyze(f, p, nT=14, nS=500, R=7, seed=1):
    alg = Alg(f)
    lam = alg.lam0()
    base = alg.gram(alg.one(), lam)
    h1 = hasse(base, p)
    rng = random.Random(seed)
    S = sample_H(alg, p, nS, R, rng)
    ev = {}
    def e(d):
        k = tuple(d)
        if k not in ev: ev[k] = hasse(alg.gram(d, lam), p) * h1
        return ev[k]
    T = S[:nT] if nT <= len(S) else S
    # use independent test set (random) to build signatures
    T = sample_H(alg, p, nT, R, random.Random(seed + 77))
    def B(d1, d2):
        return e(alg.mul(d1, d2)) * e(d1) * e(d2)
    def sig(d):
        return tuple(B(d, t) for t in T)
    classes = {}
    for d in S:
        classes.setdefault(sig(d), []).append(d)
    # epsilon per class (should be well-defined)
    bad = 0
    res = {}
    for s, ds in classes.items():
        vals = set(e(d) for d in ds)
        if len(vals) > 1: bad += 1
        res[s] = e(ds[0])
    return alg, classes, res, bad, e, B, T

if __name__ == "__main__":
    f = eval(sys.argv[1]); p = int(sys.argv[2])
    alg, classes, res, bad, e, B, T = analyze(f, p)
    n = len(classes)
    ker = sum(1 for s in res if res[s] == 1)
    print("f", f, "p", p, "#classes", n, "ker", ker, "inconsistent classes", bad)
