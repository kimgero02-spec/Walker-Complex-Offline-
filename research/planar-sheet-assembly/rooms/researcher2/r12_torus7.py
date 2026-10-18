# R12 망상꾼 (재개): 정리 E (조각-연속 매장 <=> M° 매장) 를 써서, K_7 의 사이클 분해 중 M° 가 토러스에 매장되는 것을 전부 찾는다.
# (1) K_7 의 토러스 매장 = 삼각분할. 0 의 회전을 (1..6) 으로 고정하고 succ 제약 전파로 모두 찾음.
# (2) 각 매장에서 꼭짓점마다 '연속 짝짓기' 2 가지 -> 2^7 가지 -> 짝을 이어 붙여 닫힌 자취 -> 모두 사이클이면 분해.
import itertools, networkx as nx
from r11_levi import manual
N=7; V=range(N)
def triangulations():
    sols=[]
    succ={}
    for i in range(6): succ[(0,1+i)]=1+(i+1)%6
    def consistent(s):
        # 각 v 에서 succ_v 는 단사, 그리고 삼각 제약
        for v in V:
            img=[s[(v,u)] for u in V if (v,u) in s]
            if len(img)!=len(set(img)): return False
        for (v,u),w in list(s.items()):
            for key,val in (((w,v),u),((u,w),v)):
                if key in s and s[key]!=val: return False
        return True
    def close(s):
        ch=True
        while ch:
            ch=False
            for (v,u),w in list(s.items()):
                for key,val in (((w,v),u),((u,w),v)):
                    if key not in s: s[key]=val; ch=True
                    elif s[key]!=val: return None
        return s if consistent(s) else None
    def is_cyclic(s,v):
        u=[x for x in V if x!=v][0]; seen=[u]
        for _ in range(5): seen.append(s[(v,seen[-1])])
        return s[(v,seen[-1])]==u and len(set(seen))==6
    def rec(s):
        s=close(dict(s))
        if s is None: return
        free=[(v,u) for v in V for u in V if u!=v and (v,u) not in s]
        if not free:
            if all(is_cyclic(s,v) for v in V): sols.append(s)
            return
        v,u=free[0]
        for w in V:
            if w in (v,u): continue
            t=dict(s); t[(v,u)]=w
            if consistent(t): rec(t)
    rec(succ); return sols
T=triangulations(); print('torus triangulations of K7 with rot(0) fixed:',len(T))
def rotation(s,v):
    u=min(x for x in V if x!=v); L=[u]
    for _ in range(5): L.append(s[(v,L[-1])])
    return L
fano=[(0,1,3),(1,2,4),(2,3,5),(3,4,6),(4,5,0),(5,6,1),(6,0,2)]
FANO=nx.convert_node_labels_to_integers(manual([(list(b),[(b[0],b[1]),(b[1],b[2]),(b[2],b[0])]) for b in fano])[0])
classes=[]; decs_found=0
for s in T:
    rot={v:rotation(s,v) for v in V}
    for choice in itertools.product((0,1),repeat=N):
        pair={}
        for v in V:
            L=rot[v]; c=choice[v]
            for j in range(3):
                a,b=L[(2*j+c)%6],L[(2*j+c+1)%6]; pair[(v,a)]=b; pair[(v,b)]=a
        used=set(); cycles=[]; ok=True
        for e in itertools.combinations(V,2):
            if frozenset(e) in used: continue
            a,b=e; walk=[a,b]; used.add(frozenset(e))
            while True:
                c=pair[(walk[-1],walk[-2])]
                if frozenset((walk[-1],c)) in used: break
                used.add(frozenset((walk[-1],c))); walk.append(c)
            if walk[-1]!=walk[0] or c!=walk[1]: ok=False; break
            walk=walk[:-1]
            if len(set(walk))!=len(walk): ok=False; break
            cycles.append(walk)
        if not ok: continue
        decs_found+=1
        pieces=[(w,[(w[i],w[(i+1)%len(w)]) for i in range(len(w))]) for w in cycles]
        Mo,_,_,_=manual(pieces); X=nx.convert_node_labels_to_integers(Mo)
        if not any(nx.is_isomorphic(X,Y) for Y,_ in classes):
            classes.append((X,sorted(len(w) for w in cycles)))
print('contiguous cycle decompositions (with multiplicity):',decs_found)
print('iso classes of toroidal-contiguous 3-regular M° (N=7):',[(L,nx.girth(X), nx.is_isomorphic(X,FANO)) for X,L in classes])
