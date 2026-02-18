N=3321;B=10**1000;C=B<<N;s=k=0
while B:C=B-C;s-=C//(k-~k)**2;B=B*(k-N)//-~k;k+=1
print(f"0.{s>>N}")
