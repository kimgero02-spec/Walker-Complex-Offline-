from ag import AG
from math import gcd
def theta(ps):
    arcs=[];n=2
    for p in ps:
        prev=0
        for i in range(p-1):
            arcs.append((prev,n)); prev=n; n+=1
        arcs.append((prev,1))
    return n,arcs
ok=True
for (a,b) in [(-2,1),(2,3),(-3,2),(-6,5),(5,-4),(1,1),(-1,1),(-2,-3)]:
    for ps in [(1,2,3),(2,3,4),(1,3,5),(2,2,5),(1,1,4),(2,2,2),(3,5,7),(1,4,4),(2,5,8)]:
        n,arcs=theta(ps); T,f=AG(n,arcs,a,b)
        p1=min(ps); d=0
        for p in ps: d=gcd(d,p-p1)
        N=abs(a**d-(-b)**d) if d>0 else 0
        pred=(abs(a*b)**p1)*N if d>0 else 0
        if d==0: good=(f==1 and T==[])
        else:
            prod=1
            for t in T: prod*=t
            good=(f==0 and prod==pred and len(T)<=1)
        if not good: ok=False; print("불일치",a,b,ps,T,f,pred)
print("세타(모두 u->v) 순환·위수 공식:",ok)
