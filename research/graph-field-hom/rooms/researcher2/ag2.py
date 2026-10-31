import random
from math import gcd
from ag import AG, snf_diag
random.seed(7)
def walk_lengths(n,arcs,s,maxL=14):
    L=[set() for _ in range(n)]; cur={s}; L[s].add(0)
    for l in range(1,maxL+1):
        nxt=set()
        for (u,v) in arcs:
            if u in cur: nxt.add(v)
        for v in nxt: L[v].add(l)
        cur=nxt
    return L
def predicted(n,arcs,s,lam):
    L=walk_lengths(n,arcs,s); D=0
    for v in range(n):
        Lv=sorted(L[v]); m=Lv[0]; g=0
        for l in Lv: g=gcd(g,l-m)
        if g==0: continue
        D=gcd(D, abs(lam)**m*abs(lam**g-1) if lam**g!=1 else 0)
    return D
bad=0;tot=0
for trial in range(400):
    n=random.randint(2,7)
    # 유일한 원천 0, 모두 0에서 도달 가능
    arcs=[]
    for v in range(1,n): arcs.append((random.randrange(v),v))
    for _ in range(random.randint(0,3)):
        u=random.randrange(n); v=random.randrange(1,n); arcs.append((u,v))
    lam=random.choice([2,3,-2,4,6,5,-3])
    T,f=AG(n,arcs,-lam,1)   # b=1, a=-lam : x_head = lam x_tail
    D=predicted(n,arcs,0,lam)
    # A 는 순환 Z/D (D=0이면 Z)
    if D==0: good=(T==[] and f==1)
    elif D==1: good=(T==[] and f==0)
    else: good=(T==[D] and f==0)
    tot+=1
    if not good: bad+=1; print("불일치",n,arcs,lam,T,f,D)
print("단일원천 b=1 순환 공식:",tot-bad,"/",tot)
