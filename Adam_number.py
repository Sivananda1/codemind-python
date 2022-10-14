n=input()
a=int(n)
aa=a*a
b=n[::-1]
c=int(b)
cc=c*c
ff=str(cc)
d=ff[::-1]
dd=int(d)
if aa==dd:
    print(True)
else:
    print(False)