n=int(input())
a=0
b=1
c=a+b
s=[]
t=[]
v=[]
while c<n:
    c=a+b
    s.append(c)
    if c>n:
        s.append(c)
        break
    else:
        a=b
        b=c
for i in s:
    if i<n:
        t.append(i)
    else:
        v.append(i)
r1=t[-1]
r2=v[0]
p1=n-r1
p2=r2-n
if p1<p2:
    print(r1)
elif p1==p2:
    print(r1,r2,end=' ')
else:
    print(r2)