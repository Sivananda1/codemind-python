n=int(input())
l=list(map(int,input().split()))
#print(l)
a=[]
b=[]
for i in range(len(l)):
    if i%2:
        a.append(l[i])
    else:
        b.append(l[i])
t=[]
for j in range(len(b)):
    for k in range(0,a[j]):
        t.append(b[j])
print(*t)