import itertools, networkx as nx, sys
sys.argv=['x']
exec(open('c1_convex.py').read().split('for n in [6,8,10]:')[0])
for n in [8,10,12]:
    L=zigzag(n); hull={tuple(sorted((i,(i+1)%n))) for i in range(n)}
    A=L[0]-hull; B=L[1]-hull
    C=nx.Graph(); C.add_nodes_from(A|B); C.add_edges_from((e,f) for e in A for f in B if cross(e,f))
    print(n,"adjacent zigzag: X",C.number_of_edges(),"max cross-degree",max(d for _,d in C.degree()),"is path:",max(d for _,d in C.degree())<=2 and nx.is_tree(C))
