# 아폴로니안 이중 가젯: 한쪽 리스트 환원이 두 순서 모두 실패하는 22 정점 예
from r48_at import *
import networkx as nx
def apollo(o):  # p,q,r,s,p',q',r'
    p,q,r,s,P,Q,R=[o+i for i in range(7)]
    E=[(p,q),(p,r),(p,s),(q,r),(q,s),(r,s),(P,q),(P,r),(P,s),(Q,p),(Q,r),(Q,s),(R,p),(R,q),(R,s)]
    return E
def k4(o): return [(o+i,o+j) for i in range(4) for j in range(i+1,4)]
# V1 = 0..10 (A:0..6, Q1:7..10), V2 = 11..21 (A':11..17, Q2:18..21)
B1=apollo(0)+k4(7); B2=apollo(11)+k4(18)
def gadget(A,Q):
    p,q,r,s,P,Qq,R=[A+i for i in range(7)]
    return [(x,Q+i) for i in range(3) for x in (p,q,r)]+[(x,Q+3) for x in (P,Qq,R)]
H=gadget(0,18)+gadget(11,7)
V1=range(0,11); V2=range(11,22)
G=nx.Graph(); G.add_nodes_from(range(22)); G.add_edges_from(B1+B2+H)
dH={v:0 for v in G}
for u,v in H: dH[u]+=1; dH[v]+=1
print('max cross deg',max(dH.values()),'planar B1,B2',nx.check_planarity(G.subgraph(V1))[0],nx.check_planarity(G.subgraph(V2))[0])
def one_sided(Vf,Vs,Bf,Bs):
    # Vf 를 {0..3} 으로 4-색칠한 모든 경우, Vs 는 {4,5} ∪ ({0..3}∖c(N_f(v)))
    idx={v:i for i,v in enumerate(Vf)}
    Ef=[(idx[u],idx[v]) for u,v in Bf]
    cols=all_colorings(len(Vf),Ef,4)
    jdx={v:i for i,v in enumerate(Vs)}
    Es=[(jdx[u],jdx[v]) for u,v in Bs]
    ok=0
    for c in cols:
        lists=[]
        for v in Vs:
            used={c[idx[w]] for w in G[v] if w in idx}
            lists.append([4,5]+[a for a in range(4) if a not in used])
        if proper_coloring(len(Vs),Es,lists): ok+=1
    return len(cols),ok
print('B1 first: (#4-colorings, #good)',one_sided(list(V1),list(V2),B1,B2))
print('B2 first:',one_sided(list(V2),list(V1),B2,B1))
E=list(G.edges())
for k in (5,6):
    c=proper_coloring(22,E,[list(range(k))]*22)
    print('chi<=%d?'%k, c is not None)
    if c and k==6:
        for part,V in (('V1',V1),('V2',V2)): print(part,'colors used',sorted({c[v] for v in V}))
