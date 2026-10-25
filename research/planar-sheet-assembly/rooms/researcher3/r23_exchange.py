# R23-researcher3: CHECK of the construction in Theorem 2.1 (coordinatewise exchange), not evidence.
# Given covers P=(P_1..P_a), P'=(P'_1..P'_a) of G and b buffers, build the explicit zigzag of the proof:
# transition j: add X_j-pieces in free slots, shrink coord j to P_j∩P'_j, grow to P'_j, drop X_{j-1}-pieces.
# Every object is checked directly: each piece planar, union of pieces = E, consecutive objects comparable.
import json, random, itertools, networkx as nx
def planar(E):
    if not E: return True
    H=nx.Graph(); H.add_edges_from(E); return nx.check_planarity(H)[0]
def planar_split(S):        # greedy planar pieces of edge set S (number of pieces >= theta(S); used as decomposition)
    pieces=[]
    for e in sorted(S):
        for p in pieces:
            if planar(p|{e}): p.add(e); break
        else: pieces.append({e})
    return pieces
def zigzag(E,P,Pp,b,split=None):
    a=len(P); split=split or planar_split
    X=[set(E)-set().union(*(Pp[:j]+P[j:])) for j in range(a+1)]
    assert not X[0] and not X[a]
    main=[set(p) for p in P]; slots=[set() for _ in range(b)]; cur={}   # cur: slot -> owner j
    objs=[]; snap=lambda: objs.append([set(p) for p in main]+[set(s) for s in slots])
    snap(); need=0
    for j in range(1,a+1):
        pcs=split(X[j]); free=[s for s in range(b) if s not in cur]
        need=max(need,len(cur)+len(pcs))
        if len(pcs)>len(free): return None,need,X
        for s,pc in zip(free,pcs): slots[s]=set(pc); cur[s]=j
        snap()
        main[j-1]=main[j-1]&Pp[j-1]; snap()
        main[j-1]=set(Pp[j-1]); snap()
        for s in [s for s,o in cur.items() if o==j-1]: slots[s]=set(); del cur[s]
        snap()
    for s in list(cur): slots[s]=set()
    snap()
    ok=True
    for i,o in enumerate(objs):
        if not all(planar(p) for p in o) or set().union(*o)!=set(E): ok=False
        if i and not (all(x<=y for x,y in zip(o,objs[i-1])) or all(x>=y for x,y in zip(o,objs[i-1])) ): ok=False
    return ok,need,X
def rand_cover(E,rng,maxp):
    P=[set() for _ in range(maxp)]; L=list(E); rng.shuffle(L)
    for e in L:
        ks=list(range(maxp)); rng.shuffle(ks)
        for k in ks:
            if planar(P[k]|{e}): P[k].add(e); break
        else: return None
    return P
def norm(L): return [tuple(sorted(map(int,e))) for e in L]
if __name__=="__main__":
    Q=[set(norm(q)) for q in json.load(open('r20_locked_only_N80_n3.json'))['Q']]
    R=[set(norm(r)) for r in json.load(open('r21_g80_other_cover.json'))['R']]
    E=set().union(*Q)
    print("G80: R -> Q, b=2:", zigzag(E,R,Q,2)[:2], "  thickness bounds of X_j: |X_j| =",[len(x) for x in zigzag(E,R,Q,2)[2]])
    print("G80: R -> Q, b=1:", zigzag(E,R,Q,1)[:2])
    rng=random.Random(1)
    for name,G,th in [("K5",nx.complete_graph(5),2),("K33",nx.complete_bipartite_graph(3,3),2),("K8",nx.complete_graph(8),2),("K9",nx.complete_graph(9),3)]:
        E=set(tuple(sorted(e)) for e in G.edges()); res=[]
        for t in range(6):
            a=th+rng.randint(0,1)
            P=rand_cover(E,rng,a); Pp=rand_cover(E,rng,th)
            if P is None or Pp is None: continue
            Pp=Pp+[set() for _ in range(a-th)]   # T padded with empty (point) pieces at the end
            res.append(zigzag(E,P,Pp,th-1)[:2])
        print(name,"theta",th,"b=theta-1 results (ok,slots used):",res)
