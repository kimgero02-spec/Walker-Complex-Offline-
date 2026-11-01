import sys,random,itertools
sys.path.insert(0,'.')
from r4_blowup import *
def cn2(n,k=2):
    G=nx.Graph(); G.add_nodes_from(range(n))
    for i in range(n):
        for d in range(1,k+1): G.add_edge(i,(i+d)%n)
    return G
def rep(name,G,ms,order=None,tries=0):
    G=nx.convert_node_labels_to_integers(G); V,idx,nb,T=types2(G); n=len(V); w=omega(G)
    o0=list(range(n)) if order is None else order
    res=[]
    for m in ms:
        v,_=Dsigma(n,T,o0,m); bst=v
        for _ in range(tries):
            o=list(range(n)); random.shuffle(o)
            bst=min(bst,Dsigma(n,T,o,m)[0])
        res.append((m,v+1,bst+1,m*w))
    print(f"{name}: n={n} omega={w} 타입={len(T)}  (m, 자연순서 상계 tau<=, 무작위30 최선, m*omega)", res)
random.seed(1)
for n in range(7,13): rep(f"C_{n}^2",cn2(n),[1,2,3,4],tries=30)
for n in (9,10): rep(f"C_{n}^3",cn2(n,3),[1,2,3,4],tries=30)
rep("Petersen",nx.petersen_graph(),[1,2,3],tries=5)
# 사다리, 격자, K33 : 이분 순서 vs 나쁜 순서
L=nx.ladder_graph(5); rep("ladder(5) 자연(층별)",L,[1,2,3],tries=0)
bip=nx.bipartite.sets(L); order=sorted(L.nodes(),key=lambda v:(v not in bip[0],v))
G=nx.convert_node_labels_to_integers(L); 
V,idx,nb,T=types2(G); n=len(V)
print("ladder 이분 순서:",[(m,Dsigma(n,T,[idx[v] for v in order],m)[0]+1) for m in (1,2,3)])
rep("K_{3,3}-자연(이분 순서)",nx.complete_bipartite_graph(3,3),[1,2,3])
