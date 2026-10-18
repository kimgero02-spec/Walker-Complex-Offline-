# R12 망상꾼: K_7 의 해밀턴 사이클 3개 분해 전부 -> M° 의 구조 수, Aut 궤도, 구조별 분해 동형류 (반례 탐색)
import itertools, networkx as nx
from r12_cycdec import analyse, perfect_codes
from r11_levi import manual
from r12_lloyd import check_W
N=7; E=set(frozenset(e) for e in itertools.combinations(range(N),2))
hams=set()
for p in itertools.permutations(range(1,N)):
    if p[0]<p[-1]:
        c=(0,)+p; hams.add(frozenset(frozenset((c[i],c[(i+1)%N])) for i in range(N)))
hams=list(hams); decs=set()
for a,b in itertools.combinations(range(len(hams)),2):
    if hams[a]&hams[b]: continue
    rest=E-hams[a]-hams[b]
    g=nx.Graph([tuple(e) for e in rest])
    if g.number_of_nodes()==N and all(d==2 for _,d in g.degree()) and nx.is_connected(g):
        decs.add(frozenset([hams[a],hams[b],frozenset(rest)]))
print('ham decompositions',len(decs))
def tocyc(es):
    g=nx.Graph([tuple(e) for e in es]); c=[e[0] for e in nx.find_cycle(g,0)]; return (c,[tuple(e) for e in es])
seen=[]
for d in decs:
    cyc=[tocyc(h) for h in d]; Mo,_,_,_=manual(cyc); X=nx.convert_node_labels_to_integers(Mo)
    if any(nx.is_isomorphic(X,Y) for Y in seen): continue
    seen.append(X); analyse(cyc,'ham')
