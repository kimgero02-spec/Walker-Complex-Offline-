import itertools
n = 10
E = set()
for i in range(5):
    for j in range(5):
        if (j-i) % 5 in (1, 4):
            for s in range(2):
                for t in range(2):
                    E.add(frozenset((2*i+s, 2*j+t)))
adj = [[frozenset((a, b)) in E for b in range(n)] for a in range(n)]
order = list(range(n))          # identity order: (0,0'),(1,1'),...,(4,4')
pos = {v: k for k, v in enumerate(order)}
worst = 0; cnt_b = 0
for la in range(1, 1 << n):
    A = [i for i in range(n) if la >> i & 1]
    common = [j for j in range(n) if not la >> j & 1 and all(adj[a][j] for a in A)]
    for lb in range(1, 1 << len(common)):
        B = [common[k] for k in range(len(common)) if lb >> k & 1]
        cnt_b += 1
        seq = sorted([(pos[v], 0) for v in A] + [(pos[v], 1) for v in B])
        runs = 1 + sum(seq[k][1] != seq[k-1][1] for k in range(1, len(seq)))
        worst = max(worst, runs)
print("bicliques (all, nonempty A,B):", cnt_b, " max runs under identity order:", worst)
