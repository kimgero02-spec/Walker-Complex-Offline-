# R21-researcher3: GENERATOR (not evidence). Random-walk exchange search for a planar 2-cover A,B of the
# graph E(G)= union of the sheets in a JSON file. A hit is written out and re-verified by direct planarity tests.
import sys, json, random, networkx as nx
def planar(E):
    H=nx.Graph(); H.add_edges_from(E); return nx.check_planarity(H)[0]
def kur(E):
    H=nx.Graph(); H.add_edges_from(E); ok,K=nx.check_planarity(H,counterexample=True)
    return None if ok else [tuple(sorted(e)) for e in K.edges()]
def greedy(order):
    S=[]
    for e in order:
        if planar(S+[e]): S.append(e)
    return S
if __name__=="__main__":
    fn=sys.argv[1]; seed=int(sys.argv[2]); STEPS=int(sys.argv[3]); rng=random.Random(seed)
    d=json.load(open(fn)); E=sorted(set(tuple(sorted(e)) for q in d["Q"] for e in q))
    order=E[:]; rng.shuffle(order); A=set(greedy(order)); rest=[e for e in order if e not in A]
    B=set(greedy(rest)); L=[e for e in rest if e not in B]; best=len(L)
    print("start leftover",len(L),flush=True)
    tabu={}
    for it in range(STEPS):
        if not L: break
        e=L.pop(rng.randrange(len(L))); X=rng.choice([A,B]); Y=B if X is A else A
        if planar(list(X)+[e]): X.add(e); continue
        if planar(list(Y)+[e]): Y.add(e); continue
        K=kur(list(X)+[e]); cand=[f for f in K if f!=e and tabu.get(f,-1)<it]
        if not cand: L.append(e); continue
        f=rng.choice(cand); X.discard(f); X.add(e); tabu[e]=it+5
        if planar(list(X)): L.append(f)
        else: X.discard(e); X.add(f); L.append(e)
        if len(L)<best: best=len(L); print("it",it,"leftover",best,flush=True)
    print("final leftover",len(L))
    if not L:
        ok=planar(list(A)) and planar(list(B)) and A|B==set(E)
        print("2-cover found; direct check A planar, B planar, A u B = E :",ok)
        json.dump({"A":[list(e) for e in sorted(A)],"B":[list(e) for e in sorted(B)]},open(fn.replace(".json","_2cover.json"),"w"))
