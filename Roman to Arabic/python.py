import sys
for r in sys.argv[1:]:p=0;print(sum((v:=10**(-~q//2)>>q%2)-2*p*(p<(p:=v))for q in map('IVXLCDM'.find,r)))
