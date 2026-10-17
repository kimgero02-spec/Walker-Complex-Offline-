"""Generate closed K_c-chains (circular-arc model) with lifetimes in a window, by backtracking over departures."""
import random, itertools
from r04 import chain, holonomy, sign

def cycle_type(g):
    seen = [False] * len(g); t = []
    for i in range(len(g)):
        if not seen[i]:
            L = 0; j = i
            while not seen[j]: seen[j] = True; j = g[j]; L += 1
            t.append(L)
    return tuple(sorted(t, reverse=True))

def gen(m, c, lo, hi, rng, tries=2000):
    for _ in range(tries):
        ell = [None] * m; used = set(); ok = True
        order = list(range(m))
        def bt(j, tot):
            if j == m: return tot == c * m
            rem = m - j
            if tot + rem * lo > c * m or tot + rem * hi < c * m: return False
            opts = list(range(lo, hi + 1)); rng.shuffle(opts)
            for l in opts:
                d = (j + l) % m
                if d in used: continue
                used.add(d); ell[j] = l
                if bt(j + 1, tot + l): return True
                used.discard(d)
            return False
        if bt(0, 0):
            try:
                G, T, cc = chain(m, ell)
            except AssertionError:
                continue
            if cc == c: return ell
    return None

def find(c, m, ctype, lo, hi, seed=0, tries=300):
    rng = random.Random(seed)
    for t in range(tries):
        ell = gen(m, c, lo, hi, rng)
        if ell is None: continue
        G, T, cc = chain(m, ell)
        g = holonomy(m, ell, T, cc)
        if cycle_type(g) == ctype: return ell
    return None
