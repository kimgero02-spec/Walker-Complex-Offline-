# 추측 R5 의 반례 구성 탐색: 평면 L, 독립 삼중쌍 T 에서 5-색칠 무지개 불가인 것
import random, sys
from r04_lib import *
from r04_m4 import rainbow_possible
random.seed(int(sys.argv[1]))
for it in range(int(sys.argv[2])):
    n=random.randint(7,int(sys.argv[3])); L=nx.empty_graph(n)
    E=list(itertools.combinations(range(n),2)); random.shuffle(E)
    for u,v in E:
        L.add_edge(u,v)
        if not nx.check_planarity(L)[0]: L.remove_edge(u,v)
    for t in itertools.combinations(L.nodes(),3):
        if indep(L,t) and not rainbow_possible(L,t):
            print('COUNTER', t, sorted(L.edges())); sys.exit()
print('none')
