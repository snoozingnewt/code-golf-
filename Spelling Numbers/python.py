import sys;w="zero one two three four five six s eight nine ten el twelve thirfourfifsixseighninetwenthirforfifsixseighnine".translate({1:"teen ",2:"ty ",3:"even"}).split()
for n in map(int,sys.argv[1:]):t=n%100;print([r:=t>19and w[t//10+18]+("-"+w[t%10])*(t%10>0)or w[t],w[n//100]+" hundred"+(" and "+r)*(t>0),"one thousand"][(n>99)+(n>999)])
