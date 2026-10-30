# Does a triangle-gadget force the order of T={0,1,2} in every Q_3 order?  (obstruction to 3-sums)
import itertools, time, networkx as nx
from radon import max_pairs
from r03_conv import runs
def exists_with_T_order(G,d,Torder,tlimit=60):
    n=G.number_of_nodes(); pairs=max_pairs(G)
    inv={v:[] for v in range(n)}
    for i,(A,B) in enumerate(pairs):
        for v in set(A)|set(B): inv[v].append(i)
    t0=time.time()
    def dfs(prefix,pos):
        if time.time()-t0>tlimit: raise TimeoutError
        if len(prefix)==n: return True
        for v in range(n):
            if v in pos: continue
            if v in Torder:
                k=Torder.index(v)
                if any(u not in pos for u in Torder[:k]): continue
            pos[v]=len(prefix); prefix.append(v)
            ok=True
            for i in inv[v]:
                A,B=pairs[i]; A2=[a for a in A if a in pos]; B2=[b for b in B if b in pos]
                if A2 and B2 and runs(pos,A2,B2)>d+1: ok=False;break
            if ok and dfs(prefix,pos): return True
            prefix.pop(); del pos[v]
        return False
    return dfs([],{})
def gadget(a01,a02,a12,tri):
    G=nx.Graph([(0,1),(0,2),(1,2)]); nxt=3
    for (i,j),a in (((0,1),a01),((0,2),a02),((1,2),a12)):
        for _ in range(a): G.add_edges_from([(nxt,i),(nxt,j)]); nxt+=1
    for _ in range(tri): G.add_edges_from([(nxt,0),(nxt,1),(nxt,2)]); nxt+=1
    return G
if __name__=="__main__":
    for (a,b,c,t) in [(2,0,0,0),(2,2,0,0),(2,2,2,0),(0,0,0,2),(1,0,0,2),(2,0,0,2),(2,1,0,2),(2,2,0,1),(0,0,0,3),(1,1,1,2)]:
        G=gadget(a,b,c,t)
        res={}
        for mid in range(3):
            others=[x for x in range(3) if x!=mid]
            Tord=[others[0],mid,others[1]]
            res[mid]=exists_with_T_order(G,3,Tord)
        print((a,b,c,t),"n=",G.number_of_nodes(),"planar",nx.check_planarity(G)[0],"middle=v feasible:",res,flush=True)
