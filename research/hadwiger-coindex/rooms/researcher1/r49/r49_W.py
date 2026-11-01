# theta (transfer width) for the icosahedron pair W of R48-r1, shift (0,1,2)
import networkx as nx, itertools
I=nx.icosahedral_graph(); V=sorted(I)
cols=[]
def bt(i,c):
    if i==len(V): cols.append(dict(c)); return
    v=V[i]
    for x in range(4):
        if all(c.get(u)!=x for u in I[v]): c[v]=x; bt(i+1,c); del c[v]
bt(0,{})
print("#4-colourings of icosahedron",len(cols))
for sh in [(0,1,2),(0,1,5),(0,3,7),(0,4,8)]:
    X={j:[(j-s)%12 for s in sh] for j in range(12)}   # X of (2,j) inside sheet 1
    best=min(max(len({c[x] for x in X[j]}) for j in range(12)) for c in cols)
    prof=sorted(set(tuple(sorted(len({c[x] for x in X[j]}) for j in range(12))) for c in cols))
    print(sh,"theta_{1->2} =",best, " #phi with max<=2:",sum(1 for c in cols if max(len({c[x] for x in X[j]}) for j in range(12))<=2))
# one-sided framework on W: fix phi on sheet 1, sheet 2 lists {4,5} U ([4]-phi(X_v))
def listcol(G,L):
    Vs=sorted(G,key=lambda v:len(L[v])); c={}
    def go(i):
        if i==len(Vs): return True
        v=Vs[i]
        for x in L[v]:
            if all(c.get(u)!=x for u in G[v]): c[v]=x; 
            else: continue
            if go(i+1): return True
            del c[v]
        return False
    return go(0)
for sh in [(0,1,2),(0,1,5),(0,3,7)]:
    X={j:[(j-s)%12 for s in sh] for j in range(12)}
    good=sum(1 for c in cols if listcol(I,{j:[4,5]+[a for a in range(4) if a not in {c[x] for x in X[j]}] for j in range(12)}))
    print(sh,"one-sided framework succeeds for",good,"of",len(cols),"phi")
