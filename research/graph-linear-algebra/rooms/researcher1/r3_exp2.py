import sys, random
from r3_exp1 import *

def run(f, p, R=25, nS=400, nT=24, seed=3, ntri=300):
    alg, classes, res, bad, e, B, T = analyze(f, p, nT=nT, nS=nS, R=R, seed=seed)
    ker = sum(1 for s in res if res[s] == 1)
    S = sample_H(alg, p, 120, R, random.Random(seed+5))
    rng = random.Random(9)
    nonbil = 0; nonalt = 0
    for _ in range(ntri):
        a, b, c = rng.choice(S), rng.choice(S), rng.choice(S)
        bc = alg.mul(b, c)
        if B(a, bc) != B(a, b) * B(a, c): nonbil += 1
        if B(a, a) != 1: nonalt += 1
        # symmetric
        if B(a, b) != B(b, a): nonalt += 1
    return len(classes), ker, bad, nonbil, nonalt

if __name__ == "__main__":
    f = eval(sys.argv[1]); p = int(sys.argv[2])
    R = int(sys.argv[3]) if len(sys.argv) > 3 else 25
    print("f", f, "p", p, "(#classes, ker, inconsistent, nonbilinear, nonalternating) =", run(f, p, R=R))
