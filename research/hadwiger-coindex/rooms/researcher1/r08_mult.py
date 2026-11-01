# R08 researcher1: zig certificates for the A-type multiplicative counterexample pieces. Guessing aid only.
from r08_zig import graph, search
def circ(n, dists):
    E=set()
    for i in range(n):
        for d in dists:
            j=(i+d)%n
            E.add((min(i,j),max(i,j)))
    return graph(n, sorted(E))
for name,adj in [("C10(1,2)",circ(10,[1,2])),("C10(3,4,5)",circ(10,[3,4,5]))]:
    b,o=search(adj, iters=8000, seed=5)
    print(name, "zig certificate (runs) =", b, "order =", o)
# edge-disjoint union check
E1=set((min(i,(i+d)%10),max(i,(i+d)%10)) for i in range(10) for d in [1,2])
E2=set((min(i,(i+d)%10),max(i,(i+d)%10)) for i in range(10) for d in [3,4,5])
print("edge counts", len(E1), len(E2), "disjoint", not (E1&E2), "total", len(E1|E2), "= K10 edges 45:", len(E1|E2)==45)
