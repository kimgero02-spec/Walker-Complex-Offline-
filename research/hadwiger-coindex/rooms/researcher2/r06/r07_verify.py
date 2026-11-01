# R07 반례꾼: 곱 법칙 반례 K_n = C_n(1,2) ∪ C_n(S2) 의 독립 검증 (완전 열거 + 명시적 순서)
import sys
sys.path.insert(0,'.')
from graphs import circulant, zig_at_most, clique_number
def all_complete_pairs(n, adj):
    # 모든 (A,B), A,B 비공집합, A∩B=∅, A×B ⊆ E  (독립 열거, 극대성 가정 없음)
    res = []
    for A in range(1, 1<<n):
        common = (1<<n)-1
        for v in range(n):
            if A>>v&1: common &= adj[v]
        if common == 0: continue
        B = common
        sub = B
        while sub:
            res.append((A, sub))
            sub = (sub-1) & B
    return res
def max_runs(n, adj, order):
    pos = {v:i for i,v in enumerate(order)}
    worst = 0
    for A, B in all_complete_pairs(n, adj):
        seq = sorted([(pos[v],0) for v in range(n) if A>>v&1] + [(pos[v],1) for v in range(n) if B>>v&1])
        r = 0; last=None
        for _, s in seq:
            if s != last: r += 1; last = s
        worst = max(worst, r)
    return worst
for n, S2 in [(10,[3,4,5]), (11,[3,4,5])]:
    g1 = circulant(n,[1,2]); g2 = circulant(n,S2)
    for name,(m,adj) in [('C%d(1,2)'%n,g1), ('C%d(%s)'%(n,','.join(map(str,S2))),g2)]:
        o = zig_at_most(m, adj, 3)
        print(name, 'omega', clique_number(m,adj), 'order with max runs<=3 found:', o is not None, 'independent max runs:', max_runs(m,adj,o) if o else None, flush=True)
    # K_n: 완전 그래프 zig = n (τ(K_n)=n <= zig): 확인 - 3 로는 불가능한지: 임의 순서의 max runs 는 n? 
    kn = circulant(n, list(range(1, n//2+1)))
    print('K%d check: zig_at_most(%d) ->' % (n, n-1), zig_at_most(kn[0], kn[1], n-1) is not None, flush=True)
