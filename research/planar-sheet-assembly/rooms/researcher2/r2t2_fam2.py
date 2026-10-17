# s=3: realize ALL 32 families as Pi_3 of planar pieces.
# step 1: small gadgets with ports on a common face (K<=3 extra vertices)
# step 2: the two missing families as disc-gluings (P inside, P' outside a circle through the ports) = intersections
import numpy as np, itertools, networkx as nx
names=['123','12|3','13|2','23|1','1|2|3']
def pi3(H):
    n=H.number_of_nodes(); idx={v:i for i,v in enumerate(H.nodes())}
    res=set()
    # backtracking enumerate colorings restricted to ports 'x1','x2','x3'
    import sys
    order=list(nx.bfs_tree(H, 'x1')) ; rest=[v for v in H if v not in order]; order+=rest
    ports=['x1','x2','x3']
    # enumerate port colorings, test extension
    for cs in itertools.product(range(3),repeat=3):
        if cs[0]!=0: continue
        col=dict(zip(ports,cs))
        if any(H.has_edge(p,q) and col[p]==col[q] for p,q in itertools.combinations(ports,2)): continue
        free=[v for v in order if v not in col]
        def rec(i):
            if i==len(free): return True
            v=free[i]; forb={col[u] for u in H[v] if u in col}
            for c in range(3):
                if c not in forb:
                    col[v]=c
                    if rec(i+1): return True
                    del col[v]
            return False
        if rec(0):
            a,b,c=cs; k=0 if a==b==c else 1 if a==b else 2 if a==c else 3 if b==c else 4
            res.add(k)
    return frozenset(res)
def onface(H):
    H2=H.copy(); H2.add_edges_from(('apex',p) for p in ['x1','x2','x3']); return nx.check_planarity(H2)[0]
gad={}
for K in range(0,4):
    V=['x1','x2','x3']+['e%d'%i for i in range(K)]
    pairs=list(itertools.combinations(V,2))
    for mask in range(1<<len(pairs)):
        E=[pairs[i] for i in range(len(pairs)) if mask>>i&1]
        H=nx.Graph(); H.add_nodes_from(V); H.add_edges_from(E)
        if not onface(H): continue
        f=pi3(H)
        if f not in gad: gad[f]=H
print("families with a face-gadget (K<=3):",len(gad))
def disc_glue(H1,H2):
    H=nx.Graph(); 
    for t,Hh in ((1,H1),(2,H2)):
        r=lambda v:v if v in ('x1','x2','x3') else (t,v)
        H.add_nodes_from(r(v) for v in Hh); H.add_edges_from((r(a),r(b)) for a,b in Hh.edges())
    return H
allf=set(gad)
for target in [frozenset({1,2,3}), frozenset({0,4})]:
    done=False
    for f1 in list(gad):
        for f2 in list(gad):
            if f1&f2==target:
                H=disc_glue(gad[f1],gad[f2])
                assert nx.check_planarity(H)[0]
                got=pi3(H)
                print("target",[names[k] for k in sorted(target)],"=",[names[k] for k in sorted(f1)],"∩",[names[k] for k in sorted(f2)],
                      "| glued planar:",nx.check_planarity(H)[0],"| Pi3 exact:",got==target,"| edges:",sorted(map(str,H.edges())))
                allf.add(got); done=True; break
        if done: break
print("total families realized by planar pieces:",len(allf),"of 32")
