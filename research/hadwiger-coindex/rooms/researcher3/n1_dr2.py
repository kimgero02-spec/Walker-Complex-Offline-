import networkx as nx, itertools, random, sys
from networkx.generators.atlas import graph_atlas_g
exec(open('n1_q2.py').read().split("t=time.time()")[0])
def conds(G):
    A={v:set(G[v]) for v in G}
    T=[]  # (x,(y1,y2,y3)) point in triangle
    for x in G:
        for ys in itertools.combinations(sorted(A[x]),3): T.append((x,ys))
    S=[]  # crossing segments
    for (p,q),(r,s) in c4s(G): S.append((p,q,r,s))
    return T,S
def orient(P,a,b,c): return (P[b][0]-P[a][0])*(P[c][1]-P[a][1])-(P[b][1]-P[a][1])*(P[c][0]-P[a][0])
def viol(P,T,S):
    c=0
    for x,(a,b,d) in T:
        o1,o2,o3=orient(P,a,b,x),orient(P,b,d,x),orient(P,d,a,x)
        if (o1>0 and o2>0 and o3>0) or (o1<0 and o2<0 and o3<0): c+=1
    for p,q,r,s in S:
        if orient(P,p,q,r)*orient(P,p,q,s)<0 and orient(P,r,s,p)*orient(P,r,s,q)<0: c+=1
    return c
def search(G,iters=40000,seed=0):
    random.seed(seed); nodes=sorted(G); T,S=conds(G)
    best=None
    for restart in range(30):
        P={v:(random.random(),random.random()) for v in nodes}
        cur=viol(P,T,S)
        for it in range(iters//30):
            if cur==0: return P
            v=random.choice(nodes); old=P[v]
            sc=random.choice([0.3,0.05,1.0])
            P[v]=(old[0]+random.gauss(0,sc),old[1]+random.gauss(0,sc))
            nv=viol(P,T,S)
            if nv<=cur or random.random()<0.02: cur=nv
            else: P[v]=old
    return None
if __name__=="__main__":
    atlas=graph_atlas_g()
    for i in [187,775,777,951,968,974,1005,1079,1095,1097,1104,1167,1212]:
        G=atlas[i]
        P=search(G)
        print(i,G.number_of_nodes(),G.number_of_edges(),"planar placement:", "FOUND" if P else "none", flush=True)
        if P: print(sorted(G.edges()),P)
