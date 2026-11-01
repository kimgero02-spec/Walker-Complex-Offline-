# K7 원환면 삼각분할 (회전 i -> i+1,i+3,i+2,i+6,i+4,i+5) 에서 V1 = 3 점 집합의 관 구조 확인
from r49_tube import *
import itertools
for off in itertools.permutations([1,2,3,4,5,6]):
    if off[0]!=1: continue
    rot={i:[(i+o)%7 for o in off] for i in range(7)}
    if genus(rot)==1: break
print('rotation offsets',off,'genus',genus(rot))
F=[frozenset(a for a,b in w) for w in faces(rot)]
print('faces',len(F))
ok=[];
for T in itertools.combinations(range(7),3):
    t=tube_info(rot,T)
    ok.append((frozenset(T) in F, t['bad'], t['curves'], t['g1'], t['g2']))
from collections import Counter
print(Counter(ok))
