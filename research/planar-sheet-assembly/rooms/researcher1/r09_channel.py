# R09 researcher1: channel decomposition for the K4 3-ring with base junction S={1,2} (size 2).
# T = N2 N3 N1 in End_{S_q}(V^{⊗2}); P = Tr T = sum over S_q-isotypic channels lambda of tr(T E_lambda).
import itertools, math
from fractions import Fraction

def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0:
        yield {}
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n-k, k):
            d = dict(rest); d[k] = d.get(k, 0) + 1
            yield d

def brute_T(q):
    # T[x,y] = sum_{x3,x4} N2(x,x4) N3(x4,x3) N1(x3,y), x=(x1,x2), y=(y1,y2)
    pairs = list(itertools.product(range(q), repeat=2))
    idx = {p: i for i, p in enumerate(pairs)}
    T = [[0]*len(pairs) for _ in pairs]
    for x in pairs:
        for y in pairs:
            if y[0] == y[1]:
                continue
            s = 0
            for x3 in range(q):
                if x3 == y[0] or x3 == y[1]:
                    continue
                for x4 in range(q):
                    if x4 == x[0] or x4 == x[1] or x4 == x3:
                        continue
                    s += 1
            T[idx[x]][idx[y]] = s
    return pairs, T

def cycle_types(q):
    for p in partitions(q):
        yield p

def class_size(q, ct):
    z = 1
    for l, m in ct.items():
        z *= l**m * math.factorial(m)
    return math.factorial(q) // z

def perm_on_pairs_matrix(q, ct):
    # build a permutation sigma with cycle type ct on range(q)
    sigma = list(range(q)); pos = 0
    for l in sorted(ct, reverse=True):
        for _ in range(ct[l]):
            cyc = list(range(pos, pos+l))
            for i in range(l):
                sigma[cyc[i]] = cyc[(i+1) % l]
            pos += l
    return sigma

def channel_values(q):
    pairs, T = brute_T(q)
    n = len(pairs)
    idx = {p: i for i, p in enumerate(pairs)}
    tot = {'triv': 0, 'std': 0, 'q-2,2': 0, 'q-2,1,1': 0}
    trace_T = sum(T[i][i] for i in range(n))
    G = math.factorial(q)
    res = {}
    for ct in cycle_types(q):
        sig = perm_on_pairs_matrix(q, ct)
        # tau = tr(T P(sigma)) ; P(sigma) e_x = e_{sigma x}
        tau = 0
        for x in pairs:
            sx = (sig[x[0]], sig[x[1]])
            # (T P)[x,x] = sum_y T[x,y] P[y,x], P[y,x]=1 iff y = sigma(x)... use P e_x = e_{sx}
            # tr(T P) = sum_x (T P)_{xx} = sum_x T[x, sigma^{-1}... ] ; compute directly
            pass
        # direct: P matrix M[y][x] = 1 if y == sx; tr(T M) = sum_{x,y} T[x][y] M[y][x] = sum_x T[x][sx]
        tau = sum(T[idx[x]][idx[(sig[x[0]], sig[x[1]])]] for x in pairs)
        f = ct.get(1, 0)
        t = ct.get(2, 0)
        chars = {
            'triv': 1,
            'std': f - 1,
            'q-2,2': math.comb(f, 2) + t - f,
            'q-2,1,1': ((f-1)**2 - (f + 2*t - 1)) // 2,
        }
        dims = {
            'triv': 1, 'std': q-1,
            'q-2,2': q*(q-3)//2, 'q-2,1,1': (q-1)*(q-2)//2,
        }
        cs = class_size(q, ct)
        for k in tot:
            tot[k] += Fraction(cs * chars[k] * tau, 1)
    out = {}
    for k in tot:
        out[k] = Fraction(dims[k], G) * tot[k]
    return out, trace_T

if __name__ == "__main__":
    for q in range(1, 9):
        out, tr = channel_values(q)
        s = sum(out.values())
        print(q, "trace=", tr, "sum_channels=", s, {k: str(v) for k, v in out.items()})
