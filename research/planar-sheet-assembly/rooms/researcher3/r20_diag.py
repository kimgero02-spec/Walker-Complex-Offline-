import random, sys
from r20_prism import *
k=int(sys.argv[1]); rng=random.Random(2)
A=[norm(e) for e in prism(k)]
cnt={'disj':0,'Asat':0,'Bsat':0}
good=[]
for s in range(20000):
    B=rand_label(k,rng)
    if set(A)&set(B): continue
    cnt['disj']+=1
    if not all(not planar(A+[e]) for e in B): continue
    cnt['Asat']+=1
    if all(not planar(B+[e]) for e in A): cnt['Bsat']+=1; good.append(B)
print(cnt)
# pairwise compatible good B's
import itertools
gs=[g for i,g in enumerate(good) if g not in good[:i]]
print(len(gs))
for B,C in itertools.combinations(gs,2):
    if set(B)&set(C): continue
    if frozen([A,B,C]): print("frozen pair"); break
else: print("no frozen pair")
