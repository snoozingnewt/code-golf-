import sys,re
F=lambda p,d,z:p>-1!=a[p:p+1]>"."and(z,F(p+d,d,1))[a[p]>"O"]
for a in sys.argv[1:]:print(re.sub('\.',lambda m:".!"[any(F(m.start()+d,d,0)for d in(~9,~8,~7,~0,1,8,9,10))],a)+"\n")
