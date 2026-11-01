# R03 researcher3: moment-curve criterion Q_d  (linear order, every biclique has <= d+1 label runs)
import itertools, sys, time, random
import numpy as np, networkx as nx
from radon import max_pairs, score
from scipy.optimize import linprog

def runs(order_pos, A, B):
    pts=sorted([(order_pos[a],0) for a in A]+[(order_pos[b],1) for b in B])
    r=1
    for i in range(1,len(pts)):
        if pts[i][1]!=pts[i-1][1]: r+=1
    return r

def Qd_search(G,d,tlimit=60):
    G=nx.convert_node_labels_to_integers(G); n=G.number_of_nodes()
    pairs=max_pairs(G)
    pairs=[(A,B) for A,B in pairs if len(A)>=1 and len(B)>=1]
    t0=time.time(); sol=[None]
    inv={v:[] for v in range(n)}
    for i,(A,B) in enumerate(pairs):
        for v in set(A)|set(B): inv[v].append(i)
    def dfs(prefix,pos):
        if time.time()-t0>tlimit: raise TimeoutError
        if len(prefix)==n: sol[0]=list(prefix); return True
        for v in range(n):
            if v in pos: continue
            pos[v]=len(prefix); prefix.append(v)
            ok=True
            for i in inv[v]:
                A,B=pairs[i]
                A2=[a for a in A if a in pos]; B2=[b for b in B if b in pos]
                if A2 and B2 and runs(pos,A2,B2)>d+1: ok=False;break
            if ok and dfs(prefix,pos): return True
            prefix.pop(); del pos[v]
        return False
    try:
        r=dfs([],{})
    except TimeoutError:
        return None
    return sol[0] if r else False

def hulls_meet(P,Xi,Yi):
    d=P.shape[1]; nx_,ny=len(Xi),len(Yi)
    Aeq=np.zeros((d+2,nx_+ny)); beq=np.zeros(d+2)
    Aeq[:d,:nx_]=P[Xi].T; Aeq[:d,nx_:]=-P[Yi].T
    Aeq[d,:nx_]=1; beq[d]=1; Aeq[d+1,nx_:]=1; beq[d+1]=1
    r=linprog(np.zeros(nx_+ny),A_eq=Aeq,b_eq=beq,bounds=[(0,None)]*(nx_+ny),method='highs')
    return r.status==0

if __name__=="__main__":
    which=sys.argv[1]
    if which=="T0":   # K1,K2,K3 offsets
        for n in (2,3,4,5):
            G=nx.complete_graph(n)
            print("K%d"%n,[ (d,bool(Qd_search(G,d))) for d in range(1,n)])
    if which=="T6":   # lemma: hulls on moment curve meet <=> runs >= d+2  (exhaustive labelings, N points)
        N=7; bad=0; tot=0
        for d in (2,3,4):
            t=np.arange(1,N+1)/N
            P=np.stack([t**k for k in range(1,d+1)],axis=1)
            for lab in itertools.product((0,1),repeat=N):
                X=[i for i in range(N) if lab[i]==0]; Y=[i for i in range(N) if lab[i]==1]
                if not X or not Y: continue
                r=1+sum(lab[i]!=lab[i-1] for i in range(1,N))
                # runs over *labelled* sequence = runs of X/Y
                meet=hulls_meet(P,X,Y); tot+=1
                if meet!=(r>=d+2): bad+=1; print("MISMATCH",d,lab,meet,r)
        print("T6 lemma checks",tot,"mismatches",bad)
