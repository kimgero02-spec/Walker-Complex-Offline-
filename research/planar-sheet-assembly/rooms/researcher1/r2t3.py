# R2-T3 researcher1: (1) T8 deficit check, (2) D6 error 4 with (W), (3) same D6 data different chi
import networkx as nx, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'researcher2'))
from r2t2 import colorable, chi

def T8():
    T = nx.complete_graph(4)
    for i in range(4):
        T.add_edges_from((4+i, j) for j in range(4) if j != i)
    return T

def T11():
    T = T8()
    # stack color-0 points into faces {s1,2,3},{s2,1,3},{s3,1,2}
    for v, face in [(8, (5, 2, 3)), (9, (6, 1, 3)), (10, (7, 1, 2))]:
        T.add_edges_from((v, u) for u in face)
    return T

def assemble(pieces, classes):
    """pieces: list of graphs; classes: list of lists of (k, v). returns G, A(t), H"""
    Gam = nx.Graph()
    for k, P in enumerate(pieces):
        Gam.add_nodes_from((k, v) for v in P)
        Gam.add_edges_from(((k, a), (k, b)) for a, b in P.edges())
    rep = {}
    for i, cl in enumerate(classes):
        for x in cl: rep[x] = ('J', i)
    G = nx.Graph()
    G.add_nodes_from(rep.get(x, x) for x in Gam)
    for a, b in Gam.edges():
        G.add_edge(rep.get(a, a), rep.get(b, b))
    H = G.subgraph([('J', i) for i in range(len(classes))]).copy()
    def At(t):
        A = Gam.copy()
        for i, cl in enumerate(classes):
            K = [('K', i, j) for j in range(t)]
            A.add_edges_from((K[a], K[b]) for a in range(t) for b in range(a+1, t))
            A.add_edges_from((k, x) for k in K for x in cl)
        return A
    return G, At, H, Gam

def report(name, pieces, classes, tmax):
    G, At, H, Gam = assemble(pieces, classes)
    print(name)
    print('  pieces planar:', [nx.check_planarity(P)[0] for P in pieces])
    print('  pieces uniq-4col sanity chi:', [chi(P) for P in pieces])
    ports = {x for cl in classes for x in cl}
    inner = [Gam.subgraph([(k, v) for v in P if (k, v) not in ports]) for k, P in enumerate(pieces)]
    print('  chi(P_k \\ J_k):', [chi(I) for I in inner])
    print('  H edges:', H.number_of_edges(), 'loops:', nx.number_of_selfloops(H), 'chi(H):', chi(H))
    print('  chi(G):', chi(G))
    seq = [chi(At(t)) for t in range(tmax+1)]
    print('  chi(A^(t)):', seq, ' d:', [s-(t+1) for t, s in enumerate(seq)])

# (1) opponent's T8 example, one class of 4 stacked points ((W) violated)
report('T8, one class {4,5,6,7}', [T8()], [[(0, 4), (0, 5), (0, 6), (0, 7)]], 5)
# (2) (W)-respecting error-4: T11 color-0 ports {4,8,9,10} vs T8 rainbow ports {4,5,6,7}
cls = [[(0, p), (1, s)] for p, s in zip([4, 8, 9, 10], [4, 5, 6, 7])]
report('W-version: T11(color-0 ports) + T8(rainbow ports)', [T11(), T8()], cls, 5)
# (3) same D6 data, chi 4: T11 color-0 ports + second T11 color-0 ports
cls2 = [[(0, p), (1, p)] for p in [4, 8, 9, 10]]
report('control: T11 + T11, color-0 ports both sides', [T11(), T11()], cls2, 5)
# (4) same pieces (T11, T11), same H (edgeless, 4 vertices), only port choice differs -> chi 5 vs 4
cls3 = [[(0, p), (1, s)] for p, s in zip([4, 8, 9, 10], [4, 5, 6, 7])]
report('same pieces T11+T11, rainbow ports on copy 2', [T11(), T11()], cls3, 5)
