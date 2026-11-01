import sys, itertools; sys.path.insert(0,'/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3')
from r06_lib import *
K=lambda n: list(itertools.combinations(range(n),2))
K33=[(i,3+j) for i in range(3) for j in range(3)]
def induced(n,E,S):
    m={v:i for i,v in enumerate(S)}
    return len(S),[(m[u],m[v]) for u,v in E if u in m and v in m]
cases=[("K5",5,K(5),[[0,1,2,3],[4]]),("K5",5,K(5),[[0,1],[2,3,4]]),
       ("K6",6,K(6),[[0,1,2,3],[4,5]]),("K6",6,K(6),[[0,1,2],[3,4,5]]),
       ("K33",6,K33,[[0,1,2],[3,4,5]]),("K33",6,K33,[[0,1,3],[2,4,5]])]
for nm,n,E,parts in cases:
    z=zig(make(n,E),n)
    zs=[]
    for S in parts:
        m,Ei=induced(n,E,S); zs.append(max(1,zig(make(m,Ei),m)) if m>0 else 0)
    print(nm,parts,"zig(G)=",z,"block zigs=",zs,"sum=",sum(zs),"ok" if z<=sum(zs) else "VIOLATION", flush=True)
