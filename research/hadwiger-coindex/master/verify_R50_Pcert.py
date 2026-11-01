import sys
sys.argv=['x']
exec(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'verify_R49_conjK.py')).read().split("H=nx.read_edgelist")[0])
choice={1:{'x','y','c','q1','q3'},2:{'x','z','c','q4'},3:{'z','c','p','q2','q4'},4:{'x','c','p','q5'},5:{'x','z','c','q4'},6:{'y','c','p','q1','q3'}}
outer={1:('a','b','c'),2:('b','d','a'),3:('c','d','a'),4:('b','c','d'),5:('a','c','q1#1'),6:('d','a','q5#3')}
S={'a','b'}
for t,s in choice.items():
    m={'x':outer[t][0],'y':outer[t][1],'z':outer[t][2]}
    for v in s: S.add(m.get(v,v+f'#{t}'))
for t,s in choice.items():
    for k,v in zip('xyz',outer[t]): assert (k in s)==(v in S),(t,k,v)
T=set(G)-S
print('T bipartite',nx.is_bipartite(G.subgraph(T)),len(S),len(T))
ok=True
for cc in nx.connected_components(G.subgraph(S)):
    C=G.subgraph(cc); cyc=C.number_of_edges()-C.number_of_nodes()+1
    good = cyc==0 or (cyc==1 and all(len(c)%2==0 for c in nx.cycle_basis(C)))
    ok&=good; print(' comp',len(cc),'cyclomatic',cyc,[len(c) for c in nx.cycle_basis(C)],good)
print('S components all 2-choosable (tree or unicyclic even):',ok)
