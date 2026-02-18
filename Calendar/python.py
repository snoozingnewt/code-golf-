import calendar as c
for a in c.sys.argv[1:]:print(c.month(int(a[3:]),int(a[:2])).split('\n',1)[1])
