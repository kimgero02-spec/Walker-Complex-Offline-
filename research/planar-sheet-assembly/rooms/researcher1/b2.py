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
