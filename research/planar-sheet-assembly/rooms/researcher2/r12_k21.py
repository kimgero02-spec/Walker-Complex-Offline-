# R12 망상꾼: Pi2 (브럭-라이저 유사) 반증 시도. K_21 을 4-정칙 평면 그래프로 정확히 분해 (Z_7 x {0,1,2}, Z_7 궤도).
import itertools, random, sys, networkx as nx
def medial(G):
    ok,emb=nx.check_planarity(G); faces=[]; seen=set()
    for u,v in emb.edges():
        if (u,v) in seen: continue
        f=emb.traverse_face(u,v,mark_half_edges=seen); faces.append(f)
    M=nx.Graph()
    for f in faces:
        es=[frozenset((f[i],f[(i+1)%len(f)])) for i in range(len(f))]
        for i in range(len(es)): M.add_edge(es[i],es[(i+1)%len(es)])
    return nx.convert_node_labels_to_integers(M)
prism=nx.circular_ladder_graph(3); M9=medial(prism)
assert all(d==4 for _,d in M9.degree()) and nx.check_planarity(M9)[0] and M9.number_of_nodes()==9
octa=nx.octahedral_graph()
pts=[(a,i) for i in range(3) for a in range(7)]
def cls(p,q):
    (a,i),(b,j)=p,q
    if i==j: d=(b-a)%7; return (i,i,min(d,7-d))
    if i>j: (a,i),(b,j)=(b,j),(a,i)
    return (i,j,(b-a)%7)
ALL={(i,i,d) for i in range(3) for d in (1,2,3)}|{(i,j,d) for i in range(3) for j in range(i+1,3) for d in range(7)}
assert len(ALL)==30
def place(G,forbid,need_exact=None,limit=None):
    order=list(nx.bfs_tree(G,0)); res=[]
    def bt(k,assign,used):
        if limit and len(res)>=limit: return
        if k==len(order):
            if need_exact is None or used==need_exact: res.append((dict(assign),set(used)))
            return
        v=order[k]; cand=pts if k>0 else [(0,i) for i in range(3)]
        for p in cand:
            if p in assign.values(): continue
            new=[]; ok=True
            for u in G[v]:
                if u in assign:
                    c=cls(assign[u],p)
                    if c in forbid or c in used or c in new or (need_exact is not None and c not in need_exact): ok=False;break
                    new.append(c)
            if not ok: continue
            assign[v]=p; bt(k+1,assign,used|set(new)); del assign[v]
    bt(0,{},frozenset()); return res
random.seed(0)
octs=place(octa,set(),limit=200000)
print('octahedron placements',len(octs),flush=True)
random.shuffle(octs); tried=0
for oa,used in octs:
    rest=ALL-used; tried+=1
    sol=place(M9,used,need_exact=rest,limit=1)
    if sol:
        print('FOUND after',tried); print('octa',oa); print('M9',sol[0][0]); break
    if tried%500==0: print('tried',tried,flush=True)
    if tried>=5000: print('none in 5000'); break
