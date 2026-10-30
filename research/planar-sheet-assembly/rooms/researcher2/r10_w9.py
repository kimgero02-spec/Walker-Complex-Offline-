# R10: look for a hub split of W_9 / W_11 with kappa_H(u,v)>=4 (targeted construction search, not evidence)
import itertools, networkx as nx, sys
from r10_wheel import build, analyze
n=int(sys.argv[1])
def ok3(Su,Sv):  # fast 3-colorability of G via rim constraints: u=0,v=1
    allowed=[ {0,1,2}-({0} if i in Su else set())-({1} if i in Sv else set()) for i in range(n)]
    # cycle list coloring by DP
    for a in allowed[0]:
        cur={a}
        for i in range(1,n):
            cur={b for b in allowed[i] if any(b!=x for x in cur)} if len(cur)>1 else {b for b in allowed[i] if b not in cur}
        # crude: exact check below
    return True
found=0
for Su in itertools.combinations(range(n),4):
    if Su[0]!=0: continue
    rest=[i for i in range(n) if i not in Su]
    for k in range(0,3):
        for ov in itertools.combinations(Su,k):
            Sv=tuple(sorted(rest+list(ov)))
            G=build(n,Su,Sv); H=G.copy(); H.remove_edge('u','v')
            if nx.node_connectivity(H,'u','v')<4: continue
            a=analyze(G)
            if a and a['danger'] and not a['t4'] and not a['t5']:
                print(Su,Sv,a); found+=1
                if found>=3: sys.exit()
