# R10 researcher1: strand coefficients m_I, m_tau for pieces with private vertices.
from r10_channels import piece_n, P
def m_coeffs(q, E, priv, jx, jy):
    n = piece_n(q, E, priv, jx, jy); g = lambda s: n[P(s)]
    mI = g('0 2|1 3') - g('0 2|1|3') - g('0|1 3|2') + g('0|1|2|3')
    mT = g('0 3|1 2') - g('0 3|1|2') - g('0|1 2|3') + g('0|1|2|3')
    return mI, mT
X = ('a','b'); Y = ('c','d')   # x1=a,x2=b,y1=c,y2=d ; straight boundary order a,b,d,c
pieces = {
 'square+centre (planar, straight)': ([('a','c'),('c','d'),('d','b'),('b','a')]+[('o',v) for v in 'abcd'], ['o']),
 'square+centre, no junction edges': ([('a','c'),('d','b')]+[('o',v) for v in 'abcd'], ['o']),
 'two private o,p: a-o-c, b-p-d, o-p': ([('a','o'),('o','c'),('b','p'),('p','d'),('o','p')], ['o','p']),
 'K_{2,2} a,b | c,d (one-sided swap)': ([('a','c'),('a','d'),('b','c'),('b','d')], []),
 'nonplanar-ish: o adj all + a-d, b-c': ([('o',v) for v in 'abcd']+[('a','d'),('b','c'),('a','c'),('b','d')], ['o']),
}
for name,(E,pr) in pieces.items():
    print(name, [(q,)+m_coeffs(q,E,pr,X,Y) for q in (4,5,6,7)])
