import sys
for a in sys.argv[1:]:d,b=map(int,a.split());B=b**d;print((~-B**b//~-B)**d//B**(d//2*~-b)%B)
