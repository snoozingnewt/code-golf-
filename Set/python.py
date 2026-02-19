import itertools as I,sys
for a in sys.argv[1:]:c=a.split();[all(len({*p})%2for p in zip(*t))and print(*t)for t in I.combinations(c,3)]
