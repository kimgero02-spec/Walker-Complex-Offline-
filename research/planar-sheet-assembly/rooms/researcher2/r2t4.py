# R2-T4 researcher2: final response. Independent constructions (does not import r2t3.py).
import networkx as nx, itertools, sys
sys.setrecursionlimit(10000)
# helpers copied verbatim from r2t2.py (colorable, chi)
def colorable(G, q):
    """exact q-colorability, backtracking with DSATUR-like ordering"""
    nodes = list(G.nodes())
    if q <= 0: return len(nodes) == 0
    adj = {v: set(G[v]) for v in nodes}
    for v in nodes:
        if v in adj[v]: return False
    col = {}
    def pick():
        best=None; bk=None
        for v in nodes:
            if v in col: continue
            sat = len({col[u] for u in adj[v] if u in col})
            key=(sat, len(adj[v]))
            if bk is None or key>bk: bk=key; best=v
        return best
    def rec(used):
        v = pick()
        if v is None: return True
        forb = {col[u] for u in adj[v] if u in col}
        for c in range(min(q, used+1)):
            if c in forb: continue
            col[v]=c
            if rec(max(used, c+1)): return True
            del col[v]
        return False
    return rec(0)

def chi(G, cap=12):
    for q in range(0, cap+1):
        if colorable(G, q): return q
    return None


def build(pieces, classes, t, wt_white=None, uniform_b=None):
    """2-colored manual graph A (pieces + white star per class). Substitute K_t at whites."""
    A = nx.Graph()
    for k,P in enumerate(pieces):
        A.add_nodes_from((k,v) for v in P); A.add_edges_from(((k,a),(k,b)) for a,b in P.edges())
    for i,cl in enumerate(classes):
        K=[('w',i,j) for j in range(t)]
        A.add_nodes_from(K); A.add_edges_from(itertools.combinations(K,2))
        A.add_edges_from((x,p) for x in K for p in cl)
    return A

def glue(pieces, classes):
    rep={}
    for k,P in enumerate(pieces):
        for v in P: rep[(k,v)]=(k,v)
    for cl in classes:
        for p in cl: rep[p]=('J',tuple(cl))
    G=nx.Graph()
    for k,P in enumerate(pieces):
        G.add_nodes_from(rep[(k,v)] for v in P)
        for a,b in P.edges():
            x,y=rep[(k,a)],rep[(k,b)]
            G.add_edge(x,y)
    return G

def H_of(pieces, classes):
    cid={p:i for i,cl in enumerate(classes) for p in cl}
    H=nx.Graph(); H.add_nodes_from(range(len(classes)))
    for k,P in enumerate(pieces):
        for a,b in P.edges():
            if (k,a) in cid and (k,b) in cid: H.add_edge(cid[(k,a)],cid[(k,b)])
    return H

def chiG(G):
    if any(u==v for u,v in G.edges()): return float('inf')
    return chi(G)

def dseq(pieces, classes, tmax):
    return [chi(build(pieces,classes,t)) for t in range(tmax+1)]

def lexprod(X,b):
    return nx.lexicographic_product(X, nx.complete_graph(b))

# ---------- planar stacked triangulations ----------
def T8():
    G=nx.complete_graph(4)
    for i in range(4):
        s=4+i; G.add_edges_from((s,j) for j in range(4) if j!=i)
    return G
def T11():
    G=T8()
    # faces {s1,2,3},{s2,1,3},{s3,1,2}; s_i=4+i
    for new,face in zip((8,9,10),[(5,2,3),(6,1,3),(7,1,2)]):
        G.add_edges_from((new,f) for f in face)
    return G

def line(s): print(s)

if __name__=='__main__':
    line('=== P1: independent check of opponent (b-1),(b-2) ===')
    for name,P in (('T8',T8()),('T11',T11())):
        line(f'{name}: planar={nx.check_planarity(P)[0]}, chi={chi(P)}, |V|={P.number_of_nodes()}')
    # unique 4-coloring check of T11 forced colors
    P1,P2=T11(),T8()
    cls=[[(0,a),(1,4+i)] for i,a in enumerate((4,8,9,10))]
    G=glue([P1,P2],cls); H=H_of([P1,P2],cls)
    line(f'T11(4,8,9,10)+T8(4..7): chi(G)={chiG(G)}, |E(H)|={H.number_of_edges()}, d-seq chi(A^(t))={dseq([P1,P2],cls,5)}')
    for ports2,lab in (((4,5,6,7),'rainbow'),((4,8,9,10),'color-0')):
        cls2=[[(0,a),(1,b)] for a,b in zip((4,8,9,10),ports2)]
        G=glue([T11(),T11()],cls2); H=H_of([T11(),T11()],cls2)
        line(f'T11+T11, copy2 ports {lab}: chi(G)={chiG(G)}, |E(H)|={H.number_of_edges()}')

    line('\n=== P2: uniform b-fold chromatic numbers of unlabeled A cannot read chi(G) ===')
    # manual 1: K4 = (K4-uv) + K2, classes {u,u'},{v,v'}
    K4e=nx.complete_graph(4); K4e.remove_edge(0,1); K2=nx.Graph([(0,1)])
    m1=([K4e,K2],[[(0,0),(1,0)],[(0,1),(1,1)]])
    A1=build(*m1,1)
    # manual 2: the graph A1 itself as a single piece, no identifications
    P=nx.convert_node_labels_to_integers(A1)
    m2=([P],[])
    A2=build(*m2,1)
    line(f'A1 ~= A2 as unlabeled graphs: {nx.is_isomorphic(A1,A2)}; A1 planar={nx.check_planarity(A1)[0]}')
    line(f'chi(G1)={chiG(glue(*m1))}, chi(G2)={chiG(glue(*m2))}')
    for b in (1,2,3):
        line(f'  chi_b(A) = chi(A[K_b]) b={b}: A1 {chi(lexprod(A1,b),cap=14)}, A2 {chi(lexprod(A2,b),cap=14)}')
    line(f'  white-only substitution seq (Thm A): m1 {dseq(*m1,4)}, m2 {dseq(*m2,4)}')

    line('\n=== P3: no single number of the manual graph (chi(A), chi(P_k)) reads chi(G) ===')
    for n in range(3,7):
        pieces=[nx.Graph([(0,1)]) for _ in itertools.combinations(range(n),2)]
        classes=[[(k,e.index(v)) for k,e in enumerate(itertools.combinations(range(n),2)) if v in e] for v in range(n)]
        A=build(pieces,classes,1)
        line(f'K_{n} from K2 pieces: chi(A)={chi(A)}, chi(A[K_2] uniform)={chi(lexprod(A,2)) if n<=5 else '-'}, chi(G)={chiG(glue(pieces,classes))}, chi(H)={chi(H_of(pieces,classes))}')

    line('\n=== P4: trimmed presentation M=(H,f,P°): port-port edges moved to manual ===')
    def trim(pieces,classes):
        ports={p for cl in classes for p in cl}
        newp=[]; extra=[]; newcls=[list(cl) for cl in classes]
        cid={p:i for i,cl in enumerate(classes) for p in cl}
        Hedges=set()
        for k,P in enumerate(pieces):
            Q=P.copy()
            for a,b in list(P.edges()):
                if (k,a) in ports and (k,b) in ports:
                    Q.remove_edge(a,b); Hedges.add(tuple(sorted((cid[(k,a)],cid[(k,b)]))))
            newp.append(Q)
        # realize each H-edge as a K2 piece attached to the two junctions (formal: H with f)
        for (i,j) in sorted(Hedges):
            k=len(newp); newp.append(nx.Graph([(0,1)]))
            newcls[i].append((k,0)); newcls[j].append((k,1))
        return newp,newcls,Hedges
    C5=nx.cycle_graph(5); C5s=nx.Graph([(i,(i+2)%5) for i in range(5)])
    ex={'K5=C5+C5*':([C5,C5s],[[(0,i),(1,i)] for i in range(5)]),
        'K5=(K5-ab)+K2':(None,None),
        'T11+T8 (b-1)':([T11(),T8()],[[(0,a),(1,4+i)] for i,a in enumerate((4,8,9,10))])}
    K5e=nx.complete_graph(5); K5e.remove_edge(0,1)
    ex['K5=(K5-ab)+K2']=([K5e,nx.Graph([(0,1)])],[[(0,0),(1,0)],[(0,1),(1,1)]])
    for name,(pc,cl) in ex.items():
        G0=glue(pc,cl); np_,nc,He=trim(pc,cl); G1=glue(np_,nc)
        planar_ok=all(nx.check_planarity(Q)[0] for Q in np_)
        line(f'{name}: G iso after trim={nx.is_isomorphic(G0,G1)}, trimmed pieces planar={planar_ok}, |E(H)|={len(He)}, chi(G)={chiG(G0)}')
        line(f'   ports independent in trimmed pieces: {all(not ((k,a) in {p for c in nc for p in c} and (k,b) in {p for c in nc for p in c}) for k,Q in enumerate(np_[:len(pc)]) for a,b in Q.edges())}')
        line(f'   Thm A seq before={dseq(pc,cl,5)}, after trim={dseq(np_,nc,5)}')

    line('\n=== P5: does the Thm A sequence carry info beyond (max chi(P_k), chi(G))? ===')
    W4=nx.wheel_graph(5)  # hub 0, rim 1..4 ; chi=3
    # K5 = W4 + two K2 (rim diagonals 1-3, 2-4)
    m_w=([W4,nx.Graph([(0,1)]),nx.Graph([(0,1)])],[[(0,1),(1,0)],[(0,3),(1,1)],[(0,2),(2,0)],[(0,4),(2,1)]])
    m_c=ex['K5=C5+C5*']
    # K5 = two triangles sharing nothing? use: triangle-free? K5 = C5 + 5 K2 (pentagram split)
    m_k=([C5]+[nx.Graph([(0,1)]) for _ in range(5)], None)
    cls=[[(0,i)] for i in range(5)]
    for j in range(5):
        a,b=j,(j+2)%5; cls[a].append((1+j,0)); cls[b].append((1+j,1))
    m_k=(m_k[0],cls)
    for name,m in (('W4+2K2',m_w),('C5+C5*',m_c),('C5+5K2',m_k)):
        G=glue(*m); mx=max(chi(P) for P in m[0])
        line(f'{name}: G~K5={nx.is_isomorphic(G,nx.complete_graph(5))}, max chi(P)={mx}, chi(A^(t)) t=0..5: {dseq(*m,3)}, d={[c-t-1 for t,c in enumerate(dseq(*m,3))]}')
