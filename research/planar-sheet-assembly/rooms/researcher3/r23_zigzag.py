# R23-researcher3: direct zigzag  Q⊔x ~ R⊔x  in Ref^(4)(G80)  (check only; the argument is in the report).
# 1) M := edges whose Q-index and R-index differ (best permutation). 2) structure of M (degrees, |M|).
# 3) build the 5-object zigzag of Lemma 1.1 and check every object directly: pieces planar, union = E.
import json, itertools, networkx as nx
def norm(L): return [tuple(sorted(map(int,e))) for e in L]
def planar(E):
    H=nx.Graph(); H.add_edges_from(E); return nx.check_planarity(H)[0]
Q=[set(norm(q)) for q in json.load(open('r20_locked_only_N80_n3.json'))['Q']]
R=[set(norm(r)) for r in json.load(open('r21_g80_other_cover.json'))['R']]
E=set().union(*Q); assert E==set().union(*R)
best=None
for s in itertools.permutations(range(3)):
    A=set().union(*[Q[k]&R[s[k]] for k in range(3)]); M=E-A
    if best is None or len(M)<len(best[1]): best=(s,M)
s,M=best; print("best perm",s,"|M|",len(M))
for e in sorted(M):
    print("  edge",e,"Q-index",[k for k in range(3) if e in Q[k]][0],"R-index",[i for i in range(3) if e in R[i]][0])
H=nx.Graph(); H.add_edges_from(M)
print("M: vertices",H.number_of_nodes(),"degrees",sorted(d for _,d in H.degree()),"components",nx.number_connected_components(H),"planar",planar(M))
def obj(pieces):
    ok=all(planar(list(p)) if p else True for p in pieces); cov=set().union(*pieces)==E
    return ok,cov
Rs=[R[s[k]] for k in range(3)]
chain=[("Q⊔x",[Q[0],Q[1],Q[2],set()]),
       ("(Q,M)",[Q[0],Q[1],Q[2],M]),
       ("(Q∩R,M)",[Q[k]&Rs[k] for k in range(3)]+[M]),
       ("(R,M)",[Rs[0],Rs[1],Rs[2],M]),
       ("R⊔x",[Rs[0],Rs[1],Rs[2],set()])]
for name,P in chain: print(name,"sizes",[len(p) for p in P],"planar,cover =",obj(P))
