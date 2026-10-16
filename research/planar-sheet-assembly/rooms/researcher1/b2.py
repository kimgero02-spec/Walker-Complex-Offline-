# b>=2 시험: 경계 성분마다 W_i-다리 겹침 그래프 이분성(필요조건)이 충분한가? 결정적 예 하나로 시험.
import networkx as nx, itertools as it
from r02 import analyze, from_polygons
from n2 import overlap
def per_component(pieces,name):
    r=analyze(pieces,name); K=r['K']
    cnt={}
    for _,C in pieces:
        for x in zip(C,C[1:]+C[:1]): cnt[frozenset(x)]=cnt.get(frozenset(x),0)+1
    bd=nx.Graph([tuple(k) for k,v in cnt.items() if v==1])
    out=[]
    for comp in nx.connected_components(bd):
        W=[u for u,_ in nx.find_cycle(bd.subgraph(comp))]; Ws=set(W)
        # K 의 W-다리
        Br=[]
        for u,v in K.edges():
            if u in Ws and v in Ws and not bd.has_edge(u,v): Br.append(frozenset((u,v)))
        R=K.subgraph([x for x in K if x not in Ws])
        for c in nx.connected_components(R): Br.append(frozenset(y for x in c for y in K[x] if y in Ws))
        O=nx.Graph(); O.add_nodes_from(range(len(Br)))
        for a,b in it.combinations(range(len(Br)),2):
            if overlap(Br[a],Br[b],W): O.add_edge(a,b)
        out.append((len(W),len(Br),nx.is_bipartite(O)))
    print(name,"b=",r['b'],"Kplanar=",r['Kplanar'],"per-component (|W|,#bridges,overlap bipartite):",out)
L=[8,4,4,4,4]
gl3=[(0,0,1,0,1),(1,2,2,0,1),(2,2,0,4,-1),(0,2,3,0,1),(3,2,4,0,1),(4,2,0,6,-1)]
per_component(from_polygons(L,gl3),"two twisted, interlaced")
gl2=[(0,0,1,0,1),(1,2,2,0,1),(2,2,0,2,1),(0,4,3,0,1),(3,2,4,0,1),(4,2,0,6,1)]
per_component(from_polygons(L,gl2),"non-interlaced straight (planar ribbon)")
from r02 import strip
per_component(strip(4,1),"prism k=4")

# 봉합 사각형 환원 (정리 U+): b>=2 이면 서로 다른 경계 성분을 잇는 호 e 의 끝점 x1,x2 에서
# W-변 f1 (x1 에 닿음), f2 (x2 에 닿음) 을 사각형 조각으로 이어 b 를 1 줄인다. 모든 선택을 시도.
def boundary_info(pieces):
    cnt={}
    for _,C in pieces:
        for x in zip(C,C[1:]+C[:1]): cnt[frozenset(x)]=cnt.get(frozenset(x),0)+1
    bd=nx.Graph([tuple(k) for k,v in cnt.items() if v==1])
    comp={v:i for i,c in enumerate(nx.connected_components(bd)) for v in c}
    return bd,comp
def reductions(pieces):
    r=analyze(pieces); bd,comp=boundary_info(pieces); out=[]
    for (i,j,p,e) in r['arcs']:
        x1,x2=p[0],p[-1]
        if comp[x1]==comp[x2]: continue
        for y1 in bd[x1]:
            for y2 in bd[x2]:
                for C in [[x1,y1,('z',len(out)),y2,x2,('w',len(out))],[x1,y1,('z',len(out)),x2,y2,('w',len(out))]]:
                    # 새 변은 새 정점으로 세분 (다중변 방지)
                    new=pieces+[(list(zip(C,C[1:]+C[:1])),C)]
                    out.append(new)
    return out
def planar_via_reduction(pieces,depth=0):
    r=analyze(pieces)
    if r['b']==1: return r['Ibip']
    return any(planar_via_reduction(nw,depth+1) for nw in reductions(pieces))
for nm,pc in [("two twisted, interlaced",from_polygons(L,gl3)),("prism k=4",strip(4,1)),("prism k=3",strip(3,1)),
              ("non-interlaced straight (b=3)",from_polygons(L,gl2))]:
    r=analyze(pc); print(nm,"b=",r['b'],"환원 판정:",planar_via_reduction(pc),"실제 K planar:",r['Kplanar'])
