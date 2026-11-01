# 개선된 국소 탐색 (면 수 최대화, 온도 재시작). K8 로 보정 (종수 2 를 찾아야 함) 후 U 에 적용.
from r49_tube import *
import itertools, random, math
def anneal(G, target, restarts=30, iters=150000, seed=0):
    rnd=random.Random(seed); best=10**9
    darts=[(a,b) for a in G for b in G[a]]
    for rs in range(restarts):
        rot={v:list(G[v]) for v in G}
        for v in rot: rnd.shuffle(rot[v])
        F=len(faces(rot)); T=1.5
        for it in range(iters):
            v=rnd.choice(list(G)); L=rot[v]
            if len(L)<3: continue
            i,j=rnd.sample(range(len(L)),2); L[i],L[j]=L[j],L[i]
            F2=len(faces(rot))
            if F2>=F or rnd.random()<math.exp((F2-F)/T): F=F2
            else: L[i],L[j]=L[j],L[i]
            T=max(0.08,T*0.9999)
            g=(2-len(G)+G.number_of_edges()-F)//2
            if g<best: best=g
            if best<=target: return best,rot
    return best,None
K8=nx.complete_graph(8)
print('K8:',anneal(K8,2,restarts=10)[0])
p,q,r,s,P,Q_,R=range(7); v1,v2,v3,v4=7,8,9,10
U=nx.Graph()
U.add_edges_from(itertools.combinations([p,q,r,s],2))
U.add_edges_from([(P,q),(P,r),(P,s),(Q_,p),(Q_,r),(Q_,s),(R,p),(R,q),(R,s)])
U.add_edges_from(itertools.combinations([v1,v2,v3,v4],2))
U.add_edges_from([(v1,p),(v2,q),(v3,r),(v4,P),(v4,Q_),(v4,R)])
g,rot=anneal(U,1,restarts=30)
print('U best genus',g)
if rot: print('rotation',rot,'tube_info',tube_info(rot,range(7)))
