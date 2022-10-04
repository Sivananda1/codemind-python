n=int(input())
s=0
while n:
    r=n%10
    s+=(r*r)
    n=n//10
    if s>9 and n==0:
        n=s
        s=0
if s==7 or s==1:
    print(True)
else:
    print(False)