import sys, networkx as nx, numpy as np, time
from radon import search
from r03_conv import Qd_search
w=sys.argv[1]
if w=="W5":
    Y,s,np_=search(nx.wheel_graph(6),2,iters=300,seed=1)
    print("W5 R^2 general placement:", "found" if Y is not None else "none", s if Y is None else round(s,4)); 
    if Y is not None: print(np.round(Y,3).tolist())
if w=="stack":
    def stack(faces_to_fill):
        G=nx.complete_graph(4); faces=[(0,1,2),(0,1,3),(0,2,3),(1,2,3)]; nxt=4
        for f in faces_to_fill(faces):
            pass
    # Apollonian: stack into every face of K4 (n=8), then every face of that outer-level (n=12)
    G=nx.complete_graph(4); faces=[(0,1,2),(0,1,3),(0,2,3),(1,2,3)]; nxt=4
    new=[]
    for f in faces:
        G.add_edges_from((nxt,x) for x in f); new+= [(f[0],f[1],nxt),(f[0],f[2],nxt),(f[1],f[2],nxt)]; nxt+=1
    print("Apollonian n=8 planar",nx.check_planarity(G)[0]); t=time.time()
    print("Q3 n=8:",Qd_search(G,3,120),round(time.time()-t,1),flush=True)
    G2=G.copy()
    for f in new[:4]:
        G2.add_edges_from((nxt,x) for x in f); nxt+=1
    t=time.time(); print("Q3 n=12 partial stack:",Qd_search(G2,3,150),round(time.time()-t,1),flush=True)
