# r1 요청: b>=2 에서 정리 U 의 단순 확장("같은 경계 성분 위 호들의 엇갈림 그래프 이분") 시험
import networkx as nx, itertools as it
from collections import defaultdict
import importlib.util,sys
def build(C0,Qc,Rc,arcs):
    pieces={'P0':C0,'Q':Qc,'R':Rc}
    E=defaultdict(list)
    for k,C in pieces.items():
        for i in range(len(C)): E[frozenset((C[i],C[(i+1)%len(C)]))].append(k)
    G=nx.Graph([tuple(e) for e in E])
    bd=nx.Graph([tuple(e) for e,l in E.items() if len(l)==1])
    comps=[set(c) for c in nx.connected_components(bd)]
    V=set(G); chi=len(V)-len(E)+3
    return G,bd,comps,chi
C0=['u1','m1','w1','g1','s1','n1','t1','g2','u2','m2','w2','g3','s2','n2','t2','g4']
# 꼬인 손잡이: a 정방향, a' 역방향
Qc=['u1','m1','w1','p','w2','m2','u2','q']; Rc=['s1','n1','t1','r1','t2','n2','s2','r2']
arcs={'a':('u1','w1'),'a2':('u2','w2'),'b':('s1','t1'),'b2':('s2','t2')}
G,bd,comps,chi=build(C0,Qc,Rc,arcs)
print("꼬인 손잡이 2개(엇갈림): χ=",chi,"b=",len(comps),"G 평면",nx.check_planarity(G)[0])
for name,(x,y) in arcs.items():
    print(" 호",name,"끝점 성분:",[i for i,c in enumerate(comps) if x in c],[i for i,c in enumerate(comps) if y in c])
# 같은 성분 위 호 쌍의 엇갈림
def cyc_order(c):
    H=bd.subgraph(c); start=next(iter(c)); order=[start]; prev=None
    while True:
        nb=[v for v in H[order[-1]] if v!=prev]
        nxt=nb[0] if len(order)==1 else [v for v in H[order[-1]] if v!=order[-2]][0]
        if nxt==start: break
        prev=order[-1]; order.append(nxt)
    return order
Iedges=[]
for (e,(x,y)),(f,(z,w)) in it.combinations(arcs.items(),2):
    for c in comps:
        if {x,y,z,w}<=c:
            o=cyc_order(c); pos={v:i for i,v in enumerate(o)}
            a,b_=sorted((pos[x],pos[y]))
            inside=[a<pos[z]<b_, a<pos[w]<b_]
            if inside[0]!=inside[1]: Iedges.append((e,f))
I=nx.Graph(); I.add_nodes_from(arcs); I.add_edges_from(Iedges)
print(" 같은 성분 엇갈림 그래프 변:",Iedges," 이분:",nx.is_bipartite(I))
