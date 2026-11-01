# zig(G) = min over linear orders of max over bicliques (A,B), A,B nonempty disjoint, A x B in E,
# of the number of runs of the label word (a/b) restricted to A u B.  Brute force, n <= 6.
import itertools

def zig(n, edges):
    E = set(frozenset(e) for e in edges)
    adj = [[frozenset((i, j)) in E for j in range(n)] for i in range(n)]
    # enumerate bicliques as (A,B) bitmasks, A,B nonempty disjoint, complete between
    bics = []
    for la in range(1, 1 << n):
        A = [i for i in range(n) if la >> i & 1]
        common = [j for j in range(n) if all(adj[a][j] for a in A) and not (la >> j & 1)]
        # B nonempty subset of common
        for lb in range(1, 1 << len(common)):
            B = [common[k] for k in range(len(common)) if lb >> k & 1]
            bics.append((A, B))
    best = None
    for order in itertools.permutations(range(n)):
        pos = {v: i for i, v in enumerate(order)}
        worst = 0
        for A, B in bics:
            seq = sorted([(pos[v], 'a') for v in A] + [(pos[v], 'b') for v in B])
            runs = 1 + sum(1 for k in range(1, len(seq)) if seq[k][1] != seq[k-1][1])
            if runs > worst:
                worst = runs
                if best is not None and worst >= best:
                    break
        if best is None or worst < best:
            best = worst
    return best

def K(n):
    return [(i, j) for i in range(n) for j in range(i+1, n)]

if __name__ == "__main__":
    # octahedron K_{2,2,2}: parts {0,1},{2,3},{4,5}; nonadjacent = same part
    part = {0: 0, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2}
    oct_e = [(i, j) for i in range(6) for j in range(i+1, 6) if part[i] != part[j]]
    pm3 = [(0, 1), (2, 3), (4, 5)]
    print("zig(K_5) =", zig(5, K(5)))
    print("zig(K_6) =", zig(6, K(6)))
    print("zig(octahedron) =", zig(6, oct_e))
    print("zig(3K_2) =", zig(6, pm3))
    print("zig(K_{3,3}) =", zig(6, [(i, j) for i in range(3) for j in range(3, 6)]))
    print("zig(C_5) =", zig(5, [(i, (i+1) % 5) for i in range(5)]))
    print("zig(K_4) =", zig(4, K(4)))
    print("zig(K_6 minus PM3 = oct, union PM3 = K_6 check):", sorted(set(map(frozenset, oct_e + pm3))) == sorted(set(map(frozenset, K(6)))))
