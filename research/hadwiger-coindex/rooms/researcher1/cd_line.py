# 선(line) 표현: 원소 = C_n 의 간선 a_i=(i,i+1), e_i = {a_{i-1}, a_i}. e_i∩e_j≠∅ ⇔ |i-j|=1 (mod n) ⇒ KG(H) = complement(C_n).
from cd_check import cd_of
def line_rep(n):
    ground = [('a', i) for i in range(n)]
    hedges = {i: frozenset([('a', (i - 1) % n), ('a', i)]) for i in range(n)}
    return ground, hedges
for n in (5, 7):
    ground, H = line_rep(n)
    # 인접 검증: KG(H) = complement of C_n
    for x in range(n):
        for y in range(x + 1, n):
            adj_G = ((y - x) % n not in (1, n - 1))  # 보완 그래프 간선
            assert (not (H[x] & H[y])) == adj_G
    res = cd_of(ground, H)
    print('comp(C%d) line rep: cd(H)=' % n, res[0], 'U=', res[1], flush=True)
