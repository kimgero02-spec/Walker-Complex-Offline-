import networkx as nx
from n1_lib2 import *
from n1_run4 import poset, chains
from n1_bock import *
from collections import Counter
from networkx.generators.atlas import graph_atlas_g
c=Counter()
for G in graph_atlas_g():
    n=G.number_of_nodes()
    if n<4 or n>7 or G.number_of_edges()==0 or not nx.is_connected(G): continue
    pairs=maxbic(G); P=poset(pairs); ch=chains(P)
    if len(ch)!=3: continue
    z=zig(n,pairs)
    c[(z,bockstein_zero(P,ch))]+=1
print(c)
G=nx.complement(nx.cycle_graph(7)); pairs=maxbic(G);P=poset(pairs);ch=chains(P);print(len(ch),zig(7,pairs),bockstein_zero(P,ch))
