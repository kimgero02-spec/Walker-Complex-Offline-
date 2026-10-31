n = 10
names = ["0","0'","1","1'","2","2'","3","3'","4","4'"]
E = set()
for i in range(5):
    for j in range(5):
        if (j-i) % 5 in (1, 4):
            for s in range(2):
                for t in range(2):
                    E.add(frozenset((2*i+s, 2*j+t)))
print("edge count", len(E))
adj = [[frozenset((a, b)) in E for b in range(n)] for a in range(n)]
pos = {v: v for v in range(n)}
res = {}
for la in range(1, 1 << n):
    A = [i for i in range(n) if la >> i & 1]
    common = [j for j in range(n) if not (la >> j) & 1 and all(adj[a][j] for a in A)]
    for lb in range(1, 1 << len(common)):
        B = [common[k] for k in range(len(common)) if lb >> k & 1]
        seq = sorted([(v, 0) for v in A] + [(v, 1) for v in B])
        runs = 1 + sum(seq[k][1] != seq[k-1][1] for k in range(1, len(seq)))
        res.setdefault(runs, []).append((A, B))
print({k: len(v) for k, v in res.items()})
for A, B in res[max(res)][:3]:
    print("A", [names[a] for a in A], "B", [names[b] for b in B])
