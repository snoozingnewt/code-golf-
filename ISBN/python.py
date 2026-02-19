import sys
for s in sys.argv[1:]:b=0;print(s+'0123456789X'[sum((b:=b+1)*int(c)for c in s if'-'<c)%11])
