# F-R1 병합마스터: 병합 설명서 B 의 작은 예 확인 (뫼비우스/프리즘 정사각형 3장, K4 두 정사각형)
import networkx as nx, itertools
def build(n, twist):
    # 정사각형 k: 경계 a_k b_k c_k d_k (순환), 호 k: (c_k d_k) 와 (a_{k+1} b_{k+1}) 를 붙임
    B = nx.Graph()
    for k in range(n):
        cyc = [f"a{k}", f"b{k}", f"c{k}", f"d{k}"]
        for i in range(4):
            B.add_edge(cyc[i], cyc[(i+1)%4], kind="bd")
    for k in range(n):
        j = (k+1) % n
        tw = twist and k == n-1
        # 곧게: c_k~b_j, d_k~a_j (경계 방향 반대로 지남, eps=+1); 꼬임: c_k~a_j, d_k~b_j
        pairs = [(f"c{k}", f"a{j}"), (f"d{k}", f"b{j}")] if tw else [(f"c{k}", f"b{j}"), (f"d{k}", f"a{j}")]
        ws = []
        for (x, y) in pairs:
            w = f"w_{x}_{y}"; ws.append(w)
            B.add_node(w, white=True); B.add_edge(w, x, kind="j"); B.add_edge(w, y, kind="j")
        B.add_edge(ws[0], ws[1], kind="ww")
    return B
def G_of(B):
    H = nx.Graph(B)
    for w in [v for v in B if B.nodes[v].get("white")]:
        for x in list(B[w]):
            if not B.nodes[x].get("white"):
                H = nx.contracted_nodes(H, w, x, self_loops=False) if w in H and x in H else H
    return nx.Graph(H)  # 단순화
def A_of(B):
    A = nx.Graph(B); A.remove_edges_from([(u,v) for u,v,d in B.edges(data=True) if d["kind"]=="ww"]); return A
def subst(A, t):
    S = nx.Graph(); whites = [v for v in A if A.nodes[v].get("white")]
    for u,v in A.edges():
        if u not in whites and v not in whites: S.add_edge(u,v)
    for v in A:
        if v not in whites: S.add_node(v)
    for w in whites:
        K = [(w,i) for i in range(t)]
        for a,b in itertools.combinations(K,2): S.add_edge(a,b)
        for x in A[w]:
            for c in K: S.add_edge(x,c)
    return S
def colorable(G, q):
    nodes = sorted(G, key=lambda v: -G.degree(v)); col = {}
    def bt(i):
        if i == len(nodes): return True
        v = nodes[i]
        for c in range(q):
            if all(col.get(u) != c for u in G[v]):
                col[v] = c
                if bt(i+1): return True
                del col[v]
        return False
    return bt(0)
def chi(G):
    q = 1
    while not colorable(G, q): q += 1
    return q
for n, tw in [(3, False), (3, True), (2, True)]:
    B = build(n, tw); G = G_of(B); A = A_of(B)
    seq = [chi(subst(A, t)) for t in range(4)]
    print(n, tw, "V,E=", G.number_of_nodes(), G.number_of_edges(), "planar", nx.check_planarity(G)[0],
          "K33" if nx.is_isomorphic(G, nx.complete_bipartite_graph(3,3)) else "", "K4" if nx.is_isomorphic(G, nx.complete_graph(4)) else "",
          "chi(A^t)=", seq, "chi(G)=", chi(G))
