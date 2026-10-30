# R12 망상꾼: 작은 K_N 분해의 M°/M 에서 매뉴얼 구조가 둘 이상인 경우, Aut 궤도가 하나인지 (예측 Π7 의 반례 탐색)
import itertools, networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher
from r11_levi import manual, recognize
def conn_subgraphs(N):
    V=list(range(N)); E=list(itertools.combinations(V,2)); out=[((v,),()) for v in V]
    for r in range(1,len(E)+1):
        for es in itertools.combinations(E,r):
            g=nx.Graph(es)
            if nx.is_connected(g) and nx.check_planarity(g)[0]: out.append((tuple(sorted(g.nodes())),es))
    return out
seen=[]; multi=0; bad=0
for N in (2,3,4):
    cs=conn_subgraphs(N)
    for k in range(1,6 if N<4 else 4):
        for combo in itertools.combinations_with_replacement(range(len(cs)),k):
            ps=[cs[i] for i in combo]
            if len({frozenset(e) for p in ps for e in p[1]})!=N*(N-1)//2: continue
            if {v for p in ps for v in p[0]}!=set(range(N)): continue
            Mo,M,G,mu=manual([(list(p[0]),list(p[1])) for p in ps])
            if Mo.number_of_nodes()>13: continue
            for mode,X in (('Mo',Mo),('M',M)):
                X=nx.convert_node_labels_to_integers(X)
                if any(md==mode and nx.is_isomorphic(X,Y) for md,Y in seen): continue
                seen.append((mode,X))
                S=[frozenset(W) for W,_ in recognize(X,mode)]
                if len(S)<2: continue
                multi+=1
                auts=list(GraphMatcher(X,X).isomorphisms_iter())
                orb={frozenset(a[x] for x in S[0]) for a in auts}
                if set(S)-orb:
                    bad+=1; print('NON-TRANSITIVE',mode,N,ps,'structures',len(S),'orbit of first',len(orb),flush=True)
print('graphs',len(seen),'with >=2 structures',multi,'non-transitive',bad)
