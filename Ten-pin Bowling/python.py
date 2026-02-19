import sys
for a in sys.argv[1:]:
 s=p=0;j=27;B=D=1
 for c in a:
  if c>" ":p=10-p*(c<"X")if c in"X/"else(ord(c)-48)%59*c.isdigit();s+=B*p;B,D=D+(c in"X/"*j),1+(c in"X"*j)
  j-=1
 print(s)
