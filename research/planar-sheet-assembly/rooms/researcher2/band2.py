# 띠의 면(조각) 목록을 직접 만들어 가향성(=홀로노미) 확인 + (iii) 동형 쌍 구성
import itertools as it, networkx as nx
from collections import defaultdict
def band_faces(ts, ss, twist):
    k=len(ts); c=[0]
    def new(): c[0]+=1; return c[0]
    T=[[new()]]; B=[[new()]]  # 각 가로대의 위/아래 끝
    tops=[T[0][0]]; bots=[B[0][0]]
    faces=[]; tarcs=[]; barcs=[]
    for i in range(k):
        last=i==k-1
        def arc(s,L,end):
            path=[s]
            for j in range(L):
                path.append(end if (last and j==L-1) else new())
            return path
        et = (bots[0] if twist else tops[0]); eb=(tops[0] if twist else bots[0])
        pt=arc(tops[-1],ts[i],et); pb=arc(bots[-1],ss[i],eb)
        tarcs.append(pt); barcs.append(pb)
        if not last: tops.append(pt[-1]); bots.append(pb[-1])
    # 핀치 병합(길이0 호): union-find
    uf={}
    def f(x):
        uf.setdefault(x,x)
        while uf[x]!=x: x=uf[x]
        return x
    for i in range(k):
        endT = tarcs[i][-1] if ts[i]>0 else None
        if ts[i]==0:
            tgt = (bots[0] if twist else tops[0]) if i==k-1 else tops[i+1] if i+1<len(tops) else None
            uf[f(tgt)]=f(tarcs[i][0])
        if ss[i]==0:
            tgt = (tops[0] if twist else bots[0]) if i==k-1 else bots[i+1]
            uf[f(tgt)]=f(barcs[i][0])
    for i in range(k):
        nt = tops[i+1] if i<k-1 else (bots[0] if twist else tops[0])
        nb = bots[i+1] if i<k-1 else (tops[0] if twist else bots[0])
        # 경계: 윗호 정방향, 다음 가로대 위->아래, 아랫호 역방향 (가로대 i 아래->위로 닫힘)
        top=[f(x) for x in tarcs[i]]
        if ts[i]==0: top=[f(tops[i])]
        bot=[f(x) for x in barcs[i]]
        if ss[i]==0: bot=[f(bots[i])]
        cyc = top + [f(nb)] if top[-1]!=f(nb) else top
        # top 끝은 nt
        cyc = top[:] if top[-1]==f(nt) else top+[f(nt)]
        rb=[x for x in reversed(bot)]
        if rb[0]==f(nb): rb=rb
        else: rb=[f(nb)]+rb
        cyc = cyc + [x for x in rb if True]
        # 중복 인접 제거
        out=[]
        for x in cyc:
            if not out or out[-1]!=x: out.append(x)
        if out[0]==out[-1]: out.pop()
        faces.append(tuple(out))
    return faces
def check(faces):
    occ=defaultdict(list)
    for fi,F in enumerate(faces):
        L=len(F)
        for t in range(L): occ[frozenset((F[t],F[(t+1)%L]))].append((fi,(F[t],F[(t+1)%L])))
    # 가향: 각 면에 부호, 공유변이 반대방향이면 같은 부호
    import networkx as nx
    sign={0:1}; ok=True; st=[0]
    adj=defaultdict(list)
    for e,l in occ.items():
        if len(l)==2:
            (f1,d1),(f2,d2)=l
            same = (d1==d2)  # 같은 방향이면 부호 반대여야 함
            adj[f1].append((f2,-1 if same else 1)); adj[f2].append((f1,-1 if same else 1))
    while st:
        x=st.pop()
        for y,s in adj[x]:
            if y in sign:
                if sign[y]!=sign[x]*s: ok=False
            else: sign[y]=sign[x]*s; st.append(y)
    G=nx.Graph(); [G.add_edge(*tuple(e)) for e in occ]
    return ok, G, all(len(set(F))==len(F) for F in faces)
for name,ts,ss in [("sq3",[1]*3,[1]*3),("2fan m=5",[0]*5+[1]*5+[2],[1]*5+[0]*5+[2])]:
    for tw in (False,True):
        ok,G,cyc=check(band_faces(ts,ss,tw))
        print(name,"twist" if tw else "straight","가향(홀로노미 자명)=",ok,"면이 사이클",cyc,"평면",nx.check_planarity(G)[0],"V,E",G.number_of_nodes(),G.number_of_edges())
ok,G1,_=check(band_faces([1]*3,[1]*3,True)); print("sq3 twist ≅K33", nx.is_isomorphic(G1,nx.complete_bipartite_graph(3,3)))
# (iii) 같은 k 에서 twisted ≅ straight 인 쌍 구성 (k=3,4, 호 길이 0..2, 단순그래프만)
found=None
for k in (3,4):
    S={}
    for ts in it.product(range(3),repeat=k):
        for ss in it.product(range(3),repeat=k):
            if any(a+b==0 for a,b in zip(ts,ss)): continue
            for tw in (False,True):
                F=band_faces(list(ts),list(ss),tw)
                ok,G,cyc=check(F)
                if not cyc or ok==tw: continue  # 면이 사이클이고 홀로노미가 의도대로
                if any(len(F[i])<3 for i in range(k)): continue
                S.setdefault(tw,[]).append((ts,ss,G))
    for a in S[False]:
        for b in S[True]:
            if a[2].number_of_edges()==b[2].number_of_edges() and a[2].number_of_nodes()==b[2].number_of_nodes() and nx.is_isomorphic(a[2],b[2]):
                found=(k,a[0],a[1],b[0],b[1],a[2]); break
        if found: break
    if found: break
print("iii", found[:5] if found else None, sorted(dict(found[5].degree()).values()) if found else "")
if found: print("edges", sorted(found[5].edges()), "planar", nx.check_planarity(found[5])[0])
