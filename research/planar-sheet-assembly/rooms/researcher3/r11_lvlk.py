# R11: level-k chain; objects: u-copies + tag partition; lower objects merge one tag pair, upper merge pairs below
import sys,os,itertools; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from r09_check import *
def run(k):
    lower=['D3']+[f'X{i}' for i in range(1,k)]+['Z']
    nu={'D2':2,'D3':3,'Z':1,**{f'X{i}':2 for i in range(1,k)}}
    up={'D1':['D3','X1']}
    for i in range(1,k-1): up[f'Y{i}']=[f'X{i}',f'X{i+1}']
    up[f'Y{k-1}']=[f'X{k-1}','Z']
    for y in up: nu[y]=2
    tags=[(f'a{l}',f'b{l}') for l in lower]
    def blocks(o):
        merged=[l for l in lower if l==o] if o in lower else (up[o] if o in up else [])
        B=[]
        for l,(x,y) in zip(lower,tags):
            B+= [{x,y}] if l in merged else [{x},{y}]
        return B
    obj={o:[({'u'},set())]*nu[o]+[(b,set()) for b in blocks(o)] for o in nu}
    def mk(a,b,um):
        S,T=obj[a],obj[b]; f=list(um)
        for P in S[nu[a]:]: f.append(next(j for j in range(nu[b],len(T)) if P[0]<=T[j][0]))
        return (a,b,tuple(f))
    M={'tau':mk('D2','D3',(0,1)),'sig':mk('D3','D1',(0,0,1)),'t':mk('D2','Z',(0,0)),'s':mk('Z',f'Y{k-1}',(0,))}
    for i in range(1,k):
        M[f'p{i}']=mk('D2',f'X{i}',(0,0)); M[f'h{i}']=mk(f'X{i}',f'Y{i}',(0,1))
        M[f'q{i}']=mk(f'X{i}','D1' if i==1 else f'Y{i-1}',(0,1))
    C=lambda g,f:(M[f][0],M[g][1],tuple(M[g][2][j] for j in M[f][2]))
    sq=[('sig','tau','q1','p1')]+[(f'h{i}',f'p{i}',f'q{i+1}',f'p{i+1}') for i in range(1,k-1)]+[(f'h{k-1}',f'p{k-1}','s','t')]
    for a,b,c,d in sq: assert C(a,b)==C(c,d); M['c_'+a+b]=C(a,b)
    Ls={n:L(obj[a],obj[b],f)[2] for n,(a,b,f) in M.items()}
    cmp=lambda F,G:{x:F[G[x]] for x in G}
    names=list(M); cnt=0
    for ch in itertools.product(*[range(len(Ls[n])) for n in names]):
        c=dict(zip(names,[Ls[n][i] for n,i in zip(names,ch)]))
        if all(cmp(c[a],c[b])==c['c_'+a+b] and cmp(c[cc],c[d])==c['c_'+a+b] for a,b,cc,d in sq): cnt+=1
    # omega: for each composite, does some factorization force white and another force copy?
    om=[]
    for a,b,cc,d in sq:
        I1={cmp(G,F)[('w','u')][0] for F in Ls[b] for G in Ls[a]}; I2={cmp(G,F)[('w','u')][0] for F in Ls[d] for G in Ls[cc]}
        om.append((I1,I2))
    print('k=',k,'functorial choices:',cnt,' factorization images (w=white,c=copy):',om)
for k in (2,3,4): run(k)
