# R09 researcher1: m=2 ring test with uniform junction size s=2 for K4.
# P1 = C4 on (1,3,2,4) [edges 13,32,24,41], P2 = matching {12,34}; S_1={1,2}, S_2={3,4}.
# T(x,x') = sum_y N2(x,y) N1(y,x') in End_{S_q}(V^{⊗2}); P = Tr T = proper colorings of K4.
import itertools, math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r09_channel import class_size, cycle_types, perm_on_pairs_matrix
from fractions import Fraction

def channels_from_T(q, T, pairs):
    idx = {p: i for i, p in enumerate(pairs)}
    G = math.factorial(q)
    out = {'triv': 0, 'std': 0, 'q-2,2': 0, 'q-2,1,1': 0}
    for ct in cycle_types(q):
        sig = perm_on_pairs_matrix(q, ct)
        tau = sum(T[idx[x]][idx[(sig[x[0]], sig[x[1]])]] for x in pairs)
        f = ct.get(1, 0); t = ct.get(2, 0)
        chars = {'triv': 1, 'std': f-1, 'q-2,2': math.comb(f, 2)+t-f,
                 'q-2,1,1': ((f-1)**2-(f+2*t-1))//2}
        cs = class_size(q, ct)
        for k in out:
            out[k] += cs * chars[k] * tau
    dims = {'triv': 1, 'std': q-1, 'q-2,2': q*(q-3)//2, 'q-2,1,1': (q-1)*(q-2)//2}
    return {k: Fraction(dims[k]*out[k], G) for k in out}

def build(q):
    pairs = list(itertools.product(range(q), repeat=2))
    N1 = lambda y, x: int(x[0] != y[0] and y[0] != x[1] and x[1] != y[1] and y[1] != x[0])
    N2 = lambda x, y: int(x[0] != x[1] and y[0] != y[1])
    T = [[sum(N2(x, y) * N1(y, xp) for y in pairs) for xp in pairs] for x in pairs]
    tr = sum(T[i][i] for i in range(len(pairs)))
    return pairs, T, tr

if __name__ == "__main__":
    for q in range(2, 9):
        pairs, T, tr = build(q)
        ch = channels_from_T(q, T, pairs)
        print(q, "Tr=", tr, "K4 proper count=", q*(q-1)*(q-2)*(q-3), {k: str(v) for k, v in ch.items()}, "sum=", sum(ch.values()))
