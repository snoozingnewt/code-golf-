import sys,re
for s in sys.argv[1:]:print(''.join(chr(b'A@CFILOSV'[int(b)]+len(a))for a,b in re.findall(r'((\d)\2*)',s)))