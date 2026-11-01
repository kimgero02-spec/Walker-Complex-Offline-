# R3 researcher1: epsilon quadratic form tools. Exact rational arithmetic.
from fractions import Fraction as Fr
import random, itertools
from math import gcd

def vp(n, p):
    n = int(n)
    if n == 0: raise ValueError
    c = 0
    while n % p == 0:
        n //= p; c += 1
    return c

def split_rat(a, p):
    """a nonzero Fraction -> (alpha, u) a = p^alpha * u, u p-adic unit rational (num,den ints)"""
    a = Fr(a)
    al = vp(a.numerator, p) - vp(a.denominator, p)
    u = a / Fr(p) ** al
    return al, u

def unit_mod(u, m):
    return (u.numerator * pow(u.denominator, -1, m)) % m

def hilbert(a, b, p):
    """Hilbert symbol (a,b)_p in {+1,-1}; p=0 means real place."""
    a = Fr(a); b = Fr(b)
    if p == 0:
        return -1 if (a < 0 and b < 0) else 1
    al, u = split_rat(a, p); be, v = split_rat(b, p)
    if p == 2:
        um = unit_mod(u, 8); vm = unit_mod(v, 8)
        e = lambda x: ((x - 1) // 2) % 2
        w = lambda x: ((x * x - 1) // 8) % 2
        ex = (e(um) * e(vm) + al * w(vm) + be * w(um)) % 2
        return -1 if ex else 1
    def leg(x):
        x %= p
        return 1 if pow(x, (p - 1) // 2, p) == 1 else -1
    r = 1
    if (al * be) % 2 and p % 4 == 3: r = -r
    if be % 2: r *= leg(unit_mod(u, p))
    if al % 2: r *= leg(unit_mod(v, p))
    return r

def is_square_p(a, p):
    a = Fr(a)
    if a == 0: return True
    if p == 0: return a > 0
    al, u = split_rat(a, p)
    if al % 2: return False
    if p == 2: return unit_mod(u, 8) == 1
    return pow(unit_mod(u, p), (p - 1) // 2, p) == 1

def diagonalize(G):
    """symmetric Fraction matrix (list of lists) -> list of diagonal entries (congruent form)."""
    n = len(G)
    G = [[Fr(x) for x in r] for r in G]
    diag = []
    idx = list(range(n))
    cur = G
    while len(cur) > 0:
        m = len(cur)
        # find nonzero diagonal
        piv = None
        for i in range(m):
            if cur[i][i] != 0: piv = i; break
        if piv is None:
            # find nonzero offdiag
            found = None
            for i in range(m):
                for j in range(m):
                    if cur[i][j] != 0: found = (i, j); break
                if found: break
            if not found:
                diag += [Fr(0)] * m; break
            i, j = found
            # replace e_i by e_i+e_j
            for k in range(m): cur[i][k] += cur[j][k]
            for k in range(m): cur[k][i] += cur[k][j]
            piv = i
        d = cur[piv][piv]
        diag.append(d)
        rest = [k for k in range(m) if k != piv]
        new = [[cur[a][b] - cur[a][piv] * cur[piv][b] / d for b in rest] for a in rest]
        cur = new
    return diag

def hasse(G, p):
    d = diagonalize(G)
    assert all(x != 0 for x in d)
    s = 1
    for i in range(len(d)):
        for j in range(i + 1, len(d)):
            s *= hilbert(d[i], d[j], p)
    return s

# ---- etale cubic algebra Q[t]/f ----
class Alg:
    def __init__(self, f):
        # f = [a1,a2,a3] monic t^3+a1 t^2+a2 t+a3
        self.f = [Fr(x) for x in f]
        a1, a2, a3 = self.f
        self.a = (a1, a2, a3)
    def mul(self, x, y):
        a1, a2, a3 = self.a
        c = [Fr(0)] * 5
        for i in range(3):
            for j in range(3):
                c[i + j] += x[i] * y[j]
        # reduce t^4, t^3
        for k in (4, 3):
            co = c[k]; c[k] = Fr(0)
            # t^k = t^{k-3} * t^3 = t^{k-3}(-a1 t^2 - a2 t - a3)
            c[k - 1] -= a1 * co; c[k - 2] -= a2 * co; c[k - 3] -= a3 * co
        return c[:3]
    def one(self): return [Fr(1), Fr(0), Fr(0)]
    def th(self): return [Fr(0), Fr(1), Fr(0)]
    def mat(self, x):
        cols = []
        basis = [[Fr(1), 0, 0], [0, Fr(1), 0], [0, 0, Fr(1)]]
        for b in basis:
            cols.append(self.mul(x, [Fr(t) for t in b]))
        return [[cols[j][i] for j in range(3)] for i in range(3)]
    def tr(self, x):
        M = self.mat(x); return M[0][0] + M[1][1] + M[2][2]
    def norm(self, x):
        M = self.mat(x)
        return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1]) - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0]) + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
    def inv(self, x):
        M = self.mat(x)
        import sympy
        S = sympy.Matrix(3, 3, lambda i, j: sympy.Rational(M[i][j].numerator, M[i][j].denominator))
        sol = S.LUsolve(sympy.Matrix([1, 0, 0]))
        return [Fr(int(s.p), int(s.q)) for s in sol]
    def fprime(self):
        a1, a2, a3 = self.a
        th = self.th(); th2 = self.mul(th, th)
        return [a2 + 0, 2 * a1 + 0, Fr(3)] and [a2 + Fr(0), 2*a1, Fr(3)]  # 3t^2+2a1 t + a2
    def fprime_el(self):
        a1, a2, a3 = self.a
        return [a2, 2 * a1, Fr(3)]
    def lam0(self):
        return [-2 * c for c in self.inv(self.fprime_el())]
    def gram(self, delta, lam=None):
        if lam is None: lam = self.lam0()
        c = self.mul(lam, delta)
        pw = [self.one(), self.th(), self.mul(self.th(), self.th())]
        return [[self.tr(self.mul(c, self.mul(pw[i], pw[j]))) for j in range(3)] for i in range(3)]

def eps(alg, delta, p, lam=None, base=None):
    G = alg.gram(delta, lam)
    G1 = base if base is not None else alg.gram(alg.one(), lam)
    return hasse(G, p) * hasse(G1, p)

def disc_cubic(f):
    a, b, c = [Fr(x) for x in f]
    return a*a*b*b - 4*b**3 - 4*a**3*c - 27*c*c + 18*a*b*c
