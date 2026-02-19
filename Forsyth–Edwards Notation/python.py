import sys
for a in sys.argv[1:]:print(''.join(chr(9812+"KQRBNPkqrbnp".find(c))*(c>"9")or" "*(ord(c)-48)or"\n"for c in a.split()[0]+"/"))
