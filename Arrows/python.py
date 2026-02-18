import sys
x=y=0
for i in sys.argv[1:]:d=b'( "* (!&)$%%"*( '[ord(i)%50%36%22];x+=d//4-9;y+=d%4-1;print(x,y)
