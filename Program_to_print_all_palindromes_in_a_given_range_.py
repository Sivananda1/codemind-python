def pal(n):
    s=n
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    if s==rev:
        return True
n1=int(input())
n2=int(input())
s=[]
for i in range(n1,n2+1):
    if pal(i):
        s.append(i)
print(*s)        