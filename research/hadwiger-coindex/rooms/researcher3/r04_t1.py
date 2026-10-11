from r04_lib import *
for name,G in tests():
    t=time.time(); o,np_=solve(G); mx=max(dict(G.degree()).values())
    res=[]
    for r in list(G.nodes())[:: max(1,G.number_of_nodes()//8)]:
        o2,_=solve_levels(G,r); res.append(bool(o2))
    print(name,"pairs",np_,"maxdeg",mx,"free SAT",bool(o),"BFS-level-monotone SAT per root:",res,round(time.time()-t,1),flush=True)
