# 정확(유리수) 검증: y 를 분모 D 의 유리수로 반올림하고, 각 극대쌍 (A,B) 에 대해 LP 로 얻은 (w,c) 를 유리수로 반올림한 뒤
# 모든 부등식 w.y_a + c >= 1 (a in A), w.y_b + c <= -1 (b in B) 을 Fraction 으로 직접 확인한다.
import sys
from fractions import Fraction
import numpy as np
import networkx as nx
sys.path.insert(0, "/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2")
from cert import lex_product_c, max_pairs, margin_for_pair

def complement_c7():
    G = nx.complement(nx.cycle_graph(7))
    return G

def exact_check(G, Y, d, D=10**4):
    V = list(G.nodes()); idx = {v: k for k, v in enumerate(V)}
    Yq = [[Fraction(round(float(x) * D), D) for x in row] for row in Y]
    Y = np.array([[float(x) for x in row] for row in Yq])  # LP 도 반올림된 y 로 푼다
    pairs = max_pairs(G)
    worst_margin_float = 1e9
    for (Al, Bl) in pairs:
        dl, sol = margin_for_pair(np.array(Y), Al, Bl, idx, d)
        worst_margin_float = min(worst_margin_float, dl)
        # 정수 스케일 (w,c) 를 유리수로 반올림 후 1/ (w,c) 를 키워 정확 검사: 목표는 w.y+c >= 1 / <= -1 이므로 여기선 w,c 를 (1/delta) 배
        if sol is None or dl <= 0:
            return False, ("float 분리 실패", Al, Bl)
        w = [Fraction(round(float(x) * 10**9), 10**9) / Fraction(dl * 0.5) for x in sol[:d]]
        c = Fraction(round(float(sol[d]) * 10**9), 10**9) / Fraction(dl * 0.5)
        for a in Al:
            val = sum(w[i] * Yq[idx[a]][i] for i in range(d)) + c
            if not val >= 1:  # 여유 비율 0.5 로 스케일 (실제 여유 2)
                return False, ("A 쪽 실패", a, float(val))
        for b in Bl:
            val = sum(w[i] * Yq[idx[b]][i] for i in range(d)) + c
            if not val <= -1:
                return False, ("B 쪽 실패", b, float(val))
    return True, ("pairs", len(pairs), "float worst margin", worst_margin_float, "rational D", D)

if __name__ == "__main__":
    which, d = sys.argv[1], int(sys.argv[2])
    Y = np.load(f"/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/{which}_d{d}.npy")
    if which == "C5K2": G = lex_product_c(5, 2)
    elif which == "C5K3": G = lex_product_c(5, 3)
    elif which == "C7K2": G = lex_product_c(7, 2)
    elif which == "compC7": G = complement_c7()
    print(exact_check(G, Y, d))
