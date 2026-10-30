import networkx as nx, itertools
from r19_lib import *
# 1. R18-2 Ex 5.2 : T = C5 + {50,52}
T=nx.cycle_graph(5); T.add_edges_from([(5,0),(5,2)])
report(6,[T,nx.complement(T)],"K6 T u Tbar")
# 2. K7 = (C5 + K2) u (C5' join 2K1)   [Op B on K5 = C5 u C5']
P=nx.cycle_graph(5); P.add_edge(5,6)
Q=nx.Graph(); Q.add_edges_from([(i,(i+2)%5) for i in range(5)]); Q.add_edges_from([(a,i) for a in (5,6) for i in range(5)])
report(7,[P,Q],"K7 OpB")
print(" Q == complement(P):", nx.is_isomorphic(Q,nx.complement(P)) and set(map(frozenset,Q.edges()))==set(map(frozenset,nx.complement(P).edges())))
# 3. Op A: pair addition  D on K_N -> K_{N+2}
def opA(N,pieces,recv):
    x,y=N,N+1
    new=[P.copy() for P in pieces]
    new[recv].add_edge(x,y)
    B=nx.Graph(); B.add_edges_from([(u,v) for u in (x,y) for v in range(N)])
    return N+2,new+[B]
N,D=6,[T,nx.complement(T)]
for _ in range(3):
    N,D=opA(N,D,0); report(N,D,"OpA from K6")
N,D=7,[P,Q]
for _ in range(3):
    N,D=opA(N,D,0); report(N,D,"OpA from K7")
# 4. Z_2^3 Cayley decomposition refuting Pi2
els=list(itertools.product([0,1],repeat=3))
idx={v:i for i,v in enumerate(els)}
add=lambda u,v: tuple((a+b)%2 for a,b in zip(u,v))
def cay(S):
    G=nx.Graph(); G.add_nodes_from(range(8))
    for g in els:
        for s in S: G.add_edge(idx[g],idx[add(g,s)])
    return G
a,b,c=(1,0,0),(0,1,0),(0,0,1)
ab=add(a,b); ca=add(c,a); cb=add(c,b); cab=add(ca,b)
pieces=[cay([a,b,ab]), cay([c,ca,cb]), cay([cab])]
report(8,pieces,"Z2^3 Cayley")
# 5. K4 x K2 nonplanar ; 4-subsets of Z2^3 Cayley planar?
print("K4xK2 planar:",planar(nx.cartesian_product(nx.complete_graph(4),nx.complete_graph(2))))
nz=[v for v in els if any(v)]
print("planar Cayley with |S|=4:",[S for S in itertools.combinations(nz,4) if planar(cay(S))])
