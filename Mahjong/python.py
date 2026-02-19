import sys
def f(C,p=0):
 if max(C)<1:return p
 i=C.index(max(C))
 for d in(i,)*3,(i,i+1,i+2),(i,i):
  D=C[:];q=len(d)<3
  for j in d:D[j]-=1
  if min(D)>=0and(d[1]==i or i>6and(i-7)%9<7)and(q<1or p<1)and f(D,p+q):return 1
for a in sys.argv[1:]:
 A=[ord(c)%62for c in a];C=[0]*36
 for c in A:C[c]+=1
 if f(C)or{*C}=={0,2}or{*A}=={*range(8),15,16,24,25,33}:print(a)
