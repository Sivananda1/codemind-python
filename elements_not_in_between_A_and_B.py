n=int(input())
s=[]
l=list(map(int,input().split()))
a,b=map(int,input().split())
for i in range(len(l)):
    if l[i]<a or l[i]>b:
        s.append(l[i])
if len(s)==0:
    print(-1)
else:
    print(*s)