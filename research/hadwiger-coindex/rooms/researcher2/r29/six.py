import itertools, networkx as nx
def circ(n, S):
    G=nx.Graph(); G.add_nodes_from(range(n))
    for i in range(n):
        for s in S: G.add_edge(i,(i+s)%n)
    return G
def grotzsch():
    G=nx.Graph()
    for i in range(5): G.add_edge(i,(i+1)%5)
    for i in range(5):
        G.add_edge(5+i,(i-1)%5); G.add_edge(5+i,(i+1)%5); G.add_edge(5+i,10)
    return G
def k443():
    G=nx.Graph(); parts=[range(0,4),range(4,8),range(8,11)]
    for i in range(3):
        for j in range(i+1,3):
            for u in parts[i]:
                for v in parts[j]: G.add_edge(u,v)
    return G
cands={"Grotzsch":grotzsch(),"C11(1,2)":circ(11,[1,2]),"C11(1,3,4)?":circ(11,[1,3,4]),"K_{4,4,3}":k443()}
for name,G in cands.items():
    from networkx.algorithms.clique import find_cliques
    om=max(len(c) for c in find_cliques(G))
    planar6=[S for S in itertools.combinations(G.nodes(),6) if nx.check_planarity(G.subgraph(S))[0]]
    print(f"{name}: n={G.number_of_nodes()} m={G.number_of_edges()} omega={om} planar 6-sets={len(planar6)}/462")
    if planar6: print("   example planar 6-set", planar6[0])
