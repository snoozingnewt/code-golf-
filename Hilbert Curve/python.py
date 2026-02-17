C=' ╶╵└╴─┘ ╷┌│ ┐'
s='A';exec("s=s.translate({65:'+BF-AFA-FB+',66:'-AF+BFB+FA-'});"*5)
W=2<<5;g=[[0]*~-W for _ in' '*~-W];x=0;y=W-2;u=1;v=0
for c in s:
 if c>'E':d=(u>0)|4*(u<0)|2*(v<0)|8*(v>0);g[y][x]|=d;g[y+v][x+u]=d|d*4&15|d>>2;x+=u+u;y+=v+v;g[y][x]|=d*4&15|d>>2
 elif c<'.':u,v=[(-v,u),(v,-u)][c<',']
for r in g[::2]:print(''.join(C[c]for c in r).rstrip())
5<5!=print()
