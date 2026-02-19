import sys;w="zero one two three four five six s eight nine ten el twelve thirfourfifsixseighninetwenthirforfifsixseighnine".translate({1:'teen ',2:'ty ',3:'even'}).split()
for n in map(int,sys.argv[1:]):t=n%100;r=t>19and w[t//10+18]+("-"+w[t%10])*(t%10>0)or w[t];print("one thousand"*(n>999)or w[n//100]+" hundred"+(" and "+r)*(t>0)if n>99else r)
