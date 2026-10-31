import itertools, networkx as nx
from r04_sat import pairs_of, check
E=[(0, 1), (0, 2), (0, 3), (0, 5), (0, 6), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (3, 4), (3, 6)]
G=nx.Graph(E); print(nx.check_planarity(G)[0], "pairs>=3:",pairs_of(G))
T=(0,2,3); R=[v for v in G if v not in T]
cnt=0; tot=0
for p in itertools.permutations(R):
    for q in itertools.permutations(T):
        tot+=1; cnt+=check(G,list(p)+list(q))
print("T-last valid orders:",cnt,"of",tot)
allv=sum(check(G,list(p)) for p in itertools.permutations(G.nodes()))
print("all valid orders:",allv,"of 5040")
# T-first, and T consecutive anywhere
cons=0
for p in itertools.permutations(G.nodes()):
    pos={v:i for i,v in enumerate(p)}
    s=sorted(pos[t] for t in T)
    if s[2]-s[0]==2 and check(G,list(p)): cons+=1
print("valid with T consecutive:",cons)
