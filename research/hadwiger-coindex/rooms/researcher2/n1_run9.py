import networkx as nx, itertools, time
from b0 import simplices
def circ(n,ks):
    G=nx.Graph(); G.add_nodes_from(range(n))
    for i in range(n):
        for k in ks: G.add_edge(i,(i+k)%n)
    return G
G=circ(11,(1,2,3))
S,n=simplices(G)
from collections import Counter
print(len(S),Counter(bin(A).count('1')+bin(B).count('1') for A,B in S))
