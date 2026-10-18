import itertools, random, sys, time
import numpy as np, networkx as nx
from radon import max_pairs, score
from r03_conv import Qd_search, runs

def check_order(G,order,d):
    pos={v:i for i,v in enumerate(order)}
    for A,B in max_pairs(G):
        if runs(pos,A,B)>d+1: return False,(A,B)
    return True,None

# --- P-B: 2-tree insertion algorithm (the proof's construction) on a cyclic order
def two_tree(seq):
    """seq: list of (new, u, v) attaching new to existing edge uv; starts with edge (0,1)."""
    G=nx.Graph(); G.add_edge(0,1); cyc=[0,1]
    for w,u,v in seq:
        assert G.has_edge(u,v)
        C=set(G[u])&set(G[v])           # common nbrs (before w)
        i,j=cyc.index(u),cyc.index(v)
        # arcs of cyclic order between u and v
        n=len(cyc)
        arc1=[cyc[(i+k)%n] for k in range(1,(j-i)%n)]
        if any(c in arc1 for c in C):  # place w inside arc1, right after u
            cyc.insert(i+1,w)
        else:                          # arc2 (or C empty): right after v
            cyc.insert(j+1,w)
        G.add_edge(w,u); G.add_edge(w,v)
    return G,cyc

def run_P_B():
    out=[]
    # fan, book K_{1,1,m}, nested 'branchy' tree, adversarial: attach on same edge repeatedly then on new edges
    fan=[(k,0,k-1) for k in range(2,8)]
    book=[(k,0,1) for k in range(2,8)]
    rnd=random.Random(1)
    br=[]; edges=[(0,1)]
    for k in range(2,11):
        u,v=rnd.choice(edges); br.append((k,u,v)); edges+= [(k,u),(k,v)]
    for nm,s in (("fan",fan),("book",book),("branchy",br)):
        G,cyc=two_tree(s)
        ok,_=check_order(G,cyc,2)
        out.append((nm,G.number_of_nodes(),ok))
    return out

if __name__=="__main__":
    w=sys.argv[1]
    if w=="PB": print(run_P_B())
    if w=="PC":
        # diamond: u,v + a,b. R^2 coordinates
        G=nx.Graph([(0,1),(0,2),(1,2),(0,3),(1,3)])
        for nm,Y in (("opposite",[(0,0),(1,0),(.5,1),(.5,-1)]),("same",[(0,0),(1,0),(.5,1),(.5,2)])):
            Y=np.array(Y,float); print("diamond",nm,"Radon-free margin",round(score(Y,max_pairs(G)),4))
    if w=="PD":
        def W(m): 
            G=nx.wheel_graph(m+1); return G
        def bip(m):
            G=nx.cycle_graph(m); G.add_edges_from((m,i) for i in range(m)); G.add_edges_from((m+1,i) for i in range(m)); return G
        for nm,G in (("W5",W(5)),("W6",W(6))):
            print(nm,"Q2",bool(Qd_search(G,2)),"Q3",bool(Qd_search(G,3)),flush=True)
        for m in (4,5,6,7):
            print("bipyramid",m,"Q3",Qd_search(bip(m),3,60),flush=True)
        print("K33 Q1",bool(Qd_search(nx.complete_bipartite_graph(3,3),1)))
        print("K5-e Q3",Qd_search(nx.complete_graph(5).copy() if False else (lambda g:(g.remove_edge(3,4),g)[1])(nx.complete_graph(5)),3))
