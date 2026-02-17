C=' ╶╵└╴─┘ ╷┌│ ┐'
s='A';exec("s=s.translate({65:'+BF-AFA-FB+',66:'-AF+BFB+FA-'});"*5)
g=[[0]*63for _ in' '*63];x=v=0;u=1;y=62
for c in s:
 if c>'E':d=1<<v*v-u-~v;e=d*4%15;g[y][x]|=d;g[y+v][x+u]=d|e;x+=u+u;y+=v+v;g[y][x]|=e
 elif c<'.':k=ord(c)%4-2;u,v=v*k,-u*k
for r in g[::2]:print(''.join(C[c]for c in r).rstrip())