# reduction: proper 5-coloring + class order; violation iff rainbow K_{2,3} with 2-side colors at positions (2,4)
from r04_lib import *
def smallest_last(G):
    H=G.copy(); seq=[]
    while H.number_of_nodes():
        v=min(H.nodes(),key=H.degree); seq.append(v); H.remove_node(v)
    return seq[::-1]
def greedy(G,seq):
    c={}
    for v in seq:
        used={c[u] for u in G[v] if u in c}; c[v]=min(k for k in range(1,10) if k not in used)
    return c
def dangerous(G,c):
    D=set()
    for a,b,C in pairs_of(G):
        if c[a]==c[b]: continue
        cols={c[x] for x in C}
        if len(cols)>=3:
            # need three distinct colors besides c[a],c[b]; they are automatically != c[a],c[b]
            D.add(frozenset((c[a],c[b])))
    return D
def orderfromcol(G,c,perm):
    rank={col:i for i,col in enumerate(perm)}
    return sorted(G.nodes(),key=lambda v:rank[c[v]])
if __name__=="__main__":
    for name,G in tests():
        c=greedy(G,smallest_last(G)); k=max(c.values())
        D=dangerous(G,c)
        print(name,"colors",k,"dangerous pairs",sorted(tuple(sorted(p)) for p in D),flush=True)
        if k==5:
            cols=range(1,6); ok=False
            for perm in itertools.permutations(cols):
                if frozenset((perm[1],perm[3])) not in D:
                    o=orderfromcol(G,c,perm); print("   perm",perm,"violations",nviol(G,o)); ok=True; break
            print("   bridge-free pair exists:",ok)
