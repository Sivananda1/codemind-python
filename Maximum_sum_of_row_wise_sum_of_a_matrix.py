n,m=map(int,input().split())
f=[]
s=0
for k in range(n):
    a=list(map(int,input().split()))
    f.append(a)
for i in range(len(f)):
    if s<sum(f[i]):
        s=sum(f[i])
print(s)