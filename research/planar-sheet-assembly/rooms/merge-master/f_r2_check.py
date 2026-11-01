# F-R2: 정의 R' (흰-흰 간선은 데이터가 아니라 유도) 로 E3/E4 재구성 확인
import networkx as nx, itertools
def assemble(pieces, classes):
    """pieces: {name: (edges, boundary_cycle_list)}, classes: list of sets of (piece, v)."""
    rep = {}
    for i, c in enumerate(classes):
        for pv in c: rep[pv] = f"J{i}"
    G = nx.MultiGraph(); 
    for k, (E, C) in pieces.items():
        for u, v in E:
            G.add_edge(rep.get((k,u), (k,u)), rep.get((k,v), (k,v)), piece=k)
    return G
def derived_white_edges(pieces, classes):
    # ww' 흰-흰 간선 <=> 포트가 인접한 조각이 둘 이상 (정의 R'(R3))
    out = []
    for (i, a), (j, b) in itertools.combinations(list(enumerate(classes)), 2):
        ks = []
        for k, (E, C) in pieces.items():
            pa = [v for (kk, v) in a if kk == k]; pb = [v for (kk, v) in b if kk == k]
            if any((u, v) in E or (v, u) in E for u in pa for v in pb): ks.append(k)
        if len(ks) >= 2: out.append((i, j, tuple(ks)))
    return out
def link(classes, wedges):
    L = {i: nx.Graph() for i in range(len(classes))}
    for i, j, ks in wedges:
        for x in (i, j): L[x].add_edge(*ks[:2]) if len(ks) == 2 else None
    return L
def cyc(vs): return [(vs[i], vs[(i+1) % len(vs)]) for i in range(len(vs))]
def report(name, pieces, classes):
    M = assemble(pieces, classes); G = nx.Graph(M)
    w = derived_white_edges(pieces, classes); L = link(classes, w)
    par = M.number_of_edges() - G.number_of_edges()
    shared = sum(1 for _, _, ks in w)
    print(name, "| V,E =", G.number_of_nodes(), G.number_of_edges(), "| planar:", nx.check_planarity(G)[0],
          "| K5:", nx.is_isomorphic(G, nx.complete_graph(5)), "| 겹친간선(식별 대상):", par, "흰-흰 간선:", shared)
    for i, c in enumerate(classes):
        if len(c) > 2 or (L[i].number_of_nodes() and not nx.is_tree(L[i])):
            print("   흰점", i, "포트", sorted(c), "링크 L(w) 간선", sorted(L[i].edges()), "경로?",
                  L[i].number_of_nodes() > 0 and nx.is_tree(L[i]) and max(dict(L[i].degree()).values()) <= 2)
# E4: W4 (테두리 a b d c, 중심 e) + C4 (a b c d), 호 ab, cd
W4 = (cyc("abdc") + [("e", x) for x in "abdc"], list("abdc"))
C4 = (cyc("abcd"), list("abcd"))
cls = [{("W", x), ("C", x)} for x in "abcd"]
report("E4  W4∪C4", {"W": W4, "C": C4}, cls)
# 비교: 정사각형 두 장 (같은 호, 같은 부호) -> K4
S1 = (cyc("abdc"), list("abdc"))
report("K4  C4∪C4", {"W": S1, "C": C4}, cls)
# W4∪W4 (둘 다 강체) 
W4b = (cyc("abcd") + [("f", x) for x in "abcd"], list("abcd"))
report("W4∪W4", {"W": W4, "C": W4b}, cls)
# E3 재구성: W4 를 삼각형 4장으로 쪼갬 + C4
T = {f"T{i}": (cyc(t), list(t)) for i, t in enumerate(["eab", "ebd", "edc", "eca"])}
T["C"] = C4
cls3 = [{("T0","a"),("T3","a"),("C","a")}, {("T0","b"),("T1","b"),("C","b")},
        {("T1","d"),("T2","d"),("C","d")}, {("T2","c"),("T3","c"),("C","c")},
        {("T0","e"),("T1","e"),("T2","e"),("T3","e")}]
report("E3  4삼각형∪C4", T, cls3)
# 대안 쪼갬: W4 를 경로 b-e-c 로 둘로 (Q1 = a b e c + 현 ae, Q2 = b d c e + 현 ed)
Q1 = (cyc("abec") + [("a","e")], list("abec")); Q2 = (cyc("bdce") + [("e","d")], list("bdce"))
cls4 = [{("Q1","a"),("C","a")}, {("Q1","b"),("Q2","b"),("C","b")}, {("Q1","c"),("Q2","c"),("C","c")},
        {("Q2","d"),("C","d")}, {("Q1","e"),("Q2","e")}]
report("E3' Q1∪Q2∪C4", {"Q1": Q1, "Q2": Q2, "C": C4}, cls4)
# 혼합 평면 예: K4 띠 + W4 를 변 bc 에 매단 것
W4c = (cyc("bcpq") + [("g", x) for x in "bcpq"], list("bcpq"))
cls5 = [{("W", "a"), ("C", "a")}, {("W", "b"), ("C", "b"), ("R", "b")}, {("W", "c"), ("C", "c"), ("R", "c")}, {("W", "d"), ("C", "d")}]
report("혼합  C4∪C4∪W4(bc)", {"W": S1, "C": C4, "R": W4c}, cls5)
