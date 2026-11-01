import random
from r3_exp1 import *
from fractions import Fraction as Fr

def leg_p(x, p): return 1 if pow(x % p, (p-1)//2, p) == 1 else -1

def hilbert_K(b1, b2, p, D):
    """Hilbert symbol in K=Q_p(sqrt D), p odd, D squarefree int, D nonsquare in Q_p. b=(x,y)=x+y sqrt D."""
    ram = (D % p == 0)
    def val_unit(b):
        x, y = Fr(b[0]), Fr(b[1])
        if ram:
            vx = vp_f(x, p) * 2 if x != 0 else 10**9
            vy = vp_f(y, p) * 2 + 1 if y != 0 else 10**9
            v = min(vx, vy)
            # u = b / pi^v, pi = sqrt D ; residue in F_p
            if v % 2 == 0:
                u = x / Fr(D) ** (v // 2)       # real part
            else:
                u = y / Fr(D) ** ((v - 1) // 2)
            return v, ('p', unit_mod(u, p))
        else:
            vx = vp_f(x, p) if x != 0 else 10**9
            vy = vp_f(y, p) if y != 0 else 10**9
            v = min(vx, vy)
            xx = x / Fr(p) ** v; yy = y / Fr(p) ** v
            return v, ('q', unit_mod(xx, p), unit_mod(yy, p))
    v1, u1 = val_unit(b1); v2, u2 = val_unit(b2)
    if ram:
        q = p
        a = u1[1]; b = u2[1]
        val = ((-1) ** (v1 * v2)) * pow(a, v2, q) * pow(b, -v1, q) % q
        return leg_p(val, p)
    else:
        # F_{p^2} = F_p[s]/(s^2 - D)
        def mul(u, w): return ((u[0]*w[0] + D*u[1]*w[1]) % p, (u[0]*w[1] + u[1]*w[0]) % p)
        def pw(u, e):
            r = (1, 0); base = u
            if e < 0:
                # inverse: conj / norm
                nrm = (u[0]*u[0] - D*u[1]*u[1]) % p
                inv = (u[0]*pow(nrm, -1, p) % p, (-u[1])*pow(nrm, -1, p) % p)
                base = inv; e = -e
            while e:
                if e & 1: r = mul(r, base)
                base = mul(base, base); e >>= 1
            return r
        a = (u1[1], u1[2]); b = (u2[1], u2[2])
        t = mul(pw(a, v2), pw(b, -v1))
        t = ((((-1) ** (v1 * v2)) * t[0]) % p, (((-1) ** (v1 * v2)) * t[1]) % p)
        r = pw(t, (p*p - 1)//2)
        assert r[1] == 0 and r[0] in (1, p-1)
        return 1 if r[0] == 1 else -1

def vp_f(x, p):
    x = Fr(x)
    return vp(x.numerator, p) - vp(x.denominator, p)

def test_split(f, roots, p, n=300, R=25, seed=1):
    alg = Alg(f); rng = random.Random(seed)
    S = sample_H(alg, p, 80, R, rng)
    lam = alg.lam0(); h1 = hasse(alg.gram(alg.one(), lam), p)
    e = lambda d: hasse(alg.gram(d, lam), p) * h1
    bad = 0; tot = 0
    def ev(d, r): return d[0] + d[1]*r + d[2]*r*r
    for _ in range(n):
        a, b = rng.choice(S), rng.choice(S)
        B = e(alg.mul(a, b)) * e(a) * e(b)
        W = 1
        for r in roots: W *= hilbert(ev(a, Fr(r)), ev(b, Fr(r)), p)
        tot += 1; bad += (B != W)
    return tot, bad

def test_12(f, r, D, p, n=300, R=40, seed=1):
    """f=(t-r)(t^2-s t+nn) with disc of quadratic = D*square, D squarefree. here f=[a1,a2,a3] given."""
    alg = Alg(f); rng = random.Random(seed)
    S = sample_H(alg, p, 80, R, rng)
    lam = alg.lam0(); h1 = hasse(alg.gram(alg.one(), lam), p)
    e = lambda d: hasse(alg.gram(d, lam), p) * h1
    a1, a2, a3 = [Fr(x) for x in f]
    # quadratic factor t^2 + (a1 + r) t + c with c = -a3/r ... compute by division
    r = Fr(r)
    s1 = a1 + r            # t^2 + s1 t + c0
    c0 = a2 + r * s1
    disc = s1*s1 - 4*c0    # = D * sq
    # sqrt(disc) = k sqrt D
    k2 = disc / D
    import math
    kn = Fr(math.isqrt(int(k2.numerator)), math.isqrt(int(k2.denominator)))
    assert kn*kn == k2, (disc, D)
    k = kn
    bad = 0
    for _ in range(n):
        a, b = rng.choice(S), rng.choice(S)
        B = e(alg.mul(a, b)) * e(a) * e(b)
        def comp(d):
            # K: t = (-s1 + k sqrt D)/2
            tx = -s1/2; ty = k/2
            # t^2 = tx^2 + D ty^2 + 2 tx ty sqrtD
            t2x = tx*tx + D*ty*ty; t2y = 2*tx*ty
            return (d[0] + d[1]*tx + d[2]*t2x, d[1]*ty + d[2]*t2y)
        def ev(d): return d[0] + d[1]*r + d[2]*r*r
        W = hilbert(ev(a), ev(b), p) * hilbert_K(comp(a), comp(b), p, D)
        bad += (B != W)
    return n, bad

if __name__ == "__main__":
    for p in (3, 5, 2, 0):
        print("split t^3-4t p", p, test_split([0, -4, 0], [0, 2, -2], p, n=200))
    print("split t^3-7t+6 (roots 1,2,-3)", [ (p,test_split([0,-7,6],[1,2,-3],p,n=150)) for p in (3,5,7,0)])
    for p in (5, 7, 3, 11):
        print("(1)(2) t^3-3t, K=Q(sqrt3), p", p, test_12([0, -3, 0], 0, 3, p))
    for p in (5,7,3):
        print("(1)(2) t(t^2-2) K=Q(sqrt 2) p", p, test_12([0,-2,0], 0, 2, p))
    for p in (5, 7, 11, 13):
        print("(1)(2) (t-1)(t^2+1) -> t^3 - t^2 + t - 1, K=Q(i), p", p, test_12([-1,1,-1], 1, -1, p))
