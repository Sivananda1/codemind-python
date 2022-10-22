n=int(input())
s=str(n)
t=len(s)
c=0
k=n
for i in range(t):
    r=n%10
    c+=(r**t)
    n=n//10
    t-=1
if c==k:
    print(True)
else:
    print(False)