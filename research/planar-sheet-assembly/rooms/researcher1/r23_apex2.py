import sys, json, networkx as nx
from r23_penta import dense_planar_girth5
from r23_apex import find_S
for n in range(int(sys.argv[1]),int(sys.argv[2])+1,10):
    for sd in range(int(sys.argv[3])):
        G=dense_planar_girth5(n,sd)
        S,it=find_S(G,maxit=20000)
        print(G.number_of_nodes(),sd,G.number_of_edges(),'S=',S if not isinstance(S,list) else ('FOUND',len(S)),it,flush=True)
        if isinstance(S,list):
            json.dump(dict(E=[list(map(int,e)) for e in G.edges()],S=list(map(int,S))),open(f'r23_apexD_{n}_{sd}.json','w'))
