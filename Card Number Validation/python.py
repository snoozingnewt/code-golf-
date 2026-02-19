import sys
for n in sys.argv[1:]:j=0;sum([d:=int(c),d*2%9or d][j:=~j]for c in n if'/'<c)%10or print(n)
