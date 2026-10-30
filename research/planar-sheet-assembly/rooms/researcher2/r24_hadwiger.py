# R24 researcher2 (해드위거 판): 손 증명의 오타 확인용 작은 계산. 근거로 쓰지 않는다.
import itertools, networkx as nx

def has_Kt_minor(G, t):
    """가지 집합 배정 전수 (작은 그래프 전용). 각 점에 0..t (t=미사용) 를 준다."""
    V = list(G.nodes()); n = len(V)
    for lab in itertools.product(range(t + 1), repeat=n):
        if any(lab.count(i) == 0 for i in range(t)): continue
        if lab[0] not in (0, t): continue          # 대칭 줄이기
        B = [[V[j] for j in range(n) if lab[j] == i] for i in range(t)]
        if not all(nx.is_connected(G.subgraph(b)) for b in B): continue
        ok = True
        for i, j in itertools.combinations(range(t), 2):
            if not any(G.has_edge(u, v) for u in B[i] for v in B[j]): ok = False; break
        if ok: return B
    return None

def K4K2():
    return nx.cartesian_product(nx.complete_graph(4), nx.complete_graph(2))

def ident(G, u, v):
    H = nx.contracted_nodes(G, u, v, self_loops=False); return nx.Graph(H)

if __name__ == '__main__':
    P = K4K2()
    print('K4xK2: K5 model', has_Kt_minor(P, 5)); print('K4xK2: K6?', has_Kt_minor(P, 6))
    C4 = nx.cycle_graph(4)
    print('C4 K3?', bool(has_Kt_minor(C4, 3)), ' C4/{0=2} K3?', bool(has_Kt_minor(ident(C4, 0, 2), 3)))
    P4 = nx.path_graph(4)
    print('P4 K3?', bool(has_Kt_minor(P4, 3)), ' P4/{0=3} K3?', bool(has_Kt_minor(ident(P4, 0, 3), 3)))
    # Hajos 합 K4 (+) K4: K4 마이너 유지 확인
    G1 = nx.relabel_nodes(nx.complete_graph(4), {0: 'x', 1: 'a1', 2: 'a2', 3: 'a3'})
    G2 = nx.relabel_nodes(nx.complete_graph(4), {0: 'x', 1: 'b1', 2: 'b2', 3: 'b3'})
    H = nx.compose(G1, G2); H.remove_edge('x', 'a1'); H.remove_edge('x', 'b1'); H.add_edge('a1', 'b1')
    print('K4 hajos K4: K4 minor', has_Kt_minor(H, 4))
