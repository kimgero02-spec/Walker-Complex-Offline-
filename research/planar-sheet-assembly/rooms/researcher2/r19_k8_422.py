# try ONE realization of chi-profile {4,2,2} (4-piece K4-free) for K_8, via fiber labels f:V->{0,1}^2
import networkx as nx, random, itertools, sys
from r19_lib import *
def attempt(seed,sizes):
    rnd=random.Random(seed)
    lab=[]
    for t,s in zip([(0,0),(0,1),(1,0),(1,1)],sizes): lab+= [t]*s
    N=len(lab)
    P=nx.Graph(); B1=nx.Graph(); B2=nx.Graph()
    for G in (P,B1,B2): G.add_nodes_from(range(N))
    E=list(itertools.combinations(range(N),2)); rnd.shuffle(E)
    for u,v in E:
        opts=[]
        if lab[u][0]!=lab[v][0]: opts.append(B1)
        if lab[u][1]!=lab[v][1]: opts.append(B2)
        rnd.shuffle(opts)
        if rnd.random()<0.5: opts.append(P)
        else: opts.insert(0,P)
        if lab[u]==lab[v]: opts=[P]
        for G in opts:
            G.add_edge(u,v)
            if planar(G) and (G is not P or omega(G)<=3): break
            G.remove_edge(u,v)
        else: return None
    if chi(P)==4: return P,B1,B2
for sizes in [(3,3,1,1),(2,2,2,2),(3,2,2,1),(3,3,2,0),(3,2,1,2)]:
    for s in range(3000):
        r=attempt(s,sizes)
        if r:
            print("sizes",sizes,"seed",s); report(8,list(r),"K8 {4,2,2}")
            print([sorted(G.edges()) for G in r]); sys.exit()
print("none found")
