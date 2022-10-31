def fun(n):
    s=0
    while n:
        r=n%10
        s+=1
        n=n//10
    return s
n=int(input())
l=list(map(int,input().split()))
t=min(l)
v=fun(t)
w=0
for i in l:
    r=fun(i)
    if r==v:
        w+=1
print(w)