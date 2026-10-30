# r20_tf12_out.txt 검산: K_12 의 4장 분해, 각 장 (3,2) 평면 => Delta=4=N/3.
import ast, itertools, networkx as nx
from r19_lib import chi, omega
L=open('r20_tf12_out.txt').read().splitlines(); Es=ast.literal_eval(L[1])
P=[nx.Graph(E) for E in Es]
for G in P: G.add_nodes_from(range(12))
cnt={}
for G in P:
    for e in G.edges(): cnt[frozenset(e)]=cnt.get(frozenset(e),0)+1
print("정확:",set(cnt)==set(frozenset(e) for e in itertools.combinations(range(12),2)) and all(c==1 for c in cnt.values()))
print("평면:",[nx.check_planarity(G)[0] for G in P],"chi:",[chi(G) for G in P],"omega:",[omega(G) for G in P])
