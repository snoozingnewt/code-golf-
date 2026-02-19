import sys;Z="Straight";K=" of a Kind"
for a in sys.argv[1:]:Y,X,*_,W=s=sorted((r:=ord(c)%16)-r//13for c in a);t=sum(map(s.count,s));S=t<6and(W-Y<5or X-Y>8);print(max(a)<chr(ord(min(a))|15)and[Z+" ","Royal "][X>9>Y]*S+"Flush"or("Pair","Full House",Z*S or"High Card","Three"+K,"Four"+K,"Two Pair")[-t%7])
