# K6=K3+K3, K7=K4+K3, K8=K4+K4 의 관 종수 상계 (관 매장 찾기) 와 자유 종수
from r49_tube import *
def join(a,b):
    G=nx.complete_graph(a+b); return G, list(range(a))
for (a,b,tgt) in [(3,3,1),(4,3,1),(4,4,2)]:
    G,V1=join(a,b)
    res=None
    for m in (False,True):
        for s in range(6):
            c,t,rot=tube_search(G,V1,iters=60000,seed=s,mirror2=m,target=tgt)
            if res is None or c<res[0]: res=(c,t,m,s)
            if c<=tgt: break
        if res[0]<=tgt: break
    print('K%d=K%d+K%d'%(a+b,a,b),'best cost',res[0],res[1],'mirror',res[2],'seed',res[3])
