import sys,itertools as I
for a in sys.argv[1:]:print(*map(''.join,I.zip_longest(*a.split(),fillvalue='')))
