import sys
for a in sys.argv[1:]:
 adj={};d={};S=set()
 for l in a.split('\n'):
  u,v=map(int,l.split())
  S|={u,v}
  adj.setdefault(u,[]).append(v)
  d[v]=d.get(v,0)+1
 r=[]
 q=[n for n in S if d.get(n,0)==0]
 while q:
  n=q.pop(0)
  r+=n,
  for v in adj.get(n,[]):
   d[v]-=1
   if d[v]<1:q+=v,
 print(*r)
