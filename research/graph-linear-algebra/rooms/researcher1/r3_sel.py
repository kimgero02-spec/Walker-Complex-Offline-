import random, itertools, sys
from fractions import Fraction as Fr
from r3lib import *
from r3_exp1 import sample_H
import sympy

def fmod2(x): return x % 2

def norm_vec(n, primes):
    """n integer -> bits (sign, e_p mod 2 for p in primes); returns None if other primes occur"""
    n = int(n)
    v = [1 if n < 0 else 0]
    n = abs(n)
    for p in primes:
        e = 0
        while n % p == 0: n //= p; e += 1
        v.append(e % 2)
    return v if n == 1 else None

class Local:
    def __init__(self, alg, p, nT=20, R=40, seed=11):
        self.alg, self.p = alg, p
        self.lam = alg.lam0()
        self.h1 = hasse(alg.gram(alg.one(), self.lam), p)
        self.T = sample_H(alg, p, nT, R, random.Random(seed))
        self.cache = {}
    def e(self, d):
        k = tuple(d)
        if k not in self.cache:
            self.cache[k] = hasse(self.alg.gram(d, self.lam), self.p) * self.h1
        return self.cache[k]
    def B(self, a, b):
        return self.e(self.alg.mul(a, b)) * self.e(a) * self.e(b)
    def sig(self, d):
        return tuple(self.B(d, t) for t in self.T)
    def kummer(self, K=6, J=2, rng=None):
        """set of signatures of Kummer image sampled"""
        alg, p = self.alg, self.p
        a1, a2, a3 = alg.a
        f = lambda t: t**3 + a1*t*t + a2*t + a3
        W = {tuple([1]*len(self.T)): [Fr(1), Fr(0), Fr(0)]}  # t0 = infinity -> delta=1
        pts = []
        if p == 0:
            import math
            for num in range(-60, 61):
                for den in (1, 2, 3, 4, 5, 7, 8):
                    pts.append(Fr(num, den))
        else:
            for j in range(0, J + 1):
                for a in range(0, p ** K):
                    pts.append(Fr(a, p ** j))
        for t0 in pts:
            v = 2 * f(t0)
            if v == 0: continue
            if not is_square_p(v, p): continue
            d = [2 * t0, Fr(-2), Fr(0)]
            s = self.sig(d)
            if s not in W: W[s] = d
        return W

def mulall(alg, els):
    r = alg.one()
    for e in els: r = alg.mul(r, [Fr(x) for x in e])
    return r

def selmer(f, gens, S, verbose=True, K2=7, K=None):
    alg = Alg(f)
    primes = S
    vecs = []
    for g in gens:
        n = alg.norm([Fr(x) for x in g])
        nv = norm_vec(n, primes)
        assert nv is not None, ("gen not S-unit", g, n)
        vecs.append(nv)
    k = len(gens)
    # H(S): combos with zero norm vector
    Hs = []
    for bits in itertools.product([0, 1], repeat=k):
        tot = [0] * (len(primes) + 1)
        for b, v in zip(bits, vecs):
            if b: tot = [(x + y) % 2 for x, y in zip(tot, v)]
        if not any(tot):
            els = [g for b, g in zip(bits, gens) if b]
            Hs.append((bits, mulall(alg, els)))
    if verbose: print("dim L(S,2) =", k, " |H(S)| =", len(Hs))
    places = [0] + list(primes)
    info = {}
    for v in places:
        Kv = K if K is not None else (8 if v == 2 else (5 if v in (3,) else 3))
        loc = Local(alg, v)
        W = loc.kummer(K=Kv)
        info[v] = (loc, W)
        if verbose: print(" place", v, "Kummer classes found:", len(W))
    rows = []
    for bits, d in Hs:
        row = {}
        for v in places:
            loc, W = info[v]
            # delta must lie in H_v (norm square) -- yes since N=square globally
            s = loc.sig(d)
            row[v] = (loc.e(d), s in W)
        rows.append((bits, d, row))
    return alg, Hs, rows, info

if __name__ == "__main__":
    pass
