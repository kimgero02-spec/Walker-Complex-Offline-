# h_M(G) >= 5 판정: K5 의 평면분해 D 중 |V(M°(D))| <= |V(G)| 인 것을 모두 만들고, M°(D) ⪯ G 인지 모형을 찾는다.
# (G 가 3-정칙이면 차수 d 인 X-점의 가지 집합은 d-2 점 이상 필요)
import networkx as nx, itertools as it, sys
sys.setrecursionlimit(10000)
E5=list(it.combinations(range(5),2))
def Mcirc(N,pieces):
    X=nx.Graph(); F={v:[] for v in range(N)}
    for k,P in enumerate(pieces):
        vs=set(x for e in P for x in e)
        for v in vs: F[v].append(k); X.add_node(('c',v,k))
        for u,v in P: X.add_edge(('c',u,k),('c',v,k))
    for v in range(N):
        if len(F[v])>=2:
            for k in F[v]: X.add_edge(('w',v),('c',v,k))
    return X
def decomps(budget):
    pcs=[]
    for r in range(1,10):
        for S in it.combinations(range(10),r):
            pcs.append(frozenset(S))   # 10변 전부(K5)는 제외(비평면)
    seen=set(); out=[]
    def cost(pl):
        f=[0]*5
        for P in pl:
            for x in set(x for i in P for x in E5[i]): f[x]+=1
        return sum((1 if c==1 else c+1) for c in f if c>0), f
    def rec(pl,cov,start):
        c,f=cost(pl)
        if c>budget: return
        if len(cov)==10:
            if all(x>=1 for x in f): out.append(list(pl))
            return
        # 가장 작은 미덮임 변을 포함하는 조각만 추가 (중복 허용: mu>=2)
        e=min(set(range(10))-cov)
        for i in range(start,len(pcs)):
            P=pcs[i]
            if e in P: rec(pl+[P],cov|P,i)
    rec([],frozenset(),0)
    return out
def has_minor(G,X,maxset=8):
    # 연결 부분집합
    CS={}
    for v in G:
        stack=[frozenset([v])]
        while stack:
            S=stack.pop()
            if S in CS: continue
            CS[S]=set().union(*[set(G[x]) for x in S])-S
            if len(S)<maxset:
                for x in S:
                    for y in G[x]:
                        if y not in S: stack.append(S|{y})
    dmax=max(d for _,d in G.degree())
    need=lambda d: max(1,d-(dmax-1)) if dmax==3 else 1
    order=sorted(X.nodes(),key=lambda x:-X.degree(x))
    # BFS-ish order to use adjacency pruning
    o=[order[0]]
    while len(o)<len(order):
        cand=[x for x in order if x not in o]
        cand.sort(key=lambda x:(-sum(1 for y in X[x] if y in o),-X.degree(x)))
        o.append(cand[0])
    bysize=sorted(CS,key=len)
    n=G.number_of_nodes()
    def rec(i,asg,used):
        if i==len(o): return dict(asg)
        rem=sum(need(X.degree(x)) for x in o[i:])
        if rem>n-len(used): return None
        x=o[i]; nbrs=[asg[y] for y in X[x] if y in asg]
        for S in bysize:
            if len(S)<need(X.degree(x)) or S&used: continue
            if len(CS[S])<X.degree(x): continue
            if all(CS[S]&T for T in nbrs):
                asg[x]=S; r=rec(i+1,asg,used|S)
                if r: return r
                del asg[x]
        return None
    return rec(0,{},frozenset())
if __name__=='__main__':
    name=sys.argv[1]
    G={'heawood':nx.heawood_graph(),'petersen':nx.petersen_graph()}[name]
    Ds=decomps(G.number_of_nodes())
    Xs=[];hs=set()
    for D in Ds:
        X=Mcirc(5,[[E5[i] for i in P] for P in D])
        h=nx.weisfeiler_lehman_graph_hash(X)
        if any(h==hh and nx.is_isomorphic(X,Y) for hh,Y in Xs): continue
        Xs.append((h,X))
    print(name,'decomps',len(Ds),'distinct M°',len(Xs))
    for h,X in sorted(Xs,key=lambda t:t[1].number_of_nodes()):
        m=has_minor(G,X)
        print(X.number_of_nodes(),X.number_of_edges(),sorted(d for _,d in X.degree()),'MINOR' if m else '-')
        if m: print({str(k):sorted(v) for k,v in m.items()}); break
