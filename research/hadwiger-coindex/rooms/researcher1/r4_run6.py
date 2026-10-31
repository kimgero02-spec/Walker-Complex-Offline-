import sys,random,itertools
sys.path.insert(0,'.')
from r4_blowup import *
random.seed(11)
def randtf(n,p):
    G=nx.Graph(); G.add_nodes_from(range(n))
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]; random.shuffle(pairs)
    for i,j in pairs:
        if random.random()<p and not (set(G[i])&set(G[j])): G.add_edge(i,j)
    return G
def ls(n,T,m,restarts=3,iters=300):
    best=10**9
    for _ in range(restarts):
        o=list(range(n)); random.shuffle(o); cur=Dsigma(n,T,o,m)[0]
        for _ in range(iters):
            i,j=random.sample(range(n),2); o2=o[:]; o2[i],o2[j]=o2[j],o2[i]
            v=Dsigma(n,T,o2,m)[0]
            if v<=cur: o,cur=o2,v
        best=min(best,cur)
    return best
hits=[]
for trial in range(300):
    n=random.choice([8,9]); G=randtf(n,0.7)
    if nx.is_bipartite(G) or omega(G)!=2: continue
    V,idx,nb,T=types2(G)
    v=ls(n,T,2)+1
    if v>4: hits.append((v,sorted(G.edges())))
print(len(hits))
hits.sort(key=lambda x:-x[0])
for h in hits[:3]: print(h)
