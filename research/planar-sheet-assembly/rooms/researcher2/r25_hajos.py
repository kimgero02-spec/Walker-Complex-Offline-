# 하요시 구성 (합 + 비인접 동일화) 으로 만든 chi>=4 그래프에서 S4 반례 (어려운 쌍) 탐색. 반례 찾기 전용.
import random, itertools, networkx as nx, sys
from r25_hard import k4free, chi, hard, ident
random.seed(int(sys.argv[1]))
def relabel(G,t): return nx.relabel_nodes(G,{x:(t,x) for x in G})
base=[nx.complete_graph(4)]+[nx.wheel_graph(m) for m in (6,8)]+[nx.mycielski_graph(4)]
def hsum(G1,G2):
    G1=relabel(G1,1); G2=relabel(G2,2)
    x1,y1=random.choice(list(G1.edges())); x2,y2=random.choice(list(G2.edges()))
    G=nx.union(G1,G2); G=nx.contracted_nodes(G,x1,x2,self_loops=False)
    G.remove_edge(x1,y1); G.remove_edge(x1,y2); G.add_edge(y1,y2)
    return nx.convert_node_labels_to_integers(G)
tested=0
for t in range(300):
    G=random.choice(base).copy()
    for s in range(random.randint(1,3)):
        if random.random()<0.6 and G.number_of_nodes()<10:
            G=hsum(G,random.choice(base[:3]))
        else:
            non=[(a,b) for a,b in itertools.combinations(G,2) if not G.has_edge(a,b)]
            if non:
                a,b=random.choice(non); G=nx.convert_node_labels_to_integers(ident(G,a,b))
    if G.number_of_nodes()>12: continue
    assert chi(G)>=4
    tested+=1
    for u,v in itertools.combinations(G,2):
        if G.has_edge(u,v): continue
        if hard(G,u,v):
            print("HARD",sorted(G.edges()),u,v); sys.exit()
print("no hard pair; graphs:",tested)
