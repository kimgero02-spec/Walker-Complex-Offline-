# R2 검증: Z/n 위 대칭 부분가군 열거, Goursat (I,J,theta) 개수, Hom 구조 공식 확인
import itertools, sys
from math import gcd
def submodules(n):
    # Z/n x Z/n 의 부분군 = 부분가군. 생성원 집합 폐포로 열거
    els=[(a,b) for a in range(n) for b in range(n)]
    def span(gens):
        S={(0,0)}; ch=True
        while ch:
            ch=False
            for s in list(S):
                for g in gens:
                    t=((s[0]+g[0])%n,(s[1]+g[1])%n)
                    if t not in S: S.add(t); ch=True
        return frozenset(S)
    subs={span([])}
    frontier=list(subs)
    # 모든 부분군은 2생성 이하 (Z/n x Z/n)
    for g in els:
        for h in els:
            subs.add(span([g,h]))
    return subs
def sym(S): return all((b,a) in S for a,b in S)
def goursat(n,S):
    J=frozenset(a for a,b in S); I=frozenset(a for a,b in S if b==0)
    return J,I
def hom_set(n,S,V,E):
    out=[]
    for phi in itertools.product(range(n),repeat=V):
        if all((phi[u],phi[v]) in S for u,v in E): out.append(phi)
    return out
def comps(V,E):
    par=list(range(V))
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for u,v in E: par[f(u)]=f(v)
    cs={}
    for v in range(V): cs.setdefault(f(v),[]).append(v)
    return list(cs.values())
def bip(C,E):
    col={C[0]:0}; st=[C[0]]
    while st:
        x=st.pop()
        for u,v in E:
            for a,b in ((u,v),(v,u)):
                if a==x:
                    if b not in col: col[b]=1-col[x]; st.append(b)
                    elif col[b]==col[x]: return False
    return True
def formula(n,S,V,E):
    J,I=goursat(n,S)
    # J_theta: x in J with (x,x) in S
    Jt=[x for x in J if (x,x) in S]
    tot=1
    for C in comps(V,E):
        Es=[e for e in E if e[0] in C]
        if not Es: tot*=n; continue
        if bip(C,Es): tot*=len(S)*len(I)**(len(C)-2)
        else: tot*=len(Jt)*len(I)**(len(C)-1)
    return tot
def ordhist(n,H):
    from collections import Counter
    c=Counter()
    for phi in H:
        o=1
        for x in phi:
            oo=n//gcd(n,x) if x else 1
            o=o*oo//gcd(o,oo)
        c[o]+=1
    return tuple(sorted(c.items()))
def cyc(k): return [(i,(i+1)%k) for i in range(k)]
graphs={
 'K2':(2,[(0,1)]),'P3':(3,[(0,1),(1,2)]),'K3':(3,cyc(3)),'C4':(4,cyc(4)),'loop+K2':(3,[(0,0),(1,2)]),
 'K3+K2+pt':(6,[(0,1),(1,2),(2,0),(3,4)]),
 'C6':(6,cyc(6)),'K33':(6,[(i,j) for i in range(3) for j in range(3,6)]),
 'P6':(6,[(i,i+1) for i in range(5)]),
}
for n in [4,6,8,9]:
    subs=[S for S in submodules(n) if sym(S)]
    print('n=',n,'대칭 부분가군 수',len(subs))
    bad=0
    for S in subs:
        for name,(V,E) in graphs.items():
            if n**V>300000: continue
            H=hom_set(n,S,V,E)
            if len(H)!=formula(n,S,V,E): bad+=1; print('불일치',n,sorted(S)[:4],name,len(H),formula(n,S,V,E))
        if n**6<=300000:
            h1=ordhist(n,hom_set(n,S,*graphs['C6'])); h2=ordhist(n,hom_set(n,S,*graphs['K33'])); h3=ordhist(n,hom_set(n,S,*graphs['P6']))
            if not(h1==h2==h3): bad+=1; print('C6/K33 구분!',n)
    print(' 불일치/구분 건수',bad)
    if n in(4,6,8,9) and n<=9:
        for S in sorted(subs,key=len):
            J,I=goursat(n,S)
            print('  |S|=%d J=%s I=%s  S=%s'%(len(S),sorted(J),sorted(I),sorted(S) if len(S)<=12 else '...'))
