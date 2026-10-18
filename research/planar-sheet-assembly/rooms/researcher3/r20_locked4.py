# R20-researcher3: generator for a LOCKED planar n-partition (n=4 by default) of G with a certified planar (n-1)-cover.
# Pieces = relabeled 3-connected cubic planar graphs (duals of degree-balanced random triangulations).
# Generator only; certify() re-checks with direct planarity tests (no Whitney shortcut).
import random, sys, json
import networkx as nx
from r20_locked import planar, dual_cubic

def bal_tri(t, rng, rounds=4000):
    G = nx.Graph(); G.add_edges_from([(0,1),(1,2),(0,2)]); faces=[(0,1,2),(0,2,1)]
    for v in range(3,t):
        a,b,c = faces.pop(rng.randrange(len(faces)))
        G.add_edges_from([(v,a),(v,b),(v,c)]); faces += [(a,b,v),(b,c,v),(c,a,v)]
    for _ in range(rounds):
        u,v = rng.choice(list(G.edges())); cn=list(nx.common_neighbors(G,u,v))
        if len(cn)!=2: continue
        x,y=cn
        if G.has_edge(x,y): continue
        d=G.degree
        if (d[u]-1-6)**2+(d[v]-1-6)**2+(d[x]+1-6)**2+(d[y]+1-6)**2 >= (d[u]-6)**2+(d[v]-6)**2+(d[x]-6)**2+(d[y]-6)**2: continue
        if d[u]<=3 or d[v]<=3: continue
        G.remove_edge(u,v); G.add_edge(x,y)
        if not nx.check_planarity(G)[0]: G.remove_edge(x,y); G.add_edge(u,v)
    return G

def certify(Q, T):
    allE=[e for q in Q for e in q]
    assert len(set(allE))==len(allE)
    for j,q in enumerate(Q):
        assert planar(q) and len(set(v for e in q for v in e))==len(set(v for e in allE for v in e))
        S=set(q)
        for e in allE:
            if e not in S: assert not planar(q+[e]), (j,e)
    for t in T: assert planar(t)
    assert set().union(*map(set,T))==set(allE) and not planar(allE)
    return True

def cover(E, m, rng, tries):
    for _ in range(tries):
        order=E[:]; rng.shuffle(order); H=[nx.Graph() for _ in range(m)]; ok=True
        for e in order:
            js=list(range(m)); rng.shuffle(js); placed=False
            for j in js:
                H[j].add_edge(*e)
                if nx.check_planarity(H[j])[0]: placed=True; break
                H[j].remove_edge(*e)
            if not placed: ok=False; break
        if ok: return [sorted(tuple(sorted(e)) for e in h.edges()) for h in H]
    return None

if __name__=="__main__":
    t=int(sys.argv[1]); n=int(sys.argv[2]); rng=random.Random(int(sys.argv[3])); iters=int(sys.argv[4])
    base=[dual_cubic(bal_tri(t,rng)) for _ in range(n)]
    N=base[0][2]
    P=[list(range(N)) for _ in range(n)]
    for p in P[1:]: rng.shuffle(p)
    def build(k):
        E,vf,_=base[k]; p=P[k]
        return [tuple(sorted((p[a],p[b]))) for a,b in E], {p[i]:s for i,s in vf.items()}
    QV=[build(k) for k in range(n)]
    def viol():
        bad=[]
        for j in range(n):
            for e in QV[j][0]:
                for k in range(n):
                    if k!=j and QV[k][1][e[0]] & QV[k][1][e[1]]: bad.append((j,k,e))
        return bad
    bad=viol(); cur=len(bad); T0=2.0
    for it in range(iters):
        if cur==0: break
        j,k,e=rng.choice(bad); kk=rng.choice([x for x in (j,k) if x!=0] or [k if k else j])
        if kk==0: continue
        a=rng.choice(e); b=rng.randrange(N)
        # swap labels a,b in piece kk
        p=P[kk]; ia=p.index(a); ib=p.index(b); p[ia],p[ib]=p[ib],p[ia]
        QV[kk]=build(kk); nb=viol(); c=len(nb)
        temp=T0*(1-it/iters)+0.05
        if c<=cur or rng.random()<pow(2.718,-(c-cur)/temp): cur=c; bad=nb
        else: p[ia],p[ib]=p[ib],p[ia]; QV[kk]=build(kk)
    print("N",N,"n",n,"violations",cur,"it",it, flush=True)
    if cur==0:
        Q=[sorted(q) for q,_ in QV]; E=[e for q in Q for e in q]
        T=cover(E,n-1,rng,200)
        print("cover found" if T else "no cover")
        if T and certify(Q,T):
            print("CERTIFIED")
            json.dump({"Q":Q,"T":T},open("r20_locked_cert_N%d_n%d.json"%(N,n),"w"))
