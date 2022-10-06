n=int(input())
l=list(map(int,input().split()))
s=[]
m=int(input())
for i in range(len(l)):
    if m>=l[i]:
        s.append(l[i])
print(sum(s))