n=int(input())
x=n
s=n**2
t=10
f=0
while n:
    r=s%t
    if r==x:
        f=1
    n=n//10
    t=t*10
if f==1:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")