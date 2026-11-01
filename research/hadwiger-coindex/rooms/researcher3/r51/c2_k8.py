# C2: find 8 points s.t. K_8 straight-line splits into 2 plane layers (crossing graph bipartite)
import itertools, random
import networkx as nx
random.seed(1)
def orient(p,q,r): return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
def segx(P,e,f):
    a,b=e;c,d=f
    if len({a,b,c,d})<4: return False
    return orient(P[a],P[b],P[c])*orient(P[a],P[b],P[d])<0 and orient(P[c],P[d],P[a])*orient(P[c],P[d],P[b])<0
def crossg(P,n):
    E=list(itertools.combinations(range(n),2))
    C=nx.Graph(); C.add_nodes_from(E)
    for e,f in itertools.combinations(E,2):
        if segx(P,e,f): C.add_edge(e,f)
    return C
def oddness(C):
    # greedy: size of min edges to delete to make bipartite approx via max-cut local search
    nodes=list(C.nodes()); col={v:random.randint(0,1) for v in nodes}
    improved=True
    while improved:
        improved=False
        for v in nodes:
            same=sum(1 for u in C[v] if col[u]==col[v]); diff=C.degree(v)-same
            if same>diff: col[v]^=1; improved=True
    return sum(1 for u,v in C.edges() if col[u]==col[v]), col
n=8
best=None
for restart in range(40):
    P=[(random.random(),random.random()) for _ in range(n)]
    C=crossg(P,n); s=min(oddness(C)[0] for _ in range(5))
    for it in range(1500):
        if nx.is_bipartite(C): break
        i=random.randrange(n); old=P[i]
        P[i]=(old[0]+random.gauss(0,0.05),old[1]+random.gauss(0,0.05))
        C2=crossg(P,n); s2=min(oddness(C2)[0] for _ in range(3))
        if s2<=s: s=s2;C=C2
        else: P[i]=old
    if nx.is_bipartite(C):
        best=P;break
if best:
    C=crossg(best,n); col=nx.bipartite.color(C)
    L=[[e for e in C if col[e]==k] for k in (0,1)]
    print("FOUND points",[(round(x,4),round(y,4)) for x,y in best])
    print("layer sizes",[len(l) for l in L],"crossings X=",C.number_of_edges())
    print("omega(Cr)=",max(len(c) for c in nx.find_cliques(C)))
    hull=[]
    print("L1",L[0]);print("L2",L[1])
else: print("not found")
