# R12 r1: example checks (not evidence): short-cycle core G_{<=5}, diameters, all W for a few named graphs
import itertools, networkx as nx
from r11_inverse import try_W, subdiv3
def short_core(G, L=5):
    E=set()
    for c in nx.simple_cycles(G.to_directed()) if False else []: pass
    # edges on cycles of length <= L: edge uv lies on such a cycle iff dist_{G-uv}(u,v) <= L-1
    for u,v in G.edges():
        G.remove_edge(u,v)
        try: d=nx.shortest_path_length(G,u,v)
        except nx.NetworkXNoPath: d=99
        G.add_edge(u,v)
        if d<=L-1: E.add((u,v))
    return nx.Graph(list(E))
def allW(G, mode):
    D=dict(nx.all_pairs_shortest_path_length(G))
    ok=(lambda a,b:D[a][b]==3) if mode=='circ' else (lambda a,b:D[a][b] in (1,3))
    C=nx.Graph(); C.add_nodes_from(v for v in G if G.degree(v)>=2)
    C.add_edges_from((a,b) for a,b in itertools.combinations(list(C),2) if ok(a,b))
    return [W for W in [()]+[tuple(c) for c in nx.enumerate_all_cliques(C)] if try_W(G,W,mode) is not None]
def mob(k):
    G=nx.cycle_graph(2*k); G.add_edges_from((i,i+k) for i in range(k)); return G
tests={'M8':mob(4),'M10':mob(5),'M12':mob(6),'M14':mob(7),'Petersen':nx.petersen_graph(),
       'K33^(3)':None,'C7':nx.cycle_graph(7),'Heawood':nx.heawood_graph()}
K=nx.complete_bipartite_graph(3,3); S=nx.Graph()
for u,v in K.edges(): nx.add_path(S,[('h',u),(u,v,'a'),(u,v,'b'),('h',v)])
tests['K33^(3)']=S
for n,G in tests.items():
    core=short_core(G)
    pl = nx.check_planarity(core)[0] if core.number_of_edges() else True
    print(n, 'diam',nx.diameter(G),'|core E|',core.number_of_edges(),'/',G.number_of_edges(),'core planar',pl,
          'circ W:',[(len(W),G.number_of_nodes()-sum(G.degree(w) for w in W)) for W in allW(G,'circ')],
          'full #W:',len(allW(G,'full')))
