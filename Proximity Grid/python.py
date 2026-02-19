import sys
for A in sys.argv[1:]:
 *G,=A.replace(*' \n')+'\n'*10;Q=[(i,0)for i in range(99)if'0'==G[i]]
 for i,v in Q:
  if v<1or'-'==G[i]:G[i]=chr(v+48+7*(v>9)+6*(v>35));Q+=[(i+d,v+1)for d in(~9,~0,1,10)]
 print(*G[:-9],sep='')
