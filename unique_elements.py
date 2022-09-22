n=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(len(l)):
    if l[i] not in c:
        c.append(l[i])
print(*c)