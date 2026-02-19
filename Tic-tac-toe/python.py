import sys
for g in sys.argv[1:]:print(max('-XO',key=lambda p:p*3in' '.join([g,g[::4],g[1::4],g[2::4],g[::5],g[2::3]])))
