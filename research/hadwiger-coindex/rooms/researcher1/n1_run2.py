import networkx as nx, time, sys
from networkx.generators.atlas import graph_atlas_g
from n1_lib import *
def chainlen(pairs):
    # closed pairs as (A,B) both orientations; poset: (A1,B1)<(A2,B2) iff A1 proper subset A2 (then B2 proper subset B1 automatically)
    P=set()
    for a,b in pairs:
        P.add((a,b)); P.add((b,a))
    P=sorted(P,key=lambda p:bin(p[0]).count('1'))
    best={}
    for p in P:
        best[p]=1+max([best[q] for q in best if q[0]!=p[0] and q[0]&p[0]==q[0]]+[0])
    return max(best.values())
cnt=0;bad=[]
t=time.time()
for G in graph_atlas_g():
    n=G.number_of_nodes()
    if n<2 or n>7 or G.number_of_edges()==0: continue
    pairs=maxbic(G)
    # ensure single closed pairs (a,a) not present
    l=chainlen(pairs)
    z,_=rho(G,pairs)
    cnt+=1
    if l+1<z: bad.append((n,sorted(G.edges()),l,z)); print("BAD",bad[-1],flush=True)
print(cnt,len(bad),time.time()-t)
