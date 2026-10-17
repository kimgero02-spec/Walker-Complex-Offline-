# upper bound on zig for larger graphs by randomized local search over orders (upper bound only)
import sys, random; sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3')
from r06_lib import *
def cost(p, MB):
    return max(runs(p,X,Y) for X,Y in MB)
def search(n, E, iters=20000, seed=0):
    random.seed(seed); adj=make(n,E); MB=max_bicliques(adj,n)
    p=list(range(n)); random.shuffle(p); c=cost(p,MB); best=(c,p[:])
    T=1.0
    for it in range(iters):
        q=p[:]; i,j=random.sample(range(n),2)
        q[i],q[j]=q[j],q[i]
        cq=cost(q,MB)
        if cq<=c or random.random()<pow(2.718,-(cq-c)/max(T,1e-3)):
            p,c=q,cq
            if c<best[0]: best=(c,p[:])
        T*=0.9997
    return best
P=[(i,(i+1)%5) for i in range(5)]+[(5+i,5+(i+2)%5) for i in range(5)]+[(i,5+i) for i in range(5)]
if __name__=="__main__":
    for seed in range(3):
        print("Petersen zig-upper seed",seed, search(10,P,iters=20000,seed=seed), flush=True)
    C=[(i,(i+1)%7) for i in range(7)]
    print("C7 check", search(7,C,iters=5000,seed=1), flush=True)
