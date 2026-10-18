# R20-researcher3: generator for a locked planar 3-partition of some G subset of K_N (N<=9), with planar 2-cover check.
# state: each pair of K_N -> 0 (absent) or piece 1..3. Cost = #(piece k, edge e of G not in Q_k, Q_k+e planar)
#        + penalty for nonplanar pieces / empty pieces. Generator only; certificate rechecked directly.
import random, sys, itertools, json
import networkx as nx
def planar(E):
    H=nx.Graph(); H.add_edges_from(E); return nx.check_planarity(H)[0]
def cost(st, pairs):
    Q=[[p for p in pairs if st[p]==k] for k in (1,2,3)]
    c=0
    for q in Q:
        if not q: c+=50; continue
        if not planar(q): c+=50; continue
    if c: return c,Q
    G=[p for p in pairs if st[p]]
    for q in Q:
        S=set(q)
        for e in G:
            if e not in S and planar(q+[e]): c+=1
    return c,Q
def cover2(E,rng,tries=3000):
    for _ in range(tries):
        o=E[:]; rng.shuffle(o); P=[[],[]]; ok=True
        for e in o:
            js=[0,1]; rng.shuffle(js)
            for j in js:
                if planar(P[j]+[e]): P[j].append(e); break
            else: ok=False; break
        if ok: return P
N=int(sys.argv[1]); rng=random.Random(int(sys.argv[2])); iters=int(sys.argv[3])
pairs=list(itertools.combinations(range(N),2))
st={p:rng.choice([1,2,3]) for p in pairs}
cur,Q=cost(st,pairs)
for it in range(iters):
    p=rng.choice(pairs); old=st[p]; st[p]=rng.choice([x for x in (0,1,2,3) if x!=old])
    c,Q=cost(st,pairs)
    if c<=cur or rng.random()<0.02: cur=c
    else: st[p]=old
    if cur==0:
        c,Q=cost(st,pairs); G=[p for p in pairs if st[p]]
        if planar(G): st[p]=old; cur,Q=cost(st,pairs); continue
        T=cover2(G,rng)
        print("LOCKED it",it,"|E|",len(G),[len(q) for q in Q],"cover2",bool(T),flush=True)
        if T:
            json.dump({"N":N,"Q":Q,"T":T},open("r20_small_cert_N%d.json"%N,"w")); print("Q=",Q); print("T=",T); break
        else:
            st[p]=old; cur,Q=cost(st,pairs)
print("end cur",cur)
