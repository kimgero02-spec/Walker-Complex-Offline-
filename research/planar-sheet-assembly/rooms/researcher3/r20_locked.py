# R20-researcher3: search generator for a LOCKED (saturated) planar 3-partition Q1|Q2|Q3 of a graph G with theta(G)=2.
# Q_k: relabeled 3-connected cubic planar graphs (duals of random triangulations).
# Whitney: for 3-connected planar Q, Q+uv planar iff u,v cofacial. Search = generator only; certify() re-checks
# everything by direct planarity tests (networkx), independent of the cofacial shortcut.
import random, sys, itertools
import networkx as nx

def planar(E):
    H = nx.Graph(); H.add_edges_from(E); return nx.check_planarity(H)[0]

def rand_tri(t, rng, flips=300):
    G = nx.Graph(); G.add_edges_from([(0,1),(1,2),(0,2)]); faces=[(0,1,2),(0,2,1)]
    for v in range(3,t):
        a,b,c = faces.pop(rng.randrange(len(faces)))
        G.add_edges_from([(v,a),(v,b),(v,c)]); faces += [(a,b,v),(b,c,v),(c,a,v)]
    for _ in range(flips):
        u,v = rng.choice(list(G.edges())); cn=list(nx.common_neighbors(G,u,v))
        if len(cn)!=2: continue
        x,y=cn
        if G.has_edge(x,y) or G.degree(u)<=3 or G.degree(v)<=3: continue
        G.remove_edge(u,v); G.add_edge(x,y)
        if not nx.check_planarity(G)[0]: G.remove_edge(x,y); G.add_edge(u,v)
    return G

def dual_cubic(T):
    ok, emb = nx.check_planarity(T)
    faces=[]; seen=set()
    for u,v in emb.edges():
        if (u,v) in seen: continue
        f = emb.traverse_face(u,v, mark_half_edges=seen); faces.append(tuple(f))
    idx = {}
    for i,f in enumerate(faces):
        for j in range(len(f)): idx[(f[j], f[(j+1)%len(f)])] = i
    E=set()
    for (a,b),i in idx.items(): E.add(tuple(sorted((i, idx[(b,a)]))))
    # faces of dual <-> vertices of T: dual vertex i lies on dual-face w iff w in faces[i]
    vf = {i:set(f) for i,f in enumerate(faces)}
    return sorted(E), vf, len(faces)

def relabel(E, vf, p):
    return sorted(tuple(sorted((p[a],p[b]))) for a,b in E), {p[i]:s for i,s in vf.items()}

def cost(Q, VF):
    c=0
    for j in range(3):
        for e in Q[j]:
            for k in range(3):
                if k==j: continue
                u,v=e
                if VF[k][u] & VF[k][v]: c+=1   # cofacial (includes being an edge of Q_k)
    return c

def certify(Q, T1, T2):
    allE=[e for q in Q for e in q]
    assert len(set(allE))==len(allE), "not edge-disjoint"
    for j in range(3):
        assert planar(Q[j])
        S=set(Q[j])
        for e in allE:
            if e not in S: assert not planar(Q[j]+[e]), (j,e)
    assert planar(T1) and planar(T2) and set(T1)|set(T2)==set(allE) and not planar(allE)
    return True

def thick2(E, rng, tries):
    for t in range(tries):
        order=E[:]; rng.shuffle(order); P=[[],[]]
        H=[nx.Graph(),nx.Graph()]; ok=True
        for e in order:
            js=[0,1]; rng.shuffle(js); placed=False
            for j in js:
                H[j].add_edge(*e)
                if nx.check_planarity(H[j])[0]: P[j].append(e); placed=True; break
                H[j].remove_edge(*e)
            if not placed: ok=False; break
        if ok: return P
    return None

if __name__=="__main__":
    t=int(sys.argv[1]); seed=int(sys.argv[2]); rng=random.Random(seed)
    for trial in range(int(sys.argv[3])):
        base=[dual_cubic(rand_tri(t,rng)) for _ in range(3)]
        N=base[0][2]
        P=[list(range(N)) for _ in range(3)]
        for p in P[1:]: rng.shuffle(p)
        Q=[None]*3; VF=[None]*3
        for k in range(3): Q[k],VF[k]=relabel(base[k][0],base[k][1],P[k])
        cur=cost(Q,VF)
        for it in range(20000):
            if cur==0: break
            k=rng.choice([1,2]); i,j=rng.sample(range(N),2)
            P[k][i],P[k][j]=P[k][j],P[k][i]
            Q[k],VF[k]=relabel(base[k][0],base[k][1],P[k]); c=cost(Q,VF)
            if c<=cur or rng.random()<0.003: cur=c
            else:
                P[k][i],P[k][j]=P[k][j],P[k][i]; Q[k],VF[k]=relabel(base[k][0],base[k][1],P[k])
        print("trial",trial,"N",N,"cost",cur, flush=True)
        if cur: continue
        E=[e for q in Q for e in q]
        T=thick2(E,rng,400)
        if T:
            print("CERTIFIED", certify(Q,T[0],T[1]))
            print("Q1=",Q[0]); print("Q2=",Q[1]); print("Q3=",Q[2]); print("T1=",T[0]); print("T2=",T[1])
            sys.exit()
        else: print("  locked but no thickness-2 cover found")
