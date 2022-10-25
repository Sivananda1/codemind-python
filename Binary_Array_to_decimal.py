n=int(input())
l=list(map(int,input().split()))
r=len(l)
s=0
for i in range(r):
    r-=1
    s+=(l[i]*2**r)
print(s)