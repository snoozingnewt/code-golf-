import sys
for a in sys.argv[1:]:
 s=p=B=D=0;j=27
 for c in a:
  if" "<c:p=[ord(c)%59%48%34%11,10-p*(c<"X")][c in"X/"];s+=-~B*p;B,D=D+(c in"X/"*j),c in"X"*j
  j-=1
 print(s)
