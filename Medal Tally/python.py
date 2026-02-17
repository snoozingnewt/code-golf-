import sys
for l in sys.argv[1:]:
 l=l.split();g=p=0;m=[0]*3
 for x in l:
  if(p:=p+m[p]*(g!=x))>2:break
  m[p]+=1;g=x
 print('1💎 '*(l.count(l[0])<2)+f'{m[0]}🥇'+f' {m[1]}🥈'*(m[1]>0)+f' {m[2]}🥉'*(m[2]>0))