# 반례 탐색(구성용): 평면 3-색 P 에서 '모든 독립 삼중쌍 비무지개' 4-색칠이 없는 것 찾기
import random, sys
from r04_lib import *
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 0)
def rand_planar(n, dens):
    P = nx.empty_graph(n); E = list(itertools.combinations(range(n),2)); random.shuffle(E)
    for u,v in E:
        if random.random() > dens: continue
        P.add_edge(u,v)
        if not nx.check_planarity(P)[0]: P.remove_edge(u,v)
    return P
found = 0
for it in range(4000):
    n = random.randint(7,11)
    P = rand_planar(n, random.uniform(0.3,1.0))
    if not nx.is_connected(P) or chi(P) != 3: continue
    T = [t for t in itertools.combinations(P.nodes(),3) if indep(P,t)]
    if col_ok(P, T) is None:
        print('FOUND', n, P.number_of_edges(), sorted(P.edges())); found += 1
        if found > 3: break
print('done', it)
