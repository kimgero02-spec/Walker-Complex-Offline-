# 무작위 4-임계 그래프에서 어려운 경우 (모든 K4 모형이 u,v 를 가름) 찾기. 반례 탐색용.
import random, itertools, networkx as nx, sys
from r25_hard import k4free, chi, hard
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 0)
def critical(G,k=4):
    G=G.copy(); es=list(G.edges()); random.shuffle(es)
    for e in es:
        G.remove_edge(*e)
        if chi(G)<k: G.add_edge(*e)
    G.remove_nodes_from([x for x in list(G) if G.degree(x)==0])
    return G
cnt=0
for trial in range(4000):
    n=random.randint(8,11); p=random.uniform(0.3,0.6)
    G=nx.gnp_random_graph(n,p,seed=random.randint(0,10**9))
    if chi(G)<4: continue
    C=critical(G)
    cnt+=1
    for u,v in itertools.combinations(C.nodes(),2):
        if C.has_edge(u,v): continue
        if hard(C,u,v):
            print("HARD",C.number_of_nodes(),sorted(C.edges()),u,v); sys.exit()
print("none; critical graphs tested:",cnt)
