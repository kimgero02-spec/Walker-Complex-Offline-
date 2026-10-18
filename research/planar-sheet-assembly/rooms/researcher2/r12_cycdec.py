# R12 망상꾼 (이어서): K_7 의 사이클 분해 -> 3-정칙 28점 M°. 매뉴얼 구조(완전 부호) 수와 Aut 궤도.
# 예측 "매뉴얼 구조들은 Aut 의 한 궤도" 의 반례 찾기 (근거 아님, 반례 탐색용)
import itertools, random, numpy as np, networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher
from r11_levi import manual
from r12_lloyd import check_W

def random_cycle_dec(N, rnd):
    R = nx.complete_graph(N); cycles = []
    while R.number_of_edges():
        v = rnd.choice([x for x in R if R.degree(x)]); path = [v]; pos = {v: 0}
        while True:
            u = rnd.choice(list(R[path[-1]]))
            if len(path) >= 2 and u == path[-2] and R.degree(path[-1]) > 1:
                continue
            if u in pos:
                cyc = path[pos[u]:]; break
            pos[u] = len(path); path.append(u)
        es = [(cyc[i], cyc[(i + 1) % len(cyc)]) for i in range(len(cyc))]
        R.remove_edges_from(es); cycles.append((list(cyc), es))
    return cycles

def perfect_codes(X):
    V = list(X.nodes()); out = []
    def rec(chosen, covered):
        if len(covered) == len(V): out.append(frozenset(chosen)); return
        v = min(set(V) - covered)
        for c in [v] + list(X[v]):
            cl = {c} | set(X[c])
            if cl & covered: continue
            rec(chosen + [c], covered | cl)
    rec([], set()); return set(out)

def analyse(cycles, label):
    Mo, M, G, mu = manual(cycles); X = nx.convert_node_labels_to_integers(Mo)
    codes = [W for W in perfect_codes(X) if check_W(X, sorted(W)) is not None]
    auts = list(GraphMatcher(X, X).isomorphisms_iter())
    orbits = []; left = set(codes)
    while left:
        W = left.pop(); orb = {frozenset(a[x] for x in W) for a in auts}
        orbits.append(len(orb)); left -= orb
    A = nx.to_numpy_array(X); m1 = int(np.sum(abs(np.linalg.eigvalsh(A) + 1) < 1e-8))
    lens = sorted(len(c[0]) for c in cycles)
    print(label, 'cycle lengths', lens, 'structures', len(codes), 'Aut', len(auts), 'orbit sizes', sorted(orbits), 'mult(-1)', m1, flush=True)
    return len(codes), sorted(orbits), len(auts)

if __name__ == '__main__':
    analyse([(list(range(7)), [(i, (i + s) % 7) for i in range(7)]) for s in (1, 2, 3)], 'Coxeter-type')
    rnd = random.Random(12); seen = []
    for t in range(60):
        cyc = random_cycle_dec(7, rnd)
        Mo, _, _, _ = manual(cyc); X = nx.convert_node_labels_to_integers(Mo)
        if any(nx.faster_could_be_isomorphic(X, Y) and nx.is_isomorphic(X, Y) for Y in seen): continue
        seen.append(X)
        n, orb, a = analyse(cyc, 'rand%d' % t)
        if len(orb) > 1:
            print('NON-TRANSITIVE', cyc);
