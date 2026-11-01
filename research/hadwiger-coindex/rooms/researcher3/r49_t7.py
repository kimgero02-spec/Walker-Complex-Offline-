# 가젯 단위 U = 아폴로니안 A (V1) + K4 Q (V2), 교차 v1-p, v2-q, v3-r, v4-{p',q',r'}
from r49_ladder import *
p,q,r,s,P,Q_,R=range(7); v1,v2,v3,v4=7,8,9,10
U=nx.Graph()
U.add_edges_from(itertools.combinations([p,q,r,s],2))
U.add_edges_from([(P,q),(P,r),(P,s),(Q_,p),(Q_,r),(Q_,s),(R,p),(R,q),(R,s)])
U.add_edges_from(itertools.combinations([v1,v2,v3,v4],2))
U.add_edges_from([(v1,p),(v2,q),(v3,r),(v4,P),(v4,Q_),(v4,R)])
print('n,e',U.number_of_nodes(),U.number_of_edges(),'planar',nx.check_planarity(U)[0])
pl=[e for e in U.edges() if nx.check_planarity(nx.restricted_view(U,[],[e]))[0]]
print('edges e with U-e planar:',pl)
V1=range(7)
for t in (2,3):
    res=search(U,V1,t)
    print('tubes',t,'->',None if res is None else (res['pairs'],[len(l) for l in res['ladders']],res['info']))
    if res: break
# 22 정점 가젯 = U 두 벌 (서로소) 인지 확인
