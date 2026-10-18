import sys, time
sys.path.insert(0,'.')
from graphs import *
from exactsep import *
# 정합성: 2D 결과와 SAT 판정 비교 (C5 R^2 feasible 기대, K4 R^2 infeasible, K4 R^3 feasible)
K4 = from_edges(4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)])
K5 = from_edges(5, [(i,j) for i in range(5) for j in range(i+1,5)])
print('K4 R^3 search:', anneal_d(*K4, 3, 3, 3000, 1)[0])
print('K4 R^2 search:', anneal_d(*K4, 2, 3, 3000, 1)[0])
print('K5 R^3 search (expect >0):', anneal_d(*K5, 3, 3, 3000, 1)[0])
print('K5 R^4 search (expect 0):', anneal_d(*K5, 4, 3, 6000, 2)[0])
print('C5 R^2:', anneal_d(*cycle(5), 2, 3, 3000, 1)[0])
