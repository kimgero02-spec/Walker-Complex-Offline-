import itertools, numpy as np
A=np.array([[0,1,1],[1,0,1],[1,1,0]])
def OA(p):
    iso=[v for v in itertools.product(range(p),repeat=3) if (2*(v[0]*v[1]+v[1]*v[2]+v[0]*v[2]))%p==0]
    def bil(u,v): return (u[0]*(v[1]+v[2])+u[1]*(v[0]+v[2])+u[2]*(v[0]+v[1]))%p
    G=[]
    for r1 in iso:
        for r2 in iso:
            if bil(r1,r2)!=1: continue
            for r3 in iso:
                if bil(r1,r3)==1 and bil(r2,r3)==1:
                    G.append(np.array([r1,r2,r3]))
    return G
if __name__=="__main__":
    for p in (3,5,7): print(p,len(OA(p)),2*p*(p*p-1))
