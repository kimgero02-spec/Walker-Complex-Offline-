import networkx as nx, itertools, sys
Wadj={'x':'y z p q1 q2 q3','y':'x z p q4 q5','z':'x y q1 q5','p':'x y q3 q4','c':'q1 q2 q3 q4 q5'}
W=nx.Graph()
for u,vs in Wadj.items():
    for v in vs.split(): W.add_edge(u,v)
for i in range(1,6): W.add_edge(f'q{i}',f'q{i%5+1}')
print("W n,m",W.number_of_nodes(),W.number_of_edges(),"planar",nx.check_planarity(W)[0])
def is_forest(G,S): H=G.subgraph(S); return nx.is_forest(H) if len(S) else True
def is_bip(G,S): return nx.is_bipartite(G.subgraph(S))
V=list(W); fb=[];bad=0
for mask in range(1<<len(V)):
    F=[V[i] for i in range(len(V)) if mask>>i&1]; B=[v for v in V if v not in F]
    if is_forest(W,F) and is_bip(W,B):
        fb.append(set(F))
print("W FB count",len(fb),"with x,y in F:",sum(1 for F in fb if {'x','y'}<=F))
# build G*: K4 a,b,c,d; attach copy of W into a face (u,v,w) mapping x->u,y->v,z->w (interior vertices new)
G=nx.complete_graph(['a','b','c','d']); cnt=[0]
def attach(u,v,w):
    cnt[0]+=1; t=f'#{cnt[0]}'; m={'x':u,'y':v,'z':w}
    for a,b in W.edges(): G.add_edge(m.get(a,a+t),m.get(b,b+t))
    return t
t1=attach('a','b','c'); attach('b','d','a'); t3=attach('c','d','a'); attach('b','c','d')
# check faces exist: (a,c,q1#1) and (d,a,q5#3) are triangles
print("faces ok", G.has_edge('a','q1'+t1) and G.has_edge('c','q1'+t1), G.has_edge('d','q5'+t3) and G.has_edge('a','q5'+t3))
attach('a','c','q1'+t1); attach('d','a','q5'+t3)
print("G* n,m",G.number_of_nodes(),G.number_of_edges(),"3n-6",3*G.number_of_nodes()-6,"planar",nx.check_planarity(G)[0])
# each copy induced? check that the copy's vertex set induces exactly 24 edges
ok=True
for k in range(1,7):
    S=[n for n in G if n.endswith(f'#{k}')]
    # outer verts
print("forbidden pairs:",[('a','b'),('b','d'),('c','d'),('b','c'),('a','c'),('d','a')])
H=nx.read_edgelist(sys.argv[1]) if len(sys.argv)>1 else None
if H is not None: print("their edgelist n,m",H.number_of_nodes(),H.number_of_edges(),"isomorphic to mine:",nx.is_isomorphic(G,H))
