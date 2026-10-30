# R22-researcher3: algorithm-independent certificates for locking of Q (G80).
# For each sheet k and each edge e not in Q_k: extract a Kuratowski subgraph of Q_k+e (networkx),
# then verify by OUR OWN code that it (i) is a subgraph of Q_k+e, (ii) contains e, (iii) after
# suppressing degree-2 vertices is exactly K5 or K3,3 (and has no vertices of degree 1 or >4).
# Also: cofacial test (faces of the embedding of Q_k) -- with Whitney's theorem this is a proof route.
import json, itertools, networkx as nx
def norm(L): return [tuple(sorted(map(int,e))) for e in L]
Q=[norm(q) for q in json.load(open('r20_locked_only_N80_n3.json'))['Q']]
E=sorted(set(e for q in Q for e in q))
def smooth(H):
    H=nx.MultiGraph(H)
    for v in [v for v in H if H.degree(v)==2]:
        nb=[u for u in H.neighbors(v)]
        if len(nb)!=2 or nb[0]==nb[1]: return None
        H.remove_node(v); H.add_edge(nb[0],nb[1])
    return H
def is_K5_or_K33(M):
    if M is None: return None
    G=nx.Graph(M)
    if G.number_of_edges()!=M.number_of_edges(): return None  # multi-edges -> not a subdivision of simple K
    n,m=G.number_of_nodes(),G.number_of_edges()
    degs=set(d for _,d in G.degree())
    if n==5 and m==10 and degs=={4}: return "K5"
    if n==6 and m==9 and degs=={3} and nx.is_bipartite(G):
        a,b=nx.bipartite.sets(G)
        if len(a)==3 and all(G.has_edge(x,y) for x in a for y in b): return "K33"
    return None
cnt={"K5":0,"K33":0}; fail=[]
for k,q in enumerate(Q):
    s=set(q); Hk=nx.Graph(q)
    ok,emb=nx.check_planarity(Hk); emb.check_structure()
    faces=[]; seen=set()
    for u,v in emb.edges():
        if (u,v) in seen: continue
        f=emb.traverse_face(u,v,mark_half_edges=seen); faces.append(set(f))
    V,Ek=Hk.number_of_nodes(),Hk.number_of_edges()
    assert V-Ek+len(faces)==2, "Euler fails"
    cof=0
    for e in E:
        if e in s: continue
        if any(e[0] in f and e[1] in f for f in faces): cof+=1
        H=nx.Graph(q+[e]); pl,cert=nx.check_planarity(H,counterexample=True)
        if pl: fail.append((k,e)); continue
        ce=set(tuple(sorted(x)) for x in cert.edges())
        if not ce<=set(q)|{e} or e not in ce: fail.append((k,e,"subgraph/e")); continue
        if min(d for _,d in cert.degree())<2 or max(d for _,d in cert.degree())>4: fail.append((k,e,"deg")); continue
        t=is_K5_or_K33(smooth(cert))
        if t is None: fail.append((k,e,"type")); continue
        cnt[t]+=1
    print(f"sheet {k}: V={V} E={Ek} faces={len(faces)} face sizes={sorted(set(len(f) for f in faces))} "
          f"3conn={nx.node_connectivity(Hk)} cofacial-other-edges={cof}")
print("certificates:",cnt,"total",sum(cnt.values()),"failures",fail)
