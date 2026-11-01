from descent import *
th=(0,2,-2)   # f=t^3-4t ; E: y^2=x^3-16x ~ y^2=x^3-x
print("S",primes_S(th))
for v in [0,2,3,5]:
    S,r=kummer_image(th,v)
    cands=local_candidates(th,v)
    ker=[d for d in cands if isotropic_class(th,d,v)]
    # kernel cut: classes
    kercls={clsvec(d,v) for d in ker}; allcls={clsvec(d,v) for d in cands}
    print(v,"img dim",r,"|img|",len(S),"|H1|",len(allcls),"|ker|",len(kercls),"img in ker:",S<=kercls)
