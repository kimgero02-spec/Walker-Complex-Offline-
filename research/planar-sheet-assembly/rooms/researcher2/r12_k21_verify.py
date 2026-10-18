import itertools, numpy as np, networkx as nx
from r11_levi import manual
from r12_lloyd import check_W
def medial(G):
    ok,emb=nx.check_planarity(G); seen=set(); M=nx.Graph()
    for u,v in emb.edges():
        if (u,v) in seen: continue
        f=emb.traverse_face(u,v,mark_half_edges=seen)
        es=[frozenset((f[i],f[(i+1)%len(f)])) for i in range(len(f))]
        for i in range(len(es)): M.add_edge(es[i],es[(i+1)%len(es)])
    return nx.convert_node_labels_to_integers(M)
M9=medial(nx.circular_ladder_graph(3)); octa=nx.octahedral_graph()
oa={0: (0, 0), 1: (3, 1), 2: (1, 1), 3: (2, 1), 4: (6, 2), 5: (4, 0)}
ma={0: (0, 0), 1: (1, 0), 2: (5, 2), 5: (5, 0), 3: (0, 2), 6: (2, 2), 4: (5, 1), 8: (1, 2), 7: (1, 1)}
name=lambda p:7*p[1]+p[0]
pieces=[]
for G,asg in ((octa,oa),(M9,ma)):
    for t in range(7):
        f=lambda v:name(((asg[v][0]+t)%7,asg[v][1]))
        pieces.append(([f(v) for v in G],[(f(u),f(v)) for u,v in G.edges()]))
cnt={}
for Vk,Ek in pieces:
    P=nx.Graph(); P.add_nodes_from(Vk); P.add_edges_from(Ek)
    assert nx.check_planarity(P)[0] and all(d==4 for _,d in P.degree())
    for u,v in Ek: e=frozenset((u,v)); cnt[e]=cnt.get(e,0)+1
print('pairs covered',len(cnt),'of',21*20//2,'mu values',set(cnt.values()))
Mo,M,G,mu=manual(pieces); X=nx.convert_node_labels_to_integers(Mo,label_attribute='o')
W=[i for i in X if X.nodes[i]['o'][1]=='*']
print('n',X.number_of_nodes(),'degrees',set(dict(X.degree()).values()),'|W|',len(W),'N from check_W',check_W(X,W),'M==Mo',nx.utils.graphs_equal(M,Mo))
A=nx.to_numpy_array(X); ev=np.linalg.eigvalsh(A); print('mult(-1)',int(np.sum(abs(ev+1)<1e-8)),'connectivity',nx.node_connectivity(X))
print('pieces with vertex sets:',[sorted(p[0]) for p in pieces[:1]],'...')
