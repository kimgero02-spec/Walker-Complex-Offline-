# F-R2: R4 일반화 - 간격 중점에 붙은 2-부착 다리 (정리 F3) 확인
import networkx as nx, itertools
exec(open('f_r2.py').read().split('if __name__')[0])
from f_r1_ribbon import cyc

def torus12(chord):
    O=list(range(12)); P0=cyc(O)
    if chord: P0.add_edge(*chord)
    S=['p','q','r','s','t','u']   # hexagon squares-with-gaps: arcs pq and st, gaps q-r-s, t-u-p
    P=[P0]+[cyc(S) for _ in range(4)]; C=[O]+[S]*4
    arcs=[(0,[0,1],1,['q','p']),(0,[6,7],2,['q','p']),(1,['s','t'],2,['t','s']),
          (0,[3,4],3,['q','p']),(0,[9,10],4,['q','p']),(3,['s','t'],4,['t','s'])]
    return P,C,arcs

def decompose(P,C,arcs):
    # assemble by hand to keep names; return cycles of dX and chords (arc edges + piece chords)
    rep={}
    for k,Pk in enumerate(P):
        for v in Pk: rep[(k,v)]=(k,v)
    def f(x):
        while rep[x]!=x: x=rep[x]
        return x
    arcE=set()
    for (k,pk,j,pj) in arcs:
        for a,b in zip(pk,pj): rep[f((k,a))]=f((j,b))
        for i in range(len(pk)-1): arcE.add((k,frozenset(pk[i:i+2]))); arcE.add((j,frozenset(pj[i:i+2])))
    bd=nx.Graph(); chords=set()
    for k,Ck in enumerate(C):
        for i in range(len(Ck)):
            u,v=Ck[i],Ck[(i+1)%len(Ck)]
            if (k,frozenset((u,v))) in arcE: chords.add(frozenset((f((k,u)),f((k,v)))))
            else: bd.add_edge(f((k,u)),f((k,v)))
    for k,Pk in enumerate(P):
        cedges={frozenset((Ck_u,Ck_v)) for Ck_u,Ck_v in zip(C[k],C[k][1:]+C[k][:1])}
        for u,v in Pk.edges():
            if frozenset((u,v)) not in cedges: chords.add(frozenset((f((k,u)),f((k,v)))))
    cycles=[]
    for comp in nx.connected_components(bd):
        H=bd.subgraph(comp); cycles.append([u for u,_ in nx.find_cycle(H)])
    return cycles,[tuple(c) for c in chords]

for ch in [None,(2,5),(5,8),(8,11),(11,2),(2,8),(5,11)]:
    cycles,chords=decompose(*torus12(ch))
    T=build_T(cycles,chords); pl=nx.check_planarity(T)[0]
    if len(cycles)==1:
        labs,E=overlap(walk(cycles,chords,set(),{})); pred=bip(labs,E)
    else:
        c1,c2,_,_=theorem_F2(cycles,chords); pred=c1 and c2
    print(f"chord {ch}: b={len(cycles)} planar={pl}  F3 prediction={pred}")

print("---- unequal gaps")
def torusG(gl, chord):
    # octagon-type piece: arcs a,b,a',b' each length 1, gap lengths gl[0..3]
    O=[]; arcpos=[]; v=0
    for g in gl:
        arcpos.append((v,v+1)); O+= [v,v+1]; v+=2
        for _ in range(g-1): O.append(v); v+=1
    P0=cyc(O)
    if chord: P0.add_edge(*chord)
    S=['p','q','r','s','t','u']
    P=[P0]+[cyc(S) for _ in range(4)]; C=[O]+[S]*4
    a,b,a2,b2=arcpos
    arcs=[(0,list(a),1,['q','p']),(0,list(a2),2,['q','p']),(1,['s','t'],2,['t','s']),
          (0,list(b),3,['q','p']),(0,list(b2),4,['q','p']),(3,['s','t'],4,['t','s'])]
    return P,C,arcs,O,arcpos
gl=(2,4,3,5)
P,C,arcs,O,arcpos=torusG(gl,None)
interior=[x for x in O if all(x not in ap for ap in arcpos)]
N=len(O); rows=[]
for u,w in itertools.combinations(interior,2):
    iu,iw=O.index(u),O.index(w); L=min(abs(iu-iw),N-abs(iu-iw))
    if L<2: continue
    side={nm for nm,ap in zip(['a','b',"a'","b'"],arcpos) if iu<O.index(ap[0])<iw}
    other={'a','b',"a'","b'"}-side
    part=frozenset([frozenset(side),frozenset(other)])
    cycles,chords=decompose(*torusG(gl,(u,w))[:3])
    pl=nx.check_planarity(build_T(cycles,chords))[0]
    labs,E=overlap(walk(cycles,chords,set(),{})); pred=bip(labs,E)
    rows.append((L,tuple(sorted(tuple(sorted(s)) for s in part)),pl,pred,(u,w)))
from collections import defaultdict
byL=defaultdict(set); bypart=defaultdict(set)
for L,pt,pl,pred,ch in rows:
    assert pl==pred
    byL[L].add(pl); bypart[pt].add(pl)
print("partition -> planarity values:", {str(k):v for k,v in bypart.items()})
for L,s in sorted(byL.items()):
    if len(s)>1:
        ex=[r for r in rows if r[0]==L]
        p1=next(r for r in ex if r[2]); p2=next(r for r in ex if not r[2])
        print(f"length {L}: planar example {p1[4]} part {p1[1]}  | nonplanar example {p2[4]} part {p2[1]}")
print("all", len(rows), "placements: planar == F3 prediction")
