# R03 반례꾼 점검 코드 (증명의 구현 점검일 뿐, 근거 아님). 소요: 수 초.
import itertools, random
import numpy as np
import networkx as nx

def two_colorable(ground, sets):
    # 소규모 전수: 지면 원소 <= 14
    g = list(ground); n = len(g); pos = {x:i for i,x in enumerate(g)}
    masks = [sum(1<<pos[x] for x in s) for s in sets]
    full = (1<<n)-1
    for col in range(1<<n):
        if all((m & col) != m and (m & col) != 0 for m in masks): return True
    return not masks

def cd(ground, sets):
    g = list(ground)
    for k in range(len(g)+1):
        for U in itertools.combinations(g,k):
            Us=set(U)
            rem=[s for s in sets if not (s&Us)]
            if two_colorable([x for x in g if x not in Us], rem): return k
    return len(g)

def kg(sets):
    G=nx.Graph(); G.add_nodes_from(range(len(sets)))
    for i,j in itertools.combinations(range(len(sets)),2):
        if not (sets[i]&sets[j]): G.add_edge(i,j)
    return G

# ---- (1) 정리 A 의 명시적 사상 점검: 무작위 소형 H ----
def thmA_check(trials=300, seed=1):
    rnd=random.Random(seed); bad=0; tested=0
    for _ in range(trials):
        N=rnd.randint(3,7); m=rnd.randint(2,6)
        sets=list({frozenset(rnd.sample(range(N), rnd.randint(1,min(3,N)))) for _ in range(m)})
        c=cd(range(N), sets)
        if c==0: continue
        G=kg(sets); tested+=1
        ts=np.arange(1,N+1,dtype=float)
        M=np.array([[t**k for k in range(c)] for t in ts])
        for _ in range(40):
            y=np.random.default_rng(rnd.randint(0,10**9)).normal(size=c)
            z=M@y
            a=[min(max(z[i],0) for i in e) for e in sets]
            b=[min(max(-z[i],0) for i in e) for e in sets]
            s=sum(a)+sum(b)
            if s<=1e-9: bad+=1; continue
            A=[i for i in range(len(sets)) if a[i]>1e-12]; B=[i for i in range(len(sets)) if b[i]>1e-12]
            if any(not G.has_edge(i,j) for i in A for j in B): bad+=1
    return tested,bad

# ---- (2) C5 와 comp(C7) 의 Kneser 표현: 증명에서 고른 U 가 통하는지 + cd 최댓값 ----
def reps_from_intersection_graph(Gi, mult_edge, mult_priv):
    # Gi: 교차 그래프(= 보완). 점 = Gi 의 간선(다중도 mult_edge) 또는 사적 점
    pts=[]; owner=[]
    for (u,v) in Gi.edges():
        for r in range(mult_edge): owner.append({u,v})
    for v in Gi.nodes():
        for r in range(mult_priv[v]): owner.append({v})
    sets={v:frozenset(i for i,o in enumerate(owner) if v in o) for v in Gi.nodes()}
    return sets, len(owner)

def test_rep_family(Gi, trials, seed):
    rnd=random.Random(seed); worst=0
    for _ in range(trials):
        me=rnd.randint(1,2); mp={v:rnd.randint(0,1) for v in Gi.nodes()}
        sets,N=reps_from_intersection_graph(Gi,me,mp)
        if N>16: continue
        S=[sets[v] for v in sorted(Gi.nodes())]
        G=kg(S)
        c=cd(range(N), S)
        worst=max(worst,c)
    return worst

if __name__=="__main__":
    print("정리 A 사상 점검 (시험 수, 위반):", thmA_check())
    C5=nx.cycle_graph(5)           # 교차 그래프 = 보완(C5)=C5 (동형)
    print("C5 표현들의 cd 최댓값(표본):", test_rep_family(nx.complement(nx.cycle_graph(5)),300,2))
    C7=nx.cycle_graph(7)           # KG = comp(C7) 이면 교차 그래프 = C7
    print("comp(C7) 표현들의 cd 최댓값(표본):", test_rep_family(C7,150,3))
