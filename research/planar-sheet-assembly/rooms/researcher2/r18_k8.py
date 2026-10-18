# K8 = T u Tbar, both planar, chi(T)+chi(Tbar)=8 ? (예 하나를 찾는 구성 탐색, 근거 아님)
import networkx as nx, random
from r18_sum import chi
random.seed(18)
E=[(i,j) for i in range(8) for j in range(i+1,8)]
best=None
for trial in range(20000):
    random.shuffle(E)
    T=nx.empty_graph(8)
    for e in E:
        T.add_edge(*e)
        if not nx.check_planarity(T)[0]: T.remove_edge(*e)
    # T maximal planar (18 edges); complement has 10 edges
    Tb=nx.complement(T)
    if not nx.check_planarity(Tb)[0]: continue
    a,b=chi(T),chi(Tb)
    if best is None or a+b>best[0]:
        best=(a+b,a,b,sorted(T.edges()))
    if a+b==8: break
print(best)
