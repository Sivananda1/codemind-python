n=int(input())
s=1
t=0
while n>0:
    r=n%10
    n=n//10
    s=(s*r)
    t+=r
print(s-t)