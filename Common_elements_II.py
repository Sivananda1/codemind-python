a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s=[]
t=[]
for i in l1:
    s.append(i)
for j in l2:
    s.append(j)
for k in range(len(s)):
    if s.count(s[k])==1:
        t.append(s[k])
print(*t)