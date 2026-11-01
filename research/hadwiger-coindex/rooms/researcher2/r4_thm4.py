# Steiner 정리 4 (10-11쪽) 구성의 점검: S(n,k) 안의 홀수 K_{n-2k+2} 확장
import itertools, networkx as nx
def stable(S,n):
    return all(((x%n)+1) not in S for x in S) and not (1 in S and n in S)
def check(n,k):
    V=[frozenset(c) for c in itertools.combinations(range(1,n+1),k) if stable(set(c),n)]
    Vs=set(V)
    adj=lambda a,b: not (a&b)
    # A = S(2k-1,k-1) 의 정점
    A=[frozenset(c) for c in itertools.combinations(range(1,2*k),k-1) if stable(set(c),2*k-1)]
    A0=frozenset(range(2,2*k-1,2)); A1=frozenset(range(1,2*k-2,2))
    def c(a):
        if a==A0: return 1
        return 1 if 1 in a else 2
    trees=[];col={}
    for i in range(1,n-2*k+1):
        T=[]
        for a in A:
            X=a|{i+c(a)+2*k-2}; assert X in Vs
            T.append(X); col[X]=c(a)
        trees.append(T)
    t1=frozenset(range(1,2*k,2)); t2=frozenset(list(range(2,2*k-1,2))+[n])
    assert t1 in Vs and t2 in Vs
    trees.append([t1]); trees.append([t2]); col[t1]=1; col[t2]=1
    allv=[x for T in trees for x in T]; assert len(allv)==len(set(allv))
    for T in trees[:-2]:
        H=nx.Graph(); H.add_nodes_from(T)
        for a,b in itertools.combinations(T,2):
            if adj(a,b): H.add_edge(a,b)
        assert nx.is_tree(H), "경로 아님"
        for a,b in H.edges(): assert col[a]!=col[b]
    for p,q in itertools.combinations(range(len(trees)),2):
        assert any(adj(a,b) and col[a]==col[b] for a in trees[p] for b in trees[q]),(p,q)
    return len(trees),len(V)
for n,k in [(4,2),(5,2),(6,2),(7,2),(8,2),(9,3),(10,3),(11,3),(13,4),(14,4)]:
    try: print(n,k,check(n,k),"= n-2k+2 =",n-2*k+2,"OK")
    except AssertionError as e: print(n,k,"FAIL",e)
