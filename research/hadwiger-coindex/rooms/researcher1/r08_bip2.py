# R08 researcher1: can C5[K2] be split into 2 induced bipartite pieces? (guessing aid)
from r08_zig import C5K2
adj = C5K2()
V = sorted(adj)
def bipartite(S):
    col = {}
    for s in S:
        if s in col: continue
        col[s]=0; stack=[s]
        while stack:
            u=stack.pop()
            for w in adj[u]:
                if w in S:
                    if w not in col:
                        col[w]=1-col[u]; stack.append(w)
                    elif col[w]==col[u]:
                        return False
    return True
found=None
for mask in range(2**10):
    A=[v for v in V if (mask>>v)&1]
    B=[v for v in V if not (mask>>v)&1]
    if bipartite(set(A)) and bipartite(set(B)):
        found=(A,B); break
print("2 induced bipartite pieces:", found)
