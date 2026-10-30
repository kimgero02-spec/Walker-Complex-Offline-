# R24 researcher1: chromatic polynomials via independent-set partitions (a_i = #partitions into i independent sets).
# Values check / counterexample search only, not evidence.
import itertools, random

def partitions(elems):
    if not elems:
        yield []
        return
    first, rest = elems[0], elems[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i+1:]
        yield [[first]] + p

def ff_coeffs(V, E):
    Es = {frozenset(e) for e in E}
    a = [0] * (len(V) + 1)
    for p in partitions(list(V)):
        if all(frozenset((u, v)) not in Es for B in p for u, v in itertools.combinations(B, 2)):
            a[len(p)] += 1
    return a

def pmul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i + j] += x * y
    return r

def ff_to_mono(a):
    # x^(i) = x(x-1)...(x-i+1); coefficient lists low->high degree
    res = [0] * len(a)
    f = [1]
    for i, c in enumerate(a):
        for d, x in enumerate(f):
            res[d] += c * x
        f = pmul(f, [-i, 1])
    return res

def ev(p, x):
    return sum(c * x ** d for d, c in enumerate(p))

def chi_from_ff(a):
    return min(i for i, c in enumerate(a) if c)

def umbral(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r

# Gamma
A = ['w', 'a1', 'a2', 'a3', 'a4']; B = ['w', 'b1', 'b2', 'b3', 'b4']
V = ['w', 'a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4']
G = set()
for S in (A, B):
    for e in itertools.combinations(S, 2):
        G.add(frozenset(e))
G -= {frozenset(('w', 'a1')), frozenset(('w', 'b1'))}
G.add(frozenset(('a1', 'b1')))
P1 = {frozenset(e) for e in [('a1','a2'),('a1','a3'),('a1','a4'),('a1','b1'),('a2','w'),('a3','w'),('a4','w'),('b1','b2'),('b3','w'),('b4','w')]}
P2 = G - P1
print('|E|', len(G), len(P1), len(P2))
for name, E in [('Gamma', G), ('P1', P1), ('P2', P2)]:
    a = ff_coeffs(V, [tuple(e) for e in E])
    m = ff_to_mono(a)
    print(name, 'ff', a, 'chi', chi_from_ff(a), 'mono', m, 'vals', [ev(m, k) for k in range(7)])

def mono_str(p):
    return ' + '.join(f'{c}x^{d}' for d, c in enumerate(p) if c)

# closed forms
def prod(*ps):
    r = [1]
    for p in ps:
        r = pmul(r, p)
    return r
x = [0, 1]; xm = lambda c: [-c, 1]
closedG = prod(x, xm(1), xm(2), xm(2), xm(3), xm(3), xm(4), [6, -4, 1])
closedP1 = prod(x, xm(1), xm(1), xm(1), xm(1), xm(1), [-7, 10, -5, 1])
closedP2 = prod(x, x, x, xm(1), xm(1), xm(1), xm(2), xm(2), xm(2))
for name, E, c in [('Gamma', G, closedG), ('P1', P1, closedP1), ('P2', P2, closedP2)]:
    print(name, 'closed form matches:', ff_to_mono(ff_coeffs(V, [tuple(e) for e in E])) == c)

# Hajos bilinear formula check: P(G1 hajos G2) = (k-2)/(k(k-1)) Q1Q2 + (Q1R2+R1Q2)/k, for K5,K5 at integer k
from fractions import Fraction
def K(n): return prod(*[xm(i) for i in range(n)])
Q = K(5); R = K(4)
for k in range(2, 9):
    lhs = ev(closedG, k)
    rhs = Fraction(k - 2, k * (k - 1)) * ev(Q, k) ** 2 + Fraction(2 * ev(Q, k) * ev(R, k), k)
    assert lhs == rhs, (k, lhs, rhs)
print('Hajos bilinear formula OK for K5,K5 at k=2..8')

# join of restrictions J = G[V1] + G[V2]
V1 = ['w', 'a1', 'b1']; V2 = [v for v in V if v not in V1]
EV1 = [tuple(e) for e in G if e <= set(V1)]; EV2 = [tuple(e) for e in G if e <= set(V2)]
a1 = ff_coeffs(V1, EV1); a2 = ff_coeffs(V2, EV2)
aJ = umbral(a1, a2)
aG = ff_coeffs(V, [tuple(e) for e in G])
print('G[V1] ff', a1, 'G[V2] ff', a2, 'J ff', aJ, 'chi(J)', chi_from_ff(aJ))
print('aG - aJ', [x - y for x, y in zip(aG, aJ)])
print('P(Gamma,k) vs P(J,k):', [(k, ev(ff_to_mono(aG), k), ev(ff_to_mono(aJ), k)) for k in range(4, 8)])
