import sys
for a in sys.argv[1:]:
 w=a.split();S={*w};r=[]
 while S:n=min(S-{b for a,b in zip(*[iter(w)]*2)if{a}&S});r+=n,;S-={n}
 print(*r)
