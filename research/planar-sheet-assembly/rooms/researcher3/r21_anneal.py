# R21-researcher3: GENERATOR ONLY (not evidence). Anneal an edge 3-colouring of G=A u B (A,B planar triangulations)
# toward a locked partition. Any hit is re-verified by r21_verify.py with direct planarity tests.
import random, sys, json, networkx as nx
from r21_search import rand_tri, planar
def bad(cls, k, E, col):
    q=[e for e in E if col[e]==k]
    if not planar(q): return 1000
    return sum(1 for e in E if col[e]!=k and planar(q+[e]))
if __name__=="__main__":
    N=int(sys.argv[1]); rng=random.Random(int(sys.argv[2])); trials=int(sys.argv[3]); n=int(sys.argv[4]); STEPS=int(sys.argv[5])
    for t in range(trials):
        A=rand_tri(N,rng); B=rand_tri(N,rng); EA=set(tuple(sorted(e)) for e in A.edges())
        best=None
        for _ in range(2000):
            p=list(range(N)); rng.shuffle(p); EB=set(tuple(sorted((p[u],p[v]))) for u,v in B.edges())
            if best is None or len(EA&EB)<len(EA&best): best=EB
            if not EA&EB: break
        EB=best
        E=sorted(EA|EB)
        if planar(E): continue
        col={e:rng.randrange(n) for e in E}
        sc=[bad(None,k,E,col) for k in range(n)]; cur=sum(sc); T0=2.0
        for it in range(STEPS):
            if cur==0: break
            e=rng.choice(E); old=col[e]; new=rng.choice([k for k in range(n) if k!=old])
            col[e]=new; so,sn=bad(None,old,E,col),bad(None,new,E,col)
            d=so+sn-sc[old]-sc[new]; T=T0*(1-it/STEPS)+0.05
            if d<=0 or rng.random()<pow(2.718,-d/T): sc[old],sc[new]=so,sn; cur+=d
            else: col[e]=old
        print("trial",t,"N",N,"|E|",len(E),"cost",cur,flush=True)
        if cur==0:
            Q=[[list(e) for e in E if col[e]==k] for k in range(n)]
            json.dump({"E":[list(e) for e in E],"A":[list(e) for e in sorted(EA)],"B":[list(e) for e in sorted(EB)],"Q":Q},open(f"r21_hit_N{N}_n{n}.json","w"))
            print("HIT saved"); sys.exit()
