from t3 import *
for name,adj,n in [("K3",K3,3),("C4",C4,4)]:
    ps=aut_perms(n,adj); d,U=comm_units(n,ps,3)
    for m in (1,2):
        print(name,len(ps),d,len(U),"m",m,orbits(n,m,3,U))
# elimination game fill
def fill(n,edges,order):
    adj={i:set() for i in range(n)}
    for a,b in edges: adj[a].add(b);adj[b].add(a)
    pos={v:i for i,v in enumerate(order)};f=0
    for v in order:
        later=[w for w in adj[v] if pos[w]>pos[v]]
        for a in later:
            for b in later:
                if a<b and b not in adj[a]: adj[a].add(b);adj[b].add(a);f+=1
    return f
import itertools
star=[(0,i) for i in range(1,5)]
print("star K1,4 center first",fill(5,star,[0,1,2,3,4]),"center last",fill(5,star,[1,2,3,4,0]))
c4=[(0,1),(1,2),(2,3),(3,0)]
print("C4 fill per order:",sorted({fill(4,c4,o) for o in itertools.permutations(range(4))}))
p4=[(0,1),(1,2),(2,3)]
print("P4 orders fill set:",sorted({fill(4,p4,o) for o in itertools.permutations(range(4))}), "fill 1 order [1,2,0,3]:",fill(4,p4,[1,2,0,3]))
c5=[(i,(i+1)%5) for i in range(5)]
print("C5 min fill",min(fill(5,c5,o) for o in itertools.permutations(range(5))))
print("K4",fill(4,[(i,j) for i in range(4) for j in range(i)],[0,1,2,3]), "empty",fill(4,[],[0,1,2,3]))
