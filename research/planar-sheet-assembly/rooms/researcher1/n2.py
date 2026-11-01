# R02 researcher1: n=2 뫼비우스 설명서의 다리-면 배정 판정(정리 N2) 단계 확인. 정선된 예만.
import networkx as nx, itertools as it
from r02 import analyze

def bridges(E, C):
    P=nx.Graph(E); Cs=set(C); out=[]
    ce={frozenset(x) for x in zip(C,C[1:]+C[:1])}
    for u,v in P.edges():
        if u in Cs and v in Cs and frozenset((u,v)) not in ce: out.append(frozenset((u,v)))
    R=P.subgraph([x for x in P if x not in Cs])
    for comp in nx.connected_components(R):
        out.append(frozenset(y for x in comp for y in P[x] if y in Cs))
    return out

def overlap(S1,S2,T):
    if len(S1&S2)>=3: return True
    idx={v:i for i,v in enumerate(T)}
    for x,y in it.combinations(S1,2):
        for u,v in it.combinations(S2,2):
            if len({x,y,u,v})<4: continue
            a,b=sorted((idx[x],idx[y]))
            if (a<idx[u]<b)!=(a<idx[v]<b): return True
    return False

def n2_test(pieces, name):
    r=analyze(pieces,name); K=r['K']
    assert r['n']==2 and r['m']==2 and not r['orientable']
    branch={v for (_,_,p,_) in r['arcs'] for v in (p[0],p[-1])}
    faces=[]
    for c in nx.cycle_basis(K)+[]: pass
    # 모든 사이클 열거 후 분기점 정확히 3개 지나는 것
    seen=set()
    for c in nx.simple_cycles(K.to_directed()):
        if len(c)<3: continue
        key=frozenset(frozenset(e) for e in zip(c,c[1:]+c[:1]))
        if key in seen: continue
        seen.add(key)
        if len(branch&set(c))==3: faces.append(c)
    assert len(faces)==4, len(faces)
    Bs=[(k,S) for k,(E,C) in enumerate(pieces) for S in bridges(E,C)]
    allowed=[[f for f in range(4) if S<=set(faces[f])] for k,S in Bs]
    # 같은 조각 다리끼리는 같은 면에서 겹치지 않음을 확인 (보조정리 N2-b)
    for (a,(k,S)),(b,(l,S2)) in it.combinations(enumerate(Bs),2):
        if k==l:
            for f in set(allowed[a])&set(allowed[b]): assert not overlap(S,S2,faces[f]), "same-piece overlap!"
    pred=False
    for choice in it.product(*allowed):
        good=all(not(choice[a]==choice[b] and overlap(Bs[a][1],Bs[b][1],faces[choice[a]]))
                 for a,b in it.combinations(range(len(Bs)),2))
        if good: pred=True; break
    print(f"{name}: bridges={[(k,sorted(S,key=str)) for k,S in Bs]} allowed={allowed} -> 예측 planar={pred}, 실제 planar={r['Gplanar']}")
    return pred==r['Gplanar']

def cyc(C): return list(zip(C,C[1:]+C[:1]))

if __name__=="__main__":
    # 1. K4 = 정사각형 2장
    A0,A1,B0,B1='a0','a1','b0','b1'
    C1=[A0,A1,B0,B1]; C2=[A0,A1,B1,B0]
    print(n2_test([(cyc(C1),C1),(cyc(C2),C2)],"K4"))
    # 2. K5 = W4 u C4
    a,b,c,d,e='abcde'
    C1=[a,b,d,c]; P1=cyc(C1)+[(e,x) for x in 'abcd']; C2=[a,b,c,d]
    print(n2_test([(P1,C1),(cyc(C2),C2)],"K5=W4+C4"))
    # 3. 피터슨 2조각 (R01 r01.py 와 같은 구성, 여기서 다시 만듦)
    Pe=nx.petersen_graph(); cs={}
    for cy in nx.simple_cycles(Pe.to_directed()):
        if len(cy)==5: cs[frozenset(frozenset(x) for x in cyc(cy))]=cy
    Cl=list(cs.items()); Ee=[frozenset(x) for x in Pe.edges()]
    for S in it.combinations(range(len(Cl)),6):
        cnt={x:0 for x in Ee}
        for i in S:
            for x in Cl[i][0]: cnt[x]+=1
        if all(v==2 for v in cnt.values()): faces=[Cl[i][1] for i in S]; break
    rest=faces[1:]; lab=(0,1,1,0,1); pcs=[]
    for g in range(2):
        fl=[rest[i] for i in range(5) if lab[i]==g]; cnt={}
        for f in fl:
            for x in cyc(f): cnt[frozenset(x)]=cnt.get(frozenset(x),0)+1
        bd=nx.Graph([tuple(k) for k,v in cnt.items() if v==1])
        C=[u for u,_ in nx.find_cycle(bd)]; E=[x for f in fl for x in cyc(f)]
        pcs.append((E,C))
    print(n2_test(pcs,"Petersen 2-piece"))
    # 4. 결정적 쌍: alpha = a0 p q a1, sigma1 = a1 s b0, beta = b0 b1, sigma1' = b1 a0
    #    P2: alpha, rail a1-b1, beta(b1->b0), rail b0 t a0
    p,q,s,t='p','q','s','t'
    C1=[A0,p,q,A1,s,B0,B1]; C2=[A0,p,q,A1,B1,B0,t]
    print(n2_test([(cyc(C1)+[(p,s)],C1),(cyc(C2)+[(q,t)],C2)],"decisive conflict (p-s | q-t)"))
    print(n2_test([(cyc(C1)+[(q,s)],C1),(cyc(C2)+[(p,t)],C2)],"decisive no-conflict (q-s | p-t)"))
    # 5. 조건 (i) 만 보는 판정은 4번 첫 예를 평면으로 잘못 판정: 각 다리는 한 면에 들어감
    # 6. alpha-beta 를 잇는 내부 경로 (보조정리 6 의 '가로대 방향' 판): P1 에 p - b1 현? b1 은 beta 끝점이므로 beta 내부 필요
    C1=[A0,p,A1,s,B0,'r',B1]; C2=[A0,p,A1,B1,'r',B0,t]
    print(n2_test([(cyc(C1)+[(p,'r')],C1),(cyc(C2),C2)],"alpha-int to beta-int chord"))
