# pendant-triangle sheet: core K4 a,b,c,d ; each core v has triangle T_v, v adjacent to all of T_v
from lib import *
def sheet(t):
    B=nx.Graph(); core=[f'{t}{c}' for c in 'abcd']
    B.add_edges_from(itertools.combinations(core,2)); W=[]
    for v in core:
        T=[f'{v}_{i}' for i in range(3)]; W+=T
        B.add_edges_from(itertools.combinations(T,2)); B.add_edges_from((v,u) for u in T)
    return B,W
B,W=sheet('L')
print("planar",nx.check_planarity(B)[0],"n",B.number_of_nodes(),"chi(B[W])=3 (4 disjoint triangles)")
for q in (6,7):
    for k in (3,4):
        ok=colorable(B,q,allowed={w:set(range(k)) for w in W})
        print(f"q={q}: W within {k} colours ->",ok is not None)
B2,W2=sheet('R'); G=nx.union(B,B2); G.add_edges_from((u,v) for u in W for v in W2)
print("G n,m",G.number_of_nodes(),G.number_of_edges(),"max cross deg",len(W2))
for q in (6,7): print("chi<=",q,colorable(G,q) is not None)
