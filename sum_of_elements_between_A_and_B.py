n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=[]
for i in range(len(l)):
    if a<=l[i] and b>=l[i]:
        s.append(l[i])
print(sum(s))