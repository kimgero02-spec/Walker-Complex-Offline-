from r48_at import *
import networkx as nx, itertools
W5=nx.wheel_graph(6); E=list(W5.edges())
def nonzero_ts(n,E,cap):
    out=[]
    for t in itertools.product(range(cap+1),repeat=n):
        if sum(t)==len(E):
            c=coef_brute(n,E,list(t))
            if c: out.append((t,c))
    return out
nzW=nonzero_ts(6,E,3); print('W5 nonzero t (cap3):',nzW[:6], len(nzW))
# 공식 검증
for t,c in nzW[:4]: print('formula',t,coef(6,E,list(t)),c)
B1=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
nzK=nonzero_ts(4,B1,3); print('K4',nzK[:4])
B2=[(4+u,4+v) for u,v in E]
H=[(0,5),(1,5),(2,5),(1,6),(2,6),(3,6),(0,7),(3,7),(2,8),(3,9),(0,9),(1,9)]
dH={v:0 for v in range(10)}
for u,v in H: dH[u]+=1; dH[v]+=1
G=B1+B2+H
for (t1,c1) in nzK[:2]:
  for (t2,c2) in nzW[:3]:
    t=list(t1)+[t2[i]+dH[4+i] for i in range(6)]
    cG=coef(10,G,t)
    print(t1,t2,'c1',c1,'c2',c2,'cG',cG,'cG/(c1c2)',cG/(c1*c2))
