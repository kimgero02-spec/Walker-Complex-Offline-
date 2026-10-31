# K8 종수 2 매장을 찾고, 4+4 분할 중 관 구조 (종수 2 = 관 3 개) 가 되는 것이 있는지 확인
from r49_tube import *
import itertools
G=nx.complete_graph(8)
found=0
for s in range(40):
    g,rot=free_genus_search(G,iters=80000,seed=s,target=2)
    if g>2: continue
    for T in itertools.combinations(range(8),4):
        if 0 not in T: continue
        t=tube_info(rot,T)
        if t['bad']==0 and t['g1']==0 and t['g2']==0:
            print('seed',s,'V1',T,t); found+=1; break
    if found: break
print('found',found)
