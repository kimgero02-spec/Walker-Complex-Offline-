# R12 망상꾼: -1 이 고윳값이 아닐 때 W = (A+I)^{-1}(1-chi_S), |S|<=4 로 모든 (나)-구조를 찾는 알고리즘과 무차별 인식기의 비교
import itertools, numpy as np, networkx as nx
from fractions import Fraction
import sympy as sp
from r11_levi import recognize, manual
def check_W(X,W):
    # recognize() 의 조건을 한 W 에 대해서만
    Ws=set(W); V=list(X.nodes()); B=[x for x in V if x not in Ws]
    if any(X.has_edge(a,b) for a,b in itertools.combinations(W,2)): return None
    for w in W:
        if len([x for x in X[w] if x not in Ws])<2: return None
    if any(sum(1 for y in X[b] if y in Ws)>1 for b in B): return None
    XB=X.subgraph(B); comp={}
    for i,c in enumerate(nx.connected_components(XB)):
        for x in c: comp[x]=i
    for w in W:
        nb=[x for x in X[w] if x not in Ws]
        if len({comp[x] for x in nb})<len(nb): return None
    if any(not nx.check_planarity(XB.subgraph(c))[0] for c in nx.connected_components(XB)): return None
    cls={}
    for w in W:
        cls[w]=w
        for x in X[w]:
            if x not in Ws: cls[x]=w
    for b in B: cls.setdefault(b,b)
    Q=nx.Graph(); Q.add_nodes_from(set(cls.values()))
    for a,b in XB.edges(): Q.add_edge(cls[a],cls[b])
    n=Q.number_of_nodes()
    return n if Q.number_of_edges()==n*(n-1)//2 else None
def lloyd_structures(X,smax=4):
    V=list(X.nodes()); n=len(V)
    A=sp.Matrix(nx.to_numpy_array(X,nodelist=V).astype(int))+sp.eye(n)
    if A.det()==0: return 'singular'
    Ainv=A.inv(); out=set()
    for s in range(0,smax+1):
        for S in itertools.combinations(range(n),s):
            rhs=sp.Matrix([0 if i in S else 1 for i in range(n)])
            x=Ainv*rhs
            if all(v in (0,1) for v in x):
                W=tuple(V[i] for i in range(n) if x[i]==1)
                N=check_W(X,W)
                if N is not None: out.add((W,N))
    return sorted(out)
if __name__=='__main__':
    tests=[('C7',nx.cycle_graph(7)),('C9',nx.cycle_graph(9)),('C8',nx.cycle_graph(8)),('petersen',nx.petersen_graph()),('heawood',nx.heawood_graph()),('K4',nx.complete_graph(4))]
    # 실현 예 몇 개 (비정칙): 예 1.5 (K5 = 오각형 + 오각별), K5=(K5-e)+K2
    P1=(list(range(5)),[(i,(i+1)%5) for i in range(5)]); P2=(list(range(5)),[(i,(i+2)%5) for i in range(5)])
    Mo,_,_,_=manual([P1,P2]); tests.append(('Ex1.5 Mo',nx.convert_node_labels_to_integers(Mo)))
    E5=[e for e in itertools.combinations(range(5),2) if e!=(0,1)]
    Mo,_,_,_=manual([(list(range(5)),E5),([0,1],[(0,1)])]); tests.append(('K5-e+K2 Mo',nx.convert_node_labels_to_integers(Mo)))
    for name,X in tests:
        L=lloyd_structures(X)
        bf=sorted((tuple(W),N) for W,N in recognize(X,'Mo')) if X.number_of_nodes()<=16 else 'skip'
        print(name,'n',X.number_of_nodes(),'lloyd:',L if L=='singular' else [(len(W),N) for W,N in L],'| brute:',bf if bf=='skip' else [(len(W),N) for W,N in bf], '| same' if L!='singular' and bf!='skip' and L==bf else '')
    X=nx.LCF_graph(30,[-13,-9,7,-7,9,13],5); print('tutte-coxeter lloyd',lloyd_structures(X,smax=2))
