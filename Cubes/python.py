R=range;s,v,d,c=' │╱█'
for z in R(1,8):W=s*z;H,P=c+'─'*z*4+c,v+W*4+v+W;T,B=zip(*[(W[i:]+d+W*4+d+s*i+v,P[:~i]+d)for i in R(z)]);*map(print,[s+W+H,*T,H+W+v,*[P+v]*~-z,P+c,*B,H,'']),
