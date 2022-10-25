n=int(input())
l=list(map(int,input().split()))
s=[]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
for i in l1:
    s.append(i)
    s.append(l.count(i))
print(*s)