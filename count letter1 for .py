a=input('enter a:')
l=len(a)
b=""
for i in range(l):
    d=ord(a[i])
    r=d+32 if(d>=65 and d<=90) else d-32
    f=chr(r)
    print(f,end='')
    