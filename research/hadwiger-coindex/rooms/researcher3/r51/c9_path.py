import itertools
exec(open('c1b_tri.py').read().split('for n in [5')[0])
for n in [6,7,8,9,10]:
    T=list(set(tris(0,n-1))); found=None; cnt=0
    for A,B in itertools.combinations(T,2):
        if A&B: continue
        deg={}
        for e in A:
            for f in B:
                if cross(e,f): deg[e]=deg.get(e,0)+1; deg[f]=deg.get(f,0)+1
        if max(deg.values())<=2: cnt+=1; found=found or (sorted(A),sorted(B))
    print(n,"disjoint pairs with crossing degrees (2,2):",cnt,"example",found)
