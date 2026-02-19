a=lambda i:f"{i or'no more'} bottle{'s'[:i^1]} of beer on the wall";z=99
while~z:c=a(z);print(f"{c.capitalize()}, {c[:-12]}.\n{z and'Take one down and pass it around'or'Go to the store and buy some more'}, {a(~-z%100)}.\n");z-=1
