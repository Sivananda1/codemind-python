n,m=map(int,input().split())
f=[]
s=0
d=[]
for _ in range(n):
    a=list(map(int,input().split()))
    f.append(a)
for i in range(m):
    for j in range(n):
        s+=f[j][i]
    d.append(s)
    s=0
print(max(d))