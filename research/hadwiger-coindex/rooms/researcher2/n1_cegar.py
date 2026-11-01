# CEGAR: is there a graph on n vertices with an antisymmetric arc-labeling by +-[k] (no antipodal on any 4-walk)
# such that EVERY vertex order has an alternating biclique pattern of length k+2 (zig >= k+2)?  k=2: convex C4.
import itertools, sys, time, networkx as nx
from pysat.solvers import Cadical153
from n1_zig import zig_le
def run(n,k,t,tlimit=250):
    cnt=0
    E={}
    for u in range(n):
        for v in range(u+1,n):
            cnt+=1;E[(u,v)]=cnt
    e=lambda u,v:E[(u,v)] if u<v else E[(v,u)]
    labs=[(i,s) for i in range(k) for s in (1,-1)]
    L={}
    for u in range(n):
        for v in range(n):
            if u!=v:
                for x in labs:
                    cnt+=1;L[(u,v,x)]=cnt
    S=Cadical153()
    neg=lambda x:(x[0],-x[1])
    for u in range(n):
        for v in range(u+1,n):
            for x in labs:
                S.add_clause([-L[(u,v,x)],L[(v,u,neg(x))]]); S.add_clause([-L[(v,u,x)],L[(u,v,neg(x))]])
            S.add_clause([-e(u,v)]+[L[(u,v,x)] for x in labs])
            for x,y in itertools.combinations(labs,2):
                S.add_clause([-L[(u,v,x)],-L[(u,v,y)]])
    for a in range(n):
        for a2 in range(n):
            for b in range(n):
                for b2 in range(n):
                    if len({a,b})<2 or len({a2,b2})<2 or len({a,b2})<2 or len({a2,b})<2: continue
                    if a==a2 and b==b2: continue
                    for x in labs:
                        S.add_clause([-e(a,b),-e(a,b2),-e(a2,b),-e(a2,b2),-L[(a,b,x)],-L[(a2,b2,neg(x))]])
    # symmetry breaking light: none
    t0=time.time(); it=0
    aux=cnt
    while True:
        if time.time()-t0>tlimit: return 'timeout',it
        if not S.solve(): return 'UNSAT',it
        m=set(l for l in S.get_model() if l>0)
        G=nx.Graph(); G.add_nodes_from(range(n))
        for (u,v),var in E.items():
            if var in m: G.add_edge(u,v)
        pass
        r,order=zig_le(G,t,True)
        if not r: return ('SAT',sorted(G.edges())),it
        it+=1
        # block: G must contain convex pattern of length k+2 wrt this order (k=2 -> convex C4; implement k=2 and general via alternating tuples)
        L2=t+1
        ys=[]
        for pos in itertools.combinations(range(n),L2):
            vs=[order[p] for p in pos]
            lits=[]
            for i in range(L2):
                for j in range(i+1,L2):
                    if (j-i)%2==1: lits.append(e(vs[i],vs[j]))
            aux+=1; ys.append(aux)
            for l in lits: S.add_clause([-aux,l])
        S.add_clause(ys)
if __name__=="__main__":
    n=int(sys.argv[1]);k=int(sys.argv[2]);t=int(sys.argv[3]);tl=float(sys.argv[4]) if len(sys.argv)>4 else 250
    print(n,k,t,run(n,k,t,tl),flush=True)
