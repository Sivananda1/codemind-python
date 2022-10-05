a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s=[]
t=[]
for i in l1:
    for j in l2:
        if i==j:
            s.append(j)
for k in range(len(s)):
    if s[k] not in t:
        t.append(s[k])
print(*t)
