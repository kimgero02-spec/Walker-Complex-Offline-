# Gadget-level list analysis of W: for outer precoloring (x,y,z) (distinct colors from 1..6),
# is there an internal M (7 internal vertices, M(v) 2-subset of 1..4, list {5,6}+M) blocking extension?
from common import *
from pysat.solvers import Cadical153
PAIRS=list(itertools.combinations([1,2,3,4],2))
w=W(); I=[v for v in w if v not in 'xyz']
def extend(pre,M):
    s=Cadical153(); var={}; k=0
    L={v:[5,6]+list(M[v]) for v in I}
    for v in I:
        cs=[c for c in L[v] if all(pre[u]!=c for u in w[v] if u in pre)]
        if not cs: return None
        for c in cs: k+=1; var[v,c]=k
        s.add_clause([var[v,c] for c in cs])
    for u,v in w.edges():
        if u in I and v in I:
            for c in set(L[u])&set(L[v]):
                if (u,c) in var and (v,c) in var: s.add_clause([-var[u,c],-var[v,c]])
    if not s.solve(): return None
    m=set(x for x in s.get_model() if x>0)
    return {v:c for (v,c),x in var.items() if x in m}
def block(pre):
    s=Cadical153(); mv={}; k=0
    for v in I:
        for p in PAIRS: k+=1; mv[v,p]=k
        s.add_clause([mv[v,p] for p in PAIRS])
        for p,q in itertools.combinations(PAIRS,2): s.add_clause([-mv[v,p],-mv[v,q]])
    it=0
    while s.solve():
        m=set(x for x in s.get_model() if x>0); it+=1
        M={v:[p for p in PAIRS if mv[v,p] in m][0] for v in I}
        c=extend(pre,M)
        if c is None: return M,it
        s.add_clause([mv[v,p] for v in I if c[v]<=4 for p in PAIRS if c[v] not in p])
    return None,it
# representatives up to S4 on {1..4} and swap 5<->6
reps={'SSS':(1,2,3),'SST':(1,2,5),'STS':(1,5,2),'TSS':(5,1,2),'STT':(1,5,6),'TST':(5,1,6),'TTS':(5,6,1)}
for name,(a,b,c) in reps.items():
    M,it=block({'x':a,'y':b,'z':c})
    print(name,(a,b,c),'BLOCKABLE' if M else 'always extends',M if M else '','iters',it)
