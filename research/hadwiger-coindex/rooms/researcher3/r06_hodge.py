# Real discrete Hodge decomposition of B0_empty(G) with the copy-swap involution S.
# harmonic_k = ker L_k ; split by S-sign: dim of S-anti-invariant harmonic k-cochains.
import sys; sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3')
from r06_lib import *
import numpy as np
def cyc(n): return [(i,(i+1)%n) for i in range(n)]
def perm_sign(seq):
    s=list(seq); sg=1
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i]>s[j]: sg=-sg
    return sg
def hodge(adj,n,name):
    F=B0_empty(adj,n)
    ks=sorted(k for k in F if k>=0)
    idx={k:{f:i for i,f in enumerate(F[k])} for k in ks}
    # boundary matrices d_k : C_k -> C_{k-1}
    D={}
    for k in ks:
        if k-1 in idx:
            M=np.zeros((len(F[k-1]),len(F[k])))
            for j,f in enumerate(F[k]):
                for t in range(len(f)):
                    g=f[:t]+f[t+1:]
                    M[idx[k-1][g],j]=(-1)**t
            D[k]=M
    # swap operator on C_k (signed permutation matrix)
    def swap_mat(k):
        S=np.zeros((len(F[k]),len(F[k])))
        for j,f in enumerate(F[k]):
            img=[(v+n if v<n else v-n) for v in f]
            sg=perm_sign(img)
            tgt=tuple(sorted(img))
            S[idx[k][tgt],j]=sg
        return S
    out={}
    for k in ks:
        dk = D.get(k, np.zeros((0,len(F[k]))))
        dk1 = D.get(k+1, np.zeros((len(F[k]),0)))
        L = dk.T@dk + dk1@dk1.T
        S = swap_mat(k)
        # anti-invariant subspace: basis of ker(S+I)
        w,V = np.linalg.eigh((S+S.T)/2)  # S is orthogonal permutation-signed
        Pm = V[:, np.abs(w+1)<1e-9]      # anti-invariant basis (S v = -v)
        Pp = V[:, np.abs(w-1)<1e-9]
        def hdim(P):
            if P.shape[1]==0: return 0
            M=P.T@L@P
            ev=np.linalg.eigvalsh(M)
            return int(np.sum(np.abs(ev)<1e-8))
        out[k]=(hdim(Pp), hdim(Pm))
    return out
if __name__=="__main__":
    G = {
     "K2":(2,[(0,1)]),
     "K3":(3,list(itertools.combinations(range(3),2))),
     "K4":(4,list(itertools.combinations(range(4),2))),
     "K5":(5,list(itertools.combinations(range(5),2))),
     "C5":(5,cyc(5)),
     "C6":(6,cyc(6)),
    }
    for name,(n,E) in G.items():
        o=hodge(make(n,E),n,name)
        print(name, "k: (inv harmonic, anti harmonic)=", {k:v for k,v in o.items() if v!=(0,0)}, flush=True)
