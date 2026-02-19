import sys
for s in sys.argv[1:]:b=0;d=sum((b:=b+1)*int(c)for c in s if'-'<c)%11;print(s+f'X{d}'[d<10])
