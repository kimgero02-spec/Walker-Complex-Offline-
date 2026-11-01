import random
from ag import AG
random.seed(11)
for trial in range(14):
    n=random.randint(4,9)
    arcs=[]
    for v in range(1,n):
        u=random.randrange(v); arcs.append((u,v) if random.random()<.5 else (v,u))
    ind=[0]*n; outd=[0]*n
    for u,v in arcs: outd[u]+=1; ind[v]+=1
    S=sum(1 for i in range(n) if ind[i]==0); K=sum(1 for i in range(n) if outd[i]==0)
    T,f=AG(n,arcs,-2,1); T3,f3=AG(n,arcs,-6,1)
    print(arcs,"원천",S,"싱크",K,"| a=-2,b=1:",T,f,"| a=-6,b=1:",T3,f3)
