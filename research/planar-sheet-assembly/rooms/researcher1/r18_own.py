# 예 몇 개에서 소유 분할(G[V_k] ⊆ P_k)과 접합 분할(교차 완전 + chi(G[V_k])=chi(P_k)) 존재 확인
import itertools
from r18_sum import chi, min_tuples
def check(name,n,pieces):
    E=set(tuple(sorted(e)) for P in pieces for e in P)
    Ps=[set(tuple(sorted(e)) for e in P) for P in pieces]
    a=[chi(n,list(P)) for P in Ps]; q=chi(n,list(E))
    own=[];join=[]
    for lab in itertools.product(range(len(Ps)),repeat=n):
        blocks=[[v for v in range(n) if lab[v]==k] for k in range(len(Ps))]
        ok=all((u,v) in Ps[lab[u]] for (u,v) in E if lab[u]==lab[v])
        if ok: own.append(lab)
        cross=all(tuple(sorted((u,v))) in E for u in range(n) for v in range(u+1,n) if lab[u]!=lab[v])
        if cross and all(blocks[k] and chi(n,[e for e in E if e[0] in blocks[k] and e[1] in blocks[k]] )- (n-len(blocks[k]))*0==a[k] for k in range(len(Ps))):
            # chi of induced subgraph: isolated outside vertices count as colorable by 1 color, fine since a[k]>=1
            join.append(lab)
    print(name,"chi pieces",a,"sum",sum(a),"chiG",q,"aligned-min-tuples",min_tuples(n,[list(P) for P in Ps]),
          "#own",len(own),"#join",len(join),"own-and-join",len([l for l in own if l in join]))
K4a=[[(0,1),(1,2),(2,3),(3,0)],[(0,2),(2,1),(1,3),(3,0)]]
check("K4=C4uC4",4,K4a)
check("K4=(K4-uv)uK2",4,[[e for e in itertools.combinations(range(4),2) if e!=(0,1)],[(0,1)]])
check("C4=P3uP3",4,[[(0,1),(1,2)],[(2,3),(3,0)]])
A23=[(u,v) for u in (0,1) for v in (2,3,4)]
check("K5=K23uK221",5,[A23,[e for e in itertools.combinations(range(5),2) if e not in [(0,2),(1,3)]]])
check("K5=K23u(K2+K3)",5,[A23,[(0,1),(2,3),(2,4),(3,4)]])
W5A=[(0, 2), (0, 4), (0, 5), (1, 2), (2, 3), (3, 4), (5, 1)];W5B=[(0, 1), (0, 3), (0, 5), (1, 2), (2, 3), (3, 4), (4, 5)]
check("W5",6,[W5A,W5B])
check("K6-02",6,[[(0, 3), (1, 4), (2, 5), (3, 4), (4, 5)],[(0, 1), (0, 4), (0, 5), (1, 2), (1, 3), (1, 5), (2, 3), (2, 4), (3, 5)]])
