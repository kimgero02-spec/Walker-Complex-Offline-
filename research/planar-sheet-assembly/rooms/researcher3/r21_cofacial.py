# R21-researcher3: GENERATOR ONLY (not evidence). G = A u B, A,B edge-disjoint random triangulations (theta(G)<=2).
# Local search for a 3-colouring whose classes are planar and such that no edge of another class joins two
# cofacial vertices in the (computed) embedding of a class (Whitney-style heuristic for "locked").
# Any hit is written to JSON and must be re-verified by r21_verify.py (direct planarity tests).
import random, sys, json, math, networkx as nx
from r21_search import rand_tri
def emb_cost(q, others):
    H=nx.Graph(); H.add_edges_from(q)
    ok,emb=nx.check_planarity(H)
    if not ok: return 10**4
    seen=set(); cof=set()
    for u,v in emb.edges():
        if (u,v) in seen: continue
        f=emb.traverse_face(u,v,mark_half_edges=seen)
        fs=set(f)
        for a in fs:
            for b in fs:
                if a<b: cof.add((a,b))
    return sum(1 for e in others if e in cof or e[0] not in H or e[1] not in H)
def run(N, rng, steps, n=3, keep=1.0):
    A=rand_tri(N,rng,flips=10*N); B=rand_tri(N,rng,flips=10*N); EA=set(tuple(sorted(e)) for e in A.edges())
    best=None
    for _ in range(5000):
        p=list(range(N)); rng.shuffle(p); EB=set(tuple(sorted((p[u],p[v]))) for u,v in B.edges())
        if best is None or len(EA&EB)<len(EA&best): best=EB
        if not EA&EB: break
    EB=best
    EA=set(e for e in EA if rng.random()<keep); EB=set(e for e in EB if rng.random()<keep); E=sorted(EA|EB)
    col={e:rng.randrange(n) for e in E}
    def cls(k): return [e for e in E if col[e]==k]
    def cost(k): q=cls(k); return emb_cost(q,[e for e in E if col[e]!=k])
    sc=[cost(k) for k in range(n)]; cur=sum(sc)
    for it in range(steps):
        if cur==0: break
        e=rng.choice(E); old=col[e]; new=rng.choice([k for k in range(n) if k!=old]); col[e]=new
        so,sn=cost(old),cost(new); third=[k for k in range(n) if k not in (old,new)]
        st=[cost(k) for k in third]
        d=so+sn+sum(st)-sum(sc)
        T=1.5*(1-it/steps)+0.05
        if d<=0 or rng.random()<math.exp(-d/T):
            sc[old],sc[new]=so,sn
            for k,s in zip(third,st): sc[k]=s
            cur=sum(sc)
        else: col[e]=old
    return cur,E,EA,EB,col
if __name__=="__main__":
    N=int(sys.argv[1]); seed=int(sys.argv[2]); trials=int(sys.argv[3]); steps=int(sys.argv[4]); keep=float(sys.argv[5]) if len(sys.argv)>5 else 1.0
    rng=random.Random(seed)
    for t in range(trials):
        cur,E,EA,EB,col=run(N,rng,steps,keep=keep)
        print("N",N,"trial",t,"|E|",len(E),"overlap",len(EA&EB),"cost",cur,flush=True)
        if cur==0:
            Q=[[list(e) for e in E if col[e]==k] for k in range(3)]
            fn=f"r21_hit_cof_N{N}_s{seed}_t{t}.json"
            json.dump({"E":[list(e) for e in E],"A":[list(e) for e in sorted(EA)],"B":[list(e) for e in sorted(EB)],"Q":Q},open(fn,"w"))
            print("HIT",fn,flush=True)
