# R07 반례꾼 검증: 시트 분해 주장들의 직접 계산
import sys, time
sys.path.insert(0,'.')
from graphs import *
from homol import betti_gf2, box_complex_empty
def E_of(n, adj): return sorted({(i,j) for i in range(n) for j in range(i+1,n) if adj[i]>>j&1})
def kn(n): return from_edges(n, [(i,j) for i in range(n) for j in range(i+1,n)])
def multipartite(parts):
    n = sum(parts); lab=[]
    for p,s in enumerate(parts): lab += [p]*s
    E=[(i,j) for i in range(n) for j in range(i+1,n) if lab[i]!=lab[j]]
    return from_edges(n, E)
def faces_of_sub(n, edges):
    adj=[0]*n
    for a,b in edges: adj[a]|=1<<b; adj[b]|=1<<a
    return box_complex_empty(n, adj)
if __name__ == '__main__':
    oct_ = multipartite([2,2,2]); pm3 = from_edges(6, [(0,1),(2,3),(4,5)])
    print('K6 check: zig(oct)', zig(*oct_)[0], 'zig(PM3)', zig(*pm3)[0], 'zig(K6)', zig(*kn(6))[0], flush=True)
    n=5; K5E = E_of(*kn(5))
    e_one = [(0,1)]; rest = [e for e in K5E if e != (0,1)]
    print('K5 X betti', betti_gf2(box_complex_empty(*kn(5))), flush=True)
    print('sheet K5-e betti', betti_gf2(faces_of_sub(n,rest)), flush=True)
    U = faces_of_sub(n, rest) | faces_of_sub(n, e_one)
    print('union betti', betti_gf2(U), flush=True)
    k333 = multipartite([3,3,3])
    print('zig(K333)', zig(*k333)[0], flush=True)
