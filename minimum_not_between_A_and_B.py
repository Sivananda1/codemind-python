n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=[]
for i in range(len(l)):
    if a>l[i] or b<l[i]:
        s.append(l[i])
if len(s)==0:
    print(-1)
else:
    print(min(s))