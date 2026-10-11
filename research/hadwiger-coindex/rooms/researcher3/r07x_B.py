import sys; sys.path.insert(0,'/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3')
from r06_lib import *
def sub(n,E,S):
    # induced subgraph on S, relabeled
    m={v:i for i,v in enumerate(S)}
    return len(S),[(m[u],m[v]) for u,v in E if u in m and v in m]
def faces_restrict(F,n,S):
    # faces of X(G) lying entirely in block S x {1,2}  (= X(G[S]) as full subcomplex)
    Sc=set(S)|{n+v for v in S}
    return {k:[f for f in v if set(f)<=Sc] for k,v in F.items()}
def union(Fs):
    U={}
    for F in Fs:
        for k,v in F.items(): U.setdefault(k,set()).update(v)
    return {k:sorted(v) for k,v in U.items()}
def vpart(name,n,E,parts):
    adj=make(n,E); F=B0_empty(adj,n)
    blocks=[faces_restrict(F,n,S) for S in parts]
    U=union(blocks)
    bf=reduced_betti(F); bu=reduced_betti(U)
    nF=sum(len(v) for v in F.values()); nU=sum(len(v) for v in U.values())
    print(name,"parts",parts,"| X(G) H~",{k:v for k,v in bf.items() if v},"| union of blocks H~",{k:v for k,v in bu.items() if v},"| faces",nF,nU,flush=True)
    return F,U
K=lambda n: list(itertools.combinations(range(n),2))
K33=[(i,3+j) for i in range(3) for j in range(3)]
if __name__=="__main__": vpart("K5",5,K(5),[[0,1,2,3],[4]])
if __name__=="__main__": vpart("K5",5,K(5),[[0,1],[2,3,4]])
if __name__=="__main__": vpart("K6",6,K(6),[[0,1,2,3],[4,5]])
if __name__=="__main__": vpart("K6",6,K(6),[[0,1,2],[3,4,5]])
if __name__=="__main__": vpart("K33",6,K33,[[0,1,2],[3,4,5]])
if __name__=="__main__": vpart("K33",6,K33,[[0,1,3],[2,4,5]])
