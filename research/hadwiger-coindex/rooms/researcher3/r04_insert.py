# Conjecture C1: any pair-valid order of the retriangulated G-v extends to a pair-valid order of G by inserting v.
from r04_lib import *
import random
def valid(G,order): return nviol(G,order)==0
def retri(G,v):
    # remove v (deg<=5), retriangulate the hole by a fan from a random neighbour; need planar embedding for cyclic order
    ok,emb=nx.check_planarity(G); nb=list(emb.neighbors_cw_order(v)); H=G.copy(); H.remove_node(v)
    r=random.randrange(len(nb))
    for j in range(len(nb)):
        if j!=r and abs(j-r)%len(nb) not in (1,len(nb)-1) : H.add_edge(nb[r],nb[j])
    # for deg 5 with fan from r: edges r-(r+2),r-(r+3)
    return H,nb
def walk(H,order,steps):
    order=list(order)
    for _ in range(steps):
        i=random.randrange(len(order)-1); j=random.randrange(len(order)); 
        o2=order[:]; x=o2.pop(i); o2.insert(j,x)
        if valid(H,o2): order=o2
    return order
def slots(G,v,order):
    c=0
    for p in range(len(order)+1):
        o=order[:p]+[v]+order[p:]
        if valid(G,o): c+=1
    return c
random.seed(1)
for name,G in tests():
    if G.number_of_nodes()>40: continue
    worst=10**9; tot=0
    vs=[v for v in G if G.degree(v)<=5]
    for v in vs[:6]:
        for rep in range(4):
            H,nb=retri(G,v)
            o,_=solve(H)
            if not o: print("H unsat?!"); continue
            o=walk(H,o,300)
            s=slots(G,v,o); worst=min(worst,s); tot+=1
            if s==0: print("  ** NO SLOT",name,"v",v,"deg",G.degree(v)); 
    print(name,"tested",tot,"min free slots",worst,flush=True)
