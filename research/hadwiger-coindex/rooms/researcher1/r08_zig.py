# R08 researcher1: zig (run-number) upper certificates by random search. Guessing aid only.
import itertools, random

def graph(n, edges):
    adj = {v:set() for v in range(n)}
    for a,b in edges: adj[a].add(b); adj[b].add(a)
    return adj

def K(n): return graph(n, [(i,j) for i in range(n) for j in range(i+1,n)])
def K33(): return graph(6, [(i,j) for i in range(3) for j in range(3,6)])
def C5K2():
    # vertex (i,s) -> 2*i+s
    E=[]
    for i in range(5):
        E.append((2*i,2*i+1))
        j=(i+1)%5
        for s in (0,1):
            for t in (0,1): E.append((2*i+s, 2*j+t))
    return graph(10, E)

def maximal_bicliques(adj):
    V = sorted(adj); out=[]
    for r in range(1,len(V)+1):
        for A in itertools.combinations(V,r):
            common=set(V)
            for a in A: common &= adj[a]
            common -= set(A)
            if common: out.append((frozenset(A), frozenset(common)))
    return V,out

def runs_max(order, bics):
    m=0
    for A,B in bics:
        seq=[1 if v in A else 2 for v in order if (v in A or v in B)]
        r=1+sum(1 for i in range(1,len(seq)) if seq[i]!=seq[i-1])
        m=max(m,r)
    return m

def search(adj, iters=20000, seed=1):
    V,bics = maximal_bicliques(adj)
    rnd=random.Random(seed); order=V[:]; rnd.shuffle(order)
    cur=runs_max(order,bics); best=cur; bo=order[:]
    for _ in range(iters):
        i,j=rnd.sample(range(len(order)),2)
        new=order[:]; new[i],new[j]=new[j],new[i]
        val=runs_max(new,bics)
        if val<=cur or rnd.random()<0.03:
            order,cur=new,val
            if val<best: best,bo=val,new[:]
    return best,bo

if __name__=="__main__":
    for name,adj in [("K5",K(5)),("K6",K(6)),("K33",K33()),("C5[K2]",C5K2())]:
        b,o=search(adj, iters=8000, seed=3)
        print(name, "best runs found =", b, "order =", o)
