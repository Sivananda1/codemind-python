n=int(input())
l=list(map(int,input().split()))
m=int(input())
s=[]
t=[]
for i in l:
    f=0
    for j in range(2,i):
        if i%j==0:
            f=1
    if f==0:
        s.append(i)
if s[0]==1:
    s.remove(1)
for k in s:
    if m>=k:
        t.append(k)
print(len(t))