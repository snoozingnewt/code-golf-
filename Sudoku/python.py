import sys;R=range;p=print
b=[*map(list,sys.argv[1:])]
def s():
 for q in R(81):
  if(w:=b[q//9])[c:=q%9]>'9':
   for n in{*'123456789'}-{*w}-{z[c]for z in b}-{b[q//27*3+i//3][c-c%3+i%3]for i in R(9)}:w[c]=n;s()
   w[c]='_';return
 for i in R(10):a,h,c,d,e,*_=[chr(9436+c)for c in b"3%SW7D$`fLG%coO;%[_?"[(877972>>i*2&3)*5:]];p(a+d.join([c.join([h*3]*3)]*3)+e);p('┃'+' %s │ %s │ %s ┃'*3%(*b[i],))
s()
