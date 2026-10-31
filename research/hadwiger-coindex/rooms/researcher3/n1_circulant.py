import networkx as nx, subprocess, itertools, time, math, sys
sys.argv=['x']
exec(open('n1_dr2.py').read().split('if __name__')[0])
def rho1(G):
    n=G.number_of_nodes()
    inp=f"{n} {G.number_of_edges()} "+" ".join(f"{u} {v}" for u,v in G.edges())+"\n"
    return int(subprocess.run(["./n1_rho1","x"],input=inp,capture_output=True,text=True,timeout=280).stdout.split()[0])
seen=set(); t0=time.time(); rows=[]
for n in range(8,12):
    half=list(range(1,n//2+1))
    for r in range(2,len(half)+1):
        for S in itertools.combinations(half,r):
            # canonical under multiplier
            units=[u for u in range(1,n) if math.gcd(u,n)==1]
            can=min(tuple(sorted(min((u*s)%n,n-(u*s)%n) for s in S)) for u in units)
            if (n,can) in seen: continue
            seen.add((n,can))
            if can!=tuple(S): continue
            G=nx.circulant_graph(n,list(S))
            if not nx.is_connected(G): continue
            if max(len(c) for c in nx.find_cliques(G))>=4: continue
            if nx.is_bipartite(G): continue
            if time.time()-t0>200: break
            r_=rho1(G)
            if r_>=4:
                P=search(G,iters=30000)
                rows.append((n,S,G.number_of_edges(),r_,"placement" if P else "none"))
                print(n,S,G.number_of_edges(),"zig=",r_,"planar placement:", "FOUND" if P else "none",flush=True)
print("done",time.time()-t0)
