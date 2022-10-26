n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    l=list(map(int,input().split()))
    l1=l[x-y:]
    l=l1+l
    l2=[]
    for i in range(x):
        l2.append(l[i])
    print(*l2)