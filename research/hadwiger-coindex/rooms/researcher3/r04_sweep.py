import numpy as np, networkx as nx, itertools, sys
from r04_sat import *
from r04_hard import flips
def tutte(G,outer):
    nodes=list(G.nodes()); idx={v:i for i,v in enumerate(nodes)}; n=len(nodes)
    A=np.zeros((n,n)); bx=np.zeros((n,2))
    ang=[0,2*np.pi/3,4*np.pi/3]
    fixed={o:np.array([np.cos(a),np.sin(a)]) for o,a in zip(outer,ang)}
    for v in nodes:
        i=idx[v]
        if v in fixed: A[i,i]=1; bx[i]=fixed[v]
        else:
            A[i,i]=G.degree(v)
            for u in G[v]: A[i,idx[u]]-=1
    P=np.linalg.solve(A,bx); return {v:P[idx[v]] for v in nodes}
def viol(G,order):
    pos={v:i for i,v in enumerate(order)}; c=0
    for a,b,C in pairs_of(G):
        lo,hi=sorted((pos[a],pos[b]))
        if len(set(0 if pos[x]<lo else (1 if pos[x]<hi else 2) for x in C))==3: c+=1
    return c
def faces_tri(G):
    return [t for t in itertools.combinations(G.nodes(),3) if G.has_edge(t[0],t[1]) and G.has_edge(t[1],t[2]) and G.has_edge(t[0],t[2])]
if __name__=="__main__":
    tests=[("stacked40",stacked(1,40)),("flip40",flips(tri_graph(1,40),800,1)),("delaunay60",tri_graph(2,60)),("flip60",flips(tri_graph(0,60),1200,0))]
    for name,G in tests:
        ok,emb=nx.check_planarity(G)
        # real faces
        seen=set(); fs=[]
        for u,v in emb.edges():
            f=emb.traverse_face(u,v)
            if len(f)==3 and frozenset(f) not in seen: seen.add(frozenset(f)); fs.append(f)
        best=(10**9,None)
        for f in fs[:6]:
            P=tutte(G,f)
            for th in np.linspace(0,np.pi,37)[:-1]:
                d=np.array([np.cos(th),np.sin(th)])
                o=sorted(G.nodes(),key=lambda v:P[v]@d)
                x=viol(G,o)
                if x<best[0]: best=(x,(f,th))
        print(name,"pairs",len(pairs_of(G)),"min sweep violations",best[0],flush=True)
