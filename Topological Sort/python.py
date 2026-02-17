import sys
for a in sys.argv[1:]:
 w=a.split();S={*w};r=[]
 while S:n=(S-{*w[1::2]}).pop();r+=n,;S-={n};w=[x for i,x in enumerate(w)if w[i&-2]!=n]
 print(*r)