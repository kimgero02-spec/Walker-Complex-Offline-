"""R23-2: falsification attempts (not proof) for Theorem 1.2: (star)(G1△G2) <=> (star)(G1-e1) and (star)(G2-e2); plus Gamma sums."""
from r23_star import *
import random, networkx as nx
random.seed(11)
def rnd(n,p):
    while True:
        E=[(i,j) for i in range(n) for j in range(i+1,n) if random.random()<p]
        g=nx.Graph(E)
        if g.number_of_nodes()==n and nx.is_connected(g): return E
agree=0; dis=0; both=[0,0]
for it in range(500):
    E1=rnd(random.randint(5,8),random.uniform(.5,.95)); E2=rnd(random.randint(5,8),random.uniform(.5,.95))
    A1=adj_from_edges(E1);A2=adj_from_edges(E2)
    x1=random.choice(list(A1)); y1=random.choice(list(A1[x1])); x2=random.choice(list(A2)); y2=random.choice(list(A2[x2]))
    lhs = star_witness(adj_from_edges(hajos(E1,x1,y1,E2,x2,y2))) is None
    def minus(E,x,y): 
        F=[e for e in E if set(e)!={x,y}]; A=adj_from_edges(F)
        for v in {v for e in E for v in e}: A.setdefault(v,set())
        return A
    rhs = star_witness(minus(E1,x1,y1)) is None and star_witness(minus(E2,x2,y2)) is None
    both[lhs]+=1
    if lhs==rhs: agree+=1
    else: dis+=1; print('DISAGREE',E1,(x1,y1),E2,(x2,y2),lhs,rhs)
print('agree',agree,'disagree',dis,'(star) false/true counts',both)

# Gamma_m construction (R22-1 3.1) and Gamma_m △ Gamma_m' iso Gamma_{m+m'}
def Gm(m):
    E=set()
    for i in range(1,m+1):
        Q=['w']+[f'x{i}_{q}' for q in range(1,5)]
        for a in range(5):
            for b in range(a+1,5): E.add(tuple(sorted((Q[a],Q[b]))))
        if i>=2: E.discard(tuple(sorted(('w',f'x{i}_1'))))
        if i<=m-1: E.discard(tuple(sorted(('w',f'x{i}_2'))))
    for i in range(1,m): E.add(tuple(sorted((f'x{i}_2',f'x{i+1}_1'))))
    return sorted(E)
for m,mp in [(2,2),(2,3),(3,3)]:
    S=hajos(Gm(m),'w','x1_1',Gm(mp),'w','x1_1')  # remove w-x1_1 in first copy... 
    print(m,mp,nx.is_isomorphic(nx.Graph(S),nx.Graph(Gm(m+mp))))
