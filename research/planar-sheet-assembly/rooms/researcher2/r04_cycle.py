from r04_lib import *
for n in [5,7,9,11]:
    P = nx.cycle_graph(n)
    T = [t for t in itertools.combinations(P.nodes(),3) if indep(P,t)]
    c = col_ok(P, T)
    G = assemble(P, T)
    print(n, len(T), 'witness' , c, 'chi(G)=', chi(G) if G.number_of_nodes()<=40 else '-')
