from common import *
G=gstar()
choice={1:{'x','y','c','q1','q3'},2:{'x','z','c','q4'},3:{'z','c','p','q2','q4'},4:{'x','c','p','q5'},
        5:{'x','z','c','q4'},6:{'y','c','p','q1','q3'}}
outer={1:('a','b','c'),2:('b','d','a'),3:('c','d','a'),4:('b','c','d'),5:('a','c',(1,'q1')),6:('d','a',(3,'q5'))}
S={'a','b'}
for t,s in choice.items():
    m={'x':outer[t][0],'y':outer[t][1],'z':outer[t][2]}
    for v in s: S.add(m.get(v,(t,v)))
# consistency: outer statuses must match what the choices say
for t,s in choice.items():
    for k,v in zip('xyz',outer[t]): assert (k in s)==(v in S),(t,k,v)
T=set(G)-S
H=G.subgraph(S)
print('T bipartite',nx.is_bipartite(G.subgraph(T)),'|S|',len(S),'|T|',len(T))
for cc in nx.connected_components(H):
    C=H.subgraph(cc); print(' S comp',len(cc),'edges',C.number_of_edges(), 'cycles',[sorted(map(str,c)) for c in nx.cycle_basis(C)])
# list-colour check for random-free sanity: 2-SAT-type argument holds; also test specific M that blocks FB-type reasoning
