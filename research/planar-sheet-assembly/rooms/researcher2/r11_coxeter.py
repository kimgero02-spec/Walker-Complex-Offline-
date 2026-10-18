# 3 해밀턴 사이클 분해 K7 의 M° 와 코xeter 그래프; 완전 부호(흰 점 후보) 열거
import itertools, networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher
X=nx.Graph()
for i in range(7):
    X.add_edge(('a',i),('a',(i+1)%7)); X.add_edge(('b',i),('b',(i+2)%7)); X.add_edge(('c',i),('c',(i+3)%7))
    for t in 'abc': X.add_edge(('d',i),(t,i))
# Coxeter 그래프 독립 구성: Fano 의 반깃발(점 p, 직선 L, p∉L), (p,L)~(q,M) iff {p,q,...}: 표준: 서로 다른 점, 서로 다른 직선, p∈M, q∈L 이 아님... 대신 거리 정칙성 확인
print('cubic',set(dict(X.degree()).values()),'girth',min(len(c) for c in nx.minimum_cycle_basis(X)),'diam',nx.diameter(X))
aut=sum(1 for _ in GraphMatcher(X,X).isomorphisms_iter()); print('|Aut|',aut)
# 정점 추이성: 궤도
orb={}
for f in GraphMatcher(X,X).isomorphisms_iter():
    orb.setdefault(f[('d',0)],0)
print('orbit of white d0 size',len(orb))
# 크기 7 완전 부호: 닫힌 이웃이 V 분할
V=list(X); codes=[]
def rec(cov,chosen,start):
    if len(cov)==28: codes.append(list(chosen)); return
    u=min(x for x in V if x not in cov)  # u 는 어떤 닫힌 이웃에 들어가야 함
    for c in [u]+list(X[u]):
        N=set(X[c])|{c}
        if N & cov: continue
        rec(cov|N,chosen+[c],0)
rec(set(),[],0)
codes={frozenset(c) for c in codes}
print('#perfect codes',len(codes))
import sys; sys.path.insert(0,'.')
from r11_levi import is_complete
for W in list(codes)[:8]:
    B=[x for x in V if x not in W]; XB=X.subgraph(B)
    comps=[len(c) for c in nx.connected_components(XB)]
    cls={}
    for w in W:
        for x in X[w]: cls[x]=w
    ok=all(len({frozenset(c) for c in nx.connected_components(XB) if x in c} )==1 for x in B)
    compid={x:i for i,c in enumerate(nx.connected_components(XB)) for x in c}
    r4=all(len({compid[x] for x in X[w]})==3 for w in W)
    Q=nx.Graph([(cls[a],cls[b]) for a,b in XB.edges()])
    print(sorted(comps),'R4',r4,'quotient K7',is_complete(Q) and Q.number_of_nodes()==7, 'planar',all(nx.check_planarity(XB.subgraph(c))[0] for c in nx.connected_components(XB)))
# Aut 의 8 부호 위 작용
cl=list(codes); idx={c:i for i,c in enumerate(cl)}
perms=set()
for f in GraphMatcher(X,X).isomorphisms_iter():
    perms.add(tuple(idx[frozenset(f[x] for x in c)] for c in cl))
print('#distinct perms on 8 codes',len(perms))
triples={}
for p in perms:
    triples[(p[0],p[1],p[2])]=triples.get((p[0],p[1],p[2]),0)+1
print('ordered triple images',len(triples),'multiplicities',set(triples.values()))
