# R12 망상꾼: 완전 부호(로이드형) 항등식 (A+I)chi_W = 1 - chi_S 의 확인과 정다면체 조각 구성
import itertools, random, numpy as np, networkx as nx
from r11_levi import manual, recognize
def mult(X,lam):
    ev=np.linalg.eigvalsh(nx.to_numpy_array(X)); return int(np.sum(np.abs(ev-lam)<1e-8))
def identity_check(X,W):
    A=nx.to_numpy_array(X,nodelist=list(X.nodes())); idx={v:i for i,v in enumerate(X.nodes())}
    chi=np.zeros(len(idx)); 
    for w in W: chi[idx[w]]=1
    r=(A+np.eye(len(idx)))@chi
    S=[v for v in X.nodes() if r[idx[v]]==0]
    return set(np.round(r).astype(int)), len(S)
# 1) 코xeter형 (K7 = C7(1)+C7(2)+C7(3))
hc=[(list(range(7)),[(i,(i+s)%7) for i in range(7)]) for s in (1,2,3)]
Mo,M,G,_=manual(hc); X=nx.convert_node_labels_to_integers(Mo)
sols=[s[0] for s in recognize(X,'Mo')] if False else None
print('Coxeter-type: n',X.number_of_nodes(),'spec',sorted(set(np.round(np.linalg.eigvalsh(nx.to_numpy_array(X)),4))),'mult(-1)',mult(X,-1))
# 8 perfect codes: find via independent sets of size 7 with closed nbhds partitioning
V=list(X.nodes()); codes=[]
A=nx.to_numpy_array(X)
def search(chosen,covered,start):
    if len(covered)==len(V): codes.append(tuple(chosen)); return
    v=min(set(V)-covered)
    for c in [v]+list(X[v]):
        cl={c}|set(X[c])
        if cl & covered: continue
        search(chosen+[c],covered|cl,0)
search([],set(),0)
codes=sorted(set(tuple(sorted(c)) for c in codes)); print('perfect codes',len(codes))
vecs=np.array([[1.0 if v in c else 0 for v in V] for c in codes])-0.25
print('rank of chi_W - 1/4 vectors',np.linalg.matrix_rank(vecs,1e-8),' all in ker(A+I):',np.allclose((A+np.eye(len(V)))@vecs.T,0))
# 2) 절단 파노
fano=[(0,1,3),(1,2,4),(2,3,5),(3,4,6),(4,5,0),(5,6,1),(6,0,2)]
Mo,M,G,_=manual([(list(b),list(itertools.combinations(b,2))) for b in fano]); Xf=nx.convert_node_labels_to_integers(Mo)
print('Fano-trunc mult(-1)',mult(Xf,-1),'spec',sorted(set(np.round(np.linalg.eigvalsh(nx.to_numpy_array(Xf)),4))))
# 3) 정십이면체, 피터슨, 헤우드, 큐브
for name,Y in [('dodeca',nx.dodecahedral_graph()),('petersen',nx.petersen_graph()),('heawood',nx.heawood_graph()),('cube',nx.hypercube_graph(3)),('tutte-coxeter',nx.LCF_graph(30,[-13,-9,7,-7,9,13],5))]:
    n=Y.number_of_nodes(); d=max(dict(Y.degree()).values())
    print(name,'n',n,'d',d,'n mod (d+1)',n%(d+1),'mult(-1)',mult(Y,-1))
# 4) 정다면체 조각: d 장의 (d-1)-정칙 평면 그래프를 같은 꼭짓점 위에 덮기
def platonic_cover(P,d,tries=20000,seed=1):
    rnd=random.Random(seed); m=P.number_of_nodes(); E=list(P.edges())
    for t in range(tries):
        perms=[list(range(m))]+[rnd.sample(range(m),m) for _ in range(d-1)]
        cov=set()
        for p in perms:
            for a,b in E: cov.add(frozenset((p[a],p[b])))
        if len(cov)==m*(m-1)//2:
            return [(list(range(m)),[(p[a],p[b]) for a,b in E]) for p in perms]
    return None
for d,P in [(2,nx.complete_graph(2)),(3,nx.complete_graph(3)),(4,nx.complete_graph(4)),(5,nx.octahedral_graph()),(6,nx.icosahedral_graph())]:
    ps=platonic_cover(P,d)
    if ps is None: print('d',d,'no cover found'); continue
    Mo,M,G,mu=manual(ps); Y=nx.convert_node_labels_to_integers(Mo)
    degs=set(dict(Y.degree()).values()); n=Y.number_of_nodes()
    W=[i for i,v in enumerate(Mo.nodes()) if v[1]=='*']
    print('d',d,'piece',P.number_of_nodes(),'pts; n',n,'degs',degs,'A complete',G.number_of_edges()==P.number_of_nodes()*(P.number_of_nodes()-1)//2,
          'mult(-1)',mult(Y,-1),'identity (values,|S|)',identity_check(Y,W),'mu max',max(mu.values()),'planar',nx.check_planarity(Y)[0])
