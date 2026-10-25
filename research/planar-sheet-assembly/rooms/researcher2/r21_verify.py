# R21 독립 검산기: (1) K_9 기반 장의 궤도 대표 표, (2) K_8 꽉 찬 (3,2)+이분+이분 예 (sigma=7).
import itertools, networkx as nx
from r19_lib import chi, omega
E0=[(0,2),(0,3),(0,7),(1,2),(1,6),(1,8),(3,8),(4,7),(4,8),(5,6),(5,8),(6,7)]
inv=[]
for u,v in E0:
    (i,r),(j,s)=divmod(u,3),divmod(v,3)
    if r>s or (r==s and False): (i,r),(j,s)=(j,s),(i,r)
    inv.append((r,s,(j-i)%3 if r!=s else min((j-i)%3,(i-j)%3)))
print('K9 궤도 불변량:',inv,'서로 다름:',len(set(inv))==12)
P=nx.Graph([(0,1),(2,3),(4,5),(6,7),(2,4),(2,6),(5,7)])
B1=nx.Graph([(0,4),(0,5),(0,6),(0,7),(1,4),(1,5),(2,7),(3,6),(3,7)])
B2=nx.Graph([(0,2),(0,3),(1,2),(1,3),(1,6),(1,7),(2,5),(3,4),(3,5),(4,6),(4,7),(5,6)])
cnt={}
for G in (P,B1,B2):
    for e in G.edges(): cnt[frozenset(e)]=cnt.get(frozenset(e),0)+1
print('K8 정확:',set(cnt)==set(frozenset(e) for e in itertools.combinations(range(8),2)) and all(c==1 for c in cnt.values()))
for nm,G in (('P',P),('B1',B1),('B2',B2)):
    print(nm,'평면',nx.check_planarity(G)[0],'chi',chi(G),'omega',omega(G),'변',G.number_of_edges())
print('B1 쪽:',nx.bipartite.sets(B1) if nx.is_connected(B1) else 'n/a')
