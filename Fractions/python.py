import fractions as f
for i in f.sys.argv[1:]:print('%d/%d'%f.Fraction(i).__reduce__()[1])
