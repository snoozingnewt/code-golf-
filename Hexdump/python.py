import sys
for s in sys.argv[1:]:
 i=0
 while c:=s[i:i+16]:print(f'{i:08x}: {c.encode().hex(" ",-2):40}',c.replace(*'\n.'));i+=16
 print()
