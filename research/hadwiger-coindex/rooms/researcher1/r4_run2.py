import sys,random,itertools
sys.path.insert(0,'.')
from r4_blowup import *
def analyze(name,G,ms,perm_all=True,verify=()):
    G=nx.convert_node_labels_to_integers(G)
    V,idx,nb,T=types(G); n=len(V); w=omega(G)
    print(f"== {name}: n={n} omega={w} 극대타입={len(T)}")
    for m in ms:
        best=None
        orders=itertools.permutations(range(n)) if perm_all else [list(range(n))]
        for o in orders:
            v,_=Dsigma(n,T,o,m)
            if best is None or v<best[0]: best=(v,o)
        print(f"  m={m}: min_sigma D = {best[0]} (=> tau<= {best[0]+1}); m*omega={m*w}; 최선 순서 {best[1]}")
        if m in verify:
            br=brute(G,m); ex=expand(n,m,T)
            print("    brute==타입전개:",br==ex,len(br))
            d=best[0]
            print("    exact 모멘트 검증 (최대변화,실패수):",check_moment(n,m,br,list(best[1]),d))
analyze("Cbar7=C7^2",nx.complement(nx.cycle_graph(7)),[1,2,3],verify=(2,))
analyze("W5",nx.wheel_graph(6),[1,2,3],verify=(2,3))
