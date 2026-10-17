import random, itertools, networkx as nx, time
from r03_conv import Qd_search
def rand3tree(n,seed):
    r=random.Random(seed); G=nx.complete_graph(4); tris=[t for t in itertools.combinations(range(4),3)]
    for w in range(4,n):
        t=r.choice(tris); G.add_edges_from((w,x) for x in t)
        tris+= [tuple(sorted((a,b,w))) for a,b in itertools.combinations(t,2)]
    return G
for n,seed in [(9,0),(9,1),(9,2),(10,3),(10,4),(10,5),(11,6),(11,7)]:
    G=rand3tree(n,seed); t=time.time()
    print(n,seed,"Q3:",Qd_search(G,3,25),round(time.time()-t,1),flush=True)
