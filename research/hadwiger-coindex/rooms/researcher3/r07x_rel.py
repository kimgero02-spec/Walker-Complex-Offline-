import sys; sys.path.insert(0,'/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3')
from r07x_B import *
def rel_betti(F,U,p=10007):
    Uset={k:set(v) for k,v in U.items()}
    Q={k:[f for f in v if f not in Uset.get(k,set())] for k,v in F.items()}
    Q={k:v for k,v in Q.items() if v}
    # relative chain complex: C_k = span(Q_k); boundary drops faces in U (they are zero).
    dims=sorted(Q)
    idx={k:{f:i for i,f in enumerate(Q[k])} for k in dims}
    ranks={}
    for k in dims:
        if k-1 not in idx: ranks[k]=0; continue
        rows=[]
        for f in Q[k]:
            row={}
            for j in range(len(f)):
                g=f[:j]+f[j+1:]
                if g in idx[k-1]: row[idx[k-1][g]]=(-1)**j
            rows.append(row)
        ranks[k]=rank_mod_p(rows,len(Q[k-1]),p)
    return {k:len(Q[k])-ranks[k]-ranks.get(k+1,0) for k in dims if len(Q[k])-ranks[k]-ranks.get(k+1,0)}
if __name__=="__main__":
  for name,n,E,parts in [("K5",5,K(5),[[0,1,2,3],[4]]),("K5",5,K(5),[[0,1],[2,3,4]]),
     ("K6",6,K(6),[[0,1,2,3],[4,5]]),("K6",6,K(6),[[0,1,2],[3,4,5]]),
     ("K33",6,K33,[[0,1,2],[3,4,5]]),("K33",6,K33,[[0,1,3],[2,4,5]])]:
    adj=make(n,E); F=B0_empty(adj,n)
    U=union([faces_restrict(F,n,S) for S in parts])
    print(name,parts,"relative H (X, union of blocks):",rel_betti(F,U),flush=True)
