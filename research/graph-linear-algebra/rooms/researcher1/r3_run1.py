import sys
from r3_exp1 import *
f = eval(sys.argv[1]); p = int(sys.argv[2]); R=int(sys.argv[3]); nS=int(sys.argv[4]); nT=int(sys.argv[5])
alg, classes, res, bad, e, B, T = analyze(f, p, nT=nT, nS=nS, R=R)
ker = sum(1 for s in res if res[s] == 1)
print("f", f, "p", p, "#classes", len(classes), "ker", ker, "inconsistent", bad)
