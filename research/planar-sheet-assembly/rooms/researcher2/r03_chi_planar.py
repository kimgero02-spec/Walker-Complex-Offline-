# E6': E6 와 같은 G 를 평면 조각(정규화, 나무형 접합, 접합 크기<=4)으로
import itertools, networkx as nx
from r03_chi import chi, g, union, K113, G6
W = g([('a','b'),('b','c'),('c','a'),('x','b'),('x','c'),('y','a'),('y','c'),('z','a'),('z','b')], nodes=['p','q','r'])
Pp = g([('a','b'),('x','b'),('y','a'),('p','a'),('p','b'),('p','x'),('p','y')])
Pq = g([('a','c'),('x','c'),('z','a'),('q','a'),('q','c'),('q','x'),('q','z')])
Pr = g([('b','c'),('y','c'),('z','b'),('r','b'),('r','c'),('r','y'),('r','z')])
K1 = K113(('x','y','z'),'h'); K2 = K113(('p','q','r'),'k')
pieces = {'C':W,'Pp':Pp,'Pq':Pq,'Pr':Pr,'K1':K1,'K2':K2}
tree = [('C','Pp'),('C','Pq'),('C','Pr'),('C','K1'),('C','K2')]  # 별 모양 H
G = union(*pieces.values())
print("G 가 E6 와 같은가:", nx.utils.graphs_equal(G, G6) if hasattr(nx.utils,'graphs_equal') else (set(map(frozenset,G.edges()))==set(map(frozenset,G6.edges())) and set(G)==set(G6)))
for a,b in tree:
    S = set(pieces[a]) & set(pieces[b])
    GS = G.subgraph(S)
    norm = all(pieces[a].has_edge(*e) and pieces[b].has_edge(*e) for e in GS.edges())
    print(f"접합 {a}-{b}: S={sorted(S)} |S|={len(S)} G[S] 변={sorted(map(sorted,GS.edges()))} 정규화={norm}")
# 나무 분해 조건: 두 조각이 공유하는 점은 나무 경로 위 모든 조각에 있다 (별이므로 중심 C 에 있으면 충분)
names=list(pieces)
ok=all((set(pieces[u])&set(pieces[v]))<=set(W) for u,v in itertools.combinations(names,2) if 'C' not in (u,v))
print("나무 분해 조건(잎끼리 공유 ⊆ 중심):", ok)
for k,P in pieces.items(): print(k, "chi", chi(P), "평면", nx.check_planarity(P)[0])
print("chi(G) =", chi(G))
