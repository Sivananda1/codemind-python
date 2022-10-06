n=int(input())
l=list(map(int,input().split()))
s=[]
t=0
for i in range(len(l)):
    if l[i] not in s:
        s.append(l[i])
for j in s:
    if j%2==1:
        t+=j
print(t)
        