z=range
print("  ",*z(2,8),'\n',13*"-")
for i in z(16):print("%X:"%i,*map(chr,z(32+i,127,16)),i//15*'DEL')
