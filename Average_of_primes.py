n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    f=0
    for j in range(2,i):
        if i%j==0:
            f=1
            break
    if f==0:
        s.append(i)
if l[0]==1:
    s.remove(1)
t=sum(s)
v=len(s)
print("{:.2f}".format(t/v))