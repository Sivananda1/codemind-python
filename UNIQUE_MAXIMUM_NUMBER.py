n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(len(l)):
    if l.count(l[i])==1 and s<l[i]:
        s=l[i]
if s==0:
    print(-1)
else:
    print(s)