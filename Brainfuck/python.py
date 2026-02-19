import sys
for s in sys.argv[1:]:
 d=j=0;P='';a=[0]*9**5
 for c in s:d-=c>'[';P+=' '*d+"while a[j]:||||a[j]+=1||a[j]-=1|print(end=chr(a[j]))|j-=1||j+=1".split("|")[ord(c)%13]+"\n";d+=c=='['
 exec(P)
