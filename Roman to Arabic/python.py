import sys
for r in sys.argv[1:]:p=0;print(sum((v:=5**((q:='IVXLCDM'.find(c))%2)*10**(q//2))-2*v*(v<p)+(p:=v)*0for c in r[::-1]))
