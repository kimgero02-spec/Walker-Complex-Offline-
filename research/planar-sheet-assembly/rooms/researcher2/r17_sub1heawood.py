# sub¹(Heawood) 에서 몇 개의 표적 M°(D) (N=5) 를 마이너로 찾는다 (찾으면 결정적 증거, 못 찾으면 아무 결론 없음)
import networkx as nx, itertools as it, sys
from r17_hM import has_minor, Mcirc
H=nx.heawood_graph(); S=nx.Graph()
for u,v in H.edges(): S.add_edge(u,('s',u,v)); S.add_edge(('s',u,v),v)
E5=list(it.combinations(range(5),2))
targets={
 'C5+C5*':[[(i,(i+1)%5) for i in range(5)],[(i,(i+2)%5) for i in range(5)]],
 'K5-e+K2':[[e for e in E5 if e!=(3,4)],[(3,4)]],
 'K4+K14':[[e for e in E5 if 4 not in e],[(i,4) for i in range(4)]],
}
name=sys.argv[1]
X=Mcirc(5,targets[name]); m=has_minor(S,X,maxset=int(sys.argv[2]))
print(name,X.number_of_nodes(),'FOUND' if m else 'not found (within maxset)')
if m: print({str(k):sorted(map(str,v)) for k,v in m.items()})
