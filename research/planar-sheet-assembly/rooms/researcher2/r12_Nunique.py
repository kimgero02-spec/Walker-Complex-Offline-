# R12 망상꾼: N 의 유일성 반례 찾기 (작은 K_N 분해에서 M° 를 만들고 다른 W 로 다른 N 이 나오는지)
import itertools, networkx as nx
from r11_levi import manual, recognize
def conn_subgraphs(N):
    V=list(range(N)); E=list(itertools.combinations(V,2)); out=[]
    for v in V: out.append(((v,),()))
    for r in range(1,len(E)+1):
        for es in itertools.combinations(E,r):
            g=nx.Graph(); g.add_edges_from(es)
            if nx.is_connected(g) and nx.check_planarity(g)[0]:
                out.append((tuple(sorted(g.nodes())),es))
    return out
found=[]; seen=[]
for N in (2,3,4):
    cs=conn_subgraphs(N)
    for k in range(1,6 if N<4 else 4):
        for combo in itertools.combinations_with_replacement(range(len(cs)),k):
            ps=[cs[i] for i in combo]
            cov=set(frozenset(e) for p in ps for e in p[1])
            if len(cov)!=N*(N-1)//2: continue
            if {v for p in ps for v in p[0]}!=set(range(N)): continue
            Mo,M,G,mu=manual([(list(p[0]),list(p[1])) for p in ps])
            if Mo.number_of_nodes()>13: continue
            for mode,X in (('Mo',Mo),('M',M)):
                X=nx.convert_node_labels_to_integers(X)
                if any(nx.is_isomorphic(X,Y) for (md,Y) in seen if md==mode): continue
                seen.append((mode,X))
                Ns=sorted({s[1] for s in recognize(X,mode)})
                if len(Ns)>1:
                    found.append((mode,N,ps,Ns)); print('DIFFERENT N',mode,N,ps,Ns,flush=True)
print('graphs tested',len(seen),'counterexamples',len(found))
