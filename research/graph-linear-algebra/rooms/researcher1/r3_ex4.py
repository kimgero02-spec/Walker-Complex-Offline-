import sys, math
from r3_sel import *
from r3_exp1 import sample_H

def hdim(loc, nS=400, R=30):
    alg, p = loc.alg, loc.p
    S = sample_H(alg, p, nS, R, random.Random(5))
    cl = set(loc.sig(d) for d in S)
    return len(cl), cl

def local_report(f, p, K, nS=400):
    alg = Alg(f)
    loc = Local(alg, p, nT=24, R=30, seed=21)
    ncl, cl = hdim(loc, nS)
    W = loc.kummer(K=K, J=1)
    # all W classes in cl? isotropy checks
    els = list(W.values())
    eW = [loc.e(d) for d in els]
    pair_ok = all(loc.B(a, b) == 1 for a in els for b in els)
    return dict(p=p, H=ncl, W=len(W), eps_on_W=set(eW), Bzero=pair_ok)

if __name__ == "__main__":
    f = eval(sys.argv[1]); p = int(sys.argv[2]); K = int(sys.argv[3])
    print(local_report(f, p, K))
