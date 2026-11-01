# R04 researcher2 (b): Dirac(차수<=2 정점)만으로 Q_2 순서를 만드는 귀납의 구현과 점검.
import random, itertools, networkx as nx

def cyc_runs_ok(order, X, Y):
    seq=[('X' if v in X else 'Y') for v in order if v in X or v in Y]
    if not seq: return True
    runs=sum(1 for i in range(len(seq)) if seq[i]!=seq[i-1])
    return runs<=2

def max_pairs(G):
    V=list(G.nodes()); out=set()
    for r in range(1,len(V)+1):
        for X in itertools.combinations(V,r):
            Y=set(V)
            for x in X: Y&=set(G[x])
            if not Y: continue
            X2=set(V)
            for y in Y: X2&=set(G[y])
            out.add((frozenset(X2),frozenset(Y)))
    return out

def Q2(G,order):
    for X,Y in max_pairs(G):
        if len(X)>=2 and len(Y)>=2 and not cyc_runs_ok(order,X,Y): return False
    return True

def build(G):
    """차수<=2 정점을 떼고 거꾸로 삽입. 반환: 원형 순서(리스트)."""
    H=G.copy(); stack=[]
    while H.number_of_nodes()>0:
        w=next(v for v in H if H.degree(v)<=2)   # Dirac: 항상 존재 (K4-마이너-자유)
        nb=list(H[w]); stack.append((w,nb)); H.remove_node(w)
    order=[]
    H=nx.Graph()
    for w,nb in reversed(stack):
        # 삽입
        if len(nb)==2:
            u,v=nb
            C=set(H[u])&set(H[v])            # w 를 넣기 전, H 안에서의 공통이웃 C'
            iu,iv=order.index(u),order.index(v)
            n=len(order)
            def arc(i,j):   # i 에서 j 로 시계 방향 열린 호
                out=[];k=(i+1)%n
                while k!=j: out.append(order[k]); k=(k+1)%n
                return out
            a1=arc(iu,iv); a2=arc(iv,iu)
            s1=[c for c in C if c in a1]; s2=[c for c in C if c in a2]
            assert not(s1 and s2), "C' 가 두 호에 걸침: 귀납 가정 위반"
            # w 를 C' 가 있는 호(없으면 a1) 안, u 바로 뒤나 v 바로 뒤에 삽입
            if s2 and not s1: order.insert(iv+1,w)
            else: order.insert(iu+1,w)
        else:
            order.append(w)
        H.add_node(w)
        for x in nb: H.add_edge(w,x)
    return order

def rand_sp(n,seed):
    r=random.Random(seed); G=nx.Graph(); G.add_edge(0,1); k=2
    while k<n:
        op=r.random(); e=r.choice(list(G.edges()))
        if op<0.5:      # 2-트리 삽입
            G.add_edge(k,e[0]); G.add_edge(k,e[1])
        elif op<0.75:   # 세분
            G.remove_edge(*e); G.add_edge(k,e[0]); G.add_edge(k,e[1])
        else:           # 가지
            G.add_edge(k,r.choice(list(G.nodes())))
        k+=1
    for e in list(G.edges()):
        if r.random()<0.15: G.remove_edge(*e)
    return G

if __name__=="__main__":
    bad=0; cnt=0
    for seed in range(40):
        G=rand_sp(random.Random(seed).choice([7,8,9,10]),seed)
        order=build(G); ok=Q2(G,order); cnt+=1
        if not ok: bad+=1; print("실패",seed)
    print("총",cnt,"개 중 Q2 위반",bad)
    # 비인접 u,v 이웃 정점 w 를 가진 그래프 명시 예: C4 + 2 chord-free: K_{2,3}
    G=nx.complete_bipartite_graph(2,3); o=build(G); print("K23",o,Q2(G,o))
    G=nx.complete_bipartite_graph(2,5); o=build(G); print("K25",o,Q2(G,o))
    # K4 에서는 Dirac 가정 실패 (최소차수 3)
    print("K4 min deg",min(d for _,d in nx.complete_graph(4).degree()))
    # 휠
    for k in (5,6):
        W=nx.wheel_graph(k+1)
        V=list(W.nodes()); ok2=False
        for p in itertools.permutations(V[1:]):
            if p[0]>p[-1]: continue
            if Q2(W,[V[0]]+list(p)): ok2=True;break
        print(f"W_{k} Q2 존재:",ok2)
