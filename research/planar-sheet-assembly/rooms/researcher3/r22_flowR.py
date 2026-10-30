# R22-researcher3: run the R21 Thm 4.2 flow on the other cover R (all 6 orders); report terminal
# object, whether it is fully locked (R20 Def 3.1), and its overlap with Q. Reference only.
import json, itertools, networkx as nx
def norm(L): return [tuple(sorted(map(int,e))) for e in L]
def planar(E):
    H=nx.Graph(); H.add_edges_from(E); return nx.check_planarity(H)[0]
Q=[set(norm(q)) for q in json.load(open('r20_locked_only_N80_n3.json'))['Q']]
R=[set(norm(r)) for r in json.load(open('r21_g80_other_cover.json'))['R']]
E=set().union(*Q)
for order in itertools.permutations(range(3)):
    P=[set(R[i]) for i in order]; steps=0; moved=True
    while moved:
        moved=False
        for k in range(3):
            for j in range(k+1,3):
                for e in sorted(P[j]):
                    if planar(list(P[k])+[e]):
                        P[k].add(e); P[j].remove(e); steps+=1; moved=True
                        break
                if moved: break
            if moved: break
    viol=[(k,e) for k in range(3) for e in sorted(E-P[k]) if planar(list(P[k])+[e])]
    print("order",order,"steps",steps,"sizes",[len(p) for p in P],"nonempty",all(P),
          "full-lock violations",len(viol),viol[:6],
          "overlap with Q",[[len(p&q) for q in Q] for p in P])
