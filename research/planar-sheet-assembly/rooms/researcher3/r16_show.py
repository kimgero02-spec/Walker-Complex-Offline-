from r16_search import chi,hasK
import networkx as nx, itertools
for x in nx.graph_atlas_g()[1:]:
    if x.number_of_nodes()!=7 or not nx.is_connected(x) or not nx.check_planarity(x)[0] or chi(x)!=3: continue
    for H in itertools.combinations(x.nodes(),3):
        y=x.copy(); y.add_edges_from(itertools.combinations(H,2))
        if not hasK(y,5) and chi(y)>=5:
            print('T',sorted(x.edges()),H, 'complement of y:',sorted(nx.complement(y).edges())); break
    for a in itertools.permutations(x.nodes(),4):
        y=x.copy(); y.add_edges_from([(a[0],a[1]),(a[2],a[3])])
        if a[0]<a[1] and a[2]<a[3] and a[0]<a[2] and not hasK(y,5) and chi(y)>=5:
            print('8',sorted(x.edges()),a,'complement of y:',sorted(nx.complement(y).edges())); break
