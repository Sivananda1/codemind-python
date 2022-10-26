n=int(input())
l=list(map(int,input().split()))
s=0
if n%2==1:
    s=l[n//2]
    l.remove(l[(n//2)])
    k=[]
    x=len(l)-1
    for i in range(len(l)//2):
        k.append(l[i])
        k.append(l[x])
        x-=1
    k.append(s)
    k.append(0)
    print(*k)
else:
    k=[]
    x=len(l)-1
    for i in range(len(l)//2):
        k.append(l[i])
        k.append(l[x])
        x-=1
    print(*k)