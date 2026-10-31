# s=3: which families of <=3-block port partitions are Pi_3 of some planar piece (ports anywhere)?
import numpy as np, itertools, networkx as nx, sys, random
K=int(sys.argv[1]) if len(sys.argv)>1 else 4
n=3+K
cols=np.array(list(itertools.product(range(3),repeat=n)),dtype=np.int8)
cols=cols[cols[:,0]==0]           # fix color of port x1 (S3 symmetry)
# partition code of ports (x1,x2,x3): 0:'123' 1:'12|3' 2:'13|2' 3:'23|1' 4:'1|2|3'
a,b,c=cols[:,0],cols[:,1],cols[:,2]
code=np.where((a==b)&(b==c),0,np.where(a==b,1,np.where(a==c,2,np.where(b==c,3,4))))
names=['123','12|3','13|2','23|1','1|2|3']
pairs=list(itertools.combinations(range(n),2))
neq=[cols[:,i]!=cols[:,j] for i,j in pairs]
found={}
# edges: allow all pairs; enumerate masks with pruning by random order for speed
m=len(pairs)
order=list(range(1<<m)) if m<=21 else None
for mask in range(1<<m):
    ok=np.ones(len(cols),bool)
    E=[]
    for i in range(m):
        if mask>>i&1: ok&=neq[i]; E.append(pairs[i])
    fam=0
    for k in set(code[ok].tolist()): fam|=1<<k
    if fam in found: continue
    H=nx.Graph(); H.add_nodes_from(range(n)); H.add_edges_from(E)
    if nx.check_planarity(H)[0]:
        found[fam]=E
print("K=%d extra vertices: realized families %d of 32"%(K,len(found)))
miss=[f for f in range(32) if f not in found]
print("missing:",[[names[k] for k in range(5) if f>>k&1] for f in miss])
