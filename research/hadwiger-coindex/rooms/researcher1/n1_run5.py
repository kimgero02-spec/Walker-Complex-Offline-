import networkx as nx, time
from networkx.generators.atlas import graph_atlas_g
from n1_lib2 import *
from n1_run4 import poset, chains
from n1_bock import *
hits=[]
cnt=0
for G in graph_atlas_g():
    n=G.number_of_nodes()
    if n<4 or n>7 or G.number_of_edges()==0 or not nx.is_connected(G): continue
    pairs=maxbic(G)
    z=zig(n,pairs)
    if z<4: continue
    P=poset(pairs); ch=chains(P)
    if len(ch)>3: 
        continue  # only 2-dim for now
    cnt+=1
    bz=bockstein_zero(P,ch)
    if bz: hits.append((n,sorted(G.edges()),z)); print("HIT",hits[-1],flush=True)
print(cnt,len(hits))
