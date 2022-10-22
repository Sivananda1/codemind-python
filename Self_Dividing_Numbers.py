def fun(x):
    s=x
    while x:
        r=x%10
        x=x//10
        if r==0 or s%r!=0:
            return False
    return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    if fun(i):
        print(i,end=' ')