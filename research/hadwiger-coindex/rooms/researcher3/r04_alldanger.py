# Does a proper 5-coloring exist in which ALL 10 color pairs are dangerous (so a careless 5-coloring fails)?
from r04_lib import *
from pysat.solvers import Cadical153
def alldanger(G):
    nodes=list(G.nodes()); cnt=[0]
    def new(): cnt[0]+=1; return cnt[0]
    col={(v,k):new() for v in nodes for k in range(5)}
    S=Cadical153()
    for v in nodes:
        S.add_clause([col[v,k] for k in range(5)])
        for k in range(5):
            for l in range(k+1,5): S.add_clause([-col[v,k],-col[v,l]])
    for u,v in G.edges():
        for k in range(5): S.add_clause([-col[u,k],-col[v,k]])
    W={}
    for a,b,C in pairs_of(G):
        for p in range(5):
            for q in range(5):
                if p==q: continue
                w=new(); W[a,b,p,q]=w
                S.add_clause([-w,col[a,p]]); S.add_clause([-w,col[b,q]])
                for r in range(5):
                    if r in (p,q): continue
                    S.add_clause([-w]+[col[c,r] for c in C])
    for p in range(5):
        for q in range(p+1,5):
            S.add_clause([W[a,b,x,y] for (a,b,x,y) in W if {x,y}=={p,q}])
    if S.solve():
        m=set(l for l in S.get_model() if l>0)
        c={v:1+[k for k in range(5) if col[v,k] in m][0] for v in nodes}
        return c
    return None
for name,G in tests():
    t=time.time(); c=alldanger(G)
    print(name,"all-10-dangerous 5-coloring exists:",c is not None, round(time.time()-t,1),flush=True)
    if c:
        D=dangerous_check=None
