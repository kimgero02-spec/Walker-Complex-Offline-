# R01 researcher1: 정선된 예제 검증 (각 예는 보고서의 특정 보조정리에 쓰임)
import networkx as nx, itertools as it

def glue(pieces):
    """pieces: list of edge lists on global vertex names (decomposition setting)."""
    G=nx.Graph()
    for P in pieces: G.add_edges_from(P)
    return G

def sign_of_arc(cyc1, cyc2, arc):
    """cyc: boundary cycle as vertex list (orientation). arc: vertex path list.
    returns +1 if traversal directions are opposite (orientation-compatible), -1 if same."""
    def direction(cyc, a, b):
        i=cyc.index(a); n=len(cyc)
        if cyc[(i+1)%n]==b: return 1
        if cyc[(i-1)%n]==b: return -1
        raise ValueError("not consecutive")
    d1=direction(cyc1,arc[0],arc[1]); d2=direction(cyc2,arc[0],arc[1])
    return 1 if d1!=d2 else -1

# --- Ex1: K5 = W4 (rim a b d c, hub e) U C4 (a b c d) glued along ab, cd
a,b,c,d,e='abcde'
P1=[(a,b),(b,d),(d,c),(c,a),(e,a),(e,b),(e,c),(e,d)]
P2=[(a,b),(b,c),(c,d),(d,a)]
G=glue([P1,P2])
print("K5 manual: iso K5?", nx.is_isomorphic(G,nx.complete_graph(5)))
print(" P1 planar?",nx.check_planarity(nx.Graph(P1))[0]," P2 planar?",nx.check_planarity(nx.Graph(P2))[0])
s1=sign_of_arc([a,b,d,c],[a,b,c,d],[a,b]); s2=sign_of_arc([a,b,d,c],[a,b,c,d],[c,d])
print(" signs",s1,s2,"holonomy",s1*s2)
I=nx.intersection(nx.Graph(P1),nx.Graph(P2)); print(" P1∩P2 edges",sorted(I.edges()))

# --- Ex2: rung-deletion lemma M_{2n} -> M_{2n-2}
def mob(n):
    G=nx.cycle_graph(2*n); G.add_edges_from((i,i+n) for i in range(n)); return G
def suppress(G):
    G=G.copy()
    while True:
        v=[x for x in G if G.degree(x)==2]
        if not v: return G
        x=v[0]; u,w=list(G[x]); G.remove_node(x); G.add_edge(u,w)
for n in [4,5]:
    H=mob(n); H.remove_edge(0,n); print("M_%d minus rung ~ M_%d:"%(2*n,2*n-2), nx.is_isomorphic(suppress(H),mob(n-1)))
print("M6 ~ K33:",nx.is_isomorphic(mob(3),nx.complete_bipartite_graph(3,3)), " M4~K4:",nx.is_isomorphic(mob(2),nx.complete_graph(4)))

# --- Ex3: Petersen. PP embedding faces (hemi-dodecahedron) then a 3-piece Mobius band manual
Pe=nx.petersen_graph()
cyc5=[c for c in nx.simple_cycles(Pe.to_directed()) if len(c)==5]
cs={}
for c in cyc5:
    k=frozenset(frozenset(e) for e in zip(c,c[1:]+c[:1])); cs[k]=c
C=list(cs.items()); print("Petersen 5-cycles:",len(C))
E=[frozenset(e) for e in Pe.edges()]
faces=None
for S in it.combinations(range(len(C)),6):
    cnt={x:0 for x in E}
    for i in S:
        for x in C[i][0]: cnt[x]+=1
    if all(v==2 for v in cnt.values()):
        faces=[C[i][1] for i in S]; break
print("PP faces:",faces)
def boundary_cycle(facelist):
    cnt={}
    for f in facelist:
        for x in zip(f,f[1:]+f[:1]): k=frozenset(x); cnt[k]=cnt.get(k,0)+1
    bd=nx.Graph([tuple(k) for k,v in cnt.items() if v==1])
    if bd.number_of_edges()==0 or not all(dg==2 for _,dg in bd.degree()) or not nx.is_connected(bd): return None
    return [u for u,_ in nx.find_cycle(bd)]
def piece_graph(facelist):
    g=nx.Graph()
    for f in facelist: g.add_edges_from(zip(f,f[1:]+f[:1]))
    return g
def path_list(I):
    ends=[v for v in I if I.degree(v)==1]; return nx.shortest_path(I,ends[0],ends[1])
rest=faces[1:]
lab=(0,1,1,0,1)
groups=[[rest[i] for i in range(5) if lab[i]==g] for g in range(2)]
bds=[boundary_cycle(g) for g in groups]; Ps=[piece_graph(g) for g in groups]
print("Petersen 2-piece band (face",faces[0],"dropped):")
for k in range(2): print("  piece",k,"faces",groups[k],"boundary",bds[k],"chi",Ps[k].number_of_nodes()-Ps[k].number_of_edges()+len(groups[k]))
V=set(Ps[0])&set(Ps[1]); I=nx.Graph(); I.add_nodes_from(V)
I.add_edges_from(e for e in Ps[0].edges() if Ps[1].has_edge(*e))
hol=1
for comp in nx.connected_components(I):
    p=path_list(I.subgraph(comp)); sg=sign_of_arc(bds[0],bds[1],p); hol*=sg; print("  arc",p,"sign",sg)
print("  holonomy",hol," union=Petersen?",nx.is_isomorphic(nx.compose_all(Ps),Pe))
# --- Ex4: cube faces -> H = octahedron
Q=nx.hypercube_graph(3)
qf=[c for c in nx.simple_cycles(Q.to_directed()) if len(c)==4]
qs={}
for c in qf: qs[frozenset(frozenset(e) for e in zip(c,c[1:]+c[:1]))]=c
qf=list(qs.values())
Hc=nx.Graph(); Hc.add_nodes_from(range(len(qf)))
for i,j in it.combinations(range(len(qf)),2):
    if len(set(map(frozenset,zip(qf[i],qf[i][1:]+qf[i][:1])))&set(map(frozenset,zip(qf[j],qf[j][1:]+qf[j][:1]))))>0: Hc.add_edge(i,j)
print("cube 4-cycles",len(qf)," H (share-an-edge) ~ octahedron?",nx.is_isomorphic(Hc,nx.octahedral_graph()))

# --- Ex5: label-type K5: double cosets D5 \ S5 / D5
from itertools import permutations
n=5
D=[]
for r in range(n):
    D.append(tuple((r+i)%n for i in range(n))); D.append(tuple((r-i)%n for i in range(n)))
D=set(D)
def comp(p,q): return tuple(p[q[i]] for i in range(n))
seen=set(); classes=[]
for s in permutations(range(n)):
    if s in seen: continue
    cl={comp(comp(x,s),y) for x in D for y in D}; seen|=cl; classes.append(s)
print("D5\\S5/D5 classes:",len(classes))
for s in classes:
    g=nx.cycle_graph(5); g2=nx.relabel_nodes(nx.cycle_graph(5),dict(enumerate(s)))
    print("  rep",s," shared edges",len(set(map(frozenset,g.edges()))&set(map(frozenset,g2.edges()))),
          " union K5?",nx.is_isomorphic(nx.compose(g,g2),nx.complete_graph(5)))
