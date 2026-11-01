import itertools, sys
# W5 on vertices 0..5 (0 = hub, 1..5 rim cycle); C5 on 6..10.
def base_edges():
    E = set()
    for i in range(1, 6):
        E.add((0, i))
        j = i % 5 + 1
        E.add((min(i, j), max(i, j)))
    for i in range(5):
        a, b = 6 + i, 6 + (i + 1) % 5
        E.add((min(a, b), max(a, b)))
    return E
def cross_pairs():
    return [(u, v) for u in range(6) for v in range(6, 11)]
N = 11

def has_K_minor(edges, t, n=N):
    adj = [0] * n
    for a, b in edges:
        adj[a] |= 1 << b; adj[b] |= 1 << a
    full = (1 << n) - 1
    def connected(S):
        if S == 0: return False
        start = S & -S; seen = start; frontier = start
        while frontier:
            v = (frontier & -frontier).bit_length() - 1
            frontier &= frontier - 1
            nb = adj[v] & S & ~seen
            seen |= nb; frontier |= nb
        return seen == S
    conn = [S for S in range(1, full + 1) if connected(S)]
    nbr = {}
    def N_(S):
        r = 0
        x = S
        while x:
            v = (x & -x).bit_length() - 1; x &= x - 1
            r |= adj[v]
        return r & ~S
    nb_of = {S: N_(S) for S in conn}
    conn_sorted = sorted(conn, key=lambda S: (S & -S))
    # DFS: choose branch sets in increasing order of lowest vertex
    def dfs(chosen, used, count):
        if count == t:
            return True
        for S in conn_sorted:
            if S & used: continue
            if (S & -S) <= (chosen[-1] & -chosen[-1] if chosen else 0): continue
            if all(S & nb_of[T] for T in chosen):
                if dfs(chosen + [S], used | S, count + 1):
                    return True
        return False
    return dfs([], 0, 0)

if __name__ == "__main__":
    E = base_edges() | set((u, v) for u, v in cross_pairs())
    print("edges", len(E), "K7 minor (full join):", has_K_minor(E, 7))
